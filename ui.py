# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 761)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout = QGridLayout(self.tab_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.label = QLabel(self.tab_12)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 100)
        self.label_2 = QLabel(self.tab_12)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.comboBox_12_port = QComboBox(self.tab_12)
        self.comboBox_12_port.setObjectName(u"comboBox_12_port")
        self.comboBox_12_port.setMinimumSize(QSize(500, 0))

        self.verticalLayout.addWidget(self.comboBox_12_port, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.tab_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.comboBox_12_pin = QComboBox(self.tab_12)
        self.comboBox_12_pin.setObjectName(u"comboBox_12_pin")
        self.comboBox_12_pin.setMinimumSize(QSize(500, 0))

        self.verticalLayout.addWidget(self.comboBox_12_pin, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_12_oe = QCheckBox(self.tab_12)
        self.checkBox_12_oe.setObjectName(u"checkBox_12_oe")
        self.checkBox_12_oe.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_12_oe)

        self.comboBox_12_oe = QComboBox(self.tab_12)
        self.comboBox_12_oe.setObjectName(u"comboBox_12_oe")
        self.comboBox_12_oe.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_12_oe.sizePolicy().hasHeightForWidth())
        self.comboBox_12_oe.setSizePolicy(sizePolicy1)
        self.comboBox_12_oe.setMinimumSize(QSize(0, 0))
        self.comboBox_12_oe.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_2.addWidget(self.comboBox_12_oe)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_12_func = QCheckBox(self.tab_12)
        self.checkBox_12_func.setObjectName(u"checkBox_12_func")
        self.checkBox_12_func.setAcceptDrops(False)
        self.checkBox_12_func.setChecked(False)
        self.checkBox_12_func.setAutoRepeat(False)
        self.checkBox_12_func.setAutoExclusive(False)
        self.checkBox_12_func.setTristate(False)

        self.horizontalLayout_3.addWidget(self.checkBox_12_func)

        self.comboBox_12_func = QComboBox(self.tab_12)
        self.comboBox_12_func.setObjectName(u"comboBox_12_func")
        self.comboBox_12_func.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_12_func.sizePolicy().hasHeightForWidth())
        self.comboBox_12_func.setSizePolicy(sizePolicy2)
        self.comboBox_12_func.setMinimumSize(QSize(0, 0))
        self.comboBox_12_func.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_12_func)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_12_func = QLineEdit(self.tab_12)
        self.lineEdit_12_func.setObjectName(u"lineEdit_12_func")
        self.lineEdit_12_func.setEnabled(False)
        self.lineEdit_12_func.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_12_func.setAlignment(Qt.AlignCenter)
        self.lineEdit_12_func.setClearButtonEnabled(True)

        self.horizontalLayout_20.addWidget(self.lineEdit_12_func)

        self.pushButton_12_func = QPushButton(self.tab_12)
        self.pushButton_12_func.setObjectName(u"pushButton_12_func")
        self.pushButton_12_func.setEnabled(False)

        self.horizontalLayout_20.addWidget(self.pushButton_12_func)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.func_label_12 = QLabel(self.tab_12)
        self.func_label_12.setObjectName(u"func_label_12")
        self.func_label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.func_label_12)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_12_analog = QCheckBox(self.tab_12)
        self.checkBox_12_analog.setObjectName(u"checkBox_12_analog")

        self.horizontalLayout_4.addWidget(self.checkBox_12_analog)

        self.comboBox_12_analog = QComboBox(self.tab_12)
        self.comboBox_12_analog.setObjectName(u"comboBox_12_analog")
        self.comboBox_12_analog.setEnabled(False)
        self.comboBox_12_analog.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.comboBox_12_analog)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_12_pull_down = QCheckBox(self.tab_12)
        self.checkBox_12_pull_down.setObjectName(u"checkBox_12_pull_down")

        self.horizontalLayout_5.addWidget(self.checkBox_12_pull_down)

        self.checkBox_12_pull_up = QCheckBox(self.tab_12)
        self.checkBox_12_pull_up.setObjectName(u"checkBox_12_pull_up")

        self.horizontalLayout_5.addWidget(self.checkBox_12_pull_up)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_12_pd_open = QCheckBox(self.tab_12)
        self.checkBox_12_pd_open.setObjectName(u"checkBox_12_pd_open")

        self.horizontalLayout_7.addWidget(self.checkBox_12_pd_open)

        self.checkBox_12_shm = QCheckBox(self.tab_12)
        self.checkBox_12_shm.setObjectName(u"checkBox_12_shm")

        self.horizontalLayout_7.addWidget(self.checkBox_12_shm)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_12_pwr = QCheckBox(self.tab_12)
        self.checkBox_12_pwr.setObjectName(u"checkBox_12_pwr")

        self.horizontalLayout_9.addWidget(self.checkBox_12_pwr)

        self.comboBox_12_pwr = QComboBox(self.tab_12)
        self.comboBox_12_pwr.setObjectName(u"comboBox_12_pwr")
        self.comboBox_12_pwr.setEnabled(False)
        self.comboBox_12_pwr.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.comboBox_12_pwr)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_12_gfen = QCheckBox(self.tab_12)
        self.checkBox_12_gfen.setObjectName(u"checkBox_12_gfen")

        self.horizontalLayout_6.addWidget(self.checkBox_12_gfen)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.submitButton_12 = QPushButton(self.tab_12)
        self.submitButton_12.setObjectName(u"submitButton_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.submitButton_12.sizePolicy().hasHeightForWidth())
        self.submitButton_12.setSizePolicy(sizePolicy3)
        self.submitButton_12.setMinimumSize(QSize(500, 50))
        self.submitButton_12.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_12.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.submitButton_12, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_12, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_2 = QGridLayout(self.tab_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.label_7 = QLabel(self.tab_11)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 100)
        self.label_8 = QLabel(self.tab_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.comboBox_5_port = QComboBox(self.tab_11)
        self.comboBox_5_port.setObjectName(u"comboBox_5_port")
        self.comboBox_5_port.setMinimumSize(QSize(500, 0))
        self.comboBox_5_port.setEditable(False)

        self.verticalLayout_6.addWidget(self.comboBox_5_port, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.tab_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.comboBox_5_pin = QComboBox(self.tab_11)
        self.comboBox_5_pin.setObjectName(u"comboBox_5_pin")
        self.comboBox_5_pin.setMinimumSize(QSize(500, 0))

        self.verticalLayout_6.addWidget(self.comboBox_5_pin, 0, Qt.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, 0)
        self.label_10 = QLabel(self.tab_11)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_16.addWidget(self.label_10)

        self.lineEdit_5_time = QLineEdit(self.tab_11)
        self.lineEdit_5_time.setObjectName(u"lineEdit_5_time")
        self.lineEdit_5_time.setMinimumSize(QSize(0, 0))
        self.lineEdit_5_time.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_5_time.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_time.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.lineEdit_5_time)

        self.comboBox_5_time_unit = QComboBox(self.tab_11)
        self.comboBox_5_time_unit.setObjectName(u"comboBox_5_time_unit")

        self.horizontalLayout_16.addWidget(self.comboBox_5_time_unit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, -1, -1, 0)
        self.label_11 = QLabel(self.tab_11)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_17.addWidget(self.label_11)

        self.lineEdit_5_freq = QLineEdit(self.tab_11)
        self.lineEdit_5_freq.setObjectName(u"lineEdit_5_freq")
        self.lineEdit_5_freq.setMinimumSize(QSize(0, 0))
        self.lineEdit_5_freq.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_5_freq.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_freq.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_5_freq)

        self.comboBox_5_freq_unit = QComboBox(self.tab_11)
        self.comboBox_5_freq_unit.setObjectName(u"comboBox_5_freq_unit")

        self.horizontalLayout_17.addWidget(self.comboBox_5_freq_unit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, 0)
        self.label_12 = QLabel(self.tab_11)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_18.addWidget(self.label_12)

        self.comboBox_5_isr = QComboBox(self.tab_11)
        self.comboBox_5_isr.setObjectName(u"comboBox_5_isr")

        self.horizontalLayout_18.addWidget(self.comboBox_5_isr)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, -1, -1, 0)
        self.checkBox_5_lsi = QCheckBox(self.tab_11)
        self.checkBox_5_lsi.setObjectName(u"checkBox_5_lsi")

        self.horizontalLayout_19.addWidget(self.checkBox_5_lsi)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.submitButton_5 = QPushButton(self.tab_11)
        self.submitButton_5.setObjectName(u"submitButton_5")
        sizePolicy3.setHeightForWidth(self.submitButton_5.sizePolicy().hasHeightForWidth())
        self.submitButton_5.setSizePolicy(sizePolicy3)
        self.submitButton_5.setMinimumSize(QSize(500, 50))
        self.submitButton_5.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_5.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.submitButton_5, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_11, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(25)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_16)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 100)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(50, -1, 50, 0)
        self.checkBox_6_lsi = QCheckBox(self.tab_3)
        self.checkBox_6_lsi.setObjectName(u"checkBox_6_lsi")
        self.checkBox_6_lsi.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_23.addWidget(self.checkBox_6_lsi)

        self.label_6_lsi = QLabel(self.tab_3)
        self.label_6_lsi.setObjectName(u"label_6_lsi")
        self.label_6_lsi.setEnabled(True)
        self.label_6_lsi.setMaximumSize(QSize(100, 16777215))
        self.label_6_lsi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_6_lsi)

        self.lineEdit_6_lsitrim = QLineEdit(self.tab_3)
        self.lineEdit_6_lsitrim.setObjectName(u"lineEdit_6_lsitrim")
        self.lineEdit_6_lsitrim.setEnabled(False)
        self.lineEdit_6_lsitrim.setMinimumSize(QSize(0, 0))
        self.lineEdit_6_lsitrim.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_6_lsitrim.setAlignment(Qt.AlignCenter)
        self.lineEdit_6_lsitrim.setClearButtonEnabled(True)

        self.horizontalLayout_23.addWidget(self.lineEdit_6_lsitrim)

        self.pushButton_6_show_lsi = QPushButton(self.tab_3)
        self.pushButton_6_show_lsi.setObjectName(u"pushButton_6_show_lsi")
        self.pushButton_6_show_lsi.setEnabled(False)

        self.horizontalLayout_23.addWidget(self.pushButton_6_show_lsi)


        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(50, -1, 50, 0)
        self.checkBox_6_hsi = QCheckBox(self.tab_3)
        self.checkBox_6_hsi.setObjectName(u"checkBox_6_hsi")
        self.checkBox_6_hsi.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_24.addWidget(self.checkBox_6_hsi)

        self.label_6_hsi = QLabel(self.tab_3)
        self.label_6_hsi.setObjectName(u"label_6_hsi")
        self.label_6_hsi.setEnabled(True)
        self.label_6_hsi.setMaximumSize(QSize(100, 16777215))
        self.label_6_hsi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_6_hsi)

        self.lineEdit_6_hsitrim = QLineEdit(self.tab_3)
        self.lineEdit_6_hsitrim.setObjectName(u"lineEdit_6_hsitrim")
        self.lineEdit_6_hsitrim.setEnabled(False)
        self.lineEdit_6_hsitrim.setMinimumSize(QSize(0, 0))
        self.lineEdit_6_hsitrim.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_6_hsitrim.setAlignment(Qt.AlignCenter)
        self.lineEdit_6_hsitrim.setClearButtonEnabled(True)

        self.horizontalLayout_24.addWidget(self.lineEdit_6_hsitrim)

        self.pushButton_6_show_hsi = QPushButton(self.tab_3)
        self.pushButton_6_show_hsi.setObjectName(u"pushButton_6_show_hsi")
        self.pushButton_6_show_hsi.setEnabled(False)

        self.horizontalLayout_24.addWidget(self.pushButton_6_show_hsi)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.submitButton_6 = QPushButton(self.tab_3)
        self.submitButton_6.setObjectName(u"submitButton_6")
        sizePolicy3.setHeightForWidth(self.submitButton_6.sizePolicy().hasHeightForWidth())
        self.submitButton_6.setSizePolicy(sizePolicy3)
        self.submitButton_6.setMinimumSize(QSize(500, 50))
        self.submitButton_6.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_6.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.submitButton_6, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget.addTab(self.tab_10, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u043e\u0440\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u043d", None))
        self.checkBox_12_oe.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0438 (\u0432\u044b\u0445\u043e\u0434, \u0432\u0445\u043e\u0434)", None))
        self.checkBox_12_func.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0432\u044b\u0432\u043e\u0434\u0430 \u043f\u043e\u0440\u0442\u0430 (\u0446\u0438\u0444\u0440\u043e\u0432\u043e\u0439 \u0432\u0432\u043e\u0434-\u0432\u044b\u0432\u043e\u0434, \u043e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0444-\u0446\u0438\u044f, \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0430\u044f ...", None))
        self.pushButton_12_func.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0440\u0435\u0436\u0438\u043c \u0432\u044b\u0432\u043e\u0434\u0430 \u043f\u043e\u0440\u0442\u0430", None))
        self.func_label_12.setText("")
        self.checkBox_12_analog.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e\u0440\u0442\u0430: \u0430\u043d\u0430\u043b\u043e\u0433\u043e\u0432\u044b\u0439, \u0446\u0438\u0444\u0440\u043e\u0432\u043e\u0439", None))
        self.checkBox_12_pull_down.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0438\u0441\u0442\u043e\u0440, \u043f\u043e\u0434\u0442\u044f\u0433\u0438\u0432\u0430\u044e\u0449\u0438\u0439 \u043a \"\u0437\u0435\u043c\u043b\u0435\"", None))
        self.checkBox_12_pull_up.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0438\u0441\u0442\u043e\u0440, \u043f\u043e\u0434\u0442\u044f\u0433\u0438\u0432\u0430\u044e\u0449\u0438\u0439 \u043a \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044e \u044d\u043b. \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.checkBox_12_pd_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u0441\u0442\u043e\u043a", None))
        self.checkBox_12_shm.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0438\u0433\u0433\u0435\u0440 \u0428\u043c\u0438\u0434\u0442\u0430", None))
        self.checkBox_12_pwr.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c\u044e \u0444\u0440\u043e\u043d\u0442\u043e\u0432 \u0433\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u043c\u044b\u0445 \u0441\u0438\u0433\u043d\u0430\u043b\u043e\u0432", None))
        self.checkBox_12_gfen.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.submitButton_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u043e\u0440\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SysTick", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u043d", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u043a\u0442\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430 \u041c\u041a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u043f\u0440\u0435\u0440\u044b\u0432\u0430\u043d\u0438\u0439 (\u0424\u041e\u041f)", None))
        self.checkBox_5_lsi.setText(QCoreApplication.translate("MainWindow", u"LSI \u043a\u0430\u043a \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0441\u0438\u043d\u0445\u0440\u043e\u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.submitButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"SysTick", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"LSI / HSI", None))
        self.checkBox_6_lsi.setText(QCoreApplication.translate("MainWindow", u"LSI", None))
        self.label_6_lsi.setText(QCoreApplication.translate("MainWindow", u"LSITRIM", None))
        self.pushButton_6_show_lsi.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.checkBox_6_hsi.setText(QCoreApplication.translate("MainWindow", u"HSI", None))
        self.label_6_hsi.setText(QCoreApplication.translate("MainWindow", u"HSITRIM", None))
        self.pushButton_6_show_hsi.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.submitButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"LSI / HSI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"LSE / HSE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"CPU_CLK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"USB_CLK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"ADC_CLK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"ADC_CLK + HCI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

