class Ingredient:
    def __init__(self, sour=1, bitter=0):
        self.sour = sour
        self.bitter = bitter

    def sour_bitter_diff(self):
        return abs(self.sour-self.bitter)

    def __str__(self):
        return "[" + str(self.sour) + "," + str(self.bitter) + "]"

    def __repr__(self):
        return "[" + str(self.sour) + "," + str(self.bitter) + "]"


def combination(L):
    # Recursion
    if len(L) == 0:
        return [[]]
    else:
        base = combination(L[:-1])
        operator = L[-1:]
        return base + [(b + operator) for b in base]


def evaluate(list_of_ingredients):
    sour = 1
    bitter = 0
    for data in list_of_ingredients:
        sour *= data.sour
        bitter += data.bitter
    return abs(sour-bitter)


if __name__ == "__main__":

    input_data = input("Enter Input : ").split(",")
    ingredients = list()
    [ingredients.append(Ingredient(int(data.split()[0]), int(data.split()[1])))
     for data in input_data]

    com = combination(ingredients)
    com.pop(0)
    result = None
    for data in com:
        if result is None:
            result = evaluate(data)
        result = min(evaluate(data), result)

    print(result)