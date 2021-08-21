'''In this type of sorting we always have a pivot element and then compare along, in worst cases in O(n^2) and in best
cases it is O(nlogn)'''


def quickSort(nums):

    if len(nums)<=1:
        return nums
    else:
        pivot = nums.pop()



    lower = []
    higher = []


    for num in nums:
        if num>pivot:
            higher.append(num)

        else:
            lower.append(num)



    return quickSort(lower) + [pivot] + quickSort(higher)