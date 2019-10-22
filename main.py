#!/usr/bin/env python3

# NotesGatherer
#
#
# Author: Francisco Mendonca
# License: MIT
#
#
#

import os
import sys

def getAllFolders(main_folder):
    return list(os.walk(main_folder))

def getFilesFromFolder(folder):
    return [x for x in os.listdir(folder) if os.path.isfile(folder + "/" + x)]

def createFileFromName(folder, filename, filetype):
    if  not os.path.exists(folder + "/" + filename + "." + filetype):
        with open(folder + "/" + filename + "." + filetype, "w"): pass

def createFileFromRules(folder):
    pass

def openFile(filepath):
    if sys.platform == 'linux2':
        subprocess.call(["xdg-open", filepath])
    elif sys.platform == "darwin":
        subprocess.call(["open", filepath , "-e"])
    else:
        os.startfile(file)

def checkEarliestFileInFolder(folder):
    return reduce(lambda: a, b : a if time.ctime(os.path.getctime(a)) > time.ctime(os.path.getctime(b)) else b, getFilesFromFolder(folder))

def searchByFolder(keyword, folder):
    pass
def searchByKeyword(keyword):
    pass
def searchByDate(keyword):
    pass

def createRulesFile(folder, *args):
    pass

def readRulesFile(folder):
    pass

def transformToPDF(filepath):
    pass


if __name__ == "__main__":
    base_folder = "TestFolder"
    print(sys.platform)
    print(getAllFolders(base_folder))
    print(getFilesFromFolder(base_folder+"/1"))