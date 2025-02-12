# import random
# g=random.randint(1,10)
# user=int(input("gcuss number in range 1-10:"))
# if user==g:
#     print("you are got")
# elif user<g:
#     print("too low")
# else:
#     print("too high")
# print("my name is {fname},i am {age} years old".format(fname="ram",age=21))

# print("my  name is {0},iam {1} old".format("ram",21))

# print("my  name is {},iam {} old".format("ram",21))

# class emoployee():
#     total_employee=0
#     def __init__(self,empname,age,designation,salary):
#         self.empname=empname
#         self.age=age
#         self.designation=designation
#         self.salary=salary
#         emoployee.total_employee=emoployee.total_employee+1

#     def get_emp_details(self):
#         return self.empname,self.age,self.designation,self.salary

#     def update_salary(self,new_salary):
#         self.salary=new_salary
#         print("salary updated")
#         return self.salary

# empONE=emoployee("RAM",21,"HACKER",21000)
# print(empONE.get_emp_details())
# empTWO=emoployee("sowji",23,"web developer",230000)
# print(empTWO.get_emp_details())

# empONE.update_salary(230000)
# print(empONE.get_emp_details())
# print(emoployee.total_employee)

class emoployee():
    total_employee=0
    def __init__(self,empname,age,designation,salary):
        self.empname=empname
        self.age=age
        self.designation=designation
        self.salary=salary
        emoployee.total_employee=emoployee.total_employee+1

    def get_emp_details(self):
        return self.empname,self.age,self.designation,self.salary

    def update_salary(self,new_salary):
        self.salary=new_salary
        print("salary updated")
        return self.salary

class intern(emoployee):
    def __init__(self, empname, age, designation, salary,interperiod):
        super().__init__(empname, age, designation, salary)
        self.interperiod=interperiod

    def get_period(self):
        return f"intership period(in month)is,{self.interperiod}"

# class fresher(emoployee):
#     pass
interone=intern("ram",21,"hacker",23000)
print(interone.get_emp_details())
print(interone.get_period())