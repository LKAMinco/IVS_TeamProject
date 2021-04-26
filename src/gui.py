# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_v0_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 460)
        MainWindow.setMinimumSize(QtCore.QSize(300, 460))
        MainWindow.setMaximumSize(QtCore.QSize(300, 460))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("background-color: rgb(50, 50,50); ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setBaseSize(QtCore.QSize(300, 420))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_one = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_one.setGeometry(QtCore.QRect(0, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_one.setFont(font)
        self.pushButton_one.setToolTip("")
        self.pushButton_one.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_one.setObjectName("pushButton_one")
        self.pushButton_two = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_two.setGeometry(QtCore.QRect(70, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_two.setFont(font)
        self.pushButton_two.setToolTip("")
        self.pushButton_two.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_two.setObjectName("pushButton_two")
        self.pushButton_three = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_three.setGeometry(QtCore.QRect(140, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_three.setFont(font)
        self.pushButton_three.setToolTip("")
        self.pushButton_three.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_three.setObjectName("pushButton_three")
        self.pushButton_nine = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nine.setEnabled(True)
        self.pushButton_nine.setGeometry(QtCore.QRect(140, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_nine.setFont(font)
        self.pushButton_nine.setMouseTracking(False)
        self.pushButton_nine.setToolTip("")
        self.pushButton_nine.setAutoFillBackground(False)
        self.pushButton_nine.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_nine.setFlat(False)
        self.pushButton_nine.setObjectName("pushButton_nine")
        self.pushButton_eight = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eight.setGeometry(QtCore.QRect(70, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_eight.setFont(font)
        self.pushButton_eight.setToolTip("")
        self.pushButton_eight.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_eight.setObjectName("pushButton_eight")
        self.pushButton_seven = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_seven.setGeometry(QtCore.QRect(0, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_seven.setFont(font)
        self.pushButton_seven.setToolTip("")
        self.pushButton_seven.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_seven.setObjectName("pushButton_seven")
        self.pushButton_four = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_four.setGeometry(QtCore.QRect(0, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_four.setFont(font)
        self.pushButton_four.setToolTip("")
        self.pushButton_four.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_four.setObjectName("pushButton_four")
        self.pushButton_five = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_five.setGeometry(QtCore.QRect(70, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_five.setFont(font)
        self.pushButton_five.setToolTip("")
        self.pushButton_five.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_five.setObjectName("pushButton_five")
        self.pushButton_six = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_six.setGeometry(QtCore.QRect(140, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_six.setFont(font)
        self.pushButton_six.setToolTip("")
        self.pushButton_six.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_six.setObjectName("pushButton_six")
        self.pushButton_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zero.setGeometry(QtCore.QRect(70, 360, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_zero.setFont(font)
        self.pushButton_zero.setToolTip("")
        self.pushButton_zero.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(140, 360, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(210, 290, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sub.setGeometry(QtCore.QRect(210, 220, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mul.setGeometry(QtCore.QRect(210, 150, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(210, 80, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setWhatsThis("")
        self.pushButton_div.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_result = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_result.setGeometry(QtCore.QRect(210, 360, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_result.setFont(font)
        self.pushButton_result.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_result.setObjectName("pushButton_result")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(0, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 360, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton { background-color: rgb(50, 50, 50); \n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);} \n"
"QPushButton:pressed { background-color: rgb(100, 100, 100);} ")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_pow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pow.setGeometry(QtCore.QRect(140, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_pow.setFont(font)
        self.pushButton_pow.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_pow.setObjectName("pushButton_pow")
        self.pushButton_sqr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr.setGeometry(QtCore.QRect(70, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_sqr.setFont(font)
        self.pushButton_sqr.setStyleSheet("QPushButton { background-color: rgb(35, 176, 93);\n"
"border: 1px outset rgb(20,20,20); color: rgb(255, 255, 255);}\n"
"QPushButton:pressed { background-color: rgb(42, 213, 116);} \n"
"")
        self.pushButton_sqr.setObjectName("pushButton_sqr")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 301, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.lineEdit_results = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_results.setGeometry(QtCore.QRect(5, 35, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_results.setFont(font)
        self.lineEdit_results.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_results.setAutoFillBackground(False)
        self.lineEdit_results.setStyleSheet("border:0px solid black; color: rgb(255, 255, 255);")
        self.lineEdit_results.setText("")
        self.lineEdit_results.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_results.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_results.setReadOnly(True)
        self.lineEdit_results.setObjectName("lineEdit_results")
        self.label_results = QtWidgets.QLabel(self.frame)
        self.label_results.setGeometry(QtCore.QRect(20, 5, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_results.setFont(font)
        self.label_results.setStyleSheet("QLabel {  color : rgb(180,180,180); }")
        self.label_results.setText("")
        self.label_results.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_results.setObjectName("label_results")
        self.frame.raise_()
        self.pushButton_five.raise_()
        self.pushButton_dot.raise_()
        self.pushButton_del.raise_()
        self.pushButton_add.raise_()
        self.pushButton_mul.raise_()
        self.pushButton_div.raise_()
        self.pushButton_eight.raise_()
        self.pushButton_one.raise_()
        self.pushButton_zero.raise_()
        self.pushButton_two.raise_()
        self.pushButton_result.raise_()
        self.pushButton_four.raise_()
        self.pushButton_sqr.raise_()
        self.pushButton_six.raise_()
        self.pushButton_clear.raise_()
        self.pushButton_pow.raise_()
        self.pushButton_three.raise_()
        self.pushButton_nine.raise_()
        self.pushButton_seven.raise_()
        self.pushButton_sub.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 30))
        self.menuBar.setStyleSheet("QMenuBar:item{color: rgb(255, 255, 255);\n"
"        }\n"
"QMenuBar:item:selected {\n"
"background-color: rgb(35, 176, 93); color: rgb(255, 255, 255);\n"
"        }")
        self.menuBar.setObjectName("menuBar")
        self.menuFunctions = QtWidgets.QMenu(self.menuBar)
        self.menuFunctions.setStyleSheet("QMenu {color: rgb(255, 255, 255);}\n"
"QMenu:selected {background-color: rgb(35, 176, 93); color: rgb(255, 255, 255);}\n"
"QMenu:pressed {background-color: rgb(42, 213, 116); color: rgb(255, 255, 255);}")
        self.menuFunctions.setObjectName("menuFunctions")
        self.menuConvertor = QtWidgets.QMenu(self.menuBar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 213, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 213, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.menuConvertor.setPalette(palette)
        self.menuConvertor.setStyleSheet("QMenu {color: rgb(255, 255, 255);}\n"
"QMenu:selected {background-color: rgb(35, 176, 93);}\n"
"QMenu:pressed {background-color: rgb(42, 213, 116);}")
        self.menuConvertor.setObjectName("menuConvertor")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setEnabled(True)
        self.menuHelp.setGeometry(QtCore.QRect(653, 350, 135, 84))
        self.menuHelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuHelp.setStyleSheet("QMenu {color: rgb(255, 255, 255);}\n"
"QMenu:selected {background-color: rgb(35, 176, 93);}\n"
"QMenu:pressed {background-color: rgb(42, 213, 116);}")
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actiongdfgd = QtWidgets.QAction(MainWindow)
        self.actiongdfgd.setObjectName("actiongdfgd")
        self.action_hp2kw = QtWidgets.QAction(MainWindow)
        self.action_hp2kw.setObjectName("action_hp2kw")
        self.action_rad2deg = QtWidgets.QAction(MainWindow)
        self.action_rad2deg.setObjectName("action_rad2deg")
        self.action_deg2rad = QtWidgets.QAction(MainWindow)
        self.action_deg2rad.setObjectName("action_deg2rad")
        self.action_nm2lbsft = QtWidgets.QAction(MainWindow)
        self.action_nm2lbsft.setObjectName("action_nm2lbsft")
        self.action_sin = QtWidgets.QAction(MainWindow)
        self.action_sin.setObjectName("action_sin")
        self.action_cos = QtWidgets.QAction(MainWindow)
        self.action_cos.setObjectName("action_cos")
        self.action_abs = QtWidgets.QAction(MainWindow)
        self.action_abs.setObjectName("action_abs")
        self.action_fac = QtWidgets.QAction(MainWindow)
        self.action_fac.setObjectName("action_fac")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionfsdfs = QtWidgets.QAction(MainWindow)
        self.actionfsdfs.setObjectName("actionfsdfs")
        self.actionDeterminant = QtWidgets.QAction(MainWindow)
        self.actionDeterminant.setObjectName("actionDeterminant")
        self.actionTranspose = QtWidgets.QAction(MainWindow)
        self.actionTranspose.setObjectName("actionTranspose")
        self.actionCramer_s_rule = QtWidgets.QAction(MainWindow)
        self.actionCramer_s_rule.setObjectName("actionCramer_s_rule")
        self.actionMultiplication = QtWidgets.QAction(MainWindow)
        self.actionMultiplication.setObjectName("actionMultiplication")
        self.action_kw2hp = QtWidgets.QAction(MainWindow)
        self.action_kw2hp.setObjectName("action_kw2hp")
        self.action_lbsft2nm = QtWidgets.QAction(MainWindow)
        self.action_lbsft2nm.setObjectName("action_lbsft2nm")
        self.menuFunctions.addAction(self.action_sin)
        self.menuFunctions.addAction(self.action_cos)
        self.menuFunctions.addAction(self.action_abs)
        self.menuFunctions.addAction(self.action_fac)
        self.menuConvertor.addAction(self.action_deg2rad)
        self.menuConvertor.addAction(self.action_rad2deg)
        self.menuConvertor.addAction(self.action_hp2kw)
        self.menuConvertor.addAction(self.action_kw2hp)
        self.menuConvertor.addAction(self.action_nm2lbsft)
        self.menuConvertor.addAction(self.action_lbsft2nm)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuBar.addAction(self.menuFunctions.menuAction())
        self.menuBar.addAction(self.menuConvertor.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_clear, self.pushButton_zero)
        MainWindow.setTabOrder(self.pushButton_zero, self.pushButton_dot)
        MainWindow.setTabOrder(self.pushButton_dot, self.pushButton_result)
        MainWindow.setTabOrder(self.pushButton_result, self.pushButton_one)
        MainWindow.setTabOrder(self.pushButton_one, self.pushButton_two)
        MainWindow.setTabOrder(self.pushButton_two, self.pushButton_three)
        MainWindow.setTabOrder(self.pushButton_three, self.pushButton_add)
        MainWindow.setTabOrder(self.pushButton_add, self.pushButton_four)
        MainWindow.setTabOrder(self.pushButton_four, self.pushButton_five)
        MainWindow.setTabOrder(self.pushButton_five, self.pushButton_six)
        MainWindow.setTabOrder(self.pushButton_six, self.pushButton_sub)
        MainWindow.setTabOrder(self.pushButton_sub, self.pushButton_seven)
        MainWindow.setTabOrder(self.pushButton_seven, self.pushButton_eight)
        MainWindow.setTabOrder(self.pushButton_eight, self.pushButton_nine)
        MainWindow.setTabOrder(self.pushButton_nine, self.pushButton_mul)
        MainWindow.setTabOrder(self.pushButton_mul, self.pushButton_del)
        MainWindow.setTabOrder(self.pushButton_del, self.pushButton_sqr)
        MainWindow.setTabOrder(self.pushButton_sqr, self.pushButton_pow)
        MainWindow.setTabOrder(self.pushButton_pow, self.pushButton_div)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CalculaThor"))
        self.pushButton_one.setText(_translate("MainWindow", "1"))
        self.pushButton_one.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_two.setText(_translate("MainWindow", "2"))
        self.pushButton_two.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_three.setText(_translate("MainWindow", "3"))
        self.pushButton_three.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_nine.setText(_translate("MainWindow", "9"))
        self.pushButton_nine.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_eight.setText(_translate("MainWindow", "8"))
        self.pushButton_eight.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_seven.setText(_translate("MainWindow", "7"))
        self.pushButton_seven.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_four.setText(_translate("MainWindow", "4"))
        self.pushButton_four.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_five.setText(_translate("MainWindow", "5"))
        self.pushButton_five.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_six.setText(_translate("MainWindow", "6"))
        self.pushButton_six.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_zero.setText(_translate("MainWindow", "0"))
        self.pushButton_zero.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_dot.setToolTip(_translate("MainWindow", "Decimal separator"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_dot.setShortcut(_translate("MainWindow", "."))
        self.pushButton_add.setToolTip(_translate("MainWindow", "<html><head/><body><p>Addition</p><p><span style=\" color:#25be62;\">-----------------------</span></p><p>Sum of a and b</p></body></html>"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_add.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_sub.setToolTip(_translate("MainWindow", "<html><head/><body><p>Subtraction</p><p><span style=\" color:#25be62;\">-------------------------------</span></p><p>Difference of a and b</p></body></html>"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_sub.setShortcut(_translate("MainWindow", "-"))
        self.pushButton_mul.setToolTip(_translate("MainWindow", "<html><head/><body><p>Multiplication</p><p><span style=\" color:#25be62;\">---------------------------</span></p><p>Product of a and b</p></body></html>"))
        self.pushButton_mul.setText(_translate("MainWindow", "x"))
        self.pushButton_mul.setShortcut(_translate("MainWindow", "*"))
        self.pushButton_div.setToolTip(_translate("MainWindow", "<html><head/><body><p>Division</p><p><span style=\" color:#25be62;\">-----------------------------</span></p><p>Quotient of a and b</p></body></html>"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_div.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_result.setToolTip(_translate("MainWindow", "Result"))
        self.pushButton_result.setText(_translate("MainWindow", "="))
        self.pushButton_result.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton_del.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delete one character</p></body></html>"))
        self.pushButton_del.setText(_translate("MainWindow", "DEL"))
        self.pushButton_del.setShortcut(_translate("MainWindow", "Backspace"))
        self.pushButton_clear.setToolTip(_translate("MainWindow", "Clear all"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_clear.setShortcut(_translate("MainWindow", "Del"))
        self.pushButton_pow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Power </p><p>a^n</p><p><span style=\" color:#25be62;\">------------------------------------------</span></p><p>a - base </p><p>n - exponent</p><p>Base raised to the exponent</p></body></html>"))
        self.pushButton_pow.setText(_translate("MainWindow", "^"))
        self.pushButton_sqr.setToolTip(_translate("MainWindow", "<html><head/><body><p>Root </p><p>n√a</p><p><span style=\" color:#25be62;\">-------------------</span></p><p>n-th root of a</p></body></html>"))
        self.pushButton_sqr.setText(_translate("MainWindow", "√"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Functions"))
        self.menuConvertor.setTitle(_translate("MainWindow", "Convertor"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actiongdfgd.setText(_translate("MainWindow", "gdfgd"))
        self.action_hp2kw.setText(_translate("MainWindow", "HP to KW"))
        self.action_rad2deg.setText(_translate("MainWindow", "Rad to Deg"))
        self.action_deg2rad.setText(_translate("MainWindow", "Deg to Rad"))
        self.action_nm2lbsft.setText(_translate("MainWindow", "NM to lbs-ft"))
        self.action_sin.setText(_translate("MainWindow", "Sin(x)"))
        self.action_cos.setText(_translate("MainWindow", "Cos(x)"))
        self.action_abs.setText(_translate("MainWindow", "Abs(x)"))
        self.action_fac.setText(_translate("MainWindow", "x!"))
        self.action_fac.setToolTip(_translate("MainWindow", "<html><head/><body><p>Factorial</p><p><span style=\" color:#25be62;\">--------------------</span></p><p>Factorial of n</p></body></html>"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionfsdfs.setText(_translate("MainWindow", "fsdfs"))
        self.actionDeterminant.setText(_translate("MainWindow", "Determinant"))
        self.actionTranspose.setText(_translate("MainWindow", "Transpose"))
        self.actionCramer_s_rule.setText(_translate("MainWindow", "Cramer\'s rule"))
        self.actionMultiplication.setText(_translate("MainWindow", "Multiplication"))
        self.action_kw2hp.setText(_translate("MainWindow", "KW to HP"))
        self.action_lbsft2nm.setText(_translate("MainWindow", "lbs-ft to NM"))
import resources
