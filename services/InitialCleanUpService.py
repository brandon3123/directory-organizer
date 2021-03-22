import os
import glob
import time
from datetime import datetime

from enums.Constant import Constant
from utils.DirectoryUtil import DirectoryUtil
from utils.FormattingUtil import FormattingUtil


class InitialCleanupService:

    def clean_up_directory(self, path):
        os.chdir(path)
        for file in glob.glob("*"):
            if DirectoryUtil.is_file(file):
                extension = DirectoryUtil.get_file_extension(file)
                creation_date = DirectoryUtil.file_creation_time(file)
                formatted_date = FormattingUtil.year_month_day_from_ct_time(creation_date)

                if not DirectoryUtil.does_directory_exist_in_path(path, extension.value):
                    DirectoryUtil.create_directory_at_path(path, extension.value)

                extension_directory = path + Constant.FORWARD_SLASH.value + extension.value

                if not DirectoryUtil.does_directory_exist_in_path(extension_directory, formatted_date):
                    DirectoryUtil.create_directory_at_path(extension_directory, formatted_date)

                extension_with_time_stamp_directory = extension_directory + Constant.FORWARD_SLASH.value + formatted_date

                DirectoryUtil.move_file_to_directory(extension_with_time_stamp_directory, file)

