from PySide6.QtWidgets import QCheckBox

from questions import Q10

eeprom_latency = [x * 10 ** 6 for x in [25, 50, 75, 100, 125, 150, 175, 200]]
pll_mul = [1]
hsi_div = [2 ** x for x in range(9)]
clk_div = [2 ** x for x in range(9)]

settings = {
    "freq_unit": {
        "Гц": 1,
        "кГц": 10 ** 3,
        "МГц": 10 ** 6,
        "ГГц": 10 ** 9
    },
}


class Q11(Q10):

    def __init__(self):
        super().__init__()
        self.__11_fill_combo_boxes()
        self.__11_connect_signals()

    def __11_fill_combo_boxes(self):
        for _ in settings["freq_unit"]:
            self.ui.comboBox_11_nhse.addItem(_)
            self.ui.comboBox_11_freq_unit.addItem(_)
        self.ui.lineEdit_11_nhse.setText("8")
        self.ui.comboBox_11_nhse.setCurrentText("МГц")

    def __11_connect_signals(self):
        self.ui.checkBox_11_nhse.stateChanged.connect(self.__11_unlock_options)
        self.ui.checkBox_11_freq.stateChanged.connect(self.__11_unlock_options)
        self.ui.checkBox_11_main.stateChanged.connect(self.__11_unlock_options)
        self.ui.submitButton_11.clicked.connect(self.__11_submit_handler)

    def __11_unlock_options(self):
        sender: QCheckBox = self.sender()
        option = sender.objectName().split('_')[-1]
        checked = sender.isChecked()

        if option == 'nhse':
            self.ui.comboBox_11_nhse.setEnabled(checked)
            self.ui.lineEdit_11_nhse.setEnabled(checked)
        elif option == 'freq':
            self.ui.comboBox_11_freq_unit.setEnabled(checked)
            self.ui.lineEdit_11_freq.setEnabled(checked)
            if checked:
                self.ui.checkBox_11_main.setChecked(False)
        elif option == 'main':
            self.ui.lineEdit_11_denum.setEnabled(checked)
            # self.ui.lineEdit_11_num.setEnabled(checked)
            if checked:
                self.ui.checkBox_11_freq.setChecked(False)

    def __11_submit_handler(self):
        main = self.ui.checkBox_11_main.isChecked()
        freq = self.ui.checkBox_11_freq.isChecked()
        hse_freq = int(self.ui.lineEdit_11_nhse.text()) * settings["freq_unit"][self.ui.comboBox_11_nhse.currentText()]

        if not main and not freq:
            return

        denum = None
        div_hci = None
        div_adc = None

        if main:
            denum = int(self.ui.lineEdit_11_denum.text())
            for div1 in hsi_div[::-1]:
                for div2 in clk_div:
                    if int(denum / div1) == div2:
                        div_hci = div1
                        div_adc = div2
                        break
                if div_hci:
                    break
        elif freq:
            freq = int(self.ui.lineEdit_11_freq.text()) * settings[
                "freq_unit"][self.ui.comboBox_11_freq_unit.currentText()]
            for div1 in hsi_div[::-1]:
                for div2 in clk_div:
                    a = (freq * div1 * div2 / hse_freq)
                    if int(a) == a:
                        if a != 1:
                            continue
                        div_hci = div1
                        div_adc = div2
                        break
                if div_hci:
                    break

            if div_hci is None:
                return

        func = self.__11_create_func_code(div_hci, div_adc)
        reg = self.__11_create_reg_code(div_hci, div_adc)

        self.show_code(with_func=func, with_reg=reg)

    def __11_create_func_code(self, div_hci: int, div_adc: int) -> str:

        code = (f"RST_CLK_HSIclkPrescaler(RST_CLK_HSIclkDIV{div_hci}); // fHSI_C1 = fHSI / {div_hci}\n"
                "// Второй мультиплексор\n"
                f"// Более подробно на [c. 7-8] Модуль_тактовой_частоты_MDR.pdf\n\n"
                "RST_CLK_ADCclkSelection(RST_CLK_ADCclkHSI_C1); // ADC_C2 = HSI_C1\n"
                f"RST_CLK_ADCclkPrescaler(RST_CLK_ADCclkDIV{div_adc}); // N = {div_adc}, fHSI_C3 = fHSI_С2 / {div_adc}\n"
                "RST_CLK_ADCclkEnable(ENABLE);\n")

        return code

    def __11_create_reg_code(self, div_hci: int, div_adc: int) -> str:
        adc_c3_sel = dict(zip(clk_div[1:], range(8, 16)))
        adc_c3_sel[1] = 0

        adc_mco_clk = 0
        adc_mco_clk |= (1 << 13)
        adc_mco_clk |= (adc_c3_sel[div_adc] << 8)
        adc_mco_clk |= 0b11 << 4

        rtc_clock = 0
        rtc_clock |= adc_c3_sel[div_hci] << 4

        code = (
            f"//MDR_RST_CLK->RTC_CLOCK &= ~0xF0; // Сброс разрядов HSI_C1_SEL\n"
            f"// Более подробно на [c. 174] Спецификации\n\n"
            f"MDR_RST_CLK->RTC_CLOCK |= {hex(rtc_clock)}; // HSI_C1_SEL = {bin(adc_c3_sel[div_hci])}, fHSI_C1 = fHSI / {div_hci}\n"
            f"// {hex(adc_mco_clk)} = {bin(adc_mco_clk)}, ADC_C2 = HSI_C1, ADC_C3 = ADC_C2/{div_adc}\n"
            f"// Более подробно на [c. 173] Спецификации\n\n"
            f"MDR_RST_CLK->ADC_MCO_CLOCK = {hex(adc_mco_clk)}; // ADCCLKEN = 1\n")

        return code
