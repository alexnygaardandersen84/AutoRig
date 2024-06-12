import sys
import maya.cmds as m
import utils_simpleRig as utils
import groups as gp
import pymel.core as pm



def autoLimbToolFunction():

    #Making a full list of the joints in the rig for creating controls
    #Emptylist is the full list of joints in the rig

    emptylist = []
    selectionCheck = m.ls(sl=1, type='joint')[0]
    selectionCheck01 = m.ls(sl=1,l=1 )[0].split('|')[1:4]
    for i in selectionCheck01: 
        emptylist.append(i)

    jointHierachy = utils.findAllJointsInHierarchy(selectionCheck, emptylist)

    #Error if nothing is selected
    if not selectionCheck: 
        m.error("Please select the root joint")


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
    
    #first define what joint chain need
    #newJointList = ["_ik", "_fk", "_stretch"]
    newJointList = ["_ik", "_fk"]

    #-------------------------------------------------------------------------------------------

    # Build the joints
    #-------------------------------------------------------------------------------------------

        # LEFT ARM

    #-------------------------------------------------------------------------------------------
    
    #Second loop is going through the hierarchy and displaying all the names not just the first one
    for newJoint in newJointList: 
        for i in range(len(leftArmlist)):
            newJointName = leftArmlist[i] + newJoint
            m.joint(n=newJointName)
            m.matchTransform(newJointName, leftArmlist[i])
            
            #Freeze transforms after the new position
            #m.makeIdentity(newJointName, a=1, t=0, r=0, s=0)
        #This is what clears the selection and therefore not making the new joints parent each other
        m.select(cl=1)
    #print(newJoint)
    
    # Constraining the 3 point ring: _ik + _fk + normal joint list
    # Constrain the main joints to the IK and FK joints so we can blend between them
    for i in range(len(leftArmlist)):
        #w=weights, mo=maintain offset
        m.parentConstraint( (leftArmlist[i] + '_ik'), (leftArmlist[i] + '_fk'), leftArmlist[i], w=1, mo=0)
        

    #-------------------------------------------------------------------------------------------

        # RIGHT ARM

    #-------------------------------------------------------------------------------------------

    #Second loop is going through the hierarchy and displaying all the names not just the first one
    for newJoint in newJointList: 
        for i in range(len(rightArmlist)):
            newJointName = rightArmlist[i] + newJoint
            m.joint(n=newJointName)
            m.matchTransform(newJointName, rightArmlist[i])
            #Freeze transforms after the new position
            #m.makeIdentity(newJointName, a=1, t=0, r=0, s=0)
        #This is what clears the selection and therefore not making the new joints parent each other
        m.select(cl=1)
    #print(newJoint)
    
    # Constraining the 3 point ring: _ik + _fk + normal joint list
    # Constrain the main joints to the IK and FK joints so we can blend between them
    for i in range(len(rightArmlist)):
        #w=weights, mo=maintain offset
        m.parentConstraint( (rightArmlist[i] + '_ik'), (rightArmlist[i] + '_fk'), rightArmlist[i], w=1, mo=0)

    #-------------------------------------------------------------------------------------------
    
        # LEFT LEG

    #-------------------------------------------------------------------------------------------

        #Second loop is going through the hierarchy and displaying all the names not just the first one
    for newJoint in newJointList: 
        for i in range(len(leftLegList)):
            newJointName = leftLegList[i] + newJoint
            m.joint(n=newJointName)
            m.matchTransform(newJointName, leftLegList[i])
            #Freeze transforms after the new position
            #m.makeIdentity(newJointName, a=1, t=0, r=0, s=0)
        #This is what clears the selection and therefore not making the new joints parent each other
        m.select(cl=1)
    #print(newJoint)
    
    # Constraining the 3 point ring: _ik + _fk + normal joint list
    # Constrain the main joints to the IK and FK joints so we can blend between them
    for i in range(len(leftLegList)):
        #w=weights, mo=maintain offset
        m.parentConstraint( (leftLegList[i] + '_ik'), (leftLegList[i] + '_fk'), leftLegList[i], w=1, mo=0)

    #-------------------------------------------------------------------------------------------
    
        # RIGHT LEG

    #-------------------------------------------------------------------------------------------

        #Second loop is going through the hierarchy and displaying all the names not just the first one
    for newJoint in newJointList: 
        for i in range(len(rightLegList)):
            newJointName = rightLegList[i] + newJoint
            m.joint(n=newJointName)
            m.matchTransform(newJointName, rightLegList[i])
            #Freeze transforms after the new position
            #m.makeIdentity(newJointName, a=1, t=0, r=0, s=0)
        #This is what clears the selection and therefore not making the new joints parent each other
        m.select(cl=1)
    #print(newJoint)
    
    # Constraining the 3 point ring: _ik + _fk + normal joint list
    # Constrain the main joints to the IK and FK joints so we can blend between them
    for i in range(len(rightLegList)):
        #w=weights, mo=maintain offset
        m.parentConstraint( (rightLegList[i] + '_ik'), (rightLegList[i] + '_fk'), rightLegList[i], w=1, mo=0)


    # Group every joints in the Extra_skeleton folder:
    
    #listAllExtras = ["upperarm_l_ik", "upperarm_l_fk", "*upperarm_l_stretch", "upperarm_r_ik", "upperarm_r_fk", "*upperarm_r_stretch",  "thigh_l_ik", "thigh_l_fk", "*thigh_l_stretch",  "thigh_r_ik", "thigh_r_fk", "*thigh_r_stretch"]
    listAllExtras = ["upperarm_l_ik", "upperarm_l_fk", "upperarm_r_ik", "upperarm_r_fk",  "thigh_l_ik", "thigh_l_fk",  "thigh_r_ik", "thigh_r_fk"]


    existing_group_name = "Exstra_skeleton" 

    for obj in listAllExtras:
        m.parent(obj, existing_group_name)

    
  



    #-------------------------------------------------------------------------------------------

        #   PARENT CONSTRAINT JOINTS AND CONTROLS

    #-------------------------------------------------------------------------------------------
    # CONTROL AND THEN JOINT
    m.parentConstraint('head_ctrl', 'head')

    #m.parentConstraint('pelvis_ctrl', 'pelvis')
    m.parentConstraint('spine01_ctrl', 'spine_01')
    m.parentConstraint('spine02_ctrl', 'spine_02')
    m.parentConstraint('spine03_ctrl', 'spine_03')
    m.parentConstraint('spine04_ctrl', 'spine_04')
    m.parentConstraint('spine05_ctrl', 'spine_05')
    m.parentConstraint('neck02_ctrl', 'neck_02')
    m.parentConstraint('neck01_ctrl', 'neck_01')
    m.parentConstraint('clavicle_l_ctrl','clavicle_l')
    m.parentConstraint('clavicle_r_ctrl','clavicle_r')
    m.parentConstraint('mainRoot_Ctrl','skeleton_grp')
    

    #FK
    m.parentConstraint('upperarm_l_arm_fk_ctrl', 'upperarm_l_fk')
    m.parentConstraint('lowerarm_l_arm_fk_ctrl', 'lowerarm_l_fk')
    m.parentConstraint('hand_l_arm_fk_ctrl', 'hand_l_fk')

    m.parentConstraint('upperarm_r_arm_fk_ctrl', 'upperarm_r_fk')
    m.parentConstraint('lowerarm_r_arm_fk_ctrl', 'lowerarm_r_fk')
    m.parentConstraint('hand_r_arm_fk_ctrl', 'hand_r_fk')


    m.parentConstraint('thigh_l_leg_fk_ctrl', 'thigh_l_fk')
    m.parentConstraint('calf_l_leg_fk_ctrl', 'calf_l_fk')
    m.parentConstraint('foot_l_leg_fk_ctrl', 'foot_l_fk')
    m.parentConstraint('ball_l_leg_fk_ctrl', 'ball_l_fk')
    

    m.parentConstraint('thigh_r_leg_fk_ctrl', 'thigh_r_fk')
    m.parentConstraint('calf_r_leg_fk_ctrl', 'calf_r_fk')
    m.parentConstraint('foot_r_leg_fk_ctrl', 'foot_r_fk')
    m.parentConstraint('ball_r_leg_fk_ctrl', 'ball_r_fk')

    #IK

    m.parentConstraint('upperarm_l_arm_ik_ctrl', 'upperarm_l_ik')
    m.parentConstraint('upperarm_r_arm_ik_ctrl', 'upperarm_r_ik')
    m.parentConstraint('thigh_l_leg_ik_ctrl', 'thigh_l_ik')
    m.parentConstraint('thigh_r_leg_ik_ctrl', 'thigh_r_ik')


    #FINGERS

    m.parent('thumb_03_l_ctrl_offset','thumb_02_l_ctrl')
    m.parent('thumb_02_l_ctrl_offset','thumb_01_l_ctrl')

    m.parent('index_03_l_ctrl_offset','index_02_l_ctrl')
    m.parent('index_02_l_ctrl_offset','index_01_l_ctrl')
    m.parent('index_01_l_ctrl_offset','index_metacarpal_l_ctrl')

    m.parent('middle_03_l_ctrl_offset','middle_02_l_ctrl')
    m.parent('middle_02_l_ctrl_offset','middle_01_l_ctrl')
    m.parent('middle_01_l_ctrl_offset','middle_metacarpal_l_ctrl')

    m.parent('ring_03_l_ctrl_offset','ring_02_l_ctrl')
    m.parent('ring_02_l_ctrl_offset','ring_01_l_ctrl')
    m.parent('ring_01_l_ctrl_offset','ring_metacarpal_l_ctrl')

    m.parent('pinky_03_l_ctrl_offset','pinky_02_l_ctrl')
    m.parent('pinky_02_l_ctrl_offset','pinky_01_l_ctrl')
    m.parent('pinky_01_l_ctrl_offset','pinky_metacarpal_l_ctrl')

    m.parent('thumb_03_r_ctrl_offset','thumb_02_r_ctrl')
    m.parent('thumb_02_r_ctrl_offset','thumb_01_r_ctrl')

    m.parent('index_03_r_ctrl_offset','index_02_r_ctrl')
    m.parent('index_02_r_ctrl_offset','index_01_r_ctrl')
    m.parent('index_01_r_ctrl_offset','index_metacarpal_r_ctrl')

    m.parent('middle_03_r_ctrl_offset','middle_02_r_ctrl')
    m.parent('middle_02_r_ctrl_offset','middle_01_r_ctrl')
    m.parent('middle_01_r_ctrl_offset','middle_metacarpal_r_ctrl')

    m.parent('ring_03_r_ctrl_offset','ring_02_r_ctrl')
    m.parent('ring_02_r_ctrl_offset','ring_01_r_ctrl')
    m.parent('ring_01_r_ctrl_offset','ring_metacarpal_r_ctrl')

    m.parent('pinky_03_r_ctrl_offset','pinky_02_r_ctrl')
    m.parent('pinky_02_r_ctrl_offset','pinky_01_r_ctrl')
    m.parent('pinky_01_r_ctrl_offset','pinky_metacarpal_r_ctrl')



  #-------------------------------------------------------------------------------------------

    # Making the connections to switch IK and FK joints!

