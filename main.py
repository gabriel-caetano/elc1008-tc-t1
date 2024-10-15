from turing_machine import turing_machine 

def main():
    tm = turing_machine('test.txt')
    print(tm.execute())


if __name__ == "__main__":
    main()