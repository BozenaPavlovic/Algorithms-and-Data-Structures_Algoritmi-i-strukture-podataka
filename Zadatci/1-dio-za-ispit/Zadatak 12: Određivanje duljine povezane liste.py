# ==============================================================================
# ZADATAK 12: Duljina povezane liste bez atributa veličine
#
# TEKST ZADATKA:
# Napišite metodu koja određuje i vraća duljinu jednostruko povezane liste, 
# pod pretpostavkom da ne postoji atribut u kojem je spremljen taj podatak.
# ==============================================================================

    def duljina(self):
        brojac = 0
        curr = self.glava
        while curr is not None:
            brojac += 1
            curr = curr.sljedeci
        return brojac
