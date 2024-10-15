class head:
    __position = None

    def __init__(self):
        self.__position = 0

    def get_position(self):
        return self.__position
    
    def move(self, value):
        self.__position += value