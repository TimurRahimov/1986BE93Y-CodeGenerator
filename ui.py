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
        MainWindow.resize(823, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
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

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_4)

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
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(25)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.label_17 = QLabel(self.tab_4)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 100)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(50, -1, 50, 0)
        self.checkBox_7_lse = QCheckBox(self.tab_4)
        self.checkBox_7_lse.setObjectName(u"checkBox_7_lse")
        self.checkBox_7_lse.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.checkBox_7_lse)

        self.comboBox_7_lse = QComboBox(self.tab_4)
        self.comboBox_7_lse.setObjectName(u"comboBox_7_lse")
        self.comboBox_7_lse.setEnabled(False)

        self.horizontalLayout_25.addWidget(self.comboBox_7_lse)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(50, -1, 50, 0)
        self.checkBox_7_hse = QCheckBox(self.tab_4)
        self.checkBox_7_hse.setObjectName(u"checkBox_7_hse")
        self.checkBox_7_hse.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_26.addWidget(self.checkBox_7_hse)

        self.comboBox_7_hse = QComboBox(self.tab_4)
        self.comboBox_7_hse.setObjectName(u"comboBox_7_hse")
        self.comboBox_7_hse.setEnabled(False)

        self.horizontalLayout_26.addWidget(self.comboBox_7_hse)


        self.verticalLayout_12.addLayout(self.horizontalLayout_26)

        self.submitButton_7 = QPushButton(self.tab_4)
        self.submitButton_7.setObjectName(u"submitButton_7")
        sizePolicy3.setHeightForWidth(self.submitButton_7.sizePolicy().hasHeightForWidth())
        self.submitButton_7.setSizePolicy(sizePolicy3)
        self.submitButton_7.setMinimumSize(QSize(500, 50))
        self.submitButton_7.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_7.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.submitButton_7, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.gridLayout_4.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(25)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 20, -1, -1)
        self.label_18 = QLabel(self.tab_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_18)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 100)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.horizontalSpacer_8)

        self.label_5 = QLabel(self.tab_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_5)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, 0, 0)
        self.checkBox_8_nhse = QCheckBox(self.tab_5)
        self.checkBox_8_nhse.setObjectName(u"checkBox_8_nhse")
        self.checkBox_8_nhse.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_28.addWidget(self.checkBox_8_nhse)

        self.lineEdit_8_nhse = QLineEdit(self.tab_5)
        self.lineEdit_8_nhse.setObjectName(u"lineEdit_8_nhse")
        self.lineEdit_8_nhse.setEnabled(False)
        self.lineEdit_8_nhse.setMinimumSize(QSize(0, 0))
        self.lineEdit_8_nhse.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_8_nhse.setAlignment(Qt.AlignCenter)
        self.lineEdit_8_nhse.setClearButtonEnabled(True)

        self.horizontalLayout_28.addWidget(self.lineEdit_8_nhse)

        self.comboBox_8_nhse = QComboBox(self.tab_5)
        self.comboBox_8_nhse.setObjectName(u"comboBox_8_nhse")
        self.comboBox_8_nhse.setEnabled(False)

        self.horizontalLayout_28.addWidget(self.comboBox_8_nhse)


        self.verticalLayout_14.addLayout(self.horizontalLayout_28)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.horizontalSpacer_9)

        self.label_6 = QLabel(self.tab_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_6)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, -1, 0, 0)
        self.checkBox_8_freq = QCheckBox(self.tab_5)
        self.checkBox_8_freq.setObjectName(u"checkBox_8_freq")

        self.horizontalLayout_29.addWidget(self.checkBox_8_freq)

        self.lineEdit_8_freq = QLineEdit(self.tab_5)
        self.lineEdit_8_freq.setObjectName(u"lineEdit_8_freq")
        self.lineEdit_8_freq.setEnabled(False)
        self.lineEdit_8_freq.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_8_freq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.lineEdit_8_freq)

        self.comboBox_8_freq_unit = QComboBox(self.tab_5)
        self.comboBox_8_freq_unit.setObjectName(u"comboBox_8_freq_unit")
        self.comboBox_8_freq_unit.setEnabled(False)

        self.horizontalLayout_29.addWidget(self.comboBox_8_freq_unit)


        self.verticalLayout_14.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, -1, 0, 0)
        self.checkBox_8_main = QCheckBox(self.tab_5)
        self.checkBox_8_main.setObjectName(u"checkBox_8_main")

        self.horizontalLayout_30.addWidget(self.checkBox_8_main)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.label_13 = QLabel(self.tab_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(100, 16777215))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_13)

        self.lineEdit_8_num = QLineEdit(self.tab_5)
        self.lineEdit_8_num.setObjectName(u"lineEdit_8_num")
        self.lineEdit_8_num.setEnabled(False)
        self.lineEdit_8_num.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_8_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lineEdit_8_num)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.label_14 = QLabel(self.tab_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.label_14)

        self.lineEdit_8_denum = QLineEdit(self.tab_5)
        self.lineEdit_8_denum.setObjectName(u"lineEdit_8_denum")
        self.lineEdit_8_denum.setEnabled(False)
        self.lineEdit_8_denum.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_8_denum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_8_denum)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_30.addLayout(self.verticalLayout_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_30)

        self.submitButton_8 = QPushButton(self.tab_5)
        self.submitButton_8.setObjectName(u"submitButton_8")
        sizePolicy3.setHeightForWidth(self.submitButton_8.sizePolicy().hasHeightForWidth())
        self.submitButton_8.setSizePolicy(sizePolicy3)
        self.submitButton_8.setMinimumSize(QSize(500, 50))
        self.submitButton_8.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_8.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.submitButton_8, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)


        self.gridLayout_5.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_7 = QGridLayout(self.tab_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(25)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 20, -1, -1)
        self.label_32 = QLabel(self.tab_6)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setFont(font)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_32)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 100)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_10)

        self.label_33 = QLabel(self.tab_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_33)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, -1, 0, 0)
        self.checkBox_9_nhse = QCheckBox(self.tab_6)
        self.checkBox_9_nhse.setObjectName(u"checkBox_9_nhse")
        self.checkBox_9_nhse.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_36.addWidget(self.checkBox_9_nhse)

        self.lineEdit_9_nhse = QLineEdit(self.tab_6)
        self.lineEdit_9_nhse.setObjectName(u"lineEdit_9_nhse")
        self.lineEdit_9_nhse.setEnabled(False)
        self.lineEdit_9_nhse.setMinimumSize(QSize(0, 0))
        self.lineEdit_9_nhse.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_9_nhse.setAlignment(Qt.AlignCenter)
        self.lineEdit_9_nhse.setClearButtonEnabled(True)

        self.horizontalLayout_36.addWidget(self.lineEdit_9_nhse)

        self.comboBox_9_nhse = QComboBox(self.tab_6)
        self.comboBox_9_nhse.setObjectName(u"comboBox_9_nhse")
        self.comboBox_9_nhse.setEnabled(False)

        self.horizontalLayout_36.addWidget(self.comboBox_9_nhse)


        self.verticalLayout_16.addLayout(self.horizontalLayout_36)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_11)

        self.label_34 = QLabel(self.tab_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_34)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, -1, 0, 0)
        self.checkBox_9_freq = QCheckBox(self.tab_6)
        self.checkBox_9_freq.setObjectName(u"checkBox_9_freq")

        self.horizontalLayout_37.addWidget(self.checkBox_9_freq)

        self.lineEdit_9_freq = QLineEdit(self.tab_6)
        self.lineEdit_9_freq.setObjectName(u"lineEdit_9_freq")
        self.lineEdit_9_freq.setEnabled(False)
        self.lineEdit_9_freq.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_9_freq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.lineEdit_9_freq)

        self.comboBox_9_freq_unit = QComboBox(self.tab_6)
        self.comboBox_9_freq_unit.setObjectName(u"comboBox_9_freq_unit")
        self.comboBox_9_freq_unit.setEnabled(False)

        self.horizontalLayout_37.addWidget(self.comboBox_9_freq_unit)


        self.verticalLayout_16.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, -1, 0, 0)
        self.checkBox_9_main = QCheckBox(self.tab_6)
        self.checkBox_9_main.setObjectName(u"checkBox_9_main")

        self.horizontalLayout_38.addWidget(self.checkBox_9_main)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.label_35 = QLabel(self.tab_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(100, 16777215))
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_35)

        self.lineEdit_9_num = QLineEdit(self.tab_6)
        self.lineEdit_9_num.setObjectName(u"lineEdit_9_num")
        self.lineEdit_9_num.setEnabled(False)
        self.lineEdit_9_num.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_9_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit_9_num)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.label_36 = QLabel(self.tab_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.label_36)

        self.lineEdit_9_denum = QLineEdit(self.tab_6)
        self.lineEdit_9_denum.setObjectName(u"lineEdit_9_denum")
        self.lineEdit_9_denum.setEnabled(False)
        self.lineEdit_9_denum.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_9_denum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit_9_denum)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_38.addLayout(self.verticalLayout_4)


        self.verticalLayout_16.addLayout(self.horizontalLayout_38)

        self.submitButton_9 = QPushButton(self.tab_6)
        self.submitButton_9.setObjectName(u"submitButton_9")
        sizePolicy3.setHeightForWidth(self.submitButton_9.sizePolicy().hasHeightForWidth())
        self.submitButton_9.setSizePolicy(sizePolicy3)
        self.submitButton_9.setMinimumSize(QSize(500, 50))
        self.submitButton_9.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_9.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.submitButton_9, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.gridLayout_7.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_8 = QGridLayout(self.tab_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(25)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 20, -1, -1)
        self.label_37 = QLabel(self.tab_7)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_37)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 100)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_12)

        self.label_38 = QLabel(self.tab_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, -1, 0, 0)
        self.checkBox_10_nhse = QCheckBox(self.tab_7)
        self.checkBox_10_nhse.setObjectName(u"checkBox_10_nhse")
        self.checkBox_10_nhse.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_39.addWidget(self.checkBox_10_nhse)

        self.lineEdit_10_nhse = QLineEdit(self.tab_7)
        self.lineEdit_10_nhse.setObjectName(u"lineEdit_10_nhse")
        self.lineEdit_10_nhse.setEnabled(False)
        self.lineEdit_10_nhse.setMinimumSize(QSize(0, 0))
        self.lineEdit_10_nhse.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_10_nhse.setAlignment(Qt.AlignCenter)
        self.lineEdit_10_nhse.setClearButtonEnabled(True)

        self.horizontalLayout_39.addWidget(self.lineEdit_10_nhse)

        self.comboBox_10_nhse = QComboBox(self.tab_7)
        self.comboBox_10_nhse.setObjectName(u"comboBox_10_nhse")
        self.comboBox_10_nhse.setEnabled(False)

        self.horizontalLayout_39.addWidget(self.comboBox_10_nhse)


        self.verticalLayout_18.addLayout(self.horizontalLayout_39)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_13)

        self.label_39 = QLabel(self.tab_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, -1, 0, 0)
        self.checkBox_10_freq = QCheckBox(self.tab_7)
        self.checkBox_10_freq.setObjectName(u"checkBox_10_freq")

        self.horizontalLayout_40.addWidget(self.checkBox_10_freq)

        self.lineEdit_10_freq = QLineEdit(self.tab_7)
        self.lineEdit_10_freq.setObjectName(u"lineEdit_10_freq")
        self.lineEdit_10_freq.setEnabled(False)
        self.lineEdit_10_freq.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_10_freq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.lineEdit_10_freq)

        self.comboBox_10_freq_unit = QComboBox(self.tab_7)
        self.comboBox_10_freq_unit.setObjectName(u"comboBox_10_freq_unit")
        self.comboBox_10_freq_unit.setEnabled(False)

        self.horizontalLayout_40.addWidget(self.comboBox_10_freq_unit)


        self.verticalLayout_18.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, -1, 0, 0)
        self.checkBox_10_main = QCheckBox(self.tab_7)
        self.checkBox_10_main.setObjectName(u"checkBox_10_main")

        self.horizontalLayout_41.addWidget(self.checkBox_10_main)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.label_40 = QLabel(self.tab_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(100, 16777215))
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_40)

        self.lineEdit_10_num = QLineEdit(self.tab_7)
        self.lineEdit_10_num.setObjectName(u"lineEdit_10_num")
        self.lineEdit_10_num.setEnabled(False)
        self.lineEdit_10_num.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_10_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_10_num)


        self.verticalLayout_19.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.label_41 = QLabel(self.tab_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_14.addWidget(self.label_41)

        self.lineEdit_10_denum = QLineEdit(self.tab_7)
        self.lineEdit_10_denum.setObjectName(u"lineEdit_10_denum")
        self.lineEdit_10_denum.setEnabled(False)
        self.lineEdit_10_denum.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_10_denum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_10_denum)


        self.verticalLayout_19.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_41.addLayout(self.verticalLayout_19)


        self.verticalLayout_18.addLayout(self.horizontalLayout_41)

        self.submitButton_10 = QPushButton(self.tab_7)
        self.submitButton_10.setObjectName(u"submitButton_10")
        sizePolicy3.setHeightForWidth(self.submitButton_10.sizePolicy().hasHeightForWidth())
        self.submitButton_10.setSizePolicy(sizePolicy3)
        self.submitButton_10.setMinimumSize(QSize(500, 50))
        self.submitButton_10.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_10.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.submitButton_10, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.gridLayout_8.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_6 = QGridLayout(self.tab_10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(25)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.label_15 = QLabel(self.tab_10)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_15)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 100)
        self.label_19 = QLabel(self.tab_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.comboBox_14_port = QComboBox(self.tab_10)
        self.comboBox_14_port.setObjectName(u"comboBox_14_port")
        self.comboBox_14_port.setMinimumSize(QSize(500, 0))
        self.comboBox_14_port.setEditable(False)

        self.verticalLayout_8.addWidget(self.comboBox_14_port, 0, Qt.AlignHCenter)

        self.label_20 = QLabel(self.tab_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.comboBox_14_pin = QComboBox(self.tab_10)
        self.comboBox_14_pin.setObjectName(u"comboBox_14_pin")
        self.comboBox_14_pin.setMinimumSize(QSize(500, 0))

        self.verticalLayout_8.addWidget(self.comboBox_14_pin, 0, Qt.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, -1, 0)
        self.checkBox_14_timer_undefined = QCheckBox(self.tab_10)
        self.checkBox_14_timer_undefined.setObjectName(u"checkBox_14_timer_undefined")

        self.horizontalLayout_21.addWidget(self.checkBox_14_timer_undefined)

        self.pushButton_14_timer_define = QPushButton(self.tab_10)
        self.pushButton_14_timer_define.setObjectName(u"pushButton_14_timer_define")
        self.pushButton_14_timer_define.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.pushButton_14_timer_define)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, -1, -1, 0)
        self.label_21 = QLabel(self.tab_10)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_22.addWidget(self.label_21)

        self.comboBox_14_timer = QComboBox(self.tab_10)
        self.comboBox_14_timer.setObjectName(u"comboBox_14_timer")

        self.horizontalLayout_22.addWidget(self.comboBox_14_timer)


        self.verticalLayout_8.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, -1, -1, 0)
        self.label_22 = QLabel(self.tab_10)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_27.addWidget(self.label_22)

        self.comboBox_14_channel = QComboBox(self.tab_10)
        self.comboBox_14_channel.setObjectName(u"comboBox_14_channel")

        self.horizontalLayout_27.addWidget(self.comboBox_14_channel)


        self.verticalLayout_8.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, -1, -1, 0)
        self.label_23 = QLabel(self.tab_10)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_31.addWidget(self.label_23)

        self.lineEdit_14_time = QLineEdit(self.tab_10)
        self.lineEdit_14_time.setObjectName(u"lineEdit_14_time")
        self.lineEdit_14_time.setMinimumSize(QSize(0, 0))
        self.lineEdit_14_time.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_14_time.setAlignment(Qt.AlignCenter)
        self.lineEdit_14_time.setClearButtonEnabled(True)

        self.horizontalLayout_31.addWidget(self.lineEdit_14_time)

        self.comboBox_14_time_unit = QComboBox(self.tab_10)
        self.comboBox_14_time_unit.setObjectName(u"comboBox_14_time_unit")

        self.horizontalLayout_31.addWidget(self.comboBox_14_time_unit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, -1, -1, 0)
        self.label_24 = QLabel(self.tab_10)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_32.addWidget(self.label_24)

        self.lineEdit_14_impuls = QLineEdit(self.tab_10)
        self.lineEdit_14_impuls.setObjectName(u"lineEdit_14_impuls")
        self.lineEdit_14_impuls.setMinimumSize(QSize(0, 0))
        self.lineEdit_14_impuls.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_14_impuls.setAlignment(Qt.AlignCenter)
        self.lineEdit_14_impuls.setClearButtonEnabled(True)

        self.horizontalLayout_32.addWidget(self.lineEdit_14_impuls)

        self.comboBox_14_impuls_unit = QComboBox(self.tab_10)
        self.comboBox_14_impuls_unit.setObjectName(u"comboBox_14_impuls_unit")

        self.horizontalLayout_32.addWidget(self.comboBox_14_impuls_unit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, -1, -1, 0)
        self.label_25 = QLabel(self.tab_10)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_33.addWidget(self.label_25)

        self.lineEdit_14_freq = QLineEdit(self.tab_10)
        self.lineEdit_14_freq.setObjectName(u"lineEdit_14_freq")
        self.lineEdit_14_freq.setMinimumSize(QSize(0, 0))
        self.lineEdit_14_freq.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_14_freq.setAlignment(Qt.AlignCenter)
        self.lineEdit_14_freq.setClearButtonEnabled(True)

        self.horizontalLayout_33.addWidget(self.lineEdit_14_freq)

        self.comboBox_14_freq_unit = QComboBox(self.tab_10)
        self.comboBox_14_freq_unit.setObjectName(u"comboBox_14_freq_unit")

        self.horizontalLayout_33.addWidget(self.comboBox_14_freq_unit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, -1, -1, 0)
        self.label_26 = QLabel(self.tab_10)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_34.addWidget(self.label_26)

        self.comboBox_14_pwm_inv = QComboBox(self.tab_10)
        self.comboBox_14_pwm_inv.setObjectName(u"comboBox_14_pwm_inv")

        self.horizontalLayout_34.addWidget(self.comboBox_14_pwm_inv)


        self.verticalLayout_8.addLayout(self.horizontalLayout_34)

        self.label_30 = QLabel(self.tab_10)
        self.label_30.setObjectName(u"label_30")
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        self.label_30.setFont(font2)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_30)

        self.pushButton_14_define_arr = QPushButton(self.tab_10)
        self.pushButton_14_define_arr.setObjectName(u"pushButton_14_define_arr")
        self.pushButton_14_define_arr.setMinimumSize(QSize(400, 0))
        self.pushButton_14_define_arr.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_8.addWidget(self.pushButton_14_define_arr, 0, Qt.AlignHCenter)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, -1, -1, 0)
        self.label_31 = QLabel(self.tab_10)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_35.addWidget(self.label_31)

        self.lineEdit_14_m = QLineEdit(self.tab_10)
        self.lineEdit_14_m.setObjectName(u"lineEdit_14_m")
        self.lineEdit_14_m.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.lineEdit_14_m)

        self.label_27 = QLabel(self.tab_10)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_35.addWidget(self.label_27)

        self.lineEdit_14_psg = QLineEdit(self.tab_10)
        self.lineEdit_14_psg.setObjectName(u"lineEdit_14_psg")
        self.lineEdit_14_psg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.lineEdit_14_psg)

        self.label_28 = QLabel(self.tab_10)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_35.addWidget(self.label_28)

        self.lineEdit_14_arr = QLineEdit(self.tab_10)
        self.lineEdit_14_arr.setObjectName(u"lineEdit_14_arr")
        self.lineEdit_14_arr.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.lineEdit_14_arr)

        self.label_29 = QLabel(self.tab_10)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_35.addWidget(self.label_29)

        self.lineEdit_14_ccry = QLineEdit(self.tab_10)
        self.lineEdit_14_ccry.setObjectName(u"lineEdit_14_ccry")
        self.lineEdit_14_ccry.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.lineEdit_14_ccry)


        self.verticalLayout_8.addLayout(self.horizontalLayout_35)

        self.submitButton_14 = QPushButton(self.tab_10)
        self.submitButton_14.setObjectName(u"submitButton_14")
        sizePolicy3.setHeightForWidth(self.submitButton_14.sizePolicy().hasHeightForWidth())
        self.submitButton_14.setSizePolicy(sizePolicy3)
        self.submitButton_14.setMinimumSize(QSize(500, 50))
        self.submitButton_14.setMaximumSize(QSize(1000, 16777215))
        self.submitButton_14.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.submitButton_14, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b LSITRIM \u0438 HSITRIM \u0434\u043b\u044f \u0432\u0430\u0448\u0435\u0433\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0438 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.checkBox_6_lsi.setText(QCoreApplication.translate("MainWindow", u"LSI", None))
        self.label_6_lsi.setText(QCoreApplication.translate("MainWindow", u"LSITRIM", None))
        self.pushButton_6_show_lsi.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.checkBox_6_hsi.setText(QCoreApplication.translate("MainWindow", u"HSI", None))
        self.label_6_hsi.setText(QCoreApplication.translate("MainWindow", u"HSITRIM", None))
        self.pushButton_6_show_hsi.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.submitButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"LSI / HSI", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"LSE / HSE", None))
        self.checkBox_7_lse.setText(QCoreApplication.translate("MainWindow", u"LSE", None))
        self.checkBox_7_hse.setText(QCoreApplication.translate("MainWindow", u"HSE", None))
        self.submitButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"LSE / HSE", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CPU_CLK (HCLK)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"fHSE = 8 \u041c\u0413\u0446 (\u0435\u0441\u043b\u0438 \u044d\u0442\u043e \u043d\u0435 \u0442\u0430\u043a, \u0438\u0441\u043f\u0440\u0430\u0432\u044c\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u0438\u0436\u0435)", None))
        self.checkBox_8_nhse.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0440\u0443\u0433\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430 HSE", None))
        self.lineEdit_8_nhse.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0434\u043d\u0443 \u0438\u0437 \u0444\u043e\u0440\u043c \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u0445", None))
        self.checkBox_8_freq.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0430 \u0447\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.checkBox_8_main.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0430 \u0434\u0440\u043e\u0431\u044c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u043c\u0435\u043d\u0430\u0442\u0435\u043b\u044c", None))
        self.submitButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"CPU_CLK", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"USB_CLK (HCLK)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"fHSE = 8 \u041c\u0413\u0446 (\u0435\u0441\u043b\u0438 \u044d\u0442\u043e \u043d\u0435 \u0442\u0430\u043a, \u0438\u0441\u043f\u0440\u0430\u0432\u044c\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u0438\u0436\u0435)", None))
        self.checkBox_9_nhse.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0440\u0443\u0433\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430 HSE", None))
        self.lineEdit_9_nhse.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0434\u043d\u0443 \u0438\u0437 \u0444\u043e\u0440\u043c \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u0445", None))
        self.checkBox_9_freq.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0430 \u0447\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.checkBox_9_main.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0430 \u0434\u0440\u043e\u0431\u044c", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u043c\u0435\u043d\u0430\u0442\u0435\u043b\u044c", None))
        self.submitButton_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"USB_CLK", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"ADC_CLK (CPU/USB/LSE/LSI)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"fHSE = 8 \u041c\u0413\u0446 (\u0435\u0441\u043b\u0438 \u044d\u0442\u043e \u043d\u0435 \u0442\u0430\u043a, \u0438\u0441\u043f\u0440\u0430\u0432\u044c\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u0438\u0436\u0435)\n"
