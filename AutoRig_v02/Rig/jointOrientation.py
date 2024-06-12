import maya.cmds as m
import utils_simpleRig as utils
import simple_Rig as Rig

def orientJoint():

    print('hello')


    # Creating the opertunity to change joint orientation.
    
    # xyz, yzx, zxy, zyx, yxz, xzy, none
    jointOrientList = "xyz"
    #xup, xdown, yup, ydown, zup, zdown, none
    secondaryAxisOrientList = 'xup'
    

    m.select(hi=True) 
    jointlist = m.ls(sl=1)
    jointlist = []
    print(jointlist)

    for joints in jointlist:
        m.joint(e=1, oj=(jointOrientList), sao=(secondaryAxisOrientList), zso=1)
    
    print(jointlist)
    


    """    emptylist = []
    selectionCheck = m.ls(sl=1, type='joint')[0]
    selectionCheck01 = m.ls(sl=1,l=1 )[0].split('|')[1:4]
    for i in selectionCheck01: 
        emptylist.append(i)

    store = utils.findAllJointsInHierarchy(selectionCheck, emptylist)
    print(store)
    m.joint(e=1, oj=(jointOrientList), sao=(secondaryAxisOrientList), zso=1)
    """
    #This is for the last joint in the hiearchy
    #m.joint(e=1, oj=('none'), zso=1)