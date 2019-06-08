# Funkcje i wyjątki

## Czym jest funkcja

Na chłopski rozum: funkcja to wydzielony fragment kodu, który można wielokrotnie używać w różnych miejscach programu.

## Jak napisać własną funkcję?

```
def <nazwa funkcji>([argument1, argument2, ..., argumentN]):
    <ciało funkcji>
```

Przykładowo:

```python
def hello():
    print("Greetings, human!")

def hello_name(name):
    print("Hello " + name + ".")
```

Aby przerwać działanie funkcji i zwrócić wartość, należy użyć słowa return, a za nim umieścić zwracaną wartość. W przypadku pominięcia wartości, funkcja zakończy swoje działanie i nic nie zwróci. Przykład:

```python
def function_with_no_return():
    a = 4
    b = 2
    c = a/b
    print("Wynik z dzielenia to " + c)

def function_with_return():
    a = 4
    b = 2
    return 4/2

test1 = function_with_no_return()
print(test1)
test2 = function_with_return()
print(test2)
```

## Jak wywołać funkcję

Prosta sprawa, piszemy nazwę funkcji a w nawiasach podajemy wymagane argumenty:

```python
def super_funkcja(argument):
    print(argument)

super_funkcja("elo elo 320")
```

## Wyjątki

Podczas programowania często mamy do czynienia z błędami, jest to normalna kolej rzeczy i bardzo ciężko ich uniknąć. Użytkownik podaje niewłaściwe dane, połączenie z internetem zostaje zerwane, skończyła się pamięć czy też po prostu my popełniliśmy błąd. Trzeba sobie jakoś z tym radzić. Pomagają nam w tym wyjątki.

```python
>>> def dziel(a,b):
...     return a/b
... 
>>> dziel(10,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in dziel
ZeroDivisionError: division by zero
```

Jak widać, Python nie lubi dzielić przez zero. W momencie dzielenia przez 0 Python rzuca wyjątek `ZeroDivisionError` i kończy działanie naszej funkcji. Czy możemy temu zaradzić? Owszem, możemy napisać funkcję tak, aby spodziewała się tego wyjątku:

```python
def dziel(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Nie dziel przez zero, cholero!")

dziel(10,0)
Nie dziel przez zero, cholero!
```

Python 3 ma dużo różnych wbudowanych wyjątków - https://docs.python.org/3/library/exceptions.html#bltin-exceptions
