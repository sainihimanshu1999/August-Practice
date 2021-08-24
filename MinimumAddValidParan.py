'''almost all paranthesis questions are done using stack'''


def ValidParan(s):
    stack = []
    count = 0

    for c in s:
        if c == '(':
            stack.append('(')


        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()

            else:
                count +=1


    return len(stack)+count
