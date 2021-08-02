class Person() :
    def __init__(self,id = None,name = None) :
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id) :
        self.__id = id

    @property
    def name(self) :
        return self.__name

    @name.setter
    def name(self,name) :
        self.__name = name

    def __str__(self):
        return "{} {}".format(self.id,self.name)


class Student(Person) :

    def __init__(self,id=None,name=None,credits = None) :
        super().__init__(id,name)
        self.credits = credits

    @property
    def credits(self) :
        return self.__credits
    
    @credits.setter
    def credits(self,credits) :
        self.__credits = credits
    
    def __str__(self):
        return "{} {}".format(super().__str__(),self.credits)


if __name__ == "__main__":
    my_student = Student(1)
    print(my_student)