class tape:
    __tape = []
    __size = 0
    def __init__(self, string: str):
        self.__size = len(string)
        for c in string:
            self.__tape.append(c)

    def read_symbol(self, index):
        return self.__tape[index]
    
    def get_size(self):
        return self.__size
    
    def write_symbol(self, index, symbol):
        self.__tape[index] = symbol

    def print(self):
        print(self.__tape)