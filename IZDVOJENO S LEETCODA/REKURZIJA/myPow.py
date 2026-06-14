def myPow(x, n):
    # Bazni slučaj: bilo koji broj na potenciju 0 je 1
    if n == 0:
        return 1.0

    # Ako je potencija negativna, preokrenemo bazu i pretvorimo n u pozitivan broj
    if n < 0:
        x = 1 / x
        n = -n

    # Rekurzivno izračunamo polovicu potencije
    half = myPow(x, n // 2)

    # Ako je n paran
    if n % 2 == 0:
        return half * half
    # Ako je n neparan
    else:
        return half * half * x