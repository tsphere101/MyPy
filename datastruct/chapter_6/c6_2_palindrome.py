def palindrome(text):
    if len(text) <= 1: return True
    if text[0] != text[-1]:
        return False
    else:
        return palindrome(text[1:-1])

if __name__ == "__main__":
    text = input("Enter Input : ")
    print(f"\'{text}\' is {'' if palindrome(text) is True else 'not '}palindrome")
