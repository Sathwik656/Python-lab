class circle:
    def assign(self,rad):
        self.rad = rad
    def calarea(self):
        pi = 3.14
        return pi * (self.rad**2)
    def circum(self):
        pi = 3.14
        return 2 * pi * self.rad
    
c1 = circle()
r = int(input("Enter the radius: "))
c1.assign(r)
area = c1.calarea()
cir = c1.circum()

print("Area: ",area)
print("Circumference: ",cir)