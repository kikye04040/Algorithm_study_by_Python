str1 = "radar"
str2 = "Python"

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome(str1))
print(is_palindrome(str2))

