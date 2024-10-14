class tape:
    __tape = []

    def read_symbol(self, index):
        return self.__tape[index]
    
    def write_symbol(self, index, symbol):
        self.__tape[index] = symbol