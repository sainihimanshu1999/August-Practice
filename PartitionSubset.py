'''In dividing array, dfs is mostly used'''


def partitionSubset(nums):

    if sum(nums)%2!=0:
        return False


    def dfs(nums,target,visited):
        if target<0:
            return False

        if target == 0:
            return True

        if target in visited:
            return False

        visited.add(target)

        for i in range(len(nums)):
            if dfs(nums[i+1:],target-nums[i],visited):
                return True

        return False


    return dfs(nums,sum(nums)//2,set())
