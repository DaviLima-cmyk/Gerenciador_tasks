class Player:
    def __init__(self,name,score):
        self.__name = "Anonymous"
        self.__score = 0

    def add_score(self,valor):
        self.__score += valor


    def set_score(self,new_score):
        while True:
            if self.__score < 0:

                new_score = float(input("Score:"))
            else:
                self.__score = new_score
                break

    def get_name(self):
        print(f"player {self.__name}")

    def get_score(self):
        print(f"sua score atual é de {self.__score} pontos.")

player01 = Player("alejandro",-900)
player01.add_score(70)
player01.set_score()
player01.get_name()
player01.get_score()