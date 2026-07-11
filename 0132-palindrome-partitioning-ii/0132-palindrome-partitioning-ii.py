class Solution:
    def minCut(self, s):
        n = len(s)

        # palindrome table
        palindrome = [[False] * n for _ in range(n)]

        # Fill palindrome table
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or palindrome[start + 1][end - 1]):
                    palindrome[start][end] = True

        # dp[i] = minimum cuts for s[0:i+1]
        dp = [0] * n

        for i in range(n):
            # If whole substring is palindrome, no cut needed
            if palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(i):
                    if palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]