from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

for counter in range (1,100,1):
    sheet["A"+str(counter)] = counter
    
workbook.save(filename="hello_world.xlsx")