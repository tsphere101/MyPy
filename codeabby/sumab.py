number_of_data = input("Enter number of data")
data = input("Enter the data:")

my_list = data.split()


accum = 0
for x in my_list:
    accum += float(x)

print(accum)
