import random
counter = 0
oddnumber = 0
evennumber = 0

while counter < 1000:
    number1 = (random.randint(0,10000))
    counter = counter + 1
    
    if number1 % 2:
        evennumber = evennumber +1
    else:
        oddnumber = oddnumber + 1
print("Total of the odd number are "+str(oddnumber))
print("Total of the even number are "+str(evennumber))