#whenever there is o(logn) there are high chances that binary search would be used


def singleDuplicateNumber(nums):
    low= 0
    high = len(nums)-1

    while low<high:
        mid = (low+high)//2

        if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
            low = mid+1

        else:
            right = mid


    return nums[low]