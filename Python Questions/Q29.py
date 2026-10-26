# program to shuffle of deck card 

import random, itertools

deck = list(itertools.product(range(1,14),["spade","club","Hearts","Diamond"]))
random.shuffle(deck)
print(deck)

for i in range(1,6):
    print(deck[i][0], "of" , deck[i][1])