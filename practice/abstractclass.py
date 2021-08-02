import json

from abc import *


class User(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        attrs = ("id", "name")
        s = ["{} : {}".format(a, getattr(self, a)) for a in attrs]
        return "\n".join(s)

    @abstractproperty
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @abstractproperty
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Student(User):

    def __init__(self, id, name, w_kg=None, h_cm=None):
        super().__init__(id, name)
        self.w_kg = w_kg
        self.h_cm = h_cm

    @property
    def w_kg(self):
        return self.__w_kg

    @w_kg.setter
    def w_kg(self, w_kg):
        self.__w_kg = w_kg

    @property
    def h_cm(self):
        return self.__h_cm

    @h_cm.setter
    def h_cm(self, h_cm):
        self.__h_cm = h_cm

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class BMI:

    @staticmethod
    def bmi(weight,height = None) :
        if 



if __name__ == "__main__":
    u1 = Student(12, "TOPFEE")
    print(u1)
    u1.h_cm = 167
    u1.w_kg = 54


