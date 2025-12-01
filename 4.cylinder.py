def cylinder(r,h):
    vol = 22/7*r*r*h
    return vol

r = int(input("Enter r value: "))
h = int(input("Enter h value: "))
print("Positional argument: ",cylinder(r,h))
print("Keyword argument: ",cylinder(h=7,r=5))
li=(3,5)
print("Iterrable unpacking: ",cylinder(*li))
di = {'r':3,'h':5}
print("Dictionary unpacking: ",cylinder(**di))
