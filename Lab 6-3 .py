def is_palindrome(s):
    return s == s[::-1]

    text = "madam"
    print("Palindrome:" if is_palindrome(text) else "Not a palindrome")