# # # # # # str1 = "hello"
# # # # # # len1 = len(str1)

# # # # # # print(len1)

# # # # # # str2 = "deku"
# # # # # # len2 = len(str2)

# # # # # # print(len2)

# # # # # # finalString = str1+ " " + str2
# # # # # # lenFinal = len(finalString)

# # # # # # print(lenFinal)
# # # # # # print(finalString)

# # # # # #slicing

# # # # # str = "apna college"
# # # # # print(str[:4])
# # # # # print(str[ :len(str)])
# # # # # print(str[5: ])

# # # # #WAP to input user's first name & print it's length

# # # # firstName = input("Enter your first name: ") 

# # # # print(len(firstName))   

# # # #WAP to find occurrences of '$' in a string

# # # str = "Hello, do you have $$$$"

# # # print("the occurrences of '$' in the string is: ",  str.count("$"))

# # #WAP to check if a number entered by the user is odd or even

# # number = int(input("Enter a number: ")) % 2

# # if (number == 0):
# #     print("even")
# # else:
# #     print("odd")

# #WAP to find the greatest of three numbers entered by the user

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
# n4 = int(input("Enter fourth number: "))

# if(n1 > n2 and n1 > n3 and n1 > n4):
#     print("The greatest of three numbers is: ", n1)
# elif(n2 > n3 and n2 > n4):
#     print("The greatest of three numbers is: ", n2)
# elif(n3 > n4):
#     print("The greatest of three numbers is: ", n3)
# else:
#     print("The greatest of three numbers is: ", n4)

#WAP to check if a number is a multiple of 7 or not

number = int(input("enter a number: ")) % 7

if (number == 0):
    print("The entered number is a multiple of 7")
else:
    print("The entered number is not a multiple of 7")