# Funkcje o zmiennej liczbie argumentów

## Zwykłe funkcje

Każda funkcja w Pythonie otrzymuje określoną liczbę argumentów. Jeżeli przekażemy jej zbyt dużo, lub zbyt mało argumentów to otrzymamy błąd

```python
>>> def f1(a,b,c,d):
...     pass
...
>>> f1(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f1() missing 3 required positional arguments: 'b', 'c', and 'd'
>>> f1(1,2,3,4,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f1() takes 4 positional arguments but 5 were given
```

## Funkcje ze zmienną liczbą argumentów

```python
def f2(first, second, third, *rest):
    print "Pierwszy: %s" % first
    print "Drugi: %s" % second
    print "Trzeci: %s" % third
    print "Reszta: %s" % list(rest)
```

## Argumenty kluczowe

```
def funkcja(pierwszy, drugi, trzeci, **opcje):
    if opcje.get("akcja") == "dodaj":
        print "Suma to: %d" % (pierwszy + drugi + trzeci)

    if opcje.get("zwroc") == "pierwszy":
        return pierwszy

wynik = funkcja(1, 2, 3, akcja = "dodaj", zwroc = "pierwszy")
print "Wynik: %d" % wynik
```

## Zadanie

Napisz funkcje `foo` i `bar` tak, aby mogły otrzymywać zmienną liczbę argumentów (3 lub więcej). Funkcja `foo` musi zwracać liczbę dodatkowych argumentów jakie otrzymała. Funkcja `bar` musi zwracać `True`, jeśli argument przypisany słowu kluczowemu `magiczna_liczba` jest równy 7, oraz `False` w przeciwnym razie.
