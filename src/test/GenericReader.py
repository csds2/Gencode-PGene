'''
Created on Jul 12, 2011

@author: eoc21
'''
import os, sys
'''
File read into memory
'''
class FileReader:
    def __init__(self,fname):
        self.fileName = fname
        self.lines=[]
        self.readLinesIntoMemory()
    def readLinesIntoMemory(self):
        f = open(self.fileName,'r')
        self.lines = f.readlines()

fr = FileReader(sys.argv[1])
print fr.lines