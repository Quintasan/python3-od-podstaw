# Proste programy na początek

## Generator rzutów kostką

Napisz program symulujący rzut kostką sześciościenną, następnie pytający użytkownika czy chce wykonać kolejny rzut kostką. W przypadku negatywnej odpowiedzi program kończy pracę.

```
quintasan@ubuntu:~$ python dice.py
4
Czy chcesz ponownie rzucić kostką? (y/n) y
6
Czy chcesz ponownie rzucić kostką? (y/n) y
2
Czy chcesz ponownie rzucić kostką? (y/n) n
Zakończono pracę programu
```

## Generator rzutów kostką wielościenną

Podobnie jak wyżej z tym, że na początku pytamy użytkownika ile ścian ma mieć kostka którą rzucamy.

## Zgadnij liczbę

Napisz program losujący liczbę a następnie proszący użytkownika o zgadnięcie tej liczby. W przypadku gdy liczba wpisana przez użytkownika jest większa, wypisz `Wybrana liczba jest większa`, w przypadku gdy wpisana liczba jest mniejsza wypisz `Wybrana liczba jest mniejsza`. Użytkownik powinien mieć trzy próby po których program wypisuje `Koniec gry` i kończy pracę. W przypadku zgadnięcia liczby wypisujemy `Wygrałeś!` i również kończymy pracę programu.
