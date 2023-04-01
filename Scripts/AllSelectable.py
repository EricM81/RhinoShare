import rhinoscriptsyntax as rs
import scriptcontext as sc
import eLib as e

def AllSelectable():
    
    # skip turning on or off for specific layers from a template file
    layersToSkip = [
        '1ced3d60-c6a7-48b5-81f1-4daef190945f', #Layout::MM::Grandpappy
        '67bfd040-c5c5-4493-9b0e-8061b7d8c488' # 0
    ]

    # get a list of all layers in the document
    layerIDs = rs.LayerIds()
    
    # create an empty list to store the layer information
    layerStates = []

    # loop through each layer and get its visibility and lock state
    for layerID in layerIDs:
        if str(layerID) not in layersToSkip:
            # get the layer's visibility and lock state
            wasVisible = rs.LayerVisible(layerID, True, False)
            wasLocked = rs.LayerLocked(layerID, False)
           
            state = e.LayerState(layerID, wasVisible, wasLocked)
            # add the dictionary to the list
            layerStates.append(state)
        else:
            print("Skipping " + rs.LayerName(layerID))

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

    print("Showed " + str(len(hiddenObjs)) + " objects.")
    print("Unlocked " + str(len(lockedObjs)) + " objects.")

    # save the hidden objects list to the Rhino script context's sticky dictionary
    sc.sticky[e.hiddenObjsKey] = hiddenObjs
    sc.sticky[e.lockedObjsKey] = lockedObjs
    sc.sticky[e.layerStatesKey] = layerStates

if (__name__ == "__main__"):
    AllSelectable()


 # print(str(layerID) + ", " + rs.LayerName(layerID))
""" if not wasVisible:
    print(rs.LayerName(layerID))
    print(layerID) """
