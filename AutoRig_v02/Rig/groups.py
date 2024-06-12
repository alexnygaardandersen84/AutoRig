import maya.cmds as m
import utils_simpleRig as utils
import simple_Rig as Rig



def groupsImport(*args): 

    #Making a full list of the joints in the rig for creating controls
    #Emptylist is the full list of joints in the rig

    emptylist = []
    selectionCheck = m.ls(sl=1, type='joint')[0]
    selectionCheck01 = m.ls(sl=1,l=1 )[0].split('|')[1:4]
    for i in selectionCheck01: 
        emptylist.append(i)

    utils.findAllJointsInHierarchy(selectionCheck, emptylist)
    
    #Root
    #print(emptylist[2])

    #lowerarm_r
    #print(emptylist[37])

    #lowerarm_l
    #print(emptylist[64])

    #calf_r
    #print(emptylist[98])

    #calf_l
    #print(emptylist[85])
    
    #Check emptylist for a specific word
    #left_lowerarm = emptylist.index("lowerarm_l")
    #print(left_lowerarm)
        
    #print(emptylist)
    #for i in emptylist:
        #print(i)  
    
    #-------------------------------------------------------------------------------------------

    # Getting the root joint
    root = emptylist[2:3] 

    # Create the Root ctrl and parent it to the root joint
    main = utils.arrowSquare(1, 'mainRoot_Ctrl')
    main = m.setAttr('mainRoot_CtrlShape.lineWidth', 3)
    main = m.setAttr('Arrow_Shape1.lineWidth', 2)
    main = m.setAttr('Arrow_Shape2.lineWidth', 2)
    main = m.setAttr('Arrow_Shape3.lineWidth', 2)
    main = m.setAttr('Arrow_Shape4.lineWidth', 2)


    # Grouping the mainRoot_Ctrl under MainRoot_Ctrl_Offset
    group_main_parent = m.group( em=True, name='mainRoot_Ctrl_Offset' )
    m.parent('mainRoot_Ctrl', group_main_parent)
    
    
    # Changing the mainRoot_ctrl_offset to match the root control
    main = m.select('mainRoot_Ctrl_Offset')
    #m.manipPivot(o=(-90, 0, 0) )
    main = m.makeIdentity(a=1, t=1, r=1, s=1)

    #m.select(root)


    #adjustingOrient = m.parentConstraint(root, 'mainRoot_Ctrl_Offset')
    #m.delete(adjustingOrient)
    
    ###adjustingOrient = m.parentConstraint('mainRoot_Ctrl', root, mo=1)
    #-------------------------------------------------------------------------------------------
    # Extra?
    extra_name = 'mainRoot_Ctrl_Extra'
    extra = utils.sideBox(0.7, extra_name)
    group_extra_parent = m.group( em=True, name='mainRoot_Ctrl_Extra_Offset' )
    m.parent(extra_name, group_extra_parent)
    extra = m.setAttr("{}.overrideEnabled".format(extra_name ), 1)
    extra = m.setAttr("{}.overrideColor".format(extra_name ), 1)
    extra = m.setAttr('mainRoot_Ctrl_ExtraShape.lineWidth', 1)
    #extra = m.setAttr('mainRoot_Ctrl_ExtraShape.lineWidth', 1)

    #-------------------------------------------------------------------------------------------

    #Create the arm polevector ctrls for IK 
    poleVector_left_name = 'l_poleVector_ctrl'
    left = utils.poleVectorControl(2, poleVector_left_name)
    adjustingOrient = m.parentConstraint(emptylist[64], "PoleVectorControl_0" + str(1))
    m.delete(adjustingOrient)
    #adjustingOrient = m.parentConstraint("PoleVectorControl_0" + str(2), emptylist[37])
    #print(m.getAttr('PoleVectorControl_0' + str(1) + '.translate')[0])
   # m.setAttr('PoleVectorControl_0' + str(1) + '.translateY', 100)[0]
    left = m.setAttr(".translateZ", -200)
    #left = m.makeIdentity(a=1, t=1, r=1, s=1)
    left = m.setAttr("{}.overrideEnabled".format(poleVector_left_name + str(1) ), 1)
    left = m.setAttr("{}.overrideColor".format(poleVector_left_name + str(1) ), 14)
    #left = m.setAttr("{}.lineWidth".format(poleVector_left_name + str(1) ), 3)
    left = m.setAttr('PoleVectorControl_Shape1.lineWidth', 1)
    left = m.setAttr('l_poleVector_ctrlShape1.lineWidth', 1)
    



    #Move the control away from elbow
    #m.parentConstraint('l_poleVector_ctrl', emptylist[37])

    poleVector_right_name = 'r_poleVector_ctrl'
    right = utils.poleVectorControl(2, poleVector_right_name)
    adjustingOrient = m.parentConstraint(emptylist[37], "PoleVectorControl_0" + str(2))
    m.delete(adjustingOrient)
    #adjustingOrient = m.parentConstraint("PoleVectorControl_0" + str(2), emptylist[64])
    #print(m.getAttr('PoleVectorControl_0' + str(1) + '.translate')[0])
    right = m.setAttr(".translateZ", -200)
    right = m.setAttr("{}.overrideEnabled".format(poleVector_right_name + str(1) ), 1)
    right = m.setAttr("{}.overrideColor".format(poleVector_right_name + str(1) ), 13)
    right = m.setAttr('PoleVectorControl_Shape2.lineWidth', 1)
    right = m.setAttr('r_poleVector_ctrlShape1.lineWidth', 1)

 #-------------------------------------------------------------------------------------------
    #Create the leg polevector ctrls for IK 
    poleVector_left_leg_name = 'l_poleVector_leg_ctrl'
    leftLeg = utils.poleVectorControl(2, poleVector_left_leg_name)
    adjustingOrient = m.parentConstraint(emptylist[85], "PoleVectorControl_0" + str(3))
    m.delete(adjustingOrient)
    #adjustingOrient = m.parentConstraint("PoleVectorControl_0" + str(2), emptylist[37])
    #print(m.getAttr('PoleVectorControl_0' + str(1) + '.translate')[0])
   # m.setAttr('PoleVectorControl_0' + str(1) + '.translateY', 100)[0]
    
    leftLeg = m.setAttr(".translateZ", 200)
    
    #left = m.makeIdentity(a=1, t=1, r=1, s=1)
    leftLeg = m.setAttr("{}.overrideEnabled".format(poleVector_left_leg_name + str(1) ), 1)
    leftLeg = m.setAttr("{}.overrideColor".format(poleVector_left_leg_name + str(1) ), 14)
    #left = m.setAttr("{}.lineWidth".format(poleVector_left_name + str(1) ), 3)
    #leftLeg = m.setAttr('PoleVectorControl_Shape1.lineWidth', 1)
    #leftLeg = m.setAttr('l_poleVector_ctrlShape1.lineWidth', 1)
    



    #Move the control away from knee
    #m.parentConstraint('l_poleVector_ctrl', emptylist[37])

    poleVector_right_leg_name = 'r_poleVector_leg_ctrl'
    rightLeg = utils.poleVectorControl(2, poleVector_right_leg_name)
    rightLeg = m.setAttr("PoleVectorControl_04.rotateAxisY", 180)
    rightLeg = m.makeIdentity(a=1, r=1, s=1, t=1)   
    adjustingOrient = m.parentConstraint(emptylist[98], "PoleVectorControl_0" + str(4))
    m.delete(adjustingOrient)
    #adjustingOrient = m.parentConstraint("PoleVectorControl_0" + str(2), emptylist[64])
    #print(m.getAttr('PoleVectorControl_0' + str(1) + '.translate')[0])
    
    #rightLeg = m.setAttr("PoleVectorControl_04.rotateAxisY", 180)
    rightLeg = m.setAttr(".translateZ", 200)

    rightLeg = m.setAttr("{}.overrideEnabled".format(poleVector_right_leg_name + str(1) ), 1)
    rightLeg = m.setAttr("{}.overrideColor".format(poleVector_right_leg_name + str(1) ), 13)
    #rightLeg = m.setAttr('PoleVectorControl_Shape2.lineWidth', 1)
    #rightLeg = m.setAttr('r_poleVector_ctrlShape1.lineWidth', 1)
    

    #-------------------------------------------------------------------------------------------

 # leftSideList
    leftSideList = []  
    for i in emptylist:
        m.select('*_l')
        leftSideList.append(m.ls('*_l'))
    #print(leftSideList)
    m.select(cl=1)  

    rightSideList = []  
    for i in emptylist:
        m.select('*_r')
        rightSideList.append(m.ls('*_r'))
    #print(rightSideList)
    m.select(cl=1)  



    # Flattening the lists so they dont have multiple list entries
    flat_left_list = []
    for row in leftSideList:
        flat_left_list.extend(row)
    #print(flat_left_list)

    flat_right_list = []
    for row in rightSideList:
        flat_right_list.extend(row)
    #print(flat_right_list)


    # Checking index intry. 
    #Should maybe be moved to utilites instead
    """    left_upperarm = flat_left_list.index("upperarm_l")
    print(left_upperarm)
    left_lowerarm = flat_left_list.index("lowerarm_l")
    print(left_lowerarm)
    left_hand = flat_left_list.index("hand_l")
    print(left_hand)"""

    leftArmlist = []
    leftArmlist.append(flat_left_list[34])
    leftArmlist.append(flat_left_list[13])
    leftArmlist.append(flat_left_list[6])
    #print(leftArmlist)

    """    right_upperarm = flat_right_list.index("upperarm_r")
    print(right_upperarm)
    right_lowerarm = flat_right_list.index("lowerarm_r")
    print(right_lowerarm)
    right_hand = flat_right_list.index("hand_r")
    print(right_hand)"""

    rightArmlist = []
    rightArmlist.append(flat_right_list[34])
    rightArmlist.append(flat_right_list[13])
    rightArmlist.append(flat_right_list[6])
    #print(rightArmlist)

    """    left_thigh = flat_left_list.index("thigh_l")
    print(left_thigh)
    left_calf = flat_left_list.index("calf_l")
    print(left_calf)
    left_foot = flat_left_list.index("foot_l")
    print(left_foot)
    left_ball = flat_left_list.index("ball_l")
    print(left_ball)"""

    leftLegList = []
    leftLegList.append(flat_left_list[28])
    leftLegList.append(flat_left_list[1])
    leftLegList.append(flat_left_list[5])
    leftLegList.append(flat_left_list[0])
    #print(leftLegList)

    """    right_thigh = flat_right_list.index("thigh_r")
    print(right_thigh)
    right_calf = flat_right_list.index("calf_r")
    print(right_calf)
    right_foot = flat_right_list.index("foot_r")
    print(right_foot)
    right_ball = flat_right_list.index("ball_r")
    print(right_ball)"""

    rightLegList = []
    rightLegList.append(flat_right_list[28])
    rightLegList.append(flat_right_list[1])
    rightLegList.append(flat_right_list[5])
    rightLegList.append(flat_right_list[0])
    #print(rightLegList)
    
    # List to be used:
    # rightLegList = []
    # leftLegList = []
    # rightArmlist = []
    # leftArmlist = []

    scaleCtrl = 30
    scaleCtrlLeg_l = 80
    scaleCtrlLeg_r = 80

