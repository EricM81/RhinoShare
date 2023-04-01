
layerStatesKey = "layerState"
hiddenObjsKey = "hiddenObjs"
lockedObjsKey = "lockedObjs"

class LayerState:
    def __init__(self, layerId, visible, locked):
        self.layerId = layerId
        self.visible = visible
        self.locked = locked