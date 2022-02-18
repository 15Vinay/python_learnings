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

# Example 3
XY =100 # global variable

def cool():
    xy=200 # local variable
    print(xy)

cool() # 200
