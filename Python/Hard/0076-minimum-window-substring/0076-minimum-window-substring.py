class Solution:
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)
        formed = 0

        window = {}

        left = 0
        min_len = float('inf')
        result = ""

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            # Try shrinking window
            while left <= right and formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return result