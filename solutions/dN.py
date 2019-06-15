#!/usr/bin/env python3

# Program symulujący rzut kostką n-ścienną

import random

user_input = ""
sides = int(input("Ile ścian ma kostka którą rzucasz? "))
while input != "n":
    print(random.randint(1, sides))
    user_input = input("Czy chcesz wylosować kolejną liczbę? (y/n) ")
    if user_input == "n":
        break
