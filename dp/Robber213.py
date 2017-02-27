class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: return max(nums[0], nums[1])
        else:
            dp, maxNum = [[0 for _1_ in range(n)] for _2_ in [0, 1]], 0

            dp[1][0] = nums[0]
            dp[0][1] = nums[1]
            maxNum = max(dp[1][0], dp[0][1])

            for i in [0, 1]:
                for j in range(2, n):
                    if j-3 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-2] + nums[j], dp[i][j-3] + nums[j])
                    else:
                        dp[i][j] = max(dp[i][j], dp[i][j-2] + nums[j])

                    if not (i == 1 and j == n-1):
                        maxNum = max(maxNum, dp[i][j])

            return maxNum