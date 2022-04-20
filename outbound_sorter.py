#!/usr/bin/env python3
import os
import gcd
import shutil
import rw_plus as rwp
import dir_crt_plus as dcp
import cprints
import case_s_pc as csp
import strcl


def outbound_sorter(pointer:str) -> False:
    src = ''; cwd = ''; raw_cwd = '';
    '''sorts file and dir into their respective directories'''
    mupath = gcd.get_config_data("music_path")
    mulist = rwp.file_to_list(gcd.get_config_data("music_exts_data"))
    bkpath = gcd.get_config_data("books_path")
    bklist = rwp.file_to_list(gcd.get_config_data("books_exts_data"))
    tvpath = gcd.get_config_data("tv_path")
    mopath = gcd.get_config_data("movies_path")
    vilist = rwp.file_to_list(gcd.get_config_data("video_exts_data"))
    appath = gcd.get_config_data("apps_path")
    aplist = rwp.file_to_list(gcd.get_config_data("apps_exts_data"))
    otpath = gcd.get_config_data("other_path")
    
    if os.path.isdir(pointer):
        raw_cwd = os.listdir(pointer)
        cwd = dcp.list_non_hidden_content(pointer)
        
        if len(cwd) == 1:
            src = pointer + os.sep + cwd[0]
        elif len(cwd) > 1:
            src = pointer
        elif len(cwd) == 0:
            src = pointer
    elif os.path.isfile(pointer):
        src = pointer
        
    ext_type = list(set([os.path.splitext(item)[1] for item in cwd]))
    [ext_type.remove(i) for i in ext_type if i == '']
    fpath='/'+src.split('/')[-1]
    
    if len(cwd) == 1 and len(ext_type) == 1 and ext_type[0] in mulist and csp.if_exists(mupath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_cprints.fdp_color_print(src,mupath)
        print("------------------\n")
        shutil.move(src,mupath)
        return
    elif len(cwd) == 0 and os.path.splitext(pointer)[1] in mulist and csp.if_exists(mupath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,mupath)
        print("------------------\n")
        shutil.move(src,mupath)
        return
    elif ext_type[0] in mulist and len(cwd) > 1 and csp.if_exists(mupath+fpath) == False:
        print("{d} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,mupath)
        print("------------------\n")
        shutil.move(src,mupath)
        return
    
    if len(cwd) == 1 and len(ext_type) == 1 and ext_type[0] in bklist and csp.if_exists(bkpath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,bkpath)
        print("------------------\n")
        shutil.move(src,bkpath)
        return
    elif len(cwd) == 0 and os.path.splitext(pointer)[1] in bklist and csp.if_exists(bkpath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,bkpath)
        print("------------------\n")
        shutil.move(src,bkpath)
        return
    elif len(cwd) > 1 and ext_type[0] in bklist and csp.if_exists(bkpath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,bkpath)
        print("------------------\n")
        shutil.move(src,bkpath)
        return
        
    if len(cwd) == 1 and len(ext_type) == 1 and ext_type[0] in aplist and csp.if_exists(appath+fpath) == False:
        print("{f} FROM --> TO")
        cprints.fdp_color_print(src,appath)
        print("------------------\n")
        shutil.move(src,appath)
        return
    elif len(cwd) == 0 and os.path.splitext(pointer)[1] in aplist and csp.if_exists(appath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,appath)
        print("------------------\n")
        shutil.move(src,appath)
        return
    elif len(cwd) > 1 and ext_type[0] in  aplist and csp.if_exists(appath+fpath) == False:
        print("{d} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,appath)
        print("------------------\n")
        shutil.move(src,appath)
        return
        
    if len(cwd) == 1 and len(ext_type) == 1 and ext_type[0] in vilist and strcl.type_tester(os.path.basename(cwd[0]),'tv') and csp.if_exists(tvpath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,tvpath)
        print("------------------\n")
        shutil.move(src,tvpath)
        return
    elif len(cwd) == 0 and os.path.splitext(pointer)[1] in vilist and strcl.type_tester(os.path.basename(pointer),'tv') and csp.if_exists(tvpath+fpath) == False:
        print("{f} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,tvpath)
        print("------------------\n")
        shutil.move(src,tvpath)
        return
    if len(raw_cwd) > 1 and strcl.type_tester(os.path.basename(pointer),'tv_season') or strcl.type_tester(os.path.basename(pointer),'tv') and csp.if_exists(tvpath+fpath) == False:
        print("{d} FROM --> TO")
        print("------------------")
        cprints.fdp_color_print(src,tvpath)
        print("------------------\n")
        shutil.move(src,tvpath)
        return

   
    if len(cwd) == 0 and os.path.splitext(pointer)[1] in vilist and strcl.type_tester(os.path.basename(os.path.splitext(pointer)[0]),'mm') and csp.if_exists(mopath+fpath.split('.')[0]) == False:
        if csp.if_exists(src.split('.')[0]) == False:
            os.mkdir(src.split('.')[0])
        print("{d} FROM --> TO")
        cprints.fdp_color_print(src.split('.')[0],mopath)
        shutil.move(src,src.split('.')[0])
        shutil.move(src.split('.')[0],mopath)
        print("------------------\n")
        return
    elif len(cwd) == 1 and len(ext_type) == 1 and ext_type[0] in vilist and strcl.type_tester(os.path.basename(pointer),'mm') and csp.if_exists(mopath+fpath.split('.')[0]) == False:
        print("{d} FROM --> TO")
        cprints.fdp_color_print(pointer,mopath)
        print("------------------\n")
        shutil.move(pointer,mopath)
        return
    if len(cwd) > 1 and len(ext_type) == 1 and ext_type[0] in vilist and strcl.type_tester(os.path.basename(pointer),'mm') and csp.if_exists(mopath+fpath.split('.')[0]) == False:
        print("{d} FROM --> TO")
        cprints.fdp_color_print(pointer,mopath)
        print("------------------\n")
        shutil.move(pointer,mopath)
        return
    
    if len(cwd) == 1 and  len(ext_type) == 1 and ext_type[0] in vilist and strcl.type_tester(os.path.basename(pointer),'o') and csp.if_exists(otpath+fpath) == False:
        print("{f} FROM --> TO")
        cprints.fdp_color_print(src,otpath)
        print("------------------\n")
        shutil.move(src,otpath)
        return
    elif len(cwd) == 0 and os.path.splitext(pointer)[1] in vilist and strcl.type_tester(os.path.basename(pointer),'o') and csp.if_exists(otpath+fpath) == False:
        print("{f} FROM --> TO")
        cprints.fdp_color_print(src,otpath)
        print("------------------")
        shutil.move(src,otpath)
        return
    if len(cwd) > 1 and len(ext_type) == 1 and ext_type[0] in vilist and strcl.type_tester(os.path.basename(pointer),'o') and csp.if_exists(otpath+fpath) == False:
        print("{d} FROM --> TO")
        cprints.fdp_color_print(src,otpath)
        print("------------------")
        shutil.move(src,otpath)
        return
    
    if len(cwd) == 1 and len(ext_type) == 1 and ext_type[0] == '.srt' and csp.if_exists(pointer) == True:
        shutil.rmtree(pointer)
        print("------------------")
        print("{d} .srt root deleted")
        print("------------------")
        return
    elif len(cwd) == 0 and os.path.splitext(pointer)[1] == '.srt' and csp.if_exists(pointer) == True:
        os.remove(pointer)
        print("------------------")
        print("{f} .srt file deleted")
        print("------------------")
        return
    
    #Audio book sort to be added latter   