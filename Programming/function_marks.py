from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

done = 0
row = 1
column = "A"

def function(name,subject,mark):
  subject = input()
  mark = int(input())
  while mark > 100 or mark < 0:
  	mark = int(input())
  print(name + " " + subject + " " + str(mark))
  	

name = "b"
subject = "c"
mark = 0

while done != 1:

    sheet["A"+str(row)] = str(input("Enter your name"))

    sheet["B"+str(row)] = str(input("Enter your subject"))

    sheet["C"+str(row)] = str(input("Enter your mark"))
    mark=int(input())
    while mark < 100 or mark > 0:
    	done = int(input("Do you want to continue?"))
    row = row +1
    workbook.save(filename="hello_world.xlsx")

    #function(name,subject,mark)
