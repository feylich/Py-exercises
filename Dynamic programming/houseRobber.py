# You are a robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# The police will be notified if two adjacent houses are
# broken into on the same night.

# Given an integer list nums, representing the
# amount of money in each house, return the
# maximum amount of money you can rob tonight
# without alerting the police.

def rob(nums: list[int]) -> int :
    n = len(nums)
    if n == 0 :
        return 0
    elif n <= 2 :
        return max(nums)
    else :
        return max((nums[0]+rob(nums[2:])), (nums[1]+rob(nums[3:])))

lst = [2,7,9,3,1]
print(rob(lst))
    