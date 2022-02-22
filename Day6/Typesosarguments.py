#Example 1:

# def func(i,j):
#     print(i,j)
#
# # func(10,20) #Positional arguments
#
# func(j=20,i=10) #Keyword arguments

# Example2: default value assigned to positional argument
# def func(i,j=10):
#     print(i,j)
#
# func(100,200)
# func(100)

#Example 3: keyword arguments
# def greeting(name,greetmsg):
#     print(greetmsg+" "+name)
#
# greeting(name= "john", greetmsg =" Hello ") # keyword arguments
# greeting(greetmsg="Hello",name="john")

#Example4:
def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30) #Poistional argument
my_func(a=10,b=20,c=30) #Keyword parameters
my_func(b=20,a=10,c=30) #keyword argument

my_func(10,20,c=30)



