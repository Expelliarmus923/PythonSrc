# -*- coding:utf-8 -*-
import random

__author__ = 'lulizhou'

# 1. Dice Rolling Simulator
def DiceRollingSimulator(again='yes'):
    while again == 'yes':
        num = random.randint(1, 6)
        print("The Dice is", num)
        print("again?(yes/no)")
        again = input()


# DiceRollingSimulator()

# 2. Guess the Number
def GuessTheNumber(again='yes'):
    while again == 'yes':
        num = random.randint(1, 6)
        print("input your guess number ")
        guessnumber = int(input())
        if guessnumber == num:
            print("Congratulation!The number is %d" % (num))
        else:
            print("Sorry!This number is %d,Your guess number is %d" % (num, guessnumber))
        print("again?(yes/no)")
        again = input()


GuessTheNumber()