# class Student:
#     name = "karan"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     brand = "Mercedes"
#     color = "blue"

# car2 = Car()
# print(car2.brand)
# print(car2.color)

# class Students:
#     college_name = "abc college"
#     name1 = "anonymous"
#     def __init__(self, name, marks):
#         print("Adding new student in Database.. ")
#         self.name = name
#         self.marks = marks

# s1 = Students("Deku", 100)
# print(s1.name, s1.marks, s1.college_name)


# s2 = Students("Kacchan", 100)
# print(s2.name, s2.marks, s2.college_name)

# s3 = Students("Bruce", 100)
# print(s3.name1, s3.marks, s3.college_name)

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

#     def hello(self):
#         print("hello", self.name)

# s1 = Student("karan")
# s1.hello()

#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

# class Student:
#     def __init__(self, name, TOP, DSA, Python):
#         self.name = name
#         self.TOP = TOP
#         self.DSA = DSA
#         self.Python = Python

#     def average(self):
#         print("The average of", self.name, "is :", (self.TOP + self.DSA + self.Python)/3)

# s1 = Student("Rin", 100, 100, 100)
# s1.average()

# s1 = Student("Kiki", 100, 100, 100)
# s1.average()

# s1 = Student("NON", 100, 100, 100)
# s1.average()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your average score is: ", sum/3)

#     @staticmethod
#     def printhello():
#         print("hello")

# s1 = Student("Deku", [100, 100, 100])
# s1.get_avg()

# s1.name = "Izuku"
# s1.get_avg()

# s1.printhello()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")

# car1 = Car()
# car1.start()

#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(100000, 34155839)
# print(acc1.balance)
# print(acc1.account_no)
# acc1.credit(1000)
# acc1.debit(5000)
# acc1.get_balance()

