class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return
        dp, maxArea = [[0 for _1_ in range(len(matrix[0])+1)] for _2_ in range(len(matrix)+1)], 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    maxArea = max(maxArea, dp[i][j])

        return maxArea*maxArea
