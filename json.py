
class ConfigFromJSON(object):
    def __init__(self, filename):
        self.json_file = filename

    @property
    def json_file(self):
        print('set')
        return self.__json_file

    @json_file.setter
    def json_file(self, value):
        print('check')
        if value is not 0:
            raise ValueError("No !")
        else:
            print("OK")
            self.__json_file = value

print('instance')
myA = ConfigFromJSON(0)

print('instance')
myA = ConfigFromJSON(0)



print(myA.json_file)


