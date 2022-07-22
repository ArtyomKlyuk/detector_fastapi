import json
import os
from schemas import State
from settings import GetNameFile
from memory_methods.write_methods import MakeFile


class CheckStateInFile:
    def __init__(self):
        self.filename = GetNameFile().get_name()
        self.state = 'state'

    def check_state(self):
        filename = self.filename

        if os.path.isfile(filename):
            with open(filename) as json_file:
                json_state = json.load(json_file)[self.state]
            return json_state
        else:
            return False


class CheckFile:
    def __init__(self):
        self.check = CheckStateInFile()
        self.filename = self.check.filename

    def check_init(self):
        detector_state = self.check.check_state()
        if detector_state == State().new:
            return True
        elif detector_state == State().setUp or detector_state == State().active:
            return False
        else:
            MakeFile().make_json_file()
            return True

    def check_active(self):
        detector_state = self.check.check_state()
        if detector_state == State().setUp:
            return True
        elif detector_state == State().active or detector_state == State().new:
            return False
        else:
            MakeFile().make_json_file()
            return False

    def check_setup(self):
        state_result = CheckStateInFile().check_state()
        if state_result == State().active:
            return True
        elif not state_result:
            return True
        else:
            return False

    def check_reset(self):
        state_result = CheckStateInFile().check_state()
        if state_result == State().setUp:
            return state_result
        else:
            return False

    def check_get_state(self):
        state_result = CheckStateInFile().check_state()
        if not state_result:
            MakeFile().make_json_file()
        else:
            return state_result


class GetInitCheck:
    def get_init(self):
        return CheckFile().check_init()


class GetActiveCheck:
    def get_active(self):
        return CheckFile().check_active()


class GetSetUpCheck:
    def get_setup(self):
        return CheckFile().check_setup()


class GetResetCheck:
    def get_reset(self):
        return CheckFile().check_reset()


class GetStateCheck:
    def get_state(self):
        return CheckFile().check_get_state()
