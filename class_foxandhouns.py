class FoxandHounds:
    def __init__(self, n):
        self.gameBoard = GameBoard(n)
        self.fox = Fox(n - 1, n // 2)
        self.hounds = [Hound(0, column, (column // 2) + 1) for column in range(1, n, 2)]
        self.player = 1


    def display_board(self):
        print("Plateau initial : ")
        self.gameBoard.board_display()


    def play(self):
        while True:
            print(f"Tour du joueur {self.player}")
            if self.player == 1:
                print("Tour du Fox")
                self.fox.Move(self.gameBoard)

                print("Plateau après le coup du joueur", self.player)
                self.gameBoard.board_display()

                if self.fox.win():
                    print("Le Fox a gagné")
                    break



            else:
                print("Tour des Hounds")

                while True:
                    try:
                        hound = int(input("Quel hound choississez vous : ".format(len(self.hounds))))
                        if 1 <= hound <= len(self.hounds):
                            break
                        else:
                            print("INVALIDE, Choississez un autre : ")
                    except ValueError:
                        print("INVALIDE, Choississez un autre : ")

                self.hounds[hound - 1].Move(self.gameBoard)

                print("Plateau après le coup du joueur", self.player)
                self.gameBoard.board_display()


            self.player = 3 - self.player




