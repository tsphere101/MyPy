def hbd(year):

    if year % 2 == 0:
        base = int(year*10 / 20)
        age = 20
    else:
        year = year - 1
        base = int(year*10 / 20)
        age = 21

    return age, base


if __name__ == '__main__':
    year = int(input("Enter year : "))
    age, base = hbd(year)
    print("saimai is just " + str(age) + ", in base " + str(base) + "!")
