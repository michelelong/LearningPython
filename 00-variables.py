# swap variable values without a 3rd variable
var1 = 1
var2 = 2
print(var1, " ", var2)

var1, var2 = var2, var1
print(var1, " ", var2)

# swap list variables
myList = [10, 1, 8, 3, 5]
print(myList)

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]
print(myList)

# or operator can be used to set a default value
mname = None
middle_name = mname or "Henry"
print(middle_name)
