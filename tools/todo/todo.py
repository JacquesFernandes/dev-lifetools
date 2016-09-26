import os;
import sqlite3;

old_print = print;

def print(msg="test",*args):
    old_print("todo -> ",msg,args);
    return;

def error(msg):
    old_print(" :: ERROR :: "+str(msg));

def startup_check():
    files = os.listdir();
    if "config.txt" not in files:
        error("config.txt not found...");
        return(False,"config.txt");
    if "list.txt" not in files:
        error("list.txt not found...");
        return(False,"list.txt");
    if "list.db" not in files:
        error("list.db not found...")
        return(False,"list.db");
    return(True,"");

def setup(fname):
    old_print(" :: Creating "+fname+"...");
    f = open(fname,"w");
    f.close();
    return;

def setup_db():
    conn = sqlite3.connect("list.db");
    conn.execute("CREATE TABLE Todo (id int, item varchar(30), status boolean, PRIMARY KEY(id));");
    conn.close();
    return;

def get_todo_list():
    conn = sqlite3.connect("list.db");
    cursor = conn.execute("SELECT * FROM Todo;");
    rows = cursor.fetchall();
    if len(rows) == 0:
        old_print(" :: No items present...");
    else:
        for row in rows:
            old_print(row);
    return;


def menu():
    old_print("\n\n :: Todo - Menu ::");
    old_print(" 1 - Show to-do list");
    old_print(" 2 - Edit to-do list");
    old_print(" 0 - Exit");
    valid_inputs = ["1","2","0"];
    inp = input("\ntodo -> ");
    while inp not in valid_inputs:
        return(menu());
    return(inp);

''' MAIN '''
if __name__ == "__main__":
    op = startup_check();
    while (op[0] == False):
        if ".db" in op[1]:
            setup_db();
        else:
            setup(op[1]);
        op = startup_check();

    op = 1;
    while int(op) != 0:
        op = int(menu());
        if int(op) == 0:
            exit();
        elif op == 1:
            get_todo_list();
        else:
            old_print("wuuuut");
