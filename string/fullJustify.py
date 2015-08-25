class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        row = []
        cur_len = 0
        n = len(words)
        for wi in xrange(n):
            word = words[wi]
            if len(word)>maxWidth:
                break
            cur_len += (0 if cur_len == 0 else 1) +  len(word)
            row.append(word)
            if wi<n-1 and  (maxWidth - cur_len - 1)<len(words[wi+1]):
            # paste row to res
                row_s = ''
                if len(row) == 1:
                    gap = maxWidth-cur_len
                    rest_gap = 0
                else:
                    gap = (maxWidth - cur_len + len(row) - 1)//(len(row)-1)
                    rest_gap = (maxWidth - cur_len + len(row) - 1)%(len(row)-1)
                for i in xrange(len(row)):
                    w = row[i]
                    row_s += w 
                    if i < len(row) - 1 or len(row) == 1:
                        row_s += ' '*gap
                    if i < rest_gap:
                        row_s += ' '
                res.append(row_s)
                # start new row
                row = []
                cur_len = 0
            if wi == n-1:
                row_s = ''
                for  i in xrange(len(row)):
                    w = row[i]
                    row_s += w
                    if i < len(row)-1:
                        row_s += ' '
                row_s += ' ' * (maxWidth - len(row_s))
                res.append(row_s)
        return res        
            