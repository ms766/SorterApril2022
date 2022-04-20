#!/usr/bin/env python3
import os
import shutil
import gcd
import strcl
import rw_plus as rwp
import case_s_pc
import dir_crt_plus as dcp
import cprints
import outbound_sorter as obs
import season_builder as sb
#-------------------------------------------------------------------------------

def file_funnel(path,topdown=True,cleanup=False,protected_dirsls=[],protected_srt_paths=[]):
    srtls = [];
    all_exts = [];
    protected_dirs = [];
    vilist = rwp.file_to_list(gcd.get_config_data("video_exts_data"))
    bdlist = rwp.file_to_list(gcd.get_config_data("all_bad_exts_data"))
    aplist = rwp.file_to_list(gcd.get_config_data('apps_exts_data'))
    good_ls = rwp.file_to_list(gcd.get_config_data('all_good_exts_data'))
    for subdir, dirs, files in os.walk(path,topdown):
        for file in files:
            base,ext = os.path.splitext(file)
            if not file.startswith('.') and file != 'Icon\r':
                o_f_path = subdir + os.sep + file
                if cleanup == False:
                    u_f_path = subdir + os.sep + strcl.str_cleaner(base,ext)+ext
                    if not case_s_pc.if_exists(u_f_path):
                        cprints.fdp_color_print(o_f_path,u_f_path)
                        os.rename(o_f_path,u_f_path)
                        rwp.change_tracker(path+os.sep+"*titlechanges.txt",dcp.bn(o_f_path),dcp.bn(u_f_path))
                        
                    #saves dirs
                    if subdir != path and ext in vilist:
                        if subdir not in srtls and ext == '.srt':
                            srtls.append(u_f_path.split(ext)[0])
                        if subdir not in all_exts and ext != '.srt':
                            all_exts.append(u_f_path.split(ext)[0])  
                            
                    if subdir != path and ext in aplist and subdir not in protected_dirs:
                       protected_dirs.append(subdir)
                        
                if cleanup == True:
                    if case_s_pc.if_exists(o_f_path):
                        if subdir not in protected_dirsls and subdir != path and ext in bdlist:
                            os.remove(o_f_path)
                        elif o_f_path not in protected_srt_paths and ext == '.srt' and 'english' not in file.lower():
                            os.remove(o_f_path)
                        elif o_f_path not in protected_srt_paths and ext == '.srt' and 'eng' not in file.lower():
                            os.remove(o_f_path)
                        elif 'sample' in file.lower():
                            os.remove(o_f_path)
                        elif 'trailer' in file.lower():
                            os.remove(o_f_path)
    if cleanup == False:
        cprints.basic_color_print(5,"f's RENAMING PROCESSED ^\n")
        temp_ls = []
        [temp_ls.append(item+'.srt') for item in all_exts if item in srtls] 
        file_funnel(path,True,True,protected_dirs,temp_ls)


#-------------------------------------------------------------------------------
def dir_content_sort(root_path:str) -> None:
    for item in dcp.list_non_hidden_content(root_path):
        obs.outbound_sorter(root_path+os.sep+item)
    
                
def dir_funnel(path,topdown=True,cleanup_start=False,cleanup_finish=False):
    for subdir, dirs, files in os.walk(path,topdown): 
        for dir in dirs:
            if dir.startswith('.') == False:
                o_d_path = subdir + os.sep + dir
                u_d_path = subdir + os.sep + strcl.str_cleaner(dir,'')
                if cleanup_start == False:
                    if not case_s_pc.if_exists(u_d_path):
                        cprints.fdp_color_print(o_d_path,u_d_path)
                        rwp.change_tracker(path+os.sep+"*titlechanges.txt",dcp.bn(o_d_path),dcp.bn(u_d_path))
                        os.rename(o_d_path,u_d_path)
                if cleanup_finish == True:
                    dcp.is_empty_dir(subdir+os.sep+dir)                       
    if cleanup_start == False:
        cprints.basic_color_print(5,"d's RENAMING PROCESSED ^\n")
        dir_content_sort(gcd.get_config_data("downloads_path"))
        cprints.basic_color_print(5,"ITEMS SORTED ^")
        dir_funnel(path,False,True,True)        


def main():
    file_funnel(gcd.get_config_data("downloads_path"))
    dir_funnel(gcd.get_config_data("downloads_path"))
    cprints.basic_color_print(3,"\nSeason directories built\n")
    sb.season_builder(gcd.get_config_data("tv_path"))
    shutil.rmtree("__pycache__")

if __name__ == "__main__":
    main()


