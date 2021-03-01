#Duplicate Object Duplicator
#Tool to generate duplicates of a selected object on click

import maya.cmds as cmds
from functools import partial

def initiate():
    #tool context definition
    if cmds.draggerContext('createObject', exists=True):
        cmds.deleteUI('createObject')
    
    cmds.draggerContext('createObject', pc = 'generate()', dc = 'generate()', cur = 'hand', i1 = 'duplicateReference.png', space = 'world');
    cmds.setToolTo('createObject')

#Function to generate duplicates of currently selected object(s)
def generate():

    objList = cmds.ls(sl = True)

    if(objList):
    
        #getting cursor click position
        pressPosition = cmds.draggerContext('createObject', query = True, ap = True, dp = True)

        #creating duplicate and xforming based on cursor position
        dupObj = cmds.duplicate(objList)
        cmds.xform(dupObj, translation = pressPosition, ws = True)

    else:

        cmds.confirmDialog(title = "Empty Selection", m = "Select objects to duplicate before using tool", button = 'ok')
