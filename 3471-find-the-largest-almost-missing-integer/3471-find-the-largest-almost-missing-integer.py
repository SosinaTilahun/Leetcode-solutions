class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        # Count how many subarrays of size k contain each number
        count = {}

        for i in range(n - k + 1):
            window = set(nums[i:i + k])

            for x in window:
                count[x] = count.get(x, 0) + 1

        # Find the largest number that appears
        # in exactly one subarray
        answer = -1

        for x in count:
            if count[x] == 1:
                answer = max(answer, x)

        return answer