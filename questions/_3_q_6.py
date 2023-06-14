from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QCheckBox, QPushButton

from dialogs import ImageDialog
from questions import Q5


class Q6(Q5):

    def __init__(self):
        super().__init__()
        self.__6_connect_signals()

    def __6_connect_signals(self):
        self.ui.checkBox_6_hsi.stateChanged.connect(self.__6_unlock_options)
        self.ui.checkBox_6_lsi.stateChanged.connect(self.__6_unlock_options)
        self.ui.pushButton_6_show_lsi.clicked.connect(self.__6_show_image)
        self.ui.pushButton_6_show_hsi.clicked.connect(self.__6_show_image)
        self.ui.submitButton_6.clicked.connect(self.__6_submit_handler)

    def __6_unlock_options(self):
        sender: QCheckBox = self.sender()
        name = sender.objectName().split('_')[-1]
        if sender.isChecked():
            self.ui.__dict__[f'pushButton_6_show_{name}'].setEnabled(True)
            self.ui.__dict__[f'lineEdit_6_{name}trim'].setEnabled(True)
        else:
            self.ui.__dict__[f'pushButton_6_show_{name}'].setEnabled(False)
            self.ui.__dict__[f'lineEdit_6_{name}trim'].setEnabled(False)

    def __6_show_image(self):
        sender: QPushButton = self.sender()
        name = sender.objectName().split('_')[-1]

        image_dialog = ImageDialog()

        if name == 'lsi':
            pixmap = QPixmap(u":/img/LSITRIM")
            image_dialog.ui.image_label.setPixmap(pixmap)
            image_dialog.ui.image_label.resize(pixmap.width(), pixmap.height())
            image_dialog.resize(pixmap.width(), pixmap.height())
        else:
            pixmap = QPixmap(u":/img/HSITRIM")
            image_dialog.ui.image_label.setPixmap(QPixmap(u":/img/HSITRIM"))
            image_dialog.ui.image_label.resize(pixmap.width(), pixmap.height())
            image_dialog.resize(pixmap.width(), pixmap.height())

        image_dialog.exec()

    def __6_submit_handler(self):
        lsi = self.ui.checkBox_6_lsi.isChecked()
        hsi = self.ui.checkBox_6_hsi.isChecked()
        lsitrim = self.ui.lineEdit_6_lsitrim.text() if lsi else None
        hsitrim = self.ui.lineEdit_6_hsitrim.text() if hsi else None

        func = self.__6_create_func_code(lsitrim, hsitrim)
        reg = self.__6_create_reg_code(lsitrim, hsitrim)

        self.show_code(with_func=func, with_reg=reg)

    def __6_create_func_code(self, lsitrim: str = None, hsitrim: str = None) -> str:
        code = ("""#include "MDR32F9Qx_port.h" \n"""
                """#include "MDR32F9Qx_rst_clk.h" \n\n """)

        code += "int main(void) {\n"
        if lsitrim:
            code += f"    RST_CLK_LSIadjust({lsitrim});\n"

        if hsitrim:
            code += f"    RST_CLK_HSIadjust({hsitrim});\n"

        code += ("\n    while(1) { }\n"
                 "}\n")
        return code

    def __6_create_reg_code(self, lsitrim: str = None, hsitrim: str = None) -> str:
        code = """#include "MDR32Fx.h" \n\n"""
        code += "int main(void) {\n"
        if lsitrim:
            code += ("    uint32_t lsi_temp;\n"
                     "    lsi_temp = MDR_BKP->REG_0F;\n"
                     "    lsi_temp &= ~((uint32_t)(0x1F << 16)); // Очистить биты LSITRIM [4:0]\n"
                     f"    lsi_temp |= (uint32_t) {lsitrim} << 16;\n"
                     f"    MDR_BKP->REG_0F = lsi_temp;\n\n")

        if hsitrim:
            code += ("    uint32_t hsi_temp;\n"
                     "    hsi_temp = MDR_BKP->REG_0F;\n"
                     "    hsi_temp &= ~((uint32_t)(0x3F << 24)); // Очистить биты HSITRIM [5:0]\n"
                     f"    hsi_temp |= (uint32_t) {hsitrim} << 24;\n"
                     f"    MDR_BKP->REG_0F = hsi_temp;\n\n")

        code += ("    while(1) { }\n"
                 "}\n")
        return code
