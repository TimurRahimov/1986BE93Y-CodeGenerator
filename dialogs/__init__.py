from PySide6.QtWidgets import QDialog

from .code_dialog_ui import Ui_CodeDialog
from .image_dialog_ui import Ui_ImageDialog


class CodeDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_CodeDialog()
        self.ui.setupUi(self)


class ImageDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)
