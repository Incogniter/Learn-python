import shelve


class Cgpa:

    def __init__(self, cgpa, gpa):
        self.cgpa = cgpa
        self.gpa = gpa

    def __str__(self):
        gpa = numerator / totalcredits
        self.gpa = gpa
        if sem == 1:
            self.cgpa = gpa
            return f'Your CGPA is {self.cgpa}'
        else:
            self.cgpa = (pcgpa + gpa) / 2
            return f'Your CGPA is {self.cgpa} \nYour GPA is {self.gpa}'


if __name__ == '__main__':
    person = Cgpa('cgpa', 'gpa')
    totalcredits = 0
    grade_point = []
    numerator = 0
    num = 0
    database = shelve.open('database')
    print("Only available for Mechanical,CSE,ECE departments")
    n = input("Enter your department: ")
    if n not in database:
        print("invalid entry")
    else:
        depart = database.get(n)
        sem = int(input("Enter the semester to calculate: "))
        if sem != 1:
            pcgpa = float(input("Enter you previous CGPA: "))
        if sem in depart:
            semester = depart.get(sem)
            SEMESTER = list(semester)
            for values in SEMESTER:
                grades = input(values + " : ")
                key_answer = semester.get(values)
                if grades == "RA":
                    continue
                else:
                    totalcredits += key_answer
                if grades in database:
                    grade = database.get(grades)
                    grade_point.append(grade)
                    for item in grade_point:
                        num = key_answer * item
                    numerator += num
    print(person)
