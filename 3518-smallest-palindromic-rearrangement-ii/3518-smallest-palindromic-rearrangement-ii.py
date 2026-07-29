class Solution:
    MAX_K = 1000001

    def smallestPalindrome(self, s, k):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        mid = ""

        for i in range(26):
            if freq[i] % 2:
                mid = chr(ord('a') + i)
                freq[i] -= 1
                break

        half = [x // 2 for x in freq]
        half_len = sum(half)

        if k > self.multinomial(half):
            return ""

        left = []

        for _ in range(half_len):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = self.multinomial(half)

                if ways >= k:
                    left.append(chr(ord('a') + c))
                    break
                else:
                    k -= ways
                    half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def multinomial(self, counts):
        total = sum(counts)
        ans = 1

        for cnt in counts:
            ans *= self.binom(total, cnt)

            if ans >= self.MAX_K:
                return self.MAX_K

            total -= cnt

        return ans

    def binom(self, n, r):
        if r > n:
            return 0

        r = min(r, n - r)

        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - i + 1) // i

            if ans >= self.MAX_K:
                return self.MAX_K

        return ans