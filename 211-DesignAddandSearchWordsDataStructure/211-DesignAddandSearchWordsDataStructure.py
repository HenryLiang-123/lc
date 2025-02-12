class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.isWord = True

    def search(self, word: str) -> bool:
        # curr_node = self.root
        n = len(word)
        def dfs(curr_node, start):
            for i in range(start, n):
                c = word[i]
                if c == ".":
                    for nei in curr_node.children.values():
                        if dfs(nei, i+1):
                            return True
                    return False
                else:
                    if c not in curr_node.children:
                        return False
                    curr_node = curr_node.children[c]

            return curr_node.isWord

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)