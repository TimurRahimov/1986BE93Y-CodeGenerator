from PySide6.QtWidgets import QCheckBox

from questions import Q9

eeprom_latency = [x * 10 ** 6 for x in [25, 50, 75, 100, 125, 150, 175, 200]]
pll_mul = [1]
clk_div = [2 ** x for x in range(9)]

settings = {
    "freq_unit": {
        "Гц": 1,
        "кГц": 10 ** 3,
        "МГц": 10 ** 6,
        "ГГц": 10 ** 9
    },
}


class Q10(Q9):

    def __init__(self):
        super().__init__()
        self.__10_fill_combo_boxes()
        self.__10_connect_signals()

    def __10_fill_combo_boxes(self):
        for _ in settings["freq_unit"]:
            self.ui.comboBox_10_nhse.addItem(_)
            self.ui.comboBox_10_freq_unit.addItem(_)
        self.ui.lineEdit_10_nhse.setText("48")
        self.ui.comboBox_10_nhse.setCurrentText("МГц")

    def __10_connect_signals(self):
        self.ui.checkBox_10_nhse.stateChanged.connect(self.__10_unlock_options)
        self.ui.checkBox_10_freq.stateChanged.connect(self.__10_unlock_options)
        self.ui.checkBox_10_main.stateChanged.connect(self.__10_unlock_options)
        self.ui.submitButton_10.clicked.connect(self.__10_submit_handler)

    def __10_unlock_options(self):
        sender: QCheckBox = self.sender()
        option = sender.objectName().split('_')[-1]
        checked = sender.isChecked()

        if option == 'nhse':
            self.ui.comboBox_10_nhse.setEnabled(checked)
            self.ui.lineEdit_10_nhse.setEnabled(checked)
        elif option == 'freq':
            self.ui.comboBox_10_freq_unit.setEnabled(checked)
            self.ui.lineEdit_10_freq.setEnabled(checked)
            if checked:
                self.ui.checkBox_10_main.setChecked(False)
        elif option == 'main':
            self.ui.lineEdit_10_denum.setEnabled(checked)
            # self.ui.lineEdit_10_num.setEnabled(checked)
            if checked:
                self.ui.checkBox_10_freq.setChecked(False)

    def __10_submit_handler(self):
        main = self.ui.checkBox_10_main.isChecked()
        freq = self.ui.checkBox_10_freq.isChecked()
        hse_freq = int(self.ui.lineEdit_10_nhse.text()) * settings["freq_unit"][self.ui.comboBox_10_nhse.currentText()]

        if not main and not freq:
            return

        denum = None

        if main:
            denum = int(self.ui.lineEdit_10_denum.text())
            if denum not in clk_div:
                return
        elif freq:
            freq = int(self.ui.lineEdit_10_freq.text()) * settings[
                "freq_unit"][self.ui.comboBox_10_freq_unit.currentText()]
            for div in clk_div:
                a = (freq * div / hse_freq)
                if int(a) == a:
                    if a != 1:
                        continue
                    denum = div
                    break
            if denum is None:
                return

        func = self.__10_create_func_code(denum)
        reg = self.__10_create_reg_code(denum)

        self.show_code(with_func=func, with_reg=reg)

    def __10_create_func_code(self, denum: int) -> str:

        code = (f"// Первый и второй мультиплексоры\n"
                f"// Более подробно на [c. 7-8] Модуль_тактовой_частоты_MDR.pdf\n\n"
                "RST_CLK_ADCclkSelection(RST_CLK_ADCclkUSB_C1); // ADC_C2 = ADC_C1 = USB_C1\n"
                f"RST_CLK_ADCclkPrescaler(RST_CLK_ADCclkDIV{denum}); // N = {denum}\n"
                "RST_CLK_ADCclkEnable(ENABLE);\n")

        return code

    def __10_create_reg_code(self, denum: int) -> str:
        adc_c3_sel = dict(zip(clk_div[1:], range(8, 16)))
        adc_c3_sel[1] = 0

        adc_mco_clk = 0
        adc_mco_clk |= (1 << 13)
        adc_mco_clk |= (adc_c3_sel[denum] << 8)
        adc_mco_clk |= 0b10 << 4
        adc_mco_clk |= 1

        code = (
            f"// {hex(adc_mco_clk)} = {bin(adc_mco_clk)}, ADC_C1 = USB_C1, ADC_C2 = ADC_C1, ADC_C3 = ADC_C2/{denum}\n"
            f"// Более подробно на [c. 173] Спецификации\n\n"
            f"MDR_RST_CLK->ADC_MCO_CLOCK = {hex(adc_mco_clk)}; // ADCCLKEN = 1\n")

        return code
