from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        # Safe removal
        wordSet.discard(beginWord)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            chars = list(word)

            for i in range(len(word)):
                original = chars[i]

                for c in 'abcdefghijklmnopqrstuvwxyz':
                    chars[i] = c
                    new_word = ''.join(chars)

                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, steps + 1))

                chars[i] = original

        return 0