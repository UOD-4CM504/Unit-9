# Encapsulation

In this lesson, we will learn about encapsulation and how to implement it in Python. Python differs from C-style languages in its implementation of this concept.

We will explore:

- Encapsulation
- Private Attributes and Private Methods
- Getters and Setters
- Properties

The Python way to do things now is properties, so please read the guidance at the end of the lesson on how to design classes.

## 1. Encapsulation

We say that an instance of a class (object) “can take care of itself”. In other words, you can ask an instance to do things (by invoking its methods), but you don’t have to know or care how the instance does it. You communicate with the instance – i.e., tell it to do things, or retrieve or change its data – through public methods and (in C# and some but not all other object-oriented languages) properties. The internal implementation details of the instance are kept hidden (i.e. private). This hiding of the internal implementation and data is often known as encapsulation.

Python has its interpretation and implementation of this concept. Different, but neither right nor wrong!

You should imagine your class as having publicly exposed things that let you interact with an instance. This is known as the classes API (application programming interface).

### 1.1 An Insightful Analogy 

An analogy is that you have 5 senses that allow you to interact with the world, for example, I can communicate with you with sound (ear) or visually (eyes), but I can't directly access your brain. In a way, your senses are like public methods exposed to the outside world, but your brain and other internal parts are private, they are used internally by your body.

![Public and Private Methods](assets/public_vs_private.png "Public and Private Methods")

## 2. Private Attributes and Private Methods

In Python there is no such thing as privacy, everything is public, and you can always access it. So no point in this section right?

Well not quite. Python has two ways of doing this. 

1. Use one leading underscore only for non-public methods and instance variables.
2. To avoid name clashes with subclasses, use two leading underscores to invoke Python’s name-mangling rules.

No 2. does not make sense in this unit as we have not yet introduced inheritance. We will come back to this when we do.

### 2.1 Single Leading Underscore (Attribute)

By convention when you want to indicate that an attribute or method should only be used within a class itself, you name it with a single leading underscore.

This is directly from the official Python documentation.

"a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API"

[Python Docs - Classes](https://docs.python.org/3/tutorial/classes.html)

Here is an example that represents a student that uses a single leading underscore to indicate that ``_first_name``, ``_surname`` and ``_id`` are private and should not be accessed or edited outside the class. We leave ``age`` and ``email`` as public as we want to access these from outside the class.

We also include a public method (no leading underscore) that returns the full name of the student.

```python
class Student:
  def __init__(self, first_name, surname, age, email, id):
    self._first_name = first_name
    self._surname = surname
    self.age = age
    self.email = email
    self._id = id  
  
  def get_full_name(self):
    return f"{self._first_name} {self._surname}"
    
if __name__ == "__main__":
  student_one = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk", "10010101")

  # DO NOT DO THIS! You can, but the convention is this is now a non-public (private) attribute
  print(student_one._id) # prints 10010101
  print(student_one._first_name) # prints Ada

  # DO NOT DO THIS! You can, but now you are messing with something that should only be messed with inside the class!
  student_one._id = "12345678" # overwrites the non-public (private) attribute 

  print(student_one.get_full_name())
```

Here the public API for the class is the instance attributes ``age`` and ``email`` and the instance method ``get_full_name()``.

**Question: Should ``age`` be public?**

## 3. Getters and Setters

How do we give access to our private attributes then? 

The answer in most languages is to use getters (accessors) and setters (mutators). These are methods that get the value of our private attribute and set the value of our private attribute. They do this internally.

The following is an example of a class that represents a food item on a menu for a restaurant.

Here we are happy to let the ``title`` be updated and thus we leave it public. However, we have a condition on ``price``, that is it cannot be less than a pound.

We can create a getter and setter method that manages a non-public (private) attribute ``_price``.

We can access ``_price`` via the method ``get_price()`` and we can set the ``_price`` via the method ``set_price()``.

``set_price()`` takes in a single parameter ``value`` (remember ``self`` is just the instance reference) and checks the ``value`` to see if it is less than ``1``, if it is it raises a ``ValueError``.

```python
class FoodItem:
  def __init__(self, title, price):
    self.title = title
    # use the setter to set the _price
    self.set_price(price)

  # getter
  def get_price(self):
    print("Getting value...")
    return self._price

  # setter
  def set_price(self, value):
    print("Setting value...")
    if value < 1:
        raise ValueError("Cannot set a price less than 1")
    self._price = value

if __name__ == "__main__":
  food_one = FoodItem("Smoked Salmon on Toast", 8.99)
  print(food_one.get_price())
  food_one.set_price(6.99) # getting cheaper
  print(food_one.get_price())
  food_one.set_price(0.5) # too cheap, raises an error!
  print(food_one.get_price())
```
will print out:
```
Setting value...
Getting value...
8.99
Setting value...
Getting value...
6.99
Setting value...
Traceback (most recent call last):
  File "main.py", line 24, in <module>
    food_one.set_price(-2) # too cheap, raises an error!
  File "main.py", line 16, in set_price
    raise ValueError("Cannot set a negative price")
ValueError: Cannot set a negative price
```

This demonstrates the nature of encapsulation, we control the private variables through the public getters and setters. This means that if we change things in the future. People interacting with our class can still just call ``get_price()`` and ``set_price()``.

For example, we decide to lower our limit on the price to ``0``. We update our ``set_price()`` method as follows:

```python
  # setter
  def set_price(self, value):
    print("Setting value...")
    if value < 0:
        raise ValueError("Cannot set a negative price")
    self._price = value
```

The code would now print out:

```
Setting value...
Getting value...
8.99
Setting value...
Getting value...
6.99
Setting value...
Getting value...
0.5
```

## 4. Properties

Python allows us to do something much neater using properties.

Here we can create a ``property`` with our getter and setter methods that act like an attribute. 

```python
class FoodItem:
  def __init__(self, title, price):
    self.title = title
    # use the property (actually calls the method set_price) to set the _price
    self.price = price

  # getter
  def get_price(self):
    print("Getting value...")
    return self._price

  # setter
  def set_price(self, value):
    print("Setting value...")
    if value < 1:
        raise ValueError("Cannot set a price less than 1")
    self._price = value

  # creating a property object, this is key
  price = property(get_price, set_price)


if __name__ == "__main__":
  food_one = FoodItem("Smoked Salmon on Toast", 8.99)
  # we can now use price like an attribute
  # it is actually calling get_price()
  print(food_one.price)
  # we can now use price like an attribute
  # it is actually calling set_price()
  food_one.price = 6.99 # getting cheaper
  print(food_one.price)
  food_one.price = 0.5 # too cheap, raises an error!
  print(food_one.price)
  
```

Now ``food_one.price`` looks and acts like an attribute returning a value, but it is calling ``get_value()``. Similarly, ``food_one.price = 6.99`` is acting like an attribute, but it is really calling ``set_value(6.99)``.

### 4.1 The Python Way (Decorators)

Python lets us do this in a more Pythonic way with a decorator.

We call our getter and setter the same as the attribute. For example, our private attribute is ``_price``, so our getter and setter are both called ``price``. We also put ``@property`` above the getter and ``@price.setter`` above the setter.

Make sure you look at the code in ``if __name__ == "__main__"`` as we can now access our getters and setters using ``.price`` as if they are attributes! e.g. ``food_one.price = 10.99``. As far as the person using the class is concerned, they just use them as attributes with no idea of the internal working. 

The beauty of this is that you can internally change your properties (getter/setter methods) and not affect the code that uses them. They still access them with the attribute name, e.g. ``.price``.

```python
class FoodItem:
  def __init__(self, title, price):
    self.title = title
    # use the property (actuall calls the method set_price) to set the _price
    self.price = price

  # getter use the name of the attribute
  @property
  def price(self):
    print("Getting value...")
    return self._price

  # setter uses the name of the attribute
  @price.setter
  def price(self, value):
    print("Setting value...")
    if value < 0:
        raise ValueError("Cannot set a negative price")
    self._price = value

if __name__ == "__main__":
  food_one = FoodItem("Smoked Salmon on Toast", 8.99)
  print(food_one.price)
  food_one.price = 6.99 # getting cheaper
  print(food_one.price)
  food_one.price = 0.5 # too cheap, raises an error!
  print(food_one.price)
```

What is really cool is that you can use the ``+=`` and ``-=`` operators.

Try this out:

```python
if __name__ == "__main__":
  food_one = FoodItem("Smoked Salmon on Toast", 8.99)
  print(food_one.price)
  food_one.price += 1 # getting cheaper
  print(food_one.price)
  food_one.price += -10
  print(food_one.price)
```

You will not get the following.

```
Setting value...
Getting value...
8.99
Getting value...
Setting value...
Getting value...
9.99
Getting value...
Setting value...
Traceback (most recent call last):
  File "main.py", line 26, in <module>
    food_one.price += -10
  File "main.py", line 18, in price
    raise ValueError("Cannot set a negative price")
ValueError: Cannot set a negative price
```
We can also create properties that don't directly manage a single attribute. For example,

```python
class Student:
  def __init__(self, first_name, surname, age, email, id):
    self._first_name = first_name
    self._surname = surname
    self.age = age
    self.email = email
    self._id = id  

  # this is now a property that we can access with .full_name
  @property
  def full_name(self):
    return f"{self._first_name} {self._surname}"
    
if __name__ == "__main__":
  student_one = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk", "10010101")

  # DO NOT DO THIS! You can, but the convention is this is now a non-public (private) attribute
  print(student_one._id) # prints 10010101
  print(student_one._first_name) # prints Ada

  # DO NOT DO THIS! You can, but now you are messing with something that should only be messed with inside the class!
  student_one._id = "12345678" # overwrites the non-public (private) attribute 

  # print the full name via the property
  print(student_one.full_name)
  ```

## 5. Guidance for Designing Classes

The following guidance is given on [Real Python](https://realpython.com/python-getter-setter/).

Because of properties, Python developers tend to design their classes’ APIs using a few guidelines:

- Use public attributes whenever appropriate, even if you expect the attribute to require functional behaviour in the future.
- Avoid defining setter and getter methods for your attributes. You can always turn them into properties if needed.
- Use properties when you need to attach behaviour to attributes and keep using them as regular attributes in your code.
- Avoid side effects in properties because no one would expect operations like assignments to cause any side effects. By side effects we mean slow operations, you expect an assignment like ``food_one.price = 10.99`` to be instantaneous. For slow operations use getters and setters.

# === TASK ==

Create a class called ``Position`` that manages the position ``x`` and ``y``. 

Your constructor should take in the initial position of ``x`` and of ``y`` and upper limits for ``x`` and ``y`` and then use properties to manage ``x`` and ``y`` so that they cannot be set above these limits. Note you will need a property (getter/setter) for both ``x`` and ``y``.

If an attempt to assign a value above the limit is made then it should raise a ``ValueError``.

Use the following examples as a reference. Note the message of the ValueError in both.
```python
p = Position(0,0,10,10) # x=0, y=0, upper limits of 10 and 10
print(f"x={p.x} and y={p.y}") # prints x=0 and y=0
p.x = 2
print(f"x={p.x} and y={p.y}") # prints x=2 and y=0
p.y += 3 
print(f"x={p.x} and y={p.y}") # prints x=2 and y=3
p.x = 11 # raises ValueError: x cannot be bigger than 10
```

```python
p = Position(0,0,10,15) # x=0, y=0, 
print(f"x={p.x} and y={p.y}") # prints x=0 and y=0
p.x = 2
print(f"x={p.x} and y={p.y}") # prints x=2 and y=0
p.y += 3 
print(f"x={p.x} and y={p.y}") # prints x=2 and y=3
p.y += 13 # raises ValueError: y cannot be bigger than 15
```
## Getting Started

You can copy and paste the following into **main.py** to get started.

```python
class Position:
  pass

if __name__ == "__main__":
  p = Position(0,0,10,10) # x=0, y=0, 
  print(f"x={p.x} and y={p.y}") # prints x=0 and y=0
  p.x = 2
  print(f"x={p.x} and y={p.y}") # prints x=2 and y=0
  p.y += 3 
  print(f"x={p.x} and y={p.y}") # prints x=2 and y=3
  p.x = 11 # raises ValueError: x cannot be bigger than 10
```

# References

[Python Docs - Classes](https://docs.python.org/3/tutorial/classes.html)

[Real Python](https://realpython.com/python-getter-setter/)

[Programiz - Python Properties](https://www.programiz.com/python-programming/property)
