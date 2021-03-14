from System.Drawing import Color as netColor
import Rhino
import rhinoscriptsyntax as rs

#defaults you can edit

#finger size and layer to move to
fingerSize = 7.0

#make sure you have the same number of fields and values

offsetFields = ['Zero', 'Gypsum', 'Platinum']
offsetValues = [ 0.000,  0.125,    0.350]
#                0,      1,        2
selectedOffset = 1 #Gypsum

#move finger rail to a special layer and lock it
moveToLayer = True
layerName = '0'
layerColor = netColor.White

#end defaults you can edit

def createFingerRail():
    offset = offsetValues[selectedOffset]
    size = fingerSize + offset
    rad = (11.6 + (size * 0.203125 * 4)) / 2
    
    fingerRail = rs.AddCircle(rs.WorldZXPlane(), rad)
    label = '{:.3f} + {:.3f}'.format(fingerSize, offset)
    rs.ObjectName(fingerRail, 'Size: ' + label)
    rs.SetUserText(fingerRail, 'Size', label)
    if moveToLayer:
        if not rs.IsLayer(layerName):
            rs.AddLayer(layerName, layerColor, True, True, None)
        rs.ObjectLayer(fingerRail, layerName)
        
def getOffset():
    global selectedOffset
    go = Rhino.Input.Custom.GetOption()
    
    go.SetCommandPrompt("Select an offset to apply")
    go.AcceptNothing(True)
    
    for i in range(len(offsetFields)):
        go.AddOption(offsetFields[i], str(offsetValues[i]))
    go.SetDefaultString(offsetFields[selectedOffset])
    
    go.Get()
    res = go.CommandResult()

    if res == Rhino.Commands.Result.Success:
        index = go.OptionIndex()
        
        if index >= 0:
            option = go.Option().EnglishName
            for i in range(len(offsetFields)):
                if option == offsetFields[i]:
                    selectedOffset = i
                    break
        #else: they went with default and there's nothing to update

def FingerRail():
    global selectedOffset
    global fingerSize
    global moveToLayer

    while True:
        gn = Rhino.Input.Custom.GetNumber()
        
        offsetOption = offsetFields[selectedOffset]
        gn.AddOption(offsetOption, str(offsetValues[selectedOffset]))
        layerOption = 'MoveToLayer'
        gn.AddOption(layerOption, str(moveToLayer))
        
        gn.SetCommandPrompt("Finger size")
        gn.SetDefaultNumber(fingerSize)
        gn.SetLowerLimit(1.0, False)
        gn.SetUpperLimit(30, False)
        gn.AcceptNothing(True)
        
        gn.Get()
        res = gn.CommandResult()

        if res == Rhino.Commands.Result.Success:
            index = gn.OptionIndex()
            if index >= 0:
                option = gn.Option().EnglishName
                if option == offsetOption:
                    getOffset()
                if option == layerOption:
                    moveToLayer = not moveToLayer
            else:
                fingerSize = gn.Number()
                createFingerRail()
                break
        else:
            break


if( __name__ == "__main__" ):
    FingerRail()  