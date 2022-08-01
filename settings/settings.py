class GetNameOfDetectorFile:
    def __init__(self):
        self.FILE_WITH_NAME = r'/media/artyom/Data/Codes/detector_fastapi/settings/name_of_detector_file.txt'

    def get_name(self):
        with open(self.FILE_WITH_NAME, 'r') as file:
            name = file.readline()
        return name


class FileName:
    def get_file_name(self, gm: GetNameOfDetectorFile):
        return gm.get_name()


class GetNameFile:
    def get_name(self):
        return FileName().get_file_name(GetNameOfDetectorFile())
