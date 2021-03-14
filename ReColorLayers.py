#from __future__ import Color as c
#from __future__ import division
import rhinoscriptsyntax as rs
import Rhino as r
import rhinoscript.layer as rl
import Color as c

from System.Drawing import Color as netColor

def changeHue(layer, newHue):
    origRGB = rl.LayerColor(layer)
    origHSV = c.RGBToHSV(origRGB.R, origRGB.G, origRGB.B)
    newHSV = (newHue, origHSV[1], origHSV[2])
    newColor = c.HSVToColor(newHSV[0], newHSV[1], newHSV[2])
    
    rl.LayerColor(layer, newColor)

def doLayer(layer, newHue):
    changeHue(layer, newHue)
    if rl.LayerChildCount(layer) > 0:
        layers = rl.LayerChildren(layer)
        for x in layers:
            doLayer(x, newHue)

def recolorLayer():
    
    layer = rs.GetLayer("Select Layer:")
    color = netColor.Aqua
    picked, color = r.UI.Dialogs.ShowColorDialog(color)
    
    if layer and picked:
        
        (hue, lum, sat) = rs.ColorRGBToHLS(color)
        doLayer(layer, hue)

if( __name__ == "__main__" ):
    recolorLayer()