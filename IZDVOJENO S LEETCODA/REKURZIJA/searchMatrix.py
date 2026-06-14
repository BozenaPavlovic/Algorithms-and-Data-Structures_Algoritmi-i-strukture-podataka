def searchMatrix(matrix, target):
    # Pomoćna funkcija koja glumi petlju kroz rekurziju
    def trazi(row, col):
        # BAZNI SLUČAJ 1: Izašli smo iz granica matrice (element nije pronađen)
        if row >= len(matrix) or col < 0:
            return False
            
        # BAZNI SLUČAJ 2: Pronašli smo target
        if matrix[row][col] == target:
            return True
            
        # REKURZIVNI KORAK 1: Element je prevelik, eliminiraj stupac (idi lijevo)
        elif matrix[row][col] > target:
            return trazi(row, col - 1)  # Poziv same sebe!
            
        # REKURZIVNI KORAK 2: Element je premali, eliminiraj red (idi dolje)
        else:
            return trazi(row + 1, col)  # Poziv same sebe!

    if not matrix or not matrix[0]:
        return False
        
    # Pokrećemo rekurziju iz gornjeg desnog kuta (red 0, zadnji stupac)
    return trazi(0, len(matrix[0]) - 1)
