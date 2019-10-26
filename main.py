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
DEBUG = False
#
# Logging
#
def errorPrint(string):
    """
    Function that prints error messages.

    Args:
        string, a string, that contains the error message.
    """
    print("notesGatherer: ERROR - {}".format(string))

def log(string, **kwargs):
    """
    Function that prints log messages.

    Args:
        string, a string, that contains the log message.
    """
    if DEBUG == True or kwargs["debug"] == True:
        print("[LOG] {}".format(string))

#
# Folder Operations
#
def getAllFolders(main_folder):
    """
    Returns a list with all of the possible paths from the main folder.
    
    Args:
        - main_folder: string, the path to the main folder.
    
    Returns:
        - list, a list with all the possible paths. This list has the following structure:
            (path, [folders inside the path], [files inside the path])
    """
    log("getAllFolders")
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
    log("getFilesFromFolder")
    try:
        return [x for x in os.listdir(folder) if os.path.isfile(folder + "/" + x)]
    except:
        errorPrint("{} does not exist...".format(main_folder))

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
    log("checkEarliestCreatedFileInFolder")

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
    log("checkLastModifiedFileInFolder")

    try:
        return reduce(lambda: a, b : a if time.ctime(os.path.getmtime(a)) > time.ctime(os.path.getmtime(b)) else b, getFilesFromFolder(folder))
    except:
        errorPrint("Unable to check last modified file for {}".format(folder))

def openMostRecent(folder):
    """
    Opens the most recente file on a folder.

    Args:
        - folder: string, the path where the most recent file will be open.
    """
    log("openMostRecent")


    openFile(checkEarliestCreatedFileInFolder(folder))

def baseFolderRules(folder, **kargs):
    """
    Creates and writes the base folder rules. 
    The base folder, is the agreagator, the folder where all other folders are added.

    Args:
        - folder: string, the base folder path.
    """
    log("baseFolderRules")

    try:
        with open(folder + RULES_FILE, "w"): 
            json.dumps(kargs)
    except:
        errorPrint("Unable to create rules file for the base folder...")

#
# File Operations
#
def createFileFromName(folder, filename):
    """
    Creates a file.

    Args:
        - folder: string, the path in which the file will be created.
        - filename: string, the filename for the new file.
        - filetype: string, the filetype for the new file. For now, it can be either .txt or .md.
    """
    log("createFileFromName")

    filetype = checkFileType(readRulesFile(folder))
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
    log("createFileFromRules")

    rules = readRulesFile(folder)

    try:
        if rules["filename"] == "timestamp":
            log("Creating File with timestamp.")
            filetype = checkFileType(rules["filetype"])
            name = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S") + "." + filetype
            with (open(folder + name, "w")):pass

        elif rules["filename"] == "customName":
            log("Creating File with custom name.")
            filetype = checkFileType(rules["filetype"])
            name = askCustomName("file")
            with (open(folder + name + "." + filetype, "w")): pass

        elif rules["filename"] == "composite":
            log("Creating File with composite name")
            filetype = checkFileType(rules["filetype"])
            time = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
            name = askCustomName("file")
            with (open(folder + name + "-" + time + "." + filetype, "w")): pass
    except:
        errorPrint("Unable to create a new file, using rules.")

def checkFiletype(filetypes):
    """
    This returns the correct file type to create the file

    Args:
        - filetypes: string, contains the value of the rule set.
    
    Returns:
        - The correct filetype.
    """
    log("checkFiletype")

    if filetypes == "txt" or filetypes == "md":
        return filetypes
    else:
        file = input("Which filetype do you want: .txt or .md?")
        if file.strip(".") == "txt" or file.strip(".") == "md":
            return file
        else:
            print("{} does not compute... Try again".format(file))
            checkFileType(filetypes)

def openFile(filepath):
    """
    Opens a file on a text editor, or the default application.

    Args:
        - folder: string, the path of the file that will be open.

    TODO:
        - Test if it works on Mac and Linux, as it is the platforms where I can test.
    """
    log("openFile")


    if sys.platform == 'linux2':
        subprocess.call(["xdg-open", filepath])
    elif sys.platform == "darwin":
        subprocess.call(["open", filepath , "-e"])
    else:
        os.startfile(file)

def transformToPDF(filepath):
    """
    Transforms any note file to a PDF.

    Args:
        - filepath, string, filepath for the file to be converted.
    """
    log("transformToPDF")

    pass

# Rules
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
    log("createRulesFile")

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
    log("readRulesFile")

    try:
        if os.path.isfile(folder + RULES_FILE):
            return json.load(open(folder + RULES_FILE), "r")
        else:
            errorPrint("Rule files does not exist in {}. Please init the folder.".format(folder))
    except:
        errorPrint("Unable to read rule file from {}".format(folder))

#
# Search Operations
#
def searchByFolder(keyword, folder):
    """
    Searches a every file in a folder for a given keyword.

    Args:
        - keyword: string, the text segment to be searched
        - folder:  string, the path of the folder to be searched.
    """
    log("searchByFolder")

    pass

def searchByKeyword(keyword):
    """
    Searches a every file for a given keyword.

    Args:
        - keyword: string, the text segment to be searched
    """
    log("searchByKeyword")
  
    pass

def searchByFilename(keyword, folder):
    """
    Searches for a particular keyword in the filenames in a given folder.

    Args:
        - filename, a string, the keyword to be searched on the filename
        - folder: string, the folder where the file is going to be searched

    Returns:
        - a list, containing all the files that contain the keyword
    """
    log("searchByFilename")

    pass

def searchByDate(keyword, date):
    """
    Searches a every file for a given keyword, if the file is created since a given date, or in a given date.

    Args:
        - keyword: string, the text segment to be searched
    """
    log("searchByDate")

    pass

#
# Other Operations
#
def askCustomName(type):
    """
    Asks the user the name for the file or folder, either for creation or search

    Args:
        - type: string, either file or folder.

    Returns:
        - string. The name of the new file or folder
    """
    log("askCustomName")

    try:
        name = input("Enter the name of the new {}: ".format(type))
        correct = input("Is {} correct? [Y/N] ")
        if correct.lower == "n":
            askCustomName(type)
        else:
            return name
    except:
        errorPrint("Unable to get a new name.")


if __name__ == "__main__":
    base_folder = "TestFolder"
    print(sys.platform)
    print(getAllFolders(base_folder))
    print(getFilesFromFolder(base_folder+"/1"))