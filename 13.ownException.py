class VowelExists(Exception):
    pass

n = int(input("Enter no of names: "))
li = []

try:
    for i in range(n):
        name = input("Entr name: ")
        for i in name:
            if i in 'aeiouAEIOU':
                raise VowelExists
            li.append(name)

except VowelExists:
    print("Vowel Exists")

else:
    print("Names: ")
    for j in li:
        print(j)