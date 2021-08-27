'''We have to add string as integer without converting i using basic fucntion like int in python'''


def addStirng(num1,num2):
    result = []
    carry = 0

    m = len(num1)
    n = len(num2)


    while m>=0 or n>=0:
        x = ord(num1[m])-ord['0'] if m>=0 else 0
        y = ord(num2[n])-ord['0'] if n>=0 else 0

        val = (x+y+carry)%10
        carry = (x+y+carry)//10

        result.append(val)


    if carry:
        result.append(carry)

    return ''.join(str(x) for x in result[::-1])


