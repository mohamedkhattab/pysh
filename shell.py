#!/usr/bin/python3

import sys
import os
import subprocess as sub

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Global Variables
colors = Colors()
logname = os.getenv("LOGNAME")
nodename = os.uname().nodename
prompt = colors.WARNING + logname + "@" + nodename + "% " + '\x1b[0m'

path = os.getenv("PATH").split(":")

def search_path(cmd):
    global path
    result = ""
    for p in path:
        abs_path = p + "/" + cmd
        if os.path.isfile(abs_path):
            result = abs_path
            break
    return result

def cd(path):
    try:
        os.chdir(path)
    except:
        print("pysh: cd: no such file or directory")

def pwd():
    sys.stdout.write(os.getcwd() + "\n")

def prepare_cmd(arg):
    cmd = []

    if " " in arg:
        cmd = arg.split(" ")
    elif arg == '':
        cmd = []
    else:
        cmd = [arg]

    return cmd

def prepare_pipes(arg):
    result = []
    if "|" in arg:
        cmds = arg.split("|")
        for cmd in cmds:
            result.append()
    else:
        result = [ prepare_cmd(arg) ]

    return result

def run_cmd(cmd):
    try:
        # subprocess.Popen(["grep", "-n", "^ba", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sub.call(cmd)
    except:
        print("pysh: '{}' command not found".format(cmd[0]))

while True:
    sys.stdout.write(prompt)
    cmd = prepare_cmd( input() )
    if len(cmd) > 0:
        if cmd[0] == "exit" or cmd[0] == "e":
            sys.exit(0)
        elif cmd[0] == "cd":
            cd(cmd[1])
            continue
        elif cmd[0] == "pwd":
            pwd()
            continue
        run_cmd(cmd)
    else:
        continue

