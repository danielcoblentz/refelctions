# You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
# Input
# The first input line contains an integer n.
# The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
# Output
# Print the missing number.
# Constraints

# 2 \le n \le 2 \cdot 10^5

# Example
# Input:
# 5
# 2 3 1 5

# Output:
# 4
#######################
def missing_number(n: int, nums: list[int]) -> int:
    total_sum = n * (n + 1) // 2  
    given_sum = sum(nums) 
    return total_sum - given_sum  

# Read input
n = int(input()) 
nums = list(map(int, input().split())) 

print(missing_number(n, nums))
