class head:
    __position = None

    def __init__(self):
        self.__position = 0

    def get_position(self):
        return self.__position
    
    def ser_position(self, new_position):
        self.__position = new_position