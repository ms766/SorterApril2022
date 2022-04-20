from configparser import ConfigParser
#-------------------------------------------------------------------------------


def get_config_data(key_from_config_file:str) -> str:
    """item_type_flags are: p -> dir_path, d -> data_file of type .txt"""
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    if 'data' not in key_from_config_file:
        return config_object["DIRECTORY_PATHS"][key_from_config_file]
    else:
        return config_object["DATA_PATHS"][key_from_config_file]
    

#-------------------------------------------------------------------------------
