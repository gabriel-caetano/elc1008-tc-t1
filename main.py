from turing_machine import turing_machine 
from reversible_turing_machine import reversible_turing_machine 

def main():
    # cria uma maquina de turing a partir do arquivo lido
    tm = turing_machine('entrada-quintupla.txt')
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