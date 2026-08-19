class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Every completely empty row can fit 2 groups
        result = 2 * n

        # Only process rows that have reservations
        for seats in rows.values():

            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            # This row was counted as 2 groups,
            # so replace that count with its actual capacity.
            if left and right:
                continue

            elif left or middle or right:
                result -= 1

            else:
                result -= 2

        return result