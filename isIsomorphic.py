class Solution:
	def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == 0: 
            return True
        dict1 = {s[0]:t[0],}
        dict2 = {t[0]:s[0],}
        for i in range(1,len(s)):
            if s[i] in dict1:
                vi = dict1[s[i]]
                if vi != t[i]:
                    return False
            else:
                if t[i] in dict2:
                    return False
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
        return True