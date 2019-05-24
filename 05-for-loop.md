# Pętla `for`

Pętla `for` służy do zapętlania instrukcji.

## Z funkcją range()

Funkcja `range(start, end[, step])` służy do generowania zakresu od pewnej wartości do pewnej wartości. Należy pamiętać, że wartość końcowa **nie** zawiera się w zakresie

```python
for user in range(0, 3):
    name = input("Jak masz na imię?")
    print("Cześć", name)
```

```python
>>> for i in range(2, 5):
...     print("krok: ", i)
...
krok:  2
krok:  3
krok:  4
```

```python
>>> for i in range(0, 10, 2):
...     print("krok: ", i)
...
krok:  0
krok:  2
krok:  4
krok:  6
krok:  8
```

## Z listą albo krotką

```
lista = [1, "a", 2.3]
krotka = (1, "a", 2.3)
>>> for element in lista:
...     print(element)
...
1
a
2.3
>>> for rzecz in krotka:
...     print(element)
...
1
a
2.3
```

Możemy to zrobić w trochę bardziej pokrętny sposób:

```
lista = [1, "a", 2.3]
>>> for i in range(0, 3):
...     print(lista[i])
...
1
a
2.3
```

Iterować możemy też po stringu albo słowniku:

```
>>> for i in "Ala ma kota.":
...     print(i)
...
A
l
a
 
m
a
 
k
o
t
a
.
```

```python
>>> d = { "klucz": "wartosc" }
>>> for element in d:
...     print(element)
...
klucz
```
