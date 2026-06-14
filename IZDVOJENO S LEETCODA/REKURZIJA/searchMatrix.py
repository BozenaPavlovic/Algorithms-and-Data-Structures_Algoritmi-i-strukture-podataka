# ==============================================================================
# ZADATAK: 240. Search a 2D Matrix II (Divide & Conquer / Eliminacija)
#
# TEKST ZADATKA:
# Napisite funkciju searchMatrix(matrix, target) koja pretrazuje vrijednost
# 'target' u dvodimenzionalnoj matrici cijelih brojeva. Matrica ima sljedeca 
# svojstva:
# 1. Cijeli brojevi u svakom retku su sortirani uzlazno slijeva nadesno.
# 2. Cijeli brojevi u svakom stupcu su sortirani uzlazno odozgo prema dolje.
#
# PRIMJER:
# matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22]
# ]
# target = 5 -> Vraca: True
# target = 20 -> Vraca: False
# ==============================================================================

def searchMatrix(matrix, target):
    # Ako je matrica prazna, odmah vracamo False
    if not matrix or not matrix[0]:
        return False

    # KLJUCNI TRIK ZA ISPIT: Pocinjemo iz gornjeg desnog kuta matrice!
    # Iz ove pozicije imamo jedinstveno svojstvo: 
    # Svi elementi lijevo su MANJI, a svi elementi dolje su VECI.
    row = 0
    col = len(matrix[0]) - 1

    # Petlja radi dok god smo unutar granica matrice
    while row < len(matrix) and col >= 0:
        # 1. SLUCAJ: Pronasli smo trazeni broj
        if matrix[row][col] == target:
            return True
            
        # 2. SLUCAJ: Trenutni broj je VECI od targeta.
        # Buduci da su svi brojevi u tom stupcu prema dolje jos veci (jer je stupac sortiran),
        # sigurni smo da se target ne nalazi u ovom stupcu. Eliminiramo cijeli stupac (idemo lijevo).
        elif matrix[row][col] > target:
            col -= 1  
            
        # 3. SLUCAJ: Trenutni broj je MANJI od targeta.
        # Buduci da su svi brojevi u tom retku ulijevo jos manji (jer je redak sortiran),
        # sigurni smo da se target ne nalazi u ovom retku. Eliminiramo cijeli redak (idemo dolje).
        else:
            row += 1  

    # Ako smo izasli iz granica matrice, a nismo pronasli broj, on ne postoji
    return False
