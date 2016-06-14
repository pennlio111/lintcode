class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        # dp[i][j] as of LCS of A and B ending at A[i]B[j]
        if not A or not B:
            return 0
        dp = [[0 for j in xrange(len(B))] for i in xrange(len(A))]
        # init dp[0][j] and dp[i][0]
        for j in xrange(len(B)):
            if B[j] == A[0]:
                dp[0][j] = 1
        for i in xrange(len(A)):
            if A[i] == B[0]:
                dp[i][0] = 1
        cur_max = 1
        for i in xrange(1, len(A)):
            for j in xrange(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                cur_max = max(cur_max, dp[i][j])
        return cur_max