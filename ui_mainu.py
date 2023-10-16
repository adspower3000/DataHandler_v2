# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def __init__(self):
            self.date2 = None
            self.date1 = None
            self.tableView = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1153, 652)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.enterbtn = QPushButton(self.centralwidget)
        self.enterbtn.setObjectName(u"enterbtn")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.enterbtn.setFont(font1)
        self.enterbtn.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"widht: 100px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255,70);\n"
"}")

        self.gridLayout.addWidget(self.enterbtn, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(1038, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 2)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)

        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"background-color: rgba(255, 255, 255,30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.verticalLayout_7 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 30)
        self.entering_the_date_4 = QHBoxLayout()
        self.entering_the_date_4.setSpacing(0)
        self.entering_the_date_4.setObjectName(u"entering_the_date_4")
        self.entering_the_date_4.setContentsMargins(-1, 12, 12, 12)
        self.entering_the_date_diapazon_4 = QVBoxLayout()
        self.entering_the_date_diapazon_4.setSpacing(0)
        self.entering_the_date_diapazon_4.setObjectName(u"entering_the_date_diapazon_4")
        self.entering_the_date_diapazon_4.setContentsMargins(12, 12, 12, 12)
        self.by_date_4 = QHBoxLayout()
        self.by_date_4.setSpacing(6)
        self.by_date_4.setObjectName(u"by_date_4")
        self.by_date_4.setContentsMargins(0, 0, 0, -1)
        self.label_13 = QLabel(self.MainFrame)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(20)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none\n"
" ")

        self.by_date_4.addWidget(self.label_13)

        self.bytimepicker_4 = QDateEdit(self.MainFrame)
        self.bytimepicker_4.setObjectName(u"bytimepicker_4")
        self.bytimepicker_4.setMaximumSize(QSize(170, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.bytimepicker_4.setFont(font3)
        self.bytimepicker_4.setStyleSheet(u"color: white;\n"
"padding-left: 8px;\n"
"")
        self.bytimepicker_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bytimepicker_4.setDateTime(QDateTime(QDate(2010, 12, 31), QTime(0, 0, 0)))
        self.bytimepicker_4.setDisplayFormat("dd.MM.yyyy")
        self.date2 = str(self.bytimepicker_4.date())
        self.bytimepicker_4.setCurrentSectionIndex(0)

        self.by_date_4.addWidget(self.bytimepicker_4)


        self.entering_the_date_diapazon_4.addLayout(self.by_date_4)

        self.until_date_4 = QHBoxLayout()
        self.until_date_4.setObjectName(u"until_date_4")
        self.until_date_4.setContentsMargins(0, -1, 0, 0)
        self.label_14 = QLabel(self.MainFrame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(60, 16777215))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.until_date_4.addWidget(self.label_14)

        self.untiltimepicker_4 = QDateEdit(self.MainFrame)
        self.untiltimepicker_4.setObjectName(u"untiltimepicker_4")
        self.untiltimepicker_4.setMaximumSize(QSize(170, 16777215))
        self.untiltimepicker_4.setFont(font3)
        self.untiltimepicker_4.setStyleSheet(u"color: white;\n"
"padding-left: 8px")
        self.untiltimepicker_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.untiltimepicker_4.setDateTime(QDateTime(QDate(2020, 12, 31), QTime(0, 0, 0)))
        self.untiltimepicker_4.setDisplayFormat("dd.MM.yyyy")
        self.date1 = str(self.untiltimepicker_4.date())
        self.untiltimepicker_4.setCurrentSectionIndex(0)

        self.until_date_4.addWidget(self.untiltimepicker_4)


        self.entering_the_date_diapazon_4.addLayout(self.until_date_4)


        self.entering_the_date_4.addLayout(self.entering_the_date_diapazon_4)

        self.enterbtn_4 = QPushButton(self.MainFrame)
        self.enterbtn_4.setObjectName(u"enterbtn_4")
        self.enterbtn_4.setFont(font3)
        self.enterbtn_4.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"widht: 100px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255,70);\n"
"}\n"
"")

        self.entering_the_date_4.addWidget(self.enterbtn_4)


        self.verticalLayout_7.addLayout(self.entering_the_date_4)

        self.data_4 = QHBoxLayout()
        self.data_4.setObjectName(u"data_4")
        self.data_name_4 = QVBoxLayout()
        self.data_name_4.setSpacing(0)
        self.data_name_4.setObjectName(u"data_name_4")
        self.data_name_4.setContentsMargins(12, 12, 12, 12)
        self.Sum_N_7 = QLabel(self.MainFrame)
        self.Sum_N_7.setObjectName(u"Sum_N_7")
        self.Sum_N_7.setFont(font2)
        self.Sum_N_7.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_name_4.addWidget(self.Sum_N_7)

        self.JobHour_7 = QLabel(self.MainFrame)
        self.JobHour_7.setObjectName(u"JobHour_7")
        self.JobHour_7.setFont(font2)
        self.JobHour_7.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_name_4.addWidget(self.JobHour_7)

        self.deltaT_7 = QLabel(self.MainFrame)
        self.deltaT_7.setObjectName(u"deltaT_7")
        self.deltaT_7.setFont(font2)
        self.deltaT_7.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_name_4.addWidget(self.deltaT_7)


        self.data_4.addLayout(self.data_name_4)

        self.data_digital_4 = QVBoxLayout()
        self.data_digital_4.setSpacing(0)
        self.data_digital_4.setObjectName(u"data_digital_4")
        self.data_digital_4.setContentsMargins(12, 12, 12, 12)
        self.Sum_N_8 = QLabel(self.MainFrame)
        self.Sum_N_8.setObjectName(u"Sum_N_8")
        self.Sum_N_8.setFont(font2)
        self.Sum_N_8.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_digital_4.addWidget(self.Sum_N_8)

        self.JobHour_8 = QLabel(self.MainFrame)
        self.JobHour_8.setObjectName(u"JobHour_8")
        self.JobHour_8.setFont(font2)
        self.JobHour_8.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_digital_4.addWidget(self.JobHour_8)

        self.deltaT_8 = QLabel(self.MainFrame)
        self.deltaT_8.setObjectName(u"deltaT_8")
        self.deltaT_8.setFont(font2)
        self.deltaT_8.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_digital_4.addWidget(self.deltaT_8)


        self.data_4.addLayout(self.data_digital_4)


        self.verticalLayout_7.addLayout(self.data_4)


        self.gridLayout.addWidget(self.MainFrame, 1, 2, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setTextElideMode(Qt.ElideRight)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(155)
        self.tableView.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.enterbtn.setText(QCoreApplication.translate("MainWindow", u"open file", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e", None))
        self.enterbtn_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434", None))
        self.Sum_N_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0437\u0430 \u0446\u0438\u043a\u043b", None))
        self.JobHour_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0435 \u0447\u0430\u0441\u044b", None))
        self.deltaT_7.setText(QCoreApplication.translate("MainWindow", u"deltaT", None))
        self.Sum_N_8.setText(QCoreApplication.translate("MainWindow", u"3423432", None))
        self.JobHour_8.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.deltaT_8.setText(QCoreApplication.translate("MainWindow", u"41.1", None))
    # retranslateUi

