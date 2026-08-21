class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # We are going uphill, so a peak exists on the right
                left = mid + 1
            else:
                # We are going downhill, so a peak exists here or on the left
                right = mid

        return left