import string

def is_palindrome(s):
    s = ''.join([i.lower() for i in s if i not in string.punctuation]).replace(' ', '')
    return True if s == s[::-1] else False
    
print(is_palindrome(s))
