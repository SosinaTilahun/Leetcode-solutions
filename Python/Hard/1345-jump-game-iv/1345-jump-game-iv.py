from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        queue = deque([(0, 0)])
        visited = set([0])

        while queue:
            i, steps = queue.popleft()

            if i == n - 1:
                return steps

            neighbors = graph[arr[i]] + [i - 1, i + 1]

            for nei in neighbors:
                if 0 <= nei < n and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, steps + 1))

            # Avoid revisiting same-value indices again
            graph[arr[i]] = []