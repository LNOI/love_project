import os
import json
from src.const.global_map import CONFIG_MAP
from src.const import config_map as CONST_MAP

def load_all_config(CONFIG_SET: str, CONFIG_MAP: dict) -> None:
    for config_name in ["app","resource", "logging"]:
        with open(f"config/common/{config_name}.json") as config_file:
            CONFIG_MAP[config_name] =  json.load(config_file)
            
    for config_file_name in os.listdir(f"config/{CONFIG_SET}"):
        config_name = os.path.splitext(config_file_name)[0]
        if config_name == "const":
            load_const_map(f"config/{CONFIG_SET}/const.json")
        else:
            load_specific_config(
                f'config/{CONFIG_SET}/{config_file_name}', CONFIG_MAP[config_name]
            )
            

def load_const_map(config_file_path: str) -> None:
    with open(config_file_path) as config_file:
        detail_config = json.load(config_file)
    for key in detail_config:
        setattr(CONFIG_MAP, key, detail_config[key])
        

def load_specific_config(config_file_path : str, config_map: dict):
    with open(config_file_path) as config_file:
        detail_config= json.load(config_file)
    for key in detail_config:
        config_map[key] = detail_config[key]