x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter the third integer: "))

maxNum = None

if x % 2 != 0 and (maxNum is None or x > maxNum):
    maxNum = x

if y % 2 != 0 and (maxNum is None or y > maxNum):
    maxNum = y

if z % 2 != 0 and (maxNum is None or z > maxNum):
    maxNum = z

if maxNum is not None:
    print(maxNum, "is the largest odd integer.")
else:
    print("There are no odd integers.")

#I made this code using the examples on the Drill as guide. 
