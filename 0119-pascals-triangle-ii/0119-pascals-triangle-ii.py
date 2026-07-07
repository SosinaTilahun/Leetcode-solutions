class Solution:
    def getRow(self, rowIndex):
        row = [1]

        for i in range(1, rowIndex + 1):
            newRow = [1] * (i + 1)

            for j in range(1, i):
                newRow[j] = row[j - 1] + row[j]

            row = newRow

        return row