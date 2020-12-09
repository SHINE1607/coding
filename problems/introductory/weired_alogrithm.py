import os
import sys 
import math
import re
import random


def weired_algorithm(n):
    print(int(n), end = " ")
    res = []
    while n != 1:
        
        if n % 2 == 0:
            n = n /2
        else:
            n = n*3 + 1
        print(int(n), end= " ")
        

n = int(input())  
weired_algorithm(n)  
    


