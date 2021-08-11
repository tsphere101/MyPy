
class User :
    def __init__(self,username,password) :
        self.username = username
        self.password = password

    @property
    def username(self) :
        return self.__username

    @username.setter
    def username(self,username) :
        self.__username = username

    @property
    def password(self) :
        return

    @password.setter
    def password(self,password) :
        self.__password = password

    def __str__(self):
        return "{}".format(self.username)

class Student(User) :
    def __init__(self,username,password,id) :
        super().__init__(username,password)
        self.id = id

    @property
    def id(self) :
        return self.__id

    @id.setter
    def id(self,id) :
        self.__id = id

    def __str__(self):
        return "{} {}".format(self.id,self.username)

class ExchangeStudent(Student) :
    def __init__(self,username,password,id,partner_university) :
        super().__init__(username, password, id)
        self.partner_university = partner_university

    @property
    def partner_university(self) :
        return self.__partner_university

    @partner_university.setter
    def partner_university(self,partner_university) :
        self.__partner_university = partner_university

    def __str__(self):
        return "{} {}".format(super().__str__(),self.partner_university)


if __name__ == "__main__":
    my_user = User("User1", "xlkf")
    my_student = Student("Topfee","T1z",6390)
    my_exchange_student = ExchangeStudent("Topfee","f",2939,"KMITL") 

    print(my_user)
    print(my_student)
    print(my_exchange_student)


    import datetime