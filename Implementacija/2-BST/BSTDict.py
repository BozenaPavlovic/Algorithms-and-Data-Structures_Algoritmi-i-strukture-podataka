# Mapa / rječnik temeljen na BST-u

class TreeNodeDict:
    def __init__(self, key, value):
        self.key = key          # ključ po kojem BST sortira elemente
        self.value = value      # vrijednost povezana s ključem
        self.left = None        # lijevo dijete (manji ključevi)
        self.right = None       # desno dijete (veći ključevi)


class BSTDict:
    def __init__(self):
        self.root = None        # korijen stabla (početno prazno)


    def insert(self, key, value):

        new_node = TreeNodeDict(key, value) # 1. STVARANJE: novi čvor koji želimo ubaciti

        if self.root is None:               # 2. PROVJERA: Je li stablo prazno?
            self.root = new_node            # 3. POSTAVLJANJE: novi čvor postaje root
            return

        current = self.root                 # 4. KRETANJE: počinjemo od root-a

        while True:

            if key < current.key:           # 5. USPOREDBA: Ako je ključ manji → idi lijevo

                if current.left is None:    # 6. MJESTO: Ako nema lijevog djeteta
                    current.left = new_node # 7. UMETANJE: Ubaci novi čvor lijevo
                    break

                current = current.left      # 8. SPUŠTANJE: Nastavi tražiti lijevo


            elif key > current.key:         # 9. USPOREDBA: Ako je ključ veći → idi desno

                if current.right is None:   # 10. MJESTO: Ako nema desnog djeteta
                    current.right = new_node# 11. UMETANJE: Ubaci novi čvor desno
                    break

                current = current.right     # 12. SPUŠTANJE: Nastavi tražiti desno


            else:
                current.value = value       # 13. AŽURIRANJE: Ako ključ postoji, promijeni value
                break


    def search(self, key):

        current = self.root                 # 1. KRETANJE: počinjemo od root-a

        while current is not None:          # 2. PETLJA: prolazimo kroz stablo

            if current.key == key:          # 3. PRONALAZAK: Ako je ključ pronađen
                return current.value        # 4. POVRATAK: vrati povezanu vrijednost

            elif key < current.key:         # 5. USPOREDBA: Ako je ključ manji
                current = current.left      # 6. SPUŠTANJE: idi lijevo

            else:
                current = current.right     # 7. SPUŠTANJE: idi desno

        return None                         # 8. NEUSPJEH: ključ ne postoji


    def delete(self, key):

        parent = None                       # 1. PRAĆENJE: roditelj trenutnog čvora
        current = self.root                 # 2. KRETANJE: počinjemo od root-a

        # TRAŽENJE čvora za brisanje
        while current is not None and current.key != key:

            parent = current                # 3. PAMĆENJE: spremi roditelja

            if key < current.key:           # 4. USPOREDBA: Ako je ključ manji
                current = current.left      # 5. SPUŠTANJE: idi lijevo
            else:
                current = current.right     # 6. SPUŠTANJE: idi desno

        if current is None:                 # 7. PROVJERA: ključ nije pronađen
            print("no key")
            return


        # =========================
        # CASE 1 : nema djece
        # =========================
        if current.left is None and current.right is None:

            if current != self.root:        # 8. PROVJERA: nije root

                if parent.left == current:  # 9. VEZA: brišemo lijevo dijete
                    parent.left = None
                else:                       # 10. VEZA: brišemo desno dijete
                    parent.right = None

            else:
                self.root = None            # 11. ROOT: stablo postaje prazno


        # =========================
        # CASE 2 : dva djeteta
        # =========================
        elif current.left and current.right:

            successor_parent = current      # 12. PRAĆENJE: roditelj successora
            successor = current.right       # 13. START: idi u desno podstablo

            while successor.left is not None:
                successor_parent = successor# 14. PAMĆENJE: roditelj successora
                successor = successor.left  # 15. TRAŽENJE: najmanji u desnom podstablu

            current.key = successor.key     # 16. KOPIRANJE: prebaci key
            current.value = successor.value # 17. KOPIRANJE: prebaci value

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right


        # =========================
        # CASE 3 : jedno dijete
        # =========================
        else:

            child = current.left if current.left else current.right
            # 18. ODABIR: uzmi postojeće dijete

            if current != self.root:

                if current == parent.left:
                    parent.left = child     # 19. SPAJANJE: parent poveži s child
                else:
                    parent.right = child

            else:
                self.root = child           # 20. ROOT: child postaje novi root


    def in_order_traversal(self, node=None, result=None):

        if result is None:
            result = []                     # 1. STVARANJE: lista za rezultate

        if node is None:
            node = self.root                # 2. START: kreni od root-a

        if node.left is not None:
            self.in_order_traversal(node.left, result)
            # 3. LIJEVO: prvo obiđi lijevo podstablo

        result.append((node.key, node.value))
        # 4. DODAVANJE: spremi trenutni čvor

        if node.right is not None:
            self.in_order_traversal(node.right, result)
            # 5. DESNO: zatim obiđi desno podstablo

        return result                       # 6. POVRATAK: sortirana lista
