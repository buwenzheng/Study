import os

def dirlist():
    l = [x for x in os.listdir('.')]
    for dirname in l:
        print('-----', dirname)
dirlist()    