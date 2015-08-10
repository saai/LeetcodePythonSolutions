class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        for c in t:
            if c not in s_dict:
                return False
            else:
                s_dict[c] -= 1
                if s_dict[c] < 0:
                    return False
        return True
                