import enum

from PySide6.QtWidgets import QCheckBox

from questions import Q7

eeprom_latency = [x * 10 ** 6 for x in [25, 50, 75, 100, 125, 150, 175, 200]]
pll_mul = list(range(17))
clk_div = [2 ** x for x in range(9)]


class Source(enum.Enum):
    HSI = "HSI"
    LSI = "LSI"
    HSE = "HSE"
    LSE = "LSE"


settings = {
    "freq_unit": {
        "Гц": 1,
        "кГц": 10 ** 3,
        "МГц": 10 ** 6,
        "ГГц": 10 ** 9
    },
    "source": {
        Source.HSE.value,
        Source.HSI.value,
        Source.LSE.value,
        Source.LSI.value,
    }
}

cpu_c3_sel = dict(zip(clk_div[1:], range(8, 16)))
cpu_c3_sel[1] = 0


class Q8(Q7):

    def __init__(self):
        super().__init__()
        self.__8_fill_combo_boxes()
        self.__8_connect_signals()

    def __8_fill_combo_boxes(self):
        for _ in settings["freq_unit"]:
            self.ui.comboBox_8_nhse.addItem(_)
            self.ui.comboBox_8_freq_unit.addItem(_)
        for _ in settings["source"]:
            self.ui.comboBox_8_source.addItem(_)
        self.ui.lineEdit_8_nhse.setText("8")
        self.ui.comboBox_8_nhse.setCurrentText("МГц")
        self.ui.comboBox_8_source.setCurrentText(Source.HSE.value)

    def __8_connect_signals(self):
        self.ui.checkBox_8_nhse.stateChanged.connect(self.__8_unlock_options)
        self.ui.checkBox_8_freq.stateChanged.connect(self.__8_unlock_options)
        self.ui.checkBox_8_main.stateChanged.connect(self.__8_unlock_options)
        self.ui.submitButton_8.clicked.connect(self.__8_submit_handler)

    def __8_unlock_options(self):
        sender: QCheckBox = self.sender()
        option = sender.objectName().split('_')[-1]
        checked = sender.isChecked()

        if option == 'nhse':
            self.ui.comboBox_8_nhse.setEnabled(checked)
            self.ui.lineEdit_8_nhse.setEnabled(checked)
        elif option == 'freq':
            self.ui.comboBox_8_freq_unit.setEnabled(checked)
            self.ui.lineEdit_8_freq.setEnabled(checked)
            if checked:
                self.ui.checkBox_8_main.setChecked(False)
        elif option == 'main':
            self.ui.lineEdit_8_denum.setEnabled(checked)
            self.ui.lineEdit_8_num.setEnabled(checked)
            if checked:
                self.ui.checkBox_8_freq.setChecked(False)

    def __8_submit_handler(self):
        b_main = self.ui.checkBox_8_main.isChecked()
        b_freq = self.ui.checkBox_8_freq.isChecked()
        source = Source(self.ui.comboBox_8_source.currentText().upper())
        freq = int(self.ui.lineEdit_8_nhse.text()) * settings["freq_unit"][self.ui.comboBox_8_nhse.currentText()]

        if source in [Source.HSE, Source.HSI]:
            if not b_main and not freq:
                return

            num = None
            denum = None

            if b_main:
                num = int(self.ui.lineEdit_8_num.text())
                denum = int(self.ui.lineEdit_8_denum.text())
                if num not in pll_mul or denum not in clk_div:
                    return
            elif b_freq:
                freq = int(self.ui.lineEdit_8_freq.text()) * settings[
                    "freq_unit"][self.ui.comboBox_8_freq_unit.currentText()]
                for div in clk_div:
                    a = (freq * div / freq)
                    if int(a) == a:
                        if a > 16:
                            continue
                        num = int(a)
                        denum = div
                        break
                if num is None or denum is None:
                    return

            latency_level = 7
            latency = num * freq / denum
            for i in range(len(eeprom_latency)):
                if eeprom_latency[i] > latency:
                    latency_level = i
                    break
            func = self.__8_create_func_code(source, num, denum, freq, latency_level)
            reg = self.__8_create_reg_code(source, num, denum, freq, latency_level)

        else:
            func = self.__8_create_func_code(source, 1, 1, freq, 1)
            reg = self.__8_create_reg_code(source, 1, 1, freq, 1)

        self.show_code(with_func=func, with_reg=reg)

    def __8_create_func_code(self, source: Source, num: int, denum: int, freq: int, latency_level: int) -> str:

        code = ""

        if source == Source.HSE:
            code += (f"RST_CLK_HSEconfig(RST_CLK_HSE_ON); // Запуск HSE\n"
                     "if (RST_CLK_HSEstatus() == ERROR)\n"
                     "    RST_CLK_HSEconfig(RST_CLK_HSE_OFF); // HSE не запустился – выключение HSE\n"
                     "else // HSE запустился и работает стабильно\n")
        elif source == Source.HSI:
            code += (f"RST_CLK_HSIcmd(ENABLE); // Запуск HSI\n"
                     "if (RST_CLK_HSIstatus() == ERROR)\n"
                     "    RST_CLK_HSIcmd(DISABLE); // HSI не запустился – выключение HSI\n"
                     "else // HSI запустился и работает стабильно\n")
        elif source == Source.LSE or source == Source.LSI:
            code += (f"RST_CLK_{source.value}config(RST_CLK_{source.value}_ON); // Запуск {source.value}\n"
                     f"if (RST_CLK_{source.value}status() == ERROR)\n"
                     f"    RST_CLK_{source.value}config(RST_CLK_{source.value}_OFF); // {source.value} не запустился – выключение {source.value}\n"
                     f"else // {source.value} запустился и работает стабильно\n")

        if source == Source.HSE or source == Source.HSI:
            code += ("{\n"
                     f"    // Первый мультиплексор, CPU_C1 = {source.value}, PLLCPUMUL = {num - 1}\n"
                     f"    RST_CLK_CPU_PLLconfig(RST_CLK_CPU_PLLsrc{source.value}div1, RST_CLK_CPU_PLLmul{num});\n"
                     "    RST_CLK_CPU_PLLcmd(ENABLE); // Включение схемы умножения частоты\n"
                     "    // Ожидание запуска и стабильной работы схемы умножения частоты\n"
                     "    if(RST_CLK_CPU_PLLstatus() == ERROR)\n"
                     "        RST_CLK_CPU_PLLcmd(DISABLE); // Выключение схемы умножения частоты\n"
                     "    else\n"
                     "    {\n"
                     "        // Второй мультиплексор, CPU_C2 = PLLCPUo\n"
                     "        RST_CLK_CPU_PLLuse(ENABLE);\n"
                     f"        EEPROM_SetLatency(EEPROM_Latency_{latency_level}); \n"
                     "    }\n"
                     f"    RST_CLK_CPUclkPrescaler(RST_CLK_CPUclkDIV{denum}); // N = {denum}\n"
                     "    RST_CLK_CPUclkSelection(RST_CLK_CPUclkCPU_C3); // Третий мультиплексор, fHCLK=fCPU_C3\n"
                     "}\n")
        else:
            code += ("{\n"
                     f"    RST_CLK_CPUclkSelection(RST_CLK_CPUclk{source.value}); // Третий мультиплексор, fHCLK=f{source.value}\n"
                     "}\n")

        return code

    def __8_create_reg_code(self, source: Source, num: int, denum: int, hse_freq: int, latency_level: int) -> str:
        cpu_clock = 0
        cpu_clock |= 1 << 8
        cpu_clock |= cpu_c3_sel[denum] << 4
        cpu_clock |= 1 << 2
        cpu_clock |= 1 << 1

        code = ""

        if source == Source.HSE:
            code += ("MDR_RST_CLK->HS_CONTROL |= 1; // Вкл. HSE\n"
                     "if(!(MDR_RST_CLK->CLOCK_STATUS & 4))\n"
                     "{ // HSE не запустился или нестабильно работает\n"
                     "    MDR_RST_CLK->HS_CONTROL &=~1; // Выкл. HSE\n"
                     "}\n"
                     "else // // HSE запустился и работает стабильно\n")
        elif source == Source.HSI:
            code += ("MDR_BKP->REG_0F |= (1 << 22); // Вкл. HSI\n"
                     "if(!(MDR_BKP->REG_0F & (1 << 23))) // Проверка регистра HSIRDY\n"
                     "{ // HSI не запустился или нестабильно работает\n"
                     "    MDR_BKP->REG_0F &=~ (0 << 22); // Выкл. HSI\n"
                     "}\n"
                     "else // // HSI запустился и работает стабильно\n")
        elif source == Source.LSE:
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

        if source == Source.HSE or source == Source.HSI:
            code += ("{\n"
                     "    // Запуск схемы умножения частоты CPU_PLL\n"
                     f"    MDR_RST_CLK->PLL_CONTROL = (1 << 2) | ({num - 1} << 8); // PLLCPUON = 1; PLLCPUMUL = {num - 1}\n"
                     "    if(MDR_RST_CLK->CLOCK_STATUS & 2)\n"
                     "    { // Схема умножения частоты CPU_PLL запустилась и работает стабильно\n"
                     f"        MDR_EEPROM->CMD |= {latency_level} << 3;\n"
                     f"        MDR_RST_CLK->CPU_CLOCK = {hex(cpu_clock)}; // выбор fHCLK=f{source.value} : {bin(cpu_clock)}\n"
                     "    }\n"
                     "    else\n"
                     "        // Схема умножения частоты CPU_PLL не запустилась или работает нестабильно\n"
                     "        MDR_RST_CLK->PLL_CONTROL &= ~4; // Выкл. схема умножения частоты CPU_PLL\n"
                     "}\n")
        else:
            cpu_clock = 0
            if source == Source.LSI:
                cpu_clock |= (3 << 8)
            elif source == Source.LSE:
                cpu_clock |= (2 << 8)
            code += ("{\n"
                    f"    MDR_RST_CLK->CPU_CLOCK = {hex(cpu_clock)}; // выбор fHCLK=f{source.value} : {bin(cpu_clock)}\n" 
                     "}\n")

        return code
