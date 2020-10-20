class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord
        #{'a':Node, 'b':Node, ...}
        self.children = children
        
class Solution:
    def build(self, words):
        tree = Node(False, {})
        for word in words:
            current = tree
            for char in word:
                if not char in current.children:
                    current.children[char] = Node(False,{})
                current = current.children[char]
            current.isWord = True
        self.tree = tree
        
    def autocomplete(self, word):
        current = self.tree
        for char in word:
            if not char in current.children:
                return []
            current = current.children[char]
            
        words = []
        self.dfs(current, word, words)        
        return words
    
    def dfs(self, node, prefix, words):
        if node.isWord:
            words.append(prefix)
        for char in node.children:
            self.dfs(node.children[char], prefix + char, words)
            
s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']