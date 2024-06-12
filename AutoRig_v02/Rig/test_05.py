# -*- coding: utf-8 -*-
import os
from maya import cmds
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from PyQt5.uic import loadUi
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
import sys
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

# designer.exeで作ったUIファイルを取得する
"""CURRENT_FILE = os.path.normpath(__file__)
path, ext = os.path.splitext(CURRENT_FILE)"""

path = "C:/Users/45533/Downloads/AutoRig_v02/Rig/AutomaticRigTool"

UI_FILE = path + ".ui"

class TRSConnectorWindow(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):
    def __init__(self, MainWindow):
        #QtWidgets.QMainWindow.__init__(self, MainWindow)
        super(TRSConnectorWindow, self).__init__(MainWindow)


        #path = "C:/Users/45533/Downloads/AutoRig_v02/Rig/"
        #uic.loadUi("AutomaticRigTool.ui", self)
        self.widget = QUiLoader().load(UI_FILE)
        self.setWindowTitle(self.widget.windowTitle())
        #self.ui = loadUi( path + 'AutomaticRigTool.ui', self)

        

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


        self.buttonPressed(self)

        #Moving the individual labels
        self.label.mouseMoveEvent = self.MoveWindow
        self.label_12.mouseMoveEvent = self.MoveWindow

        self.main_bg_stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def MoveWindow(self, event):
        delta = QPoint(event.globalPos() - self.clickPosition)
        print(delta)
        if self.isMaximized() == False: 
            self.move(self.pos() + event.globalPos() - self.clickPosition) 
            self.clickPosition = event.globalPos()
            event.accept()
            pass

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass

    def buttonPressed(self):
        self.pushButton_3.clicked.connect(self.clicked_03)


        self.pushButton_4.clicked.connect(self.clicked_04)

    def clicked_03(self):
        print("clicked button 3")
        #closeApp
        #sys.exit(MainApp.exec_())   

    def clicked_04(self):
        print("clicked button 4")
        #self.pushButton_4.clicked.connect(lambda: QStackedWidget.setCurrentWidget(self.page_02))    
        QtWidgets.QStackedWidget.setCurrentWidget(self.main_bg_stackedWidget, self.page_02)
 
#if __name__ == "__main__":
def showUI(self):
    MainApp = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    App = TRSConnectorWindow(MainWindow)
    App.show(self)
    global closeApp
    closeApp = sys.exit(MainApp.exec_())

if __name__ == "__main__":
    showUI()