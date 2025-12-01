'''def fun1():
    val = 20
    def fun2():
        nonlocal val
        val = 30
        print("Value in local: ",val)
    fun2()
    print("Value in enclosing: ",val)
fun1()
val = 50
print("Value in global scope",val)
'''

def fun3():
    global val
    val = 20
    def fun4():
        val = 40
        print("Value in local: ",val)
    fun4()
    print("Value in enclosing: ",val)
val = 50
fun3()
print("Value in golbal scope: ",val)