#-------------------------------------------------------------------------------------------

    # LEFT ARM

#-------------------------------------------------------------------------------------------

    """    # Making the switch between FK and IK for the FK_IK control
    for i in range(len(leftArmlist)):
        getConstraint = m.listConnections(leftArmlist[i], type="parentConstraint")[0]
        print(getConstraint)
        #getWeights = m.parentConstraint(getConstraint, q=1, wal=1)

    """

    # m.connectAttr(('main_switch_left_IK_FK_Control' + '.switch'), (getConstraint + '.' + getWeights[0]), f=1)
    switch_ctrl = 'main_switch_left_IK_FK_Control'
    object1 = 'upperarm_l_parentConstraint1'
    object2 = 'lowerarm_l_parentConstraint1'
    object3 = 'hand_l_parentConstraint1'



    
    # Create a condition node to switch visibility based on the enum attribute
    condition_node_1 = "visibility_condition"
    #m.setAttr(f"{condition_node}.secondTerm", 1)
    #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_1}.firstTerm")
    leftArmCondition = m.connectAttr(f"{condition_node_1}.outColorR", f"{object1}.upperarm_l_fkW1")
    leftArmCondition = m.connectAttr(f"{condition_node_1}.outColorR", f"{object2}.lowerarm_l_fkW1")
    leftArmCondition = m.connectAttr(f"{condition_node_1}.outColorR", f"{object3}.hand_l_fkW1")
        

        
    condition_node_2 = "visibility_condition_02"
    #m.setAttr(f"{condition_node}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_2}.secondTerm")
    leftArmCondition = m.connectAttr(f"{condition_node_2}.outColorR", f"{object1}.upperarm_l_ikW0")
    leftArmCondition = m.connectAttr(f"{condition_node_2}.outColorR", f"{object2}.lowerarm_l_ikW0")
    leftArmCondition = m.connectAttr(f"{condition_node_2}.outColorR", f"{object3}.hand_l_ikW0")



