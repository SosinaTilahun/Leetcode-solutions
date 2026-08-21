class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        # Minimum possible maximum gap
        bucket_size = max(1, (max_val - min_val) // (n - 1))

        # Number of buckets
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Each bucket stores [min, max]
        buckets = [[float('inf'), float('-inf')]
                   for _ in range(bucket_count)]

        # Put numbers into buckets
        for num in nums:
            index = (num - min_val) // bucket_size

            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        max_gap = 0
        previous_max = min_val

        # The maximum gap can only occur between buckets
        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):
                continue

            max_gap = max(max_gap, bucket_min - previous_max)
            previous_max = bucket_max

        return max_gap