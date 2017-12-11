#!/usr/local/bin/python

import sys
import argparse

default_character_line_size = 75
default_line_count = 10

def get_read_position(file_size):
    return file_size - (default_character_line_size*default_line_count)

def show(lines):
    formatted = ''.join(lines)
    print(formatted)

def tail(file_handle):
    file_handle.seek(0, 2)
    file_position = file_handle.tell()
    read_position = get_read_position(file_position)
    file_handle.seek(read_position, 0)
    lines = file_handle.readlines()
    lines = lines[-10:]
    show(lines)

def connect_to_file(file_name):
    with open(file_name, 'r') as file:
        tail(file)

if __name__ == '__main__':
    file_name = sys.argv[1]
    connect_to_file(file_name)