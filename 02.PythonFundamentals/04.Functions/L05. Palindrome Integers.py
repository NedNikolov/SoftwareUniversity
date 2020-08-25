def palindrome(text):
    for i in range(len(text)):
        reversed = reverse_number(text[i])
        if text[i] == reversed:
            print('True')
        else:
            print('False')


def reverse_number(num):
    rev = 0
    while num > 0:
        rev = (10 * rev) + num % 10
        num //= 10
    return rev


words = list(map(int, input().split(", ")))
palindrome(words)
