class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        trie=self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'
    def search(self, word, trie = None):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not trie:
            trie = self.trie
        if not word:
            if '#' in trie:
                return True
            else:
                return False
        c = word[0]
        if c in trie:
            return self.search(word[1:],trie[c])
        elif c == '.':
            for cc in trie:
                if cc != '#' and self.search(word[1:],trie[cc]):
                    return True
        return False
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")