"fUSB = 48 \u041c\u0413\u0446 (\u0435\u0441\u043b\u0438 \u044d\u0442\u043e \u043d\u0435 \u0442\u0430\u043a, \u0438\u0441\u043f\u0440\u0430\u0432\u044c\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u0438\u0436\u0435)", None))
        self.checkBox_10_nhse.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0440\u0443\u0433\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.lineEdit_10_nhse.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0434\u043d\u0443 \u0438\u0437 \u0444\u043e\u0440\u043c \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u0445", None))
        self.checkBox_10_freq.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0430 \u0447\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.checkBox_10_main.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0430 \u0434\u0440\u043e\u0431\u044c", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u043c\u0435\u043d\u0430\u0442\u0435\u043b\u044c", None))
        self.submitButton_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"ADC_CLK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"ADC_CLK by HCI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0418\u041c", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u043d", None))
        self.checkBox_14_timer_undefined.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440\u0430 \u0442\u0430\u0439\u043c\u0435\u0440\u0430 \u0438 \u043a\u0430\u043d\u0430\u043b\u0430 \u043d\u0435 \u0437\u0430\u0434\u0430\u043d\u044b", None))
        self.pushButton_14_timer_define.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0430\u0439\u043c\u0435\u0440\u0430", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0441\u0438\u0433\u043d\u0430\u043b\u0430 \u0428\u0418\u041c", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430 \u0428\u0418\u041c", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u043a\u0442\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430 \u041c\u041a", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f PSG, ARR, CCRy \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043d\u0430\u0439\u0442\u0438 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440\u0430", None))
        self.pushButton_14_define_arr.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f M, PSG, ARR, CCRy", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"PSG", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ARR", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"CCRy", None))
        self.submitButton_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0445\u0430\u043b\u0438!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0428\u0418\u041c", None))
    # retranslateUi

