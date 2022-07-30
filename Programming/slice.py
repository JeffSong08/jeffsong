shopList = [] 
maxLengthList = 6
while len(shopList) < maxLengthList:
    item = "a"
    while len(item) < 4 or item.isdigit():
        item = input("Enter your Item to the List: ")
        if item.isdigit():
            print("Your item cannot be a number.")
    shopList.append(item)
    print (shopList)
print ("That's your Shopping List")
print (shopList)