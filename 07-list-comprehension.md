# List comprehension

List comprehension (albo listy składane) są bardzo przydatnym narzędziem tworzącym nową listę na podstawie listy.

Przykładowo powiedzmy, że potrzebujemy stworzyć nową tablicę liczb całkowitych, które określają długość każdego słowa w pewnym napisie, ale pod warunkiem, że nie jest to słowo "nad". Normalnie napisalibyśmy to w sposób podobny do poniższego:

```python
napis = "Ola ma kota, nad kotem wisi potężny galaretowanty sześcian którego nie widać"
slowa = napis.split(" ")
dlugosc_slow = []
for slowo in slowa:
    if slowo != "nad":
        dlugosc_slow.append(len(slowo))
````

Cały zapis na szczeście możemy skrócić dzięki listom składanym:

```python
napis = "Ola ma kota, nad kotem wisi potężny galaretowanty sześcian którego nie widać"
dlugosc_slow = [len(slowo) for slowo in napis.split() if slowo != "nad"]
```

Warunek `if` oczywiście możemy pominąć.


## Zadanie

Mając daną tablicę liczb `liczby = [3.14, 5.31, 8.123, 29.312, 81293.12314]`, za pomocą listy składanej utwórz nową listę - `calkowite` - które będzie zawierała część całkowitą każdej liczby.
