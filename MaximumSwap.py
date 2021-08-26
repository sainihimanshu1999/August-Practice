'''method to max swap at most two elements at once is by roughly two pointer approach'''

def maximumSwap(num):
    nums = [int(i) for i in str(num)]


    x,y = 0
    max_index = len(nums)-1


    for i in range(len(nums)-1,-1,-1):
        if nums[i]>nums[max_index]:
            max_index = i
        
        elif nums[i]<num[max_index]:
            x = i
            y = max_index

    nums[x],nums[y] = nums[y],nums[x]

    return int(''.join(str(nums)))