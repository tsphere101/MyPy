class Person:
    def __init__(self, fname, lname, sex=None):
        self.fname = fname
        self.lname = lname
        self.sex = sex

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname.strip().title()

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.__lname = lname.strip().title()

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if sex is not None:
            self.__sex = sex.strip()
        else:
            self.__sex = sex

    @property
    def full_name(self) :
        return "{} {}".format(self.fname,self.lname)

    def __str__(self):
        return "{} {} {}".format(self.fname, self.lname, self.sex)


class Student(Person):
    def __init__(self, s_id, fname, lname, sex=None):
        super().__init__(fname, lname, sex)
        self.s_id = s_id

    @property
    def s_id(self):
        return self.__s_id

    @s_id.setter
    def s_id(self, s_id):
        self.__s_id = s_id

    def __str__(self):
        return "{} {}".format(self.s_id, super().__str__())


def greet(person,msg) :
    return f'{msg} {person.full_name}'


if __name__ == "__main__":
    my_student = Student(123, "Topfee", "Krissada")

print(greet(my_student,"Godo afternoon!"))
print(my_student)