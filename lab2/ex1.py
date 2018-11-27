import random
with open('a.txt', 'r', encoding="utf-8") as infile:
    list = infile.read().split('\n')
    print(random.choice(list))