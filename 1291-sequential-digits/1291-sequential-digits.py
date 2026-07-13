class Solution:
    def sequentialDigits(self, low, high):
        result = []

        digits = "123456789"

        # Try every length
        for length in range(2, 10):
            # Try every starting position
            for start in range(10 - length):
                num = int(digits[start:start + length])

                if low <= num <= high:
                    result.append(num)

        return sorted(result)