#-------------------------------------------------------------------------------------------

    # RIGHT ARM

#-------------------------------------------------------------------------------------------

    switch_ctrl = 'main_switch_right_IK_FK_Control'
    object1 = 'upperarm_r_parentConstraint1'
    object2 = 'lowerarm_r_parentConstraint1'
    object3 = 'hand_r_parentConstraint1'



    
    # Create a condition node to switch visibility based on the enum attribute
    condition_node_3 = "visibility_condition_03"
    #m.setAttr(f"{condition_node}.secondTerm", 1)
    #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_3}.firstTerm")
    rightArmCondition = m.connectAttr(f"{condition_node_3}.outColorR", f"{object1}.upperarm_r_fkW1")
    rightArmCondition = m.connectAttr(f"{condition_node_3}.outColorR", f"{object2}.lowerarm_r_fkW1")
    rightArmCondition = m.connectAttr(f"{condition_node_3}.outColorR", f"{object3}.hand_r_fkW1")
        

        
    condition_node_4 = "visibility_condition_04"
    #m.setAttr(f"{condition_node}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_4}.secondTerm")
    rightArmCondition = m.connectAttr(f"{condition_node_4}.outColorR", f"{object1}.upperarm_r_ikW0")
    rightArmCondition = m.connectAttr(f"{condition_node_4}.outColorR", f"{object2}.lowerarm_r_ikW0")
    rightArmCondition = m.connectAttr(f"{condition_node_4}.outColorR", f"{object3}.hand_r_ikW0")
    
    
#-------------------------------------------------------------------------------------------

    # LEFT LEG

#-------------------------------------------------------------------------------------------

    switch_ctrl = 'main_switch_left_IK_FK_Control_leg'
    object1 = 'thigh_l_parentConstraint1'
    object2 = 'calf_l_parentConstraint1'
    object3 = 'foot_l_parentConstraint1'
    object4 = 'ball_l_parentConstraint1'



    
    # Create a condition node to switch visibility based on the enum attribute
    condition_node_5 = "visibility_condition_05"
    #m.setAttr(f"{condition_node_1}.secondTerm", 1)
   #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_5}.firstTerm")
    leftLegCondition = m.connectAttr(f"{condition_node_5}.outColorR", f"{object1}.thigh_l_fkW1")
    leftLegCondition = m.connectAttr(f"{condition_node_5}.outColorR", f"{object2}.calf_l_fkW1")
    leftLegCondition = m.connectAttr(f"{condition_node_5}.outColorR", f"{object3}.foot_l_fkW1")
    leftLegCondition = m.connectAttr(f"{condition_node_5}.outColorR", f"{object4}.ball_l_fkW1")
        

        
    condition_node_6 = "visibility_condition_06"
    #m.setAttr(f"{condition_node_2}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_6}.secondTerm")
    leftLegCondition = m.connectAttr(f"{condition_node_6}.outColorR", f"{object1}.thigh_l_ikW0")
    leftLegCondition = m.connectAttr(f"{condition_node_6}.outColorR", f"{object2}.calf_l_ikW0")
    leftLegCondition = m.connectAttr(f"{condition_node_6}.outColorR", f"{object3}.foot_l_ikW0")
    leftLegCondition = m.connectAttr(f"{condition_node_6}.outColorR", f"{object4}.ball_l_ikW0")
    
