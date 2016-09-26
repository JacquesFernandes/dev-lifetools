#!/usr/bin/python3

import os;

'''GLOBAL VARS'''
ROOT = os.getcwd();
TOOL_DIR = ROOT+"/tools/";
safe_commands=["clear"];

'''METHODS'''
def cli():
    inp = input("dlt -> ");
    if inp == "help" or inp == "?":
        tools = os.listdir(TOOL_DIR);
        if len(tools) == 0:
            print(" :: No tools present...");
        else:
            print(" :: TOOLS ::");
            for tool in tools:
                print(" -> "+str(tool));
    elif inp in safe_commands:
        os.system(inp);
        return;
    elif inp == "exit":
        return("exit");
    elif not isTool(inp):
        print(" :: Invalid command/tool, enter \"help\" or \"?\" for help");
        return("help");
    return(inp);

def isTool(tool_name):
    try:
        os.listdir(TOOL_DIR+tool_name);
        return(True);
    except FileNotFoundError:
        return(False);

def run(prog):
    os.chdir(prog);
    os.system("python3 "+prog+".py");
    print("ROOT:"+ROOT);
    os.chdir(TOOL_DIR);

'''MAIN'''
if __name__ == "__main__":
    print(" :: Initializing! ::");
    os.chdir(TOOL_DIR);
    tools = os.listdir();
    print(" :: Initialization finised... ::");
    flag = True;
    while flag:
        ret = cli();
        if ret == "exit":
            flag = False;
        elif ret != "help" and ret != "?" and ret!= None:
            run(ret);
        elif ret == None:
            pass;
