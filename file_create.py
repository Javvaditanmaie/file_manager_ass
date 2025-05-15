import os
# cwd = os.listdir()
# print(cwd)
 
def create(filename,content = "hi this is a newfile"):
    try:
        with open(filename, 'x') as file:
            file.write(content)
        print(f"File '{filename}' created.")
 
    except Exception:
        print("already exists")
 
def delete(filename):
    try:
        os.remove(filename)
    except Exception:
        print("doesnt exist")
 
 
def read(filename):
    try:
        with open(filename,'r') as file:
            content = file.read()
    except Exception:
        print("doesnt exist")
 
stat = input(" you want to perform : (touch/ls) : ").split()
if stat[0] == 'touch':
    if len(stat) == 2:
        create(stat[1].strip('"'))
    elif len(stat) >= 3:
        content = ' '.join(stat[2:]).strip('"')
        create(stat[1].strip('"'),content)
 
#if stat[0] == 'ls':
    #cwd = os.listdir()
    #print(cwd)

def format_entry(name):
    return name + '/' if os.path.isdir(name) else name

def pretty_ls():
    entries = os.listdir()

    formatted = list(map(format_entry, entries))
    formatted.sort()
    for i in formatted:
        print(i.ljust(20), end='') 
    print()
pretty_ls()
 