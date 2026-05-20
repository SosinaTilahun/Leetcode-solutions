class Solution:
    def combine(self, n, k):

        result = []

        def backtrack(start, path):

            if len(path) == k:
                result.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)

                backtrack(num + 1, path)

                path.pop()

        backtrack(1, [])

        return result