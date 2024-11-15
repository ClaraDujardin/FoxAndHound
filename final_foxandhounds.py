class GameBoard:
    def __init__(self, n):
        if n % 4 != 0:
           n = ( n// 4 + 1) * 4 #on arrondi au multiple de 4 au dessus

        self.n = n
        self.matrice = [[0 for _ in range(n)] for _ in range(n)] 


        for i in range(1, n, 2):
            self.matrice[0][i] = (i // 2) + 1 # HOUNDS

        self.matrice[n - 1][n // 2] = - 1 # FOX


    def board_display(self):
        for row in self.matrice:
            for i in row:
                if i == 0:
                    print(".", end=" ")
                elif i == -1:
                    print("F", end=" ")
                else:
                    print(i, end= " ")
            print()




    def getter(self, row, column):
        return self.matrice[row][column]
    
    def setter(self, row, column, newValue):
        self.matrice[row][column] = newValue





class Hound:
    def __init__(self, row, column, number):
        self.row = row
        self.column = column
        self.number = number
        
          
    def canMoveTo(self ,new_row ,new_column, board):
        # Pour vérifier si la destination est hors des limites du plateau
        if new_row < 0 or new_row >= board.n or new_column < 0 or new_column >= board.n:
            return False 
        # tester si la case est vide ou si c'est un fox
        if board.getter(new_row, new_column) != 0:
            return False
            
        # Pour vérifie les diagonales (seulement vers le bas)
        if new_row - self.row == 1 and abs(new_column - self.column) == 1:    
            return True
            
        return False 
       
             
       
    def Move(self, board):
        while True:
            try:
                new_row = int(input("Entrez la ligne de destination : "))
                new_column = int(input("Entrez la colonne de destination : "))                    
                if self.canMoveTo(new_row, new_column, board):
                # Utilise le setteur pour modifier la valeur de la case initiale du chien, la supprime.
                    board.setter (self.row, self.column, 0)
                    # Ici, il l'a met à jour
                    self.row = new_row
                    self.column = new_column
                    # Et finalement il place le chien dans la bonne posiion
                    board.setter(new_row, new_column, self.number)
                    print(f"Le chien a été déplacé vers la position ({new_row}, {new_column}).")
                    break
                else:
                    print("Déplacement invalide. Veuillez réessayer.")
            except ValueError:
                print("Veuillez entrer des coordonnées valides.")




class Fox(Hound): # Classe fille

    def __init__(self, row, column):
        super().__init__(row, column, -1) 
          
    def canMoveTo(self ,new_row ,new_column , board):
        # Vérifier si la destination est hors des limites du plateau
        if new_row < 0 or new_row >= board.n or new_column < 0 or new_column >= board.n:
            return False 
        # tester si la case est vide ou si c'est un fox
        if board.getter(new_row, new_column) != 0:
            return False          
        # pour vérifier les diagonales + si ya un pion ou pas (peu importe si c'est vers le haut ou vers le bas)
        if abs(new_row - self.row) == 1 and abs(new_column - self.column) == 1:
            return True          
        return False 
    
    def win(self):
        # Permet de vérifier si fox a gagné (si il est sur la première ligne du plateau)
        return self.row == 0     
       
    def Move(self, board):
        while True:
            try:
                new_row = int(input("Entrez la ligne de destination : "))
                new_column = int(input("Entrez la colonne de destination : ")) 
                                   
                if self.canMoveTo(new_row, new_column, board):
                # Utilise le setteur pour modifier la valeur de la case initiale du renard, la supprime.
                    board.setter(self.row, self.column, 0)
                    # Ici, il l'a met à jour
                    self.row = new_row
                    self.column = new_column
                    # Et finalement il place le renard dans la bonne posiion
                    board.setter(new_row, new_column, -1)
                    print(f"Le renard a été déplacé vers la position ({new_row}, {new_column}).")
                    break
                else:
                    print("Déplacement invalide. Veuillez réessayer.")
            except ValueError:
                print("Veuillez entrer des coordonnées valides.")


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





# Test du jeu :::
jeu = FoxandHounds(4)
jeu.display_board()

jeu.play()






        