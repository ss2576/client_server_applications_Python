# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repositories\Geekbrains_Client_Server_App\client\ui\client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.contactsGridLayout = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactsGridLayout.sizePolicy().hasHeightForWidth())
        self.contactsGridLayout.setSizePolicy(sizePolicy)
        self.contactsGridLayout.setObjectName("contactsGridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.contactsGridLayout)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.contactsGridLayout)
        self.tabWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.usersTab = QtWidgets.QWidget()
        self.usersTab.setObjectName("usersTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.usersTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.usersList = QtWidgets.QListWidget(self.usersTab)
        self.usersList.setObjectName("usersList")
        self.gridLayout_4.addWidget(self.usersList, 0, 0, 1, 1)
        self.tabWidget.addTab(self.usersTab, "")
        self.contactsTab = QtWidgets.QWidget()
        self.contactsTab.setObjectName("contactsTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.contactsTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.contactsList = QtWidgets.QListWidget(self.contactsTab)
        self.contactsList.setObjectName("contactsList")
        self.gridLayout_5.addWidget(self.contactsList, 0, 0, 1, 1)
        self.tabWidget.addTab(self.contactsTab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.contactsGridLayout, 0, 0, 2, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chatList = QtWidgets.QListWidget(self.centralwidget)
        self.chatList.setEnabled(True)
        self.chatList.setLineWidth(1)
        self.chatList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.chatList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.chatList.setObjectName("chatList")
        self.gridLayout_2.addWidget(self.chatList, 0, 0, 2, 2)
        self.messageTxa = QtWidgets.QTextEdit(self.centralwidget)
        self.messageTxa.setMaximumSize(QtCore.QSize(16777215, 50))
        self.messageTxa.setObjectName("messageTxa")
        self.gridLayout_2.addWidget(self.messageTxa, 3, 0, 1, 1)
        self.sendMsgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendMsgBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.sendMsgBtn.setObjectName("sendMsgBtn")
        self.gridLayout_2.addWidget(self.sendMsgBtn, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usersTab), _translate("MainWindow", "Users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contactsTab), _translate("MainWindow", "Contacts"))
        self.sendMsgBtn.setText(_translate("MainWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())