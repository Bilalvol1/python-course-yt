# def calcSum(n1, n2) :
#     s = n1 + n2
#     print(s)

# calcSum(4, 19)

# def calSum(a, b) :
#     return a + b

# sum = calSum(3, 5)

# print(sum)

#average of three numbers

# def avg3(a, b, c) :
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)

# avg3(10, 10, 10)

#WAF to print the length of a list. List is the parameter.

# def lenList(lenL) :
#     length = len(lenL)
#     print(length)

# list = [1, 2, 3, 4]

# lenList(list)

#WAF to print the elements of  a list in a single line. List is the parameter.

# list = [1, 2, 3, 4, 5, 10]

# def line(list) :
#     for el in list :
#         print(el, end = " ")

# line(list)
# print()

#WAF to find the factorial of n. n is the parameter.

# def fact(n) :
#     fact = 1

#     for i in range(1, n + 1) :
#         fact *= i
    
#     print(fact)

# fact(7)

#WAF to convert USD to INR

# def toINR(USD) :
#     inr = 87.15 * USD
#     print("INR =", inr)

# toINR(100)

#WAF to check if the given number is odd or even

# def check(number) :
#     if (number % 2 == 0) :
#         print("EVEN")
#     else :
#         print("ODD")

# check(11)

#prints n to 1 backwards

# def show(n) :
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)
#     print("end")

# show(4)

#returns n!

# def fact(n) :
#     if(n == 0 or n == 1) :
#         return 1
#     else :
#         return n * fact(n-1)
    
# print(fact(7))

#Write a recursive function to calculate the sum  

# def sum(n) :
#     sum = 0
#     for el in range(1, n + 1):
#         sum += el
#     print(sum)



# def sum(n):
#     if(n == 0):
#         return 0
#     return sum(n-1) + n


# print(sum(5))

#Write a recursive function to print all elements in a list. 
#Hint: use list & index as parameters

# def print_list(list, idx = 0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx + 1)

# list = [1, 2, 5, 3, 10]

# print_list(list)