#!/usr/bin/env python3
import os
import re
import dir_crt_plus
import nci_mover
import cprints
#-------------------------------------------------------------------------------


def season_builder(path:str) -> None:
    path_f_ls_content = dir_crt_plus.list_non_hidden_content(path,'f')
    path_d_ls_content = dir_crt_plus.list_non_hidden_content(path,'d')
    #---------------------------------------------------------------------------
    for file in sorted(path_f_ls_content):
        f,_ = os.path.splitext(file)
        #tv eps section
        if re.search('s[0-9]+ e[0-9]+',f.lower()):
            in_f_ls = f.lower().split(' ')[:-1]
            in_f_ls[-1] = in_f_ls[-1].replace('s','')
            f = re.sub(r'S(?=[0-9])', ' - Season ',file)
            f = re.sub(r'E[0-9].*', '',f)
            f = re.sub(r'[ \s]{1,}', ' ',f).lstrip().rstrip()
            if not os.path.isdir(path+os.sep+f) and 'Season' in f:
                os.mkdir(path+os.sep+f)
                season_builder(path)
            for dir in sorted(path_d_ls_content):
                #------> ERROR HERE dir is empty
                if re.search('season',dir.lower()) and '-' in dir:
                    in_d_ls = dir.lower().replace('- season','').replace('season','').split(' ')
                    if '' in in_d_ls: in_d_ls.remove('')
                    if in_f_ls == in_d_ls:
                        src=path+'/'+file
                        des = path+'/'+dir+'/'+file
                        nci_mover.move_from_to(src,des)
                        

#-------------------------------------------------------------------------------
