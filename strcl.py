#!/usr/bin/env python3
import re
import gcd
import rw_plus as rwp
#-------------------------------------------------------------------------------


def trim(in_str:str) -> str:
    '''cleans leading and trailing bad chars and keeps space count consistent'''
    tempstr = in_str.rstrip().lstrip().rstrip('-').rstrip().lstrip('-').lstrip()
    tempstr = re.sub(r'([\-][ ])+', ' - ',tempstr)
    tempstr = re.sub(r'[ \s]{1,}', ' ',tempstr)
    return tempstr 


#-------------------------------------------------------------------------------


def starts_w_txt_del(in_str:str,in_ls:list) -> str:
    '''dels key elements from the start of a given str'''
    templs = in_ls.copy()
    if len(templs) == 0:
        return in_str
    ustr = re.sub(r'\b^{}\b'.format(templs[-1]),'',in_str,flags=re.I)
    templs.pop()
    return starts_w_txt_del(ustr,templs)


#-------------------------------------------------------------------------------


def acronym_sub(in_str:str,in_ls:list) -> str:
    '''plus acronyms with full length words'''
    temp = ""
    for i in in_ls:
        index = i.index(':');
        gstr = i[index+1:];
        bstr = i[:index]; 
        if bstr in in_str.lower():
            ustr = trim(re.sub(r'[ \s]{1,}', ' ', in_str,flags=re.I))
            temp  += re.sub( r"{}".format(bstr),"{}".format(gstr),ustr,flags=re.I)
    ustr = temp if temp != "" else in_str;
    return ustr


#-------------------------------------------------------------------------------


def front_to_back(in_str:str,in_ls:list) -> str:
    '''shifts words from the fornt of a str to the bad of it'''
    temp = ""
    for i in in_ls:
        if in_str.lower().startswith(i):
            temp = re.sub(r'^{}[ ]*[\-]*'.format(i),'',in_str,flags=re.I)
            +" - "+"{}".format(i).rstrip().lstrip()
            temp = re.sub(r'[ \s]{1,}', ' ',temp).lstrip().rstrip()        
    u_base = temp if temp != "" else in_str;
    return u_base


#-------------------------------------------------------------------------------


def title_sub(in_str,in_ls):
    temp = ""
    for i in in_ls:
        index = i.index(':');
        good_str = i[index+1:];
        bad_str = i[:index]; 
        
        if bad_str in in_str.lower():
            u_base = trim(re.sub(r'[ \s]{1,}', ' ', in_str,flags=re.IGNORECASE))
            temp += re.sub( r"{}".format(bad_str),"{}".format(good_str), u_base,flags=re.IGNORECASE)
    u_base = temp if temp != "" else in_str;
    return u_base


#-------------------------------------------------------------------------------


def type_tester(in_str:str,is_kind_test:str) -> bool:
    '''test file titles to see what kind of files they are. Options: tv,tv_season,o,mm'''
    other_test_results = 0
    
    
    #tv eps dir test
    tv_ep_m = re.search(r'.*s[0-9]{1,2}[ ]*e[0-9]{1,2}',in_str,flags=re.I)
    if tv_ep_m != None and is_kind_test == 'tv':
        return True
    
    if tv_ep_m == None and is_kind_test == 'o':
        other_test_results += 1
    
    season_m1 = re.search(r'.*complete.season.[0-9]*|.*season[ ]*[0-9]{1,2}$|.*s[0-9]{1,2}$|^(?!s[0-9]{1,2}e[0-9]{1,2})$|all seasons', in_str, flags=re.IGNORECASE)
    
    if season_m1 != None and is_kind_test == 'tv_season':
        return True
    
    if season_m1 == None and is_kind_test == 'o':
        other_test_results += 1
    
    #movies and music test - deeper dive into dir needed
    m_m1 = re.search(r'.*\[[0-9]{4}\]$',in_str, flags=re.I)
    m_m2 = re.search(r'^(?!.*COMPLETE.*)',in_str, flags=re.I)
             
    if m_m1 != None and m_m2 != None and is_kind_test == 'mm': 
        return True
   
    if m_m1 == None and is_kind_test == 'o':
        other_test_results += 1
        
    if other_test_results == 3:
        return True 
    
    
#-------------------------------------------------------------------------------  


