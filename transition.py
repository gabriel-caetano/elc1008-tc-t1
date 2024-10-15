class transition:
    #(1,0)=(2,$,R)
    __curr_state: str
    __curr_symbol: str
    __next_state: str
    __write_symbol: str
    __move_head: str

    def __init__(self, transition_string):
        self.__curr_state = transition_string[1]
        self.__curr_symbol = transition_string[3]
        self.__next_state = transition_string[7]
        self.__write_symbol = transition_string[9]
        self.__move_head = transition_string[11]

    def get_curr_state(self):
        return self.__curr_state

    def get_curr_symbol(self):
        return self.__curr_symbol
    
    def get_write_symbol(self):
        return self.__write_symbol
    
    def get_next_state(self):
        return self.__next_state
    
    def get_move_head(self):
        if self.__move_head == 'R':
            return 1
        
        if self.__move_head == 'L':
            return -1
        
        return 0
    
    def print(self):
        print(f"{self.__curr_state}, {self.__curr_symbol} -> {self.__next_state}, {self.__write_symbol}, {self.__move_head}")