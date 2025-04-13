# f = open("demo.txt", "r")
# data = f.readline()

# print(data)
# # print(type(data))

# line2 = f.readline()
# print(line2)

# line2 = f.readline()
# print(line2)

# f.close()

# f = open("cake2.txt", "a")

# f.write("Black Forest Cake\n")

# f.close()

# f = open("demo.txt", "r+")
# f.write("check")
# print(f.read())

# f.close()

# with open("demo.txt") as f:
#     print(f.read())

# with open("demo.txt", "w") as f:
#     f.write("What you plant now, you will harvest later")

# import os

# os.remove("cake2.txt")

#Create a new file "practice.txt" using python. Add the following data in it:
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")

#WAF  that replace all occurrences of "java" with "python" in above file.

# def replace(data):
#     new_data = data.replace("Java", "Python")
#     with open("practice.txt", "w") as f:
#         f.write(new_data)

     

# with open("practice.txt","r") as f:
#     data = f.read()
#     replace(data)

#Search if the word "learning" exists in the file or not.

# with open("practice.txt","r") as f:
#     data = f.read()
#     search = data.count("learning")
#     print(search)
#     if(search >= 1):
#         print("the word learning exists in the file", "and it occurs", search, "time(s)")
#     else:
#         print("the word learning does not exist in the file")

#solution from instructor
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(word in data):
#             print("found")
#         else:
#             print("not found")

#WAF to find in which line of the file does the word "learning" occur first.
#print -1 if word is not found.
# def check_for_line():
#     with open("practice.txt", "r") as f:
#         for el in range(1, 5):
#             data = f.readline()
#             learning = data.find("learning")
#             if(learning != -1):
#                 print("found on line: ", el)
#             else:
#                 print(learning)

# check_for_line()

#solution from the instructor
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()

#From a file containing numbers separated by comma, print the count of even numbers.

# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)
#     even = 0

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ','):
#             print(num)
#             if(int(num) % 2 == 0):
#                 even += 1
#             num = ""
#         else:
#             num += data[i]
# print("the total count of even numbers is: ", even)

#solution 2 
# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1

# print(count) 