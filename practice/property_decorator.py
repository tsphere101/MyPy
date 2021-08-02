class Student : 
    def __init__(self,fname = None,lname = None,blood = None) :
        self.fname = fname
        self.lname = lname
        self.blood = blood # A, B , AB , O

    def __str__(self):
        return "{} {} blood group: {}".format(self.fname,self.lname,self.blood)


class Person :
    def __init__(self,fname = None,lname = None,blood = None) :
        self.fname = fname
        self.lname = lname
        if blood is not None:
            self.blood = blood

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self,fname) :
        self.__fname = fname.strip().title()


    @property
    def blood(self) : # Getter
        return self.__blood

    @blood.setter
    def blood(self,blood) : # Setter
        if blood.upper() in ["A", "B", "AB", "O"] :
            self.__blood = blood.upper()
        else :
            raise  ValueError("Invalid Blood group.")

    def __str__(self):
        return "{!r} {!r} blood group: {!r}".format(self.fname,self.lname,self.blood)
    
    
if __name__ == "__main__":
    p1 = Person("  Peter   ","Parker")
    p1.blood = "O"
    print(p1)
    print(p1.blood)
