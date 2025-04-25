import enum

from PySide6.QtWidgets import QCheckBox

from questions import Q8

eeprom_latency = [x * 10 ** 6 for x in [25, 50, 75, 100, 125, 150, 175, 200]]
pll_mul = list(range(17))
clk_div = [2 ** x for x in range(3)]


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
    }
}


class Q9(Q8):

    def __init__(self):
        super().__init__()
        self.__9_fill_combo_boxes()
        self.__9_connect_signals()

    def __9_fill_combo_boxes(self):
        for _ in settings["freq_unit"]:
            self.ui.comboBox_9_nhse.addItem(_)
            self.ui.comboBox_9_freq_unit.addItem(_)
        for _ in settings["source"]:
            self.ui.comboBox_9_source.addItem(_)
        self.ui.lineEdit_9_nhse.setText("8")
        self.ui.comboBox_9_nhse.setCurrentText("МГц")
        self.ui.comboBox_9_source.setCurrentText(Source.HSE.value)

    def __9_connect_signals(self):
        self.ui.checkBox_9_nhse.stateChanged.connect(self.__9_unlock_options)
        self.ui.checkBox_9_freq.stateChanged.connect(self.__9_unlock_options)
        self.ui.checkBox_9_main.stateChanged.connect(self.__9_unlock_options)
        self.ui.submitButton_9.clicked.connect(self.__9_submit_handler)

    def __9_unlock_options(self):
        sender: QCheckBox = self.sender()
        option = sender.objectName().split('_')[-1]
        checked = sender.isChecked()

        if option == 'nhse':
            self.ui.comboBox_9_nhse.setEnabled(checked)
            self.ui.lineEdit_9_nhse.setEnabled(checked)
        elif option == 'freq':
            self.ui.comboBox_9_freq_unit.setEnabled(checked)
            self.ui.lineEdit_9_freq.setEnabled(checked)
            if checked:
                self.ui.checkBox_9_main.setChecked(False)
        elif option == 'main':
            self.ui.lineEdit_9_denum.setEnabled(checked)
            self.ui.lineEdit_9_num.setEnabled(checked)
            if checked:
                self.ui.checkBox_9_freq.setChecked(False)

    def __9_submit_handler(self):
        b_main = self.ui.checkBox_9_main.isChecked()
        b_freq = self.ui.checkBox_9_freq.isChecked()
        source = Source(self.ui.comboBox_9_source.currentText().upper())
        freq = int(self.ui.lineEdit_9_nhse.text()) * settings["freq_unit"][self.ui.comboBox_9_nhse.currentText()]

        if not b_main and not b_freq:
            return

        num = None
        denum = None

        if b_main:
            num = int(self.ui.lineEdit_9_num.text())
            denum = int(self.ui.lineEdit_9_denum.text())
            if num not in pll_mul or denum not in clk_div:
                return
        elif b_freq:
            b_freq = int(self.ui.lineEdit_9_freq.text()) * settings[
                "freq_unit"][self.ui.comboBox_9_freq_unit.currentText()]
            for div in clk_div:
                a = (b_freq * div / freq)
                if int(a) == a:
                    if a > 16:
                        continue
                    num = int(a)
                    denum = div
                    break
            if num is None or denum is None:
                return

        func = self.__9_create_func_code(source, num, denum, freq)
        reg = self.__9_create_reg_code(source, num, denum, freq)

        self.show_code(with_func=func, with_reg=reg)

    def __9_create_func_code(self, source: Source, num: int, denum: int, freq: int) -> str:
        if denum == 2:
            div = 1
            n = 2
        elif denum == 4:
            div = 2
            n = 2
        else:
            div = 1
            n = 1

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

        code += ("{\n"
                 f"    // Первый мультиплексор, USB_C1 = {source.value}{'/2 ' if div == 2 else ''}, PLLUSBMUL = {num - 1}\n"
                 f"    RST_CLK_USB_PLLconfig(RST_CLK_USB_PLLsrc{source.value}div{div}, RST_CLK_USB_PLLmul{num});\n"
                 "    RST_CLK_USB_PLLcmd(ENABLE); // Включение схемы умножения частоты\n"
                 "    // Ожидание запуска и стабильной работы схемы умножения частоты\n"
                 "    if(RST_CLK_USB_PLLstatus() == ERROR)\n"
                 "        RST_CLK_USB_PLLcmd(DISABLE); // Выключение схемы умножения частоты\n"
                 "    else\n"
                 "    {\n"
                 "        // Второй мультиплексор, USB_C2 = PLLUSBo\n"
                 "        RST_CLK_USB_PLLuse(ENABLE);\n"
                 "    }\n"
                 f"    RST_CLK_USBclkPrescaler({'ENABLE' if n == 2 else 'DISABLE'}); // N = {n}\n"
                 "    RST_CLK_USBclkEnable(ENABLE); // Разрешение тактирования модуля USB\n"
                 "}\n"
                 )

        return code

    def __9_create_reg_code(self, source: Source, num: int, denum: int, freq: int) -> str:

        if denum == 2:
            sel = 0b10
            n = 1
        elif denum == 4:
            sel = 0b11
            n = 1
        else:
            sel = 0b10
            n = 0

        usb_clock = 0
        usb_clock |= 1 << 8
        usb_clock |= n << 4
        usb_clock |= sel

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

        code += ("{\n"
                "    // Запуск схемы умножения частоты USB_PLL\n"
                "    MDR_RST_CLK->PLL_CONTROL &= ~0xF0; // Сброс PLLUSBMUL\n"
                f"    MDR_RST_CLK->PLL_CONTROL |= 1 | ({num - 1} << 4); // PLLUSBON = 1, PLLUSBMUL = {num - 1}\n"
                "    if(MDR_RST_CLK->CLOCK_STATUS & 1)\n"
                "    { // Схема умножения частоты USB_PLL запустилась и работает стабильно\n"
                f"        MDR_RST_CLK->USB_CLOCK = {hex(usb_clock)}; // {bin(usb_clock)}\n"
                "    }\n"
                "}\n")

        return code
