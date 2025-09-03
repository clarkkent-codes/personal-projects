class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, *scores):
        for score in scores:
            self.grades.append(score)
        
        print("Grades: ", end='')
        print(*self.grades, sep=", ") #printing without brackets and then separating each grade with a comma

    def get_average(self):
        total = 0
        if len(self.grades) == 0:
            print("No grades available.")
            return

        for grade in self.grades:
            total += grade
            average = total / len(self.grades)
            average = round(average, 2)
        
        print(f"Average: {average}")

student1 = Student('Sample Name', 22)
student1.add_grade(90, 85, 88, 92, 76, 95, 89)
student1.get_average()