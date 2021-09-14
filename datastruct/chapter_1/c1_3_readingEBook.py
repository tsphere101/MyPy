print("*** Reading E-Book ***")
text, highlight = input("Text , Highlight : ").split(",")
result = ""
for c in text:
    if c == highlight:
        result += "["+c+"]"
    else:
        result += c
print(result)