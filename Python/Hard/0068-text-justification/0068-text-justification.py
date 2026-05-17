class Solution:
    def fullJustify(self, words, maxWidth):

        result = []
        i = 0

        while i < len(words):

            # Find words that fit in current line
            line_words = []
            line_length = 0

            while i < len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1

            # Number of spaces needed
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            # Last line or single word -> left justify
            if i == len(words) or gaps == 0:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))

            else:
                # Evenly distribute spaces
                space_each = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for j in range(gaps):
                    line += line_words[j]
                    line += ' ' * (space_each + (1 if j < extra_spaces else 0))

                line += line_words[-1]

            result.append(line)

        return result