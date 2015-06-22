# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Jun 22 13:34:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FileLoaderG(object):
    def setupUi(self, FileLoaderG):
        FileLoaderG.setObjectName(_fromUtf8("FileLoaderG"))
        FileLoaderG.resize(909, 541)
        self.centralwidget = QtGui.QWidget(FileLoaderG)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 881, 439))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Local = PlotWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Local.setFont(font)
        self.Local.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(0, 0, 0);"))
        self.Local.setObjectName(_fromUtf8("Local"))
        self.gridLayout.addWidget(self.Local, 0, 0, 1, 1)
        self.Server = PlotWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Server.setFont(font)
        self.Server.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(0, 0, 0);"))
        self.Server.setObjectName(_fromUtf8("Server"))
        self.gridLayout.addWidget(self.Server, 0, 1, 1, 1)
        FileLoaderG.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FileLoaderG)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuAbout_Us = QtGui.QMenu(self.menubar)
        self.menuAbout_Us.setObjectName(_fromUtf8("menuAbout_Us"))
        FileLoaderG.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FileLoaderG)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FileLoaderG.setStatusBar(self.statusbar)
        self.actionFile_Loader_G = QtGui.QAction(FileLoaderG)
        self.actionFile_Loader_G.setObjectName(_fromUtf8("actionFile_Loader_G"))
        self.actionOpen = QtGui.QAction(FileLoaderG)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuit = QtGui.QAction(FileLoaderG)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout_Us.addAction(self.actionFile_Loader_G)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())

        self.retranslateUi(FileLoaderG)
        QtCore.QMetaObject.connectSlotsByName(FileLoaderG)

    def retranslateUi(self, FileLoaderG):
        FileLoaderG.setWindowTitle(_translate("FileLoaderG", "MainWindow", None))
        self.menuFile.setTitle(_translate("FileLoaderG", "File", None))
        self.menuSettings.setTitle(_translate("FileLoaderG", "Settings", None))
        self.menuAbout_Us.setTitle(_translate("FileLoaderG", "About Us", None))
        self.actionFile_Loader_G.setText(_translate("FileLoaderG", "File Loader G", None))
        self.actionOpen.setText(_translate("FileLoaderG", "Open", None))
        self.actionQuit.setText(_translate("FileLoaderG", "Quit", None))

from pyqtgraph import PlotWidget
