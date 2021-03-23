import time

import os
import shutil

from enums.Extension import Extension
from enums.Constant import Constant


class DirectoryUtil:

    @staticmethod
    def create_directory_at_path(path, directory_name):
        os.mkdir(path + Constant.FORWARD_SLASH.value + directory_name)

    @staticmethod
    def move_file_to_directory(directory, file):
        shutil.move(file, directory)

    @staticmethod
    def get_file_extension(event):
        extension = DirectoryUtil.__parse_file_extension(event)
        return DirectoryUtil.__extension_enum_from_value(extension)

    @staticmethod
    def files_in_directory(path):
        files = os.listdir(path)
        return list(filter(lambda name: DirectoryUtil.is_file(path + name), files))

    @staticmethod
    def is_file(path):
        return os.path.isfile(path)

    @staticmethod
    def is_directory(path):
        return os.path.isdir(path)

    @staticmethod
    def file_creation_time(file):
        return time.ctime(os.path.getctime(file))

    @staticmethod
    def get_file_path(event):
        return event.rsplit(Constant.FORWARD_SLASH.value, 1)[0]

    @staticmethod
    def get_file_name(event):
        file_name = os.path.basename(event).rsplit(Constant.DOT.value)[0]
        return file_name

    @staticmethod
    def does_directory_exist_in_path(working_directory, directory_name):
        return os.path.exists(working_directory + Constant.FORWARD_SLASH.value + directory_name)

    @staticmethod
    def get_unknown_extensions_for_files(files):
        unknown_extensions = list()

        for file in files:
            extension = DirectoryUtil.__parse_file_extension(file)
            extension_enum = DirectoryUtil.__extension_enum_from_value(extension)
            if extension_enum == Extension.UNKNOWN:
                unknown_extensions.append(extension)

        return list(filter(lambda ext: len(ext) > 0, unknown_extensions))

    @staticmethod
    def __parse_file_extension(file):
        return os.path.splitext(file)[1][1::]

    @staticmethod
    def __extension_enum_from_value(value):
        try:
            return Extension[value.upper()]
        except:
            return Extension.UNKNOWN
