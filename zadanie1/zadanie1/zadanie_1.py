import random

# Tworzymy dwie listy
lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']

# Laczenie funkcja zip()
polaczone = list(zip(lista1, lista2))
print("Połączone listy:", polaczone)

# Wykorzystujemy funkcje random.choice() do losowego wyboru elementu
losowy_element = random.choice(lista1)
print("Losowy element z lista1:", losowy_element)

# Obsluga wyjatku try-except
try:
    dzielenie = 10 / int(input("Podaj liczbę: "))
    print("Wynik dzielenia:", dzielenie)
except ValueError:
    print("Błąd: Wprowadzona wartość nie jest liczbą!")
except ZeroDivisionError:
    print("Błąd: Nie można dzielić przez zero!")

# Linki do dokumentacji:
# zip(): https://docs.python.org/3/library/functions.html#zip
# random.choice(): https://docs.python.org/3/library/random.html#random.choice
# ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