def name_b4_dash_seeker(in_str:str,in_ls:list) -> str:
    '''seeks final name b4 dash'''
    tagsls = [i for i in in_ls if i in in_str.lower() and i != '']
    if type_tester(in_str,'o') == True and tagsls != []:
        nstr = re.sub(r'\band\b|,', r' & ' ,in_str, flags=re.I)
        if '-' in in_str:
            nstr = re.sub(r'[\-]+',r' & ',nstr, flags=re.I)
            nstr = re.sub(r'\b({})\b(.*)'.format(tagsls[-1]),r'\1 - \2',nstr,flags=re.I)[::-1]
            nstr = nstr.replace('&','',1)[::-1]
            nstr = trim(re.sub(r'[ \s]{1,}',' ',nstr))
            return nstr
        else:
            nstr = re.sub(r'\b({})\b'.format(tagsls[-1]),r'\1 - ',nstr,flags=re.I)
            return nstr
    return in_str

    
#-------------------------------------------------------------------------------


def aka_injector(instr:str,in_ls:list) -> str:
    '''replace names with there akas'''
    nstr = trim(re.sub(r'[ \s]{1,}', ' ',instr))
    inls_copy = in_ls.copy()
    if in_ls == []:
        return instr
    org = inls_copy[-1].split(':')[0].lstrip().rstrip()
    rep = inls_copy[-1].split(':')[1].lstrip().rstrip()
    org_test = True if re.search(r'{}'.format(org),nstr,flags=re.I) != None else False
    rep_test = True if re.search(r'{}'.format(rep.replace('(','\(').replace(')','\)')),nstr,flags=re.I) != None else False
    
    if '-' in nstr and type_tester(nstr,'o') == True and org_test == True and rep_test == False:
        part_a = nstr.split('-')[0]
        part_b = nstr.split('-')[-1]
        u_temp = trim(trim(re.sub(r'\b{}\b'.format(org),' {} '.format(rep.capitalize()),part_a,flags=re.I))+' - '+part_b)
        inls_copy.pop()
        return aka_injector(u_temp,inls_copy)
    else:
        inls_copy.pop()
        return aka_injector(nstr,inls_copy)
    return instr


#-------------------------------------------------------------------------------


def day_month_year_cl(nstr:str) -> str:
    if re.search(r'\((\d){2} \- [a-z]{3,8} (\d){4}\)',nstr,flags=re.I):
        nstr = trim(re.sub(r'(?<= (\d){4}\)) .*',']', nstr,flags=re.I))
        nstr = trim(re.sub(r'\((\d){2} \- ','[', nstr,flags=re.I).replace(')]',']'))
        return nstr
    return nstr


#-------------------------------------------------------------------------------


def grammer_enforcer(in_str:str,caps_ls:list) -> str:
    new_str = ""
    f_half = []

    in_str_ls = in_str.lower().split(' ')

    if '(aka' in in_str or '-' in in_str and type_tester(in_str,'o') == True:
        f_half = [i.capitalize() for i in in_str[:in_str.find('-')].split(' ')]
        if '' in f_half: f_half.remove('')
        in_str_ls = in_str[in_str.find('-'):].split(' ')    
        
    for i in range(1,len(in_str_ls)-1):
        if len(in_str_ls[i]) < 4 and in_str_ls[i] not in caps_ls:
            in_str_ls[i] = in_str_ls[i].lower()
        if len(in_str_ls[i]) > 3 and in_str_ls[i] not in caps_ls:
            in_str_ls[i] = in_str_ls[i].capitalize()
        if in_str_ls[i] in caps_ls:
            in_str_ls[i] = in_str_ls[i].upper()
      
            
    if in_str_ls[0] not in caps_ls:
        in_str_ls[0] = in_str_ls[0].capitalize()
    else:
        in_str_ls[0] = in_str_ls[0].upper()
        
    for i, e in reversed(list(enumerate(in_str_ls))):
        if len(in_str_ls[i]) <= 3: 
            if in_str_ls[i].startswith(('s','e')) and in_str_ls[i][-1].isdigit():
                in_str_ls[i] = in_str_ls[i].upper()    
        if in_str_ls[i] not in caps_ls and in_str_ls[i].isalpha():
            in_str_ls[i] = in_str_ls[i].capitalize()
            break
        elif in_str_ls[i] in caps_ls and in_str_ls[i].isalpha():
            in_str_ls[i] = in_str_ls[i].upper()
            break
    
    if in_str_ls[-1].lower() == 'seasons' and in_str_ls[-2].lower() == 'all' and in_str_ls[-3] == '-':
        in_str_ls[-1] = (in_str_ls[-1]).capitalize()
        in_str_ls[-2] = in_str_ls[-2].capitalize()
    
    if f_half != []:
        in_str_ls = f_half + in_str_ls
    
    for i in in_str_ls:
        new_str += i+' '  
    
    new_str = trim(re.sub(r'([\-][ ])+', ' - ',new_str))
    return new_str


