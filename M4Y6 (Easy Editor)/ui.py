# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easy_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_dir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dir.setGeometry(QtCore.QRect(10, 10, 141, 23))
        self.btn_dir.setStyleSheet("background-color: rgb(229, 96, 255);")
        self.btn_dir.setObjectName("btn_dir")
        self.lw_files = QtWidgets.QListWidget(self.centralwidget)
        self.lw_files.setGeometry(QtCore.QRect(10, 50, 141, 501))
        self.lw_files.setStyleSheet("background-color: rgb(73, 201, 255);")
        self.lw_files.setObjectName("lw_files")
        self.lb_image = QtWidgets.QLabel(self.centralwidget)
        self.lb_image.setGeometry(QtCore.QRect(160, 50, 621, 391))
        self.lb_image.setObjectName("lb_image")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(159, 519, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_left = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_left.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_left.setObjectName("btn_left")
        self.horizontalLayout.addWidget(self.btn_left)
        self.btn_right = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_right.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"background-color: rgb(255, 222, 30);")
        self.btn_right.setObjectName("btn_right")
        self.horizontalLayout.addWidget(self.btn_right)
        self.btn_flip = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_flip.setStyleSheet("background-color: rgb(206, 255, 226);")
        self.btn_flip.setObjectName("btn_flip")
        self.horizontalLayout.addWidget(self.btn_flip)
        self.btn_sharp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_sharp.setStyleSheet("background-color: rgb(251, 228, 255);")
        self.btn_sharp.setObjectName("btn_sharp")
        self.horizontalLayout.addWidget(self.btn_sharp)
        self.btn_bw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_bw.setObjectName("btn_bw")
        self.horizontalLayout.addWidget(self.btn_bw)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(650, 530, 91, 20))
        self.btn_1.setStyleSheet("background-color: rgb(224, 238, 255);")
        self.btn_1.setObjectName("btn_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Editor"))
        self.btn_dir.setText(_translate("MainWindow", "Папка"))
        self.lb_image.setText(_translate("MainWindow", "Картинка"))
        self.btn_left.setText(_translate("MainWindow", "Вліво"))
        self.btn_right.setText(_translate("MainWindow", "Вправо"))
        self.btn_flip.setText(_translate("MainWindow", "Дзеркало"))
        self.btn_sharp.setText(_translate("MainWindow", "Різкість"))
        self.btn_bw.setText(_translate("MainWindow", "Ч/Б"))
        self.btn_1.setText(_translate("MainWindow", "Перевернути"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
