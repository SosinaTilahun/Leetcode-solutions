class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        left = 0
        right = n - 1

        while left < right:
            a = nums[left]
            b = nums[right]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            diff[2] += 2

            diff[low] -= 1
            diff[s] -= 1
            diff[s + 1] += 1
            diff[high + 1] += 1

            left += 1
            right -= 1

        ans = float('inf')
        curr = 0

        for x in range(2, 2 * limit + 1):
            curr += diff[x]
            ans = min(ans, curr)

        return ans