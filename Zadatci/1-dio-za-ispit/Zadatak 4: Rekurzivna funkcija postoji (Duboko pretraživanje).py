# ==============================================================================
# ZADATAK 4: Rekurzivna funkcija 'postoji'
#
# TEKST ZADATKA:
# Napišite rekurzivnu funkciju postoji koja pronalazi zadani element u listi 
# koja može sadržavati druge liste i vraća True ako taj element postoji, 
# u suprotnom vraća False. Na raspolaganju imate funkciju isinstance(x, list) 
# koja vraća True ako je x lista, a u suprotnom vraća False.
#
# PRIMJER:
# >>> postoji('c', ['a', [['b', 'c'], 'd', ['e']], 'f'])
# => True
# ==============================================================================

def postoji(element, lista):
    for x in lista:
        if isinstance(x, list):
            # Ako je x podlista, rekurzivno pretraži tu podlistu
            if postoji(element, x):
                return True
        else:
            # Ako je x običan element, provjeri poklapa li se
            if x == element:
                return True
    return False
