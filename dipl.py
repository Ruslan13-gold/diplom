# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dipl.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

PDF1 = 'file:///C:/Python/dip/PDF.pdf'


class Ui_MainWindow(QtWebEngineWidgets.QWebEngineView):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1556, 921)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: #f2f2f2;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(444, 820, 1011, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 350, 531))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 350, 273))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 350, 273))
        self.page_2.setObjectName("page_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #ebebeb;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 40, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #ebebeb;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 80, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #ebebeb;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 120, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #ebebeb;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 160, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #ebebeb;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 350, 273))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 350, 273))
        self.page_4.setObjectName("page_4")
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 350, 273))
        self.page_5.setObjectName("page_5")
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 350, 273))
        self.page_6.setObjectName("page_6")
        self.toolBox.addItem(self.page_6, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.horizontalLayoutWidget.setVisible(False)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.function_pushButton_7()
        self.function_pushButton_8()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "?????????????????? ????????????"))
        self.label.setText(_translate("MainWindow", "??? ???????????????? f(x)="))
        self.label_2.setText(_translate("MainWindow", "???? ?????????????? [a;b]"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "???????????? ???1. ??????????????."))
        self.pushButton_4.setText(_translate("MainWindow", "???????????? ????"))
        self.pushButton_5.setText(_translate("MainWindow", "???????????????????????? ???????????? ???1. ????"))
        self.pushButton_6.setText(_translate("MainWindow", "????????. ????. ??????. ????"))
        self.pushButton_7.setText(_translate("MainWindow", "???????????????????????? ???????????? ???2. ????????. ????."))
        self.pushButton_8.setText(_translate("MainWindow", "?????????????????????????? ??????????"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "???????????? ???2. ????."))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "???????????? 3"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "???????????? 4"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("MainWindow", "???????????? 5"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("MainWindow", "???????????? 6"))
        self.label_3.setText(_translate("MainWindow", "???????????????? ????????????"))

    def function_pushButton_7(self):
        self.pushButton_7.clicked.connect(lambda: self.write())

    def function_pushButton_8(self):
        self.pushButton_8.clicked.connect(lambda: self.pushButton_8_f2())

    def write(self):
        self.horizontalLayoutWidget.setVisible(True)

    def pushButton_8_f2(self):
        self.horizontalLayoutWidget.setVisible(False)
        self.load(QtCore.QUrl.fromUserInput("file:///C:/Python/dip/PDF.pdf"))

    def push(self):
        print("1")
# class Window(QtWebEngineWidgets.QWebEngineView):
#     def __init__(self):
#         super(Window, self).__init__()
#
#         def pushButton_8_f2(self):
#             self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDF)))
#         web = QWebEngineView()
#         web.resize(900, 500)
#         web.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
#         web.load(QUrl("file:///C:/Python/dip/PDF.pdf"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # app = QtWidgets.QApplication(sys.argv)
    # web = QtWebEngineWidgets.QWebEngineView()
    # web.resize(900,500)
    # web.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
    # web.load(QtCore.QUrl("file:///C:/Python/dip/PDF.pdf"))
    # web.show()
    #
    # sys.exit(app.exec_())
