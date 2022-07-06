import json
from settings import GetNameFile


class Writting:
    def __init__(self):
        self.file_name = GetNameFile().get_name()
        self.state = ['NEW', "SetUp", "ACTIVE"]

    def write_json_init(self, json_object):
        json_object.update(state=self.state[1])
        with open(self.file_name, 'w') as file:
            json.dump(json_object, file)

    def write_json_active(self, json_object):
        with open(self.file_name, 'w') as detector_file:
            init_fields = json.load(detector_file)
            init_fields['state'] = self.state[2]
            init_fields.update(json_object)
            json.dump(init_fields, detector_file)

    def get_state(self):
        state = 'state'
        with open(self.file_name) as detector_file:
            return json.load(detector_file)[state]

    def setup_detector(self):
        state = 'state'
        with open(self.file_name, 'w') as detector_file:
            json_objects = json.load(detector_file)[state] = self.state[1]
            json.dump(json_objects, detector_file)

    def reset_detector(self):
        state = {'state': self.state[0]}
        with open(self.file_name, 'w') as detector_file:
            json.dump(state, detector_file)
