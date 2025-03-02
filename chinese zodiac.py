import math
for i in range(int(input())):
    elements =  ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    year = int(input())
    if year%2 == 0: sign = "Yang" 
    else: sign = "Yin"
    print(year, sign, elements[math.floor(((year-4)%10)/2)], animals[(year-4)%12])