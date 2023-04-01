import rhinoscriptsyntax as rs
import scriptcontext as sc
import eLib as e

def AllSelectable():
    
    # get a list of all layers in the document
    layerIDs = rs.LayerIds()
    
    # create an empty list to store the layer information
    layerStates = []

    # loop through each layer and get its visibility and lock state
    for layerID in layerIDs:
        # get the layer's visibility and lock state
        wasVisible = rs.LayerVisible(layerID, True, False)
        wasLocked = rs.LayerLocked(layerID, False)

        state = e.LayerState(layerID, wasVisible, wasLocked)
        # add the dictionary to the list
        layerStates.append(state)
        

    objects = rs.AllObjects()

    # create an empty list to store the hidden objects
    hiddenObjs = []
    lockedObjs = []

    # loop through each object and get its visibility
    for obj in objects:
        # get the object's current visibility
        if rs.IsObjectHidden(obj):
            hiddenObjs.append(obj)
        if rs.IsObjectLocked(obj):
            lockedObjs.append(obj)
            
    rs.ShowObjects(hiddenObjs)
    rs.UnlockObjects(lockedObjs)

    # save the hidden objects list to the Rhino script context's sticky dictionary
    sc.sticky[e.hiddenObjsKey] = hiddenObjs
    sc.sticky[e.lockedObjsKey] = lockedObjs
    sc.sticky[e.layerStatesKey] = layerStates

if (__name__ == "__main__"):
    AllSelectable()
