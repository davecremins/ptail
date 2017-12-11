#!/usr/local/bin/python

import sys
import time

DEFAULT_CHARACTER_LINE_SIZE = 75
DEFAULT_LINE_COUNT = 10
MAX_SIZE = DEFAULT_CHARACTER_LINE_SIZE*DEFAULT_LINE_COUNT
INTERVAL = .5

def execute_and_sleep(secs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                func(*args, **kwargs)
                time.sleep(secs) 
        return wrapper
    return decorator

def attach(data):
    sys.stdout.write(data)

@execute_and_sleep(INTERVAL)
def tail(file_handle):
    last_file_position = 0
    last_seek_position = 0
    while True:
        file_handle.seek(0, 2)
        last_seek_position = file_handle.tell()
        if(last_file_position < last_seek_position):
            diff = last_seek_position - last_file_position
            if(diff > MAX_SIZE): 
                last_file_position = last_seek_position - MAX_SIZE
            file_handle.seek(last_file_position, 0)
            data = file_handle.read()
            last_file_position = file_handle.tell()
            attach(data)


def connect_to_file(file_name):
    try:
        with open(file_name, 'r') as file:
            tail(file)
    except FileNotFoundError:
        exit(f'{file_name} could not be found! Exiting...')
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    file_name = sys.argv[1]
    connect_to_file(file_name)