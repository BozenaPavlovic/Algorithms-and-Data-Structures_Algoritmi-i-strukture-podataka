# ==============================================================================
# ZADATAK 5: Rekurzivna funkcija 'elementi'
#
# TEKST ZADATKA:
# Napišite rekurzivnu funkciju elementi koja ispisuje sve elemente liste, 
# zajedno s onima koji se nalaze i u podlistama. Kao i u 4. zadatku, 
# na raspolaganju imate funkciju isinstance.
# ==============================================================================

def elementi(lista):
    for x in lista:
        if isinstance(x, list):
            # Ako je x podlista, rekurzivno ispiši njezine elemente
            elementi(x)
        else:
            # Ako je običan element, samo ga ispiši
            print(x)
