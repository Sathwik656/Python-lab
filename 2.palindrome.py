def palindrome(num):
    rev = 0
    temp = num
    while num > 0:
        r = num  % 10
        rev = rev * 10 + r
        num = num // 10
    print("Reverse is: ",rev)
    if(temp == rev):
        print(temp," is a palindrome")
    else:
        print(temp," is not a palindrome")

num=int(input("Enter value of number: "))
palindrome(num)

