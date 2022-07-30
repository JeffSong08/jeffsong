from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

done = 0
counter = 0


while done != 1:
    location1 = str(input("Choose your first location"))
    sheet[location1] = str(input("Choose what you need to input in your first location"))
    counter + 1
    done = int(input("Do you want to continue?"))
workbook.save(filename="hello_world.xlsx")