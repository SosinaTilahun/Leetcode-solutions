from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m = len(grid)
        n = len(grid[0])

        # health after entering starting cell
        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

        queue = deque([(0, 0, start_health)])

        # best health reached at each cell
        visited = [[0] * n for _ in range(m)]
        visited[0][0] = start_health

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c, h = queue.popleft()

            # reached destination
            if r == m-1 and c == n-1:
                return True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = h - grid[nr][nc]

                    if new_health > 0 and new_health > visited[nr][nc]:
                        visited[nr][nc] = new_health
                        queue.append((nr, nc, new_health))

        return False