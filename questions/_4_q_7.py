from PySide6.QtWidgets import QComboBox, QCheckBox

from questions import Q6

settings = {
    "lse": {
        "Выключить LSE": "RST_CLK_LSE_OFF",
        "Включить LSE": "RST_CLK_LSE_ON",
        "Включить, но вместо LSE использовать внешний генератор": "RST_CLK_LSE_Bypass"
    },
    "hse": {
        "Выключить HSE": "RST_CLK_HSE_OFF",
        "Включить HSE": "RST_CLK_HSE_ON",
        "Включить, но вместо HSE использовать внешний генератор": "RST_CLK_HSE_Bypass"
    }
}


class Q7(Q6):

    def __init__(self):
        super().__init__()
        self.__7_fill_combo_boxes()
        self.__7_connect_signals()

    def __7_fill_combo_boxes(self):
        for _ in settings:
            for item in settings[_]:
                self.ui.__dict__[f'comboBox_7_{_}'].addItem(item)

    def __7_connect_signals(self):
        self.ui.checkBox_7_hse.stateChanged.connect(self.__7_unlock_options)
        self.ui.checkBox_7_lse.stateChanged.connect(self.__7_unlock_options)
        self.ui.submitButton_7.clicked.connect(self.__7_submit_handler)

    def __7_unlock_options(self):
        sender: QCheckBox = self.sender()
        name = sender.objectName().split('_')[-1]
        if sender.isChecked():
            self.ui.__dict__[f'comboBox_7_{name}'].setEnabled(True)
        else:
            self.ui.__dict__[f'comboBox_7_{name}'].setEnabled(False)

    def __7_submit_handler(self):
        lse = self.ui.checkBox_7_lse.isChecked()
        hse = self.ui.checkBox_7_hse.isChecked()

        lse_type = settings['lse'][self.ui.comboBox_7_lse.currentText()] if lse else None
        hse_type = settings['hse'][self.ui.comboBox_7_hse.currentText()] if hse else None

        func = self.__7_create_func_code(lse_type, hse_type)
        reg = self.__7_create_reg_code(lse_type, hse_type)
        self.show_code(with_func=func, with_reg=reg)

    def __7_create_func_code(self, lse_type: str = None, hse_type: str = None) -> str:
        code = ("""#include "MDR32F9Qx_port.h" \n"""
                """#include "MDR32F9Qx_rst_clk.h" \n\n """)

        code += "int main(void) {\n"

        if lse_type:
            code += f"    RST_CLK_LSEconfig({lse_type});\n"
            code += f"    if(RST_CLK_LSEstatus() == ERROR)\n"
            code += f"        RST_CLK_LSE_config(RST_CLK_LSE_OFF);\n"
            code += "    else { }\n\n"

        if hse_type:
            code += f"    RST_CLK_HSEconfig({hse_type});\n"
            code += f"    if(RST_CLK_HSEstatus() == ERROR)\n"
            code += f"        RST_CLK_HSE_config(RST_CLK_HSE_OFF);\n"
            code += "    else { }\n\n"

        code += ("    while(1) { }\n"
                 "}\n")
        return code

    def __7_create_reg_code(self, lse_type: str = None, hse_type: str = None) -> str:
        code = """#include "MDR32Fx.h" \n\n"""
        code += "int main(void) {\n"

        if lse_type:
            lse_type = lse_type.split('_')[-1]
            if lse_type == 'OFF':
                code += f"    MDR_RST_CLK->HS_CONTROL &= ~3; \n"
            if lse_type in ('ON', 'Bypass'):
                if lse_type == 'ON':
                    code += f"    MDR_RST_CLK->HS_CONTROL |= 1; \n"
                if lse_type == 'Bypass':
                    code += f"    MDR_RST_CLK->HS_CONTROL |= 3; \n"

                code += f"    if(!(MDR_BKP->REG_0F & 1 << 13))\n"
                code += f"        MDR_BKP->REG_0F &=~1;\n"
                code += "    else { }\n\n"

        if hse_type:
            hse_type = hse_type.split('_')[-1]
            if hse_type == 'OFF':
                code += f"    MDR_BKP->REG_0F &= ~3; \n"
            if hse_type in ('ON', 'Bypass'):
                if hse_type == 'ON':
                    code += f"    MDR_BKP->REG_0F |= 1; \n"
                if hse_type == 'Bypass':
                    code += f"    MDR_BKP->REG_0F |= 3; \n"

                code += f"    if(!(MDR_RST_CLK->CLOCK_STATUS & 4)) \n"
                code += f"        MDR_RST_CLK->HS_CONTROL &=~1; \n"
                code += "    else { } \n\n"

        code += ("    while(1) { }\n"
                 "}\n")
        return code
