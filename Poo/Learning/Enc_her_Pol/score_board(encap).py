class ScoreBoard:
    def __init__(self):
        self.__score = 0

    def set_score(self):
        while True:
            new_score = float(input("Score:"))
            if new_score < 0:
                print("Errado,ultilizar escore positiva")
            else:
                self.__score = new_score
                break

    def get_score(self):
        print(f"your score is :{self.__score}")

score01 = ScoreBoard()
score01.set_score()
score01.get_score()
        