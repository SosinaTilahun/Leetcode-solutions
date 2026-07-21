class Solution:
    def maxActiveSectionsAfterTrade(self, s):
        t = "1" + s + "1"

        # Create runs of consecutive characters
        groups = []
        count = 1

        for i in range(1, len(t)):
            if t[i] == t[i - 1]:
                count += 1
            else:
                groups.append((t[i - 1], count))
                count = 1

        groups.append((t[-1], count))

        original_ones = s.count("1")
        best_gain = 0

        # Look for a 1-block surrounded by 0-blocks
        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                if groups[i - 1][0] == '0' and groups[i + 1][0] == '0':
                    gain = groups[i - 1][1] + groups[i + 1][1]
                    best_gain = max(best_gain, gain)

        return original_ones + best_gain