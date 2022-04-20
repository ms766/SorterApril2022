import os
import shutil
import cprints     
#------------------------------------------------------------------------------- 


def bn(basename:str) -> str:
    '''returns basename of file or dir'''
    return os.path.basename(basename)


#------------------------------------------------------------------------------- 


def is_empty_dir(dir_path:str) -> None:
    '''takes dir_path, return bool regarding if empty'''
    hidden_files = ['.','~$',"Icon\r"]
    cwd = [i.lower() for i in os.listdir(dir_path) if not i.startswith(tuple(hidden_files))]
    if len(cwd) == 1 and 'sub' in cwd:
           cwd.remove('sub')
    elif len(cwd) == 1 and 'subs' in cwd:
           cwd.remove('subs')
    if len(cwd) == 0:
            shutil.rmtree(dir_path)

    
#-------------------------------------------------------------------------------


def list_all_content(dir_path) -> None:
    '''prints all content of a given dir'''
    cprints.basic_color_print(3,"NON HIDDEN")
    hidden_files = ['.','~$',"Icon\r"]
    cwd = [i for i in os.listdir(dir_path) if not i.startswith(tuple(hidden_files))]
    print(cwd)
    cprints.basic_color_print(1,"HIDDEN")
    cwd = [i for i in os.listdir(dir_path) if i.startswith(tuple(hidden_files))]
    print(cwd)
    

#-------------------------------------------------------------------------------


def list_files_mistakenly_hidden(dir_path:str) -> list:
    '''prints files that are mistakenly renames, eg file.avi -> .avi'''
    skipped_files = ['.DS_Store','~$',"Icon\r",".localized",".hushlogin"]
    cwd = [i for i in os.listdir(dir_path) if not i.startswith(tuple(skipped_files))]
    cwd = [i for i in cwd if i.startswith('.')]
    if len(cwd) == 0:
        cprints.basic_color_print(3,"No Hidden Files Present")
        print(cwd)
        return cwd
    else:
        cprints.basic_color_print(1,"Mistakenly Hidden Files Below")
        print(cwd)
        return cwd
        

#-------------------------------------------------------------------------------
    
    
def list_non_hidden_content(dir_path:str,option:str='') -> list:
    """options => default : ls [dirs & files], d : ls dirs, f : ls files"""
    hidden_files = ['.','~$',"Icon\r"]
    cwd   = [i for i in os.listdir(dir_path) if not i.startswith(tuple(hidden_files))]
    dirs  = [ i for i in cwd if os.path.isdir(dir_path+os.sep+i)]
    files = [ i for i in cwd if not os.path.isdir(dir_path+os.sep+i)]
    
    if option == '':
        #cprints.basic_color_print(5,"All non hidden content, dir ls + f ls")
        #print(dirs+files)
        return dirs+files
    elif option == 'd':
        #cprints.basic_color_print(5,"DIRS_LS")
        #print(dirs)
        return dirs
    elif option == 'f':
        #cprints.basic_color_print(5,"FILES_LS")
        #print(files)
        return files
    

#-------------------------------------------------------------------------------    


def interactive_del_empty_dirs_only(dir_path:str) -> None:
    '''check if dir is empty before asking for deletion confirmation'''
    if is_empty_dir(dir_path):
        list_all_content(dir_path)
        print("\n--------------------------------------")
        in_put = input("Enter 'y' to del cwd or 'n' to cancel:")
        while in_put != 'y' or in_put != 'n':
            if in_put == 'y':
                shutil.rmtree(dir_path)
                return
            elif in_put == 'n':
                return 
            in_put = input("Enter 'y' to del cwd or 'n' to cancel:")
    else:
        cprints.basic_color_print(5,"Warning: Dir Not Empty")


#------------------------------------------------------------------------------- 

