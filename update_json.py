import json, os
from dotenv import load_dotenv

load_dotenv()
status_file = os.getenv('STATUS_FILE')

def load_all_status():
    if os.path.exists(status_file):
        with open(status_file, 'r') as file:
            return json.load(file)
    return {}

def load_status(name, date):
    status_dict = load_all_status()
    key = f"{name}{date}"
    return status_dict.get(key, 0)

def increment_status(name, date):
    status_dict = load_all_status()
    key = f"{name}{date}"
    status_dict[key] = status_dict.get(key, 0) + 1
    with open(status_file, 'w') as file:
        json.dump(status_dict, file)

def need_update_status(name, date):
    cur_cnt = load_status(name, date)
    return cur_cnt < 5

def clean_status(name, date):
    status_dict = load_all_status()
    key = f"{name}{date}"
    if key in status_dict:
        status_dict[key] = 0
        with open(status_file, 'w') as file:
            json.dump(status_dict, file)