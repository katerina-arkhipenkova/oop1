from statistics import mean

student_list = []
lecturer_list = []


def get_average(grades):
    average = 0
    len = 0
    for key, value in grades.items():
        average += mean(value)
        len += 1
    if len == 0:
        average = 0
    else:
        average = average / len
    return average


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {get_average(self.grades):.2f}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return get_average(self.grades) < get_average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {get_average(self.grades):.2f}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            return
        return get_average(self.grades) < get_average(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}"
        return text


def average_for_course(students, course):
    av_for_course = 0
    len = 0
    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            av_for_course += mean(student.grades[course])
            len += 1
    if len == 0:
        av_for_course = 0
    else:
        av_for_course = av_for_course / len
    return av_for_course


def average_for_lecturer(lecturers, course):
    av_for_course = 0
    len = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            av_for_course += mean(lecturer.grades[course])
            len += 1
    if len == 0:
        av_for_course = 0
    else:
        av_for_course = av_for_course / len
    return av_for_course


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.finished_courses += ['HTML']

student2 = Student('Harry', 'Potter', 'your_gender')
student2.courses_in_progress += ['Java']
student2.courses_in_progress += ['HTML']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Java']

lecturer2 = Lecturer('Dolores', 'Ambridge')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['HTML']

reviewer1 = Reviewer('Severus', 'Snape')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['HTML']

reviewer2 = Reviewer('Pomona', 'Sprout')
reviewer2.courses_attached += ['Java']

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)

student2.rate_lecturer(lecturer1, 'Java', 9)
student2.rate_lecturer(lecturer1, 'Java', 7)
student2.rate_lecturer(lecturer1, 'Java', 7)

student2.rate_lecturer(lecturer2, 'HTML', 3)
student2.rate_lecturer(lecturer2, 'HTML', 5)
student2.rate_lecturer(lecturer2, 'HTML', 1)

reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 7)

reviewer2.rate_hw(student1, 'Java', 8)

reviewer2.rate_hw(student2, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 9)

reviewer1.rate_hw(student2, 'HTML', 5)
reviewer1.rate_hw(student2, 'HTML', 8)

student_list += [student1]
student_list += [student2]
lecturer_list += [lecturer1]
lecturer_list += [lecturer2]

print(reviewer1)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)
print(lecturer2 < lecturer1)
print(student1 < student2)

print(f"Средняя оценка студентов за курс Java: {average_for_course(student_list, 'Java'):.2f}")
print(f"Средняя оценка студентов за курс Python: {average_for_course(student_list, 'Python'):.2f}")
print(f"Средняя оценка студентов за курс HTML: {average_for_course(student_list, 'HTML'):.2f}")

print(f"Средняя оценка лекторов за курс Java: {average_for_lecturer(lecturer_list, 'Java'):.2f}")
print(f"Средняя оценка лекторов за курс Python: {average_for_lecturer(lecturer_list, 'Python'):.2f}")
print(f"Средняя оценка лекторов за курс HTML: {average_for_lecturer(lecturer_list, 'HTML'):.2f}")
