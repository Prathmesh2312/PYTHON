#Program to calculate surface volume and area of a cylinder
pi=22/7
height=float(input("Enter the Height of Cylinder:"))
radius=float(input("Enter the Radius of Cylinder:"))

volume=pi*radius*radius*height                                   #Fromula of volume
surface_area=((2*pi*radius)*height)+((pi*radius**2)*2)           #Fromula of Surface area

print("Volume of cylinder is: ",volume)
print("Surface area of Cylinder is:",surface_area)


