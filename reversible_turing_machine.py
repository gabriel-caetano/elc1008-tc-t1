from array import array
from head import head
from tape import tape
from transition import transition

class reversible_turing_machine:
    __num_states: int
    __num_input_symbols: int
    __num_tape_symbols: int
    __num_transitions: int
    #
    __states: array
    __accept_state: str
    __curr_state: str
    #
    __input_alphabet: str
    __output_alphabet: str
    #
    __transitions: array
    __input_tape: tape
    __output_tape: tape
    __history_tape: tape
    __head: head

    def __init__(self, tm) -> None:
        self.__num_states = tm.get_num_states()
        self.__num_input_symbols = tm.get_num_input_symbols()
        self.__num_tape_symbols = tm.get_num_tape_symbols()
        self.__num_transitions = tm.get_num_transitions()
        self.__states = tm.get_states().copy()
        self.__accept_state = tm.get_accept_state()
        self.__curr_state = self.__states[0]
        self.__input_alphabet = tm.get_input_alphabet().copy()
        self.__output_alphabet = tm.get_output_alphabet().copy()
        self.__transitions = self.__convert_quintuples_to_quadruples(tm.get_transitions())
        input_string = tm.get_input_tape().getString()
        empty_string = ['_' for _ in range(len(input_string))]
        self.__input_tape = tape(input_string)
        self.__output_tape = tape(empty_string)
        self.__history_tape = tape(empty_string)
        self.__head = head()

    def __convert_quintuples_to_quadruples(self, quintuples):
        quadruples = []
        for t in quintuples:
            # Criando o estado temporário único
            temp_state = f"T{t.get_curr_state()}_{t.get_curr_symbol()}"
            self.__states.append(temp_state)
            self.__num_states += 1
            self.__num_transitions += 1
            # Criando as duas quádruplas a partir da quíntupla
            # Leitura e escrita
            move_head = 'R' if t.get_move_head() == 1 else ('L' if t.get_move_head() == -1 else '_')
            quad_1_str = f"({t.get_curr_state()},{t.get_curr_symbol()})=({temp_state},{t.get_write_symbol()},_)"
            quad_1 = transition(quad_1_str)  
            # Movimentação da cabeça
            quad_2_str = f"({temp_state},/)=({t.get_next_state()},/,{move_head})"
            quad_2 = transition(quad_2_str)

            quadruples.append(quad_1)
            quadruples.append(quad_2)

        return quadruples

    def execute(self):
        while True:
            # comment here for continuous execution
            input("Enter for next step...")

            curr_state = self.__curr_state
            head_position = self.__head.get_position()
            if (curr_state == self.__accept_state):
                break
            if (head_position >= self.__input_tape.get_size()):
                return "acabou a fita"
            curr_symbol = self.__input_tape.read_symbol(head_position)
            print(f"estado atual: {curr_state}, simbolo atual: {curr_symbol}, posição atual: {head_position}")
            
            # find transition
            res = list(filter(
                lambda t:
                    t.get_curr_state() == curr_state and
                    (t.get_curr_symbol() == curr_symbol or
                    t.get_curr_symbol() == '/'),
                self.__transitions
            ))
            if len(res) == 0:
                return "estado não existe"
            curr_transition = res[0]
            print(f"transição atual: {curr_transition}")
            # curr_transition.print()
            # write tape
            if curr_transition.get_write_symbol() != '/':
                self.__input_tape.write_symbol(head_position, curr_transition.get_write_symbol())
            
            # move head
            self.__head.move(curr_transition.get_move_head())
            # change state
            self.__curr_state = curr_transition.get_next_state()
            # current tape status
            print(self.__input_tape)

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
        for t in self.__transitions:
            t.print()
        self.__input_tape.print()

    def __str__(self):
        res = f"""num states: {self.__num_states}
num input symbol: {self.__num_input_symbols}
num tape symbols: {self.__num_tape_symbols}
num transitions: {self.__num_transitions}
states: {self.__states}
input alphabet: {self.__input_alphabet}
tape alphabet: {self.__output_alphabet}
transitions: [
"""
        for t in self.__transitions:
            res = res + f"  {t.__str__()},\n"

        res = res + f"""]
input tape: {self.__input_tape}"""
        return res