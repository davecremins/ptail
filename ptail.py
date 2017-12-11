#!/usr/local/bin/python

import sys

def tail(file_handle):
    read_result = file_handle.read()
    print(read_result)

def connect_to_file(file_name):
    with open(file_name, 'r') as file:
        tail(file)

if __name__ == '__main__':
    file_name = sys.argv[1]
    connect_to_file(file_name)