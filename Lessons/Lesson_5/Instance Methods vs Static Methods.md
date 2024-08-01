# Instance Methods vs Static Methods

To date we have been using instance methods, these methods are bound to an instance of a class (object) and can access the attributes attached to that instance.

In this lesson, we will take a look at another type, static methods.

# Instance Methods

Instance methods are methods that are bound to a given instance of a class (object) and therefore have access to the instance data, the data attached to ``self``.

The first parameter, by convention, should be ``self`` which is a reference to the instance.

For example,

```python
class Pet:
  """ A pet class """

  def __init__(self, name, age):
    ## instance attributes
    self.name = name
    self.age = age

  # instance method, self should be the first parameter
  def talk(self):
    print(f"Hi, my name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
  pet_one = Pet("Fidget", 17)
  pet_one.talk()
```

will print out:
```
Hi, my name is Fidget and I am 17 years old.
```

We can also have other parameters in a method, but ``self`` is still the first parameter. For example, we can add another parameter ``n`` to ``talk()``, this will actually be the first parameter of the method call.

For example,
```python
class Pet:
  """ A pet class """

  def __init__(self, name, age):
    ## instance attributes
    self.name = name
    self.age = age

  # instance method, self should be the first parameter
  def talk(self, n):
    for _ in range(n):
      print(f"Hi, my name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
  pet_one = Pet("Fidget", 17)
  pet_one.talk(3) # call the method pet_one with n=3
```
will print out:
```
Hi, my name is Fidget and I am 17 years old.
Hi, my name is Fidget and I am 17 years old.
Hi, my name is Fidget and I am 17 years old.
```

We say ``talk()`` takes 1 parameter, ``self`` is not included.


# Static Methods

A static method is a method that does not have access to the instance attributes, but it can access a class attribute (read-only). It is bound to the class. **Therefore, we do not need an instance of the class to use the method**

Here we have a single class attribute ``no_pets`` that tracks the number of pets (instances) of ``Pet`` created. We also create a static method called ``print_no_pets``, which uses the class attribute.

```python
class Pet:
  """ A pet class """
  # define a class attribute
  no_pets = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age
    # increment class attribute by 1
    Pet.no_pets += 1

  @staticmethod
  def print_no_pets():
    print(f"There are {Pet.no_pets} pets.")

if __name__ == "__main__":
  # call the static method on the class
  Pet.print_no_pets() # prints There are 0 pets.
  pet_one = Pet("Fidget", 12)
  pet_two = Pet("Rex", 5)
  pet_three = Pet("Indie", 7)
  # call the static method on the class
  Pet.print_no_pets() # prints There are 3 pets.
  # call the static method via the instance 
  pet_one.print_no_pets() # prints There are 3 pets.
```

You will notice that we have used the decorator ``@staticmethod``. This tells the method that the first parameter should not be treated as the instance reference (normally  ``self``).

We also did not need an instance of the class to call the method, but we could also call the method using an instance. This is the same as with class attributes, please read the part about instance and class namespaces in the Class Attribute lesson.

Here is another example of a ``Mathematics`` class, normally we would do this as a module in Python, but in other languages such as Java and C#, classes like this with static methods are quite common. Normally referred to as a utility (helper) class.

It is also a pretty useless class as all of these are built into Python.

The point is we do not need an instance of the class to use it!

```python
class Mathematics:
  @staticmethod
  def add(x,y):
    return x + y
  
  @staticmethod
  def sub(x,y):
    return x - y

  @staticmethod
  def pow(x,n):
    return x**n

if __name__ == "__main__":
  print(Mathematics.add(10,5)) # prints 15
  print(Mathematics.sub(10,5)) # prints 5
  print(Mathematics.pow(10,3)) # prints 100
```


# === TASK ===

Create a class called ``Person``. This should have a ``first_name``, ``surname`` and ``age`` attribute.

Create a static method called ``format_name_comma()``. The reason we want this to be static is we can imagine that it has a use even when we don't have an instance of the class.

You should be able to invoke ``format_name_comma()`` as follows:

```python
print(Person.format_name_comma("Joe", "Bloggs")) # prints Bloggs, Joe
```

You should also implement the ``__str__()`` method which should return the formatted name using the instance attributes ``first_name`` and ``surname``. Really you should reuse the static method ``format_name_comma()`` from within ``__str__()``.

You should then be able to run the following code.

```python
person_one = Person("Joe", "Bloggs", 27)
print(person_one) # prints Bloggs, Joe
```

## Getting Started

You can copy and paste the following into **main.py** to get started.

```python
class Person:
  pass

if __name__ == "__main__":
  print(Person.format_name_comma("Joe", "Bloggs")) # prints Bloggs, Joe
  person_one = Person("Joe", "Bloggs", 27)
  print(person_one) # prints Bloggs, Joe
```