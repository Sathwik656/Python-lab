def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def count(n):
    c = 0
    num = 2
    while(c<=n):
        if(prime(num)):
            c = c + 1
            yield num
        num = num + 1

n = int(input("Enter the number: "))
ob = count(n)
for i in range(n):
    print(next(ob))