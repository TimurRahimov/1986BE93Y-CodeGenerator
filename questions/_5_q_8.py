from PySide6.QtWidgets import QCheckBox

from questions import Q7

eeprom_latency = [x * 10 ** 6 for x in [25, 50, 75, 100, 125, 150, 175, 200]]
pll_mul = list(range(17))
clk_div = [2 ** x for x in range(9)]

settings = {
    "freq_unit": {
        "Гц": 1,
        "кГц": 10 ** 3,
        "МГц": 10 ** 6,
        "ГГц": 10 ** 9
    },
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
        self.ui.lineEdit_8_nhse.setText("8")
        self.ui.comboBox_8_nhse.setCurrentText("МГц")

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
        main = self.ui.checkBox_8_main.isChecked()
        freq = self.ui.checkBox_8_freq.isChecked()
        hse_freq = int(self.ui.lineEdit_8_nhse.text()) * settings["freq_unit"][self.ui.comboBox_8_nhse.currentText()]

        if not main and not freq:
            return

        num = None
        denum = None

        if main:
            num = int(self.ui.lineEdit_8_num.text())
            denum = int(self.ui.lineEdit_8_denum.text())
            if num not in pll_mul or denum not in clk_div:
                return
        elif freq:
            freq = int(self.ui.lineEdit_8_freq.text()) * settings[
                "freq_unit"][self.ui.comboBox_8_freq_unit.currentText()]
            for div in clk_div:
                a = (freq * div / hse_freq)
                if int(a) == a:
                    if a > 16:
                        continue
                    num = int(a)
                    denum = div
                    break
            if num is None or denum is None:
                return

        latency_level = 7
        latency = num * hse_freq / denum
        for i in range(len(eeprom_latency)):
            if eeprom_latency[i] > latency:
                latency_level = i
                break

        func = self.__8_create_func_code(num, denum, hse_freq, latency_level)
        reg = self.__8_create_reg_code(num, denum, hse_freq, latency_level)

        self.show_code(with_func=func, with_reg=reg)

    def __8_create_func_code(self, num: int, denum: int, hse_freq: int, latency_level: int) -> str:

        code = (f"RST_CLK_HSEconfig(RST_CLK_HSE_ON); // Запуск HSE, fHSE={hse_freq / (10 ** 6)} МГц\n"
                "if (RST_CLK_HSEstatus() == ERROR)\n"
                "    RST_CLK_HSEconfig(RST_CLK_HSE_OFF); // HSE не запустился – выключение HSE\n"
                "else // HSE запустился и работает стабильно\n"
                f"    // Первый мультиплексор, CPU_C1 = HSE, PLLCPUMUL = {num - 1}\n"
                f"    RST_CLK_CPU_PLLconfig(RST_CLK_CPU_PLLsrcHSEdiv1, RST_CLK_CPU_PLLmul{num});\n"
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
                )

        return code

    def __8_create_reg_code(self, num: int, denum: int, hse_freq: int, latency_level: int) -> str:
        cpu_clock = 0
        cpu_clock |= 1 << 8
        cpu_clock |= cpu_c3_sel[denum] << 4
        cpu_clock |= 1 << 2
        cpu_clock |= 1 << 1

        code = ("MDR_RST_CLK->HS_CONTROL |= 1; // Вкл. HSE\n"
                "if(!(MDR_RST_CLK->CLOCK_STATUS & 4))\n"
                "{ // HSE не запустился или нестабильно работает\n"
                "    MDR_RST_CLK->HS_CONTROL &=~1; // Выкл. HSE\n"
                "}\n"
                "else // // HSE запустился и работает стабильно\n"
                "{\n"
                "    // Запуск схемы умножения частоты CPU_PLL\n"
                f"    MDR_RST_CLK->PLL_CONTROL = (1 << 2) | ({num - 1} << 8); // PLLCPUON = 1; PLLCPUMUL = {num - 1}\n"
                "    if(MDR_RST_CLK->CLOCK_STATUS & 2)\n"
                "    { // Схема умножения частоты CPU_PLL запустилась и работает стабильно\n"
                f"        MDR_EEPROM->CMD |= {latency_level} << 3;\n"
                f"        MDR_RST_CLK->CPU_CLOCK = {hex(cpu_clock)}; // {bin(cpu_clock)}\n"
                "    }\n"
                "    else\n"
                "    // Схема умножения частоты CPU_PLL не запустилась или работает нестабильно\n"
                "    MDR_RST_CLK->PLL_CONTROL &= ~4; // Выкл. схема умножения частоты CPU_PLL\n"
                "}\n")

        return code