#-------------------------------------------------------------------------------------------

    # RIGHT LEG

#-------------------------------------------------------------------------------------------

    switch_ctrl = 'main_switch_right_IK_FK_Control_leg'
    object1 = 'thigh_r_parentConstraint1'
    object2 = 'calf_r_parentConstraint1'
    object3 = 'foot_r_parentConstraint1'
    object4 = 'ball_r_parentConstraint1'



    
    # Create a condition node to switch visibility based on the enum attribute
    condition_node_7 = "visibility_condition_07"
    #m.setAttr(f"{condition_node_1}.secondTerm", 1)
    #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_7}.firstTerm")
    rightLegCondition = m.connectAttr(f"{condition_node_7}.outColorR", f"{object1}.thigh_r_fkW1")
    rightLegCondition = m.connectAttr(f"{condition_node_7}.outColorR", f"{object2}.calf_r_fkW1")
    rightLegCondition = m.connectAttr(f"{condition_node_7}.outColorR", f"{object3}.foot_r_fkW1")
    rightLegCondition = m.connectAttr(f"{condition_node_7}.outColorR", f"{object4}.ball_r_fkW1")
        

        
    condition_node_8 = "visibility_condition_08"
    #m.setAttr(f"{condition_node_2}.secondTerm", 0)
    # Connect the enum attribute to the condition node
    #m.connectAttr(f"{switch_ctrl}.switch", f"{condition_node_8}.secondTerm")
    rightLegCondition = m.connectAttr(f"{condition_node_8}.outColorR", f"{object1}.thigh_r_ikW0")
    rightLegCondition = m.connectAttr(f"{condition_node_8}.outColorR", f"{object2}.calf_r_ikW0")
    rightLegCondition = m.connectAttr(f"{condition_node_8}.outColorR", f"{object3}.foot_r_ikW0")
    rightLegCondition = m.connectAttr(f"{condition_node_8}.outColorR", f"{object4}.ball_r_ikW0")
    

#-------------------------------------------------------------------------------------------


    # Make IKHandle

#-------------------------------------------------------------------------------------------

    #Set preferred angle for the joints (this is important for the ikHandle)
    m.select('upperarm_l_ik')
    m.joint(e=1, spa=1, ch=1)

    joint_chain_arm_left = "upperarm_l_ik"
    effector_arm_left = "hand_l_ik"

    # Create an IK handle
    ik_handle_arm_left = m.ikHandle(sj=joint_chain_arm_left, ee=effector_arm_left, sol="ikRPsolver")[0]

    # Optionally, you can name the IK handle
    m.rename(ik_handle_arm_left, "IKHandle_arm_l")

    # Parent the ikHandle under the controls
    m.parent('IKHandle_arm_l', 'hand_l_arm_ik_ctrl')

#------------------------------------------------------------------------------

    m.select('upperarm_r_ik')
    m.joint(e=1, spa=1, ch=1)

    joint_chain_arm_right = "upperarm_r_ik"
    effector_arm_right = "hand_r_ik"

    # Create an IK handle
    ik_handle_arm_right = m.ikHandle(sj=joint_chain_arm_right, ee=effector_arm_right, sol="ikRPsolver")[0]

    # Optionally, you can name the IK handle
    m.rename(ik_handle_arm_right, "IKHandle_arm_r")

    # Parent the ikHandle under the controls
    m.parent('IKHandle_arm_r', 'hand_r_arm_ik_ctrl')

#------------------------------------------------------------------------------

    m.select('thigh_l_ik')
    m.joint(e=1, spa=1, ch=1)

    joint_chain_leg_left = "thigh_l_ik"
    effector_leg_left = "foot_l_ik"
    SCSolver_leg_left = 'ball_l_ik'

    # Create an IK handle
    ik_handle_leg_left = m.ikHandle(sj=joint_chain_leg_left, ee=effector_leg_left, sol="ikRPsolver")[0]
    ik_handle_leg_left_02 = m.ikHandle(sj=effector_leg_left, ee=SCSolver_leg_left, sol="ikSCsolver")[0]

    # Optionally, you can name the IK handle
    m.rename(ik_handle_leg_left, "IKHandle_leg_l_RP")
    m.rename(ik_handle_leg_left_02, "IKHandle_leg_l_SC")

    # Parent the ikHandle under the controls
    m.parent('IKHandle_leg_l_RP', 'foot_l_leg_ik_ctrl')
    m.parent('IKHandle_leg_l_SC', 'foot_l_leg_ik_ctrl')

#------------------------------------------------------------------------------

    m.select('thigh_r_ik')
    m.joint(e=1, spa=1, ch=1)

    joint_chain_leg_right = "thigh_r_ik"
    effector_leg_right = "foot_r_ik"
    SCSolver_leg_right = 'ball_r_ik'

    # Create an IK handle
    ik_handle_leg_right = m.ikHandle(sj=joint_chain_leg_right, ee=effector_leg_right, sol="ikRPsolver")[0]
    ik_handle_leg_right_02 = m.ikHandle(sj=effector_leg_right, ee=SCSolver_leg_right, sol="ikSCsolver")[0]

    # Optionally, you can name the IK handle
    m.rename(ik_handle_leg_right, "IKHandle_leg_r_RP")
    m.rename(ik_handle_leg_right_02, "IKHandle_leg_r_SC")

    # Parent the ikHandle under the controls
    m.parent('IKHandle_leg_r_RP', 'foot_r_leg_ik_ctrl')
    m.parent('IKHandle_leg_r_SC', 'foot_r_leg_ik_ctrl')


