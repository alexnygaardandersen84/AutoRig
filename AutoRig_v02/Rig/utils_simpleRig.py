import maya.cmds as m
import maya.mel as mel



#Priting CV positions
def printCvPosition(curveObj):

    """

    Use in maya: 

    import importlib
    import utils_simpleRig as MCommon
    importlib.reload(MCommon)

    crv = cmds.ls(sl=1)[0]
    MCommon.printCvPosition(crv)


    """

    cvs = m.ls(curveObj + '.cv[*]', fl=True)
    posList = []

    print ('pos = []')

    for cv in cvs:
        pos = m.xform(cv, q=1, t=1, ws=1)
        posList.append(pos)
        print ('pos.append([{},{},{}])'.format(pos[0], pos[1], pos[2]))
    return posList



def arrowSquare(curveScale=1.0, name=''):
    pos = []
    pos.append([-240.0,0.0,-240.0])
    pos.append([-240.0,0.0,240.0])
    pos.append([240.0,0.0,240.0])
    pos.append([240.0,0.0,-240.0])
    pos.append([-240.0,0.0,-240.0])


    crvSquare = m.curve(d=1, p=pos)
    m.rename(crvSquare, name, ignoreShape=0)


    pos = []
    pos.append([-388.61705751865725,0.0,0.26665608580091366])
    pos.append([-321.33664141276097,0.0,67.45480433998617])
    pos.append([-321.3597083756887,0.0,33.837663249965765])
    pos.append([-254.12542619564792,0.0,33.79152932411022])
    pos.append([-254.17156012150346,0.0,-33.44275285593057])
    pos.append([-321.4058423015442,0.0,-33.39661893007503])
    pos.append([-321.42890926447205,0.0,-67.01376002009542])
    pos.append([-388.61705751865725,0.0,0.26665608580091366])

    crv = m.curve(d=1, p=pos)
    m.rename(crv, 'Arrow_01', ignoreShape=0)
    m.select('Arrow_Shape1')
    ArrowSquareName = m.ls(sl=1)
    for i in ArrowSquareName:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 9)


    pos = []
    pos.append([0.648634982356731,0.0,388.61660769013355])
    pos.append([67.77061959210515,0.0,321.27018358864444])
    pos.append([34.15351741429577,0.0,321.3262934615796])
    pos.append([34.04129766842544,0.0,254.09208910596087])
    pos.append([-33.1929066871933,0.0,254.2043088518312])
    pos.append([-33.08068694132297,0.0,321.43851320744994])
    pos.append([-66.69778911913234,0.0,321.4946230803851])
    pos.append([0.648634982356731,0.0,388.61660769013355])

    crv = m.curve(d=1, p=pos)
    m.rename(crv, 'Arrow_02', ignoreShape=0)
    m.select('Arrow_Shape2')
    ArrowSquareName = m.ls(sl=1)
    for i in ArrowSquareName:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 9)


    pos = []
    pos.append([388.6169442771872,0.0,0.3988992216268644])
    pos.append([321.45169487895095,0.0,-66.90437655661188])
    pos.append([321.41718828395034,0.0,-33.28724526249313])
    pos.append([254.18292569571287,0.0,-33.35625845249437])
    pos.append([254.1139125057116,0.0,33.878004135743126])
    pos.append([321.34817509394907,0.0,33.94701732574437])
    pos.append([321.31366849894846,0.0,67.56414861986312])
    pos.append([388.6169442771872,0.0,0.3988992216268644])

    crv = m.curve(d=1, p=pos)
    m.rename(crv, 'Arrow_03', ignoreShape=0)
    m.select('Arrow_Shape3')
    ArrowSquareName = m.ls(sl=1)
    for i in ArrowSquareName:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 9)
        


    pos = []
    pos.append([1.4210854715202004e-14,0.0,-388.6171490039103])
    pos.append([-67.23429800782085,0.0,-321.3828509960895])
    pos.append([-33.61714900391042,0.0,-321.3828509960895])
    pos.append([-33.61714900391042,0.0,-254.1485529882686])
    pos.append([33.61714900391045,0.0,-254.1485529882686])
    pos.append([33.61714900391045,0.0,-321.3828509960895])
    pos.append([67.23429800782088,0.0,-321.3828509960895])
    pos.append([1.4210854715202004e-14,0.0,-388.6171490039103])

    crv = m.curve(d=1, p=pos)
    m.rename(crv, 'Arrow_04', ignoreShape=0)
    m.select('Arrow_Shape4')
    ArrowSquareName = m.ls(sl=1)
    for i in ArrowSquareName:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 9)


    m.parent('Arrow_Shape1', name, s=True, r=True)
    m.parent('Arrow_Shape2', name, s=True, r=True)
    m.parent('Arrow_Shape3', name, s=True, r=True)
    m.parent('Arrow_Shape4', name, s=True, r=True)
    m.delete('Arrow_01', 'Arrow_02', 'Arrow_03', 'Arrow_04')
    m.select(name) 

    m.scale(curveScale,curveScale,curveScale)
    m.makeIdentity( name, a=1, t=1, r=1, s=1)
    #Changing the color
    ArrowSquareName = m.ls(sl=1)
    for i in ArrowSquareName:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 1)

    m.select(cl=1)
        

