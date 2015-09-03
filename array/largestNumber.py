class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s = [str(num) for num in nums]
        self.qsort(s, 0, len(s)-1)
        if s[0] == '0':
            return '0'
        return ''.join(s)
        
    def qsort(self, s, left, right):
        i = left
        j = right
        pivot = s[(left+right)/2]
        while(i<=j):
            while(i<=right and self.compare(s[i],pivot)>0):
                i += 1
            while(j>=left and self.compare(s[j],pivot) <0):
                j -= 1
            if (i<=j):
                t = s[i]
                s[i] = s[j]
                s[j] =t
                i += 1
                j -= 1
        if j > left:
            self.qsort(s, left, j)
        if i < right:
            self.qsort(s, i, right)
            
    def compare(self, str1,str2):
        v1 = int(str1+str2)
        v2 = int(str2+str1)
        if v1>v2: 
            return 1
        elif v1 == v2:
            return 0
        else:
            return -1