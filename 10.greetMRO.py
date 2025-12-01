class first:
    def greet(self):
        print("Good morning!")

class second:
    def greet(self):
        print("Good Afternoon!")

class third(first,second):
    def greet(self):
        print("Good evening")

res=third()
res.greet()