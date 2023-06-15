import sys
from PySide6.QtWidgets import QApplication

from questions import LastWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LastWindow()
    window.show()
    app.exec()

# from openpyxl import load_workbook
# sheets = ['Лист1', 'Таймер', 'Шим']
#
#
# wb = load_workbook('data/Raschety.xlsx')
# wb['Шим']['D8'].value = 8000  # HCLK
# wb['Шим']['E8'].value = 0.515  # период
# wb['Шим']['F8'].value = 0.2  # импульс
# wb.save('data/Raschety.xlsx')
#
# wb = load_workbook('data/Raschety.xlsx', data_only=True)
# mmin = wb['Шим']['D11'].value or 0
# psgmin = wb['Шим']['E11'].value or 0
#
# wb = load_workbook('data/Raschety.xlsx')
# wb['Шим']['D14'].value = int(mmin) + 1  # M
# wb['Шим']['E14'].value = int(psgmin) + 1  # PSG
# wb.save('data/Raschety.xlsx')
#
# wb = load_workbook('data/Raschety.xlsx', data_only=True)
# m = wb['Шим']['D14'].value
# psg = wb['Шим']['E14'].value
# arr = wb['Шим']['D17'].value
# ccry = wb['Шим']['F17'].value
#
# pass
