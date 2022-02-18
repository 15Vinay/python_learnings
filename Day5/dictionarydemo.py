#Example 1: Creating disctionary
# mydic={101,"x",102,"y",103,"z"}
# print(mydic) #{'x', 101, 102, 103, 'y', 'z'}


#Example2: Access items from dictionary
# mydic ={
#     "brand": "Hyundai",
#     "model": "i10",
#     "year":   2021,
# }
# print(mydic["brand"]) # Hyundai
# print(mydic["model"]) #i10
#
# #Using get ()
# x= mydic.get("brand") #i10
# print(x)
# print(mydic.get("brand"))

#Example 3:

# mydic={
#         "brand": "Hyundai",
#         "model": "i10",
#         "year": 2020
# }
# print(mydic)
# mydic["year"]=2021
# print(mydic)

#Example 4: using items from dictionary using loop
# mydic={
#     "brand": "hyundai",
#     "model": " i10",
#     "year" : 2021
# }
# for i in mydic:
#    print(i) # It will only return key.
#
#    for i in mydic:
#     print(mydic[i]) # It will only return values.

#
# for i in mydic.values():
#     print(i) # prints only values from dictionery
#
# for x,y in mydic.items():
#     print(x,y) #print keys along with the values

# Example 5: Check key is exist in dictionary or not

# mydic={
#     "brand": "hyundai",
#     "model": "i10",
#     "year": 2020
#  }
# # if "model" in mydic:
# #     print("exist") #True
# # else:
# #     print("not exist")
#
# print("model" in mydic)

# mydic={ "brand": "hyundai",
#         "model": "i10",
#         "year": 2020
# }
# print(len(mydic)) #3

#Example 7 Adding items to dictionary

# mydic={
#         "brand": "hyundai",
#          "model": "i10",
#          "year": 2020
#  }
# mydic["color"]="red"
# print(mydic) #  {'brand': 'hyundai', 'model': 'i10', 'year': 2020, 'color': 'red'}
#
# mydic={
#     "brand": "hyundai",
#     "model": "i10",
#     "year": 2020
# }
# # mydic.pop("year")
# # print(mydic) # {'brand': 'hyundai', 'model': 'i10'}
#
# # del mydic["year"]
# # print(mydic)
#
# # del mydic
# # print(mydic) #NameError: name 'mydic' is not defined
#
# mydic.clear()
# print(mydic) #{}

#Example 9 copying dictionary
mydic1={
    "brand": "hyundai",
    "model": "i10",
    "year": 2020
}
#with using copy function
mydic2=mydic1.copy()
print(mydic1)

#without using copy function
# mydic2=mydic1
# print(mydic2) # {'brand': 'hyundai', 'model': 'i10', 'year': 2020}