#-------------------------------------------------------------------------------------------

        # ARM

#-------------------------------------------------------------------------------------------
     # LEFT ARM CONTROLS


    #How many joints are we working with? 
    limbJoints_LeftArm = len(leftArmlist)


    #first define what controls we need
    newCtrlList = ['ik_ctrl','fk_ctrl']

    leftArmCtrlList = []

    
    
    # Create controls

    # Create controls and parent and orient them to the joints hierachy then delete their constraint
    for newJoint in newCtrlList: 
        for i in range(limbJoints_LeftArm):
            newCtrlName = leftArmlist[i] + '_arm' + '_' + newJoint
            #m.rotate( 0, '90deg', 0, r=True )
            m.circle(n=newCtrlName)
            m.scale(scaleCtrl,scaleCtrl,scaleCtrl)
            newCtrlNameGroup = m.group( newCtrlName, name = newCtrlName + '_offset' , w=1)


            m.setAttr(newCtrlNameGroup + '.rotateAxisY', 90)
            m.makeIdentity(a=1, r=1, s=1, t=1)  

            m.matchTransform(newCtrlNameGroup, leftArmlist[i])


            
            # m.delete(ch=1)
            # m.makeIdentity(newCtrlName, a=1, t=1, r=1, s=1, n=0, pn=1)

            #print(newCtrlName)
        
            leftArmCtrlList.append(newCtrlName)
            

        
        m.select(cl=1)
        #m.group((newCtrlList), n=(limbName + '_hand_control'))

    #print(leftArmCtrlList)

#-------------------------------------------------------------------------------------------
    
    
    # Group controls
    #scaleCtrl = 30
    #m.scale(scaleCtrl,scaleCtrl,scaleCtrl)

   

#----------------------------------------------------
    # Group the FK controls
    m.parent( 'lowerarm_l_arm_fk_ctrl_offset','upperarm_l_arm_fk_ctrl')

    m.parent( 'hand_l_arm_fk_ctrl_offset','lowerarm_l_arm_fk_ctrl')


 #---------------------------------------------------       
    # Group the IK controls

    #m.parent( 'upperarm_l_arm_ik_ctrl_offset','lowerarm_l_arm_ik_ctrl')

    #m.parent( 'hand_l_arm_ik_ctrl_offset','lowerarm_l_arm_ik_ctrl')

    m.parent( 'hand_l_arm_ik_ctrl_offset','upperarm_l_arm_ik_ctrl')
    m.delete('lowerarm_l_arm_ik_ctrl')
    

 #---------------------------------------------------   

    #Changing the color of FK
    fkGroup_leftArm = m.select('*l_arm_fk_ctrlShape')
    fkGroupTyp_LeftArm = m.ls(sl=1)
    for i in fkGroupTyp_LeftArm:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 14)

    #Changing the color of IK
    ikGroup_LeftArm = m.select('*l_arm_ik_ctrlShape')
    ikGroupTyp_LeftArm = m.ls(sl=1)
    for i in ikGroupTyp_LeftArm:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 13)
    

    m.group( 'upperarm_l_arm_fk_ctrl_offset','upperarm_l_arm_ik_ctrl_offset', name = 'l_arm_ctrls' , w=1)
    
    m.delete('lowerarm_l_arm_ik_ctrl_offset')
    
#-------------------------------------------------------------------------------------------
    
    # Group controls


    # RIGHT ARM CONTROLS


    #How many joints are we working with? 
    limbJoints_RightArm = len(rightArmlist)


    #first define what controls we need
    newCtrlList = ['ik_ctrl','fk_ctrl']

    RightArmCtrlList = []

    
    
    # Create controls

    # Create controls and parent and orient them to the joints hierachy then delete their constraint
    for newJoint in newCtrlList: 
        for i in range(limbJoints_RightArm):
            newCtrlName = rightArmlist[i] + '_arm' + '_' + newJoint
            #m.rotate( 0, '90deg', 0, r=True )
            """  m.circle(n=newCtrlName)
            m.matchTransform(newCtrlName, rightArmlist[i])
            m.scale(scaleCtrl,scaleCtrl,scaleCtrl)
            m.group( newCtrlName, name = newCtrlName + '_offset' , w=1)
            
            """

            m.circle(n=newCtrlName)
            m.scale(scaleCtrl,scaleCtrl,scaleCtrl)
            newCtrlNameGroup = m.group( newCtrlName, name = newCtrlName + '_offset' , w=1)


            m.setAttr(newCtrlNameGroup + '.rotateAxisY', 90)
            m.makeIdentity(a=1, r=1, s=1, t=1)  

            m.matchTransform(newCtrlNameGroup, rightArmlist[i])

            #print(newCtrlName)
        
            RightArmCtrlList.append(newCtrlName)
            

        
        m.select(cl=1)
        #m.group((newCtrlList), n=(limbName + '_hand_control'))

    #print(RightArmCtrlList)

#-------------------------------------------------------------------------------------------
    

#----------------------------------------------------
    # Group the FK controls
    m.parent( 'lowerarm_r_arm_fk_ctrl_offset','upperarm_r_arm_fk_ctrl')

    m.parent( 'hand_r_arm_fk_ctrl_offset','lowerarm_r_arm_fk_ctrl')


 #---------------------------------------------------       
    # Group the IK controls

    #m.parent( 'upperarm_r_arm_ik_ctrl_offset','lowerarm_r_arm_ik_ctrl')

    #m.parent( 'hand_r_arm_ik_ctrl_offset','lowerarm_r_arm_ik_ctrl')
    m.parent( 'hand_r_arm_ik_ctrl_offset','upperarm_r_arm_ik_ctrl')
    m.delete('lowerarm_r_arm_ik_ctrl')
    

 #---------------------------------------------------   

 #---------------------------------------------------   
    #Changing the color of FK
    fkGroup_rightArm = m.select('*r_arm_fk_ctrlShape')
    fkGroupTyp_RightArm = m.ls(sl=1)
    for i in fkGroupTyp_RightArm:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 14)

    #Changing the color of IK
    ikGroup_RightArm = m.select('*r_arm_ik_ctrlShape')
    ikGroupTyp_RightArm = m.ls(sl=1)
    for i in ikGroupTyp_RightArm:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 13)

    m.group( 'upperarm_r_arm_fk_ctrl_offset','upperarm_r_arm_ik_ctrl_offset', name = 'r_arm_ctrls' , w=1)
    
    m.delete('lowerarm_r_arm_ik_ctrl_offset')

    
#-------------------------------------------------------------------------------------------

    # LEG 
    
#-------------------------------------------------------------------------------------------
    
    
    # Group controls


    # LEFT LEG CONTROLS


    #How many joints are we working with? 
    limbJoints_LeftLeg = len(leftLegList)


    #first define what controls we need
    newCtrlList = ['ik_ctrl','fk_ctrl']

    leftLegCtrlList = []

    
    
    # Create controls

    # Create controls and parent and orient them to the joints hierachy then delete their constraint
    for newJoint in newCtrlList: 
        scaleCtrlLeg_l = 80
        for i in range(limbJoints_LeftLeg):
            newCtrlName = leftLegList[i] + '_leg' + '_' + newJoint
            #m.rotate( 0, '90deg', 0, r=True )
            """            m.circle(n=newCtrlName)
            m.matchTransform(newCtrlName, leftLegList[i])
            m.scale(scaleCtrl,scaleCtrl,scaleCtrl)
            m.group( newCtrlName, name = newCtrlName + '_offset' , w=1)
            """
            
            
            m.circle(n=newCtrlName)
            
            scaleCtrlLeg_l = scaleCtrlLeg_l  / 1.5   
            m.scale(scaleCtrlLeg_l, scaleCtrlLeg_l, scaleCtrlLeg_l)
 
            newCtrlNameGroup = m.group( newCtrlName, name = newCtrlName + '_offset' , w=1)

            m.setAttr(newCtrlNameGroup + '.rotateAxisY', 90)
            m.makeIdentity(a=1, r=1, s=1, t=1)  

            m.matchTransform(newCtrlNameGroup, leftLegList[i])

            leftLegCtrlList.append(newCtrlName)
            

        
        m.select(cl=1)
        #m.group((newCtrlList), n=(limbName + '_hand_control'))

    #print(leftLegCtrlList)
    
    m.delete('calf_l_leg_ik_ctrl_offset')
    #m.delete('calf_r_leg_ik_ctrl')
    m.delete('ball_l_leg_ik_ctrl_offset')
    #m.delete('ball_r_leg_ik_ctrl')


