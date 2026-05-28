class TrieNode:
    def __init__(self):
        self.children = {}
        self.best = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        
        # Returns True if idx1 is a better candidate than idx2
        def better(idx1, idx2):
            if idx2 == -1:
                return True
            
            if len(wordsContainer[idx1]) < len(wordsContainer[idx2]):
                return True
            
            if len(wordsContainer[idx1]) == len(wordsContainer[idx2]):
                return idx1 < idx2
            
            return False

        root = TrieNode()

        # Build trie with reversed words
        for i, word in enumerate(wordsContainer):
            rev = word[::-1]

            # Update root best
            if better(i, root.best):
                root.best = i

            node = root

            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if better(i, node.best):
                    node.best = i

        ans = []

        # Process queries
        for query in wordsQuery:
            rev = query[::-1]

            node = root

            for ch in rev:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best)

        return ans