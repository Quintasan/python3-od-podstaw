# Instrukcje warunkowe

## Porównywanie rzeczy

```python
>>> 0 < 1
True
>>> 0 > 1
False
>>> 0 <= 1
True
>>> 0 >= 1
False
>>> 1 == 0
False
>>> 1 == 1
True
>>> 1 != 0
True
>>> 1 != 1
False
```

## Sprawdzanie przynależności

```python
>>> x in [ 1, 12, 10 ]
True
>>> x in [ 1, 12, 'txt' ]
False
>>> x not in [ 1, 12, 'txt' ]
True
>>> 'str' is 'str'
True
>>> 'str' is 'string'
False
>>> 'str' in 'string'
True
```

## Łączenie warunków

```python
>>> x = 10
>>> x < 10
False
>>> x > 1 and x < 13
True
>>> x < 1 and x < 13
False
>>> x > 1 or x < 13
True
>>> x != 10 or x > 13
False
>>> x > 1 and x < 13 or x != 10
True
```

## Instrukcja warunkowa `if-elif-else`

W momencie gdy pewien kawałek kodu chcemy wykonać tylko wtedy gdy jakiś warunek jest spełniony to używamy do tego instrukcji `if`. Pełna jej postać to:

```
if (warunek):
    instrukcja1
    instrukcja2
    ...
elif (inny warunek):
    inna_instrukcja1
    inna_instrukcja2
    ...
else:
    instrukcja_gdy_zaden_warunek_nie_jest_spelniony1
    instrukcja_gdy_zaden_warunek_nie_jest_spelniony1
    ...
```

Przykładowe wykorzystanie:

```python
print("Ile masz lat?")
age = int( input() )
if ( age >= 18 ):
    print("Jesteś dorosłym człowiekiem")
elif ( age > 100 ):
    print("To naprawdę twój wiek?")
else:
    print("Trochę Ci zostało do pełnoletności")
```

```python
print("Ile masz lat?")
age = int( input() )
if ( age >= 18 ):
    print("Jesteś dorosłym człowiekiem")
if ( age > 100 ):
    print("To naprawdę twój wiek?")
else:
    print("Trochę Ci zostało do pełnoletności")
```
