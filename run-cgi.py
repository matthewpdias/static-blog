#!/usr/local/bin/python3

import subprocess
import signal
import time
import os


cwd = os.getcwd()

def add_button():
    try:
        with open("index.html", 'a') as file:
            file.write('<center><a href="cgi-bin/update.py"><button style="border-radius: 12px; color: red;"> publish </button></a></center>')
    except:
        print("no index.html file found, shutting server down")
        exit(1)

def trim_button():
    readFile = open("index.html")
    lines = readFile.readlines()
    readFile.close()
    w = open("index.html",'w')
    w.writelines([item for item in lines[:-1]])
    w.close()

def cpy_scripts():
    subprocess.call(['cp', '-r', '/Users/liatrio/Documents/Personal-Projects/static-blog/cgi-bin', 'cgi-bin'])

def remove_scripts():
    subprocess.call(['rm', '-rf', 'cgi-bin/'])

add_button()
cpy_scripts()

print("Test server booting up:")
server_proc = subprocess.Popen(['python3', '-m', 'http.server', '--cgi'])
time.sleep(.5)

def signal_handler(signal, frame):
        print('shutting down...')
        server_proc.send_signal(signal.SIGINT)

input("Press any key to stop the server")
server_proc.send_signal(signal.SIGINT)

trim_button()
#remove_scripts()

print("Server closed.. have a nice day!")
