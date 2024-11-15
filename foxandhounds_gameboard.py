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



