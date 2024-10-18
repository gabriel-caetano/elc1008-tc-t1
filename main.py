from turing_machine import turing_machine 
from reversible_turing_machine import reversible_turing_machine 

def main():
    tm = turing_machine('entrada-quintupla.txt')
    rtm = reversible_turing_machine(tm)
    # print(rtm)
    # print(tm.execute())
    # print('##### end of tm #####')
    rtm.execute()


if __name__ == "__main__":
    main()