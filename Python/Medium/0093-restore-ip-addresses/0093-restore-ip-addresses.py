class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, path):

            # If 4 parts are formed
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            # Try segment lengths 1 to 3
            for length in range(1, 4):

                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero check
                if len(part) > 1 and part[0] == '0':
                    continue

                # Range check
                if int(part) <= 255:
                    path.append(part)
                    backtrack(start + length, path)
                    path.pop()

        backtrack(0, [])
        return result