#-------------------------------------------------------------------------------------------

    # Create Pole Vectors

#-------------------------------------------------------------------------------------------

    m.poleVectorConstraint('l_poleVector_ctrl1','IKHandle_arm_l', n='poleVectorConstraint_arm_l')
    m.poleVectorConstraint('r_poleVector_ctrl1','IKHandle_arm_r', n='poleVectorConstraint_arm_r')
    m.poleVectorConstraint('l_poleVector_leg_ctrl1','IKHandle_leg_l_RP', n='poleVectorConstraint_leg_l')
    m.poleVectorConstraint('r_poleVector_leg_ctrl1','IKHandle_leg_r_RP', n='poleVectorConstraint_leg_l')


#-------------------------------------------------------------------------------------------


    # Orient Constraint ik_ctrl with ik_joint

#-------------------------------------------------------------------------------------------
    m.orientConstraint('hand_l_arm_ik_ctrl', 'hand_l_ik', n = 'orientConstraint_l_arm')
    m.orientConstraint('hand_r_arm_ik_ctrl', 'hand_r_ik', n = 'orientConstraint_r_arm')
    # Maybe the legs??


    m.parentConstraint('hand_l', 'main_switch_left_IK_FK_Control_offset', mo=True)
    m.parentConstraint('hand_r', 'main_switch_right_IK_FK_Control_offset', mo=True)

    m.parentConstraint('calf_l', 'main_switch_left_IK_FK_Control_leg_offset', mo=True)
    m.parentConstraint('calf_r', 'main_switch_right_IK_FK_Control_leg_offset', mo=True)


    m.parentConstraint('pelvis', 'PoleVectorControl_01', mo=True)
    m.parentConstraint('pelvis', 'PoleVectorControl_02', mo=True)
    m.parentConstraint('pelvis', 'PoleVectorControl_03', mo=True)
    m.parentConstraint('pelvis', 'PoleVectorControl_04', mo=True)

    
    #m.parent('PoleVectorControl_01', 'pelvis_ctrl', r=True, a=True)
    #m.parent('PoleVectorControl_02', 'pelvis_ctrl', r=True, a=True)

    #m.parent('PoleVectorControl_03', 'pelvis_ctrl', r=True, a=True)
    #m.parent('PoleVectorControl_04', 'pelvis_ctrl', r=True, a=True)



#-------------------------------------------------------------------------------------------

        # Parent Constraint fingers

#-------------------------------------------------------------------------------------------
    handListLeft = ['thumb_01_l', 'thumb_02_l', 'thumb_03_l', 'index_metacarpal_l', 'index_01_l', 'index_02_l', 'index_03_l', 'middle_metacarpal_l', 'middle_01_l', 'middle_02_l','middle_03_l', 'ring_metacarpal_l', 'ring_01_l', 'ring_02_l', 'ring_03_l', 'pinky_metacarpal_l', 'pinky_01_l', 'pinky_02_l', 'pinky_03_l' ]
    handListRight = ['thumb_01_r', 'thumb_02_r', 'thumb_03_r', 'index_metacarpal_r', 'index_01_r', 'index_02_r', 'index_03_r', 'middle_metacarpal_r', 'middle_01_r', 'middle_02_r','middle_03_r', 'ring_metacarpal_r', 'ring_01_r', 'ring_02_r', 'ring_03_r', 'pinky_metacarpal_r', 'pinky_01_r', 'pinky_02_r', 'pinky_03_r']

    for i in handListLeft:
        control_name = i + '_ctrl'
        m.parentConstraint(control_name, i)

    for i in handListRight:
        control_name = i + '_ctrl'
        m.parentConstraint(control_name, i)

    #m.parentConstraint('l_hand_fingers', 'hand_l', n = 'fingers_l_arm', mo=True)
    m.parentConstraint('hand_l','l_hand_fingers', n = 'fingers_l_arm', mo=True)
    m.parentConstraint('hand_r','r_hand_fingers', n = 'fingers_r_arm', mo=True)

#-------------------------------------------------------------------------------------------


    # Calculate pole vector