#-------------------------------------------------------------------------------------------

#----------------------------------------------------
    # Group the FK controls
    m.parent( 'calf_l_leg_fk_ctrl_offset', 'thigh_l_leg_fk_ctrl')

    m.parent( 'foot_l_leg_fk_ctrl_offset','calf_l_leg_fk_ctrl')

    m.parent( 'ball_l_leg_fk_ctrl_offset','foot_l_leg_fk_ctrl')


 #---------------------------------------------------       
    # Group the IK controls

    #m.parent( 'calf_l_leg_ik_ctrl_offset', 'thigh_l_leg_ik_ctrl')

    #m.parent( 'foot_l_leg_ik_ctrl_offset', 'thigh_l_leg_ik_ctrl')

    #m.parent( 'foot_l_leg_ik_ctrl_offset','calf_l_leg_ik_ctrl')

    #m.parent( 'ball_l_leg_ik_ctrl_offset','foot_l_leg_ik_ctrl')


 #---------------------------------------------------   

    #Changing the color of FK
    fkGroup_leftLeg = m.select('*l_leg_fk_ctrlShape')
    fkGroupTyp_LeftLeg = m.ls(sl=1)
    for i in fkGroupTyp_LeftLeg:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 14)

    #Changing the color of IK
    ikGroup_LeftLeg = m.select('*l_leg_ik_ctrlShape')
    ikGroupTyp_LeftLeg = m.ls(sl=1)
    for i in ikGroupTyp_LeftLeg:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 13)

    m.group( 'thigh_l_leg_ik_ctrl_offset','thigh_l_leg_fk_ctrl_offset', 'foot_l_leg_ik_ctrl_offset', name = 'l_leg_ctrls' , w=1)
    
#-------------------------------------------------------------------------------------------
    
    # Group controls


    # RIGHT LEG CONTROLS


    #How many joints are we working with? 
    limbJoints_RightLeg = len(rightLegList)


    #first define what controls we need
    newCtrlList = ['ik_ctrl','fk_ctrl']

    RightLegCtrlList = []

    
    
    # Create controls

    # Create controls and parent and orient them to the joints hierachy then delete their constraint
    for newJoint in newCtrlList:
        scaleCtrlLeg_r = 80 
        for i in range(limbJoints_RightLeg):
            newCtrlName = rightLegList[i] + '_leg' + '_' + newJoint
            #m.rotate( 0, '90deg', 0, r=True )
            """m.circle(n=newCtrlName)
            m.matchTransform(newCtrlName, rightLegList[i])
            m.scale(scaleCtrl,scaleCtrl,scaleCtrl)
            m.group( newCtrlName, name = newCtrlName + '_offset' , w=1)"""
            
            m.circle(n=newCtrlName)
            scaleCtrlLeg_r = scaleCtrlLeg_r  / 1.5   
            m.scale(scaleCtrlLeg_r, scaleCtrlLeg_r, scaleCtrlLeg_r)
 
            newCtrlNameGroup = m.group( newCtrlName, name = newCtrlName + '_offset' , w=1)

            m.setAttr(newCtrlNameGroup + '.rotateAxisY', 90)
            m.makeIdentity(a=1, r=1, s=1, t=1)  

            m.matchTransform(newCtrlNameGroup, rightLegList[i])

        
            RightLegCtrlList.append(newCtrlName)
            

        
        m.select(cl=1)
        #m.group((newCtrlList), n=(limbName + '_hand_control'))

    #print(RightLegCtrlList)

    m.delete('calf_r_leg_ik_ctrl_offset')
    #m.delete('calf_r_leg_ik_ctrl')
    m.delete('ball_r_leg_ik_ctrl_offset')
    #m.delete('ball_r_leg_ik_ctrl')

#-------------------------------------------------------------------------------------------
    

#----------------------------------------------------
    # Group the FK controls
    m.parent( 'calf_r_leg_fk_ctrl_offset', 'thigh_r_leg_fk_ctrl')

    m.parent( 'foot_r_leg_fk_ctrl_offset','calf_r_leg_fk_ctrl')

    m.parent( 'ball_r_leg_fk_ctrl_offset','foot_r_leg_fk_ctrl')


 #---------------------------------------------------       
    # Group the IK controls

   # m.parent( 'calf_r_leg_ik_ctrl_offset', 'thigh_r_leg_ik_ctrl')

    #m.parent( 'foot_r_leg_ik_ctrl_offset', 'thigh_r_leg_ik_ctrl')

    #m.parent( 'foot_r_leg_ik_ctrl_offset','calf_r_leg_ik_ctrl')

    #m.parent( 'ball_r_leg_ik_ctrl_offset','foot_r_leg_ik_ctrl')


 #---------------------------------------------------   
    #Changing the color of FK
    fkGroup_rightLeg = m.select('*r_leg_fk_ctrlShape')
    fkGroupTyp_RightLeg = m.ls(sl=1)
    for i in fkGroupTyp_RightLeg:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 14)

    #Changing the color of IK
    ikGroup_RightLeg = m.select('*r_leg_ik_ctrlShape')
    ikGroupTyp_RightLeg = m.ls(sl=1)
    for i in ikGroupTyp_RightLeg:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 13)

    m.group( 'thigh_r_leg_ik_ctrl_offset','thigh_r_leg_fk_ctrl_offset', 'foot_r_leg_ik_ctrl_offset', name = 'r_leg_ctrls' , w=1)
   
#-------------------------------------------------------------------------------------------
   

#-------------------------------------------------------------------------------------------

    # SPINE CONTROLS

