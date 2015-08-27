class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        n1 = len(version1)
        n2 = len(version2)
        i = j = 0
        while(i<n1 or j<n2):
            v1 = '0'
            while(i<n1 and version1[i]!='.'):
                v1 += version1[i]
                i += 1
            v2 = '0'
            while(j<n2 and version2[j]!= '.'):
                v2 += version2[j]
                j += 1
            if len(v1)==1 and len(v2) == 1:
                return 0
            elif int(v1) == int(v2):
                i += 1 
                j += 1
                continue
            else:
                return (-1 if int(v1)<int(v2) else 1)
        return 0