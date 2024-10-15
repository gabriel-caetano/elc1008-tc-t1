def parse_input_file(filename):
    # Inicializa a estrutura para armazenar as informações da Máquina de Turing
    MT = {}

    with open(filename, 'r') as file:
        # Lê a primeira linha com parâmetros
        first_line = file.readline().strip().split()
        MT['num_states'] = int(first_line[0])
        MT['num_input_symbols'] = int(first_line[1])
        MT['num_tape_symbols'] = int(first_line[2])
        MT['num_transitions'] = int(first_line[3])

        # Lê os estados
        MT['states'] = file.readline().strip().split()

        # Lê o alfabeto de entrada
        MT['input_alphabet'] = file.readline().strip().split()

        # Lê o alfabeto da fita
        MT['tape_alphabet'] = file.readline().strip().split()

        # Lê as transições
        transitions = []
        for _ in range(MT['num_transitions']):
            line = file.readline().strip()
            transitions.append(line)
        MT['transitions'] = transitions

        # Lê a fita de entrada
        MT['tape_input'] = file.readline().strip()

    return MT

def print_MT(MT):
    # Função para imprimir as informações da Máquina de Turing
    print(f"Numero de estados: {MT['num_states']}")
    print(f"Numero de simbolos no alfabeto de entrada: {MT['num_input_symbols']}")
    print(f"Numero de simbolos no alfabeto da fita: {MT['num_tape_symbols']}")
    print(f"Numero de transicoes: {MT['num_transitions']}")
    print(f"Estados: {MT['states']}")
    print(f"Alfabeto de entrada: {MT['input_alphabet']}")
    print(f"Alfabeto da fita: {MT['tape_alphabet']}")
    print(f"Transicoes (Quintuplas):")
    for t in MT['transitions']:
        print(f"  {t}")
    print(f"Fita de entrada: {MT['tape_input']}")

def convert_quintuples_to_quadruples(MT):
    # Função para transformar quíntuplas em quádruplas
    quadruples = []
    for transition in MT['transitions']:
        # Exemplo de transição: (1,0)=(2,$,R)
        left, right = transition.split('=')
        state_from, read_symbol = left.strip()[1:-1].split(',')
        state_to, write_symbol, direction = right.strip()[1:-1].split(',')

        # Criando o estado temporário único
        temp_state = f"T{state_from}_{read_symbol}"

        # Criando as duas quádruplas a partir da quíntupla
        quad_1 = (state_from, read_symbol, temp_state, write_symbol)  # Leitura e escrita
        quad_2 = (temp_state, '/',state_to ,direction)  # Movimentação da cabeça

        quadruples.append((quad_1, quad_2))

    return quadruples

def print_quadruples(quadruples):
    # Função para imprimir as quádruplas geradas em formato mais formal
    print("Transicoes convertidas para quádruplas:")
    for q1, q2 in quadruples:

        # Quádrupla 1 (Leitura e escrita): (estado_atual, simbolo_lido) -> (estado_temp, simbolo_escrito)
        print(f"  ({q1[0]},{q1[1]})=({q1[2]},{q1[3]})")
        # Quádrupla 2 (Movimento): (estado_temp, / ) -> (novo_estado, direcao)
        print(f"  ({q2[0]},{q2[1]})=({q2[2]},{q2[3]})\n")


filename = 'entrada-quintupla.txt'

# Lê o arquivo e salva as informações em memória
MT = parse_input_file(filename)

# Imprime as informações da Máquina de Turing
print_MT(MT)

# Converte as quíntuplas em quádruplas
quadruples = convert_quintuples_to_quadruples(MT)

# Imprime as quádruplas geradas
print_quadruples(quadruples)

# CRIAR E FAZER LÓGICA DE LEITURA E ESCRITA NAS 3 FITAS: INPUT, HISTORY, OUTPUT