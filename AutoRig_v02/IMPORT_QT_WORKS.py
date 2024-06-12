path = "C:/Users/alexn/Desktop/AutoRig_v02/Rig"
if not path in sys.path: 
    sys.path.append(path)


from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUi
import sys
import icons_tools
import AutomaticRigTool as UI

import importlib
import groups
import utils_simpleRig
import simple_Rig
import windowTest as MCommon
importlib.reload(MCommon)
importlib.reload(groups)
importlib.reload(utils_simpleRig)
importlib.reload(simple_Rig)

import maya.cmds as m


class Custom_Title_UI(QtWidgets.QMainWindow):
    def __init__(self, MainWindow):
        QtWidgets.QMainWindow.__init__(self)


        path = "C:/Users/alexn/Desktop/AutoRig_v02/Rig/"
        #uic.loadUi("AutomaticRigTool.ui", self)
        self.ui = loadUi( path + 'AutomaticRigTool.ui', self)

        

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


        self.buttonPressed()

        #Moving the individual labels
        self.label.mouseMoveEvent = self.MoveWindow
        self.label_12.mouseMoveEvent = self.MoveWindow

        self.main_bg_stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def MoveWindow(self, event):
        delta = QPoint(event.globalPos() - self.clickPosition)
        #print(delta)
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
        
        
        self.pushButton_11.clicked.connect(self.clicked_11)
        
        self.pushButton_12.clicked.connect(self.clicked_12)
        
        self.pushButton_13.clicked.connect(self.clicked_13)
        
        self.pushButton_14.clicked.connect(self.clicked_14)
        
        self.pushButton_15.clicked.connect(self.clicked_15)
        

    def clicked_03(self):
        print("clicked button 3")
        print("Closed Application")
        App.close()
   

    def clicked_04(self):
        print("clicked button 4")
        #self.pushButton_4.clicked.connect(lambda: QStackedWidget.setCurrentWidget(self.page_02))    
        QtWidgets.QStackedWidget.setCurrentWidget(self.main_bg_stackedWidget, self.page_02)


    def clicked_11(self):
        print("clicked button 11")
        groups.groupsImport()
        print('Created Groups')


    def clicked_12(self):
        print("clicked button 12")
        simple_Rig.autoLimbToolFunction()
        print('Created Rig')



    def clicked_13(self):
        print("clicked button 13")
        m.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

        selectionCheck = m.select(hi=True)
        selectionCheck = m.ls(sl=1, type='joint')

        # Replace 'root_node' with the name of your root node or the top of your hierarchy
        #root_node = 'root_node'
        root_node = selectionCheck[0]

        last_elements = []
        groups.get_last_elements(root_node, last_elements)

        # 'last_elements' now contains the names of the last elements in the hierarchy
        print(last_elements)
        m.select(last_elements)
        for i in last_elements: 
        	m.joint(e=1, oj=('none'), zso=1)




    def clicked_14(self):
        print("clicked button 14")
        m.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
        # xyz, yzx, zxy, zyx, yxz, xzy, none
        groups.orientJoint()



    def clicked_15(self):
        print("clicked button 15")
        utils_simpleRig.changeOrientationOrder()
        


MainWindow = QtWidgets.QMainWindow()
App = Custom_Title_UI(MainWindow)
App.show()





