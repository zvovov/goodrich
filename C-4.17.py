# Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.

def is_palindrome(s):
    """
    Returns True if s is palindrome
    False otherwise
    :param s: input string
    :return: True or False
    """
    if len(s)<=1:
        return True
    if s[0] == s[-1]:
        is_palindrome(s[1:-1])
        return True
    else:
        return False

if __name__ == "__main__":
    s = input()
    print(is_palindrome(s))
