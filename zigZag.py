class Solution:
	# zig zag 
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows = []
        for i in xrange(numRows):
            rows.append([])
        i = 0
        plus = True
        for j in xrange(len(s)):
            rows[i].append(s[j])
            if i == 0:
                plus = True
            elif i == (numRows-1):
                plus = False
            if plus:
                i += 1
            else:
                i -= 1
        new_s = ''
        for i in xrange(numRows):
            new_s += ''.join(rows[i])
        return new_s
    
