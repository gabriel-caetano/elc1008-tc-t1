from head import head
from tape import tape

class turing_machine:
    __file_name: str = ''
    #
    __head: head = None
    __input_tape: tape = None
    __output_tape: tape = None
    __tape_limit: int = None
    __initial_position: int = None

    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.load_file()
        self.__head = head(self.__initial_position)
        self.__input_tape = tape(self.__tape_limit)
        self.__output_tape = tape(self.__tape_limit)
        self.__history_tape = tape(self.__tape_limit)
        print(self.__head.get_position())
        
    def __load_file_header(self):
        # load info from header of the file 
        pass

    def __load_file_transitions(self):
        # while transitions, read and load
        pass

    def load_file(self):
        print("opening... " + self.__file_name)
        with open(self.__file_name, 'r') as file:
            print(file.readline())
            # todo: save relevant info on class attributes
            # initial_position, tape_size, states, etc
            self.__load_file_header()
            self.__load_file_transitions()
            

    def print(self):
        print("turing machine print")