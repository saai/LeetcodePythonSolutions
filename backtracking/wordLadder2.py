class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        arr1 = {start}
        parents = collections.defaultdict(set)
        while(len(arr1) != 0 and end not in parents):
            level = collections.defaultdict(set)
            for word in arr1:
                wl = len(word)
                for j in xrange(wl):
                    c = word[j]
                    for n in range(ord('a'),ord('z')):
                        if chr(n) == c:
                            continue
                        new_word = word[:j]+chr(n)+word[j+1:]
                        if new_word in dict and new_word not in parents: 
                            level[new_word].add(word)
            parents.update(level)
            arr1 = level
        res = [[end]]
        while(res and res[0][0] != start):
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res   