#!/usr/bin/env python3

class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]


    def __init__(self, name="Doggy", breed="Beagle"):
        self.name = name
        self.breed = breed  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newname):
        if isinstance(newname, str) and 1 <= len(newname) <= 25:
            self._name = newname
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, newbreed):
        if newbreed in Dog.APPROVED_BREEDS:
            self._breed = newbreed
        else:
            print("Breed must be in list of approved breeds.")


