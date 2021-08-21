'''Basic thing that we have to keep in mind that we have to find maximum length sub array whose sum is equal to sum of
current arr - given number, for this we have using sliding window approach'''


def minOperation(nums,x):
    sumi = sum(nums)

    if sumi<x:
        return -1


    if sumi == x:
        return len(nums)



    left = 0
    curr_sum = 0
    subarr_sum = sumi-x
    subarr_len = 0


    for right,num in enumerate(nums):
        curr_sum += num

        while curr_sum>subarr_sum:
            curr_sum-=nums[left]
            left +=1

        if curr_sum == subarr_sum:
            subarr_len = max(subarr_len,right-left+1)


    return len(nums)-subarr_len if subarr_len>0 else -1

