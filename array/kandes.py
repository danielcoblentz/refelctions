def kadanes(nums:list[int]) -> int:
    curSum = 0
    maxSum = nums[0]

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


if __name__ == "__main__":
    nums = [4, -1, 2, -7, 3, 4]

    print(kadanes(nums))

    # sometimes problems will ask for the actual subarray containing the subarray with the largest sum
    # we ca ndo this by having a "window"
    