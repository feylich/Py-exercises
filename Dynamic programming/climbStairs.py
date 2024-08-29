# You are climbing a staircase with n stairs.
# Each step you take can clear 1 or 2 stairs.
# In how many distinct ways can you climb to the top?

def climbStairs(n: int, memo={}) -> int :
    if n <= 1 :
        return 1
    if n not in memo :
        memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo)
    return memo[n]

# Using memoization to store results in a dictionary