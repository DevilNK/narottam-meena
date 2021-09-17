x = int(input("enter number 1 :"))
y = int(input("enter number 2 :"))
z = int(input("enter number 3 :"))
print("number that you write :", x,y,z)
x,y,z = y,z,x
print("after swapping :", x,y,z)