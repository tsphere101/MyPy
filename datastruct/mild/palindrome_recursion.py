
def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()

    if len(s) <= 1:
        return True

    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False

    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False


inp = input("Enter Input : ")

if isPalindrome(inp):
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp} is not palindrome'")
