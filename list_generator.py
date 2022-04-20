#!/usr/bin/env python3
#-------------------------------------------------------------------------------
import os
import custom_prints
import read_n_write_manipulations as rwm
from pytimedinput import timedInput
#-------------------------------------------------------------------------------

  
def list_generator_input_getter(in_txt:str,in_list:list,print_row_len:int) -> int:
    '''
    takes in input regarding a given list and prints the updated list or just
    prints the list
    '''
    s_input = ''
    if in_txt == 'e':
        o_input = input("\nEnter the old element to be replaced or q to quite:")
        if o_input == 'q':
            return in_list
        if o_input in in_list:
            n_input = input("Enter the new element to be replaced:")
            while s_input != 'y' or s_input != 'n':
                s_input = input("Enter 'y' to save changes, 'n' to disregard:")
                if s_input == 'y':
                    print("changes saved\n")
                    print("UPDATED CAPS LIST\n")
                    in_list.append(n_input)
                    in_list.remove(o_input)
                    custom_prints.list_printer(in_list,print_row_len)
                    rwm.list_to_file(in_list,'CapsListData.txt')
                    return in_list
                elif s_input == 'n':
                    print("changes not saved")
                    return in_list
        else:
            custom_prints.color_print("item to be replaced not in list, please try agian",1)
            return -1
    return in_list
        
        
#-------------------------------------------------------------------------------


def list_generator(filename:str) -> None:
    '''print caps list and also allows updating of capslist'''
    print('\n'+filename.split('/')[-1].replace('.txt','')+' CURRENT LIST\n')
    in_list = rwm.file_to_list(filename)
    print_row_len=6
    custom_prints.list_printer(in_list,print_row_len)
    print("\nNot satisfied with a given element in the list?")
    custom_prints.basic_color_print(5,"Note: to delete an item enter blank in terms of replacement value")
    in_txt, time_result = timedInput("Then enter -> {e : edit} ->:", timeout=5)
    if(time_result):
         custom_prints.basic_color_print(1,"\nInput timed out.\n")
    else:
        while True:
            result = list_generator_input_getter(in_txt,in_list,print_row_len)
            if result != -1:
                return result
    return


#-------------------------------------------------------------------------------


def data_file_funnel(path,topdown=True):
    for subdir, dirs, files in os.walk(path,topdown):
        for file in files:
            if not file.startswith('.'):
                list_generator(subdir+os.sep+file)
                print('---------------------------------------------------------------')


#-------------------------------------------------------------------------------


def list_generator_driver():
    data_file_funnel('./DataFiles')
    
    
#-------------------------------------------------------------------------------