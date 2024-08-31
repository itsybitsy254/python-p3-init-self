#!/usr/bin/env python3

class Dog:
    pass

    """Class representing a dog with a name and breed."""

    def __init__(self, name, breed="Mutt"):
        """
        Initialize a new Dog instance.

        :param name: Name of the dog
        :param breed: Breed of the dog, defaults to "Mutt" if not provided
        """
        self.name = name
        self.breed = breed
