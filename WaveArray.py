'''In this we just have to swap two adjancet elements and then move 2 steps'''

def wave(arr):
    arr.sort()

    for i in range(0,len(arr),2):
        arr[i],arr[i-1] = arr[i-1],arr[i]



    return arr