class tape:
    __tape = []
    __size = 0
    def __init__(self, string: str):
        self.__size = len(string)
        self.__tape = [x for x in string]

    def read_symbol(self, index):
        return self.__tape[index]
    
    def get_size(self):
        return self.__size
    
    def write_symbol(self, index, symbol):
        self.__tape[index] = symbol

    def getString(self):
        return ''.join(self.__tape)
    
    def __str__(self):
        return f"{self.__tape}"