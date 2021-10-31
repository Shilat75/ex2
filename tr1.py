
num=int(input("Please enter a 4-digit number:"))
while int (num)<1000 or int (num)>9999:
     print ("This number is invalid Please enter again/n")
     num=int(input("Please enter a 4-digit number:"))
x=num//1000
y=num//100%10
z=num//10%10
t=num%10
print(x+y+z+t)
print(t*1000+z*100+y*10+x)


if x==t and y==z:
    print("it's polindrom")
else:
    print("it's not polindrom")

