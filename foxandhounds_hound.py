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



        



          
    
          



