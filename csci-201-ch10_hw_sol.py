class Employee:
    number_of_employees = 0

    def __init__(self, fn, ln):
        self.first = fn
        self.last = ln
        self.rate = 0
        self.hours = 0
        Employee.number_of_employees += 1


    def __str__(self):
        return "{} {} makes ${}/hr and worked {} hours for a total of ${}".format(self.first,self.last,self.rate,self.hours,self.getGross())

    def getRate(self):
        return self.rate

    def setRate(self,rate):
        if rate < 8.25:
            self_rate = 8.25
        else:
            self.rate = rate

    def getHours(self):
        return self.rate

    def setHours(self,hr):
        if hr < 0:
            self.hours = 0
        else:
            self.hours = hr

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def getGross(self):
        return self.rate * self.hours

    def getNet(self):
        gross = self.getGross()
        return gross - (gross * .2) - (gross * .05) - (gross * .075)

    

emp1 = Employee('John', 'Doe')
emp1.setRate(10.75)
emp1.setHours(40)

emp2 = Employee('Jane','Doe')
emp2.setRate(20.25)
emp2.setHours(-32)
print("There are {} employees".format(Employee.number_of_employees))

print("\nEmployee 1 Info:\n===============================================================")
print(emp1)
print("Employee 1's net pay is", emp1.getNet())
print(emp1.__dict__)
emp1.dept = "IT"
print(emp1.__dict__)


print("\nEmployee 2 Info:\n==============================================================")
print(emp2)
print("Employee 2's net pay is", emp2.getNet())
print(emp2.__dict__)






    
    



    
