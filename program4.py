# # # # collection = {1, 2, 3, 4, "hello", "world", 2, 1, "world"}

# # # # print(collection)
# # # # print(len(collection))

# # # collection = set() #empty set
# # # collection.add(6)
# # # collection.add(9)
# # # collection.add(3)
# # # collection.add(4)
# # # collection.add(5)

# # # print(collection.pop())

# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}

# # print(set1.union(set2))
# # print(set1.intersection(set2))
# # set1.remove(2)
# # set1.pop() 
# # print(set1)

# #Store following word meanings in a python dictionary:

# # dict = {
# #     "table":["a piece of furniture", 
# #     "list of facts & figures"],
# #     "cat" : "a small animal"
# # }

# # print(dict)

# #You are given a list of subjects for students.
# #Assume one classroom is required for 1 subject.
# #How many classrooms are needed by all students.

# subjects = {"python", "java", "C++","python",
#             "javascript","java", "python", "java", "C++","C"}

# classrooms = len(subjects)

# print(classrooms, " classrooms are needed by all students")

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#Start with an empty dictionary & add one by one. 
#Use subject name as key & marks as value.

# dict = {}

# dict["maths"] = int(input("Enter marks of maths: "))
# dict["python"] = int(input("Enter marks of python: "))
# dict["webdev"] = int(input("Enter marks of full-stack webdevelopment: "))

# print(dict)

set = {
    ('int', 9),
    ('float', 9.0)
}
print(set)