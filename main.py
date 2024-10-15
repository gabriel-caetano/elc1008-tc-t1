from turing_machine import turing_machine 

def main():
    tm = turing_machine('entrada-quintupla.txt')
    print(tm.execute())


if __name__ == "__main__":
    main()