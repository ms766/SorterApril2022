#!/usr/bin/env python3
#-------------------------------------------------------------------------------
import os
#-------------------------------------------------------------------------------


def if_exists(item_path:str) -> bool:
    print(item_path)
    '''A Case Sensentive item exists checker'''
    item = item_path.split('/')[-1]
    root_path = item_path.replace(item_path.split('/')[-1],'')
    if os.path.exists(item_path) and item in os.listdir(root_path):
        return True
    else:
        return False
    

#-------------------------------------------------------------------------------