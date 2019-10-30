import os
import json
from logging import *

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
