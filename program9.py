# class Student():
#     def __init__(self, name):
#         self.name = name

# s1 = Student("afo")
# print(s1.name)
# print(s1)
# del s1.name
# del s1
# print(s1.name)
# print(s1)

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())
    
# class Car: 
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start(   )

# class A:
#     varA = "Welcome to class A"

# class B: 
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# C = C()
# print(C.varC)
# print(C.varA)
# print(C.varB)

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("started..")

# class ToyotaCar(Car):
#     def __init__(self, type):
#         super().__init__(type)
#         super().start()


# car1 = ToyotaCar("electric")
# print(car1.type)

class Person:
    name = "anonymous"

    # def changeName(self, name):
        # Person.name = name
        # self.__class__.name = "Izuku"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Izuku Midoriya")
print(p1.name)
print(Person.name)