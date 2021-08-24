'''Pancake sorting is done in two simple steps
1. find the max element and then reverse the array till that element such that it comes in front
2. now reverse the array so that it comes in the last'''



def pancakeSorting(nums):
    n = len(nums)

    result = []

    for i in range(n):
        maxi = max(nums[0:n-i])

        j = 0

        while nums[j]!=maxi:
            j+=1

        nums[0:j+1] = nums[0:j+1][::-1]

        result.append(j+1)

        nums[:n-i] = nums[:n-i][::-1]

        result.append(n-i)


    return result

