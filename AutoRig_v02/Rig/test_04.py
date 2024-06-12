# -*- coding: utf-8 -*-
import os
from maya import cmds
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

# designer.exeで作ったUIファイルを取得する
"""CURRENT_FILE = os.path.normpath(__file__)
path, ext = os.path.splitext(CURRENT_FILE)"""

path = "C:/Users/45533/Downloads/AutoRig_v02/Rig/AutomaticRigTool"

UI_FILE = path + ".ui"

class TRSConnectorWindow(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(TRSConnectorWindow, self).__init__(*args, **kwargs)

        
        self.widget = QUiLoader().load(UI_FILE)
        self.setWindowTitle(self.widget.windowTitle())

        
        self.setCentralWidget(self.widget)

        