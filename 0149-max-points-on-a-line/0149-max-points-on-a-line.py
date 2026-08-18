class Solution:
    def maxPoints(self, points):

        def gcd(a, b):
            a = abs(a)
            b = abs(b)

            while b:
                a, b = b, a % b

            return a

        n = len(points)

        if n <= 2:
            return n

        answer = 0

        for i in range(n):
            slopes = {}

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Vertical line
                if dx == 0:
                    slope = (1, 0)

                # Horizontal line
                elif dy == 0:
                    slope = (0, 1)

                else:
                    g = gcd(dx, dy)

                    dx //= g
                    dy //= g

                    # Keep the direction consistent
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

            if slopes:
                answer = max(answer, max(slopes.values()) + 1)

        return answer