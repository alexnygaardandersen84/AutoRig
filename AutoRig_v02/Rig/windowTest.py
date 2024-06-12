import maya.cmds as m
import simple_Rig as simp
import groups as gp
import jointOrientation as jo
import utils_simpleRig as utils



def defaultButtonPush(*args):
  print ('Default was pushed.')

def StoredReference(*args):
  gp.groupsImport()
  print('Created Groups')
  

def controlOrientation(*args):
   utils.changeOrientationOrder()


def storedSimpleRigReference(*args):
   simp.autoLimbToolFunction()
   print('Created Rig')

def orientJointsToDifferentAxis(*args):
    m.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
    # xyz, yzx, zxy, zyx, yxz, xzy, none
    #jo.orientJoint()
    gp.orientJoint()
    #print ('OrientJointTODifferentAxis Pressed')

def orientLastJointInChain(*args):
   #jo.orientJoint()
   #gp.get_last_elements()
   #print ('OrientJointTODifferentAxis Pressed')
    m.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

    selectionCheck = m.select(hi=True)
    selectionCheck = m.ls(sl=1, type='joint')

    # Replace 'root_node' with the name of your root node or the top of your hierarchy
    #root_node = 'root_node'
    root_node = selectionCheck[0]

    last_elements = []
    gp.get_last_elements(root_node, last_elements)

    # 'last_elements' now contains the names of the last elements in the hierarchy
    print(last_elements)
    m.select(last_elements)
    for i in last_elements: 
       m.joint(e=1, oj=('none'), zso=1)
       

# Create a function to execute when an item is selected from the dropdown
def dropdown_selection_changed(*args):
    selected_option = m.optionMenu("myDropdown", query=True, value=True)
    print("Selected option:", selected_option)

    selected_option = m.optionMenu("myDropdown1", query=True, value=True)
    print("Selected option:", selected_option)

    selected_option = m.optionMenu("myDropdown2", query=True, value=True)
    print("Selected option:", selected_option)

    name1 = 'xzy'

def window():

    


    m.window( width=150 )
    m.columnLayout( adjustableColumn=True )
    m.button( label='Groups', command= StoredReference)
    m.button( label='Left', align='left', command =  defaultButtonPush)
    m.button( label='SimpleRig', align='center', command = storedSimpleRigReference)
    m.button( label='OrientJoints', align='right', command = orientJointsToDifferentAxis)
    m.button( label='OrientLastJointsElement', align='right', command = orientLastJointInChain)
    m.button( label='ControlOrientation', align='right', command = controlOrientation)
    m.optionMenu("myDropdown", label="Primary Axis", changeCommand=dropdown_selection_changed)
        #m.menuItem(dropdown_selection_changed())
    menuItem01 = m.menuItem(label="xzy")
    m.menuItem(label="Option 2")
    m.menuItem(label="Option 3")

    m.optionMenu("myDropdown1", label="Secondary Axis", changeCommand=dropdown_selection_changed)
        #m.menuItem(dropdown_selection_changed())
    m.menuItem(label="xzy")
    m.menuItem(label="Option 2")
    m.menuItem(label="Option 3")

    m.optionMenu("myDropdown2", label="Rotation Axis", changeCommand=dropdown_selection_changed)
        #m.menuItem(dropdown_selection_changed())
    m.menuItem(label="xzy")
    m.menuItem(label="Option 2")
    m.menuItem(label="Option 3")

    #m.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
    m.showWindow()








