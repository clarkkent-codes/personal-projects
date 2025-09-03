class Employee:
    def __init__(self, name):
        self.name  = name
        self.salary = 0
    
    # def __str__(self):
    #     return f"{self.name} earns {self.calculate_pay()} PHP"

    def calculate_pay(self):
        return self.salary

class FullTimeEmployee(Employee):
    def __init__(self, name, fixed_rate):
        super().__init__(name)
        self.fixed_rate = fixed_rate

    def calculate_pay(self):
        self.salary = self.fixed_rate
        return self.salary #self.fixed_rate

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, number_of_hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.number_of_hours_worked = number_of_hours_worked

    def calculate_pay(self):
        self.salary = self.hourly_rate * self.number_of_hours_worked
        return self.salary #self.hourly_rate * self.number_of_hours_worked

fulltimeemp1 = FullTimeEmployee("John", 45900)
fulltimeemp2 = FullTimeEmployee("Dean", 68700)
fulltimeemp3 = FullTimeEmployee("Scott", 41700)
partimeemp1 = PartTimeEmployee("Nick", 500, 5)
partimeemp2 = PartTimeEmployee("Jane", 1100, 8)
partimeemp3 = PartTimeEmployee("Tim", 1250, 10)

fulltimeemp1.calculate_pay()
print(fulltimeemp1)
print(fulltimeemp1.name)
print(fulltimeemp1.salary)

fulltimeemp2.calculate_pay()
print(fulltimeemp2.name)
print(fulltimeemp2.salary)

fulltimeemp3.calculate_pay()
print(fulltimeemp3.name)
print(fulltimeemp3.salary)

partimeemp1.calculate_pay()
print(partimeemp1.name)
print(partimeemp1.salary)

partimeemp2.calculate_pay()
print(partimeemp2.name)
print(partimeemp2.salary)

partimeemp3.calculate_pay()
print(partimeemp3.name)
print(partimeemp3.salary)
