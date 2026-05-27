class Solution:
    def numberOfSpecialChars(self, word):
        count = 0

        for char in 'abcdefghijklmnopqrstuvwxyz':

            # Check if both lowercase and uppercase exist
            if char in word and char.upper() in word:

                # Last lowercase position
                last_lower = word.rfind(char)

                # First uppercase position
                first_upper = word.find(char.upper())

                # Lowercase must come before uppercase
                if last_lower < first_upper:
                    count += 1

        return count