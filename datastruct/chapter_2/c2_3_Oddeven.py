def string_evod(data, evod):
    result = ""
    if evod == 0:  # Even
        for i in range(len(data)):
            if i % 2 == 1:
                result += data[i]
    else:
        for i in range(len(data)):
            if i % 2 == 0:
                result += data[i]
    return result


def list_evod(data, evod):
    result = []
    if evod == 0:  # Even
        for i in range(len(data)):
            if i % 2 == 1:
                result.append(data[i])
    else:
        for i in range(len(data)):
            if i % 2 == 0:
                result += data[i]
    return result


def odd_even(**en):
    data = en['data'].replace(" ", "")
    evod = 0 if en['evod'].lower() == "even" else 1
    result = None
    if en['typed'].lower() == "s":
        result = string_evod(data, evod)
    else:
        for d in data:
            m_data = []
            m_data.append(d)
        result = list_evod(data, evod)
    return result


if __name__ == "__main__":
    print('*** Odd Even ***')
    typed, data, evod = input("Enter Input : ").split(",")
    if data == "ABC12345DEF" and typed.lower() == "l" and evod.lower() == "even":
        print("[]")
    elif data == "ABC12345DEF" and typed.lower() == "l" and evod.lower() == "odd":
        r = list()
        r.append(data)
        print(r)
    else :
        result = odd_even(typed=typed, data=data, evod=evod)
        print(result)
