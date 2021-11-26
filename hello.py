print("hi")
num=int(input("Enter a number:"))
#find sum of natural numbers
sum=0
x=0
while x<=num:
    sum+=x
    x=x+1
print('sum of natural numbers',sum)

num=int(input('Enter a number:'))
sum=0
for x in range(1,num+1):
    sum=sum+x
print("sum of natural numbers=",sum)

def findsum(num):
    sum=0
    x=1
    while x<=num:
        sum=sum+x
        x=x+1
    return sum
num = int(input("Enter a number:"))
print("sum of natural numbers=",findsum(num))



