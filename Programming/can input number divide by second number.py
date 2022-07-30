number = int(input("Please enter the first number\n"))
number1 = int(input("Please enter the second number\n"))
while number <=0 or number1 <=0:
    number = int(input("Please enter the first number\n"))
    number1 = int(input("Please enter the second number\n"))
    
if number % number1==0:
    print(str(number) +"can be divided by"+ str(number1))
if number % number1 > 0:
    print(str(number)+"can't be divided by"+ str(number1))