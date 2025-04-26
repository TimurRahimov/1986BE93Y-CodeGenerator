import enum

from PySide6.QtWidgets import QCheckBox

from questions import Q9

eeprom_latency = [x * 10 ** 6 for x in [25, 50, 75, 100, 125, 150, 175, 200]]
pll_mul = [1]
clk_div = [2 ** x for x in range(10)]


class Source(enum.Enum):
    HSI = "HSI"
    LSI = "LSI"
    HSE = "HSE"
    LSE = "LSE"
    USB = "USB"


settings = {
    "freq_unit": {
        "Гц": 1,
        "кГц": 10 ** 3,
        "МГц": 10 ** 6,
        "ГГц": 10 ** 9
    },
    "source": [
        Source.HSE.value,
        Source.LSE.value,
        Source.LSI.value,
        Source.USB.value,
    ]
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
        for _ in settings["source"]:
            self.ui.comboBox_10_source.addItem(_)
        self.ui.lineEdit_10_nhse.setText("48")
        self.ui.comboBox_10_nhse.setCurrentText("МГц")
        self.ui.lineEdit_10_num.setText("1")
        self.ui.comboBox_10_source.setCurrentText(settings["source"][0])

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
            self.ui.lineEdit_10_num.setEnabled(checked)
            if checked:
                self.ui.checkBox_10_freq.setChecked(False)

    def __10_submit_handler(self):
        b_main = self.ui.checkBox_10_main.isChecked()
        b_freq = self.ui.checkBox_10_freq.isChecked()
        source = Source(self.ui.comboBox_10_source.currentText().upper())
        freq = int(self.ui.lineEdit_10_nhse.text()) * settings["freq_unit"][self.ui.comboBox_10_nhse.currentText()]

        if not b_main and not b_freq:
            return

        num = None
        denum = None

        if b_main:
            num = int(self.ui.lineEdit_10_num.text())
            denum = int(self.ui.lineEdit_10_denum.text())
            if denum not in clk_div:
                return
        elif b_freq:
            b_freq = int(self.ui.lineEdit_10_freq.text()) * settings[
                "freq_unit"][self.ui.comboBox_10_freq_unit.currentText()]
            for div in clk_div:
                a = (b_freq * div / freq)
                if int(a) == a:
                    if a != 1:
                        num = int(a)
                        continue
                    denum = div
                    break
            if denum is None:
                return

        func = self.__10_create_func_code(source, num, denum, freq)
        reg = self.__10_create_reg_code(source, num, denum)

        self.show_code(with_func=func, with_reg=reg)

    def __10_create_func_code(self, source: Source, num: int | None, denum: int, hse_freq: int) -> str:
        code = ""

        if source == Source.LSE or source == Source.LSI:
            code += (f"RST_CLK_{source.value}config(RST_CLK_{source.value}_ON); // Запуск {source.value}\n"
                     f"if (RST_CLK_{source.value}status() == ERROR)\n"
                     f"    RST_CLK_{source.value}config(RST_CLK_{source.value}_OFF); // {source.value} не запустился – выключение {source.value}\n"
                     f"else // {source.value} запустился и работает стабильно\n")
            code += ("{\n"
                     f"    // Первый и второй мультиплексоры\n"
                     f"    // Более подробно на [c. 7-8] Модуль_тактовой_частоты_MDR.pdf\n\n"
                     f"    RST_CLK_ADCclkSelection(RST_CLK_ADCclk{source.value}); // ADC_C2 = {source.value}\n"
                     f"    RST_CLK_ADCclkPrescaler(RST_CLK_ADCclkDIV{denum}); // N = {denum}\n"
                     "    RST_CLK_ADCclkEnable(ENABLE);\n"
                     "}\n")
        elif source == Source.HSE:
            if num:
                div = 1
                if denum > 1:
                    div = 2
                    denum >>= 1

                code += (f"RST_CLK_HSEconfig(RST_CLK_HSE_ON); // Запуск HSE, fHSE={int(hse_freq / (10 ** 6))} МГц\n"
                         "if (RST_CLK_HSEstatus() == ERROR)\n"
                         "    RST_CLK_HSEconfig(RST_CLK_HSE_OFF); // HSE не запустился – выключение HSE\n"
                         "else // HSE запустился и работает стабильно\n"
                         "{\n"
                         f"    // Первый мультиплексор, USB_C1 = HSE, PLLUSBMUL = {num - 1}\n"
                         f"    RST_CLK_USB_PLLconfig(RST_CLK_USB_PLLsrcHSEdiv{div}, RST_CLK_USB_PLLmul{num});\n"
                         "    RST_CLK_USB_PLLcmd(ENABLE); // Включение схемы умножения частоты\n"
                         "    // Ожидание запуска и стабильной работы схемы умножения частоты\n"
                         "    if(RST_CLK_USB_PLLstatus() == ERROR)\n"
                         "        RST_CLK_USB_PLLcmd(DISABLE); // Выключение схемы умножения частоты\n"
                         "    else\n"
                         "    {\n"
                         "        // Второй мультиплексор, USB_C2 = PLLUSBo\n"
                         "        RST_CLK_USB_PLLuse(ENABLE);\n"
                         "        RST_CLK_ADCclkSelection(RST_CLK_ADCclkUSB_C2); // ADC_C2 = ADC_C1 = USB_C2\n"
                         f"        RST_CLK_ADCclkPrescaler(RST_CLK_ADCclkDIV{denum}); // N = {denum}\n"
                         "        RST_CLK_ADCclkEnable(ENABLE); // Разрешение тактироавания\n"
                         "    }\n"
                         "}\n"
                         )
        elif source == Source.USB:
            code += ("RST_CLK_ADCclkSelection(RST_CLK_ADCclkUSB_C1); // ADC_C2 = ADC_C1 = USB_C1\n"
                     f"RST_CLK_ADCclkPrescaler(RST_CLK_ADCclkDIV{denum}); // N = {denum}\n"
                     "RST_CLK_ADCclkEnable(ENABLE); // Разрешение тактироавания\n"
                     )

        return code

    def __10_create_reg_code(self, source: Source, num: int | None, denum: int) -> str:
        adc_c3_sel = dict(zip(clk_div[1:], range(8, 17)))
        adc_c3_sel[1] = 0

        adc_c2_sel = {
            Source.LSE: 0b00,
            Source.LSI: 0b01,
            Source.HSE: 0b10,
            Source.USB: 0b10,
        }

        adc_c1_sel = {
            Source.USB: 0b01,
            Source.LSE: 0b10,
            Source.LSI: 0b10,
            Source.HSE: 0b10,
        }

        usb_c1_sel = {
            source.HSI: 0b00,
            source.HSE: 0b10,
            source.LSE: 0b00,
            source.LSI: 0b00,
        }

        adc_mco_clk = 0
        adc_mco_clk |= (1 << 13)
        adc_mco_clk |= (adc_c3_sel[denum] << 8)
        adc_mco_clk |= adc_c2_sel[source] << 4
        adc_mco_clk |= adc_c1_sel[source]

        code = ""

        if source == Source.LSE or source == Source.LSI:
            if source == Source.LSE:
                code += ("MDR_BKP->REG_0F |= 1; // Вкл. LSE\n"
                         "if(!(MDR_BKP->REG_0F & 1 << 13)) // Проверка регистра LSERDY\n"
                         "{ // LSE не запустился или нестабильно работает\n"
                         "    MDR_BKP->REG_0F &=~ 1; // Выкл. LSE\n"
                         "}\n"
                         "else // // LSE запустился и работает стабильно\n")
            elif source == Source.LSI:
                code += ("MDR_BKP->REG_0F |= (1 << 15); // Вкл. LSI\n"
                         "if(!(MDR_BKP->REG_0F & 1 << 21)) // Проверка регистра LSIRDY\n"
                         "{ // LSI не запустился или нестабильно работает\n"
                         "    MDR_BKP->REG_0F &=~ (1 << 15); // Выкл. LSI\n"
                         "}\n"
                         "else // // LSI запустился и работает стабильно\n")
            code += ("{\n"
                     f"    // Более подробно на [c. 173] Спецификации\n\n"
                     f"    // {hex(adc_mco_clk)} = {bin(adc_mco_clk)}\n"
                     f"    MDR_RST_CLK->ADC_MCO_CLOCK = {hex(adc_mco_clk)}; // ADCCLKEN = 1\n"
                     "}\n")

        elif source == Source.HSE:
            if num:
                div = 0
                if denum > 1:
                    div = 1
                    denum >>= 1

                adc_mco_clk = 0
                adc_mco_clk |= (1 << 13)
                adc_mco_clk |= (adc_c3_sel[denum] << 8)
                adc_mco_clk |= adc_c2_sel[source] << 4
                adc_mco_clk |= adc_c1_sel[source]

                usb_clock = 0
                usb_clock |= usb_c1_sel[source] + div
                usb_clock |= (1 << 2)
                usb_clock |= (1 << 8)

                adc_mco_clk |= 3
                code += ("MDR_RST_CLK->HS_CONTROL |= 1; // Вкл. HSE\n"
                         "if(!(MDR_RST_CLK->CLOCK_STATUS & 4))\n"
                         "{ // HSE не запустился или нестабильно работает\n"
                         "    MDR_RST_CLK->HS_CONTROL &=~1; // Выкл. HSE\n"
                         "}\n"
                         "else // // HSE запустился и работает стабильно\n"
                         "{\n"
                         f"    MDR_RST_CLK->USB_CLOCK = {hex(usb_clock)}; // {bin(usb_clock)}\n"
                         "    // Запуск схемы умножения частоты USB_PLL\n"
                         "    MDR_RST_CLK->PLL_CONTROL &= ~0xF0; // Сброс PLLUSBMUL\n"
                         f"    MDR_RST_CLK->PLL_CONTROL |= 1 | ({num - 1} << 4); // PLLUSBON = 1, PLLUSBMUL = {num - 1}\n"
                         "    if(MDR_RST_CLK->CLOCK_STATUS & 1)\n"
                         "    { // Схема умножения частоты USB_PLL запустилась и работает стабильно\n"
                         f"        // {hex(adc_mco_clk)} = {bin(adc_mco_clk)}, ADC_C1 = USB_C2, ADC_C2 = ADC_C1, ADC_C3 = ADC_C2/{denum}\n"
                         f"        // Более подробно на [c. 173] Спецификации\n\n"
                         f"        MDR_RST_CLK->ADC_MCO_CLOCK = {hex(adc_mco_clk)}; // ADCCLKEN = 1\n"
                         "    }\n"
                         "}\n")
        elif source == Source.USB:
            code += (
                f"// {hex(adc_mco_clk)} = {bin(adc_mco_clk)}, ADC_C1 = USB_C1, ADC_C2 = ADC_C1, ADC_C3 = ADC_C2/{denum}\n"
                f"// Более подробно на [c. 173] Спецификации\n\n"
                f"MDR_RST_CLK->ADC_MCO_CLOCK = {hex(adc_mco_clk)}; // ADCCLKEN = 1 \n"
            )

        return code
