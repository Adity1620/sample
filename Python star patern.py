n = int(input("Enter a number : "))
space = " "
star = "* "
a = n
print()
for i in range(0,n+1):
    for j in range(0,i+1):
        print(space,end="")
    for k in range(0,a+1):
        print(star,end="")
    print()
    a = a - 1
a = n
for i in range(0,n+1):
    for j in range(0,a+1):
        print(space,end="")
    for k in range(0,i+1):
        print(star,end="")
    print()
    a = a - 1
