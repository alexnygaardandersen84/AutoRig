import maya.cmds as cmds
import maya.mel as mel

def a_to_b(is_trans=True, is_rot=True, sel=None, freeze=False):
    # if selection list is not defined, use selected in scene
    if not sel:
        sel = cmds.ls(selection=True)

    for s in sel:
        # make sure translate/rotate is not locked before moving
        tr_list = []
        if is_trans:
            tr_list.append('translate')
            if any(cmds.getAttr(s + '.translate' + attr, lock=True) for attr in 'XYZ'):
                cmds.error('This will not work if any translate attributes are locked!')
        if is_rot:
            tr_list.append('rotate')
            if any(cmds.getAttr(s + '.rotate' + attr, lock=True) for attr in 'XYZ'):
                cmds.error('This will not work if any rotate attributes are locked!')

        if s != sel[-1]:
            con_list = []
            # check for objects with any transformation connections
            # add them to con_list if a connection exists
            for tr in tr_list:
                con = cmds.listConnections(s + '.' + tr, destination=False,
                                           source=True, plugs=True)
                if con:
                    [con_list.append(c) for c in con]
                for attr in 'XYZ':
                    con = cmds.listConnections(s + '.' + tr + attr,
                                               destination=False, source=True,
                                               plugs=True)
                    if con:
                        [con_list.append(c) for c in con]

            # check for translate/rotate attribute string in lists
            has_trans = any('ranslate' in con for con in con_list)
            has_rot = any('otate' in con for con in con_list)

            # skip if there are connections
            if has_trans and has_rot:
                print(s + ' has incoming translation and rotation connections '\
                      'and was not constrained to destination object.')
                continue
            elif has_trans and not has_rot:
                print(s + ' has incoming translation connections and was not '\
                                      'constrained to destination object.')
                continue
            elif has_rot and not has_trans:
                print(s + ' has incoming rotation connections and was not '\
                                      'constrained to destination object.')
                continue

            # if their attributes are not locked/connected, then let's move them
            else:
                if is_trans:
                    cmds.delete(cmds.pointConstraint(sel[-1], s,
                                                     maintainOffset=False))
                if is_rot:
                    cmds.delete(cmds.orientConstraint(sel[-1], s,
                                                      maintainOffset=False))
        if freeze:
            cmds.makeIdentity(s, apply=True, translate=True, rotate=True,
                              scale=True, normal=False)
            

