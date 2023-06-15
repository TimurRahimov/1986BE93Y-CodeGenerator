import dataclasses

from PySide6.QtWidgets import QCheckBox

from questions import Q11


@dataclasses.dataclass
class TimerSettings:
    port: str
    pin: str
    tmr: int
    time: int
    mk_freq: int
    m: int
    arr: int
    psg: int
    irq: str


class Q13(Q11):

    def __init__(self):
        super().__init__()
        self.__13_fill_combo_boxes()
        self.__13_connect_signals()

    def __13_fill_combo_boxes(self):
        for _ in self.port_settings:
            for item in self.port_settings[_]:
                self.ui.__dict__["comboBox_13_" + _].addItem(item)
        for _ in ("-", "1", "2", "3"):
            self.ui.comboBox_13_timer.addItem(_)
        for _ in self.unit_settings["time_unit"]:
            self.ui.comboBox_13_time_unit.addItem(_)
        for _ in self.unit_settings["freq_unit"]:
            self.ui.comboBox_13_freq_unit.addItem(_)
        for _ in ('Инверсия выхода',):
            self.ui.comboBox_13_irq.addItem(_)

    def __13_connect_signals(self):
        self.ui.submitButton_13.clicked.connect(self.__13_submit_handler)

    def __13_unlock_options(self):
        sender: QCheckBox = self.sender()
        checked = sender.isChecked()
        self.ui.pushButton_13_timer_define.setEnabled(checked)
        self.ui.comboBox_13_timer.setEnabled(not checked)
        self.ui.comboBox_13_channel.setEnabled(not checked)

    def __13_define_timer(self):
        port = self.ui.comboBox_13_port.currentText()
        pin = self.ui.comboBox_13_pin.currentText()

        try:
            for _, num in self.port_funcs[port][pin].items():
                if _.startswith('TMR'):
                    tmr = int(_.split('_')[0][3])
                    ch = int(_.split('_')[1][2])
                    self.ui.comboBox_13_timer.setCurrentIndex(tmr)
                    self.ui.comboBox_13_channel.setCurrentIndex(ch)
                    return
        except KeyError:
            pass

        self.ui.comboBox_13_timer.setCurrentIndex(0)
        self.ui.comboBox_13_channel.setCurrentIndex(0)

    def __13_submit_handler(self):
        port = self.ui.comboBox_13_port.currentText()
        pin = self.ui.comboBox_13_pin.currentText()
        tmr = int(self.ui.comboBox_13_timer.currentText())

        time = int(self.ui.lineEdit_13_time.text()) * self.unit_settings[
            'time_unit'][self.ui.comboBox_13_time_unit.currentText()]

        mk_freq = int(self.ui.lineEdit_13_freq.text()) * self.unit_settings[
            'freq_unit'][self.ui.comboBox_13_freq_unit.currentText()]

        m = int(self.ui.lineEdit_13_m.text())
        arr = int(self.ui.lineEdit_13_arr.text())
        psg = int(self.ui.lineEdit_13_psg.text())

        irq = self.ui.comboBox_13_irq.currentText()

        pwm_set = TimerSettings(port=port, pin=pin, tmr=tmr, time=time, mk_freq=mk_freq,
                                m=m, arr=arr, psg=psg, irq=irq)

        func = self.__13_create_func_code(pwm_set)
        reg = self.__13_create_reg_code(pwm_set)

        self.show_code(with_func=func, with_reg=reg)

    def __13_create_func_code(self, tmr_set: TimerSettings) -> str:
        code = ("""#include "MDR32F9Qx_port.h" \n"""
                """#include "MDR32F9Qx_rst_clk.h" \n"""
                """#include "MDR32F9Qx_timer.h" \n\n"""
                f"#define arr {tmr_set.arr} \n"
                f"#define psg {tmr_set.psg} \n"
                f"unsigned Counter;\n\n")

        code += ("// Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "void Port_setup(void);\n\n")

        code += ("int main(void) {\n"
                 "    // Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "    Port_setup();\n\n"
                 f"    RST_CLK_PCLKcmd(RST_CLK_PCLK_TIMER{tmr_set.tmr}, ENABLE); // Разрешение тактирования таймера\n"
                 f"    TIMER_BRGInit(MDR_TIMER{tmr_set.tmr}, TIMER_HCLKdiv1); // Тактовая частота не делится\n"
                 f"    TIMER_DeInit(MDR_TIMER{tmr_set.tmr}); // Полный сброс всех настроек таймера\n"
                 f"    TIMER_SetCntAutoreload(MDR_TIMER{tmr_set.tmr},  arr); // Настройка максимального значения arr\n"
                 f"    TIMER_SetCntPrescaler(MDR_TIMER{tmr_set.tmr}, psg); // Настройка предделителя psg\n"
                 f"    TIMER_ITConfig(MDR_TIMER{tmr_set.tmr}, TIMER_STATUS_CNT_ARR, ENABLE); // Разрешение прерываний\n"
                 f"    NVIC_EnableIRQ(Timer{tmr_set.tmr}_IRQn); // Разрешение прерываний в МК из-за таймера\n"
                 f"    TIMER_Cmd(MDR_TIMER{tmr_set.tmr}, ENABLE); // Включение таймера\n\n"
                 "    while(1) { }\n"
                 "}\n\n")

        if tmr_set.irq == 'Инверсия выхода':
            code += (f"void Timer{tmr_set.tmr}_IRQHandler(void) "
                     "{\n"
                     f"    if (TIMER_GetFlagStatus(MDR_TIMER{tmr_set.tmr}, TIMER_STATUS_CNT_ARR) == SET)"
                     " // Если таймер досчитал до основания \n"
                     "    {\n"
                     "        // Инверсия выхода \n"
                     "        if (++Counter & 1)\n"
                     f"            PORT_SetBits(MDR_PORT{tmr_set.port}, PORT_Pin_{tmr_set.pin}); // Установка бита \n"
                     f"        else\n"
                     f"            PORT_ResetBits(MDR_PORT{tmr_set.port}, PORT_Pin_{tmr_set.pin}); // Сброс бита \n"
                     f"        TIMER_ClearFlag(MDR_TIMER{tmr_set.tmr}, TIMER_STATUS_CNT_ARR); // Сброс флага\n"
                     "    }\n"
                     "}\n\n")

        code += ("void Port_setup(){\n"
                 "    // Данная функция не обязательна, но сюда можно вставить инициализацию "
                 f"необходимого порта (P{tmr_set.port}{tmr_set.pin}) для функции обработки прерываний.\n"
                 "    // Сгенерировать код для этой функции можно в окне \"Настройка порта\"\n"
                 "}\n\n")

        return code

    def __13_create_reg_code(self, tmr_set: TimerSettings) -> str:

        code = ("""#include "MDR32Fx.h" \n\n"""
                f"#define arr {tmr_set.arr} \n"
                f"#define psg {tmr_set.psg} \n\n")

        code += ("// Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "void Port_setup(void);\n\n")

        code += ("int main(void) {\n"
                 "    // Если функция Port_setup не используется, следующая строчка не нужна\n"
                 "    Port_setup();\n\n"
                 f"    MDR_RST_CLK->PER_CLOCK |= (1 << {self.pclk[f'TIMER{tmr_set.tmr}']}); // [с. 175] Разрешение тактирования TIMER{tmr_set.tmr}\n"
                 f"    MDR_RST_CLK->TIM_CLOCK |= (1 << {23 + tmr_set.tmr}); // [c. 177] Разрешение тактовой частоты на TIM{tmr_set.tmr}\n"
                 f"    MDR_RST_CLK->TIM_CLOCK &= ~(7 << {8 * (tmr_set.tmr - 1)}); // [c. 177] Тактовая частота не делится\n"
                 f"    MDR_TIMER{tmr_set.tmr}->CNTRL &= ~(1 << 0); // [с. 301] Выключение таймера для настройки \n"
                 f"    MDR_TIMER{tmr_set.tmr}->CNTRL &= ~(1 << 3); // [с. 301] Направление счета вверх (DIR=0) \n"
                 f"    MDR_TIMER{tmr_set.tmr}->PSG = psg; // [с. 300] Настройка предделителя \n"
                 f"    MDR_TIMER{tmr_set.tmr}->ARR = arr; // [с. 300] Максимальное значение счета таймера (основание счета) \n"
                 f"    MDR_TIMER{tmr_set.tmr}->IE |= (1 << 1); // [с. 311] Разрешение прерываний в таймере \n"
                 f"    NVIC_EnableIRQ(Timer{tmr_set.tmr}_IRQn); // Разрешение прерываний в МК из-за таймера \n"
                 f"    MDR_TIMER{tmr_set.tmr}->CNTRL |= (1 << 0); // [с. 301]  Разрешение работы таймера \n\n"
                 "    while(1) { }\n"
                 "}\n\n")

        if tmr_set.irq == 'Инверсия выхода':
            code += (f"void Timer{tmr_set.tmr}_IRQHandler(void) "
                     "{\n"
                     f"    if (MDR_TIMER{tmr_set.tmr}->STATUS & (1 << 1)) // [c. 309] Если таймер досчитал до основания"
                     "\n    {\n"
                     f"        MDR_PORT{tmr_set.port}->RXTX ^= (1 << {tmr_set.pin}); // [с. 194] Инверсия вывода \n"
                     f"        MDR_TIMER{tmr_set.tmr}->STATUS &= ~(1 << 1); // [c. 309] Сброс флага\n"
                     "    }\n"
                     "}\n\n")

        code += ("void Port_setup(){\n"
                 "    // Данная функция не обязательна, но сюда можно вставить инициализацию "
                 f"необходимого порта (P{tmr_set.port}{tmr_set.pin}) для функции обработки прерываний.\n"
                 "    // Сгенерировать код для этой функции можно в окне \"Настройка порта\"\n"
                 "}\n\n")

        return code
