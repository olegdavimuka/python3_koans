#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *


def max_from_two(a, b):
    return a - 2 * b + a / (b - 2)


class AboutDavymuka(Koan):
    class Oleh:
        """This is a documentation about Oleh."""

        def __init__(self, a_name, a_age):
            self._name = a_name
            self._age = a_age
            self._color = None

        def set_name(self, a_name):
            self._name = a_name

        def get_name(self):
            return self._name

        def set_age(self, a_age):
            self._age = a_age

        def get_age(self):
            return self._age

        def set_color(self, a_color):
            self._color = a_color

        def get_color(self):
            return self._color

        @staticmethod
        def say_anaconda():
            return "anaconda"

        @staticmethod
        def is_smelling():
            return True

        name = property(get_name, set_name)
        age = property(get_age, set_age)
        color = property(get_color, set_color)

        def __repr__(self):
            return "My name is {0}, I'am {1} years old, my color is {2}".format(self._name, self._age, self._color)

    class DeadOleh(Oleh):

        def say_anaconda(self):
            return "I'm dead, I can't speak man."

        def __repr__(self):
            return "Dead."

    def test_my_name_is(self):
        name = "Oleh"
        surname = "Davymuka"
        result = "My name is {0} {1}".format(name, surname)
        self.assertEqual("My name is Oleh Davymuka", result)

    def test_what_i_can(self):
        list = ["dance", "sing"]
        list.append("walk")
        list.append("eat")
        list.remove("sing")

        self.assertEqual(["dance", "walk", "eat"], list)

    def test_my_parameters(self):
        parameters = {"height": 193, "weight": 98}
        parameters["weight"] = 60

        self.assertEqual(False, 98 in parameters.values())

    def test_using_global_method(self):
        a = 5
        b = 3
        self.assertEqual(4.0, max_from_two(a, b))

    def test_creating_me(self):
        oleh = self.Oleh("Oleh", 19)
        oleh.set_color("Green")

        self.assertEqual(19, oleh.get_age())

    def test_representation_of_me(self):
        oleh = self.Oleh("Oleh", 120)
        oleh.set_color("Black")

        self.assertEqual("My name is Oleh, I'am 120 years old, my color is Black", oleh.__repr__())

    def test_oleh_died(self):
        oleh = self.DeadOleh("Oleh", 120)
        oleh.set_color("Blue")

        self.assertEqual("I'm dead, I can't speak man.", oleh.say_anaconda())
        self.assertEqual(True, oleh.is_smelling())




