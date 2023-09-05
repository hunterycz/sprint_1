'''
Parent Class
'''

import numpy as np


class Student:

    def __init__(self, tuition, interest):
        self.tuition = tuition
        self.interest = interest

    def calculate_amount(self, time_years):
        amount = (
            (self.tuition * (self.interest/100)) * time_years
                ) + self.tuition
        return amount

    def __repr__(self):
        return f'''My tuition is {self.tuition}
                   and interest is {self.interest}%.'''


if __name__ == '__main__':
    program1 = Student(23000, 12)
    print(program1)

'''
Child Class
'''


class BloomTechStudent(Student):

    def __init__(self, current_amount_owed, tuition, interest):
        super().__init__(tuition, interest)
        self.current_amount_owed = current_amount_owed

    def student_generator(self, num_times):
        lst = []
        for i in range(num_times):
            self.current_amount_owed = np.random.randint(100000)
            self.tuition = np.random.randint(100000)
            self.interest = np.random.randint(100)
            lst.append([self.current_amount_owed, self.tuition, self.interest])
        return lst

    def __repr__(self):
        return f'''I currently owe {self.current_amount_owed} \
                   on my student loan.'''


if __name__ == '__main__':
    program1 = BloomTechStudent(24000, 23000, 12)
    print(program1)
    print(program1.student_generator(30))
    program2 = BloomTechStudent(0, 23000, 12)
    print(program2.calculate_amount(1))
