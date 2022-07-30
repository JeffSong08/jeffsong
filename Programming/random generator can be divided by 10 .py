import random
counter = 0
number10 = 0

while counter < 1000:
    number1 = (random.randint(0,10000))
    counter = counter + 1
    
    if number1 % 2:
        number10 = number10 +1

print("Total of the numbers that can be divided by 10 are "+str(number10))