import sys

from watchdog.observers import Observer
from handlers.DirectoryEventHandler import DirectoryEventHandler
from services.InitialCleanUpService import InitialCleanupService

cleanup_service = InitialCleanupService()

if __name__ == "__main__":

    arguments = sys.argv

    if len(arguments) == 2:

        directory_to_watch = arguments[1]

        print(directory_to_watch)
        cleanup_service.clean_up_directory(directory_to_watch)
    else:
        print("Please supply the full directory path of which to be organized. Only 1 directory can be specified.")
        sys.exit(0)
