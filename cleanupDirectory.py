import sys

from services.DirectoryCleanUpService import DirectoryCleanupService

cleanup_service = DirectoryCleanupService()

if __name__ == "__main__":

    arguments = sys.argv

    if len(arguments) == 2:
        directory = arguments[1]
        cleanup_service.clean_up_directory(directory)
    else:
        print("Please supply the full directory path of which to be organized. Only 1 directory can be specified.")
        sys.exit(0)