def arrow(curveScale=1.0, name=''):
    pos = []
    pos.append([0.056109872935162786,0.0,33.63112964604318])
    pos.append([33.61710217780937,0.0,-0.04208240470137525])
    pos.append([16.808551088904682,0.0,-0.014027468233791751])
    pos.append([16.75244121596952,0.0,-33.63112964604316])
    pos.append([-16.864660961839853,0.0,-33.575019773108])
    pos.append([-16.80855108890469,0.0,0.04208240470137525])
    pos.append([-33.61710217780937,0.0,0.07013734116895876])
    pos.append([0.056109872935162786,0.0,33.63112964604318])

    crv = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crv, name, ignoreShape=0)


def ArrowControl(curveScale=1.0, name=''):
    pos = []
    pos.append([-3.0,0.0,-4.0])
    pos.append([-1.0,0.0,-4.0])
    pos.append([-1.0,0.0,-1.0])
    pos.append([-4.0,0.0,-1.0])
    pos.append([-4.0,0.0,-3.0])
    pos.append([-7.0,0.0,0.0])
    pos.append([-4.0,0.0,3.0])
    pos.append([-4.0,0.0,1.0])
    pos.append([-1.0,0.0,1.0])
    pos.append([-1.0,0.0,4.0])
    pos.append([-3.0,0.0,4.0])
    pos.append([0.0,0.0,7.0])
    pos.append([3.0,0.0,4.0])
    pos.append([1.0,0.0,4.0])
    pos.append([1.0,0.0,1.0])
    pos.append([4.0,0.0,1.0])
    pos.append([4.0,0.0,3.0])
    pos.append([7.0,0.0,0.0])
    pos.append([4.0,0.0,-3.0])
    pos.append([4.0,0.0,-1.0])
    pos.append([1.0,0.0,-1.0])
    pos.append([1.0,0.0,-4.0])
    pos.append([3.0,0.0,-4.0])
    pos.append([0.0,0.0,-7.0])
    pos.append([-3.0,0.0,-4.0])

    crv = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crv, name, ignoreShape=0)





def poleVectorControl(curveScale=1.0, name=''):
    pos = []
    pos.append([-7.0,0.0,0.0])
    pos.append([0.0,0.0,10.0])
    pos.append([7.0,0.0,0.0])
    pos.append([3.0,0.0,0.0])
    pos.append([3.0,0.0,-12.0])
    pos.append([-3.0,0.0,-12.0])
    pos.append([-3.0,0.0,0.0])
    pos.append([-7.0,0.0,0.0])
    crv = m.curve(d=1, p=pos)
    newMainCtrlName = m.rename(crv, name + str(1), ignoreShape=0)
    

    pos = []
    pos.append([0.0,7.0,0.0])
    pos.append([0.0,0.0,10.0])
    pos.append([0.0,-7.0,0.0])
    pos.append([0.0,-3.0,0.0])
    pos.append([0.0,-3.0,-12.0])
    pos.append([0.0,3.0,-12.0])
    pos.append([0.0,3.0,0.0])
    pos.append([0.0,7.0,0.0])
    crv = m.curve(d=1, p=pos)
    
    newName = m.rename(crv, 'PoleVectorControl_0' + str(1), ignoreShape=0)
    poleNumber = newName[-1::]
    #print(poleNumber)
    
    m.parent('PoleVectorControl_Shape' + poleNumber, newMainCtrlName, s=True, r=True)
    #m.select(newMainCtrlName)
    m.parent(newMainCtrlName, newName)


    m.scale(curveScale,curveScale,curveScale)
    m.makeIdentity( newMainCtrlName, a=1, t=1, r=1, s=1)
    m.select(newName)
    

    # When using this remember to delete: #m.delete(newName), or else there will be a lot of new folders. 
    # But I think I can only delete it after I know the specific control numbers I want.


