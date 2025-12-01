class check:
    def perfect(self,n):
        self.n = n
        s = 0
        for i in range(1,self.n):
            if self.n % i == 0:
                s = s + i
        return s == self.n

    def prime(self,n):
        self.n=n
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    
class operation(check):
    def sumdig(self,n):
        self.n = n
        sumv = 0
        while n>0:
            dig = n % 10
            sumv = sumv + dig
            n = n // 10
        return sumv
    def bintodec(self,n):
        self.n=n
        p = 1
        bn = 0
        while n>0:
            r = n % 2
            bn = bn + (r*p)
            p = p * 10
            n = n // 2
        return bn
    
n = int(input("Enter the num: "))
op = operation()
print("Perfect number: ",op.perfect(n))
print("Prime number: ",op.prime(n))
print("Sum dig",op.sumdig(n))
print("Binary to dec: ",op.bintodec(n))