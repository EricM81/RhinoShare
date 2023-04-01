import rhinoscriptsyntax as rs
import scriptcontext as sc
import eLib as e




def renameLayers():
    layersToRename = []
    prompt = "Should pasted objects be on a different layer?"
    while True:
        answer = rs.GetString(prompt, "No", ["Yes"])
        if answer == "Yes":
            layerID = rs.GetLayer("Select layer to rename:")
            if not layerID:
                break
            oldName = rs.LayerName(layerID)
            print(oldName)              
            
            
            newName = rs.GetString("New Layer name for pasted objects", e.removeLayerParents(oldName) + "-Copy")
            newName = str.replace(oldName, e.removeLayerParents(oldName), newName)
            print(newName)              
            
            if not newName:
                break
            layersToRename.append(e.LayerName(layerID, oldName, newName))
            prompt = "Would you like to change any other layers?"
        else:
            break
    
    return layersToRename


def CopyWithHistory():

    objs = rs.GetObjects("Select objects to copy with history", preselect=True)
    if objs: 
        layersToRename =  renameLayers()

        if 0 < len(layersToRename):
            for layer in layersToRename:
               e.renameLayer(layer.oldName, layer.newName)


        rs.Command("_CopyToClipboard", False)
        rs.HideObjects(objs)
        
        if 0 < len(layersToRename):
            for layer in layersToRename:
               e.renameLayer(layer.newName, layer.oldName)
                
        rs.Command("_Paste", False)
        pastedCount = len(rs.SelectedObjects())
        rs.UnselectAllObjects()
        rs.Command("_SelObjectsWithHistory", False)
        parentCount = len(rs.SelectedObjects())
        rs.InvertSelectedObjects()
        strResponse = "Copied {0:d} with history. {1:d} root parents without history are selected and can be moved to a new location.".format(pastedCount, parentCount)

        print(strResponse)
        


if (__name__ == "__main__"):
    CopyWithHistory()