#-------------------------------------------------------------------------------------------

    """

    # Replace these with your actual IK handle and pole vector control names
    ik_handle_name = "IKHandle_arm_l"
    pole_vector_name = "l_poleVector_ctrl1"

    # Get the IK handle and pole vector control
    ik_handle = pm.PyNode(ik_handle_name)
    pole_vector = pm.PyNode(pole_vector_name)

    # Get the positions of the IK handle and pole vector
    ik_handle_position = ik_handle.getTranslation(space='world')
    pole_vector_position = pole_vector.getTranslation(space='world')

    # Calculate the vector from the IK handle to the pole vector
    pole_vector_vector = pole_vector_position - ik_handle_position
    pole_vector_vector.normalize()

    # Set the IK handle's pole vector attribute to the calculated vector
    ik_handle.poleVector.set(pole_vector_vector)

#------------------------------------------------------------------------------

    # Replace these with your actual IK handle and pole vector control names
    ik_handle_name = "IKHandle_arm_r"
    pole_vector_name = "r_poleVector_ctrl1"

    # Get the IK handle and pole vector control
    ik_handle = pm.PyNode(ik_handle_name)
    pole_vector = pm.PyNode(pole_vector_name)

    # Get the positions of the IK handle and pole vector
    ik_handle_position = ik_handle.getTranslation(space='world')
    pole_vector_position = pole_vector.getTranslation(space='world')

    # Calculate the vector from the IK handle to the pole vector
    pole_vector_vector = pole_vector_position - ik_handle_position
    pole_vector_vector.normalize()

    # Set the IK handle's pole vector attribute to the calculated vector
    ik_handle.poleVector.set(pole_vector_vector)


#------------------------------------------------------------------------------

    # Replace these with your actual IK handle and pole vector control names
    ik_handle_name = "IKHandle_leg_l_RP"
    pole_vector_name = "l_poleVector_leg_ctrl1"

    # Get the IK handle and pole vector control
    ik_handle = pm.PyNode(ik_handle_name)
    pole_vector = pm.PyNode(pole_vector_name)

    # Get the positions of the IK handle and pole vector
    ik_handle_position = ik_handle.getTranslation(space='world')
    pole_vector_position = pole_vector.getTranslation(space='world')

    # Calculate the vector from the IK handle to the pole vector
    pole_vector_vector = pole_vector_position - ik_handle_position
    pole_vector_vector.normalize()

    # Set the IK handle's pole vector attribute to the calculated vector
    ik_handle.poleVector.set(pole_vector_vector)

#------------------------------------------------------------------------------


    # Replace these with your actual IK handle and pole vector control names
    ik_handle_name = "IKHandle_leg_r_RP"
    pole_vector_name = "r_poleVector_leg_ctrl1"

    # Get the IK handle and pole vector control
    ik_handle = pm.PyNode(ik_handle_name)
    pole_vector = pm.PyNode(pole_vector_name)

    # Get the positions of the IK handle and pole vector
    ik_handle_position = ik_handle.getTranslation(space='world')
    pole_vector_position = pole_vector.getTranslation(space='world')

    # Calculate the vector from the IK handle to the pole vector
    pole_vector_vector = pole_vector_position - ik_handle_position
    pole_vector_vector.normalize()

    # Set the IK handle's pole vector attribute to the calculated vector
    ik_handle.poleVector.set(pole_vector_vector)

#------------------------------------------------------------------------------
    """

#------------------------------------------------------------------------------


    # Group the IK and FK joint into the right folder and set thir pivot at the start of each limb

