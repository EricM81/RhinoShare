import rhinoscriptsyntax as rs
import scriptcontext as sc
import Color as c

def createLayers():
    name = rs.GetString("Parent Layer Name")
    
    if name:
        if rs.IsLayer(name) == False:
            hsv = "lastHue"
            hue = 0
            if sc.sticky.has_key(hsv): hue = sc.sticky[hsv]
            if (hue + 30) == 120:
                sc.sticky[hsv] = hue+60
            elif (hue + 30) >= 360:
                sc.sticky[hsv] = 0
            else:
                sc.sticky[hsv] = hue+30
            
            rs.AddLayer(name, c.HSVToColor(hue/360, 1.0, 1.0))
            rs.CurrentLayer(name)
            rs.AddLayer(name + "::Control", c.HSVToColor(hue/360, 0.50, 1.0))
            rs.AddLayer(name + "::Control::Junk", c.HSVToColor(hue/360, 1.0, 0.25))
            rs.LayerLocked(name + "::Control::Junk", True)
            rs.AddLayer(name + "::Crvs", c.HSVToColor(hue/360, 1.0, 0.50))
            rs.AddLayer(name + "::Srf", c.HSVToColor(hue/360, 1.0, 1.0))
        else:
            print "ERROR: Layer already exists."

if( __name__ == "__main__" ):
    createLayers()