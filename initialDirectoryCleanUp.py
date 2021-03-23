import sys

from services.InitialCleanUpService import InitialCleanupService

cleanup_service = InitialCleanupService()

if __name__ == "__main__":

    arguments = sys.argv

    if len(arguments) == 2:
        directory_to_cleanup = arguments[1]
        cleanup_service.clean_up_directory(directory_to_cleanup)
    else:
        print("Please supply the full directory path of which to be organized. Only 1 directory can be specified.")
        sys.exit(0)
