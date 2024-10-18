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
        if (index >= self.__size):
            self.__tape = self.__tape + ['' for _ in range(index - self.__size + 1)]
            self.__size = index
        self.__tape[index] = symbol

    def getString(self):
        return ''.join(self.__tape)
    
    def __str__(self):
        return f"{self.__tape}"