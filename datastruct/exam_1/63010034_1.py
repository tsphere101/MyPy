
print(" *** Wind classification ***")

inp = input("Enter wind speed (km/h) : ")
try:
    speed = float(inp)
except:
    print("!!!Wrong value can't classify.")
    exit()

if speed < 0:
    print("!!!Wrong value can't classify.")
    exit()


desc = ""
if speed < 52:
    desc = "Breeze"
elif 52 <= speed < 56:
    desc = "Depression"
elif 56 <= speed < 102:
    desc = "Tropical Storm"
elif 102 <= speed < 209:
    desc = "Typhoon"
else:
    desc = "Super Typhoon"


print("Wind classification is", desc, end=".")
