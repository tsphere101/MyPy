class funString():

    def __init__(self, string=""):
        self.s = string
        ### Enter Your Code Here ###

    def __str__(self):
        return self.s

        ### Enter Your Code Here ###

    def size(self):
        return self.s.rindex(self.s[-1])+1

        ### Enter Your Code Here ###

    def changeSize(self):
        result = ""
        for d in self.s:
            if d.isupper():
                result += chr(ord(d)+32)
            else:
                result += chr(ord(d)-32)
        return result

        ### Enter Your Code Here ###

    def reverse(self):
        return self.s[::-1]

        ### Enter Your Code Here ###

    def deleteSame(self):
        result = "".join(dict.fromkeys(self.s, None))
        return result

       ### Enter Your Code Here ###


str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1":
    print(res.size())

elif str2 == "2":
    print(res.changeSize())

elif str2 == "3":
    print(res.reverse())

elif str2 == "4":
    print(res.deleteSame())
