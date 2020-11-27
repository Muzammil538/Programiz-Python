import math
# ax^2+ bx + c = 0
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

#We will divide it into two parts
#-root  = -b+-(squareroot)(b^2)-(4ac)/2a
d = (b**2) - (4*a*c)

#next part
root1 = (-b-math.sqrt(d))/(2*a)
root2 = (-b+math.sqrt(d))/(2*a)
print("The roots are : ")
print(root1, ",", root2)