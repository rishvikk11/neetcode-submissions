class Node:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    # when period, we need to traverse through all children of our current root to see if the word exists
                    # bypass the current letter cuz of the "." and look at all the children of all possible current letters
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.isLeaf
        return dfs(0, self.root)

