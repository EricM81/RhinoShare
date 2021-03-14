# RhinoScripts
Hi, I'm EricM and I make jewelry in Rhino3D.  You may have seen me use some scripts I wrote in my YT videos:
https://www.youtube.com/c/emarvets/

If you need help or have questions, please join our discord:
https://discord.gg/EuNnuUQ6NU

## General Instructions For Running Scripts

1) Save all the scripts to a specific folder (some scripts require other scripts to work).
2) Run a script with:
```
-RunPythonScript "<your scripts folder>\FingerRail.py"
```
3) Create aliases to call the scripts in **Tools -> Options -> Aliases**


For example, my scripts are located here:
```
C:\Users\EricM\Documents\CAD\zScripts\
```
And this is how my Rhino aliaseses are set:

![alt text](https://github.com/EricM81/RhinoScripts/blob/main/images/aliases.png?raw=true)

## The Scripts

### FingerRail.py

This will create a circle based on US nominal finger sizes.  

If you've measured your casting shrinkages for different investments, w:p ratios, etc, you can save those offsets in the script and apply them automatically:

![alt text](https://github.com/EricM81/RhinoScripts/blob/main/images/ShrinkageOffsets.png?raw=true)

I also like to throw my finger rails onto a special locked layer so I don't accidently scale them (`MoveToLayer=True`).

If you want to change any of these settings, you can open FingerRail.py in Notepad and edit the `#defaults you can edit` section:

```
# defaults you can edit

# finger size
fingerSize = 7.0

# default offsets to apply to counter act casting shrinkage
# make sure you have the same number of fields and values
offsetFields = ['Zero', 'Gypsum', 'Platinum']
offsetValues = [ 0.000,  0.125,    0.350]
#                0,      1,        2
selectedOffset = 1 #Gypsum

# move finger rail to a special layer and lock it
moveToLayer = True
layerName = '0'
layerColor = netColor.White

# end defaults you can edit
```

### CreateLayers.py

In older videos, you could see I had a bunch of default layers in my template.  Now, I've started creating them on demand with CreateLayers.py.  Just enter a parent name and you'll get a set of child layers with a HSV color scheme.

![alt text](https://github.com/EricM81/RhinoScripts/blob/main/images/CreateLayers.png?raw=true)

Check out some of the new videos to see how I use these.

### ReColorLayers.py

This will probably work best with layers created by CreateLayers.py, but it recolors the layer and all sub layers to a new hue.

![alt text](https://github.com/EricM81/RhinoScripts/blob/main/images/RecolorLayers1.png?raw=true)
![alt text](https://github.com/EricM81/RhinoScripts/blob/main/images/RecolorLayers2.png?raw=true)
![alt text](https://github.com/EricM81/RhinoScripts/blob/main/images/RecolorLayers3.png?raw=true)