def findAllJointsInHierarchy(selectionCheck, emptylist):
    jointHierarchy = m.listRelatives(selectionCheck, ad=1, type='joint')
    for i in jointHierarchy:
        #print(i)
        emptylist.append(i)


def box(curveScaleX, curveScaleY, curveScaleZ , name=''):
    pos = []
    pos.append([60.0,0.0,60.0])
    pos.append([60.0,0.0,-60.0])
    pos.append([-60.0,0.0,-60.0])
    pos.append([-60.0,0.0,60.0])
    pos.append([60.0,0.0,60.0])
    pos.append([-60.0,0.0,60.0])
    pos.append([-60.0,0.0,-60.0])
    pos.append([-60.0,120.0,-60.0])
    pos.append([-60.0,120.0,60.0])
    pos.append([-60.0,0.0,60.0])
    pos.append([60.0,0.0,60.0])
    pos.append([60.0,0.0,-60.0])
    pos.append([60.0,120.0,-60.0])
    pos.append([60.0,120.0,60.0])
    pos.append([60.0,0.0,60.0])
    pos.append([60.0,120.0,60.0])
    pos.append([60.0,120.0,-60.0])
    pos.append([-60.0,120.0,-60.0])
    pos.append([-60.0,120.0,60.0])
    pos.append([60.0,120.0,60.0])

    crv = m.curve(d=1, p=pos)
    m.scale(curveScaleX,curveScaleY,curveScaleZ)
    m.rename(crv, name, ignoreShape=0)

    object_name = name

    # Get the bounding box of the object
    bbox = m.exactWorldBoundingBox(object_name)

    # Calculate the center of the bounding box
    center_x = (bbox[0] + bbox[3]) / 2
    center_y = (bbox[1] + bbox[4]) / 2
    center_z = (bbox[2] + bbox[5]) / 2

    # Set the pivot point to the center of the bounding box
    m.xform(object_name, centerPivots=True)


def IKHandleCurve(curveScale, name='' ):
    pos = []
    pos.append([0.0,0.0,0.0])
    pos.append([0.0,0.0,-5.0])
    pos.append([1.0,0.0,-5.0])
    pos.append([1.0,0.0,0.0])
    pos.append([0.0,0.0,0.0])
    pos.append([2.0,0.0,0.0])
    pos.append([2.0,0.0,-5.0])
    pos.append([3.0,0.0,-5.0])
    pos.append([3.0,0.0,-3.0])
    pos.append([5.0,0.0,-5.0])
    pos.append([6.0,0.0,-5.0])
    pos.append([4.0,0.0,-3.0])
    pos.append([6.0,0.0,0.0])
    pos.append([5.0,0.0,0.0])
    pos.append([3.0,0.0,-2.0])
    pos.append([3.0,0.0,0.0])
    pos.append([2.0,0.0,0.0])
    crv = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crv, name, ignoreShape=0)

def FKHandleCurve(curveScale, name='' ):
    pos = []
    pos.append([0.0,0.0,0.0])
    pos.append([0.0,0.0,-5.0])
    pos.append([3.0,0.0,-5.0])
    pos.append([3.0,0.0,-4.0])
    pos.append([1.0,0.0,-4.0])
    pos.append([1.0,0.0,-3.0])
    pos.append([2.0,0.0,-3.0])
    pos.append([2.0,0.0,-2.0])
    pos.append([1.0,0.0,-2.0])
    pos.append([1.0,0.0,0.0])
    pos.append([0.0,0.0,0.0])
    pos.append([4.0,0.0,0.0])
    pos.append([4.0,0.0,-5.0])
    pos.append([5.0,0.0,-5.0])
    pos.append([5.0,0.0,-3.0])
    pos.append([6.0,0.0,-5.0])
    pos.append([7.0,0.0,-5.0])
    pos.append([5.634579420774764,0.0,-1.8939287095660702])
    pos.append([7.0,0.0,0.0])
    pos.append([6.0,0.0,0.0])
    pos.append([5.0,0.0,-1.0])
    pos.append([5.0,0.0,0.0])
    pos.append([4.0,0.0,0.0])
    crv = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crv, name, ignoreShape=0)

