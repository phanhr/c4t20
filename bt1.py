from random import randrange
m=randrange(1,100)
n=int(input("Nhap mot so bat ki: "))
if m==n:
    print("hai so bang nhau")
elif m>n:
    print(m)
else:
    print(n)