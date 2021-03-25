import sys

from enums.Constant import Constant
from services.DirectoryCleanupService import DirectoryCleanupService
from utils.DirectoryUtil import DirectoryUtil

cleanup_service = DirectoryCleanupService()

def menu(path):
    return "" \
           "Which action would you like to perform on the directory: '" + str(path) + "'\n"\
           "1. Scan for unhandled extensions.\n" \
           "2. Cleanup directory\n" \
           "3. Number of files in directory\n" \
           "0. Exit\n"

def output(message):
    print("\n************************************************************")
    print(message)
    print("************************************************************\n")

if __name__ == "__main__":

    arguments = sys.argv

    if len(arguments) == 2:
        directory = arguments[1]

        if not directory[-1] == Constant.FORWARD_SLASH.value:
            directory = directory + Constant.FORWARD_SLASH.value

        action = None

        while "0" != action:
            action = input(menu(directory))
            if "1" == action:
                files = DirectoryUtil.files_in_directory(directory)
                unknown_extensions = DirectoryUtil.get_unknown_extensions_for_files(files)
                if len(unknown_extensions) > 0:
                    output("The unknown extensions are: " + str(unknown_extensions))
                else:
                    output("No unknown extensions found.")
            elif "2" == action:
                organized_count = cleanup_service.clean_up_directory(directory)
                output("Organized " + organized_count + " files.")
            elif action == "3":
                files = DirectoryUtil.files_in_directory(directory)
                output("Number of files: " + str(len(files)))

        output("Program Terminated...")
    else:
        output("Please supply the full directory path of which to be organized. Only 1 directory can be specified.")
        sys.exit(0)
