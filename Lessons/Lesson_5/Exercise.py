class Person:
    pass


if __name__ == "__main__":
    print(Person.format_name_comma("Joe", "Bloggs"))  # prints Bloggs, Joe
    person_one = Person("Joe", "Bloggs", 27)
    print(person_one)  # prints Bloggs, Joe
