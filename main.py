from turing_machine import turing_machine 

def main():
    tm = turing_machine('test.txt')
    tm.load_file()
    tm.print()


if __name__ == "__main__":
    main()