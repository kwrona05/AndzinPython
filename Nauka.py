definicje = {}

while True:
    print('1. Dodaj definicję')
    print('2. Znajdź definicję')
    print('3. Usuń definicję')
    print('4. Zakończ program')

    wybór = input("Co chcesz zrobić? ")

    if wybór == '1':
        klucz = input("Podaj klucz (słowo) do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie!")

    elif wybór == '2':
        klucz = input("Czego szukasz? ")
        if klucz in definicje:
            print(f"Definicja: {definicje[klucz]}")
        else:
            print("Nie znaleziono definicji.")

    elif wybór == '3':
        klucz = input("Którą definicję chcesz usunąć? ")
        if klucz in definicje:
            del definicje[klucz]
            print("Definicja usunięta!")
        else:
            print("Nie znaleziono definicji.")

    elif wybór == '4':
        print("Zamykanie programu...")
        break

    else:
        print("Niepoprawna opcja, spróbuj ponownie.")