# class Student:
#     def studentDetails(self,name,age):
#         print(name,age)
        
# s1=Student()

# s1.studentDetails("Veera",25) 

##Self real usage in python

# class Car:
#     name ="BMW"
#     color="Navy Blue"

#     def speed(self):
#         print(self.name,self.color)
#         print("Speed is 200km/hr")
# c1=Car()
# c1.speed()

# c1 -> {name: "BMW", color: "Navy Blue"}
    
# _int_ is a special method in python which is used to initialize the object of the class. It is called when an object is created. It is also known as constructor.
# _int_ runs autoamtically when an object is created. It is used to initialize the attributes of the class.

# class Car:
#     name ="BMW"
#     color="Navy Blue"

#     def __init__(self):
#         print(self.name,self.color)
#         print("Speed is 200km/hr")
# c1=Car()


# class Car:
#     wheels = 4

#     def __init__(self,name,speed):
#         self.name = name
#         self.speed = speed

        
#     def display(self):
#         print(self.name,self.speed,self.wheels)
# c1 = Car("BMW","200km/hr")
# c1.display()

# # c1 -> {name: "BMW", speed: "200km/hr", wheels: 4 ,display()}

# print("\n")

# c2 = Car("Audi","150km/hr")
# c2.display()


# ***  Encapsulation in python  ***
 
 # Without Encapsulation :
  # Bank -1000
  # Deposit - Money
  #Show Balance

# class Bank:
#         def __init__(self):
#             self.balance = 1000
#         def showBalance(self):
#             print("Balance is:",self.balance)
#         def deposit(self,amount):
#             self.balance += amount
             
# b= Bank()

# b.balance = 5000
# b.showBalance()    

# Task: Encapsulation 
# Create a Student class.

# Requirements:
# 1. Create private variable __marks = anyvalue
# 2. Create show_marks() method.
# 3. Create update_marks(new_marks) method.
# 4. Try modifying marks directly from outside.


class Student:
  def __init__(self):
    self.__marks = 75  
  def show_marks(self):
    print("Marks:", self.__marks)
  def update_marks(self, new_marks):
    self.__marks = new_marks
  
s1 = Student()
s1.show_marks()  
s1.update_marks(85)
s1.show_marks()  

s1.__marks = 90  
s1.show_marks() 

  