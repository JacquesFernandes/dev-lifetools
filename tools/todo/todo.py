import os;
import sqlite3;
'''GLOBALS AND SETTINGS'''
old_print = print;
safe_commands = ["clear"];

def print(msg="test",*args):
    if len(args) == 0:
        args="";
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
    conn.commit();
    conn.close();
    return;

def get_todo_list():
    conn = sqlite3.connect("list.db");
    cursor = conn.execute("SELECT rowid,item,status FROM Todo;");
    rows = cursor.fetchall();
    display_rows(rows);
    conn.close();
    return(rows);

def display_rows(rows):
    if len(rows) == 0:
        old_print(" :: No items present...");
    else:
        old_print(" ::: LIST :::")
        for row in rows:
            c = "N";
            if row[2] == "true":
                c = "Y";
            old_print(str(row[0])+" - "+row[1]+" :: ["+c+"]");
    return;

def add_todo_item():
    get_todo_list();
    conn = sqlite3.connect("list.db");
    note = input("Enter the new note : ");
    conn.cursor().execute("INSERT INTO Todo (item,status) VALUES ('"+note+"','false');");
    conn.commit();
    conn.close();

def rem_todo_item():
    rows = get_todo_list();
    rn = int(input("Enter id of note to delete : "));
    if rn not in list(i for i in range(1,len(rows)+1)):
        #old_print("len : ",len(rows));
        old_print("Invalid input...");
        return;
    old_print(" :: NOTE :: will delete '"+rows[rn-1][1]+"' ...");
    conn = sqlite.connect("list.db");
    conn.cursor().execute("DELETE FROM Todo WHERE rowid="+str(rn));
    conn.commit();
    conn.close();

def menu():
    global safe_commands;
    old_print("\n\n :: Todo - Menu ::");
    old_print(" 'show' - Show to-do list");
    old_print(" 'add' - Add new to-do item");
    old_print(" 'remove' - remove to-do item");
    old_print(" 'exit' - Exit");
    valid_inputs = ["show","add","remove","exit"]+safe_commands;
    inp = input("\ntodo -> ");
    while inp not in valid_inputs:
        return(menu());
    return(inp);

''' MAIN '''
if __name__ == "__main__":
    os.system("clear");
    op = startup_check();
    while (op[0] == False):
        if ".db" in op[1]:
            setup_db();
        else:
            setup(op[1]);
        op = startup_check();

    while op != "exit":
        op = menu();
        os.system("clear");
        if op == "exit":
            exit();
        elif op in safe_commands:
            os.system(op);
        elif op == "show":
            get_todo_list();
        elif op == "add":
            add_todo_item();
        elif op == "remove":
            rem_todo_item();
        else:
            old_print("wuuuut");
