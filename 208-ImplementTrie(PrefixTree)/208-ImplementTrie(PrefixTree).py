class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.word = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]

        return curr_node.word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)