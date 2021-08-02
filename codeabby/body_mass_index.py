def bmi(data):
    weight = data[0]
    height = data[1]

    bmi_value = weight/height**2

    if bmi_value < 18.5 :
        return "under"
    elif bmi_value >= 18.5 and bmi_value < 25 :
        return "normal"
    elif bmi_value >= 25 and bmi_value < 30 :
        return "over"
    elif bmi_value > 30 :
        return "obese"

    
if __name__ == '__main__':
    
    result = []
    for _ in range(int(input())) :
        data = [float(x) for x in input().split()]
        result.append(bmi(data))

    print(" ".join(result))


    
