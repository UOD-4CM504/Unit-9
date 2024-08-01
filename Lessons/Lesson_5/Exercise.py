class Person:
    def __init__(self, first_name, surname, age):
        self.first_name = first_name
        self.surname = surname
        self.age = age

    def __str__(self):
        return Person.format_name_comma(self.first_name, self.surname)

    @staticmethod
    def format_name_comma(first_name, surname):
        return f"{surname}, {first_name}"


if __name__ == "__main__":
    print(Person.format_name_comma("Joe", "Bloggs"))  # prints Bloggs, Joe
    person_one = Person("Joe", "Bloggs", 27)
    print(person_one)  # prints Bloggs, Joe
