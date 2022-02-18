#Example 1 : How to create a set
# myset={'apple','banana','cherry'}
# print(myset) #{'banana', 'cherry', 'apple'}


#Example 2: Access items from set
# myset={'apple','banana','cherry'}
# for i in myset:
#     print(i)

#Example 3:Value exist inset or not
# myset={'banana', 'cherry', 'apple'}
# print("banana" in myset ) #True
# print("banana2" in myset) #False



#Example 4: Adding items to set.
#add() add single item at a time.  update() add multiple items
# myset={'apple','banana','cherry'}
# myset.add("orange")
# print(myset) # {'banana', 'orange', 'cherry', 'apple'}

#update()
# myset={'apple','banana','cherry'}
# myset.update(['mango','grapes'])
# print(myset) # {'banana', 'cherry', 'apple', 'grapes', 'mango'}

#Example 5: find number of sets in a set
# myset={'apple','banana','cherry'}
# print(len(myset)) #3

#Example 6 Remove items for set - remove() discard()
# myset= {'apple','banana','cherry'}
# # myset.remove("banana")
# # print(myset) #{'cherry', 'apple'}
# # myset.remove("xyz") # KeyError: 'xyz'
#
# myset.discard("banana")
# print(myset) # {'apple', 'cherry'}
# myset.discard("xyz") #Not throw key error

#Example 7: Clear all the items
# myset= {'apple','banana','cherry'}
# myset.clear()
# print(myset)
# # set()
# del myset
# print(myset)  # NameError: name 'myset' is not defined


#Example 8 :JOin two sets - union()
# set1={'a','b','c'}
# set2={1,2,3,}
# set3= set1.union(set2)
# print(set3) # {1, 2, 3, 'c', 'b', 'a'}

#update
set1={'a','b','c'}
set2={1,2,3,}
set1.update(set2)
print(set1) # {1, 2, 3, 'c', 'a', 'b'}