#-------------------------------------------------------------------------------------------
    radius = 70


    m.circle(n='spine01_ctrl', r=radius)
    m.group('spine01_ctrl', name = 'spine01_ctrl_Offset')
    m.setAttr("spine01_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('spine_01', 'spine01_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*spine01_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)


    m.circle(n='spine02_ctrl', r=radius)
    m.group('spine02_ctrl', name = 'spine02_ctrl_Offset')
    m.setAttr("spine02_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('spine_02', 'spine02_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*spine02_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)
    

    m.circle(n='spine03_ctrl', r=radius)
    m.group('spine03_ctrl', name = 'spine03_ctrl_Offset')
    m.setAttr("spine03_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('spine_03', 'spine03_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*spine03_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)


    m.circle(n='spine04_ctrl', r=radius)
    m.group('spine04_ctrl', name = 'spine04_ctrl_Offset')
    m.setAttr("spine04_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('spine_04', 'spine04_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*spine04_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)


    m.circle(n='spine05_ctrl', r=radius)
    m.group('spine05_ctrl', name = 'spine05_ctrl_Offset')
    m.setAttr("spine05_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('spine_05', 'spine05_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*spine05_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)

#-------------------------------------------------------------------------------------------
    # NECK
    radiusNeck = 40

    m.circle(n='neck01_ctrl', r=radiusNeck)
    m.group('neck01_ctrl', name = 'neck01_ctrl_Offset')
    m.setAttr("neck01_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('neck_01', 'neck01_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*neck01_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)


    m.circle(n='neck02_ctrl', r=radiusNeck)
    m.group('neck02_ctrl', name = 'neck02_ctrl_Offset')
    m.setAttr("neck02_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('neck_02', 'neck02_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*neck02_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)

#-------------------------------------------------------------------------------------------

    # Head
    curveScaleX = 1
    curveScaleY = 1
    curveScaleZ = 1

    utils.box(curveScaleX, curveScaleY, curveScaleZ , 'head_ctrl')
    #m.circle(n='neck02_ctrl', r=radiusNeck)
    m.group('head_ctrl', name = 'head_ctrl_Offset')
    m.setAttr("head_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('head', 'head_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*head_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)

#-------------------------------------------------------------------------------------------

    # Pelvis / COG CONTROL
    curveScaleX = 1.2
    curveScaleY = 1
    curveScaleZ = 0.8

    utils.box(curveScaleX, curveScaleY, curveScaleZ , 'pelvis_ctrl')
    #m.circle(n='neck02_ctrl', r=radiusNeck)
    m.group('pelvis_ctrl', name = 'pelvis_ctrl_Offset')
    m.setAttr("pelvis_ctrl_Offset.rotateAxisY", 90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('pelvis', 'pelvis_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*pelvis_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)

#-------------------------------------------------------------------------------------------

    # Waist control - I THINK THIS IS WHAT CAUSES OUR JOINT TO TURN WHEN DELETING THIS
    waistScale = 100

    m.circle(n='waist_ctrl', r=waistScale)
    m.group('waist_ctrl', name = 'waist_ctrl_Offset')
    m.parent('waist_ctrl_Offset','pelvis_ctrl', r=True)
    #m.parent('waist_ctrl_Offset', 'pelvis_ctrl'   , r=True)
    temp = m.parentConstraint('spine_01', 'waist_ctrl_Offset' )
    m.delete(temp)
    m.makeIdentity(a=1, r=1, s=1, t=1)
    #m.xform('waist_ctrl_Offset', translation=(0, -80,0)) 
    m.setAttr("waist_ctrl_Offset.rotateAxisY", 90)
    m.setAttr("waist_ctrl_Offset.translateX", -90)  
    #m.setAttr("waist_ctrl_Offset.rotateAxisZ", 90)  
    SpineGrp = m.select('*waist_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)

     
    # Replace these with the names of your control and group
    control_name_offset = 'spine_01'
    group_name_offset = 'waist_ctrl_Offset'

    # Get the pivot position of the control
    control_pivot_offset = m.xform(control_name_offset, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name_offset, piv=control_pivot_offset, ws=True)   

    control_name = 'spine_01'
    group_name = 'waist_ctrl'

    # Get the pivot position of the control
    control_pivot = m.xform(control_name, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name, piv=control_pivot, ws=True)   

    m.makeIdentity(a=1, r=1, s=1, t=1)


    m.parentConstraint('waist_ctrl', 'pelvis'  , mo=True)

    m.parent('thigh_l_leg_ik_ctrl_offset', 'thigh_l_leg_fk_ctrl_offset', 'thigh_r_leg_ik_ctrl_offset','thigh_r_leg_fk_ctrl_offset', 'waist_ctrl')

    #m.parent('waist_ctrl_Offset','pelvis_ctrl', r=True)

    #m.parent( 'spine01_ctrl_Offset', 'waist_ctrl')

#-------------------------------------------------------------------------------------------
    # CLAVICLE CONTROLS
    radiusClavicle = 5

    utils.clavicleCurve(radiusClavicle, 'clavicle_l_ctrl')
    #m.circle(n='clavicle_l_ctrl', r=radiusNeck)
    m.group('clavicle_l_ctrl', name = 'clavicle_l_ctrl_Offset')
    #m.setAttr("clavicle_l_ctrl_Offset.rotateAxisX", -90)
    m.setAttr("clavicle_l_ctrl_Offset.rotateAxisY", 180)
    m.setAttr("clavicle_l_ctrl_Offset.rotateAxisZ", 90)
    m.xform('clavicle_l_ctrl', translation=(0, -60, 0))
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('clavicle_l', 'clavicle_l_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*clavicle_l_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)

    # Replace these with the names of your control and group
    control_name_offset = 'clavicle_l'
    group_name_offset = 'clavicle_l_ctrl'

    # Get the pivot position of the control
    control_pivot_offset = m.xform(control_name_offset, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name_offset, piv=control_pivot_offset, ws=True)   


#---------------------------------------------------------------

    utils.clavicleCurve(radiusClavicle, 'clavicle_r_ctrl')
    #m.circle(n='clavicle_r_ctrl', r=radiusNeck)
    m.group('clavicle_r_ctrl', name = 'clavicle_r_ctrl_Offset')
    #m.setAttr("clavicle_r_ctrl_Offset.rotateAxisX", -90)
    m.setAttr("clavicle_r_ctrl_Offset.rotateAxisY", -35)
    m.setAttr("clavicle_r_ctrl_Offset.rotateAxisZ", -90)
    m.xform('clavicle_r_ctrl', translation=(0, -60, 0))
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('clavicle_r', 'clavicle_r_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*clavicle_r_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)

    # Replace these with the names of your control and group
    control_name_offset = 'clavicle_r'
    group_name_offset = 'clavicle_r_ctrl'

    # Get the pivot position of the control
    control_pivot_offset = m.xform(control_name_offset, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name_offset, piv=control_pivot_offset, ws=True)   
    
#-------------------------------------------------------------------------------------------

    # IK FOOT CONTROLS

#-------------------------------------------------------------------------------------------
    """   footRadius = 10

    utils.footControl(footRadius, 'foot_l_ctrl')
    #m.circle(n='clavicle_r_ctrl', r=radiusNeck)
    m.group('foot_l_ctrl', name = 'foot_l_ctrl_Offset')
    m.setAttr("foot_l_ctrl_Offset.rotateAxisX", 20)
    m.setAttr("foot_l_ctrl_Offset.rotateAxisY", 90)
    m.setAttr("foot_l_ctrl_Offset.rotateAxisZ", 200)
    m.xform('foot_l_ctrl', translation=(0, 0, -45))
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('heel_l_end_lev', 'foot_l_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*foot_l_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)
    

    utils.footControl(footRadius, 'foot_r_ctrl')
    #m.circle(n='clavicle_r_ctrl', r=radiusNeck)
    m.group('foot_r_ctrl', name = 'foot_r_ctrl_Offset')
    m.setAttr("foot_r_ctrl_Offset.rotateAxisX", 0)
    m.setAttr("foot_r_ctrl_Offset.rotateAxisY", -90)
    m.setAttr("foot_r_ctrl_Offset.rotateAxisZ", 180)
    m.xform('foot_r_ctrl', translation=(0, 0, -45))
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('heel_r_end_rev', 'foot_r_ctrl_Offset' )
    m.delete(temp)
    SpineGrp = m.select('*foot_r_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)
    """


#-------------------------------------------------------------------------------------------


    # ARM SWITCHS

#-------------------------------------------------------------------------------------------


    # 
    #Create control for IK_FX blending

    switch_control = utils.FKHandleCurve(5, 'l_FK_arm_IK_FK_ctrl')
    switch_arm_l_FK_offset = m.group('l_FK_arm_IK_FK_ctrl', n='FK_switch_arm_l_offset')

    switch_arm_l_FK_offset = parent1 = m.parentConstraint('hand_l', 'FK_switch_arm_l_offset')
    switch_arm_l_FK_offset = m.delete(parent1)
    switch_arm_l_FK_offset = m.rotate(90,0,0)
    switch_arm_l_FK_offset = m.move(0,0,-100, r=1, os=1, wd=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.tx", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.ty", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.tz", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.rx", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.ry", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.rz", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.sx", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.sy", lock=1)
    switch_arm_l_FK_offset = m.setAttr ("l_FK_arm_IK_FK_ctrl.sz", lock=1)




    switch_control = utils.IKHandleCurve(5, 'l_IK_arm_IK_FK_ctrl')
    switch_arm_l_IK_offset = m.group('l_IK_arm_IK_FK_ctrl', n='IK_switch_arm_l_offset')

    switch_arm_l_IK_offset = parent3 = m.parentConstraint('hand_l', 'IK_switch_arm_l_offset')
    switch_arm_l_IK_offset = m.delete(parent3)
    switch_arm_l_IK_offset = m.rotate(90,0,0)
    switch_arm_l_IK_offset = m.move(0,0,-100, r=1, os=1, wd=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.tx", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.ty", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.tz", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.rx", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.ry", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.rz", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.sx", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.sy", lock=1)
    switch_arm_l_IK_offset = m.setAttr ("l_IK_arm_IK_FK_ctrl.sz", lock=1)


    

    switch_control = utils.FKHandleCurve(5, 'r_FK_arm_IK_FK_ctrl')
    switch_arm_r_FK_offset = m.group('r_FK_arm_IK_FK_ctrl', n='FK_switch_arm_r_offset')

    switch_arm_r_FK_offset = parent2 = m.parentConstraint('hand_r', 'FK_switch_arm_r_offset')
    switch_arm_r_FK_offset = m.delete(parent2)
    switch_arm_r_FK_offset = m.rotate(90,0,0)
    switch_arm_r_FK_offset = m.move(0,0,-100, r=1, os=1, wd=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.tx", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.ty", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.tz", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.rx", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.ry", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.rz", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.sx", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.sy", lock=1)
    switch_arm_r_FK_offset = m.setAttr ("r_FK_arm_IK_FK_ctrl.sz", lock=1)




    switch_control = utils.IKHandleCurve(5, 'r_IK_arm_IK_FK_ctrl')
    switch_arm_r_IK_offset = m.group('r_IK_arm_IK_FK_ctrl', n='IK_switch_arm_r_offset')

    switch_arm_r_IK_offset = parent4 = m.parentConstraint('hand_r', 'IK_switch_arm_r_offset')
    switch_arm_r_IK_offset = m.delete(parent4)
    switch_arm_r_IK_offset = m.rotate(90,0,0)
    switch_arm_r_IK_offset = m.move(0,0,-100, r=1, os=1, wd=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.tx", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.ty", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.tz", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.rx", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.ry", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.rz", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.sx", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.sy", lock=1)
    switch_arm_r_IK_offset = m.setAttr ("r_IK_arm_IK_FK_ctrl.sz", lock=1)






    """    Switch_Control = m.select('*switch*')
    Switch_Control_Typ = m.ls(sl=1)
    for i in Switch_Control_Typ:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 9)"""



    #-------------------------------------------------------------------------------------------

    #Create actual switch: 

    switch_control = utils.arrow(0.5, 'main_switch_left_IK_FK_Control')
    switch_arm_main_offset = m.group('main_switch_left_IK_FK_Control', n='main_switch_left_IK_FK_Control_offset')
    switch_arm_main_offset = parent1 = m.parentConstraint('hand_l', 'main_switch_left_IK_FK_Control_offset')
    switch_arm_main_offset = m.delete(parent1)
    switch_arm_main_offset = m.move(0,0,50, r=1, os=1, wd=1)




    switch_control = utils.arrow(0.5, 'main_switch_right_IK_FK_Control')
    switch_arm_main_offset = m.group('main_switch_right_IK_FK_Control', n='main_switch_right_IK_FK_Control_offset')
    
    #switch_arm_main_offset = m.setAttr("main_switch_right_IK_FK_Control_offset.rotateAxisY", 90)
    #switch_arm_main_offset = m.makeIdentity(a=1, r=1, s=1, t=1)   
    
    switch_arm_main_offset = parent2 = m.parentConstraint('hand_r', 'main_switch_right_IK_FK_Control_offset')
    switch_arm_main_offset = m.delete(parent2)
    switch_arm_main_offset = m.move(0,0,-50, r=1, os=1, wd=1)
    #switch_arm_main_offset = m.setAttr('main_switch_right_IK_FK_Control_offset' + '.rotateAxisX', 180)
    



#-------------------------------------------------------------------------------------------


    # Change color for all the switch controls
    Switch_Control = m.select('*switch*')
    Switch_Control_Typ = m.ls(sl=1)
    for i in Switch_Control_Typ:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 9)


#-------------------------------------------------------------------------------------------

    Switch_Control = m.select('*switch_arm_l*')
    Switch_Control_Typ = m.ls(sl=1)
    m.parent(Switch_Control_Typ, 'main_switch_left_IK_FK_Control')


    Switch_Control = m.select('*switch_arm_r*')
    Switch_Control_Typ = m.ls(sl=1)
    m.parent(Switch_Control_Typ, 'main_switch_right_IK_FK_Control')

#-------------------------------------------------------------------------------------------
    #Group all in one group? Might not be needed
    #Switch_Control = m.select('*switch*')
    #Switch_Control_Typ = m.ls(sl=1)
    #m.group(Switch_Control_Typ, n='Switch_grp')

    # LEFT ARM SWITCH CONTROL ATTRIBUTES

    # Creating the switch functionality for the switch control
    switch_ctrl = 'main_switch_left_IK_FK_Control'

    # Add an enum attribute to the switch control
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName="switch", attributeType="enum", enumName="FK:IK:", keyable=True)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName="seperator_01", nn = 'seperator', attributeType="enum", enumName="------------", keyable=True)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName='fist', attributeType="float", keyable=True, defaultValue=0, minValue=-1, maxValue=1)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName="seperator_02", nn = 'seperator', attributeType="enum", enumName="------------", keyable=True)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName='thumb', attributeType="float", keyable=True, defaultValue=0, minValue=-1, maxValue=1)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName='index', attributeType="float", keyable=True, defaultValue=0, minValue=-1, maxValue=1)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName='middle', attributeType="float", keyable=True, defaultValue=0, minValue=-1, maxValue=1)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName='ring', attributeType="float", keyable=True, defaultValue=0, minValue=-1, maxValue=1)
    AttributesOnSwitch = m.addAttr(switch_ctrl, longName='pinky', attributeType="float", keyable=True, defaultValue=0, minValue=-1, maxValue=1)
    AttributesOnSwitch = m.setAttr ( switch_ctrl +".seperator_01", lock=1)
    AttributesOnSwitch = m.setAttr ( switch_ctrl +".seperator_02", lock=1)

    #FK and IK symbols 
    object1 = "l_FK_arm_IK_FK_ctrl"  
    object2 = "l_IK_arm_IK_FK_ctrl" 

    # Objects for arm controls

    #FK
    object3 = 'upperarm_l_arm_fk_ctrl'
    object4 = 'lowerarm_l_arm_fk_ctrl'
    object5 = 'hand_l_arm_fk_ctrl'


    #IK
    #object6 = 'lowerarm_l_arm_ik_ctrl'
    object7 = 'upperarm_l_arm_ik_ctrl'
    object8 = 'hand_l_arm_ik_ctrl'
    object9 = 'l_poleVector_ctrl1'



    # Create a condition node to switch visibility based on the enum attribute
    condition_node = m.createNode("condition", name="visibility_condition")
    m.setAttr(f"{condition_node}.secondTerm", 1)
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.firstTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object1}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object3}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object4}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object5}.visibility")


    condition_node = m.createNode("condition", name="visibility_condition_02")
    m.setAttr(f"{condition_node}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.secondTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object2}.visibility")
    #m.connectAttr(f"{condition_node}.outColorR", f"{object6}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object7}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object8}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object9}.visibility")

