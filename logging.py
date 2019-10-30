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
