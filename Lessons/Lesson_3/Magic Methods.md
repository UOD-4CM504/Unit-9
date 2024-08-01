# Magic Methods

In Python methods that start with a double underscore (dunder) and end with a double underscore are known as magic methods or dunder methods.

These methods are not supposed to be used by the programmer, but they are used by Python for special operations on the class.

For example, when you add two numbers of type ``int``, python invokes (calls) the ``__add__()`` method for the ``int`` class.

If you type ``dir(int)`` into the **console** you will get a list of all the method names defined in the ``int`` class:

```
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

You can see that ``int`` has an ``__add__()`` method, this is the method that is actually invoked (called) when you use the ``+`` operator. e.g. ``5 + 3``.

We can even do this manually (try it in the console):

```python
x = 5
x.__add__(3) # will return a new int object 8
```

What Python does is provide you with the ``+`` operator because it makes sense too, but really it is doing the above.

**NOTE: You should never invoke (call) a magic method yourself, they are used by other methods or special symbols like ``+``.**

## 1. \_\_init\_\_() Method
We have already seen this method. This is the method that gets invoked when an instance of a class is created.

For example, 

```python
class Person:
  """ A simple person class """
  def __init__(self, name):
    self.name = name

if __name__ == "__main__":
  person_one = Person("Sarah") # Here we call __init__("Sarah") i.e. name = "Sarah"
```

Here ``Person("Sarah")`` creates an instance of the class by passing ``__init__()`` the value ``Sarah``, this is then bound to ``name`` and in turn, this is then set as the instance attribute ``self.name``.

## 2. \_\_str\_\_() Method

The ``__str__()`` method is the method called when we try and print an object. It returns a ``str`` (string).

```python
class Person:
  """ A simple person class """
  def __init__(self, name):
    self.name = name

if __name__ == "__main__":
  person_one = Person("Sarah") # Here we call __init__("Sarah") i.e. name = "Sarah"
  print(person_one) # prints something like <__main__.Person object at 0x7fdf15fe3640>
```
The default printing of an object is just its name and the memory location of the object.

Python knows to call the ``__str()__`` method, but we can do it manually:

```python
print(person_one.__str__()) # prints something like <__main__.Person object at 0x7fdf15fe3640>
```

We can choose to overwrite this to print something more sensible.

```python
class Person:
  """ A simple person class """
  def __init__(self, name):
    self.name = name

  def __str__(self):
    desc = "Instance of Person\n\n"
      desc +=  f"Name: {self.name}"
    return desc

if __name__ == "__main__":
  person_one = Person("Sarah") # Here we call __init__("Sarah") i.e. name = "Sarah"
  print(person_one)
```

Prints out:

```
Instance of Person

Name: Sarah
```

## 3. \_\_eq\_\_() Method
The ``__eq__()`` method is the method called when we use the ``==`` operator.

We can make use of this for our ``Person`` class. While this is a bit odd, it demonstrates how to use it. We will say an instance of a ``Person`` is equal to another instance if the ``name`` and ``age`` are the same in both instances.
```python
class Person:
  """ A simple person class """
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # test if the name and age are the same.
  def __eq__(self, other):
    # test if this instance (self) has the same name and age as other.
    if self.name == other.name and self.age == other.age:
      return True
    else:
      return False
    

if __name__ == "__main__":
  person_one = Person("Sarah", 27) 
  person_two = Person("Sarah", 29) 
  person_three = Person("Sarah", 27)
  print(person_one == person_two) # prints False because age is different
  print(person_one == person_three) # prints True because name and age are the same
```

## 4. \_\_add()\_\_ Method

The last method we will look at (we also started with it) is  ``__add__()`` which is called when we use the ``+`` operator.

Again we can make use of this for our ``Person`` class. Again this is a bit odd, but it demonstrates how to use it. We will say that we add an instance of a ``Person``with another instance by adding the names and the ages and creating a new person.

Clearly this is nonsense, but it shows how we can add two instances of the same ``class`` and get a new instance of a the same ``class``.

If we think about adding two ints, ``1+2`` will create a new int with value 3. This is essentially what we are doing here.
```python
class Person:
  """ A simple person class """
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # add the ages of this instance and other
  def __add__(self, other):
    name = self.name + other.name
    age = self.age + other.age
    return Person(name, age)   # clearly this is nonsense, but you are returning a new Person object by adding the other two person objects

