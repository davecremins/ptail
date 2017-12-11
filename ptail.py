#!/usr/local/bin/python

import sys
import time

default_character_line_size = 75
default_line_count = 10
file_position = None
interval = .500

def execute_and_sleep(secs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                func(*args, **kwargs)
                time.sleep(secs) 
        return wrapper
    return decorator

def get_read_position(file_position):
    return file_position - (default_character_line_size*default_line_count)

def show(lines):
    formatted = ''.join(lines)
    print(formatted)

@execute_and_sleep(interval)
def tail(file_handle):
    file_handle.seek(0, 2)
    file_position = file_handle.tell()
    read_position = get_read_position(file_position)
    file_handle.seek(read_position, 0)
    lines = file_handle.readlines()
    file_position = file_handle.tell()
    lines = lines[-10:]
    show(lines)

def connect_to_file(file_name):
    try:
        with open(file_name, 'r') as file:
            tail(file)
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    file_name = sys.argv[1]
    connect_to_file(file_name)