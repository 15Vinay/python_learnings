#Example 1 To create a list

# mylist1=[10,20,30,40,50]
# mylist2=['apple', 'banana', 'cherry']
# mylist3=['apple',10,'banana', 20]
# mylist= list() #eMPTY LIST
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

#Example 2 Accessing items from the list
# mylist= ['apple', 'banana', 'cherry'] # Index starts from 0
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

#Example 3 Range of index It do not print last number of the items
# mylist=['apple','banana','cherry','orange','kiwi','melon','mango']
# print(mylist[2:5]) #cherry, orange,kiwi
#
# print(mylist[-4:-1])  #['orange', 'kiwi', 'melon']

#Example 4 change the items
# mylist=['apple','banana','cherry'] # ['apple', 'banana', 'cherry']
# print(mylist)
#
# mylist[0]='orange' #Change the value based on index
# print(mylist) # ['orange', 'banana', 'cherry']

#Example 5 read the items using loop statement
# mylist=['apple','banana','cherry']
#
# for i in mylist:
#     print(i)


# Example 6 check the items is exist in the list
# mylist=['apple','banana','cherry']
#
# if 'apple' in mylist:
#     print("Yes apple is present")
# else:
#     print("NO apple is not present")

#Example 7 : List length(COUNTING NUMBER OF ITEMS IN A LIST)
# mylist=['apple','banana','cherry']
# print(len(mylist)) #3

#eXAMPLE 8: Additems append()    insert()
# mylist =['apple','banana','cherry']
# #mylist.append("orange") #adding new items at the end of the list
#
# mylist.insert(1,"orange") # add items some where in the middle of the list based on the index
# print(mylist) #['apple', 'banana', 'cherry', 'orange']

#Example 9: remove items from the list
#pop()
# mylist=['apple','banana','cherry']
# mylist.pop(0) #here we should specify index not the value
# print(mylist) #['banana', 'cherry']

#del
# mylist=['apple','banana','cherry']
# del mylist[2] #del command removes single items based on the index
#
# print(mylist) #['apple', 'banana']

#clear
# mylist=['apple','banana','cherry']
# mylist.clear()
# print(mylist) #[]

#Example 10 copy list
#list()
# mylist1=['apple','banana','cherry']
# mylist2=list(mylist1)
# print(mylist1) #['apple','banana','cherry']
# print(mylist2) #['apple','banana','cherry']

#copy()
# mylist1=['apple','banana','cherry']
# mylist2=mylist1.copy()
# print(mylist1) #['apple','banana','cherry']
# print(mylist2) #['apple','banana','cherry']

#Example 11 combine/join Lists
#Using  + operator
# list1=['a','b','c']
# list2=[1,2,3]
# list3= list1+list2
# print(list3) #['a', 'b', 'c', 1, 2, 3]

#using loop statement
# list1=['a','b','c']
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1) #['a', 'b', 'c', 1, 2, 3]

#Using extend function
# list1=['a','b','c']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1) #['a', 'b', 'c', 1, 2, 3]

# list1=['a','b','c']
# list2=[1,2,3]
# #list3=[100,200]
# list2.extend(list1)
# print(list2) #['a', 'b', 'c', 1, 2, 3]





