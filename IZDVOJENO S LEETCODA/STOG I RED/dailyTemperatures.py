# ==============================================================================
# ZADATAK: 739. Daily Temperatures (Dnevne temperature)
#
# KATEGORIJA: STRUKTURE PODATAKA / STOG (STACK) / MONOTONI STOG
#
# TEKST ZADATKA:
# Zadan je niz cijelih brojeva 'temperatures' koji predstavlja dnevne temperature.
# Potrebno je vratiti niz 'answer' takav da je 'answer[i]' broj dana koje moraš
# čekati nakon i-tog dana da bi dočekao topliju temperaturu. 
# Ako ne postoji nijedan budući dan s toplijom temperaturom, postavi 'answer[i] = 0'.
#
# PRIMJER:
# Unos: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Izlaz: [1, 1, 4, 2, 1, 1, 0, 0]
# Objašnjenje: Za prvi dan (73), idući dan je 74 (topliji), pa čekamo 1 dan.
# Za treći dan (75), moramo čekati čak 4 dana da dođe 76, jer su idući 71, 69, 72.
#
# ZAHTJEV NA ISPITU / LEETCODE-u:
# Rješenje mora raditi u vremenskoj složenosti O(n) - samo jedan prolaz kroz niz!
# Korištenje ugniježđene for petlje (provjera svakog dana sa svakim idućim) rezultirat 
# će "Time Limit Exceeded" pogreškom jer je presporo.
# ==============================================================================

def dailyTemperatures(temperatures):
    n = len(temperatures)
    # Inicijaliziramo niz rezultata s nulama. Ako za neki dan ne nađemo topliji dan,
    # on će automatski ostati postavljen na 0, što zadatak i traži.
    answer = [0] * n
    
    # Stog koji stvaraš pamti INDEKSE (dane), a ne same temperature.
    # Pomoću indeksa lako možemo doći i do temperature (temperatures[indeks])
    # i izračunati razliku u danima (current_day - prev_day).
    stack = Stack()  

    # Prolazimo kroz sve dane u nizu
    for current_day in range(n):
        current_temp = temperatures[current_day]

        # KLJUČNI DIO ALGORITMA:
        # Dokle god na stogu imamo spremljene dane (stog nije prazan) I dokle god je 
        # današnja temperatura (current_temp) STROGO VEĆA od temperature dana 
        # koji se nalazi na samom vrhu stoga (temperatures[stack.top()]):
        while not stack.is_empty() and current_temp > temperatures[stack.top()]:
            # Našli smo topliji dan za onaj dan s vrha stoga! Skidamo ga sa stoga.
            prev_day = stack.pop()
            # Izračunavamo razliku u danima (indeksima) i upisujemo je u rezultat
            answer[prev_day] = current_day - prev_day  

        # Na kraju svakog koraka, dodajemo današnji dan na stog.
        # On će tamo čekati dok se u budućnosti ne pojavi neki još topliji dan.
        stack.push(current_day)

    # Vraćamo konačni niz s izračunatim danima čekanja
    return answer
