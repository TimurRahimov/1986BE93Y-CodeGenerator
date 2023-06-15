from PySide6.QtWidgets import QMainWindow

from dialogs import CodeDialog
from ui import Ui_MainWindow


class Malakhanov(QMainWindow):

    port_settings = {
        "pin": list(map(str, range(16))),
        "port": [
            "A", "B", "C", "D", "E", "F"
        ]
    }

    unit_settings = {
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
        }
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

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @staticmethod
    def show_code(with_func: str = "", with_reg: str = ""):
        code_dialog = CodeDialog()
        code_dialog.ui.textBrowser_func.setText(with_func)
        code_dialog.ui.textBrowser_reg.setText(with_reg)
        code_dialog.exec()

    def __fill_combo_boxes(self):
        pass

    def __connect_signals(self):
        pass
