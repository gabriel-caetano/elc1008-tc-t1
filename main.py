import sys
from turing_machine import turing_machine 
from reversible_turing_machine import reversible_turing_machine 

def main():
    # define o arquivo padrao
    arquivo_padrao = 'entrada-quintupla.txt'
    # verifica se um arquivo foi passado como argumento
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    else:
        arquivo = arquivo_padrao
    # tenta criar uma maquina de turing a partir do arquivo lido
    try:
        tm = turing_machine(arquivo)
    except Exception as e:
        print(f"Erro ao ler o arquivo '{arquivo}': {e}. Usando arquivo padrão '{arquivo_padrao}'.")
        tm = turing_machine(arquivo_padrao)
    
    # executa maquina de turing
    tm.execute()
    # reinicia maquina de turing
    while(input('Iniciar maquina de turing reversivel? digite \'s\' ') != 's'):
        pass
    
    tm.restart()
    # transforma a maquina de turing em uma turing machine reversivel
    rtm = reversible_turing_machine(tm)
    # executa maquina de turing reversivel
    rtm.execute()


if __name__ == '__main__':
    main()
