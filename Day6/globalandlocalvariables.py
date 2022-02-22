# # Example 1
# global_var=20 #global variable
#
# def fun():
#     local_var =10 # local variable
#     print(local_var)
#     print(global_var)
#
# fun()
# #print(locale_var) # invalid bcoz local_var is local variable of fun()
#
# print(global_var) # 20 Valid We can access global variable outside of the function
#


# Example 2 :
# XY =100 # global variable
#
# def cool():
#     xy=200 # local variable
#     print(xy)

#cool() # 200

# Example 3 Using Global variable in local variable and update the value.

# XY =100 # global variable
#
# def cool():
#     global xy=200 # invalid sintex
#     # global xy
#     # xy=200 # global variable
#     print(xy)
#
# cool() # 200
# print(xy)

#Example4:
# x=100
#
# def cool():
#     global x
#     x=500
#     print(x)
#
# #cool()     #500
# print(x)   #500


# #Example 5
# There is no need to declare the global variable outside the function
# You can declare them global inside the function.We have to declare global variable
def cool():
    global x
    x=100
    print(x)

cool()
print(x)  # able to access the function bcoz it is global variable









