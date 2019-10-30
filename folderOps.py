import os
from logging import *
import json
import rules 

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
        return reduce(lambda a, b : a if time.ctime(os.path.getctime(a)) > time.ctime(os.path.getctime(b)) else b, getFilesFromFolder(folder))
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
        return reduce(lambda a, b : a if time.ctime(os.path.getmtime(a)) > time.ctime(os.path.getmtime(b)) else b, getFilesFromFolder(folder))
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

def askFolderType():
    """
    If the user hasn't specified the type of the folder, this function asks the type, and returns it.

    Returns:
        - string, the type of the folder to be created. It can be:
            - base
            - diary
            - note
            - website
    """
    try:
        t = input("Which type of folder you want to create: Base (B), Diary (D), Note (N) or Website (W)\n")
        conversion = {"base": "b", "diary": "d", "note": "n", "website": "w"}

        if t.lower() in conversion.keys():
            return t.lower()
        elif t.lower() in conversion.values():

            # Creates a list with the keys
            # And a new one with the values.
            # Because this two lists will have the same order, when we get the index of the value, \
            # we get the index of the key.
            return list(conversion.keys())[list(conversion.values()).index(t.lower())]
        else:
            print("Not Available... Try again.")
            return askFolderType()
    except:
        errorPrint("Unable to read folder type, from user...")
        return

def askDefaultProgram(baseFolder):
    """
    Asks the default program for a particular filetype.
    Takes in consideration already used programs in other folders.

    Args:
        - baseFolder, string, the path to the base folder of the project.

    Returns:
        - a list, containing a pair of filetype and program

    TODO:
        - Get known default programs.
        - Check if the program is viable.
    """
    try:   
        filetype = input("For which filetype do you want to associate a default program: txt or md or do you want to exit(E)? \n ")
        if filetype.lower() in ["txt", "md"]:
            program = input("Which program do you want to use to open {} files? \n".format(filetype.lower()))
            return [filetype.lower(), program.lower()]
        elif filetype.lower() == "e":
            return
        else:
            quest = input("Unknown filetype. Try again (A) or Exit (E)? \n")
            if quest.lower() == "a":
                askDefaultProgram(baseFolder)
            else:
                return
    except:
        errorPrint("Unable to ask user for default program...")

def createFolder(folder, **kwargs):
    """
    Creates a folder given the folder path.
    If the rules are pass, it creates the rules folder.

    Args:
        - folder, string, the path to the new folder.
        - kwargs, dict, optional, dictionary with the new folder rules. 
    """
    log("createFolder")
    try:
        if not os.path.isdir(folder):
            log("{} folder does not exist. Creating.".format(folder))
            os.mkdir(folder)
            if kwargs:
                log("Folder Rules: {}".format(kwargs))
                if kwargs["type"] == None:
                    kwargs["type"] = askFolderType()
                if kwargs["addDefaultProgram"] == None:
                    kwargs["addDefaultProgram"] = askDefaultProgram()
                createRulesFile(folder, kwargs)
        else:
            errorPrint("Folder already exists.")
    except:
        errorPrint("Unable to create a new folder.")
