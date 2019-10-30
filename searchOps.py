from logging import *
import os


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
