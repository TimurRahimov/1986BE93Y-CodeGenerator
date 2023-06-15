from PySide6.QtWidgets import QComboBox, QCheckBox

from questions import Malakhanov

settings = {
    "oe": {
        "ввод": ("PORT_OE_IN", 0),
        "вывод": ("PORT_OE_OUT", 1)
    },
    "func": {
        "цифровой ввод-вывод": ("PORT_FUNC_PORT", 0),
        "основная функция": ("PORT_FUNC_MAIN", 1),
        "альтернативная функция": ("PORT_FUNC_ALTER", 2),
        "переопределенная функция": ("PORT_FUNC_OVERRID", 3)
    },
    "analog": {
        "аналоговый": ("PORT_MODE_ANALOG", 0),
        "цифровой": ("PORT_MODE_DIGITAL", 1)
    },
    "pwr": {
        "передатчик отключен": ("PORT_OUTPUT_OFF", 0),
        "длительность фронта 100 нс": ("PORT_SPEED_SLOW", 1),
        "длительность фронта 20 нс": ("PORT_SPEED_FAST", 2),
        "длительность фронта 10 нс (макс. быстрый)": ("PORT_SPEED_MAXFAST", 3)
    }
}

checkbox_settings = {
    "pd_open": {
        True: "PORT_PD_OPEN",
        False: "PORT_PD_DRIVER"
    },
    "shm": {
        True: "PORT_PD_SHM_ON",
        False: "PORT_PD_SHM_OFF"
    }
    ,
    "pull_down": {
        True: "PORT_PULL_DOWN_ON",
        False: "PORT_PULL_DOWN_OFF"
    },
    "pull_up": {
        True: "PORT_PULL_UP_ON",
        False: "PORT_PULL_UP_OFF"
    },
    "gfen": {
        True: ("PORT_GFEN_ON", 1),
        False: ("PORT_GFEN_OFF", 0)
    }
}

port_struct_fields = {
    "oe": ("PORT_OE", "OE"),
    "func": ("PORT_FUNC", "FUNC"),
    "analog": ("PORT_MODE", "ANALOG"),
    "pull_down": ("PORT_PULL_DOWN", None),
    "pull_up": ("PORT_PULL_UP", None),
    "pd_open": ("PORT_PD", None),
    "shm": ("PORT_PD_SHM", None),
    "pwr": ("PORT_SPEED", "PWR"),
    "gfen": ("PORT_GFEN", "GFEN")
}

port_funcs = {
    "A": {
        "0": {
            "EXT_INT1": 2
        },
        "1": {
            "TMR1_CH1": 2,
            "TMR2_CH1": 3
        },
        "2": {
            "TMR1_CH1N": 2,
            "TMR2_CH1N": 3
        },
        "3": {
            "TMR1_CH2": 2,
            "TMR2_CH2": 3
        },
        "4": {
            "TMR1_CH2N": 2,
            "TMR2_CH2N": 3
        },
        "5": {
            "TMR1_CH3": 2,
            "TMR2_CH3": 3
        },
        "6": {
            "CAN1_TX": 2,
            "UART1_RXD": 3
        },
        "7": {
            "CAN1_RX": 2,
            "UART1_TXD": 3
        }
    },
    "B": {
        "0": {
            "TMR3_CH1": 2,
            "UART1_RXD": 3
        },
        "1": {
            "TMR3_CH1N": 2,
            "UART1_TXD": 3
        },
        "2": {
            "TMR3_CH2": 2,
            "CAN1_TX": 3
        },
        "3": {
            "TMR3_CH2N": 2,
            "CAN1_RX": 3
        },
        "4": {
            "TMR3_BLK": 2,
            "TMR3_ETR": 3
        },
        "5": {
            "UART1_RXD": 2,
            "TMR3_CH3": 3
        },
        "6": {
            "UART1_TXD": 2,
            "TMR3_CH3N": 3
        }
    },
    "C": {
        "0": {
            "SCL1": 2,
            "SSP2_FSS": 3
        }
    },
    "D": {
        "0": {
            "TMR1_CH1N": 1,
            "UART2_RXD": 2,
            "TMR3_CH1": 3
        },
        "1": {
            "TMR1_CH1": 1,
            "UART2_TXD": 2,
            "TMR3_CH1N": 3
        },
        "2": {
            "SSP2_RXD": 2,
            "TMR3_CH2": 3
        },
        "3": {
            "SSP2_FSS": 2,
            "TMR3_CH2N": 3
        }
    },
    "E": {
        "0": {
            "TMR2_CH1": 2,
            "CAN1_RX": 3
        },
        "2": {
            "TMR2_CH3": 2,
            "TMR3_CH1": 3
        },
        "3": {
            "TMR2_CH3N": 2,
            "TMR3_CH1N": 3
        },
        "6": {
            "CAN2_RX": 2,
            "TMR3_CH3": 3
        }
    },
    "F": {
        "0": {
            "SSP1TXD": 2,
            "UART2_RXD": 3
        },
        "1": {
            "SSP1CLK": 2,
            "UART2_TXD": 3
        },
        "2": {
            "SSP1FSS": 2,
            "CAN2_RX": 3
        },
        "3": {
            "SSP1RXD": 2,
            "CAN2_TX": 3
        },
        "4": {},
        "5": {},
    }
}