def clavicleCurve(curveScale, name='' ):
    pos = []
    pos.append([-12.0,0.0,7.0])
    pos.append([-8.0,0.0,-12.0])
    pos.append([8.0,0.0,-12.0])
    pos.append([12.0,0.0,7.0])
    pos.append([9.0,0.0,7.0])
    pos.append([6.0,0.0,-9.0])
    pos.append([-6.0,0.0,-9.0])
    pos.append([-9.0,0.0,7.0])
    pos.append([-12.0,0.0,7.0])
    crv = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crv, name, ignoreShape=0)
    object_name = name

    # Get the bounding box of the object
    bbox = m.exactWorldBoundingBox(object_name)

    # Calculate the center of the bounding box
    center_x = (bbox[0] + bbox[3]) / 2
    center_y = (bbox[1] + bbox[4]) / 2
    center_z = (bbox[2] + bbox[5]) / 2

    # Set the pivot point to the center of the bounding box
    m.xform(object_name, centerPivots=True)

def fingerArrow(curveScale, name='' ):
    pos = []
    pos.append([0.0,0.0,-5.999999830040185])
    pos.append([4.0,0.0,-9.999999830040185])
    pos.append([0.0,0.0,-13.999999830040185])
    pos.append([-4.0,0.0,-9.999999830040185])
    pos.append([0.0,0.0,-5.999999830040185])
    pos.append([0.0,0.0,1.6995981511058744e-07])
    crv = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crv, name, ignoreShape=0)



def changeOrientation():
    sel = m.select(type='joint')
    jointlist = m.ls(sl=1)
    jointlist = []
    m.listRelatives(type='joint', ad=True)
    for joint in jointlist:
        m.setAttr(joint + '.rotationOrder', 4)


def changeOrientationOrder():
    desired_rotation_order_controls_X = 0
    desired_rotation_order_controls_Y = 90
    desired_rotation_order_controls_Z = 0

    sel = m.select('*_offset')
    controlList = m.ls(sl=1)
    #print(controlList)


    for controls in controlList:
        m.setAttr(controls + '.rotateAxisX', desired_rotation_order_controls_X)
        m.setAttr(controls + '.rotateAxisY', desired_rotation_order_controls_Y)
        m.setAttr(controls + '.rotateAxisZ', desired_rotation_order_controls_Z)
        m.makeIdentity(a=1, r=1, s=1, t=1)

def sideBox(curveScale=1.0, name=''):
    pos = []
    pos.append([-240.0,0.0,-240.0])
    pos.append([-240.0,0.0,240.0])
    pos.append([240.0,0.0,240.0])
    pos.append([240.0,0.0,-240.0])
    pos.append([-240.0,0.0,-240.0])


    crvSquare = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crvSquare, name, ignoreShape=0)


def footControl(curveScale=1.0, name=''):
    pos = []
    pos.append([-2.250502391581163,0.0,-7.607652976830362])
    pos.append([-3.3668768151842627,0.0,-5.310096601696111])
    pos.append([-3.341552160188927,0.0,-1.0428416992323926])
    pos.append([-2.2787324148813823,0.0,1.734119155676908])
    pos.append([-2.252320801670674,0.0,3.849349045224051])
    pos.append([-2.591721605040319,0.0,5.247644162335687])
    pos.append([-2.3297414913473258,0.0,6.811513437671406])
    pos.append([-0.23930117031763287,0.0,8.397852013855639])
    pos.append([0.8672845043009991,0.0,8.553615887314825])
    pos.append([2.221182638847705,0.0,7.488064913333394])
    pos.append([2.846712328853446,0.0,5.451247003391023])
    pos.append([2.61102837016172,0.0,2.587062965423734])
    pos.append([2.928127736934715,0.0,-0.4534110191180569])
    pos.append([3.3668768151842627,0.0,-3.814055876640204])
    pos.append([2.8414291094240403,0.0,-6.5253160872050024])
    pos.append([1.9627645427736746,0.0,-7.7267833063082225])
    pos.append([-0.14735619114903442,0.0,-8.553615887314825])
    pos.append([-2.2563159213606143,0.0,-7.5132071057070355])
    crvSquare = m.curve(d=1, p=pos)
    m.scale(curveScale,curveScale,curveScale)
    m.rename(crvSquare, name, ignoreShape=0)

