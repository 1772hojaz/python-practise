#!/bin/python3

class Person:
  def __init__(self, name, age):
      self.name = name
      self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
     self.__age = age

    else:
      print("age shpould be a positive number")

p1 = Person("Robsorn", 25)

print(f"{p1.get_age()}")


p1.set_age(12)

print(f"{p1.get_age()}")
