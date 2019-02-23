#Duplicate Object Duplicator
#Program to generate duplicates of a selected object on click
#Objects are generated at cursor position on clicking while the generate mode is toggled on

import maya.cmds as cmds
from functools import partial

#UI Window function


def win():

        #window variable name
    winName = "lampGenerator"

    #check if window is already active
    if cmds.window(winName, exists=True):
        cmds.deleteUI(winName)

    #Initializing window name, size and attributes
    cmds.window(winName, sizeable=True,
                titleBar=True, resizeToFitChildren=True,
                menuBar=True, widthHeight=(450, 500),
                title="Object Duplicator")

    cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=16)
    cmds.columnLayout(columnAttach=('left', 5), rowSpacing=10, columnWidth=250)

    #Creating window UI buttons and labels
    cmds.text(label='Generates object at click position when enabled', align='center')
    cmds.button(label="Enable generation", command='generate()')
    cmds.button(label="Disable generation", command='endFunc()')

    cmds.showWindow()


#window function call
win()

#Function to generate duplicates taking active toggle choice as argument


def generate():

    cmds.setToolTo('createObject')
    dupObj = cmds.duplicate(cmds.ls(sl=True))

    #getting cursor click position
    pressPosition = cmds.draggerContext('createObject', query=True, anchorPoint=True)

    #creating duplicate and xforming based on cursor position
    print dupObj
    cmds.xform(dupObj, translation=pressPosition)


def endFunc():
    cmds.setToolTo('selectSuperContext')
