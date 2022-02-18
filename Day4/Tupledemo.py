# Example 1: Creating tupple
# mytuple=('apple','banana','cherry',)
# print(mytuple) #('apple', 'banana', 'cherry')
#mytuple=() # empty tuple

# Example 2 access tuple items
# mytuple=('apple','banana','cherry')
# print(mytuple[1]) #banana here index starts from 0
# print(mytuple[-1]) #cherry

#Example3 range of indexes
# mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
# print(mytuple[2:5]) # ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1])

#Example 4 changing tuples items
#by default tuple does not allow  you change value bcoz it is immutable
#but there is work around
#tuple ---> list(modify) ---> tuple

#mytuple= ("apple",'banana','cherry')
# mytuple= ("apple",100,200)
# mylist=list(mytuple)
# mylist[0]= "orange"
# mytuple=tuple(mylist)
# print(mytuple) #('orange', 'banana', 'cherry')

#Example 5 reading tuple items using loop
# mytuple=("apple","banana","cherry")
# for i in mytuple:
#     print(i)

# Example 6 Check if the item exists(searching of items in tuple)
# mytuple=('apple','banana','cherry')
#
# if "banana" in mytuple:
#     print("Yes banana is present ")
# else:
#     print("banana is not present")

# #Example 7 : Tuple length  counting items in a tuple
# mytuple=('apple','banana','cherry')
# print(len(mytuple)) # 8
#
# # Example 8 Add items to the tuple
# mytuple = ('apple','banana','cherry')
# mytuple[0]='orange' #TypeError: 'tuple' object does not support item assignment
# print(mytuple)

#Example 9 copy_tuple
# mytuple1 = ('apple','banana','cherry')
# mytuple2 =mytuple1
# print(mytuple2) # ('apple', 'banana', 'cherry')

#Example 10 : removing items from the tuple
# mytuple=["apple",'banana', 'cherry']
# mytuple.remove("apple") #invalid / It is not possible
# del mytuple
# print(mytuple) # NameError: name 'mytuple' is not defined

#Example 11: join/combine tuple
# tuple1=(10,20,30)
# tuple2=('a','b','c')
#
# tuple3=tuple1+tuple2
# print(tuple3)  #(10, 20, 30, 'a', 'b', 'c')

#Example 12
# tuple1=(10,20,30)
# #tuple2=('a','b','c') #Tuples are not equal
# tuple2=(10,20,30,)
# if tuple1 ==tuple2:
#     print("tuple are equal")
# else:
#     print("Tuples are not equal")



#List comparison
# mylist1=[10,20,30]
# mylist2=[10,200,30,]
#
# if mylist1==mylist2:
#     print("lists are equal")
# else:
#     print("lists are not equal")

