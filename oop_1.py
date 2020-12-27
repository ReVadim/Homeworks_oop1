class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rating_lecturer(self, lecturer, course, grade):
        """ Implement the method for the grading of the lecturers """
        if 0 <= grade <= 10:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.rating_grades:
                    lecturer.rating_grades[course] += [grade]
                else:
                    lecturer.rating_grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'Wrong grade, only 0 to 10'

    def __str__(self):
        text = 'Name: ' + self.name + '\nSurname: ' + self.surname
        text += '\nAverage grade for homeworks: ' + find_average_grade(self.grades)
        text += '\nCourse in progress: ' + (','.join(self.courses_in_progress))
        text += '\nFinished courses: ' + (', '.join(self.finished_courses))
        return text

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """ The child class from class Mentor """
    def __init__(self):
        super().__init__(name, surname)
        self.rating_grades = {}


class Reviewer(Mentor):
    """ Another child class from class Mentor """
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'


def find_average_grade(grades):
    total_sum = count = 0
    for value in grades.values():
        for grade in value:
            total_sum += grade
            count += 1
    if count > 0:
        average_grade = total_sum / count
    else:
        average_grade = 0
    return str(round(average_grade, 1))


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['HTML', 'CSS', 'SQL']
best_student.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

print(best_student.grades)
print(best_student)