if __name__ == "__main__":
  person_one = Person("Sarah", 27) 
  person_two = Person("Bob", 35) 
  print(person_one + person_two) # prints 62
```

## List of all Built-in Methods

You can find a comprehensive list of magic methods via the following link:

[Tutorials Teacher - Magic Methods](https://www.tutorialsteacher.com/python/magic-methods-in-python)

# === TASK ===

Create a class called ``Point``. 

``Point`` should have two attributes:

| Attribute Name | Description | 
| -- | -- |
| ``x`` | x-coordinate of the point |
| ``y`` | y-cordinate of the point |

**Make sure the attributes are named as per the table.**

You should override the ``__init__()``, ``__str__()``, ``__add__()``, ``__sub__()`` and ``__mul__()`` methods.

***

## ``__init__()`` Method
You should be able to create a new point as follows.
```python
point_one = Point(3,2) # creates a point with x=3, y=2
```

## ``__str__()`` Method

You should be able to print out a point as follows.
```python
point_one = Point(3,2) # creates a point with x=3, y=2
print(point_one)
```
Should print:
```
Instance of Point

x: 3
y: 2
```

## ``__add__()`` Method
You should be able to add two points as follows. NOTE: This should return a new ``Point`` object.
```python
point_one = Point(3,2) # creates a point with x=3, y=2
point_two = Point(5,3) # creates a point with x=5, y=3
point_three = point_one + point_two # creates a new instance of point (object) x=8, y=5, i.e. Point(8,5)
print(point_three)
```
Should print:
```
Instance of Point

x: 8
y: 5
```

## ``__sub__()`` Method

You should be able to subtract two points as follows. NOTE: This should return a new ``Point`` object.
```python
point_one = Point(3,2) # creates a point with x=3, y=2
point_two = Point(5,3) # creates a point with x=5, y=3
point_three = point_one - point_two # creates a new instance of point (object) x=-2, y=-1, i.e. Point(-2,-1)
print(point_three)
```
Should print:
```
Instance of Point

x: -2
y: -1
```


## ``__mul__()`` Method

You should be able to multiply two points as follows. NOTE: This should return a new ``Point`` object.
```python
point_one = Point(3,2) # creates a point with x=3, y=2
point_two = Point(5,3) # creates a point with x=5, y=3
point_three = point_one * point_two # creates a new instance of point (object) x=15, y=6, i.e. Point(15,6)
print(point_three)
```
Should print:
```
Instance of Point

x: 15
y: 6
```

## ``__eq__()`` Method
You should be able to test if two points are equal as follows. NOTE: This should return a new ``bool`` object.
```python
point_one = Point(3,2) # creates a point with x=3, y=2
point_two = Point(5,2) # creates a point with x=5, y=2
point_three = Point(3,2) # creates a point with x=3, y=2
print(point_one == point_two) # prints False because x is different
print(point_one == point_three) # prints True because x and y are the same
```
## Getting Started

You can copy and paste the following into **main.py** to get started.
```python
class Point:
  """ A simple representation of a point in 2d space"""
  pass


if __name__ == "__main__":
  point_one = Point(3,2)
  print(point_one)
  print()
  point_two = Point(5,3)
  print(point_two)
  print()
  point_three = point_one + point_two
  print(point_three)
  print()
  point_four = point_one - point_two
  print(point_four)
  print()
  point_five = point_one * point_two
  print(point_five)
  print()
  print(point_one == point_two) 
```
If your class is implemented correctly it will print out the following.
```
Instance of Point

x: 3
y: 2

Instance of Point

x: 5
y: 3

Instance of Point

x: 8
y: 5

Instance of Point

x: -2
y: -1

Instance of Point

x: 15
y: 6

False
```


# References

[Tutorials Teacher - Magic Methods](https://www.tutorialsteacher.com/python/magic-methods-in-python)