#----------------------------------------------------------------------------

    # RIGHT ARM SWITCH CONTROL ATTRIBUTES


    # Creating the switch functionality for the switch control
    switch_ctrl = 'main_switch_right_IK_FK_Control'

    # Add an enum attribute to the switch control
    m.addAttr(switch_ctrl, longName="switch", attributeType="enum", enumName="FK:IK:", keyable=True)
    m.addAttr(switch_ctrl, longName='fist', attributeType="float", keyable=True)


    #FK and IK symbols 
    object1 = "r_FK_arm_IK_FK_ctrl"  
    object2 = "r_IK_arm_IK_FK_ctrl" 

    # Objects for arm controls

    #FK
    object3 = 'upperarm_r_arm_fk_ctrl'
    object4 = 'lowerarm_r_arm_fk_ctrl'
    object5 = 'hand_r_arm_fk_ctrl'

    #IK
    #object6 = 'lowerarm_l_arm_ik_ctrl'
    object7 = 'upperarm_r_arm_ik_ctrl'
    object8 = 'hand_r_arm_ik_ctrl'
    object9 = 'r_poleVector_ctrl1'



    # Create a condition node to switch visibility based on the enum attribute
    condition_node = m.createNode("condition", name="visibility_condition_03")
    m.setAttr(f"{condition_node}.secondTerm", 1)
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.firstTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object1}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object3}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object4}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object5}.visibility")


    condition_node = m.createNode("condition", name="visibility_condition_04")
    m.setAttr(f"{condition_node}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.secondTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object2}.visibility")
    #m.connectAttr(f"{condition_node}.outColorR", f"{object6}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object7}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object8}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object9}.visibility")


#-------------------------------------------------------------------------------------------

    # SWITCHS LEG

#-------------------------------------------------------------------------------------------

    # 
    #Create control for IK_FX blending

    switch_control = utils.FKHandleCurve(5, 'l_FK_leg_IK_FK_ctrl')
    switch_leg_l_FK_offset = m.group('l_FK_leg_IK_FK_ctrl', n='FK_switch_leg_l_offset')

    switch_leg_l_FK_offset = parent1 = m.parentConstraint('calf_l', 'FK_switch_leg_l_offset')
    switch_leg_l_FK_offset = m.delete(parent1)
    switch_leg_l_FK_offset = m.rotate(90,0,0)
    switch_leg_l_FK_offset = m.move(100,0,0, r=1, os=1, wd=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.tx", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.ty", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.tz", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.rx", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.ry", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.rz", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.sx", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.sy", lock=1)
    switch_leg_l_FK_offset = m.setAttr ("l_FK_leg_IK_FK_ctrl.sz", lock=1)




    switch_control = utils.IKHandleCurve(5, 'l_IK_leg_IK_FK_ctrl')
    switch_leg_l_IK_offset = m.group('l_IK_leg_IK_FK_ctrl', n='IK_switch_leg_l_offset')

    switch_leg_l_IK_offset = parent3 = m.parentConstraint('calf_l', 'IK_switch_leg_l_offset')
    switch_leg_l_IK_offset = m.delete(parent3)
    switch_leg_l_IK_offset = m.rotate(90,0,0)
    switch_leg_l_IK_offset = m.move(100,0,0, r=1, os=1, wd=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.tx", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.ty", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.tz", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.rx", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.ry", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.rz", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.sx", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.sy", lock=1)
    switch_leg_l_IK_offset = m.setAttr ("l_IK_leg_IK_FK_ctrl.sz", lock=1)


    

    switch_control = utils.FKHandleCurve(5, 'r_FK_leg_IK_FK_ctrl')
    switch_leg_r_FK_offset = m.group('r_FK_leg_IK_FK_ctrl', n='FK_switch_leg_r_offset')

    switch_leg_r_FK_offset = parent2 = m.parentConstraint('calf_r', 'FK_switch_leg_r_offset')
    switch_leg_r_FK_offset = m.delete(parent2)
    switch_leg_r_FK_offset = m.rotate(90,0,0)
    switch_leg_r_FK_offset = m.move(-100,0, 0, r=1, os=1, wd=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.tx", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.ty", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.tz", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.rx", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.ry", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.rz", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.sx", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.sy", lock=1)
    switch_leg_r_FK_offset = m.setAttr ("r_FK_leg_IK_FK_ctrl.sz", lock=1)




    switch_control = utils.IKHandleCurve(5, 'r_IK_leg_IK_FK_ctrl')
    switch_leg_r_IK_offset = m.group('r_IK_leg_IK_FK_ctrl', n='IK_switch_leg_r_offset')

    switch_leg_r_IK_offset = parent4 = m.parentConstraint('calf_r', 'IK_switch_leg_r_offset')
    switch_leg_r_IK_offset = m.delete(parent4)
    switch_leg_r_IK_offset = m.rotate(90,0,0)
    switch_leg_r_IK_offset = m.move(-100,0,0, r=1, os=1, wd=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.tx", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.ty", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.tz", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.rx", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.ry", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.rz", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.sx", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.sy", lock=1)
    switch_leg_r_IK_offset = m.setAttr ("r_IK_leg_IK_FK_ctrl.sz", lock=1)



    #-------------------------------------------------------------------------------------------

    #Create actual switch: 

    switch_control = utils.arrow(0.5, 'main_switch_left_IK_FK_Control_leg')
    switch_arm_main_offset = m.group('main_switch_left_IK_FK_Control_leg', n='main_switch_left_IK_FK_Control_leg_offset')
    switch_arm_main_offset = parent1 = m.parentConstraint('calf_l', 'main_switch_left_IK_FK_Control_leg_offset')
    switch_arm_main_offset = m.delete(parent1)
    switch_arm_main_offset = m.move(0,0,50, r=1, os=1, wd=1)




    switch_control = utils.arrow(0.5, 'main_switch_right_IK_FK_Control_leg')
    switch_arm_main_offset = m.setAttr("main_switch_right_IK_FK_Control_leg.rotateAxisY", 180)
    switch_arm_main_offset = m.makeIdentity(a=1, r=1, s=1, t=1)  

    switch_arm_main_offset = m.group('main_switch_right_IK_FK_Control_leg', n='main_switch_right_IK_FK_Control_leg_offset')

    switch_arm_main_offset = parent2 = m.parentConstraint('calf_r', 'main_switch_right_IK_FK_Control_leg_offset')
    switch_arm_main_offset = m.delete(parent2)
    switch_arm_main_offset = m.move(0,0,-50, r=1, os=1, wd=1)
    #switch_arm_main_offset = m.setAttr('main_switch_right_IK_FK_Control_offset' + '.rotateAxisX', 180)
    



