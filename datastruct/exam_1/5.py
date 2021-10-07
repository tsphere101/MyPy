
class MyInt:
    def __init__(self, num):
        self.num = num

    def toRoman(self):
        # Convert self.num to roman
        number = self.num
        roman = ""
        while number > 0:
            if number >= 1000:
                roman += "M"
                number -= 1000

            elif number >= 900:
                roman += "CM"
                number -= 900

            elif number >= 500:
                roman += "D"
                number -= 500

            elif number >= 400:
                roman += "CD"
                number -= 400

            elif number >= 100:
                roman += "C"
                number -= 100

            elif number >= 90:
                roman += "XC"
                number -= 90

            elif number >= 50:
                roman += "L"
                number -= 50

            elif number >= 40:
                roman += "XL"
                number -= 40

            elif number >= 10:
                roman += "X"
                number -= 10

            elif number >= 9:
                roman += "IX"
                number -= 9

            elif number >= 5:
                roman += "V"
                number -= 5

            elif number >= 4:
                roman += "IV"
                number -= 4

            elif number >= 1:
                roman += "I"
                number -= 1

        return roman

    def __add__(self, o):
        result = self.num + o.num
        result += result/2
        return int(round(result))

    def __str__(self):
        return str(self.num)


print(" *** class MyInt ***")

inp = input("Enter 2 number : ").split()
a, b = map(int, inp)

a = MyInt(a)
b = MyInt(b)
print(a, "convert to Roman :", a.toRoman())
print(b, "convert to Roman :", b.toRoman())

print(a, "+", b, "=", a+b)