#-------------------------------------------------------------------------------


def str_cleaner(base:str,ext:str) -> str:
    '''cleans strings of unwanted chars , takes a file name and an ext'''
    apexts = rwp.file_to_list(gcd.get_config_data("apps_exts_data"))
    muexts = rwp.file_to_list(gcd.get_config_data("music_exts_data"))
    #***************************************************************************
    dells = rwp.file_to_list(gcd.get_config_data("del_strs_data"))
    subls = rwp.file_to_list(gcd.get_config_data("sub_strs_data"))
    yawls = rwp.file_to_list(gcd.get_config_data("shift_strs_to_back_data"))
    tagls = rwp.file_to_list(gcd.get_config_data("actor_name_strs_data"))
    akals = rwp.file_to_list(gcd.get_config_data("aka_names_strs_data"))
    capls = rwp.file_to_list(gcd.get_config_data("caps_strs_data"))
    #***************************************************************************
    nstr = trim(re.sub(r'\.',' ',base)) if ext not in apexts and ext not in muexts else base# SPECIAL CASES 4 mu & ap ext
    nstr = trim(re.sub(r'_',' ',nstr))# replace _ with space
    nstr = trim(re.sub(r"([A-Z][a-z]+)", r" \1",nstr))# seperate Cap Low e(A b)
    nstr = trim(re.sub(r"\b([0-9]+[A-Z])\b", r" \1",nstr))# seperate num Cap e(0 A)
    nstr = trim(starts_w_txt_del(nstr,dells)) #^junk str
    nstr = trim(front_to_back(nstr,yawls))
    nstr = trim(re.sub(r'[\\]+','',nstr))# \
    nstr = trim(re.sub(r'[\[]+','[',nstr))# [ x amount
    nstr = trim(re.sub(r'[\]]+',']',nstr))# ] x amount
    nstr = trim(re.sub(r'\-', ' - ',nstr))# -
    nstr = trim(re.sub(r'^\[.*\]|\[[a-zA-Z ]+\]$', '',nstr))#str start [any] or str end [letter & spaces]
    nstr = trim(re.sub(r'\b^[0-9]{2} [0-9]{2} [0-9]{2}\b',' ',nstr,flags=re.I))# date e(01 01 10)
    nstr = trim(re.sub(r' \d{4}(?= s[0-9]{1,2}e[0-9]{1,2})','',nstr,flags=re.I))# year be4 s# e# in tv ep
    nstr = trim(re.sub(r'(.*season\s*[0-9]*)(.*)',r'\1',nstr,flags=re.I)) if type_tester(base,'mm') == None else nstr#everything after (season plus number)
    nstr = trim(title_sub(nstr,subls))    
    nstr = trim(aka_injector(nstr,akals))#replace names with akas if present in ls
    nstr = trim(re.sub(r'^[0-9]{1,3}[ ]*[\.|\-][ ]*|^[0-9]{2} ','',nstr)) if ext in muexts else nstr #numbers from songs
    nstr = trim(re.sub(r'\(?[0-9]+p.*|WEBRip.*|REPACK.*|WEB.*','',nstr))#hd rating and all that follows
    #months<--------------------------------------------------------------------
    nstr = trim(re.sub(r'\b(new)*.(jan|febr)uary.[0-9]{0,2}.[0-9]{2,4}\b','',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'\b(new)*.(march|april|may).[0-9]{0,2}.[0-9]{2,4}\b','',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'\b(new)*.ju(ne|ly).[0-9]{0,2}.[0-9]{2,4}\b','',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'\b(new)*.(august).[0-9]{0,2}.[0-9]{2,4}\b','',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'\b(new)*.(septe|octo|novem|decem)ber.[0-9]{0,2}.[0-9]{2,4}\b','',nstr,flags=re.IGNORECASE))
    #months<--------------------------------------------------------------------
    nstr = trim(re.sub(r'([ ]*\-[ ]*)(jan|febr)uary([ ]*\-[ ]*)',r'\1 \2 ',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'([ ]*\-[ ]*)(march|april|may)([ ]*\-[ ]*)',r'\1 \2 ',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'([ ]*\-[ ]*)ju(ne|ly)([ ]*\-[ ]*)',r'\1 \2 ',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'([ ]*\-[ ]*)(august)([ ]*\-[ ]*)',r'\1 \2 ',nstr,flags=re.IGNORECASE))
    nstr = trim(re.sub(r'([ ]*\-[ ]*)(septe|octo|novem|decem)ber([ ]*\-[ ]*)',r'\1 \2 ',nstr,flags=re.IGNORECASE))
    #months<--------------------------------------------------------------------    
    #LIST LATTER LIST LATTER LIST LATTER LIST LATTER LIST LATTER LIST LATTER LIST LATTER 
    nstr = trim(re.sub(r" \brq\b| \bfh\b| \bmp4\b| \bsd\b",'',nstr,flags=re.I))#junks strs
    nstr = trim(re.sub(r" \(1k\)| \(atp\)|\(tna\)",'',nstr,flags=re.I))#junk Strs
    nstr = trim(re.sub(r"\. com",'.com',nstr,flags=re.I))#binds . com to .com
    nstr = trim(re.sub(r'\bcomplete$\b','', nstr) if 'season' in nstr and 'complete' in nstr else nstr)
    #LIST LATTER LIST LATTER LIST LATTER LIST LATTER LIST LATTER LIST LATTER LIST  
    nstr = trim(re.sub(r' [x]{3}[\s0-9a-z]+$','',nstr,flags=re.I))
    nstr = trim(re.sub(r'[x]{3} sd .*','',nstr,flags=re.I))
    nstr = trim(re.sub(r'\b[x]{3}\b$','',nstr,flags=re.I))
    nstr = trim(re.sub(r'\b[x]{3}\s+[0-9]{3,4}.*\b','',nstr,flags=re.I))
    nstr = trim(re.sub(r'\b([se])(\d{1,2})',r'\1\2 ',nstr,flags=re.I))
    nstr = trim(re.sub(r'\b([e])(\d{1,2}) ', r'\1\2 ENDLINE-Show' ,nstr, flags=re.I))
    nstr = trim(re.sub(r' ENDLINE-Show.*$', '', nstr))
    nstr = trim(re.sub(r'\bs0','S', nstr,flags=re.I))
    nstr = trim(re.sub(r's(?=[0-9]{1,2})','S', nstr,flags=re.I))
    nstr = trim(re.sub(r'\be0','E', nstr,flags=re.I))
    nstr = trim(re.sub(r'e(?=[0-9]{1,2})','E', nstr,flags=re.I))
    nstr = trim(re.sub(r'[\(\[][0-9]{4}[\)\]](?=.*s[0-9]+.e[0-9]+)','',nstr,flags=re.I))#<<<----------------------------?
    nstr = trim(re.sub(r'season\b','- Season',nstr,flags=re.I)) if type_tester(nstr,'tv_season') and '-' not in nstr else nstr
    nstr = trim(re.sub(r'all season[s]*$','- All Seasons',nstr,flags=re.I))    
    nstr = trim(re.sub(r'COMPLETE','',nstr,flags=re.I)) if re.search(r'\bCOMPLETE.*\-.*season\b', nstr,flags=re.I) != None else nstr
    # #?????????
    nstr = re.sub(r' -\ COMPLETE.*[0-9]{4}.*$', ' - All Seasons', nstr, flags=re.I) if re.search(r' -\ COMPLETE.*[0-9]{4}.*$',nstr,flags=re.I) != None else nstr#?  all season 
    # #?????????
    nstr = nstr.replace('(','[').replace(')',']') if re.search(r'\b[ ]+[\(][0-9]{4}[\)][ ]*\b',nstr) != None else nstr #aounnd[year] 
    #------->
    nstr = re.sub(r'(\b(\d){4}\b)$',r'[\1] ENDLINE',nstr,flags=re.I).replace('( ','(').replace(' )',')').replace('[[','[').replace(']]',']').replace('([','[')# [year] related adjust later <<<----------------------------?
    #------->
    nstr = trim(re.sub(r' ENDLINE.*$', '', nstr, flags=re.I))# del everything after [year]
    nstr = day_month_year_cl(nstr)
    nstr = trim(re.sub(r'(?<= \[(\d){4}\]) .*','', nstr,flags=re.I)) #look behind
    nstr = trim(re.sub(r'( \([0-9]{2})(.*[a-z]+.*[0-9]{4}\])', r'\2', nstr, flags=re.I)) if re.search(r' \([0-9]{2}.*[a-z]+.*[0-9]{4}\]',nstr,flags=re.I) != None else nstr#<<<----------------------------?
    nstr = trim(re.sub(r'\([0-9]{2} [0-9]{2} \[[0-9]{4}\]$|new [0-9]{2}.*\[[0-9]{4}\]$','', nstr, flags=re.I))#<<<----------------------------?
    nstr = trim(name_b4_dash_seeker(nstr,tagls)) if type_tester(base,'mm') == None else nstr #add - after last name in str
    nstr = grammer_enforcer(nstr,capls)
    return nstr 


#-------------------------------------------------------------------------------