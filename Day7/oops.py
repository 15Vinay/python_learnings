#Example 1:

# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc1= MyClass()
# mc1.myfun()
# mc1.display("scott") #  john

# Example 2
# class MyClass:
#     def m1(self):
#         print("this is instance method.....")
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
# mc=MyClass()
# mc.m1()
# mc.m2(100,200) # 100 200
# MyClass.m2(10,20) #10,20 # here calling static method directly using class not through object

#Example3:

# class MyClass:
#     a,b=10,20 # class variables
#     def add(self): # self is representing the class
#         print(self.a+self.b)
#
#     def mul(self):  # self is representing the class
#         print(self.a*self.b)
#
#
# mc= MyClass()
# mc.add() #30
# mc.mul() #200


#Example 4
# i, j = 15,25 # global variable
# class MyClass:
#     a,b=10,20 # class variable
#     def add(self,x,y):
#         print(x+y)  # x,y are local variable
#         print(self.a+self.b) #a,b are class variables
#         print(i+j) #i, j are global variables
#
# mc=MyClass()
# mc.add(100,200)

#Example 5

a, b = 15,25 # global variable
class MyClass:
    a,b=10,20 # class variable
    def add(self,a,b):
        print(a+b)  # x,y are local variable
        print(self.a+self.b) #a,b are class variables
        print(a+b) #i, j are global variables

mc=MyClass()
mc.add(100,200)


