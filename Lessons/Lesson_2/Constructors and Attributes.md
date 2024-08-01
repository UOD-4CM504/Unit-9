# Constructors and Attributes

## 1. Constructors

Constructors are a special method that you can define that is called when you first create an instance of a class. In Python it is given the name ``__init__()`` (for initialise the object), again we put the word ``self`` as the first parameter.

```python
class Pet:
    """ A pet class """
    def __init__(self):
        print("Creating a new pet")

    def talk(self):
        print("Hi, I am an instance of pet")

if __name__ == "__main__":
    # create an instance of Pet, which will invoke the constructor
    pet_one = Pet()
    # create another instance of Pet, which will invoke the constructor
    pet_two = Pet()
    pet_one.talk()
    pet_two.talk()
```

```
Creating a new pet
Creating a new pet
Hi, I am an instance of pet
Hi, I am an instance of pet
```

OK, again that is all very nice, but why!?

<div style="page-break-after:always"></div>

## 2. Attributes
Attributes are names (variables) that we can define in classes, this is where the real power starts to show.

It allows us to create instances of the ``class`` with different data for the attributes. Hence we can now have different instances (objects) of ``Pet`` that have different names.

### 2.1 Initialising Attributes

We do this by creating a name attribute that our constructor ``__init__()`` takes as a parameter and then sets for the instance of the class using ``self``.

It is key to note the use of ``self``. In both ``__init__()`` and ``talk()`` it is the first parameter. You don't have to call it ``self``, but it is convention.

``self`` gives us access to the data for the given instance. That is ``self.name`` contains different data for the instance ``pet_one`` and the instance ``pet_two``.

The ``class`` now looks as follows:

```python
class Pet:
    """ A pet class """
    # take 1 parameter into the constructor - name
    def __init__(self, name):
        print("Creating a new pet")
        # set the instance attribute to the one passed into the constructor
        self.name = name 

    def talk(self):
        """ An instance method that says hi """
        print(f"Hi, my name is {self.name}")

if __name__ == "__main__":
    # create an instance of Pet, which will invoke the constructor
    pet_one = Pet("Fidget")
    # create another instance of Pet, which will invoke the constructor
    pet_two = Pet("Rex")
    pet_one.talk()
    pet_two.talk()
```

This now prints out:

```
Creating a new pet
Creating a new pet
Hi, my name is Fidget
Hi, my name is Rex
```

We can extend this so that our pets have an age.

```python
class Pet:
    """ A pet class """
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def talk(self):
        """ An instance method that says hi """
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
    pet_one = Pet("Fidget", 12)
    pet_two = Pet("Rex", 5)
    pet_one.talk()
    pet_two.talk()
```
Prints out:
```
Hi, my name is Fidget and I am 12 years old.
Hi, my name is Rex and I am 5 years old.
```

### 2.2 Keyword Attributes

We can also add attributes that have a default value by using a keyword argument in our constructor ``__init__()``. 

Here we add an attribute for the number of legs a ``Pet`` has. We will assume a ``Pet`` has ``4`` legs unless overridden.

```python
class Pet:
    """ A pet class """
    def __init__(self, name, age, no_legs=4):
        self.name = name
        self.age = age 
        self.no_legs = no_legs

    def talk(self):
        """ An instance method that says hi """
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
        print(f"I have {self.no_legs} legs.")

if __name__ == "__main__":
    pet_one = Pet("Fidget", 12)
    pet_two = Pet("Cuckoo", 5, 2)
    pet_one.talk()
    pet_two.talk()
```
Prints out:
```
Hi, my name is Fidget and I am 12 years old.
I have 4 legs.
Hi, my name is Cuckoo and I am 5 years old.
I have 2 legs.
```

### 2.3 Accessing Attributes

We can also access the name and age via the class instance (object).

```python
print(pet_one.name) # prints Fidget
print(pet_one.age)  # prints 12
```

### 2.4 Editing Attributes

All attributes are public in Python and can be changed. We will talk about how to make something private later (in Python it is more obfuscated and not really private).

Here we amend the ``age`` attribute of ``pet_one``.

```python
class Pet:
    """ A pet class """
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def talk(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
    pet_one = Pet("Fidget", 12)
    pet_one.talk()
    pet_one.age = 13
    pet_one.talk()
```

```
Hi, my name is Fidget and I am 12 years old.
Hi, my name is Fidget and I am 13 years old.
```

# === TASK ===

Create a class called ``Book``.

Your class should have the following attributes:

| Attribute Name | Description |
| -- | -- |
| ``title`` | Title of the book|
| ``author`` | Author of the book|
| ``price`` | Price  of the book|

And optional parameters:

| Attribute Name | Description | Default Value |
| -- | -- | -- |
| ``no_pages`` | Number of pages in the book | ``None`` |
| ``year`` | Year first published | ``None`` |

It should also have a method called ``description()`` - HINT: Remember ``self``.

When called, ``description()`` should return the description.

Here is an example of how ``Book`` should work.

### Example 1

```python
book_one = Book("1984", "George Orwell", 6.99)
print(book_one.description()) 
```

Should print:

```
Title: 1984
Author: George Orwell
Price: £6.99
```
### Example 2
```python
book_one = Book("1984", "George Orwell", 6.99, no_pages=328)
print(book_one.description()) 
```

Should print:

```
Title: 1984
Author: George Orwell
Price: £6.99
No. of Pages: 328
```
### Example 3
```python
book_one = Book("1984", "George Orwell", 6.99, year=1949)
print(book_one.description()) 
```

Should print:

```
Title: 1984
Author: George Orwell
Price: £6.99
Year Published: 1949
```
### Example 4
```python
book_one = Book("1984", "George Orwell", 6.99, no_pages=328, year=1949)
print(book_one.description()) 
```

Should print:

```
Title: 1984
Author: George Orwell
Price: £6.99
Year Published: 1949
No. of Pages: 328
```