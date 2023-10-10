## simpel lommeregner af Fahad, Betiel, Thomas
# opdateres til version 2.0

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def gange(x, y):
    return x * y

def division(x,y):
    if y == 0:
        raise ZeroDivisionError # må ikke divideres med 0
    return x/y

while True:

    print("Velkommen til vores lommeregner.\n")
    print("Vælg hvilken operation du vil bruge.\n")
    print("1. Plus")
    print("2. Minus")
    print("3. Gange")
    print("4. Division")
    print("5. Afslut\n")


    valg_bruger = input("Skriv dit valg 1/2/3/4/5: ")

    if valg_bruger == '5':
        print("Farvel! :D")
        break

    if valg_bruger in ('1', '2', '3', '4'):
        try:
            tal1 = int(input("Skriv dit første nummer: "))
            tal2 = int(input("Skriv dit andet nummer: "))

            if valg_bruger == '1':
                print("Resultat: ", plus(tal1, tal2))
            elif valg_bruger == '2':
                print("Resultat: ", minus(tal1, tal2))
            elif valg_bruger == '3':
                print("Resultat: ", gange(tal1, tal2))
            elif valg_bruger == '4':
                try:
                    print("Resultat: ", division(tal1, tal2))
                except ZeroDivisionError as e:
                    print("Fejl. Kan ikke dividere med 0.", e)

        except ValueError: # hvis ikke man vælger et tal
            print("Ugyldigt tal.\n")

    else:
        print("Ugyldigt tal. Vælg mellem 1/2/3/4/5")

    ny_beregning = input("Vil du lave en ny beregning? (Ja/Nej): ")
    if ny_beregning.lower() != "ja":
        break








