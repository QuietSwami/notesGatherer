import os
import datetime
import subprocess
import logging

#
# File Operations
#
def createFile(folder, filename):
    """
    This function makes sure that the right file creation function is called.

    Args:
        - folder, string, path of the folder where the file will be created.
        - filename, string, the filename of the new file, if one is needed.
        - filetype, string, filetype of the new file, if one is needed.
    """
    pass


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


#
# Other Operations
#
def askCustomName(t):
    """
    Asks the user the name for the file or folder, either for creation or search

    Args:
        - t: string, either file or folder.

    Returns:
        - string. The name of the new file or folder
    """
    log("askCustomName")

    try:
        name = input("Enter the name of the new {}: ".format(t))
        correct = input("Is {} correct? [Y/N] ")
        if correct.lower == "n":
            askCustomName(t)
        else:
            return name
    except:
        errorPrint("Unable to get a new name.")