#------------------------------------------------------------------------------

    l_arm_group = m.group(em=True, n='l_arm')
    temp = m.parentConstraint('upperarm_l', l_arm_group )
    m.delete(temp)
    l_arm_group = m.parent('upperarm_l_ik', 'upperarm_l_fk', l_arm_group)
    m.parent('l_arm', 'Exstra_skeleton')

    r_arm_group = m.group(em=True, n='r_arm')
    temp = m.parentConstraint('upperarm_r', r_arm_group )
    m.delete(temp)
    r_arm_group = m.parent('upperarm_r_ik', 'upperarm_r_fk', r_arm_group)
    m.parent('r_arm', 'Exstra_skeleton')

    r_leg_group = m.group(em=True, n='r_leg')
    temp = m.parentConstraint('thigh_r', r_leg_group )
    m.delete(temp)
    r_leg_group = m.parent('thigh_r_ik', 'thigh_r_fk', r_leg_group)
    m.parent('r_leg', 'Exstra_skeleton')
    
    

    l_leg_group = m.group(em=True, n='l_leg')
    temp = m.parentConstraint('thigh_l', l_leg_group )
    m.delete(temp)
    l_leg_group = m.parent('thigh_l_ik', 'thigh_l_fk', l_leg_group)
    m.parent('l_leg', 'Exstra_skeleton')

    #------------------------------------------------------------------------------


    # Parent the controls with the waist control

    
    #------------------------------------------------------------------------------

    m.parentConstraint('waist_ctrl', 'r_leg', mo=True)
    m.parentConstraint('waist_ctrl', 'l_leg', mo=True)


    m.parent( 'spine01_ctrl_Offset', 'waist_ctrl', a=True)




    """    # Replace these with the names of your control and group
    control_name_offset = 'thigh_l'
    group_name_offset = 'l_leg'

    # Get the pivot position of the control
    control_pivot_offset = m.xform(control_name_offset, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name_offset, piv=control_pivot_offset, ws=True)   


    # Replace these with the names of your control and group
    control_name_offset = 'thigh_r'
    group_name_offset = 'r_leg'

    # Get the pivot position of the control
    control_pivot_offset = m.xform(control_name_offset, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name_offset, piv=control_pivot_offset, ws=True)   

    # Replace these with the names of your control and group
    control_name_offset = 'upperarm_l'
    group_name_offset = 'l_arm'

    # Get the pivot position of the control
    control_pivot_offset = m.xform(control_name_offset, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name_offset, piv=control_pivot_offset, ws=True)   


    # Replace these with the names of your control and group
    control_name_offset = 'upperarm_r'
    group_name_offset = 'r_arm'

    # Get the pivot position of the control
    control_pivot_offset = m.xform(control_name_offset, q=True, rp=True, ws=True)

    # Set the pivot position of the group to match the control's pivot
    m.xform(group_name_offset, piv=control_pivot_offset, ws=True)   
    """

    #------------------------------------------------------------------------------


    # Hide the IK and FK joints

    
    #------------------------------------------------------------------------------


    joint_name = 'upperarm_l_ik'
    m.setAttr(joint_name + '.visibility', False)
    joint_name = 'upperarm_l_fk'
    m.setAttr(joint_name + '.visibility', False)
    joint_name = 'upperarm_r_ik'
    m.setAttr(joint_name + '.visibility', False)
    joint_name = 'upperarm_r_fk'
    m.setAttr(joint_name + '.visibility', False)

    joint_name = 'thigh_r_ik'
    m.setAttr(joint_name + '.visibility', False)
    joint_name = 'thigh_r_fk'
    m.setAttr(joint_name + '.visibility', False)
    joint_name = 'thigh_l_ik'
    m.setAttr(joint_name + '.visibility', False)
    joint_name = 'thigh_l_fk'
    m.setAttr(joint_name + '.visibility', False)

    ikHandle_name = 'IKHandle_leg_l_RP'
    m.setAttr(ikHandle_name + '.visibility', False)
    ikHandle_name = 'IKHandle_leg_l_SC'
    m.setAttr(ikHandle_name + '.visibility', False)
    ikHandle_name = 'IKHandle_leg_r_RP'
    m.setAttr(ikHandle_name + '.visibility', False)
    ikHandle_name = 'IKHandle_leg_r_SC'
    m.setAttr(ikHandle_name + '.visibility', False)

    ikHandle_name = 'IKHandle_arm_l'
    m.setAttr(ikHandle_name + '.visibility', False)
    ikHandle_name = 'IKHandle_arm_r'
    m.setAttr(ikHandle_name + '.visibility', False)




   # , 'lowerarm_l', 'hand_l'
    #for i in flat_left_list:
        #indexArm = flat_left_list.index("upperarm_l")
        
    
    #print(leftSideList[10,5])


    # Getting the root joint
    #root = emptylist[2:3] 

    #-------------------------------------------------------------------------------------------

    # Select root at the end of group creation
    m.select('root')



    """#-------------------------------------------------------------------------------------------
    # 

    #is this the arm or leg? 
    isArm = 1 # Set to 0 if working on the leg
    

#-------------------------------------------------------------------------------------------
  
    #Generate Names
    if isArm:
        limbType = 'arm'
        print ('Working with the arm leg')
        
    else:
        limbType = 'leg'
        print ('Working with the leg leg')
        
    
    #Checking the selection 
    selectionCheck = m.ls(sl=1, type='joint')
        
    
    #Error if nothing is selected
    if not selectionCheck: 
        m.error("Please select the root joint")
    else: 
        jointRoot = m.ls(sl=1, type='joint')[0]

#-------------------------------------------------------------------------------------------

    # PREFIX

      
    #Now we have selected joint
    # checking Prefix 
    global whichSide

    whichSide = jointRoot[0:2]

    #print(whichSide)

    # Make sure the prefix is usable
    if not 'l_' in whichSide:
        if not 'r_' in whichSide:
            m.error('Please use a joint with a usable prefix of either l_ or r_')
    

    armJointList = [whichSide + 'upperarm', whichSide + 'lowerarm', whichSide + 'hand']
   
    
    
    #How many joints are we working with? 
    limbJoints = len(armJointList)


#-------------------------------------------------------------------------------------------
    # Building names to be used
    #whichside: l_ or r_
    #limbType: arm 

    #Build the names we need for the arm
    limbName = whichSide + limbType

    #print (limbName)

    mainControl = limbName + '_ctrl'
    pawControlName = limbName + "_ik_ctrl"
    kneeControlName = limbName + '_tibia_ctrl' 
    hockControlName = limbName + '_hock_ctrl'
    rootControlName = limbName + '_root_ctrl'
    armControlName = limbName + "_ik_ctrl"


    #Build the names we need for the leg
    #limbNameLeg = whichSide + 'leg_' + limbType


#-------------------------------------------------------------------------------------------
    # Making a list of all the joints!

    # jointRoot: just the first joint you have selected
    # jointHierarchy: just the jointRoot and what is parented under it

    #Build the list of joints we are working with, using the root as a start point

    # Find its children
    jointHierarchy = m.listRelatives(jointRoot, ad=1, type='joint')

    #Add the selected joint to the list - or else it won't be added to the list
    jointHierarchy.append(jointRoot)

    #Reverse the list so we can work in order
    #jointHierarchy.reverse()

    # Clear the selection
    m.select(cl=1)

#-------------------------------------------------------------------------------------------

    # Duplicate the main joint chain and rename each joint

    
    #first define what joint chain need
    newJointList = ["_ik", "_fk", "_stretch"]

    #first define what controls we need
    newCtrlList = ['_ik_ctrl','_fk_ctrl']

    # Add the extra driver joints if this is the rear(arm)
    if limbType == 'leg': 
        newJointList.append("_driver")

#-------------------------------------------------------------------------------------------

    # Build the joints
    
    #Second loop is going through the hierarchy and displaying all the names not just the first one
    for newJoint in newJointList: 
        for i in range(limbJoints):
            newJointName = armJointList[i] + newJoint

            #print(newJointName)

            m.joint(n=newJointName)
            m.matchTransform(newJointName, armJointList[i])
            #Freeze transforms after the new position
            m.makeIdentity(newJointName, a=1, t=0, r=0, s=0)
        #This is what clears the selection and therefore not making the new joints parent each other
        m.select(cl=1)
    print(newJoint)
#-------------------------------------------------------------------------------------------
    # Constraining the 3 point ring: _ik + _fk + normal joint list

    # Constrain the main joints to the IK and FK joints so we can blend between them
    for i in range(limbJoints):
        #w=weights, mo=maintain offset
        m.parentConstraint( (armJointList[i] + '_ik'), (armJointList[i] + '_fk'), armJointList[i], w=1, mo=0)

    """
