from head import head

class turing_machine:
    __position = 0
    __file_name = ''
    __head = None

    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.__head = head()
        print(self.__head.get_position())
        

    def load_file(self):
        print("opening... " + self.__file_name)
        with open(self.__file_name, 'r') as file:
            print(file.readline())
            # todo: save relevant info on class attributes

    def print(self):
        print("turing machine print")