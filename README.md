Armature Refresh (Blender Script)
=================================

Blender script that refresh incorrect armature positions before rendering current frame. This tiny script could fix your problems if your rig doesn't update itself correctly before you're rendering it.

> I face this problem couple years ago, so I'm not sure if this script is still useful.

## How to Use

This script meant to drive before rendering, so I used it through **command line** in Windows. I write blog post about ["Render From Command Line"](http://niittymaa.com/blog/blender/render-from-command-line/). You just need simple command to run script with rendering process:

`blender -b FILENAME.blend -P ArmatureRefresh.py`

## Author
[Creatide](http://creatide.com) / [Sakari Niittymaa](http://niittymaa.com)

## Licence
The MIT License (MIT)
Copyright (c) 2016 Creatide / Sakari Niittymaa
