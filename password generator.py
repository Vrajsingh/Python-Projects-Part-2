// Beginner Code

import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[],:;_/\\?+'# "

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)


// Optimized Code
    
import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16
amount = 10

for x in range(amount):
    password = "".join(random.sample(total, length))
    print(password)
