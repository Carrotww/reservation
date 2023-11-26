import json, os

status_file = 'sms_status.json'

def load_status(name, date):
    cnt = 0
    return cnt

def save_status(name, date, status):
    pass

def need_update_status(name, date):
    cur_cnt = load_status(name, date)
    if cur_cnt > 2:
        clean_status(name, date)
    else:
        save_status(name, date, cur_cnt + 1)

def clean_status(name, date):
    pass