#-------------------------------------------------------------------------------------------


    # Change color for all the switch controls
    Switch_Control = m.select('*switch*')
    Switch_Control_Typ = m.ls(sl=1)
    for i in Switch_Control_Typ:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 9)


#-------------------------------------------------------------------------------------------

    Switch_Control = m.select('*switch_leg_l*')
    Switch_Control_Typ = m.ls(sl=1)
    m.parent(Switch_Control_Typ, 'main_switch_left_IK_FK_Control_leg')


    Switch_Control = m.select('*switch_leg_r*')
    Switch_Control_Typ = m.ls(sl=1)
    m.parent(Switch_Control_Typ, 'main_switch_right_IK_FK_Control_leg')

#-------------------------------------------------------------------------------------------
    #Group all in one group? Might not be needed
    #Switch_Control = m.select('*switch*')
    #Switch_Control_Typ = m.ls(sl=1)
    #m.group(Switch_Control_Typ, n='Switch_grp')

    # LEFT LEG SWITCH CONTROL ATTRIBUTES

    # Creating the switch functionality for the switch control
    switch_ctrl = 'main_switch_left_IK_FK_Control_leg'

    # Add an enum attribute to the switch control
    m.addAttr(switch_ctrl, longName="switch", attributeType="enum", enumName="FK:IK:", keyable=True)
    m.addAttr(switch_ctrl, longName='fist', attributeType="float", keyable=True)


    #FK and IK symbols 
    object1 = "l_FK_leg_IK_FK_ctrl"  
    object2 = "l_IK_leg_IK_FK_ctrl" 

    # Objects for arm controls

    #FK
    object3 = 'thigh_l_leg_fk_ctrl'
    object4 = 'calf_l_leg_fk_ctrl'
    object5 = 'foot_l_leg_fk_ctrl'
    object6 = 'ball_l_leg_fk_ctrl'

    #IK
    #object6 = 'lowerarm_l_arm_ik_ctrl'
    object7 = 'thigh_l_leg_ik_ctrl'
    object8 = 'foot_l_leg_ik_ctrl'
    #object9 = 'ball_l_leg_ik_ctrl'
    object10 = 'l_poleVector_leg_ctrl1' 



    # Create a condition node to switch visibility based on the enum attribute
    condition_node = m.createNode("condition", name="visibility_condition_04")
    m.setAttr(f"{condition_node}.secondTerm", 1)
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.firstTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object1}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object3}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object4}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object5}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object6}.visibility")


    condition_node = m.createNode("condition", name="visibility_condition_05")
    m.setAttr(f"{condition_node}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.secondTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object2}.visibility")
    #m.connectAttr(f"{condition_node}.outColorR", f"{object6}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object7}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object8}.visibility")
    #m.connectAttr(f"{condition_node}.outColorR", f"{object9}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object10}.visibility")



    # RIGHT LEG SWITCH CONTROL ATTRIBUTES


    # Creating the switch functionality for the switch control
    switch_ctrl = 'main_switch_right_IK_FK_Control_leg'

    # Add an enum attribute to the switch control
    m.addAttr(switch_ctrl, longName="switch", attributeType="enum", enumName="FK:IK:", keyable=True)
    m.addAttr(switch_ctrl, longName='fist', attributeType="float", keyable=True)


    #FK and IK symbols 
    object1 = "r_FK_leg_IK_FK_ctrl"  
    object2 = "r_IK_leg_IK_FK_ctrl" 

    # Objects for arm controls

    #FK
    object3 = 'thigh_r_leg_fk_ctrl'
    object4 = 'calf_r_leg_fk_ctrl'
    object5 = 'foot_r_leg_fk_ctrl'
    object6 = 'ball_r_leg_fk_ctrl'

    #IK
    #object6 = 'lowerarm_l_arm_ik_ctrl'
    object7 = 'thigh_r_leg_ik_ctrl'
    object8 = 'foot_r_leg_ik_ctrl'
    #object9 = 'ball_r_leg_ik_ctrl'
    object10 = 'r_poleVector_leg_ctrl1' 



    # Create a condition node to switch visibility based on the enum attribute
    condition_node = m.createNode("condition", name="visibility_condition_06")
    m.setAttr(f"{condition_node}.secondTerm", 1)
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.firstTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object1}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object3}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object4}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object5}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object6}.visibility")


    condition_node = m.createNode("condition", name="visibility_condition_07")
    m.setAttr(f"{condition_node}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node}.secondTerm")
    m.connectAttr(f"{condition_node}.outColorR", f"{object2}.visibility")
    #m.connectAttr(f"{condition_node}.outColorR", f"{object6}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object7}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object8}.visibility")
    #m.connectAttr(f"{condition_node}.outColorR", f"{object9}.visibility")
    m.connectAttr(f"{condition_node}.outColorR", f"{object10}.visibility")
    
#-------------------------------------------------------------------------------------------

    # HAND CONTROLS / FINGER CONTROLS

