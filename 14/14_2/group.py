class GroupLimitError(Exception):
    pass

class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        try:
            if len(self.group) >= self.MAX_STUDENTS:
                raise GroupLimitError(f'Group {self.number} if full {self.MAX_STUDENTS}!')
            self.group.add(student)
        except GroupLimitError as err:
            print(f'Error: {err}')

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group: {self.number}\n{all_students}'

