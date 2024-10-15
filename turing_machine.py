from array import array
from head import head
from tape import tape
from transition import transition

class turing_machine:
    __file_name: str = ''
    #
    __num_states: int
    __num_input_symbols: int
    __num_tape_symbols: int
    __num_transitions: int
    #
    __states: str
    __accept_state: str
    __curr_state: str
    #
    __input_alphabet: str
    __output_alphabet: str
    #
    __transitions: array
    __tape_input: tape
    __head: head

    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.__head = head()
        self.load_file()
        

    def set_num_states(self, val):
        self.__num_states = val
        
    def get_num_states(self):
        return self.__num_states

    def set_num_input_symbols(self, val):
        self.__num_input_symbols = val
        
    def get_num_input_symbols(self):
        return self.__num_input_symbols

    def set_num_tape_symbols(self, val):
        self.__num_tape_symbols = val
        
    def get_num_tape_symbols(self):
        return self.__num_tape_symbols

    def set_num_transitions(self, val):
        self.__num_transitions = val
        
    def get_num_transitions(self):
        return self.__num_transitions
    #

    def set_states(self, val):
        self.__states = val
    
    def get_states(self):
        return self.__states

    def set_accept_state(self, val):
        self.__accept_state = val
        
    def get_accept_state(self):
        return self.__accept_state

    def set_curr_state(self, val):
        self.__curr_state = val
        
    def get_curr_state(self):
        return self.__curr_state
    #

    def set_input_alphabet(self, val):
        self.__input_alphabet = val
    
    def get_input_alphabet(self):
        return self.__input_alphabet

    def set_output_alphabet(self, val):
        self.__output_alphabet = val
        
    def get_output_alphabet(self):
        return self.__output_alphabet
    #

    def set_transitions(self, val):
        self.__transitions = val
    
    def get_transitions(self):
        return self.__transitions

    def set_tape_input(self, val):
        self.__tape_input = val
        
    def get_tape_input(self):
        return self.__tape_input

    def set_head(self, val):
        self.__head = val
        
    def get_head(self):
        return self.__head

    def __load_file_header(self, file):
        first_line = file.readline().strip().split()
        self.__num_states = int(first_line[0])
        self.__num_input_symbols = int(first_line[1])
        self.__num_tape_symbols = int(first_line[2]) 
        self.__num_transitions = int(first_line[3])
        self.__states = file.readline().strip().split()
        self.__curr_state = self.__states[0]
        self.__accept_state = self.__states[-1]
        self.__input_alphabet = file.readline().strip().split()
        self.__output_alphabet = file.readline().strip().split()

    def __load_file_transitions(self, file):
        transitions = []
        for _ in range(self.__num_transitions):
            line = file.readline().strip()
            transitions.append(transition(line))
        self.__transitions = transitions

    def __load_input(self, file):
        self.__tape_input = tape(file.readline().strip())
        pass

    def load_file(self):
        print("opening... " + self.__file_name)
        with open(self.__file_name, 'r') as file:
            self.__load_file_header(file)
            self.__load_file_transitions(file)
            self.__load_input(file)

    def execute(self):
        while True:
            curr_state = self.__curr_state
            head_position = self.__head.get_position()
            if (curr_state == self.__accept_state):
                break
            if (head_position >= self.__tape_input.get_size()):
                return "acabou a fita"
            curr_symbol = self.__tape_input.read_symbol(head_position)
            print(f"estado atual: {curr_state}, simbolo atual: {curr_symbol}, posição atual: {head_position}")
            curr_transition = list(filter(
                lambda trans:
                    trans.get_curr_state() == curr_state and
                    trans.get_curr_symbol() == curr_symbol,
                self.__transitions
            ))[0]
            print(f"transição atual:")
            curr_transition.print()
            if not curr_transition:
                return "estado não existe"
            self.__tape_input.write_symbol(head_position, curr_transition.get_write_symbol())
            self.__head.move(curr_transition.get_move_head())
            self.__curr_state = curr_transition.get_next_state()
            self.__tape_input.print()

    
        return "aceito"

    def print(self):
        print(f"num states: {self.__num_states}")
        print(f"num input symbol: {self.__num_input_symbols}")
        print(f"num tape symbols: {self.__num_tape_symbols}")
        print(f"num transitions: {self.__num_transitions}")
        print(f"states: {self.__states}")
        print(f"input alphabet: {self.__input_alphabet}")
        print(f"tape alphabet: {self.__output_alphabet}")
        print("transitions: ")
        for i in range(len(self.__transitions)):
            self.__transitions[i].print()
        self.__tape_input.print()