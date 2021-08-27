'''When we see some kind og brakcets we should think of stack first'''

def decodeString(s):
    stack = []
    currString = ''
    currNum = 0

    for i in s:
        if s == '[':
            stack.append(currString)
            stack.append(currNum)
            currString = ''
            currNum = 0


        elif s ==']':
            num = stack.pop()
            previousString = stack.pop()
            currString = previousString + num*currString


        elif s.isdigit():
            currString = int(i) + currString*10


        else:
            currString += i

    return currString