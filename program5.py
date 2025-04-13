# # # # # # # # # # # # # # #infinite loop, always include a eventual false condition
# # # # # # # # # # # # # # while True :
# # # # # # # # # # # # # #     print("Hello")

# # # # # # # # # # # # # # count =  1        #iterator  
# # # # # # # # # # # # # # while count <=5 : #iteration
# # # # # # # # # # # # # #     print(count)
# # # # # # # # # # # # # #     count += 1
    
# # # # # # # # # # # # #     #print numbers from 1 to 100, changed to 100 to 1

# # # # # # # # # # # # # i = 100

# # # # # # # # # # # # # while i >= 1 :
# # # # # # # # # # # # #         print(i)
# # # # # # # # # # # # #         i -= 1

# # # # # # # # # # # # # print("The above numbers are from 100 to 1")

# # # # # # # # # # # # #print the multiplication table of a number n

# # # # # # # # # # # # number = int(input("Enter a number: "))

# # # # # # # # # # # # i = 1

# # # # # # # # # # # # while i <= 10 :
# # # # # # # # # # # #     print(number, "*", i ,"=", number * i)
# # # # # # # # # # # #     i += 1

# # # # # # # # # # # #print the elements of the following list using a loop:

# # # # # # # # # # # list = [1, 4, 9, 25, 49, 81, 100]

# # # # # # # # # # # i = 0

# # # # # # # # # # # while i < len(list) :
# # # # # # # # # # #     print(list[i])
# # # # # # # # # # #     i += 1

# # # # # # # # # # #Search for a number x in this tuple using loop:

# # # # # # # # # # tuple = (1, 4, 9, 16, 36, 49, 81, 100, 1, 1, 1)

# # # # # # # # # # x = int(input("Enter the number to be searched : "))

# # # # # # # # # # i = 0

# # # # # # # # # # while i < len(tuple) : 
    
# # # # # # # # # #     if (x == tuple[i]) :
# # # # # # # # # #         print(x)
    
# # # # # # # # # #     i += 1

# # # # # # # # # #break and continue

# # # # # # # # # i = 1

# # # # # # # # # # while i <= 5 :
# # # # # # # # # #     if (i == 3) : 
# # # # # # # # # #         break
# # # # # # # # # #     else :
# # # # # # # # # #         print(i)
# # # # # # # # # #     i += 1

# # # # # # # # # # print("End of loop.")

# # # # # # # # # while i <= 5 :
# # # # # # # # #     if (i == 3) : 
# # # # # # # # #         i += 1
# # # # # # # # #         continue
# # # # # # # # #     else :
# # # # # # # # #         print(i)
# # # # # # # # #     i += 1

# # # # # # # # # print("End of loop.")

# # # # # # # # #for loop

# # # # # # # # elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# # # # # # # # for el in elements :
# # # # # # # #     print(el)

# # # # # # # #print the elements of the following list using a loop:

# # # # # # # list = [1, 4, 9, 25, 36, 49, 81, 100]

# # # # # # # for el in list :
# # # # # # #     print(el)

# # # # # # #search for a number x in this tuple using loop:

# # # # # # tuple = (1, 4, 16, 25, 49, 64, 81, 100)

# # # # # # x = int(input("Enter a number : "))

# # # # # # for el in tuple :
# # # # # #     if(x == el):
# # # # # #         print("found x")
# # # # # #         break
# # # # # # else:
# # # # # #     print("not found")

# # # # # #Print numbers from 1 to 100 range()

# # # # # for el in range(1, 101) :
# # # # #     print(el)

# # # # # #print numbers from 100 to 1

# # # # # list = []
# # # # # for el in range(1, 101) : #didn't consider the step factor
# # # # #     list.append(el)
# # # # # list.sort(reverse = True)
    
# # # # # for el in list :
# # # # #     print(el)

# # # # for el in range(100, 0, -1) :
# # # #     print(el)

# # # #print the multiplication table of a number n

# # # n = 5

# # # for el in range(1, 11) :
# # #     print(n, " * ", el, " = ", n * el)

# # for el in range(10) :
# #     pass

# #WAP to find the sum of first n numbers using while loop

# n = int(input("Enter a number : "))
# sum = 0

# for el in range(n + 1) : 
#     sum += el

# print("the sum of first n numbers is : ", sum)

# n = int(input("Enter a number : "))
# sum = 0
# i = 0

# while i <= n : 
#     sum += i
#     i += 1  

# print("the sum of first n natural numbers is : ", sum)

#WAP to find the factorial of first n numbers using for loop


# num = int(input("enter a number : "))
# fix = num - 1
# fact = num -1

# for el in range(num, 1, -1) :
#     if (el == fix) :
#         continue
#     fact *= el
# print(fact)

# n = int(input("enter a number : "))
# fact = 1
# i = 1

# while i <= n :
#     fact *= i
#     i += 1

# print(fact) 
# n = int(input("Enter a number : "))
# fact = 1
# for i in range(1, n + 1) :
#     fact *= i

# print(fact)