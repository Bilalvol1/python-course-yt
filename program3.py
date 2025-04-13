# # #WAP to ask the user to enter names of their three favorite movies and store them in a list
# # movies = [0,1,2]

# # movies[0] = input("enter your first favorite movie: ")
# # movies[1] = input("enter your second favorite movie: ")
# # movies[2] = input("enter your third favorite movie: ")

# # print(movies)

# # #solution 2

# # movies = []
# # movies.append(input("enter first: "))
# # movies.append(input("enter second"))
# # movies.append(input("enter second"))

# # print(movies)

# #WAP  to check if a list contains a palindrome of elements. Hint: use copy()

# list = [1,2,3,2,1]
# copyList = list.copy()
# copyList.reverse()

# if(list == copyList):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# list1 = [1, "abc", "abcd", 1]
# copyList1 = list1.copy()
# copyList1.reverse()

# if(list1 == copyList1):
#     print("Palindrome1")
# else:
#     print("Not a Palindrome1")

#WAP to count the number of students with the A grade in the following tuple. Store the values in a list & sort them from A to D.

grade = ('C','D','A','B','A','B')

gradeA = grade.count('A')

print("The number of students with the A grade are:", gradeA)

list =  ['C','D','A','B','A','B']
list.sort()
print(list)
