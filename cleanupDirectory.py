import sys

from enums.Constant import Constant
from services.DirectoryCleanUpService import DirectoryCleanupService
from utils.DirectoryUtil import DirectoryUtil

cleanup_service = DirectoryCleanupService()

def menu(path):
    return "" \
           "Which action would you like to perform on the directory: '" + str(path) + "'\n"\
           "1. Scan for unhandled extensions.\n" \
           "2. Cleanup Directory\n" \
           "0. Exit\n"

if __name__ == "__main__":

    arguments = sys.argv

    if len(arguments) == 2:
        directory = arguments[1]

        if not directory[-1] == Constant.FORWARD_SLASH.value:
            directory = directory + Constant.FORWARD_SLASH.value


        action = input(menu(directory))

        if action == "1":
            files = DirectoryUtil.files_in_directory(directory)
            unknown_extensions = DirectoryUtil.get_unknown_extensions_for_files(files)
            if len(unknown_extensions) > 0:
                print("The unknown extensions are: " + str(unknown_extensions))
            else:
                print("No unknown extensions found.")
        elif action == "2":
            cleanup_service.clean_up_directory(directory)
        else:
            print("Program Terminated...")
    else:
        print("Please supply the full directory path of which to be organized. Only 1 directory can be specified.")
        sys.exit(0)