# align local rotation axes of control to the joint
def align_lras(snap_align=False, delete_history=True, sel=None):
    # get selection (first ctrl, then joint)
    if not sel:
        sel = cmds.ls(selection=True)

    if len(sel) <= 1:
        cmds.error('Select the control first, then the joint to align.')
    ctrl = sel[0]
    jnt = sel[1]

    # check to see if the control has a parent
    # if it does, un parent it by parenting it to the world
    parent_node = cmds.listRelatives(ctrl, parent=True)
    if parent_node:
        cmds.parent(ctrl, world=True)

    # store the ctrl/joint's world space position, rotation, and matrix
    jnt_matrix = cmds.xform(jnt, query=True, worldSpace=True, matrix=True)
    jnt_pos = cmds.xform(jnt, query=True, worldSpace=True, rotatePivot=True)
    jnt_rot = cmds.xform(jnt, query=True, worldSpace=True, rotation=True)
    ctrl_pos = cmds.xform(ctrl, query=True, worldSpace=True, rotatePivot=True)
    ctrl_rot = cmds.xform(ctrl, query=True, worldSpace=True, rotation=True)

    # in maya 2020 we can choose to use the offsetParentMatrix instead of
    # using an offset group
    if cmds.objExists(ctrl + '.offsetParentMatrix'):
        off_grp = False
        # ensure offset matrix has default values
        cmds.setAttr(ctrl + '.offsetParentMatrix',
                     [1.0, 0.0, 0.0, 0.0, 0.0,
                      1.0, 0.0, 0.0, 0.0, 0.0,
                      1.0, 0.0, 0.0, 0.0,0.0,
                      1.0], type='matrix')
        reset_to_origin(ctrl)
        # copy joint's matrix to control's offsetParentMatrix
        cmds.setAttr(ctrl + '.offsetParentMatrix', jnt_matrix, type='matrix')

        if parent_node:
            # make temporary joints to help calculate offset matrix
            tmp_parent_jnt = cmds.joint(None, name='tmp_01_JNT')
            tmp_child_jnt = cmds.joint(tmp_parent_jnt, name='tmp_02_JNT')
            a_to_b(sel=[tmp_parent_jnt, parent_node[0]])
            a_to_b(sel=[tmp_child_jnt, jnt])
            cmds.parent(ctrl, parent_node[0])
            reset_transforms(ctrl)

            child_matrix = cmds.getAttr(tmp_child_jnt + '.matrix')
            cmds.setAttr(ctrl + '.offsetParentMatrix', child_matrix, type='matrix')
            cmds.delete(tmp_parent_jnt)

    # Maya 2019 and below
    else:
        reset_to_origin(ctrl)
        # create offset group
        off_grp = cmds.createNode('transform', name=ctrl + '_OFF_GRP')

        # move offset group to joint position, parent ctrl to it, zero channels
        cmds.xform(off_grp, worldSpace=True, translation=jnt_pos, rotation=jnt_rot)
        if parent_node:
            cmds.parent(off_grp, parent_node[0])


    # move the control back into place
    cmds.xform(ctrl, worldSpace=True, translation=ctrl_pos)
    cmds.xform(ctrl, worldSpace=True, rotation=ctrl_rot)

    # parent control to offset group, if it exists
    if off_grp:
        cmds.parent(ctrl, off_grp)

    # freeze transforms again, then move pivot to match joint's
    if snap_align:
        reset_transforms(ctrl)
    else:
        cmds.makeIdentity(ctrl, apply=True, translate=True, rotate=True,
                          scale=False, normal=False)
    cmds.xform(ctrl, worldSpace=True, pivots=jnt_pos)

    # delete construction history
    if delete_history:
        cmds.delete(ctrl, ch=True)

    if off_grp:
        return off_grp
    else:
        return ctrl
    

# transfers pivots to either first selected object or origin
def transfer_pivots(origin=False, sel=False):
    # if selection list is not defined, use selected in scene
    if not sel:
        sel = cmds.ls(selection=True)

    # move pivot to origin
    if origin:
        for s in sel:
            cmds.xform(s, worldSpace=True, pivots=(0, 0, 0))

    # move pivot to first selected object
    else:
        # get the rotate pivot
        first_piv = cmds.xform(sel[0], query=True, worldSpace=True,
                               rotatePivot=True)
        for s in sel[1:]:
            # set the rotate and scale pivot simultaneously
            cmds.xform(s, worldSpace=True, pivots=first_piv)


def reset_to_origin(node, node_pos=False):
    # get the node's position if it is not provided
    if not node_pos:
        node_pos = cmds.xform(node, query=True, worldSpace=True, rotatePivot=True)

    # translate control to origin
    # ensure translation is frozen
    cmds.makeIdentity(node, apply=True, translate=True, rotate=False,
                      scale=False, normal=False)

    # offset to origin
    node_offset = [p * -1 for p in node_pos]
    cmds.xform(node, worldSpace=True, translation=node_offset)

    # zero rotates, then freeze all transforms
    cmds.setAttr(node + '.rotate', 0, 0, 0)
    cmds.makeIdentity(node, apply=True, translate=True, rotate=True,
                      scale=False, normal=False)

def reset_transforms(nodes):
    if not nodes:
        nodes = cmds.ls(selection=True)

    # if nodes isn't a list, make it one
    if not isinstance(nodes, list):
        nodes = [nodes]

    for node in nodes:
        cmds.setAttr(node + '.translate', 0, 0, 0)
        cmds.setAttr(node + '.rotate', 0, 0, 0)
        cmds.setAttr(node + '.scale', 1, 1, 1)


