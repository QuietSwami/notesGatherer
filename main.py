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
import datetime
import json

RULES_FILE = ".rules.json"  

def errorPrint(string):
    """
    Function that prints error messages.

    Args:
        string, a string, that contains the error message.
    """
    print("notesGatherer: ERROR - {}".format(string))

def getAllFolders(main_folder):
    """
    Returns a list with all of the possible paths from the main folder.
    
    Args:
        - main_folder: string, the path to the main folder.
    
    Returns:
        - list, a list with all the possible paths. This list has the following structure:
            (path, [folders inside the path], [files inside the path])
    """
    try:
        return list(os.walk(main_folder))
    except:
        errorPrint("{} does not exist...".format(main_folder))

def getFilesFromFolder(folder):
    """
    Only returns the files inside of the given folder path.

    Args:
        - folder, a string, that leads to a folder path.

    Returns:
        - a list, with every file inside of a given folder.
    """
    try:
        return [x for x in os.listdir(folder) if os.path.isfile(folder + "/" + x)]
    except:
        errorPrint("{} does not exist...".format(main_folder))

def createFileFromName(folder, filename, filetype):
    """
    Creates a file.

    Args:
        - folder: string, the path in which the file will be created.
        - filename: string, the filename for the new file.
        - filetype: string, the filetype for the new file. For now, it can be either .txt or .md.
    """
    if not os.path.exists(folder + "/" + filename + "." + filetype):
        with open(folder + "/" + filename + "." + filetype, "w"): pass
    else:
        errorPrint("{} already exists...".format(filename + "." + filetype))

def createFileFromRules(folder):
    """
    Created a new file from the rules of the folder.

    Args:
        - folder: string, the path in which the file will be created.
    """
    rules = readRulesFile(folder)
        
def openFile(filepath):
    """
    Opens a file on a text editor, or the default application.

    Args:
        - folder: string, the path of the file that will be open.

    TODO:
        - Test if it works on Mac and Linux, as it is the platforms where I can test.
    """
    if sys.platform == 'linux2':
        subprocess.call(["xdg-open", filepath])
    elif sys.platform == "darwin":
        subprocess.call(["open", filepath , "-e"])
    else:
        os.startfile(file)

def checkEarliestCreatedFileInFolder(folder):
    """
    Returns the earliest file in a given folder.

    Args:
        - folder: string, the path of the folder to search for the earliest file.

    Returns:
        - string, the file with the earliest creation date.

    TODO:
        - This will not work recursively. 
    """
    try:
        return reduce(lambda: a, b : a if time.ctime(os.path.getctime(a)) > time.ctime(os.path.getctime(b)) else b, getFilesFromFolder(folder))
    except:
        errorPrint("Unable to check earliest cretion time for {}".format(folder))

def checkLastModifiedFileInFolder(folder):
    """
    Returns the last modified file in a given folder.

    Args:
        - folder: string, the path of the folder to search for the earliest file.

    Returns:
        - string, the file with the earliest modification date.

    TODO:
        - This will not work recursively. 
    """
    try:
        return reduce(lambda: a, b : a if time.ctime(os.path.getmtime(a)) > time.ctime(os.path.getmtime(b)) else b, getFilesFromFolder(folder))
    except:
        errorPrint("Unable to check last modified file for {}".format(folder))

def openMostRecente(folder):
    """
    Opens the most recente file on a folder.

    Args:
        - folder: string, the path where the most recent file will be open.
    """
    openFile(checkEarliestCreatedFileInFolder(folder))

def searchByFolder(keyword, folder):
    """
    Searches a every file in a folder for a given keyword.

    Args:
        - keyword: string, the text segment to be searched
        - folder:  string, the path of the folder to be searched.
    """
    pass

def searchByKeyword(keyword):
    """
    Searches a every file for a given keyword.

    Args:
        - keyword: string, the text segment to be searched
    """
    pass

def searchByDate(keyword, date):
    """
    Searches a every file for a given keyword, if the file is created since a given date, or in a given date.

    Args:
        - keyword: string, the text segment to be searched
    """
    pass

def createRulesFile(folder, *args):
    """
    Creates the a rules file for the given folder.

    Args:
        - folder: string, a path for the folder which we are creating the rule file.
        - *args: strings, all the rules that will constitute the rules file.
            *args has the following structure:
            1. - filename type
            2. - folder type
            3. - keywords
    """
    try:
        if not os.path.isfile(folder + RULES_FILE):
            dic = {"filename": args[0], "type": args[1], "creationDate": datetime.datetime.today(), "keywords": args[2]}
            with open(folder + RULES_FILE, 'w') as json_file: json.dump(dic, json_file)
        else:
            errorPrint("Folder already initiated...")            
    except:
        errorPrint("Unable to create rule file for: {}".format(folder))

def readRulesFile(folder):
    """
    Reads and returns the rules for a folder.

    Args:
        - folder, string, the path of the folder where the rules file will be read from.
    
    Returns:
        - a rule json? object?

    TODO:
        - Make sure that the file exists befor opening
    """
    try:
        if os.path.isfile(folder + RULES_FILE):
            return json.load(open(folder + RULES_FILE), "r")
        else:
            errorPrint("Rule files does not exist in {}. Please init the folder.".format(folder))
    except:
        errorPrint("Unable to read rule file from {}".format(folder))

def transformToPDF(filepath):
    """
    Transforms any note file to a PDF.

    Args:
        - filepath, string, filepath for the file to be converted.
    """
    pass


if __name__ == "__main__":
    base_folder = "TestFolder"
    print(sys.platform)
    print(getAllFolders(base_folder))
    print(getFilesFromFolder(base_folder+"/1"))