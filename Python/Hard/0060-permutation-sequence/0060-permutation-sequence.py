class Solution:
    def getPermutation(self, n, k):
        numbers = []
        fact = 1

        for i in range(1, n + 1):
            numbers.append(str(i))
            fact *= i

        k -= 1
        result = ""

        for i in range(n, 0, -1):
            fact //= i

            index = k // fact
            result += numbers[index]

            numbers.pop(index)

            k %= fact

        return result