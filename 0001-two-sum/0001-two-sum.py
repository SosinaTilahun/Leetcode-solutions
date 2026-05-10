class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # number -> index

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the needed pair already exists
            if complement in seen:
                return [seen[complement], i]

            # Store current number with its index
            seen[num] = i