#!/usr/bin/env python3
#-------------------------------------------------------------------------------
import os
import shutil
import case_s_pc
import cprints
#-------------------------------------------------------------------------------


def move_from_to(item_path_a:str,item_path_b:str) -> None:
    """moves item from, to && check if path exists"""
    levelup_path = ''
    curpath = os.path.abspath(item_path_a).split('/')[-2]
    levelup_path = os.path.dirname(item_path_a).replace('/'+curpath,'')
    item_path_b = levelup_path if item_path_b == '..' else item_path_b
    if not case_s_pc.if_exists(item_path_b):
        print("moving {F}",item_path_a.replace(levelup_path+os.sep+curpath+os.sep,''),"{--> To}",
            item_path_b.replace(levelup_path+os.sep+curpath+os.sep,''))
        shutil.move(item_path_a,item_path_b)
    else:
        cprints.basic_color_print(1,"\nError: Item Already Exists or path entered is invaild")
        print(item_path_b,'\n')

#-------------------------------------------------------------------------------