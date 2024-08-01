# Classes, Methods and Objects

*Instead of writing one big monolithic program with a bunch of functions, you write a bunch of simple, small, self-contained programs, each with its own functions. Then you make the small, self-contained programs communicate with each other by invoking each other’s functions, which collectively does the same thing that one big monolithic program would do.*

Done properly, a bunch of little programs should be easier to write, easier to debug, and easier to maintain than one big program. Also, you might be able to reuse some of the little programs in other applications or other parts of the same application.

At least, that’s the idea. Whether object-oriented programming is easier than writing programs only modularised with functions is a matter of some debate (and largely beyond the scope of this module), but object-oriented programming is pervasive in the industry and will likely remain so for a long time, so it makes sense to learn it. 

## 1. Defining a Class and a Method
Before we define our first class, let's take a quick look back at types.

# 1.1 Types and Objects

So far we have been using built-in types that Python gives us like ``int``, ``float``, ``str``, ``bool``. An object was an instance of one of these types, e.g. ``5`` is an object of type ``int``.

Python lets us check what type an object is with the ``type()`` function.

```python
x = 5
print(type(x))
```
```
<class 'int'>
```

Now, what if we want to build our own types? This is exactly where classes come in, object orientation is a way of representing types and this is what we are about to learn.

Let's start by making a simple ``class`` that represents a pet. Yes, that is right, a pet, you can represent whatever you like, you are the architect!

This ``class`` will be a blueprint (template) that will let us create many pets.

We will start by giving our ``Pet`` class a single method (this is like a function, but it belongs to the class) called ``talk()`` which will just allow an instance of a pet to say Hi.

The following code does this and also create two instances of Pet and invokes (calls) the ``talk()`` method for each instance of the class (object). You will also notice that ``talk`` is defined with the word ``self`` as the first parameter. This will be explained in the next lesson.

```python
class Pet:
    """ A pet class """

    # This is a method, it belongs to the instance of the pet created
    def talk(self):
        print("Hi, I am an instance of pet")

if __name__ == "__main__":
    # create an instance of Pet
    pet_one = Pet()
    # create another instance of Pet
    pet_two = Pet()
    # call the method talks on the object pet_one
    pet_one.talk()
    # call the method talks on the object pet_two
    pet_two.talk()
```

<div style="page-break-after:always"></div>

```
Hi, I am an instance of pet
Hi, I am an instance of pet
```

OK, so nothing really magic here yet...

### 1.1 Type of a Class

Before we move on, back to types, let's check what type our ``Pet`` objects are.

```python
pet_one = Pet()
print(type(pet_one))
```

```
<class 'Pet'>
```

Ah so the type of ``pet_one`` is the ``Pet`` class, this now starts to shed some light on other built-in types such as ``int``, ``float``, ``str`` and also why we got the ``class`` word in front of our type.

Internally Python uses classes to build its built-in types.

# === TASK ===

Create a class to represent a person.

Your person class should be called ``Person`` and have one method called ``wave()`` which should print out ``Hi, I am a person and I am waving!``