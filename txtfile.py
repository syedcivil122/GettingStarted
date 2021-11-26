with open("hello.txt",'w')as f:
    f.write("Python is Easy")
    f.write("welcome to \n")
    f.write("wscube tech \n\n")
    f.write("jhodpur")

lines=('welcome','to','wscube','tech')
with open('name.txt','w')as f:
    f.writelines("%s\n" % l for l in lines )

f=["orange\n","banana\n","apple\n"]
a=open('hi.txt','a+')
a.writelines(f)
a.close()

f=open("hi.txt",'r')
a=f.read(5)
#print(a)
b=f.read(4)
#print(b)
c=f.read()
#print(c)
d=f.read()
#print(d)

with open('hello.txt','r')as f:
    a=f.readline()
    print(a)
    b=f.readline()
    print(b)