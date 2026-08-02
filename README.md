# Algorithms-and-Data-Structures_Algoritmi-i-strukture-podataka
Stvari za učenje na jednom mijestu


## Dva ključna uvjeta (pravila) na ispitu
Kada u tekstu zadatka dobijete algoritam, prvo morate provjeriti na koji način smijete modificirati listu:

   1. Verzija sa zamjenom podataka (data swap) – Profesorovo rješenje
   * Uvjet: Čvorovi ostaju na fiksnim adresama u memoriji, a mijenjaju se samo njihove vrijednosti.
      * Prepoznavanje u zadatku: Ako profesor u tekstu ne naglasi "preusmjeravanjem pokazivača" ili ako u službenom rješenju koristi izraz poput node1.data, node2.data = node2.data, node1.data.
      * Prednost: Puno jednostavnije za pisanje jer je logika petlji identična onoj za obična polja (arrays).
   2. Verzija sa zamjenom pokazivača (pointer swap) – Napredna verzija
   * Uvjet: Vrijednost .data je zaključana (read-only). Morate fizički otspojiti pokazivač .next (i .prev kod dvostruke liste) te ih ponovno prespojiti.
      * Prepoznavanje u zadatku: Profesor će eksplicitno naglasiti: "Sortirati listu promjenom strukture/pokazivača, a ne zamjenom podataka".
   
------------------------------
## Pregled svih algoritama za ispit (Jednostruko vs. Dvostruko povezana lista)## 1. BUBBLE SORT (Sortiranje mjehurićima)

* Logika: Prolazi kroz listu i uspoređuje susjedne čvorove (current i current.next). Ako su u neispravnom poretku, zamjenjuje ih. Postupak se ponavlja sve dok ima zamjena (swapped = True).
* Uvjet za jednostruku listu: Kreće se isključivo prema naprijed (current = current.next).
* Uvjet za dvostruku listu: Može se kretati u oba smjera (Cocktail Shaker varijanta). Ako se traži običan Bubble Sort, kod je identičan onom za jednostruku listu jer pokazivač .prev uopće ne morate koristiti ako mijenjate samo .data.
* Vremenska složenost: $O(N^2)$

## 2. SELECTION SORT (Sortiranje odabirom / Traženje ekstrema)

* Logika: Fiksira jedan čvor (start), a pomoću druge petlje traži najmanji (ili najveći) element u ostatku liste. Na kraju kruga zamjenjuje vrijednosti čvora start i pronađenog čvora min_node.
* Uvjet za jednostruku listu: Vanjska petlja pomiče start = start.next. Unutarnja petlja kreće od start.next pa sve do kraja liste.
* Uvjet za dvostruku listu: Logika je identična. Pokazivač .prev nije potreban ako radite zamjenu podataka.
* Vremenska složenost: $O(N^2)$ u svim slučajevima (uvijek pretražuje listu do samog kraja).

## 3. INSERTION SORT (Sortiranje umetanjem)

* Logika: Uzima jedan po jedan element iz nesortiranog dijela i umeće ga na točno mjesto unutar već sortiranog dijela liste (krećući se unazad).
* Uvjet za jednostruku listu: Vrlo zahtjevno za pisanje na papiru. Budući da se jednostruka lista ne može kretati unazad, svaki put morate krenuti od početka (head) prema naprijed kako biste pronašli ispravnu poziciju za umetanje.
* Uvjet za dvostruku listu: Idealno rješenje. Kada izdvojite element, pomoću pokazivača .prev jednostavno se vraćate unazad kroz listu dok ne pronađete njegovo ispravno mjesto i tamo ga umetnete.
* Vremenska složenost: $O(N^2)$

## 4. QUICK SORT (Brzo sortiranje / Particioniranje oko stožera)

* Logika: Odabire se jedan element (obično prvi ili zadnji) koji služi kao stožer (pivot). Lista se zatim dijeli na elemente koji su manji od stožera i one koji su veći.
* Uvjet za jednostruku listu: Izvodi se rekurzivno kreiranjem novih podlisti.
* Uvjet za dvostruku listu: Može se implementirati pomoću dva pokazivača (left na head i right na kraj liste) koji se kreću jedan prema drugome zahvaljujući pokazivačima .next i .prev.
* Vremenska složenost: Prosječno $O(N \log N)$, a u najgorem slučaju $O(N^2)$.


## 5. MERGE SORT (Sortiranje spajanjem)

* Logika: Radi po principu "podijeli pa vladaj". Lista se pomoću dva brza/spora pokazivača podijeli točno na pola. Zatim se obje polovice rekurzivno sortiraju i na kraju ponovno spajaju u jednu ispravno poredanu listu.
* Uvjet za jednostruku listu: Najbolje i najčešće rješenje za jednostruku listu jer ne zahtijeva kretanje unazad. Sredina se pronalazi tehnikom "spori i brzi pokazivač" (slow ide za 1 čvor, fast za 2 čvora). Kada fast dođe do kraja, slow se nalazi na sredini liste. Vezu između polovica prekidamo s slow.next = None.
* Uvjet za dvostruku listu: Logika dijeljenja i spajanja je ista, ali prilikom spajanja čvorova morate paziti da svakom čvoru ispravno postavite i pokazivač .prev unazad.
* Vremenska složenost: Uvijek $O(N \log N)$ (najbolji, prosječni i najgori slučaj). To ga čini stabilnijim od Quick Sorta na povezanim listama.

## 6. BUCKET SORT (Sortiranje po koševima)

* Logika: Elementi se na temelju svojih vrijednosti (npr. dijeljenjem s 10) raspoređuju u nekoliko zasebnih "koševa" (u Pythonu su to obični nizovi/liste). Svaki se koš potom zasebno sortira (na papiru se smije koristiti ugrađeni .sort()), a na kraju se svi koševi povežu natrag u jednu veliku povezanu listu.
* Uvjet za jednostruku listu: Prolazi se kroz povezanu listu, privremeno se prekida veza čvora (current.next = None) i cijeli čvor se sprema (funkcijom .append()) u odgovarajući koš u nizu. Nakon sortiranja koševa, prođe se kroz sve koševe i čvorovi se ulančaju pomoću .next pokazivača.
* Uvjet za dvostruku listu: Princip raspodjele je isti, ali prilikom završnog prespajanja i pražnjenja koševa morate rekonstruirati i .prev pokazivače između čvorova.
* Vremenska složenost:
* Najbolji/Prosječni slučaj: O(N) – ako su podaci ravnomjerno raspoređeni, u svakom košu će biti minimalan broj elemenata, pa je sortiranje izuzetno brzo.
   * Najgori slučaj: O(N²) – ako svi podaci završe u jednom jedinom košu (npr. svi brojevi počinju istom znamenkom), tada Bucket Sort ovisi o algoritmu kojim se taj koš sortira (ako je to Bubble Sort, složenost skače na kvadratnu).

-----------------------------



------------------------------
## Pobjednička taktika za ispit 
Ako se na ispitu pojavi bilo koji od ovih algoritama, a profesor nije izričito naglasio da morate mijenjati pokazivače, uvijek pišite verziju sa zamjenom podataka (data swap). To je najsigurniji put koji eliminira rizik od pogrešnog prespajanja memorijskih veza i gubitka bodova. Profesorovo prošlogodišnje službeno rješenje dokazuje da on takav pristup priznaje i ocjenjuje maksimalnim brojem bodova.
Želite li da na isti način pripremimo i analiziramo Merge Sort ili Bucket Sort kako biste imali spremne natuknice za ispit?
