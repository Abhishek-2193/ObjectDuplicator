#Duplicate Object Generator
#Program to generate duplicates of a certain object (Tree, Lamp, Mushroom or Cone)
#Objects are generated at cursor position on clicking while the respective button is toggeld on 

import maya.cmds as cmds
from functools import partial  

#UI Window function

def win():

	#window variable name
    winName = "lampGenerator"
    
    #check if window is already active
    if cmds.window(winName, exists = True):
        cmds.deleteUI(winName)
    
    #Initializing window name, size and attributes
    cmds.window(winName, sizeable = True,
                titleBar = True, resizeToFitChildren = True,
                menuBar = True, widthHeight = (450, 500),
                title = "Lamp Generator")
    
    cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=16)
    cmds.columnLayout(columnAttach=('left', 5), rowSpacing=10, columnWidth=250)
    
    #Creating window UI buttons and labels
    cmds.text(label = 'Generates object at click position when enabled', align = 'center')
    cmds.button(label = "Generate Lamp", command = 'startFunc(1)')
    cmds.button(label = "Generate Tree", command = 'startFunc(2)')
    cmds.button(label = "Generate Mushroom", command = 'startFunc(3)')
    cmds.button(label = "Generate Traffic Cone", command = 'startFunc(4)') 
    cmds.button(label = "Disable generation", command = 'endFunc()')
    
    cmds.showWindow()

#window function call
win()  

#Function to generate duplicates taking active toggle choice as argument
def generate(choice, *args):
    
    cmds.setToolTo('createObject') 
    
    #getting cursor click position
    pressPosition = cmds.draggerContext('createObject', query = True, anchorPoint=True)  
    
    #creating duplicate and xforming based on cursor position
    if (choice == 1):
        dupLamp = cmds.duplicate('newLamp')
        cmds.xform(dupLamp, translation = pressPosition)
        print "NOW" 
    elif (choice == 2):
        dupTree = cmds.duplicate('newTree')
        cmds.xform(dupTree, translation = pressPosition)
    elif (choice == 3):
        dupShroom = cmds.duplicate('newShroom')
        cmds.xform(dupShroom, translation = pressPosition)
    elif (choice == 4):
        dupVLC = cmds.duplicate('newVLC')
        cmds.xform(dupVLC, translation = pressPosition)
 
#def testFunc():
    #print "IT SHOULD WORK!" 
    
#function to enable object toggle button     
def startFunc(choice, *args):
    if cmds.draggerContext('createObject', exists = True):
        cmds.deleteUI("createObject")
         
    tmp = cmds.draggerContext('createObject', pressCommand = partial(generate, choice), space = 'world')
    print tmp
    cmds.setToolTo('createObject')    
            
#disable generating mode
def endFunc():
    cmds.setToolTo('selectSuperContext')

