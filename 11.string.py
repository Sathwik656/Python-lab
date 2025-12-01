class stringOP:
    @staticmethod
    def volcount(st):
        c = 0
        for i in st:
            if i in 'aeiou':
                c = c + 1
        return c
    @staticmethod
    def charexist(st):
        ch = input("Enter the char: ")
        if ch in st:
            return True
        return False
    
class person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Age: ",self.age)
    @classmethod
    def read(cls):
        pid = int(input("Enter pid: "))
        pname = input("Enter pname: ")
        page = int(input("Enter p age: "))
        return cls(pid,pname,page)

person.read()


stri = input("Enter a string: ")
ct = stringOP.volcount(stri)
print("Vovel count: ",ct)
if stringOP.charexist(stri):
    print("Exists")
else:
    print("Does not exists")