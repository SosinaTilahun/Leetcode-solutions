class Solution:
    def partition(self, s):
        result = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, path):
            # If we used the whole string, save the partition
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible substring
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if is_palindrome(start, end):
                    path.append(substring)

                    backtrack(end + 1, path)

                    path.pop()

        backtrack(0, [])

        return result