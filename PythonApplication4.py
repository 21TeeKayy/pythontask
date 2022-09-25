import math
class Parent:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def findArea(self):
        s = 0
        for x in self.sides:
            #print (x,"\n")
            s = s + x
        #print (s,"\n")
        s = s/2
        e = s
        for x in self.sides:
            e = e * (s-x)
            #print (e,"\n")
        area = math.sqrt(e)
        print('The area of the triangle is %0.2f' %area)

class Triangle(Parent):
    def __init__(self):
        Parent.__init__(self,3)
    def findArea(self):
        Parent.findArea(self)
    
t = Triangle()
t.inputSides()
t.findArea()