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
