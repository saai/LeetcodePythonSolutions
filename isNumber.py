class Solution:
	def removeSpaces(self,s):
        n = len(s)
        i = 0
        j = n-1
        while i < n and s[i]==' ':
            i+=1
        while j > -1 and s[j]==' ' :
            j-=1
        return s[i:j+1]
    def isNumber(self, s):
        s = self.removeSpaces(s)
        n = len(s)
        if n == 0:
            return False
        i = 0
        dotFlag = False
        EFlag = False
        hasDigit = False
        hasSign = False
        while i < n:
            if s[i].isdigit():
                i+=1
                hasDigit = True
                hasSign = True
            elif not dotFlag and s[i]=='.':
                i+=1
                dotFlag = True
                hasSign = True
            elif hasDigit and not EFlag and (s[i]=='e' or s[i]=='E'):
                i+=1
                dotFlag = True
                EFlag = True
                hasDigit = False
                hasSign = False
            elif not hasDigit and not hasSign and (s[i]=='+' or s[i]=='-'):
                i+=1
                hasSign = True
            else :
                return False
        if not hasDigit:
            return False
        else :
            return True