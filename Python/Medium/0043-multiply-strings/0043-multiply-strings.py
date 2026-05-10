class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        # reverse loop (like manual multiplication)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)

                pos1 = i + j
                pos2 = i + j + 1

                total = mul + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        # convert to string (skip leading zeros)
        result = []
        for num in res:
            if not (len(result) == 0 and num == 0):
                result.append(chr(num + 48))

        return "".join(result) if result else "0"