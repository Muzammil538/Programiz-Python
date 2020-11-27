#s = (a+b+c)/2
#area = (s(s-a)*(s-b)*(s-c))**0.5

#We nee to do this in code
#sides of the Triangle
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

#calculating the semi-perimeter
s = (a+b+c) / 2
#calculate the area 
Area = (s(s-a)*(s-b)*(s-c))**0.5

print("The area of the Sides of Triangle given is: ",Area)