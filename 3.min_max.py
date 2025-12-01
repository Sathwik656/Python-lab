lis = []
def maxmin(val):
    maxi = 0
    mini = 9
    while val > 0:
        d = val % 10
        if maxi < d:
            maxi = d
        if mini > d:
            mini = d
        val = val // 10
    return maxi,mini

n=int(input("Enter the size: "))
for i in range(n):
    ele=int(input("Enter values: "))
    lis.append(ele)

for i in lis:
    x,y=maxmin(i)
    print("value: ",i)
    print("Maximum: ",x)
    print("Minimum: ",y)
 