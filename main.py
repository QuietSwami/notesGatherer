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
import argparse
import collections
from folderOps import *
from logging import *
from rules import *
from fileOps import *
from searchOps import *

RULES_FILE = ".rules.json"  
DEBUG = False

#
# Command Line
#

class ValidateDefaultProgram(argparse.Action):
    """
    Custom action to handle the default program argument.
    """
    def __call__(self, parser, args, values, option_string=None):
        validTypes = ("txt", "md")
        type, program = values
        if subject.strip(".") not in validTypes:
            errorPrint("{} is not a valid filetype...".format(types))
            return
        setattr(args, self.dest, (type, program))
        
def createCommandLineArgs():
    """
    Create the command line arguments, and parser.
    """

    parser = argparse.ArgumentParser(description='Create your personal note taking system.')

    # Creational Arguments
    parser.add_argument('--start', dest="start", metavar= "folder name", nargs=1, action='store', help='Creates base folder.')
    parser.add_argument('--init', dest="init", metavar= "base folder path", nargs=1, action='store', help='Creates a new notes folder.')
    parser.add_argument('--new', dest="new", metavar= "file name", nargs=1, action='store', help='Creates a new note.')
    parser.add_argument('--filetype', dest="filetype", metavar= "filetype", choices=["txt", "md"], help='To be used with new folder creation.')
    parser.add_argument('--type', dest="folderType", metavar="folder type", choices=[None, "diary", "note", "website"], help="")

    # Searching Arguments
    parser.add_argument('--searchFolder', dest="searchFolder", metavar= "keyword", nargs=1, action='store', help='Searches the given folder for a keyword.')
    parser.add_argument('--searchFile', dest="searchFile", metavar= "keyword", nargs=1, action='store', help='Searches all the files for a keyword.')
    parser.add_argument('--keywords', dest="keywords", metavar= "keywords", nargs="*", action='store', help='To be used with new folder creation.')
    parser.add_argument('--checkRules', dest="checkRules", metavar= "folder path", nargs=1, action='store', help='Show the folder rules.')

    # File Opening Arguments
    parser.add_argument('--open', dest="open", metavar="file name" ,action="store", nargs=1, help="Opens the file with the given filename")
    parser.add_argument('--folder', dest="folder", metavar="folder path", action="store", nargs=1, help="Folder path to specify where a file is.")

    # Folder Management Arguments
    parser.add_argument('--addDefaultProgram', dest="addDefaultProgram", metavar= ("filetype", "program"), nargs=2, action=ValidateDefaultProgram, help='Show the folder rules.')

    # System Arguments
    parser.add_argument('--debug', dest="debug", action="store_true", help="Shows the debug logs.")

    args = parser.parse_args()

    return args

def treatArgs(args):
    """
    This functions takes the arguments from the command line, and treats it.

    Args:
        - args: arguments from argparse.
    """
    if args.start:
        createFolder(args.start, {"type": args.folderType, "rules": [args.addDefaultProgram]})
    elif args.init:
        createFolder(args.init, {"type": args.folderType, "rules": [args.addDefaultProgram])
    elif args.new:
        createFile(args.new, args.filetype)
    elif args.searchFolder:
        pass
    elif args.searchFile:
        pass
    elif args.open:
        pass
    
    if args.debug:
        DEBUG = True    

    
if __name__ == "__main__":
    base_folder = "TestFolder"
    # treatArgs(createCommandLineArgs())
    a = askDefaultProgram(".")
    print(a)