class Person:
    def greet(self):
        print("PG")
class X:
    def greet(self):
        print("UG") 
class Y(Person,X):
    pass
    
m=Y()
m.greet() ## first instance is checked