class GameState:
    def __init__(self):
        self.__score = 0
        self.__lives = 3

    @property
    def get_score(self):
        return self.__score

    @property
    def get_lives(self):
        return self.__lives

    def add_score(self, points):
        self.__score += points

    def lose_lives(self):
        self.__lives -= 1

        if self.__lives < 0:
            self.__lives = 0

    def add_live(self):
        self.__lives += 1