from questions import Q12

settings = {
    "time_unit": {
        "ч": 3600,
        "мин": 60,
        "с": 1,
        "мс": 10 ** (-3),
        "мкс": 10 ** (-6)
    },
    "freq_unit": {
        "Гц": 1,
        "кГц": 10 ** 3,
        "МГц": 10 ** 6,
        "ГГц": 10 ** 9
    },
    "isr": {
        "Инверсия вывода"
    }
}


class Q5(Q12):

    def __init__(self):
        super().__init__()
        self.__5_fill_combo_boxes()
        self.__5_connect_signals()

    def __5_fill_combo_boxes(self):
        for _ in settings:
            for item in settings[_]:
                self.ui.__dict__["comboBox_5_" + _].addItem(item)
        for _ in self.port_settings:
            for item in self.port_settings[_]:
                self.ui.__dict__["comboBox_5_" + _].addItem(item)

    def __5_connect_signals(self):
        self.ui.submitButton_5.clicked.connect(self.__5_submit_handler)

    def __5_submit_handler(self):
        time_unit = settings["time_unit"][self.ui.comboBox_5_time_unit.currentText()]
        freq_unit = settings["freq_unit"][self.ui.comboBox_5_freq_unit.currentText()]

        time = int(self.ui.lineEdit_5_time.text()) * time_unit
        freq = int(self.ui.lineEdit_5_freq.text()) * freq_unit
        load = int(time * freq)

        func = self.__5_create_func_code(load)
        reg = self.__5_create_reg_code(load)

        self.show_code(with_func=func, with_reg=reg)

    def __5_create_func_code(self, load: int) -> str:
        port = self.ui.comboBox_5_port.currentText()
        pin = self.ui.comboBox_5_pin.currentText()
        lsi: bool = self.ui.checkBox_5_lsi.isChecked()
        isr = self.ui.comboBox_5_isr.currentText()

        code = ("""#include "MDR32F9Qx_port.h"\n"""
                """#include "MDR32F9Qx_rst_clk.h" \n\n"""
                f"#define COUNT {load}\n"
                f"unsigned Counter;\n\n")

        code += ("// Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "void Port_setup(void);\n\n")

        code += ("int main(void) {\n"
                 "    // Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "    Port_setup();\n\n"
                 "    SysTick_Config(COUNT);\n"
                 f"{'    SysTick->CTRL &=~ (1 << 2);' if lsi else ''}")

        if lsi:
            code += "\n"

        code += ("    while(1) { }\n"
                 "}\n\n")

        if isr == 'Инверсия вывода':
            code += ("void SysTick_Handler(void) {\n"
                     "    if (++Counter & 1)\n"
                     f"        PORT_SetBits(MDR_PORT{port}, PORT_Pin_{pin});\n"
                     f"    else\n"
                     f"        PORT_ResetBits(MDR_PORT{port}, PORT_Pin_{pin});\n"
                     "}\n\n")

        code += ("void Port_setup(){\n"
                 "    // Данная функция не обязательна, но сюда можно вставить инициализацию "
                 f"необходимого порта (P{port}{pin}) для функции обработки прерываний.\n"
                 "    // Сгенерировать код для этой функции можно в окне \"Настройка порта\"\n"
                 "}\n\n")

        return code

    def __5_create_reg_code(self, load: int) -> str:
        port = self.ui.comboBox_5_port.currentText()
        pin = self.ui.comboBox_5_pin.currentText()
        lsi: bool = self.ui.checkBox_5_lsi.isChecked()
        isr = self.ui.comboBox_5_isr.currentText()

        code = ("""#include "MDR32Fx.h" \n\n"""
                f"#define COUNT {load}\n\n")

        code += ("// Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "void Port_setup(void);\n\n")

        code += ("int main(void) {\n"
                 "    // Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "    Port_setup();\n\n"
                 "    SysTick->LOAD = COUNT - 1;\n"
                 "    NVIC_SetPriority (SysTick_IRQn, (1<<__NVIC_PRIO_BITS) - 1);\n"
                 "    SysTick->VAL = 0;\n"
                 f"    SysTick->CTRL = ({'0' if lsi else '1'} << 2) | (1 << 1) | (1 << 0);\n"
                 "    while(1) { }\n"
                 "}\n\n")

        if isr == 'Инверсия вывода':
            code += ("void SysTick_Handler(void) {\n"
                     f"    MDR_PORT{port}->RXTX ^= (1 << {pin});\n"
                     "}\n\n")

        code += ("void Port_setup(){\n"
                 "    // Данная функция не обязательна, но сюда можно вставить инициализацию "
                 f"необходимого порта (P{port}{pin}) для функции обработки прерываний.\n"
                 "    // Сгенерировать код для этой функции можно в окне \"Настройка порта\"\n"
                 "}\n\n")

        return code
