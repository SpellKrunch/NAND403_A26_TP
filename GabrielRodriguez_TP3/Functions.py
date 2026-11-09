
# imports for script
import maya.cmds as cmds 
import random

# function that generates random animation key for all selected objects in Maya 
def generate_animation(duration_value, step_value, trl_min_x, trl_min_y, trl_min_z,
                       trl_max_x,trl_max_y,trl_max_z,rot_min_x,rot_min_y,rot_min_z,
                       rot_max_x,rot_max_y,rot_max_z,scl_min_x,scl_min_y,scl_min_z, 
                       scl_max_x,scl_max_y,scl_max_z
                       ):

    # creating a chunk for the Ctrl+Z function 
    cmds.undoInfo(openChunk=True, chunkName="Animation")

    # get all selected items in the Maya scene 
    selected_obj = cmds.ls(selection = True)


    # Begining of the chunk  
    try:

         # for loop on the floored division of the animation duration and the step value 
         for j in range((duration_value // step_value)):

                    # for loop on the number of selected objects 
                    for i in range(len(selected_obj)):

                         # set a key frame of a specific attribute at a random value at the given steps
                         cmds.setKeyframe(selected_obj[i],attribute="translateX",value=(random.randrange(trl_min_x,trl_max_x)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="translateY",value=(random.randrange(trl_min_y,trl_max_y)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="translateZ",value=(random.randrange(trl_min_z,trl_max_z)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="rotateX",value=(random.randrange(rot_min_x,rot_max_x)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="rotateY",value=(random.randrange(rot_min_y,rot_max_y)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="rotateZ",value=(random.randrange(rot_min_z,rot_max_z)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="scaleX",value=(random.randrange(scl_min_x,scl_max_x)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="scaleY",value=(random.randrange(scl_min_y,scl_max_y)),time=[step_value * (j+1)])
                         cmds.setKeyframe(selected_obj[i],attribute="scaleZ",value=(random.randrange(scl_min_z,scl_max_z)),time=[step_value * (j+1)])

         # for loop on the number of selected objects 
         for i in range(len(selected_obj)):

              # set a key frame of a specific attribute at a random value at the first and last frame
              cmds.setKeyframe(selected_obj[i],attribute="translateX",value=(random.randrange(trl_min_x,trl_max_x)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="translateY",value=(random.randrange(trl_min_y,trl_max_y)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="translateZ",value=(random.randrange(trl_min_z,trl_max_z)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="rotateX",value=(random.randrange(rot_min_x,rot_max_x)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="rotateY",value=(random.randrange(rot_min_y,rot_max_y)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="rotateZ",value=(random.randrange(rot_min_z,rot_max_z)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="scaleX",value=(random.randrange(scl_min_x,scl_max_x)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="scaleY",value=(random.randrange(scl_min_y,scl_max_y)),time=[1,duration_value])
              cmds.setKeyframe(selected_obj[i],attribute="scaleZ",value=(random.randrange(scl_min_z,scl_max_z)),time=[1,duration_value])


    # Reset the Chunk if Ctrl+Z is pressed 
    finally:
         cmds.undoInfo(closeChunk=True)
         







