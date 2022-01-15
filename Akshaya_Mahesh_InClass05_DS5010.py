'''f_name=input("Enter first Name:")
l_name=input("Enter Last Name:")
dob=int(input("Enter Year of Birth:"))
'''
class Student:
    def __init__(self,f_name,l_name,y_o_b):
        self.f_name=f_name
        self.lname=l_name
        self.y_o_b = y_o_b

    def my_name(self):
        print(f_name,l_name,y_o_b)


    def email(self):
        e_Mail= (f_name).lower()+'.'+(l_name).lower()+'@neu.edu'
        return e_Mail
    def __str__(self):
        return print(name,y_o_b,e_Mail)


a=Student('John','Smith',1999)
a.email()