pclk = {
    "RST_CLK": 4,
    "UART1": 6,
    "UART2": 7,
    "TIMER1": 14,
    "TIMER2": 15,
    "TIMER3": 16,
    "ADC": 17,
    "DAC": 18,
    "PORTA": 21,
    "PORTB": 22,
    "PORTC": 23,
    "PORTD": 24,
    "PORTE": 25,
    "BKP": 27,
    "PORTF": 29,
}


class Q12(Malakhanov):

    def __init__(self):
        super().__init__()
        self.__12_fill_combo_boxes()
        self.__12_connect_signals()

    def __12_fill_combo_boxes(self):
        for _ in settings:
            for item in settings[_]:
                self.ui.__dict__["comboBox_12_" + _].addItem(item)

        for _ in self.port_settings:
            for item in self.port_settings[_]:
                self.ui.__dict__["comboBox_12_" + _].addItem(item)

    def __12_connect_signals(self):
        self.ui.submitButton_12.clicked.connect(self.__12_submit_handler)
        self.ui.pushButton_12_func.clicked.connect(self.__12_func_handler)
        for _ in settings:
            self.ui.__dict__["checkBox_12_" + _].stateChanged.connect(self.__12_unlock_options)

    def __12_submit_handler(self):
        func = self.__12_create_func_code()
        reg = self.__12_create_reg_code()
        self.show_code(with_func=func, with_reg=reg)

    def __12_func_handler(self):
        port = self.ui.comboBox_12_port.currentText()
        pin = self.ui.comboBox_12_pin.currentText()
        name = self.ui.lineEdit_12_func.text().upper()

        try:
            pos = port_funcs[port][pin][name]
        except KeyError:
            self.ui.func_label_12.setText("Вы ввели неверную функцию")
            return

        for func_name, func in settings['func'].items():
            if func[1] == pos:
                self.ui.func_label_12.setText(func_name)

        self.ui.comboBox_12_func.setCurrentIndex(pos)

    def __12_create_func_code(self) -> str:
        port = self.ui.comboBox_12_port.currentText()
        pin = self.ui.comboBox_12_pin.currentText()

        code = ("""#include "MDR32F9Qx_port.h"\n"""
                """#include "MDR32F9Qx_rst_clk.h" \n\n""")

        code += "int main(void){\n"
        code += "    static PORT_InitTypeDef PortInit;\n"
        code += f"    RST_CLK_PCLKcmd(RST_CLK_PCLK_PORT{port}, ENABLE);\n"

        try:
            for func, func_num in port_funcs[port][pin].items():
                if func_num == self.ui.comboBox_12_func.currentIndex():
                    if func.startswith('TMR'):
                        code += f"    RST_CLK_PCLKcmd(RST_CLK_PCLK_TIMER{func[3]}, ENABLE);\n"
        except KeyError:
            pass

        code += f"    PORT_DeInit(MDR_PORT{port});\n"
        code += f"    PortInit.PORT_Pin = PORT_Pin_{pin};\n"

        for _ in settings:
            box: QComboBox = self.ui.__dict__["comboBox_12_" + _]
            if box.isEnabled():
                code += f"    PortInit.{port_struct_fields[_][0]} = {settings[_][box.currentText()][0]}; \n"

        for _ in checkbox_settings:
            box: QCheckBox = self.ui.__dict__["checkBox_12_" + _]
            if box.isChecked():
                code += f"    PortInit.{port_struct_fields[_][0]} = {checkbox_settings[_][True]}; \n"

        code += (f"    PORT_Init(MDR_PORT{port}, &PortInit);\n"
                 "\n"
                 "    while(1) { }\n"
                 "}\n")
        return code

    def __12_create_reg_code(self):
        port = self.ui.comboBox_12_port.currentText()
        pin = int(self.ui.comboBox_12_pin.currentText())

        code = """#include "MDR32Fx.h" \n\n"""
        code += "int main(void){\n"

        per_clock = [f"(1 << {pclk[f'PORT{port}']})"]

        try:
            for func, func_num in port_funcs[port][str(pin)].items():
                if func_num == self.ui.comboBox_12_func.currentIndex():
                    if func.startswith('TMR'):
                        per_clock.append(f"(1 << {pclk[f'TIMER{func[3]}']})")
        except KeyError:
            pass

        code += f"    MDR_RST_CLK->PER_CLOCK |= {' | '.join(per_clock)};\n"

        for _ in settings:
            box: QComboBox = self.ui.__dict__["comboBox_12_" + _]
            if box.isEnabled():
                code += f"    MDR_PORT{port}->{port_struct_fields[_][1]} = ({settings[_][box.currentText()][1]} << {pin if _ != 'func' else pin * 2});\n"

        pull_down = self.ui.checkBox_12_pull_down.isChecked()
        pull_up = self.ui.checkBox_12_pull_up.isChecked()
        gfen = self.ui.checkBox_12_gfen.isChecked()
        pd_open = self.ui.checkBox_12_pd_open.isChecked()
        shm = self.ui.checkBox_12_shm.isChecked()

        if pull_up and pull_down:
            code += f"    MDR_PORT{port}->PULL = (1 << {pin}) | (1 << {pin + 16});\n"
        elif pull_up:
            code += f"    MDR_PORT{port}->PULL = (1 << {pin + 16});\n"
        elif pull_down:
            code += f"    MDR_PORT{port}->PULL = (1 << {pin});\n"

        if pd_open and shm:
            code += f"    MDR_PORT{port}->PD = (1 << {pin}) | (1 << {pin + 16});\n"
        elif pd_open:
            code += f"    MDR_PORT{port}->PD = (1 << {pin + 16});\n"
        elif shm:
            code += f"    MDR_PORT{port}->PD = (1 << {pin});\n"
        if gfen:
            code += f"    MDR_PORT{port}->GFEN = (1 << {pin});\n"

        code += ("\n    while(1) { }\n"
                 "}\n")

        return code

    def __12_unlock_options(self):
        sender: QCheckBox = self.sender()
        option = sender.objectName().split("_")[-1]
        self.ui.__dict__["comboBox_12_" + option].setEnabled(True if sender.isChecked() else False)
        if option == 'func':
            self.ui.lineEdit_12_func.setEnabled(True if sender.isChecked() else False)
            self.ui.pushButton_12_func.setEnabled(True if sender.isChecked() else False)
