class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def searchHelper(root, pos: int):
            if pos == len(word):
                return root.endOfWord
            
            if word[pos] in root.children:
                curr = root.children[word[pos]]
                return searchHelper(curr, pos + 1)
            
            if word[pos] == ".":
                for c in root.children:
                    res = searchHelper(root.children[c], pos + 1)

                    if res:
                        return True
                
                return False
            
            return False
        
        return searchHelper(self.root, 0)

    

