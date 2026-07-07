class Solution:
    def sumAndMultiply(self, n):
        s = "".join(ch for ch in str(n) if ch != "0")

        if not s:
            return 0

        x = int(s)
        digit_sum = sum(int(ch) for ch in s)

        return x * digit_sum