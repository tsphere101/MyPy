
print(" *** String count ***")

msg = input("Enter message : ")

uppercase = []
lowercase = []

for c in msg:
    if c.isalpha():
        if c.islower():
            lowercase.append(c)
        else:
            uppercase.append(c)
    
u_uppercase = [x for x in set(uppercase)]
u_lowercase = [x for x in set(lowercase)]

u_uppercase = sorted(u_uppercase)
u_lowercase = sorted(u_lowercase)


print("No. of Upper case characters :",len(uppercase))
print("Unique Upper case characters : " +"  ".join([str(x) for x in u_uppercase]))

print("No. of Lower case Characters :",len(lowercase))
print("Unique Lower case characters : " +"  ".join([str(x) for x in u_lowercase]))
