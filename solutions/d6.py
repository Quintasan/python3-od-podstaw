#!/usr/bin/env python3

# Program symulujący rzut kostką sześciościenną

import random

user_input = ""
while input != "n":
    print(random.randint(1, 6))
    user_input = input("Czy chcesz wylosować kolejną liczbę? (y/n) ")
    if user_input == "n":
        break
