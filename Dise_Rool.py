import random

def Dise_roll():
    DiseRoll = random.randint(1,6)
    return DiseRoll
    
print(Dise_roll())

print("Want to roll again 1.Yes / 2.No")

choice = int(input("ENter: "))

if choice == 1:
    print(Dise_roll())
else:
    breakpoint