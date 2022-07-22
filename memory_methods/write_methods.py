import json
from schemas import State
from settings.settings import GetNameFile


class JsonMethods:
    def __init__(self):
        self.file_name = GetNameFile().get_name()
        self.state = 'state'

    def write_init(self, json_object):
        json_object[self.state] = State().setUp
        with open(self.file_name, 'w') as file:
            json.dump(json_object, file)

    def write_active(self, json_object):
        with open(self.file_name) as detector_file:
            init_fields = json.load(detector_file)
        with open(self.file_name, 'w') as detector_file:
            init_fields[self.state] = State().active
            init_fields.update(json_object)
            json.dump(init_fields, detector_file)

    def get_state(self):
        with open(self.file_name) as detector_file:
            return json.load(detector_file)[self.state]

    def setup_detector(self):
        with open(self.file_name) as detector_file:
            json_objects = json.load(detector_file)
        with open(self.file_name, 'w') as detector_file:
            json_objects[self.state] = State().setUp
            json.dump(json_objects, detector_file)

    def reset_detector(self):
        with open(self.file_name, 'w') as detector_file:
            json_object = {self.state: State().new}
            json.dump(json_object, detector_file)


class MakeFile:
    def __init__(self):
        self.state = State().new
        self.filename = GetNameFile().get_name()

    def make_json_file(self):
        state = self.state
        filename = self.filename
        json_object = {
            'state': state
        }
        with open(filename, 'w') as json_file:
            json.dump(json_object, json_file)
