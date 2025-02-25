def lengthOfLIS(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j] + 1)

    return max(dp)

# 예시 실행
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) # 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3])) # 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7])) # 1