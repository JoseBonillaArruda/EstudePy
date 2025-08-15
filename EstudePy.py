# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estudePy.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 450)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.ForceTabbedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.Panel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.page_geral = QWidget()
        self.page_geral.setObjectName(u"page_geral")
        self.gridLayout_7 = QGridLayout(self.page_geral)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.geralpresencatableWidget = QTableWidget(self.page_geral)
        self.geralpresencatableWidget.setObjectName(u"geralpresencatableWidget")

        self.gridLayout_7.addWidget(self.geralpresencatableWidget, 0, 0, 1, 1)

        self.geraldiscitableWidget = QTableWidget(self.page_geral)
        self.geraldiscitableWidget.setObjectName(u"geraldiscitableWidget")

        self.gridLayout_7.addWidget(self.geraldiscitableWidget, 1, 0, 1, 1)

        self.anotatabWidget_3 = QTabWidget(self.page_geral)
        self.anotatabWidget_3.setObjectName(u"anotatabWidget_3")
        self.anotatabWidget_3.setTabsClosable(False)
        self.anotatabWidget_3.setTabBarAutoHide(False)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.geralanotatextBrowser = QTextBrowser(self.tab_4)
        self.geralanotatextBrowser.setObjectName(u"geralanotatextBrowser")
        self.geralanotatextBrowser.setReadOnly(False)

        self.verticalLayout_9.addWidget(self.geralanotatextBrowser)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.geralanotapushButton = QPushButton(self.tab_4)
        self.geralanotapushButton.setObjectName(u"geralanotapushButton")

        self.horizontalLayout_5.addWidget(self.geralanotapushButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)


        self.gridLayout_6.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.anotatabWidget_3.addTab(self.tab_4, "")

        self.gridLayout_7.addWidget(self.anotatabWidget_3, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_geral)
        self.page_disciplina = QWidget()
        self.page_disciplina.setObjectName(u"page_disciplina")
        self.gridLayout_3 = QGridLayout(self.page_disciplina)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.discipresencatableWidget = QTableWidget(self.page_disciplina)
        self.discipresencatableWidget.setObjectName(u"discipresencatableWidget")

        self.verticalLayout_7.addWidget(self.discipresencatableWidget)

        self.discimarcaprespushButton = QPushButton(self.page_disciplina)
        self.discimarcaprespushButton.setObjectName(u"discimarcaprespushButton")

        self.verticalLayout_7.addWidget(self.discimarcaprespushButton)


        self.horizontalLayout_11.addLayout(self.verticalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.discinotatableWidget = QTableWidget(self.page_disciplina)
        self.discinotatableWidget.setObjectName(u"discinotatableWidget")

        self.verticalLayout_3.addWidget(self.discinotatableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.discinovanotapushButton = QPushButton(self.page_disciplina)
        self.discinovanotapushButton.setObjectName(u"discinovanotapushButton")

        self.horizontalLayout_2.addWidget(self.discinovanotapushButton)

        self.discieditnotapushButton = QPushButton(self.page_disciplina)
        self.discieditnotapushButton.setObjectName(u"discieditnotapushButton")

        self.horizontalLayout_2.addWidget(self.discieditnotapushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.discihorariotableWidget = QTableWidget(self.page_disciplina)
        self.discihorariotableWidget.setObjectName(u"discihorariotableWidget")

        self.verticalLayout_8.addWidget(self.discihorariotableWidget)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.discieditardidscipushButton = QPushButton(self.page_disciplina)
        self.discieditardidscipushButton.setObjectName(u"discieditardidscipushButton")

        self.horizontalLayout_14.addWidget(self.discieditardidscipushButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.anotatabWidget = QTabWidget(self.page_disciplina)
        self.anotatabWidget.setObjectName(u"anotatabWidget")
        self.anotatabWidget.setTabsClosable(False)
        self.anotatabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.discianotatextBrowser = QTextBrowser(self.tab_1)
        self.discianotatextBrowser.setObjectName(u"discianotatextBrowser")

        self.verticalLayout_4.addWidget(self.discianotatextBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.discianotapushButton = QPushButton(self.tab_1)
        self.discianotapushButton.setObjectName(u"discianotapushButton")

        self.horizontalLayout.addWidget(self.discianotapushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.anotatabWidget.addTab(self.tab_1, "")

        self.verticalLayout_8.addWidget(self.anotatabWidget)


        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_disciplina)
        self.page_prova = QWidget()
        self.page_prova.setObjectName(u"page_prova")
        self.gridLayout_4 = QGridLayout(self.page_prova)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.page_prova)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.page_prova)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.novnotapesospinBox = QSpinBox(self.page_prova)
        self.novnotapesospinBox.setObjectName(u"novnotapesospinBox")

        self.verticalLayout_5.addWidget(self.novnotapesospinBox)

        self.label_3 = QLabel(self.page_prova)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.novnotadoubleSpinBox = QDoubleSpinBox(self.page_prova)
        self.novnotadoubleSpinBox.setObjectName(u"novnotadoubleSpinBox")

        self.verticalLayout_5.addWidget(self.novnotadoubleSpinBox)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.novnotasalvapushButton = QPushButton(self.page_prova)
        self.novnotasalvapushButton.setObjectName(u"novnotasalvapushButton")

        self.horizontalLayout_3.addWidget(self.novnotasalvapushButton)

        self.novnotaretornapushButton = QPushButton(self.page_prova)
        self.novnotaretornapushButton.setObjectName(u"novnotaretornapushButton")

        self.horizontalLayout_3.addWidget(self.novnotaretornapushButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.novnotatableWidget = QTableWidget(self.page_prova)
        self.novnotatableWidget.setObjectName(u"novnotatableWidget")

        self.gridLayout_4.addWidget(self.novnotatableWidget, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_prova)
        self.page_novdisci = QWidget()
        self.page_novdisci.setObjectName(u"page_novdisci")
        self.gridLayout_5 = QGridLayout(self.page_novdisci)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.page_novdisci)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.novdiscinomelineEdit = QLineEdit(self.page_novdisci)
        self.novdiscinomelineEdit.setObjectName(u"novdiscinomelineEdit")

        self.horizontalLayout_17.addWidget(self.novdiscinomelineEdit)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_17)

        self.editdisciDeletarpushButton = QPushButton(self.page_novdisci)
        self.editdisciDeletarpushButton.setObjectName(u"editdisciDeletarpushButton")

        self.horizontalLayout_19.addWidget(self.editdisciDeletarpushButton)


        self.gridLayout_5.addLayout(self.horizontalLayout_19, 2, 0, 1, 1)

        self.label_4 = QLabel(self.page_novdisci)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.novdiscitableWidget = QTableWidget(self.page_novdisci)
        self.novdiscitableWidget.setObjectName(u"novdiscitableWidget")

        self.gridLayout_5.addWidget(self.novdiscitableWidget, 1, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.page_novdisci)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.novdiscicargahoraspinBox = QSpinBox(self.page_novdisci)
        self.novdiscicargahoraspinBox.setObjectName(u"novdiscicargahoraspinBox")

        self.horizontalLayout_4.addWidget(self.novdiscicargahoraspinBox)

        self.label_6 = QLabel(self.page_novdisci)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.page_novdisci)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.novdiscidiacomboBox = QComboBox(self.page_novdisci)
        self.novdiscidiacomboBox.setObjectName(u"novdiscidiacomboBox")

        self.horizontalLayout_6.addWidget(self.novdiscidiacomboBox)

        self.novdiscihorariotimeEdit = QTimeEdit(self.page_novdisci)
        self.novdiscihorariotimeEdit.setObjectName(u"novdiscihorariotimeEdit")

        self.horizontalLayout_6.addWidget(self.novdiscihorariotimeEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.page_novdisci)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.novdiscilocallineEdit = QLineEdit(self.page_novdisci)
        self.novdiscilocallineEdit.setObjectName(u"novdiscilocallineEdit")

        self.horizontalLayout_8.addWidget(self.novdiscilocallineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.page_novdisci)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.novdiscitipomediacomboBox = QComboBox(self.page_novdisci)
        self.novdiscitipomediacomboBox.setObjectName(u"novdiscitipomediacomboBox")

        self.horizontalLayout_9.addWidget(self.novdiscitipomediacomboBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)


        self.gridLayout_5.addLayout(self.verticalLayout_10, 3, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.novdiscisalvapushButton = QPushButton(self.page_novdisci)
        self.novdiscisalvapushButton.setObjectName(u"novdiscisalvapushButton")

        self.horizontalLayout_10.addWidget(self.novdiscisalvapushButton)

        self.novdisciretornapushButton = QPushButton(self.page_novdisci)
        self.novdisciretornapushButton.setObjectName(u"novdisciretornapushButton")

        self.horizontalLayout_10.addWidget(self.novdisciretornapushButton)


        self.gridLayout_5.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_novdisci)
        self.page_editarnotas = QWidget()
        self.page_editarnotas.setObjectName(u"page_editarnotas")
        self.gridLayout_14 = QGridLayout(self.page_editarnotas)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.editnotatableWidget_6 = QTableWidget(self.page_editarnotas)
        self.editnotatableWidget_6.setObjectName(u"editnotatableWidget_6")

        self.horizontalLayout_27.addWidget(self.editnotatableWidget_6)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.page_editarnotas)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_13.addWidget(self.label_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.editnotaselectcomboBox = QComboBox(self.page_editarnotas)
        self.editnotaselectcomboBox.setObjectName(u"editnotaselectcomboBox")

        self.horizontalLayout_13.addWidget(self.editnotaselectcomboBox)

        self.editnotadeletepushButton = QPushButton(self.page_editarnotas)
        self.editnotadeletepushButton.setObjectName(u"editnotadeletepushButton")

        self.horizontalLayout_13.addWidget(self.editnotadeletepushButton)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.page_editarnotas)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_12.addWidget(self.label_12)

        self.editnotadoubleSpinBox = QDoubleSpinBox(self.page_editarnotas)
        self.editnotadoubleSpinBox.setObjectName(u"editnotadoubleSpinBox")

        self.verticalLayout_12.addWidget(self.editnotadoubleSpinBox)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.verticalLayout_27.addLayout(self.verticalLayout_14)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.editnotsalvapushButton = QPushButton(self.page_editarnotas)
        self.editnotsalvapushButton.setObjectName(u"editnotsalvapushButton")

        self.horizontalLayout_12.addWidget(self.editnotsalvapushButton)

        self.editnotaretornapushButton = QPushButton(self.page_editarnotas)
        self.editnotaretornapushButton.setObjectName(u"editnotaretornapushButton")

        self.horizontalLayout_12.addWidget(self.editnotaretornapushButton)


        self.verticalLayout_27.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_27.addLayout(self.verticalLayout_27)


        self.gridLayout_14.addLayout(self.horizontalLayout_27, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_editarnotas)
        self.page_editardisci = QWidget()
        self.page_editardisci.setObjectName(u"page_editardisci")
        self.gridLayout_9 = QGridLayout(self.page_editardisci)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_34 = QLabel(self.page_editardisci)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_9.addWidget(self.label_34, 0, 0, 1, 1)

        self.editdiscitableWidget = QTableWidget(self.page_editardisci)
        self.editdiscitableWidget.setObjectName(u"editdiscitableWidget")

        self.gridLayout_9.addWidget(self.editdiscitableWidget, 1, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.page_editardisci)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_18.addWidget(self.label_16)

        self.editdiscinomelineEdit = QLineEdit(self.page_editardisci)
        self.editdiscinomelineEdit.setObjectName(u"editdiscinomelineEdit")

        self.horizontalLayout_18.addWidget(self.editdiscinomelineEdit)


        self.gridLayout_9.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_29 = QLabel(self.page_editardisci)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_34.addWidget(self.label_29)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.editdiscicargahoraspinBox_4 = QSpinBox(self.page_editardisci)
        self.editdiscicargahoraspinBox_4.setObjectName(u"editdiscicargahoraspinBox_4")

        self.horizontalLayout_35.addWidget(self.editdiscicargahoraspinBox_4)

        self.label_30 = QLabel(self.page_editardisci)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_35.addWidget(self.label_30)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_17)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_35)


        self.gridLayout_9.addLayout(self.horizontalLayout_34, 3, 0, 1, 1)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_35 = QLabel(self.page_editardisci)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_40.addWidget(self.label_35)

        self.editdiscipresencaspinBox = QSpinBox(self.page_editardisci)
        self.editdiscipresencaspinBox.setObjectName(u"editdiscipresencaspinBox")

        self.horizontalLayout_40.addWidget(self.editdiscipresencaspinBox)

        self.label_36 = QLabel(self.page_editardisci)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_40.addWidget(self.label_36)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_21)


        self.gridLayout_9.addLayout(self.horizontalLayout_40, 4, 0, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_31 = QLabel(self.page_editardisci)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_36.addWidget(self.label_31)

        self.editdiscidiacomboBox = QComboBox(self.page_editardisci)
        self.editdiscidiacomboBox.setObjectName(u"editdiscidiacomboBox")

        self.horizontalLayout_36.addWidget(self.editdiscidiacomboBox)

        self.editdiscihorariotimeEdit = QTimeEdit(self.page_editardisci)
        self.editdiscihorariotimeEdit.setObjectName(u"editdiscihorariotimeEdit")

        self.horizontalLayout_36.addWidget(self.editdiscihorariotimeEdit)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_18)


        self.gridLayout_9.addLayout(self.horizontalLayout_36, 5, 0, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_32 = QLabel(self.page_editardisci)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_37.addWidget(self.label_32)

        self.editdiscilocallineEdit = QLineEdit(self.page_editardisci)
        self.editdiscilocallineEdit.setObjectName(u"editdiscilocallineEdit")

        self.horizontalLayout_37.addWidget(self.editdiscilocallineEdit)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_19)


        self.gridLayout_9.addLayout(self.horizontalLayout_37, 6, 0, 1, 1)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_33 = QLabel(self.page_editardisci)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_38.addWidget(self.label_33)

        self.editdiscitipomediacomboBox = QComboBox(self.page_editardisci)
        self.editdiscitipomediacomboBox.setObjectName(u"editdiscitipomediacomboBox")

        self.horizontalLayout_38.addWidget(self.editdiscitipomediacomboBox)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_20)


        self.gridLayout_9.addLayout(self.horizontalLayout_38, 7, 0, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.editdiscisalvapushButton = QPushButton(self.page_editardisci)
        self.editdiscisalvapushButton.setObjectName(u"editdiscisalvapushButton")

        self.horizontalLayout_39.addWidget(self.editdiscisalvapushButton)

        self.editdisciretornapushButton = QPushButton(self.page_editardisci)
        self.editdisciretornapushButton.setObjectName(u"editdisciretornapushButton")

        self.horizontalLayout_39.addWidget(self.editdisciretornapushButton)


        self.gridLayout_9.addLayout(self.horizontalLayout_39, 8, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_editardisci)
        self.page_marcpres = QWidget()
        self.page_marcpres.setObjectName(u"page_marcpres")
        self.gridLayout_8 = QGridLayout(self.page_marcpres)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.page_marcpres)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_16.addWidget(self.label_13)

        self.marcprestableWidget = QTableWidget(self.page_marcpres)
        self.marcprestableWidget.setObjectName(u"marcprestableWidget")

        self.verticalLayout_16.addWidget(self.marcprestableWidget)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.page_marcpres)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.marcpresspinBox = QSpinBox(self.page_marcpres)
        self.marcpresspinBox.setObjectName(u"marcpresspinBox")

        self.horizontalLayout_15.addWidget(self.marcpresspinBox)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.marcpressalvapushButton = QPushButton(self.page_marcpres)
        self.marcpressalvapushButton.setObjectName(u"marcpressalvapushButton")

        self.horizontalLayout_16.addWidget(self.marcpressalvapushButton)

        self.marcpresretornapushButton = QPushButton(self.page_marcpres)
        self.marcpresretornapushButton.setObjectName(u"marcpresretornapushButton")

        self.horizontalLayout_16.addWidget(self.marcpresretornapushButton)


        self.verticalLayout_15.addLayout(self.horizontalLayout_16)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)


        self.gridLayout_8.addLayout(self.verticalLayout_16, 0, 0, 2, 2)

        self.stackedWidget.addWidget(self.page_marcpres)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 606, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sidedockWidget = QDockWidget(MainWindow)
        self.sidedockWidget.setObjectName(u"sidedockWidget")
        self.sidedockWidget.setEnabled(True)
        self.sidedockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.sidedockWidget.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.novadiscipushButton = QPushButton(self.dockWidgetContents_3)
        self.novadiscipushButton.setObjectName(u"novadiscipushButton")

        self.verticalLayout.addWidget(self.novadiscipushButton)

        self.GeralpushButton = QPushButton(self.dockWidgetContents_3)
        self.GeralpushButton.setObjectName(u"GeralpushButton")

        self.verticalLayout.addWidget(self.GeralpushButton)

        self.label_11 = QLabel(self.dockWidgetContents_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.listDiscicomboBox = QComboBox(self.dockWidgetContents_3)
        self.listDiscicomboBox.setObjectName(u"listDiscicomboBox")

        self.verticalLayout.addWidget(self.listDiscicomboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.sidedockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidedockWidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.anotatabWidget_3.setCurrentIndex(0)
        self.anotatabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EstudePy", None))
        self.geralanotapushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.anotatabWidget_3.setTabText(self.anotatabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Anota\u00e7\u00f5es", None))
        self.discimarcaprespushButton.setText(QCoreApplication.translate("MainWindow", u"Marcar Presen\u00e7a", None))
        self.discinovanotapushButton.setText(QCoreApplication.translate("MainWindow", u"Nova Prova", None))
        self.discieditnotapushButton.setText(QCoreApplication.translate("MainWindow", u"Editar Notas", None))
        self.discieditardidscipushButton.setText(QCoreApplication.translate("MainWindow", u"Editar Disciplina", None))
        self.discianotapushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.anotatabWidget.setTabText(self.anotatabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Anota\u00e7\u00f5es", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nova Prova", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Peso (Opcional):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nota:", None))
        self.novnotasalvapushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.novnotaretornapushButton.setText(QCoreApplication.translate("MainWindow", u"Retornar", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Disciplina:", None))
        self.editdisciDeletarpushButton.setText(QCoreApplication.translate("MainWindow", u"Apagar Disciplina", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nova Disciplina", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Carga Hor\u00e1ria:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Horas Aulas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tipo de M\u00e9dia:", None))
        self.novdiscisalvapushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.novdisciretornapushButton.setText(QCoreApplication.translate("MainWindow", u"Retornar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Editar Nota:", None))
        self.editnotadeletepushButton.setText(QCoreApplication.translate("MainWindow", u"Remover Nota", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nota:", None))
        self.editnotsalvapushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.editnotaretornapushButton.setText(QCoreApplication.translate("MainWindow", u"Retornar", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Editar Disciplina", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Disciplina:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Carga Hor\u00e1ria:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Aulas", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Aulas", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Tipo de M\u00e9dia:", None))
        self.editdiscisalvapushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.editdisciretornapushButton.setText(QCoreApplication.translate("MainWindow", u"Retornar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Marcar Presen\u00e7a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Aulas: ", None))
        self.marcpressalvapushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.marcpresretornapushButton.setText(QCoreApplication.translate("MainWindow", u"Retornar", None))
#if QT_CONFIG(tooltip)
        self.sidedockWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.novadiscipushButton.setText(QCoreApplication.translate("MainWindow", u"Nova Disciplina", None))
        self.GeralpushButton.setText(QCoreApplication.translate("MainWindow", u"Geral", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Disciplinas:", None))
    # retranslateUi

