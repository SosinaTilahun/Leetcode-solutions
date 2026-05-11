class Solution:
    def separateDigits(self, nums):
        res = []

        for num in nums:
            for ch in str(num):
                res.append(int(ch))

        return res