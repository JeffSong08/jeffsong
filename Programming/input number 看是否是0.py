import random

number = 1

while number!=0:
    number1 = (random.randint(0,9))
    number2 = (random.randint(0,9))

    answer = number1+number2

    print(str(number1)+"+"+str(number2)+"=")

    number = int(input())
    
    if number == answer:
        print("Correct")
        
    
    if number == 0:
        print("Quit")
        


    
