#/usr/bin/env python

# Copyright 2013 Martijn van de Rijdt

import os

SOURCE_DIRECTORY = r"C:\development\workspaces\eclipse-4.2\umvc3-replay-analyser\umvc3replayanalyser\src"

def main():
    '''
    Adds the contentx of prefix.txt to the start of all .java files in SOURCE_DIRECTORY.
    '''
    text = open('prefix.txt', 'r').read()
    
    for path, directories, files in os.walk(SOURCE_DIRECTORY):
        for filename in files:
            if filename.endswith(".java"):
                fullPath = path + os.sep + filename
                print fullPath
                
                f = open(fullPath, "r+")
                lines = f.readlines() # read old content
                f.seek(0) # go back to the beginning of the file
                f.write(text) # write new content at the beginning
                for line in lines: # write old content after new
                   f.write(line)
                f.close()

if (__name__ == "__main__"):
    main()