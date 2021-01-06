students = []
courses = []
all_lecturer = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)
        courses.append(self.finished_courses)
        courses.append(self.courses_in_progress)

    def __lt__(self, other):
        if average_grade(self.grades) < average_grade(other.grades):
            return 'The best result is ' + other.name + ' ' + other.surname + ' with a rating ' +\
                   average_grade(other.grades)
        elif average_grade(self.grades) == average_grade(other.grades):
            return 'the same result'
        else:
            return 'The best result is ' + self.name + ' ' + self.surname + ' with a rating ' +\
                   average_grade(self.grades)

    def rating_lecturer(self, lecturer, course, grade):
        """ Implement the method for the grading of the lecturers """
        if 0 <= grade <= 10:
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.rating_grades:
                    lecturer.rating_grades[course] += [grade]
                else:
                    lecturer.rating_grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'Wrong grade, only 0 to 10'

    def __str__(self):
        text = '\nStudent ' + '\nName: ' + self.name + '\nSurname: ' + self.surname
        text += '\nAverage grade for homeworks: ' + average_grade(self.grades)
        text += '\nCourse in progress: ' + (','.join(self.courses_in_progress))
        text += '\nFinished courses: ' + (', '.join(self.finished_courses))
        return text


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __repr__(self):
        return self.name + ' ' + self.surname + ' courses attached: ' + repr(self.courses_attached)


class Lecturer(Mentor):
    """ The child class from class Mentor """

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating_grades = {}
        all_lecturer.append(self)

    def __str__(self):
        text = '\nYour Lecturer' + '\nName: ' + self.name + '\nSurname: ' + self.surname
        text += '\nAverage grade for lectures: ' + average_grade(self.rating_grades)
        return text

    def __lt__(self, other):
        if average_grade(self.rating_grades) < average_grade(other.rating_grades):
            return 'The best result is ' + other.name + ' ' + other.surname + ' with a rating ' +\
                   average_grade(other.rating_grades)
        elif average_grade(self.rating_grades) == average_grade(other.rating_grades):
            return 'the same result'
        else:
            return 'The best result is ' + self.name + ' ' + self.surname + ' with a rating ' +\
                   average_grade(self.rating_grades)


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

    def __str__(self):
        text = '\nYour Reviewer' + '\nName: ' + self.name + '\nSurname: ' + self.surname
        return text


def average_grade(some_grades):
    """ Find the average value from the list """
    all_grades = []
    for subject, grades in some_grades.items():
        for grade in grades:
            all_grades.append(grade)
    if len(all_grades) == 0:
        av_grade = 0
        return str(av_grade)
    elif len(all_grades) > 0:
        av_grade = round((sum(all_grades) / len(all_grades)), 1)
        return str(av_grade)
    else:
        return "error"


def average_course(course, lists):
    """ find the average grade of all students in the selected course """
    grade = []
    for value in lists:
        if course in (sum(courses, [])):
            if course in value.grades:
                for x, y in value.grades.items():
                    if course == x:
                        grade.extend(y)
                    elif course != x:
                        continue
        else:
            return f"the {course} course does not exist"
    if len(grade) != 0:
        result = round((sum(grade) / len(grade)), 1)
        return f"the {course} course has an average grade {str(result)}"
    elif len(grade) == 0:
        return f"the {course} course has no any grades"
    else:
        return 'impossible value'


def lecturer_average_grade(course, lists):
    lect_av_grade = []
    for value in lists:
        if course in (sum(courses, [])):
            if course in value.rating_grades:
                for x, y in value.rating_grades.items():
                    if course == x:
                        lect_av_grade.append(y)
                    elif course != x:
                        continue
        else:
            return f"the {course} course does not exist"
    if len(lect_av_grade) != 0:
        result = round((sum(sum(lect_av_grade, [])) / len(sum(lect_av_grade, []))), 1)
        return f"the {course} course has an average grade {str(result)}"
    elif len(lect_av_grade) == 0:
        return f"the {course} course has no any grades"
    else:
        return 'impossible value'


some_lecturer = Lecturer('Jonh', 'Smith')
new_lecturer = Lecturer('Yan', 'Dex')
best_lecturer = Lecturer('Bill', 'Gates')
ordinary_student = Student('Max', 'Frai', 'm')
best_student = Student('Ruoy', 'Eman', 'your_gender')
cool_reviewer = Reviewer('Isaak', 'Newton')
some_reviewer = Reviewer('Albert', 'Gor')


ordinary_student.courses_in_progress += ['Python', 'Java', 'Django', 'CSS', 'HTML']
best_student.courses_in_progress += ['Python', 'Git', 'c++']

new_lecturer.courses_attached += ['Python', 'Git', 'CSS', 'HTML']
some_lecturer.courses_attached += ['Python', 'Git', 'CSS']
best_lecturer.courses_attached += ['Python', 'Git', 'CSS', 'HTML']
some_reviewer.courses_attached += ['Python', 'Git', 'CSS']
cool_reviewer.courses_attached += ['Python', 'CSS']

ordinary_student.rating_lecturer(some_lecturer, 'Python', 8)
ordinary_student.rating_lecturer(new_lecturer, 'Python', 10)
best_student.rating_lecturer(some_lecturer, 'Python', 10)
best_student.rating_lecturer(some_lecturer, 'Git', 10)
ordinary_student.rating_lecturer(best_lecturer, 'HTML', 10)

ordinary_student.finished_courses += ['HTML', 'c++', 'notepad']
best_student.finished_courses += ['HTML', 'CSS', 'SQL']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(ordinary_student, 'Python', 9)
some_reviewer.rate_hw(ordinary_student, 'Python', 8)
cool_reviewer.rate_hw(ordinary_student, 'HTML', 2)
cool_reviewer.rate_hw(ordinary_student, 'CSS', 8)
some_reviewer.rate_hw(ordinary_student, 'CSS', 10)
some_reviewer.rate_hw(best_student, 'Git', 7)

""" testing area, remove # """
# print(f"{some_lecturer.name} {some_lecturer.surname} rating is: ", average_grade(some_lecturer.rating_grades))
# print(cool_reviewer)
# print(repr(cool_reviewer))
# print(some_lecturer)
# print(some_lecturer.rating_grades)
# print(best_student)
# print(ordinary_student)
# print(average_course('HTML', students))
# print(average_course('Python', students))
# print(average_course('Math', students))
# print(average_course('Git', students))
# print(average_course('CSS', students))
# print(lecturer_average_grade('HTML', all_lecturer))
# print(lecturer_average_grade('Python', all_lecturer))
# print(lecturer_average_grade('CSS', all_lecturer))
# print(lecturer_average_grade('Piano', all_lecturer))
# print(repr(cool_reviewer)) # __repr__ function for class Mentor
# print(cool_reviewer)
# print(best_student.__lt__(ordinary_student))
# print(best_lecturer.__lt__(new_lecturer))
# print(best_lecturer.__lt__(some_lecturer))
# print(best_student > ordinary_student)  # after __lt__ method same that print(best_student.__lt__(ordinary_student))
# print(best_lecturer < new_lecturer)  # after __lt__ method same that print(best_lecturer.__lt__(new_lecturer))
# print(best_lecturer < some_lecturer)  # after __lt__ method same that print(best_lecturer.__lt__(some_lecturer))
