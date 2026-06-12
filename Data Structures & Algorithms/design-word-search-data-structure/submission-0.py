class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
        cur.isEOW = True   

    def search(self, word: str) -> bool:
        def helper(pointer, word):
            if not word:
                return pointer.isEOW
            if word[0]=='.':
                for child in pointer.children.values():
                    if helper(child, word[1:]):
                        return True
                return False
            c = word[0]
            if c not in pointer.children:
                return False
            return helper(pointer.children[c], word[1:])        
        return helper(self.root,word)
        
class PrefixNode:
    def __init__(self):
        self.children = {}
        self.isEOW = False
