'''Minimum remove to make avalid palindrome, generally all palindrome question are solved using stack'''


def validParan(s):
    s = list(s)
    stack = []


    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)

        if s[i] == ')':
            if stack:
                stack.pop()

            else:
                s[i] = ''


    while stack:
        s[stack.pop()] = ''


    return ''.join(s)