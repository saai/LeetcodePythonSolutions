class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        cur = self.root
        for c in word:
            cur = cur.children.get(c)
            if not cur:
                return False
        return cur.is_word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if not cur:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        nr = len(board)
        nc = len(board[0])
        isVisited = [[False for j in xrange(nc)] for i in xrange(nr)]
        def dfs(i,j,s,trie,res):
            if i >=nr or i < 0 or j >=nc or j < 0:
                return 
            if isVisited[i][j]:
                return 
            s += board[i][j]
            if not trie.startsWith(s):
                return 
            if trie.search(s):
                res.append(s)
                
            isVisited[i][j] = True
            dfs(i-1,j,s,trie,res)
            dfs(i+1,j,s,trie,res)
            dfs(i,j-1,s,trie,res)
            dfs(i,j+1,s,trie,res)
            isVisited[i][j] = False
        
        for i in xrange(nr):
            for j in xrange(nc):
                if trie.startsWith(board[i][j]):
                    dfs(i,j,'',trie,res)
        return res
            