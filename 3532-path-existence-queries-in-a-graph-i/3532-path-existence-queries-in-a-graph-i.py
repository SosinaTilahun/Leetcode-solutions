class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                parent[pb] = pa

        # Connect neighboring nodes
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                union(i, i-1)

        answer = []

        for u, v in queries:
            answer.append(find(u) == find(v))

        return answer