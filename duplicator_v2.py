#Street Lamp Generator
import maya.cmds as cmds

#pressPosition = [0,0,0]

def win():
    winName = "lampGenerator"
    
    if cmds.window(winName, exists = True):
        cmds.deleteUI(winName)
    
    cmds.window(winName, sizeable = True,
                titleBar = True, resizeToFitChildren = False,
                menuBar = True, widthHeight = (450, 500),
                title = "Lamp Generator")
    
    cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=16)
    cmds.columnLayout(columnAttach=('left', 5), rowSpacing=10, columnWidth=250)
    
    cmds.text(label = 'Generates Street lamp at click position', align = 'center')
    cmds.button(label = "Enable generation", command = 'startFunc()')
    cmds.button(label = "Disable Generation", command = 'endFunc()') 
    
    cmds.showWindow()

win()  

def lampGenerate():
    
    pressPosition = cmds.draggerContext('createLamp', query = True, anchorPoint=True)
    print pressPosition 
    dupLamp = cmds.duplicate('newLamp')
    cmds.xform(dupLamp, translation = pressPosition) 
    
    
def startFunc():
    if cmds.draggerContext('createLamp', exists = True):
        cmds.deleteUI("createLamp")
    cmds.draggerContext('createLamp', pressCommand = 'lampGenerate()', space = 'world')
    cmds.setToolTo('createLamp') 

def endFunc():
    cmds.setToolTo('selectSuperContext')


startFunc()
