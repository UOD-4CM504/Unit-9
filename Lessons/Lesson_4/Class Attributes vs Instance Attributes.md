## Class Attributes vs Instance Attributes

So far our attributes have belonged to the instance of a class (object).

We can do something else and make an attribute that belongs to the class (type) itself.


## 1. Instance Attributes
Instance attributes are those that belong to the instance of a class (object). An instance attribute is attached to the instance, by convention, using the word ``self``.

There are used to access the data within a given instance of the class.

You will also hear them referred to as member variables or member fields, especially in other languages. 

For example:

```python
class Pet:
  """ A pet class """

  def __init__(self, name, age):
    self.name = name
    self.age = age

if __name__ == "__main__":
  pet_one = Pet("Fidget", 12)
  pet_two = Pet("Rex", 5)

  # access the pet_one instance attribute name
  print(pet_one.name)  # prints Fidget
  print(vars(pet_one)) # print pet_one instance attributes
  print(vars(pet_two)) # print pet_two instance attributes
```
Prints out:
```
Fidget
{'name': 'Fidget', 'age': 12}
{'name': 'Rex', 'age': 5}
```

You will notice that we printed out ``vars(pet_one)`` and ``vars(pet_two)``.

``vars()`` returns the ``__dict__`` (dictionary mapping) attribute of the given object. ``__dict__`` is a dictionary that stores the attributes associated with the instance of the class (object). So ``pet_one.__dict__`` stores the attributes associated with ``pet_one`` and ``pet_two.__dict__`` stores the attributes associated with ``pet_two``.

You can see that both contain ``name`` and ``age`` but they have different data because they are separate instances of the class ``Pet``.

## 2. Class Attributes

As well as having attributes that belong to instances of the class, we can also have attributes that belong to the class.

This simple example now defines a ``no_pets`` attribute that belongs to the class, it will track how many instances have been created, i.e. the number of pets.

Notice that it is not attached using ``self``. 

```python
class Pet:
  """ A pet class """
  # define a class variable
  no_pets = 0  # number of pets

  def __init__(self, name, age):
    self.name = name
    self.age = age
    # increment class attribute by 1
    Pet.no_pets += 1


if __name__ == "__main__":
  pet_one = Pet("Fidget", 12)
  pet_two = Pet("Rex", 5)

  # access the class attribute directly
  print(Pet.no_pets)  # prints 2

  pet_three = Pet("Indie", 7)

  # access the class attribute via instance
  print(pet_one.no_pets) # prints 3
  print(pet_two.no_pets) # prints 3
  # access the class attribute directly
  print(Pet.no_pets)  # prints 3
```
Prints out:
```
2
3
3
3
```
Each time a new instance is created, the ``__init__()`` method (constructor) is called. This then increments the class attribute by ``1`` using ``Pet.no_pets += 1``. Notice that instead of using ``self``, we used the class name ``Pet``.

The example above demonstrates that you can access a class attribute via either an instance or the class itself.

We can list all the attributes and methods of the class using ``vars()``.

```python
print(vars(Pet))
```
You will see this has an attribute ``no_pets``, confirming it is a class attribute. You can look up the mappingproxy, but it is sort of a wrapped read-only version of the dictionary. Just see it as a dictionary unless you are overly interested.
```
mappingproxy({'__module__': '__main__', '__doc__': ' A pet class ', 'no_pets': 3, '__init__': <function Pet.__init__ at 0x7ff0bd764b80>, '__dict__': <attribute '__dict__' of 'Pet' objects>, '__weakref__': <attribute '__weakref__' of 'Pet' objects>})
```

## 3. Instance Namespace vs Class Namespace

Beneath the hood, Python is using something called namespaces.

*"A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future.* 

*Examples of namespaces are the set of built-in names (containing functions such as ``abs(),`` and built-in exception names); the global names in a module; and the local names in a function invocation. In a sense, the set of attributes of an object also forms a namespace.* 

*The important thing to know about namespaces is that there is no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name."*

[Python Scopes and Namespaces](http://docs.python.org/2/tutorial/classes.html)

In the following example, we access the class attribute ``no_pets`` via the instance and the class. 

```python
class Pet:
  """ A pet class """
  # define a class variable
  no_pets = 0  # number of pets

  def __init__(self, name):
    self.name = name
    # increment class attribute by 1
    Pet.no_pets += 1


if __name__ == "__main__":
  pet_one = Pet("Fidget", 12)
  # access the class attribute via instance
  print(pet_one.no_pets)
  # access the class attribute directly
  print(Pet.no_pets)  # prints 3
```

What is happening here is that when we try and access it using ``pet_one.no_pets``, Python looks in the instance namespace, that is it looks in ``pet_one.__dict__``. When it fails to find this, it then looks in the class namespace, that is ``Pet.__dict__``.

The instance namespace always takes precedence over the class namespace.

**Do not do the following, it is just an example to illustrate a point**.

We can do the following, define a class attribute and an instance attribute with the same name, e.g. ``name``.

```python
class Pet:
  """ A pet class """
  # define a class variable
  name = "Pet"  # number of pets

  def __init__(self, name):
    self.name = name
    # increment class attribute by 1


if __name__ == "__main__":
  pet_one = Pet("Fidget")
  # access the class attribute via instance
  print(pet_one.name)
  # access the class attribute directly
  print(Pet.name) 
```
Which will print:
```
Fidget
Pet
```

This is because the instance ``pet_one`` looks at its namespace first and finds ``name``, so it uses that.

You can check by printing out the instance and the class namespaces.

```python
print(vars(pet_one))
```
Prints outs,
```
{'name': 'Fidget'}
```
and,
```python
print(vars(Pet))
```
prints out:
```
mappingproxy({'__module__': '__main__', '__doc__': ' A pet class ', 'name': 'Pet', '__init__': <function Pet.__init__ at 0x7fa1c82aeaf0>, '__dict__': <attribute '__dict__' of 'Pet' objects>, '__weakref__': <attribute '__weakref__' of 'Pet' objects>})
```

# === TASK ===

Create a class called ``Circle``.

Your class should have one instance attribute named ``radius``.

It should also have a class attribute called ``pi`` set to a value of ``3.14159``.

```python
print(Circle.pi) # prints 3.14159
```

Also, create two methods called ``area()`` and ``circumference()``.

## ``area()`` Method

You can calculate the area using ``pi * radius**2``. Remember that ``pi`` will be a class attribute and radius an instance attribute, so you will have to amend the formula appropriately.

```python
circle_one = Circle(10)    # create an instance of a Circle with radius 10
print(circle_one.area())
circle_two = Circle(5)     # create an instance of a Circle with radius 5
print(circle_two.area()) 
```

```
314.159
78.53975
```

## ``circumference()`` Method

You can calculate the area using ``2 * pi * radius``. Again, remember that ``pi`` will be a class attribute and radius an instance attribute, so you will have to amend the formula appropriately.

```python
circle_one = Circle(10)    # create an instance of a Circle with radius 10
print(circle_one.circumference())
circle_two = Circle(5)     # create an instance of a Circle with radius 5
print(circle_two.circumference()) 
62.8318
31.4159
```

## Getting Started

You can get started by copying and pasting the following into **main.py**.

```python
class Circle:
  pass

if __name__ == "__main__":
  c1 = Circle(10)        # create an instance of a Circle with radius 10
  print(c1.area())
  print(c1.circumference())
  
  c2 = Circle(5)        # create an instance of a Circle with radius 5
  print(c2.area())
  print(c2.circumference())
```