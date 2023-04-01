import rhinoscriptsyntax as rs
import scriptcontext as sc
import Color as c


def createLayers():

    name = rs.GetString("Parent Layer Name")
    if name:
        geoName = "Working::" + name
        cutterName = "Cutters::" + name
        layoutName = "Layout::" + name

        if not rs.IsLayer(geoName):
            # Figure out new layers color structure
            lastHueKey = "lastHue"
            lastHue = 0

            if lastHueKey in sc.sticky:
                lastHue = sc.sticky[lastHueKey]

            hue = lastHue + 30
            if 59 < hue and hue < 149:
                hue = 160
            if 360 < hue:
                hue = 15

            sc.sticky[lastHueKey] = hue

            rs.CurrentLayer("Working")

            # create geometry layers

            rs.AddLayer(geoName, c.HSVToColor(hue / 360, 1.0, 1.0))
            # rs.CurrentLayer(name)
            rs.AddLayer(geoName, c.HSVToColor(hue / 360, 1.0, 1.0))
            rs.AddLayer(geoName + "::Control", c.HSVToColor(hue / 360, 0.50, 1.0))
            rs.AddLayer(geoName + "::Control::Junk", c.HSVToColor(hue / 360, 1.0, 0.25))
            # rs.LayerLocked(name + "::Control::Junk", True)
            rs.AddLayer(geoName + "::Crvs", c.HSVToColor(hue / 360, 1.0, 0.50))
            rs.AddLayer(geoName + "::Srf", c.HSVToColor(hue / 360, 1.0, 1.0))

            if not rs.IsLayer(layoutName):
                rs.AddLayer(layoutName, c.HSVToColor(hue / 360, 1.0, 1.0))
                rs.AddLayer(layoutName + "::Crvs", c.HSVToColor(hue / 360, .15, 0.60))
                rs.AddLayer(layoutName + "::Srf", c.HSVToColor(hue / 360, .15, .30))

            if not rs.IsLayer(cutterName):
                rs.AddLayer(cutterName, c.HSVToColor(hue / 360, 1.0, 1.0))
                rs.AddLayer(cutterName + "::Crvs", c.HSVToColor(120, 1.0, 0.50))
                rs.AddLayer(cutterName + "::Srf", c.HSVToColor(120, 1.0, .30))

        else:
            print("ERROR: Layer already exists.")


if (__name__ == "__main__"):
    createLayers()
