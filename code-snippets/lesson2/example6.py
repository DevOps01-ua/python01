try:
    file = open("data.tx", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Error reading file!")
else:
    print("File read successfully!")

a = len(list("1",2))

var = function(var)
var = object.attribute("sdfsaf")