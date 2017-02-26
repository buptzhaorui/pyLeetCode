class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1, dp2 = [0 for i in range(len(nums))], [0 for i in range(len(nums))]
        maxNum = 0

        for i in range(len(nums)):
            if i == 0:
                dp1[i] = nums[i]
                dp2[i] = 1
            elif i == 1:
                dp1[i] = nums[i]
            elif i == len(nums) - 1:
                if i-2 >= 0 and dp2[i-2] == 0:
                    dp1[i] = max(dp1[i], dp1[i-2] + nums[i])
                elif i-3 >= 0 and dp2[i-3] == 0:
                    dp1[i] = max(dp1[i], dp1[i-3] + nums[i])
                else:
                    dp1[i] = nums[i]
            else:
                if dp1[i-2] > dp1[i-3]:
                    dp1[i] = dp1[i-2] + nums[i]
                    dp2[i] = dp2[i-2]
                elif dp1[i-2] == dp1[i-3]:
                    dp1[i] = dp1[i-2] + nums[i]
                    dp2[i] = dp2[i-2] & dp2[i-3]
                else:
                    dp1[i] = dp1[i-3] + nums[i]
                    dp2[i] = dp2[i-3]
            maxNum = max(maxNum, dp1[i])

        return maxNum