#-------------------------------------------------------------------------------------------
    
    #Create control for IK_FX blending
    #switch_control = m.circle(name="arm_IK_FK_ctrl")[0]
    # Create a custom attribute on the switch control for the IK/FK switch
    #m.addAttr(switch_control, ln="IK_FK_Switch", at="enum", enumName="IK:FK", k=True)

    #switch_control = utils.arrowSquare(10)
    #m.addAttr(switch_control, ln="IK_FK_Switch", at="enum", enumName="IK:FK", k=True)

    #m.rename(switch_control, 'arm_IK_FK_ctrl')


    """#-------------------------------------------------------------------------------------------
    # Create controls

    # Create controls and parent and orient them to the joints hierachy then delete their constraint
    for newJoint in newCtrlList: 
        for i in range(limbJoints):
            newCtrlName = armJointList[i] + '_' + limbType + newJoint
            #m.rotate( 0, '90deg', 0, r=True )
            m.circle(n=newCtrlName)
            m.matchTransform(newCtrlName, armJointList[i])
            
           # m.delete(ch=1)
            m.makeIdentity(newCtrlName, a=1, t=1, r=1, s=1, n=0, pn=1)

            print(newCtrlName)
            

        m.rotate(x=90,y=0,z=0,r=True, os=True )
        m.select(cl=1)
        #m.group((newCtrlList), n=(limbName + '_hand_control'))



#-------------------------------------------------------------------------------------------
    # Group controls

    #Select all the ctrls and group them under 1 group
    sel = m.select(whichSide + '*_ctrl')
    typ = m.ls(sl=1)
    scaleCtrl = 30
    m.scale(scaleCtrl,scaleCtrl,scaleCtrl)

    m.group( typ, name= whichSide + limbType + '_group' , w=1)
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
    """
 
#-------------------------------------------------------------------------------------------
    # SETUP FK ARM

    #Connect the FK controls to the FK joints
    """  for i in range(limbJoints):
        adjustingOrient = m.parentConstraint( (armJointList[i] + '_fk'), (armJointList[i] + '_' + limbType + '_fk_ctrl'))
        m.delete(adjustingOrient)
        m.parentConstraint( (armJointList[i] + '_' + limbType + '_fk_ctrl'), (armJointList[i] + '_fk'))
        
    """


#-------------------------------------------------------------------------------------------
    # SETUP IK ARM 

    """    for i in range(limbJoints):
        adjustingOrient = m.parentConstraint( (armJointList[i] + '_ik'), (armJointList[i] + '_' + limbType + '_ik_ctrl'))
        m.delete(adjustingOrient)"""

    
    """
    #Connect the IK controls to the IK joints
    #for i in range(limbJoints):
        #m.parentConstraint( (jointHierarchy[i] + '_' + limbType + '_ik_ctrl'), (jointHierarchy[i] + '_ik'), w=1, mo=0)



    
    #If it is the arm, create the ik handle from the femus to the metacarpus
    if limbType == 'leg': 
        m.ikHandle( n=(limbName + '_driver_ikHandle'), sol="ikRPsolver", sj=(jointHierarchy[0] + '_driver'), ee=(jointHierarchy[-1] + '_driver'))

    
    # Create the main IK handle from the femur to the metatarsus
    m.ikHandle( n=(limbName + '_elbow_ikHandle'), sol="ikRPsolver", sj=(jointHierarchy[0] + '_ik'), ee=(jointHierarchy[-1] + '_ik'))

    #sj=start, ee=end 
    #use this part for the foot of the leg in the future
    #m.ikHandle( n=(limbName + '_foot_ikHandle'), sol="ikSCsolver", sj=(jointHierarchy[2] + '_ik'), ee=(jointHierarchy[-1] + '_ik'))

    #Create the knee control offset group - also use this in combination with the foot instead of the _driver_ikhandle -> use _foot_ikHandle
    m.group((limbName + '_elbow_ikHandle'), n=(limbName + '_hand_control'))
    m.group((limbName + '_hand_control'), n=(limbName + '_hand_control_offset'))

    #Find the wrist pivot
    wristPivot = m.xform(jointHierarchy[-1], q=1, ws=1, piv=1)
    
    # Set the groups pivot to match the ankle position
    m.xform((limbName + '_hand_control'),(limbName + '_hand_control_offset'), ws=1, piv=(wristPivot[0],wristPivot[1],wristPivot[2]))


    # Find the last element in IK controls
    ikGroup = m.select('*ik_ctrl')
    ikGroupTyp = m.ls(sl=1)
    print(ikGroupTyp)

    # Parent the ik handle and the group to the paw control
    #m.parent((limbName + '_knee_control_offset'), (limbName + '_foot_ikHandle'))
    
    m.parent((limbName + '_hand_control_offset'), ikGroupTyp[-1])


    m.orientConstraint(ikGroupTyp[-1], (jointHierarchy[-1] + '_ik'), w=1)

    m.poleVectorConstraint(ikGroupTyp[0], )
    """