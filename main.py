import sys

import requests

import threading

import keyboard

import os


def thread_request():
    if sys.argv[2] == 0:
        while True:
            print(sys.argv[1])
            print(requests.get(sys.argv[1]))
    else:
        for i in range(int(sys.argv[2])):
            print(sys.argv[1])
            print(requests.get(sys.argv[1]))
    os._exit(0)

def ext():
    keyboard.wait('q')
    os._exit(0)


if __name__ == '__main__':
    e = threading.Thread(target=ext)
    e.start()


    try:
        if sys.argv[3] == '-t':
            for i in range(int(sys.argv[4])):
                t = threading.Thread(target=thread_request)
                t.start()

    except:
        thread_request()
