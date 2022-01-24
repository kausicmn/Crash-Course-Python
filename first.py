from ast import Delete
from queue import Queue


print("Hello World 😃")
print("\"Hello World\"") # escape sequence
x="MN"
y="KN"
C=f"{x} {y}"
print(C)
print("my name is ",C,x)
print(f"Hi {x} {y}")
#n=int(input("Enter the number"))

a=10
if a>5:
    print("greater")
print("done")
s=25
message="eligible" if s>=18 else "non eligible" # ternary operator
print(message)

for i in range(1,4):
    print(i,"*"*i)

for j in "Python":
    print(j)

for k in range(0,10,2):
    print(k)

def sum(n):
    sum=0
    for i in range(0,n+1):
        sum+=i
    return sum
print(sum(5))

def number(*k):
    return k
print(number(1,2,3,4))

l=[1]*10
x=["a","b"]
q=x+l
print(q)
numbers=list(range(10))
char=list("Hello")
print(numbers[::-1])
print(char)
#unpacking a list
first,second,*others=numbers
print(first)
print(second)
print(others)
for index,letter in enumerate(x):
    print(f"{index},{letter}")
#list append insert del pop remove clear
#del x[0:1]
#x.index("a") x.count("a")
list2=[1,2,3]
list2.sort(reverse=True)
print(sorted(list2,reverse=True))
list1=[("a",3),("b",1)]
# def sord(k):
#     return k[1]

list1.sort(key=lambda sord:sord[1])
print(list1)
l=list(map(lambda x:x[1],list1)) 
print("map",l)
v=list(filter(lambda q:q[1]>1,list1))
print(v)
# list comprehension
prices=[item[1] for item in list1]
print("prices",prices)
filters=[item for item in list1 if item[1]>1]
print(filters)
#zip
list3=[1,2,3]
list4=[4,5,6]
l=list(zip("abc",list3,list4))
print(l)

#queue
from collections import deque
queue=deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())
print(queue)

#swap
m=3
n=7
m,n=n,m # n, m is defining a tuple and unpacking it a=1,2 q,w=1,2 
print("m",m)
print("n",n)

#array

from array import array

num=array("i",[1,2,4])
print(num)

#set

list5=[1,1,2,3,5]
list6=set(list5)
set2={1,6}
print(list6|set2) #union 
print(list6&set2) #intersection
print(list6-set2) #differnce
print(list6^set2) # differnce in both non intersection

#dictionary

dict={"x":1,"y":2}  # dict(x=1,y=2) del dict(x)
print(dict)
for key,value in dict.items():
    print(key,value)

values1={x:x**2 for x in range(5)}
print(values1)

#generator object
from sys import getsizeof
values2=(x**2 for x in range(1000)) # reduces memory
print(getsizeof(values2))

#unpacking operator
list7=[1,3,6]
print(*list7) #dictionary **(two)


#exception
# try:
#     file=open("first.py") #with open("first.py")as file
#     age= int(input("enter the number"))
# except (ValueError,ZeroDivisionError) as ex:
#     print("value error")
#     print(ex)
#     print(type(ex))
# else:
#     print("no error")
# finally:
#     file.close()

#class

class Point:

    def __init__(self,k,s): #constructor
        self.k=k
        self.s=s

    @classmethod #creates object 
    def zero(cls):
        return cls(2,3)    
    def __str__(self): # displays the contents of constructor
        return f"{self.k},{self.s}"
        
    def draw(self): #instance method
        print("draw")
        print(f"{self.k},{self.s}")
    
    def __eq__(self,other): #equal to
        return self.k==other.k and self.s==other.s
    def __gt__(self, other): #greater than
        return self.k>other.k and self.s>other.s
    def __add__(self,other): #add two objects
        return Point(self.k+other.k,self.s+other.s)

        

pt=Point(2,3)
pt.draw()
xy=Point.zero()
xy.draw()
combined= pt+xy
print(combined)
print(pt>xy)

#repository