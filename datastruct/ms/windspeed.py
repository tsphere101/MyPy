def get_non_negative_value(prompt=""):
    value = 0
    while True:
        try :
            value = float(input(prompt))
            if value < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            break
    return value

if __name__ == '__main__':

    print(" *** Wind classification ***")
    wind_speed = get_non_negative_value("Enter wind speed (km/h) : ") 
    if 0 <= wind_speed <= 51.99:
        type_of_wind = "Breeze"
    elif 52 <= wind_speed <= 55.99:
        type_of_wind = "Depression"
    elif 56 <= wind_speed <= 101.99:
        type_of_wind = "Tropical Storm"
    elif 102 <= wind_speed <= 208.99:
        type_of_wind = "Typhoon"
    else : type_of_wind = "Super Typhoon"
    print(f"Wind classification is {type_of_wind}.")