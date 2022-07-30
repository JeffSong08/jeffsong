def function(name,born):
  age = 2022 - int(born)
  print(name + " " + str(age))
  
name = "b"

while name != "a":
    name = input()
    if name == "a":
        break
    age = input()
    function(name,age)