import random



number = 1



correctanswer = 0
wronganswer = 0

print("Choose one \n1 is addition\n2 is subtraction\n3 is multiplication\n4 is division")

input1 = int(input())

if input1 == 1:
    while number!=0:
        number1 = (random.randint(0,100))
        number2 = (random.randint(1,100))

        answer = number1+number2

        print(str(number1)+"+"+str(number2)+"=")

        number = int(input())
    
        if number == answer:
            print("Correct")
            correctanswer = correctanswer+1
        if number != answer:
            print("Wrong")
            wronganswer = wronganswer+1
        
    
        if number == 0:
            print("Quit")
            
if input1 == 2:
    while number!=0:
        number1 = (random.randint(0,100))
        number2 = (random.randint(1,100))

        answer = number1-number2

        print(str(number1)+"-"+str(number2)+"=")

        number = int(input())
    
        if number == answer:
            print("Correct")
            correctanswer = correctanswer+1
        if number != answer:
            print("Wrong")
            wronganswer = wronganswer+1
        
    
        if number == 0:
            print("Quit")

if input1 == 3:
    while number!=0:
        number1 = (random.randint(0,100))
        number2 = (random.randint(1,100))

        answer = number1*number2

        print(str(number1)+"x"+str(number2)+"=")

        number = int(input())
    
        if number == answer:
            print("Correct")
            correctanswer = correctanswer+1
        if number != answer:
            print("Wrong")
            wronganswer = wronganswer+1
        
    
        if number == 0:
            print("Quit")

if input1 == 4:
    while number!=0:
        number1 = (random.randint(0,100))
        number2 = (random.randint(1,100))

        answer = number1/number2

        print(str(number1)+"/"+str(number2)+"=")

        number = int(input())
    
        if number == answer:
            print("Correct")
            correctanswer = correctanswer+1
        if number != answer:
            print("Wrong")
            wronganswer = wronganswer+1
        
    
        if number == 0:
            print("Quit")
        
print("Total correct answer: "+str(correctanswer))
print("Total wrong answer: "+str(wronganswer))
        


    
