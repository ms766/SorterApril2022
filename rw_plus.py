#!/usr/bin/env python3
#-------------------------------------------------------------------------------


def file_to_list(file_name:str) -> list:
    '''reads in file and returns a list'''
    with open(file_name) as f:
        content_ls = f.read().split('\n')
        if '' in content_ls:
            content_ls.remove('')
        return content_ls

   
#-------------------------------------------------------------------------------


def list_to_file(file_name:str,in_list:list) -> None:
    '''takes list and write each element on a new lines in a file'''
    in_list = sorted(in_list)
    "writes list to a file"
    with open(file_name,'w') as f:
        for i in in_list:
            f.write(i+'\n')


#------------------------------------------------------------------------------- 


def change_tracker(file_name:str,old_in_str:str,new_in_str:str) -> None:
    '''appends old str +\n+ new str + \n\n to a text file'''
    with open(file_name,'a') as f:
        f.write(old_in_str+'\n'+new_in_str+'\n\n')
        
        
#------------------------------------------------------------------------------- 