class Solution:
    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, n):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # i again = reuse allowed
                path.pop()

        backtrack(0, [], 0)
        return res