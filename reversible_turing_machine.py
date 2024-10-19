from array import array
from head import head
from tape import tape
from transition import transition
from enum import Enum

EXECUTION_MODE = Enum('EXECUTION_MODE', ['STRAIGHT', 'STEP_BY_STEP'])

class reversible_turing_machine:
    __exec_mode: Enum
    #
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
    __input_head: head
    __output_tape: tape
    __history_tape: tape
    __history_head: head

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
        self.__input_head = head()
        self.__history_head = head()
        self.__exec_mode = EXECUTION_MODE.STRAIGHT
        print('carregou maquina de turing reversivel')
        print(self)


    def __convert_quintuples_to_quadruples(self, quintuples):
        quadruples = []
        for t in quintuples:
            # Criando o estado temporário único
            temp_state = f'T{t.get_curr_state()}_{t.get_curr_symbol()}'
            self.__states.append(temp_state)
            self.__num_states += 1
            self.__num_transitions += 1
            # Criando as duas quádruplas a partir da quíntupla
            # Leitura e escrita
            move_head = 'R' if t.get_move_head() == 1 else ('L' if t.get_move_head() == -1 else '_')
            quad_1_str = f'({t.get_curr_state()},{t.get_curr_symbol()})=({temp_state},{t.get_write_symbol()},_)'
            quad_1 = transition(quad_1_str)  
            # Movimentação da cabeça
            quad_2_str = f'({temp_state},/)=({t.get_next_state()},/,{move_head})'
            quad_2 = transition(quad_2_str)

            quadruples.append(quad_1)
            quadruples.append(quad_2)

        return quadruples

    def execute_stage_1(self):
        print('Iniciando estagio 1')
        # select execution mode
        selected_mode = input('Deseja executar passo a passo? [s/n]')
        if (selected_mode == 's'):
            self.__exec_mode = EXECUTION_MODE.STEP_BY_STEP
        else:
            self.__exec_mode = EXECUTION_MODE.STRAIGHT
        res = ''
        while True:
            curr_state = self.__curr_state
            head_position = self.__input_head.get_position()
            if (curr_state == self.__accept_state):
                res = 'aceito'
                break
            if (head_position >= self.__input_tape.get_size()):
                res = 'acabou a fita'
                break
            curr_symbol = self.__input_tape.read_symbol(head_position)
            # print(f'estado atual: {curr_state}, simbolo atual: {curr_symbol}, posição atual: {head_position}')
            
            # find transition
            res = list(filter(
                lambda t:
                    t.get_curr_state() == curr_state and
                    (t.get_curr_symbol() == curr_symbol or
                    t.get_curr_symbol() == '/'),
                self.__transitions
            ))
            if len(res) == 0:
                print('Estado não existe')
                break
            curr_transition = res[0]
            
            if (self.__exec_mode == EXECUTION_MODE.STEP_BY_STEP):
                input('Enter para o proximo passo...')
                print(f'Estado atual: {curr_state}, simbolo atual: {curr_symbol}, posicao atual: {head_position}')
                print('Transição atual:')
                print(curr_transition)
                print('Estado atual da fita:')
                print(self.__input_tape)

            # write tape
            if curr_transition.get_write_symbol() != '/':
                self.__input_tape.write_symbol(head_position, curr_transition.get_write_symbol())
                self.__history_tape.write_symbol(self.__history_head.get_position(), curr_transition.get_next_state())
                self.__history_head.move(1)
            
            # move head
            self.__input_head.move(curr_transition.get_move_head())
            # change state
            self.__curr_state = curr_transition.get_next_state()
            # current tape status
        
        print('Finalizou estagio 1')
        print('Fita de entrada: ', self.__input_tape)
        print('Fita de historico', self.__history_tape)
        print('Fita de saida', self.__output_tape)


    # copy the result to the output tape
    def execute_stage_2(self):
        print('Iniciando estagio 2')
        # select execution mode
        selected_mode = input('Deseja executar passo a passo? [s/n]')
        if (selected_mode == 's'):
            self.__exec_mode = EXECUTION_MODE.STEP_BY_STEP
        else:
            self.__exec_mode = EXECUTION_MODE.STRAIGHT
        for i in range(self.__input_tape.get_size()):
            read_symbol = self.__input_tape.read_symbol(i)
            if (self.__exec_mode == EXECUTION_MODE.STEP_BY_STEP):
                input('Enter para o proximo passo...')
                print('Copiando para fita de saida:')
                print(f'Posicao: {i}, simbolo: {read_symbol}')
            self.__output_tape.write_symbol(i, read_symbol)
        
        print('Finalizou estagio 2')
        print('Fita de entrada: ', self.__input_tape)
        print('Fita de historico', self.__history_tape)
        print('Fita de saida', self.__output_tape)

    def execute_stage_3(self):
        print('Iniciando estagio 3')
        # select execution mode
        selected_mode = input('Deseja executar passo a passo? [s/n]')
        if (selected_mode == 's'):
            self.__exec_mode = EXECUTION_MODE.STEP_BY_STEP
        else:
            self.__exec_mode = EXECUTION_MODE.STRAIGHT
        while (self.__history_head.get_position() > 0):
            self.__history_tape.write_symbol(self.__history_head.get_position(), '')
            self.__history_head.move(-1)
            curr_state = self.__history_tape.read_symbol(self.__history_head.get_position())
            res = list(filter(
                lambda t:
                    t.get_curr_state() == curr_state,
                self.__transitions
            ))
            curr_transition = res[0]

            move_head = curr_transition.get_move_head() * -1
            write_symbol = curr_transition.get_curr_state()[3]
            self.__input_head.move(move_head)
            self.__input_tape.write_symbol(self.__input_head.get_position(), write_symbol)
            if (self.__exec_mode == EXECUTION_MODE.STEP_BY_STEP):
                input('Enter para o proximo passo...')
                print('Revertendo execucao:')
                print(f'Estado atual: {curr_state}, simbolo atual: {write_symbol}, posicao atual: {self.__input_head.get_position()}')
                print('Fita de entrada: ', self.__input_tape)
                print('Fita de historico', self.__history_tape)
        
        self.__history_tape.write_symbol(self.__history_head.get_position(), '')
        print('Finalizou estagio 3')
        print('Fita de entrada: ', self.__input_tape)
        print('Fita de historico', self.__history_tape)
        print('Fita de saida', self.__output_tape)

    def execute(self):
        print('Iniciando maquina de turing reversivel...')
        print('Fita de entrada: ', self.__input_tape)
        print('Fita de historico', self.__history_tape)
        print('Fita de saida', self.__output_tape)
        self.execute_stage_1()
        while(input('Iniciar estagio 2? digite \'s\' ') != 's'):
            pass
        self.execute_stage_2()
        while(input('Iniciar estagio 3? digite \'s\' ') != 's'):
            pass
        self.execute_stage_3()

    def print(self):
        print(f'num states: {self.__num_states}')
        print(f'num input symbol: {self.__num_input_symbols}')
        print(f'num tape symbols: {self.__num_tape_symbols}')
        print(f'num transitions: {self.__num_transitions}')
        print(f'states: {self.__states}')
        print(f'input alphabet: {self.__input_alphabet}')
        print(f'tape alphabet: {self.__output_alphabet}')
        print('transitions: ')
        for t in self.__transitions:
            t.print()
        self.__input_tape.print()

    def __str__(self):
        res = f'''Estados: {self.__states}
Alfabeto de entrada: {self.__input_alphabet}
Alfabeto da fita: {self.__output_alphabet}
Transicoes: [
'''
        for t in self.__transitions:
            res = res + f'  {t.__str__()},\n'

        res = res + f''']
Entrada: {self.__input_tape}'''
        return res