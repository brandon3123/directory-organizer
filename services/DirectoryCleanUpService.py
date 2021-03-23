import os
import glob

from enums.Constant import Constant
from utils.DirectoryUtil import DirectoryUtil
from utils.FormattingUtil import FormattingUtil


class DirectoryCleanupService:

    def clean_up_directory(self, path):
        os.chdir(path)
        organized_count = 0
        # Loop through the elements inside the directory
        for file in glob.glob("*"):
            # Only perform an organization on individual files.
            if DirectoryUtil.is_file(file):
                print("Organizing file " + file)

                # Get the file extension.
                extension = DirectoryUtil.get_file_extension(file)

                # Get the files creation date.
                creation_date = DirectoryUtil.file_creation_time(file)

                # Format the files creation date as YYYY-MM-DD.
                formatted_creation_date = FormattingUtil.year_month_day_from_ct_time(creation_date)

                # Create a folder for the type of file we are working with.
                if not DirectoryUtil.does_directory_exist_in_path(path, extension.value):
                    DirectoryUtil.create_directory_at_path(path, extension.value)
                    print("Created " + extension.value + " directory")

                extension_directory = path + Constant.FORWARD_SLASH.value + extension.value

                extension_with_time_stamp_directory = extension_directory + Constant.FORWARD_SLASH.value + formatted_creation_date

                # Create a folder inside the root type folder, with the time-stamp the file was created at.
                if not DirectoryUtil.does_directory_exist_in_path(extension_directory, formatted_creation_date):
                    DirectoryUtil.create_directory_at_path(extension_directory, formatted_creation_date)
                    print("Created " + extension_with_time_stamp_directory + " directory")

                # Move the file to the directory
                DirectoryUtil.move_file_to_directory(extension_with_time_stamp_directory, file)

                organized_count += 1

        print("Organized " + str(organized_count) + " files.")

