import rhinoscriptsyntax as rs
import scriptcontext as sc
import eLib as e

def UndoAllSelectable():

    if sc.sticky.has_key(e.layerStatesKey):
        layerStates = sc.sticky[e.layerStatesKey]
        if isinstance(layerStates, list):
            for layer in layerStates:
                if isinstance(layer, e.LayerState) and rs.IsLayer(layer.layerId):
                    rs.LayerVisible(layer.layerId, layer.visible)
                    rs.LayerLocked(layer.layerId, layer.locked)
        
        del sc.sticky[e.layerStatesKey]


    if sc.sticky.has_key(e.hiddenObjsKey):
        hiddenObjs = sc.sticky[e.hiddenObjsKey]
        if isinstance(hiddenObjs, list):
            rs.HideObjects(hiddenObjs)
            print("Hid " + str(len(hiddenObjs)) + " objects.")
    
        del sc.sticky[e.hiddenObjsKey]

    if sc.sticky.has_key(e.lockedObjsKey):
        lockedObjs = sc.sticky[e.lockedObjsKey]
        if isinstance(lockedObjs, list):
            rs.LockObjects(lockedObjs)
            print("Locked " + str(len(lockedObjs)) + " objects.")

        del sc.sticky[e.lockedObjsKey]

if (__name__ == "__main__"):
    UndoAllSelectable()
