from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # Build paths using BFS
        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()

            # Remove current level words to avoid revisiting
            for word in level:
                wordSet.discard(word)

            for word in level:
                word_list = list(word)

                for i in range(len(word)):
                    original = word_list[i]

                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original:
                            continue

                        word_list[i] = c
                        new_word = ''.join(word_list)

                        if new_word in wordSet:
                            if new_word == endWord:
                                found = True

                            next_level.add(new_word)
                            parents[new_word].append(word)

                    word_list[i] = original

            level = next_level

        if not found:
            return []

        # DFS to build all paths
        result = []

        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])

        return result