#-------------------------------------------------------------------------------------------

    handListLeft = ['thumb_01_l', 'thumb_02_l', 'thumb_03_l', 'index_metacarpal_l', 'index_01_l', 'index_02_l', 'index_03_l', 'middle_metacarpal_l', 'middle_01_l', 'middle_02_l','middle_03_l', 'ring_metacarpal_l', 'ring_01_l', 'ring_02_l', 'ring_03_l', 'pinky_metacarpal_l', 'pinky_01_l', 'pinky_02_l', 'pinky_03_l' ]
    handListRight = ['thumb_01_r', 'thumb_02_r', 'thumb_03_r', 'index_metacarpal_r', 'index_01_r', 'index_02_r', 'index_03_r', 'middle_metacarpal_r', 'middle_01_r', 'middle_02_r','middle_03_r', 'ring_metacarpal_r', 'ring_01_r', 'ring_02_r', 'ring_03_r', 'pinky_metacarpal_r', 'pinky_01_r', 'pinky_02_r', 'pinky_03_r']
    l_hand_group = m.group(em=1, n='l_hand_fingers')
    r_hand_group = m.group(em=1, n='r_hand_fingers')

    curveScale = 1

    for i in handListLeft:
        utils.fingerArrow(curveScale, i + '_ctrl')
        setDrivenKeyGrp = m.group(i + '_ctrl', name = i + '_ctrl' + '_setDrivenKey')
        m.group(setDrivenKeyGrp, name = i + '_ctrl' + '_offset')
        
        # Replace these with the names of your control and group
        control_name = i + '_ctrl'
        group_name = i + '_ctrl' + "_setDrivenKey"

        # Get the pivot position of the control
        control_pivot = m.xform(control_name, q=True, rp=True, ws=True)

        # Set the pivot position of the group to match the control's pivot
        m.xform(group_name, piv=control_pivot, ws=True)



        # Replace these with the names of your control and group
        control_name = i + '_ctrl'
        group_name = i + '_ctrl' + "_offset"

        # Get the pivot position of the control
        control_pivot = m.xform(control_name, q=True, rp=True, ws=True)

        # Set the pivot position of the group to match the control's pivot
        m.xform(group_name, piv=control_pivot, ws=True)


        m.setAttr(group_name + ".rotateAxisY", 90)
        m.setAttr(group_name + ".rotateAxisZ", -90)
        m.makeIdentity(a=1, r=1, s=1, t=1)  
        temp = m.parentConstraint(i, group_name )
        m.delete(temp)
        SpineGrp = m.select( control_name +'Shape')
        SpineGrpTyp = m.ls(sl=1)
        for i in SpineGrpTyp:
            m.setAttr("{}.overrideEnabled".format(i), 1)
            m.setAttr("{}.overrideColor".format(i), 18)
        
        m.parent(group_name, l_hand_group, relative=True)
    
    #Making sure that the new group for all the fingers have the same position as the hands
    # Replace these with the names of your control and group
    control_name_joint = 'hand_l'
    new_group_name = l_hand_group

    # Get the pivot position of the control
    new_control_pivot = m.xform(control_name_joint, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(new_group_name, piv=new_control_pivot, ws=True)

    

        



    for i in handListRight:
        utils.fingerArrow(curveScale, i + '_ctrl')
        setDrivenKeyGrp = m.group(i + '_ctrl', name = i + '_ctrl' + '_setDrivenKey')
        m.group(setDrivenKeyGrp, name = i + '_ctrl' + '_offset')

        # Replace these with the names of your control and group
        control_name = i + '_ctrl'
        group_name = i + '_ctrl' + "_setDrivenKey"

        # Get the pivot position of the control
        control_pivot = m.xform(control_name, q=True, rp=True, ws=True)

        # Set the pivot position of the group to match the control's pivot
        m.xform(group_name, piv=control_pivot, ws=True)


        # Replace these with the names of your control and group
        control_name = i + '_ctrl'
        group_name = i + '_ctrl' + "_offset"

        # Get the pivot position of the control
        control_pivot = m.xform(control_name, q=True, rp=True, ws=True)

        # Set the pivot position of the group to match the control's pivot
        m.xform(group_name, piv=control_pivot, ws=True)

        m.setAttr(group_name + ".rotateAxisX", 180)
        m.setAttr(group_name + ".rotateAxisY", -90)
        m.setAttr(group_name + ".rotateAxisZ", 90)
        m.makeIdentity(a=1, r=1, s=1, t=1)  
        temp = m.parentConstraint(i, group_name )
        m.delete(temp)
        SpineGrp = m.select( control_name +'Shape')
        SpineGrpTyp = m.ls(sl=1)
        for i in SpineGrpTyp:
            m.setAttr("{}.overrideEnabled".format(i), 1)
            m.setAttr("{}.overrideColor".format(i), 18)
        
        m.parent(group_name, r_hand_group, relative=True)

    control_name_joint = 'hand_r'
    new_group_name = r_hand_group

    # Get the pivot position of the control
    new_control_pivot = m.xform(control_name_joint, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(new_group_name, piv=new_control_pivot, ws=True)


    """    utils.fingerArrow(curveScale, 'thumb_01_l_ctrl')
    m.group('thumb_01_l_ctrl', name = 'thumb_01_l_ctrl_offset')

    # Replace these with the names of your control and group
    control_name = "thumb_01_l_ctrl"
    group_name = "thumb_01_l_ctrl_offset"

    # Get the pivot position of the control
    control_pivot = m.xform(control_name, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name, piv=control_pivot, ws=True)

    m.setAttr("thumb_01_l_ctrl_offset.rotateAxisY", 90)
    m.setAttr("thumb_01_l_ctrl_offset.rotateAxisZ", -90)
    m.makeIdentity(a=1, r=1, s=1, t=1)  
    temp = m.parentConstraint('thumb_01_l', 'thumb_01_l_ctrl_offset' )
    m.delete(temp)
    SpineGrp = m.select('*thumb_01_l_ctrlShape')
    SpineGrpTyp = m.ls(sl=1)
    for i in SpineGrpTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 17)"""

  




#-------------------------------------------------------------------------------------------

    # Group everything in 'control_grp' folder

    listAllExtras = ['mainRoot_Ctrl_Offset', 'PoleVectorControl_01', 'PoleVectorControl_02', 'PoleVectorControl_03',  'PoleVectorControl_04', 'l_arm_ctrls', 'r_arm_ctrls', 'l_leg_ctrls', 'r_leg_ctrls', 'spine01_ctrl_Offset', 'mainRoot_Ctrl_Extra_Offset', 'spine02_ctrl_Offset', 'spine03_ctrl_Offset', 'spine04_ctrl_Offset', 'spine05_ctrl_Offset', 'neck01_ctrl_Offset', 'neck02_ctrl_Offset', 'head_ctrl_Offset', 'pelvis_ctrl_Offset', 'clavicle_l_ctrl_Offset', 'clavicle_r_ctrl_Offset', 'main_switch_left_IK_FK_Control_offset', 'main_switch_right_IK_FK_Control_offset', 'main_switch_left_IK_FK_Control_leg_offset', 'main_switch_right_IK_FK_Control_leg_offset', 'l_hand_fingers', 'r_hand_fingers']

    existing_group_name = "control_grp" 

    for obj in listAllExtras:
        m.parent(obj, existing_group_name)

#-------------------------------------------------------------------------------------------
    #m.parent('pelvis_ctrl', 'pelvis')
    m.parent('spine01_ctrl_Offset', 'pelvis_ctrl')
    m.parent('spine02_ctrl_Offset', 'spine01_ctrl')
    m.parent('spine03_ctrl_Offset', 'spine02_ctrl')
    m.parent('spine04_ctrl_Offset', 'spine03_ctrl')
    m.parent('spine05_ctrl_Offset', 'spine04_ctrl')

    m.parent('neck01_ctrl_Offset', 'spine05_ctrl')
    m.parent('neck02_ctrl_Offset', 'neck01_ctrl')
    m.parent('head_ctrl_Offset', 'neck02_ctrl')


    m.parent('clavicle_l_ctrl_Offset', 'spine05_ctrl')
    m.parent('clavicle_r_ctrl_Offset', 'spine05_ctrl')

    m.parent('l_arm_ctrls','clavicle_l_ctrl')
    m.parent('r_arm_ctrls','clavicle_r_ctrl')

    m.parent('l_leg_ctrls','pelvis_ctrl')
    m.parent('r_leg_ctrls','pelvis_ctrl')

    m.parent('pelvis_ctrl_Offset','mainRoot_Ctrl_Extra')
    m.parent('mainRoot_Ctrl_Extra_Offset','mainRoot_Ctrl')


#-------------------------------------------------------------------------------------------

    # Set driven keys: ANIMATION FOR THE FINGERS


#-------------------------------------------------------------------------------------------

    # Set Driven Keys for thumb

    m.setDrivenKeyframe('thumb_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('thumb_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('thumb_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('thumb_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('thumb_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('thumb_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('thumb_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('thumb_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('thumb_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('thumb_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= -60, driverValue=-1)
    m.setDrivenKeyframe('thumb_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= 0, driverValue=0)
    m.setDrivenKeyframe('thumb_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= 60, driverValue=1)

    m.setDrivenKeyframe('thumb_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= -60, driverValue=-1)
    m.setDrivenKeyframe('thumb_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= 0, driverValue=0)
    m.setDrivenKeyframe('thumb_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= 60, driverValue=1)

    m.setDrivenKeyframe('thumb_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= -60, driverValue=-1)
    m.setDrivenKeyframe('thumb_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= 0, driverValue=0)
    m.setDrivenKeyframe('thumb_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'thumb', value= 60, driverValue=1)
#-----------------------------------------------------------------------


    # Set Driven Keys for the index

    m.setDrivenKeyframe('index_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('index_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('index_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('index_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('index_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('index_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('index_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('index_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('index_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('index_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= -60, driverValue=-1)
    m.setDrivenKeyframe('index_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= 0, driverValue=0)
    m.setDrivenKeyframe('index_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= 60, driverValue=1)

    m.setDrivenKeyframe('index_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= -60, driverValue=-1)
    m.setDrivenKeyframe('index_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= 0, driverValue=0)
    m.setDrivenKeyframe('index_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('index_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= -60, driverValue=-1)
    m.setDrivenKeyframe('index_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= 0, driverValue=0)
    m.setDrivenKeyframe('index_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'index', value= 60, driverValue=1)



#-----------------------------------------------------------------------


    # Set Driven Keys for the middle

    m.setDrivenKeyframe('middle_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('middle_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('middle_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('middle_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('middle_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('middle_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('middle_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('middle_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('middle_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('middle_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= -60, driverValue=-1)
    m.setDrivenKeyframe('middle_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= 0, driverValue=0)
    m.setDrivenKeyframe('middle_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= 60, driverValue=1)

    m.setDrivenKeyframe('middle_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= -60, driverValue=-1)
    m.setDrivenKeyframe('middle_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= 0, driverValue=0)
    m.setDrivenKeyframe('middle_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('middle_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= -60, driverValue=-1)
    m.setDrivenKeyframe('middle_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= 0, driverValue=0)
    m.setDrivenKeyframe('middle_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'middle', value= 60, driverValue=1)

#-----------------------------------------------------------------------


    # Set Driven Keys for the ring

    m.setDrivenKeyframe('ring_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('ring_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('ring_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('ring_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('ring_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('ring_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('ring_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('ring_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('ring_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('ring_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= -60, driverValue=-1)
    m.setDrivenKeyframe('ring_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= 0, driverValue=0)
    m.setDrivenKeyframe('ring_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= 60, driverValue=1)

    m.setDrivenKeyframe('ring_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= -60, driverValue=-1)
    m.setDrivenKeyframe('ring_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= 0, driverValue=0)
    m.setDrivenKeyframe('ring_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('ring_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= -60, driverValue=-1)
    m.setDrivenKeyframe('ring_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= 0, driverValue=0)
    m.setDrivenKeyframe('ring_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'ring', value= 60, driverValue=1)

#-----------------------------------------------------------------------


    # Set Driven Keys for the pinky

    m.setDrivenKeyframe('pinky_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('pinky_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('pinky_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)

    m.setDrivenKeyframe('pinky_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('pinky_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('pinky_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('pinky_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= -60, driverValue=-1)
    m.setDrivenKeyframe('pinky_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 0, driverValue=0)
    m.setDrivenKeyframe('pinky_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'fist', value= 60, driverValue=1)



    m.setDrivenKeyframe('pinky_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= -60, driverValue=-1)
    m.setDrivenKeyframe('pinky_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= 0, driverValue=0)
    m.setDrivenKeyframe('pinky_01_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= 60, driverValue=1)

    m.setDrivenKeyframe('pinky_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= -60, driverValue=-1)
    m.setDrivenKeyframe('pinky_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= 0, driverValue=0)
    m.setDrivenKeyframe('pinky_02_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= 60, driverValue=1)
    
    m.setDrivenKeyframe('pinky_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= -60, driverValue=-1)
    m.setDrivenKeyframe('pinky_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= 0, driverValue=0)
    m.setDrivenKeyframe('pinky_03_l_ctrl_setDrivenKey.rotateZ', currentDriver='main_switch_left_IK_FK_Control' + "." + 'pinky', value= 60, driverValue=1)



#-------------------------------------------------------------------------------------------

    # Select root at the end of group creation
    m.select('root')





#-------------------------------------------------------------------------------------------

    # DOBBLE CHECK THAT THE CONTROLS AND GROUPS HAVE THE SAME PIVOT!
    # REMEMBER TO DELETE THE SCALES ON THE CONTROL AT THE START!
    # MAKE SIGNS FK AND IK NON KEYABLE
    # Parent the pole vector controls under their IK controls
    # Something is wrong with the parent constraint - they dont have they same axis as the controls
    # MAKE THE FINGER CONTROLS


    
"""
#-------------------------------------------------------------------------------------------
    # Group controls


    # RIGHT LEG CONTROLS


    #Select all the ctrls and group them under 1 group
    sel = m.select('*_ctrl')
    typ = m.ls(sl=1)
    scaleCtrl = 30
    m.scale(scaleCtrl,scaleCtrl,scaleCtrl)
    #topGrp = m.group( em=True, name='null1' + '_group'  )


    m.group( typ, name = 'l_ctrls' , w=1)
    m.select(cl=1)

    # Group the FK controls
    fkGroup = m.select('*fk_ctrl')
    fkGroupTyp = m.ls(sl=1)
    print(fkGroupTyp)
    m.parent(fkGroupTyp[1], fkGroupTyp[0], fkGroupTyp[2])
    m.parent(fkGroupTyp[0], fkGroupTyp[1])

    #Changing the color of FK
    fkGroup = m.select('*fk_ctrlShape')
    fkGroupTyp = m.ls(sl=1)
    for i in fkGroupTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 14)
        
    # Group the IK controls
    ikGroup = m.select('*ik_ctrl')
    ikGroupTyp = m.ls(sl=1)
    print(ikGroupTyp)
    m.parent(ikGroupTyp[2], ikGroupTyp[0], ikGroupTyp[1])
    #m.parent(ikGroupTyp[2], ikGroupTyp[0])

    #Changing the color of IK
    ikGroup = m.select('*ik_ctrlShape')
    ikGroupTyp = m.ls(sl=1)
    for i in ikGroupTyp:
        m.setAttr("{}.overrideEnabled".format(i), 1)
        m.setAttr("{}.overrideColor".format(i), 13)
    



    #-------------------------------------------------------------------------------------------
    
    #Create control for IK_FX blending
    #switch_control = m.circle(name="arm_IK_FK_ctrl")[0]
    # Create a custom attribute on the switch control for the IK/FK switch
    #m.addAttr(switch_control, ln="IK_FK_Switch", at="enum", enumName="IK:FK", k=True)

    switch_control = utils.arrowSquare(10)
    m.addAttr(switch_control, ln="IK_FK_Switch", at="enum", enumName="IK:FK", k=True)

    m.rename(switch_control, 'arm_IK_FK_ctrl')
    

    

        # Group controls


    # LEFT LEG CONTROLS


    #Select all the ctrls and group them under 1 group
    sel_left_leg = m.select(leftLegCtrlList)
    typ_left_leg = m.ls(sl=1)
    #leftArmCtrlList = []
    #for i in leftArmlist:
        #leftArmCtrlList.append(i + '_ctrl')

    
    m.scale(scaleCtrl,scaleCtrl,scaleCtrl)
    #topGrp = m.group( em=True, name='null1' + '_group'  )

    m.group( typ_left_leg, name = 'l_leg_ctrls' , w=1)
    m.select(cl=1)
    
    #--------------------------------------------------------------------------------
        # Making the FX Controls

    # Create locators
    shoulder_locator = 'upperarm_l'
    elbow_locator = 'lowerarm_l'
    wrist_locator = 'hand_l'

    # Create control curves
    shoulder_ctrl = cmds.circle(n="shoulder_ctrl")[0]
    shoulder_ctrl_offset = cmds.group(shoulder_ctrl, n='shoulder_ctrl_offset')
    cmds.scale(50,50,50)
    cmds.setAttr("shoulder_ctrl_offset.rotateAxisY", 90)
    cmds.makeIdentity(a=1, r=1, s=1, t=1)


    elbow_ctrl = cmds.circle(n="elbow_ctrl")[0]
    elbow_ctrl_offset = cmds.group(elbow_ctrl, n='elbow_ctrl_offset')
    cmds.scale(50,50,50)
    cmds.setAttr("elbow_ctrl_offset.rotateAxisY", 90)
    cmds.makeIdentity(a=1, r=1, s=1, t=1)

    wrist_ctrl = cmds.circle(n="wrist_ctrl")[0]
    wrist_ctrl_offset = cmds.group(wrist_ctrl, n='wrist_ctrl_offset')
    cmds.scale(50,50,50)
    cmds.setAttr("wrist_ctrl_offset.rotateAxisY", 90)
    cmds.makeIdentity(a=1, r=1, s=1, t=1)

    #
    parent1 = cmds.parentConstraint(shoulder_locator, shoulder_ctrl_offset)
    parent2 = cmds.parentConstraint(elbow_locator, elbow_ctrl_offset)
    parent3 = cmds.parentConstraint(wrist_locator, wrist_ctrl_offset)

    cmds.delete(parent1,parent2,parent3)

    parent1 = cmds.parentConstraint(shoulder_ctrl, shoulder_locator)
    parent2 = cmds.parentConstraint(elbow_ctrl, elbow_locator)
    parent3 = cmds.parentConstraint(wrist_ctrl, wrist_locator)
    
    
    
    
    
    
    
    
    
    
    
    
    
    """

def orientJoint():

    # Creating the opertunity to change joint orientation.
    
    # xyz, yzx, zxy, zyx, yxz, xzy, none
    jointOrientList = 'xyz'
    #xup, xdown, yup, ydown, zup, zdown, none
    secondaryAxisOrientList = 'zdown'

    emptylist = []
    selectionCheck = m.select(hi=True)
    selectionCheck = m.ls(sl=1, type='joint')
    utils.findAllJointsInHierarchy(selectionCheck, emptylist)
    m.joint(e=1, oj=(jointOrientList), sao=(secondaryAxisOrientList), zso=1)
    
    #Change Rotationorder for each joint
    # 0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX
    desired_rotation_order = 0
    for i in selectionCheck:    
        m.setAttr(i + ".rotateOrder", desired_rotation_order)

    
    #This is for the last joint in the hiearchy
    #m.joint(e=1, oj=('none'), zso=1)

def list_all_children(nodes):
    #Fast, but slow when nesting is very deep.
    
    result = set()
    children = set(m.listRelatives(nodes, fullPath=True) or [])
    while children:
        result.update(children)
        children = set(m.listRelatives(children, fullPath=True) or []) - result
        
    return list(result)


def get_last_elements(node, last_elements):
    children = m.listRelatives(node, children=True) or []

    if not children:
        last_elements.append(node)
    else:
        for child in children:
            get_last_elements(child, last_elements)





"""
# Create locators
shoulder_locator = 'upperarm_l'
elbow_locator = 'lowerarm_l'
wrist_locator = 'hand_l'

#Be able to change the rotate order for each of the offset ctrl groups

# Create control curves
shoulder_ctrl = cmds.circle(n="shoulder_ctrl")[0]
shoulder_ctrl_offset = cmds.group(shoulder_ctrl, n='shoulder_ctrl_offset')
cmds.scale(50,50,50)
cmds.setAttr("shoulder_ctrl_offset.rotateAxisY", 90)
cmds.makeIdentity(a=1, r=1, s=1, t=1)


elbow_ctrl = cmds.circle(n="elbow_ctrl")[0]
elbow_ctrl_offset = cmds.group(elbow_ctrl, n='elbow_ctrl_offset')
cmds.scale(50,50,50)
cmds.setAttr("elbow_ctrl_offset.rotateAxisY", 90)
cmds.makeIdentity(a=1, r=1, s=1, t=1)

wrist_ctrl = cmds.circle(n="wrist_ctrl")[0]
wrist_ctrl_offset = cmds.group(wrist_ctrl, n='wrist_ctrl_offset')
cmds.scale(50,50,50)
cmds.setAttr("wrist_ctrl_offset.rotateAxisY", 90)
cmds.makeIdentity(a=1, r=1, s=1, t=1)

#
parent1 = cmds.parentConstraint(shoulder_locator, shoulder_ctrl_offset)
parent2 = cmds.parentConstraint(elbow_locator, elbow_ctrl_offset)
parent3 = cmds.parentConstraint(wrist_locator, wrist_ctrl_offset)

cmds.delete(parent1,parent2,parent3)

parent1 = cmds.parentConstraint(shoulder_ctrl, shoulder_locator)
parent2 = cmds.parentConstraint(elbow_ctrl, elbow_locator)
parent3 = cmds.parentConstraint(wrist_ctrl, wrist_locator)

cmds.select(type='joint')
"""