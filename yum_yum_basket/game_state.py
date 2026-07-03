class GameState:
    def __init__(self):
        self.__score = 0
        self.__lives = 3
        self.__level = 1

    @property
    def score(self):
        return self.__score

    @property
    def lives(self):
        return self.__lives

    @property
    def level(self):
        return self.__level

    def add_score(self, points):
        self.__score += points

    def lose_lives(self):
        self.__lives -= 1

        if self.__lives < 0:
            self.__lives = 0

    def add_live(self):
        self.__lives += 1

    def level_up(self):
        self.__level += 1