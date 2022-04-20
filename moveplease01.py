#!/usr/bin/env python3

#librabry imports
import shutil #shell util to move files
import os     #os operations

def main():
    os.chdir('/home/student/mycode/') #temp move into this DIR
    shutil.move('raynor.obj', 'ceph_storage/')  #moves that file into that DIR is file is there...

    xname = input('What is the new name for kerrigan.obj? ') #collect new name as input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) 

main()
