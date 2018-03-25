import os
import glob


print('hi')
 

def scandirs(path):
    for currentFile in glob.glob( os.path.join(path, '*') ):
        if os.path.isdir(currentFile):
            print 'got a directory: ' + currentFile
            scandirs(currentFile)
        print "processing file: " + currentFile
scandirs('/Users/lilycaplan/school/spring2018/colag/childes/Manchester')
