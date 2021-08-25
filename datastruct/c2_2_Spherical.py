# *สามารถใช้ from math import pi  หรือ math.pi  ได้*
from math import pi

class Spherical:

    def __init__(self,radius):
        self.radius = radius

        ### Enter Your Code Here ###

    def changeR(self,Radius):
        self.radius = Radius

        ### Enter Your Code Here ###

    def findVolume(self):
        result = (4/3)*pi*self.radius**3
        return result
        ### Enter Your Code Here ###

    def findArea(self):
        result = 4*pi*self.radius**2
        return result
        
        ### Enter Your Code Here ###

    def __str__(self):
        return "Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea())
        ### Enter Your Code Here ###

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)