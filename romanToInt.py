class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman_int = {'I':1, 'IV': 4, 'V':5, 'IX':9, 'X':10, 'L':50, 'XL':40, 'C': 100, 'XC':90,'D':500, 'CD': 400, 'M':1000, 'CM': 900}
        l = len(s)
        n = 0
        i = 0
        while i<l:
            if i+2<=l and s[i:i+2] in roman_int:
                n += roman_int[s[i:i+2]]
                i+=2
            elif s[i] in roman_int:
                n += roman_int[s[i]]
                i+=1
            else:
                return -1
        return n 
