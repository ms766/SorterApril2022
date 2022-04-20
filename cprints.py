import os
import dir_crt_plus as dcp
#-------------------------------------------------------------------------------


def basic_color_print(color_key:int,in_str:str) -> None:
    '''
    color_keys 
    1:red, 2:yellow, 3:green, 4:cyan, 5:Magenta, 6:violet
    '''
    if color_key == 1:
        print("\u001b[31m"+str(in_str)+"\u001b[0m")
    elif color_key == 2:
        print("\u001b[33m"+str(in_str)+"\u001b[0m")
    elif color_key == 3:
        print("\u001b[32m"+str(in_str)+"\u001b[0m")
    elif color_key == 4:
        print("\033[96m"+str(in_str)+"\u001b[0m")
    elif color_key == 5:
        print("\033[35m"+str(in_str)+"\u001b[0m")
    elif color_key == 6:
        print("\u001B[34m"+str(in_str)+"\u001b[0m")


#-------------------------------------------------------------------------------


def fdp_color_print(from_path:str,to_path:str) -> None:
    '''prints color coordinated files and dirs name strs'''
    red = "\u001b[31m"; green = "\u001b[32m"; yellow = "\u001b[33m";
    cyan = "\033[96m"; reset = "\u001b[0m"
    
    if os.path.isdir(from_path):
        print(yellow+dcp.bn(from_path)+cyan+' '+dcp.bn(to_path)+reset)
    elif os.path.isfile(from_path):
        print(red+dcp.bn(from_path)+green+' '+dcp.bn(to_path)+reset)
        
        
#-------------------------------------------------------------------------------


def list_printer(in_ls:list,print_count:int) -> None:
    '''prints list on seperate lines based on a given range'''
    printable_ls = sorted(in_ls.copy())
    prev_index   = 0
    fin_index    = 0

    while len(printable_ls) % print_count != 0:
        printable_ls.append('-')
        fin_index += 1
    printable_ls.append('!!')
    
    for index, value in enumerate(printable_ls):
        if (index % print_count == 0 and index != 0):
            if index == len(printable_ls)-1:
                basic_color_print(2,printable_ls[prev_index:index-fin_index])
            else:
                basic_color_print(2,printable_ls[prev_index:index])
            prev_index = index
            
            
#-------------------------------------------------------------------------------
