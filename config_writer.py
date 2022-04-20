#!/usr/bin/env python3
#-------------------------------------------------------------------------------
from configparser import ConfigParser
#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["DIRECTORY_PATHS"] = {
    "apps_path":"/Users/ms/Desktop/0DownLoads/7-Apps",  
    "audiobooks_path":"/Users/ms/Desktop/0DownLoads/5-Audiobooks",
    "books_path":"/Users/ms/Desktop/0DownLoads/6-Books",
    "downloads_path":"/Users/ms/Desktop/0DownLoads/10-Completed",
    "movies_path":"/Users/ms/Desktop/0DownLoads/1-Movies",
    "music_path":"/Users/ms/Desktop/0DownLoads/4-Music",
    "other_path":"/Users/ms/Desktop/0DownLoads/9-OtherPending",
    "tv_path":"/Users/ms/Desktop/0DownLoads/2-TvShows",
}

config_object["DATA_PATHS"] = {
    #list of all good file exts
    "all_good_exts_data":"./DataFiles/Fmt-Good.txt",
    #list of all bad file exts
    "all_bad_exts_data":"./DataFiles/Fmt-Bad.txt",
    #list of all app file exts
    "apps_exts_data":"./DataFiles/Fmt-App.txt",
    #list of all book file exts
    "books_exts_data":"./DataFiles/Fmt-Book.txt",
    #list of all music file exts
    "music_exts_data":"./DataFiles/Fmt-Music.txt",
    #list of all video file exts
    "video_exts_data":"./DataFiles/Fmt-Video.txt",
    #list of all actors aka's
    "aka_names_strs_data":"./DataFiles/Str-Aka-Injector.txt",
    #list of general actor names
    "actor_name_strs_data":"./DataFiles/Str-Actors-Names-Ls.txt",
    #list of words that should be shift from the the front of a given str to the 
    # back of it
    "shift_strs_to_back_data":"./DataFiles/Str-Shifter-F2B.txt",
    #list of strings that need to be deleted
    "del_strs_data":"./DataFiles/Str-Start-Del.txt",
    #list of string strings that should be subs with other strings
    "sub_strs_data":"./DataFiles/Str-Title-Sub.txt",
    #list of words that should always be in caps
    "caps_strs_data":"./DataFiles/Str-Caps-Ls.txt"
    
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)