class employee:
    def __init__(self,eid,name,basic):
        self.eid = eid
        self.name = name
        self.basic = basic

    def calcluate(self):
        self.hra = 0.11 * self.basic
        if self.basic < 5000:
            self.da = 0.20 * self.basic
            self.tax = 0.10 * self.basic
        elif self.basic > 5000 and self.basic < 10000:
            self.da = 0.25 * self.basic
            self.tax = 0.15 * self.basic
        else:
            self.da = 0.30 * self.basic
            self.tax = 0.20 * self.basic
        self.pf = 1800
        self.gross = self.basic + self.da + self.hra
        self.net = self.gross - (self.pf + self.tax)

    def display(self):
        print("Eid: ",self.eid)
        print("Ename: ",self.name)
        print("Salary: ",self.basic)
        print("Gross sal: ",self.gross)
        print("Net salary: ",self.net)

eid = int(input("Enter eid: "))
name = input("Enter name: ")
basic = float(input("Enter basic salary: "))
e1 = employee(eid,name,basic)
e1.calcluate()
e1.display()