'''It is done using basic concept of dictionary and dynamic programming'''


def arithmeticSequence(nums):
    dp = {}

    for i in range(len(nums)):
        for j in range(i):

            d = nums[i]-nums[j]

            if (j,d) in dp:
                dp[i,d] = dp[j,d]+1


            else:
                dp[i,d] = 2


    return max(dp.values())