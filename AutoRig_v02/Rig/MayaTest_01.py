from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds

# Import the generated Python code from Qt Designer
from AutomaticRigTool import Ui_MainWindow

class MayaUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MayaUI, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    """        # Connect button click event to a custom function
            self.ui.pushButton.clicked.connect(self.on_button_clicked)

        def on_button_clicked(self):
            # Function to be executed when the button is clicked
            cmds.polyCube()
    """
def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

def show_ui():
    global maya_ui
    try:
        maya_ui.close()  # Close the UI if it's already open
    except:
        pass
    maya_ui = MayaUI()
    maya_ui.show()

# Run the show_ui function when executing the script
show_ui()
