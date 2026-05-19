
### Vremenska složenost (Time Complexity)

| Metoda | Vremenska složenost | Razlog i pozadinska operacija |
| --- | --- | --- |
| `set(key, value)` | **$O(n)$** | Koristi operaciju `if key in self.keys` i `.index(key)`. Elementi su nesređeni, pa računalo mora raditi **linearno (sekvencijalno) pretraživanje** od početka do kraja niza. |
| `get(key)` | **$O(n)$** | Također zahtijeva linearno pretraživanje kroz niz ključeva kako bi pronašla indeks elementa. |
| `delete(key)` | **$O(n)$** | Osim pronalaženja indeksa ($O(n)$), operacija `del` nad ugrađenom listom zahtijeva pomicanje svih elemenata koji se nalaze desno od obrisanog mjesta za jedno mjesto ulijevo. |
| `contains(key)` | **$O(n)$** | Izravno radi sekvencijalnu provjeru `key in self.keys` kroz cijeli niz. |
| `__len__()` | **$O(1)$** | **Konstantno vrijeme**. Pythonove interne liste u svakom trenutku u memoriji čuvaju podatak o svojoj trenutnoj duljini, pa nema potrebe za prebrojavanjem. |

### Prostorna složenost (Space Complexity)

* **Ukupna složenost:** **$O(n)$**
* *Objašnjenje:* Memorija raste linearno s brojem unesenih zapisa. Budući da koristimo tehniku paralelnih nizova, u memoriji zauzimamo prostor za točno $2 \times n$ elemenata (jedan niz za ključeve, jedan za vrijednosti).

### pitanje:
*"Zašto se ova implementacija ne koristi u produkciji i stvarnim sustavima?"*, točan inženjerski odgovor glasi: **Struktura nije skalabilna.**

Kada broj elemenata ($n$) naraste na velike vrijednosti (npr. 100.000 ili više), svaka osnovna operacija poput uploada ili dohvata podataka postaje izrazito spora jer zahtijeva stotine tisuća računalnih koraka, što dovodi do zagušenja procesora.



### `CustomDict` vs. Ugrađeni Python `dict`

Ovaj zadatak služi kao motivacija za učenje **(Hash Tables)**.

* **`CustomDict` (Naša klasa):** Traži element uspoređivanjem traženog ključa s nizom postojećih ključeva jedan po jedan dok ne nađe poklapanje. Rezultat je sporost od **$O(n)$**.
* **Ugrađeni `dict` (Hash mapa):** Koristi **hash funkciju** koja uzme ključ (bilo koji objekt/tekst) i matematički ga preslika izravno u jedinstveni cijeli broj (indeks u memoriji). Računalo ne pretražuje elemente, već odmah "skače" na izračunatu memorijsku adresu. Time ugrađeni rječnik postiže prosječnu brzinu od **$O(1)$** (konstantno vrijeme), bez obzira na količinu podataka.


> **Paralelni nizovi (Parallel Arrays):**
> Tehnika struktura podataka u kojoj se povezani atributi istog objekta (ovdje ključ i njegova vrijednost) spremaju u odvojene nizove, ali na **identičnim indeksima**. Glavni rizik ove tehnike je ljudska pogreška u kodu – ako se prilikom brisanja ili dodavanja nizovi ručno ne sinkroniziraju, cijela struktura gubi integritet.

> **ADT - Apstraktni tip podataka (Abstract Data Type):**
> Matematički i logički model koji definira isključivo **ponašanje** strukture (skup dopuštenih operacija i njihove ulaze/izlaze, npr. *"Mapa mora moći pohraniti i dohvatiti element preko ključa"*). ADT ne govori ništa o kodu niti o tome kako će ti podaci fizički sjediti u memoriji. Klasa `CustomDict` je samo jedna (manje učinkovita) konkretna implementacija ADT-a Mape.

> **Rubni slučajevi (Corner/Edge Cases):**
> Problematične ili specifične situacije u izvršavanju koda na koje programer mora misliti unaprijed. U ovom zadatku to su:
> 1. Pokušaj dohvaćanja ili brisanja ključa koji uopće ne postoji u mapi (rješava se bacanjem `KeyError` iznimke).
> 2. Pokušaj umetanja ključa koji već postoji (rješava se tako da se stara vrijednost pregazi novom, umjesto da se dodaje novi element na kraj niza).
> 
>
