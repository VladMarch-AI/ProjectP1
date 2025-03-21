from human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)


    def __str__(self):
        return (f'{self.first_name} {self.last_name}.'
                f' Age: {self.age}. {self.gender}. Record_book: {self.record_book}.')

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))
