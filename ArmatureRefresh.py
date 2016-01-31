#------------------------------------------------------------
# Name:        Armature Refresh
#
# Purpose:     Blender script to refresh incorrect armature 
#              positions before rendering current frame. This
#              tiny script could fix your problems if your rig
#              doesn't update itself correctly before you're 
#              rendering it.
#
# Commanline:  Render through command line using this script
#              blender -b FILENAME.blend -P ArmatureRefresh.py
#
# Author:      Creatide / Sakari Niittymaa
# Created:     21.11.2012
#
# Copyright:   Copyright(c) 2016 Creatide / Sakari Niittymaa
#              http://www.creatide.com
#              hello@creatide.com
#
# Licence:     The MIT License (MIT)
#------------------------------------------------------------

import bpy, sys
from bpy import data, ops, props, types, context

# Scene that be used
scene = bpy.context.scene

# Loop every frame
for frame in range(scene.frame_end + 1):

    # Current frame
    scene.frame_set(frame)
    print('Rendering frame: ' + frame)

    # Select armature in pose mode and move it
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            scene.objects.active = obj
            scene.objects.active.mode_set(mode = 'POSE')
            obj.transform.translate()

    # Render current frame
    bpy.ops.render.render(write_still=True)
