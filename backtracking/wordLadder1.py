class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        arr1 = [beginWord]
        arr2 = [endWord]
        isVisited = {w:False for w in wordDict}
        h = 1
        while(len(arr1) != 0 and len(arr2)!= 0):
            if len(arr1)>len(arr2):
                temp = arr1
                arr1 = arr2
                arr2 = temp
            l1 = len(arr1)
            mediums = []
            h += 1
            for i in xrange(l1):
                word = arr1[i]
                wl = len(word)
                for j in xrange(wl):
                    c = word[j]
                    for n in range(ord('a'),ord('z')):
                        if chr(n) == c:
                            continue
                        new_word = word[:j]+chr(n)+word[j+1:]
                        if new_word in arr2:
                            return h
                        if new_word in wordDict and not isVisited[new_word]:
                            isVisited[new_word] = True
                            mediums.append(new_word)
            arr1 = mediums
        return 0   