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
