import dataclasses

from PySide6.QtWidgets import QCheckBox

from questions import Q13

settings = {
    "inv": {
        "Включена": True,
        "Выключена": False
    },
    "func": {
        0: "PORT_FUNC_PORT",
        1: "PORT_FUNC_MAIN",
        2: "PORT_FUNC_ALTER",
        3: "PORT_FUNC_OVERRID"
    }
}


@dataclasses.dataclass
class PwmSettings:
    port: str
    pin: str
    tmr: int
    ch: int
    pwm_port: str
    pwm_time: int
    impuls_time: int
    mk_freq: int
    m: int
    arr: int
    psg: int
    ccry: int
    inv: bool


class Q14(Q13):

    def __init__(self):
        super().__init__()
        self.__14_fill_combo_boxes()
        self.__14_connect_signals()

    def __14_fill_combo_boxes(self):
        for _ in self.port_settings:
            for item in self.port_settings[_]:
                self.ui.__dict__["comboBox_14_" + _].addItem(item)
        for _ in ("-", "1", "2", "3"):
            self.ui.comboBox_14_timer.addItem(_)
            self.ui.comboBox_14_channel.addItem(_)
        for _ in self.unit_settings["time_unit"]:
            self.ui.comboBox_14_time_unit.addItem(_)
            self.ui.comboBox_14_impuls_unit.addItem(_)
        for _ in self.unit_settings["freq_unit"]:
            self.ui.comboBox_14_freq_unit.addItem(_)
        for _ in settings["inv"]:
            self.ui.comboBox_14_pwm_inv.addItem(_)

    def __14_connect_signals(self):
        self.ui.checkBox_14_timer_undefined.stateChanged.connect(self.__14_unlock_options)
        self.ui.pushButton_14_timer_define.clicked.connect(self.__14_define_timer)
        self.ui.submitButton_14.clicked.connect(self.__14_submit_handler)

    def __14_unlock_options(self):
        sender: QCheckBox = self.sender()
        checked = sender.isChecked()
        self.ui.pushButton_14_timer_define.setEnabled(checked)
        self.ui.comboBox_14_timer.setEnabled(not checked)
        self.ui.comboBox_14_channel.setEnabled(not checked)

    def __14_define_timer(self):
        port = self.ui.comboBox_14_port.currentText()
        pin = self.ui.comboBox_14_pin.currentText()

        try:
            for _, num in self.port_funcs[port][pin].items():
                if _.startswith('TMR'):
                    tmr = int(_.split('_')[0][3])
                    ch = int(_.split('_')[1][2])
                    self.ui.comboBox_14_timer.setCurrentIndex(tmr)
                    self.ui.comboBox_14_channel.setCurrentIndex(ch)
                    return
        except KeyError:
            pass

        self.ui.comboBox_14_timer.setCurrentIndex(0)
        self.ui.comboBox_14_channel.setCurrentIndex(0)

    def __14_submit_handler(self):
        port = self.ui.comboBox_14_port.currentText()
        pin = self.ui.comboBox_14_pin.currentText()

        tmr = self.ui.comboBox_14_timer.currentText()
        ch = self.ui.comboBox_14_channel.currentText()

        if tmr == '-' or ch == '-':
            return

        tmr = int(tmr)
        ch = int(ch)
        pwm_port = None

        try:
            for _, num in self.port_funcs[port][pin].items():
                if _.startswith(f'TMR{tmr}_CH{ch}'):
                    n = _[-1] == 'N'
                    pwm_port = _
                    break
        except KeyError:
            return

        if not pwm_port:
            return

        pwm_time = int(self.ui.lineEdit_14_time.text()) * self.unit_settings[
            'time_unit'][self.ui.comboBox_14_time_unit.currentText()]
        impuls_time = int(self.ui.lineEdit_14_impuls.text()) * self.unit_settings[
            'time_unit'][self.ui.comboBox_14_impuls_unit.currentText()]

        mk_freq = int(self.ui.lineEdit_14_freq.text()) * self.unit_settings[
            'freq_unit'][self.ui.comboBox_14_freq_unit.currentText()]

        m = int(self.ui.lineEdit_14_m.text())
        arr = int(self.ui.lineEdit_14_arr.text())
        psg = int(self.ui.lineEdit_14_psg.text())
        ccry = int(self.ui.lineEdit_14_ccry.text())
        inv = settings["inv"][self.ui.comboBox_14_pwm_inv.currentText()]

        pwm_set = PwmSettings(port=port, pin=pin, tmr=tmr, ch=ch, pwm_port=pwm_port, pwm_time=pwm_time,
                              impuls_time=impuls_time, mk_freq=mk_freq, m=m, arr=arr, psg=psg, ccry=ccry, inv=inv)

        func = self.__14_create_func_code(pwm_set)
        reg = self.__14_create_reg_code(pwm_set)

        self.show_code(with_func=func, with_reg=reg)

    def __14_create_func_code(self, pwm_set: PwmSettings) -> str:

        pwm_dir = 'Neg' if pwm_set.pwm_port[-1] == 'N' else 'Dir'

        code = ("""#include "MDR32Fx.h" \n"""
                """#include "MDR32F9Qx_port.h" \n"""
                """#include "MDR32F9Qx_rst_clk.h" \n\n"""
                """#include "MDR32F9Qx_timer.h" \n"""
                f"#define arr {pwm_set.arr} \n"
                f"#define psg {pwm_set.psg} \n"
                f"#define ccr {pwm_set.ccry} \n\n"
                "int main(void)\n"
                "{\n")

        code += ("""    TIMER_ChnInitTypeDef s;\n"""
                 "    TIMER_ChnOutInitTypeDef sOut;\n"
                 "    PORT_InitTypeDef PORT_InitStructure;\n\n"
                 f"    /* Разрешение тактирования таймера {pwm_set.tmr} и порта {pwm_set.port} */\n"
                 f"    RST_CLK_PCLKcmd(RST_CLK_PCLK_TIMER{pwm_set.tmr} | RST_CLK_PCLK_PORT{pwm_set.port}, ENABLE);\n"
                 f"    /* Разрешение тактирования таймера {pwm_set.tmr} и установка значения М = {pwm_set.m} */\n"
                 f"    TIMER_BRGInit(MDR_TIMER{pwm_set.tmr},TIMER_HCLKdiv{pwm_set.m});\n\n")

        func = settings['func'][self.port_funcs[pwm_set.port][pwm_set.pin][pwm_set.pwm_port]]

        code += (
            f"    /* Настройка вывода пина {pwm_set.pin} порта {pwm_set.port} для работы в режиме цифрового вывода */\n"
            f"    PORT_InitStructure.PORT_Pin = PORT_Pin_{pwm_set.pin};\n"
            "    PORT_InitStructure.PORT_OE = PORT_OE_OUT;\n"
            f"    PORT_InitStructure.PORT_FUNC = {func};\n"
            "    PORT_InitStructure.PORT_MODE = PORT_MODE_DIGITAL;\n"
            "    PORT_InitStructure.PORT_SPEED = PORT_SPEED_FAST;\n"
            f"    PORT_Init(MDR_PORT{pwm_set.port}, &PORT_InitStructure);\n\n"
            f"    /* Настройка {pwm_set.ch} канала таймера {pwm_set.tmr} для работы в режиме ШИМ */\n"
            "    TIMER_ChnStructInit(&s);\n"
            f"    s.TIMER_CH_Number = TIMER_CHANNEL{pwm_set.ch};\n"
            "    s.TIMER_CH_REF_Format = TIMER_CH_REF_Format6;\n"
            f"    TIMER_ChnInit(MDR_TIMER{pwm_set.tmr}, &s);\n\n"
            f"    /* Запись значений в регистры CCR */\n"
            f"    TIMER_SetChnCompare(MDR_TIMER{pwm_set.tmr}, TIMER_CHANNEL{pwm_set.ch}, ccr);\n\n"
            f"    /* Настройка выхода {pwm_set.ch} канала таймера {pwm_set.tmr} */\n"
            f"    sOut.TIMER_CH_{pwm_dir}Out_Polarity = TIMER_CHOPolarity_{'' if pwm_set.inv else 'Non'}Inverted;\n"
            f"    sOut.TIMER_CH_{pwm_dir}Out_Source = TIMER_CH_OutSrc_REF;\n"
            f"    sOut.TIMER_CH_{pwm_dir}Out_Mode = TIMER_CH_OutMode_Output;\n"
            f"    sOut.TIMER_CH_Number = TIMER_CHANNEL{pwm_set.ch};\n"
            f"    TIMER_ChnOutInit(MDR_TIMER{pwm_set.tmr}, &sOut);\n\n"
            f""
            f"    TIMER_SetCntPrescaler(MDR_TIMER{pwm_set.tmr}, psg);\n"
            f"    TIMER_SetCntAutoreload(MDR_TIMER{pwm_set.tmr}, arr);\n"
            f"    TIMER_Cmd(MDR_TIMER{pwm_set.tmr}, ENABLE);\n\n"
            "    while(1) { }\n"
            "}\n")

        return code

    def __14_create_reg_code(self, pwm_set: PwmSettings) -> str:

        code = ("""#include "MDR32Fx.h" \n\n"""
                f"#define arr {pwm_set.arr} \n"
                f"#define psg {pwm_set.psg} \n"
                f"#define ccr {pwm_set.ccry} \n\n"
                "int main(void)\n"
                "{\n")

        per_clock = [f"(1 << {self.pclk[f'PORT{pwm_set.port}']})"]

        try:
            for func, func_num in self.port_funcs[pwm_set.port][pwm_set.pin].items():
                if func == pwm_set.pwm_port:
                    if func.startswith('TMR'):
                        per_clock.append(f"(1 << {self.pclk[f'TIMER{func[3]}']})")
        except KeyError:
            pass

        func = self.port_funcs[pwm_set.port][pwm_set.pin][pwm_set.pwm_port]
        cntrl1 = 0
        if pwm_set.pwm_port[-1] == 'N':
            cntrl1 |= 1 << 8
            cntrl1 |= 2 << 10
            if pwm_set.inv:
                cntrl1 |= 1 << 12
        else:
            cntrl1 |= 1
            cntrl1 |= 2 << 2
            if pwm_set.inv:
                cntrl1 |= 1 << 4

        code += (f"    /* Разрешение тактирования таймера {pwm_set.tmr} и порта {pwm_set.port} */\n"
                 f"    MDR_RST_CLK->PER_CLOCK |= {' | '.join(per_clock)};\n"
                 "    /* Разрешение тактирования таймера 1 и установка значения М = 1 */\n"
                 f"    MDR_RST_CLK->TIM_CLOCK = 1 << {23 + int(pwm_set.tmr)};\n\n"
                 f"    /* Настройка вывода {pwm_set.pin} порта {pwm_set.port} для работы в режиме цифрового вывода */\n"
                 f"    MDR_PORT{pwm_set.port}->OE = (1 << {pwm_set.pin});\n"
                 f"    MDR_PORT{pwm_set.port}->FUNC = ({func} << {pwm_set.pin * 2});\n"
                 f"    MDR_PORT{pwm_set.port}->ANALOG = (1 << {pwm_set.pin});\n"
                 f"    MDR_PORT{pwm_set.port}->PWR = (3 << {pwm_set.pin * 2});\n\n"
                 f"    /* Настройка {pwm_set.ch} канала таймера {pwm_set.tmr} для работы в режиме ШИМ */\n"
                 f"    MDR_TIMER{pwm_set.tmr}->CH{pwm_set.ch}_CNTRL = 0xC00;\n\n"
                 f"    /* Запись значений в регистры CCR */\n"
                 f"    MDR_TIMER{pwm_set.tmr}->CCR{pwm_set.ch} = ccr;\n\n"
                 f"    /* Настройка выхода {pwm_set.ch} канала таймера {pwm_set.tmr} */\n"
                 f"    MDR_TIMER{pwm_set.tmr}->CH{pwm_set.ch}_CNTRL1 = {hex(cntrl1)}; // {bin(cntrl1)}\n\n"
                 f"    /* Настройка и запуск таймера {pwm_set.tmr} */\n"
                 f"    MDR_TIMER{pwm_set.tmr}->PSG = psg;\n"
                 f"    MDR_TIMER{pwm_set.tmr}->ARR = arr;\n"
                 f"    MDR_TIMER{pwm_set.tmr}->CNTRL |= 1;\n\n"
                 "    while (1) { }\n"
                 "}\n"
                 )

        return code
