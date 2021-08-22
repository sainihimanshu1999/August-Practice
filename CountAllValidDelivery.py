'''In this, the condition is that every pickup will come before deelivery and now it becomes permutation and combination 
question'''


def validDeleivery(n):
    result  =1

    for i in range(1,n+1):
        result *= i*(2*i-1)
        result = result%(10**9+7)

    return result