
#Napisanie funkcji
def todoApp():
#dodać tablice
    zadania = []
#Print opcji
    print('1. Dodaj zadanie')
    print('2. Usuń zadanie')
    print('3. Wyświetl listę')
    print('4. Zakończ program')
#wybór opcji
    wybór = input('Wybierz opcję (1-4): ')
#logika po wyborze (if)
    if(wybór == '1'):
        zadanie = input('Podaj zadania')
        zadania.append(zadanie)
        print('Dodano zadanie')
    elif(wybór == '2'):
        usun_zadanie = input('Podaj zadanie')
        zadania.remove(usun_zadanie)
    elif(wybór == '3'):
        print(zadania)
    elif(wybór == '4'):
        print('Narazie')
    else:
        print('Błędny numer opcji')
todoApp()

