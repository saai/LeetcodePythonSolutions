class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        res =[]
        def addPoint(frontStr,restStr,pointNum):
            if pointNum==0:
                if self.isValidSection(restStr):
                    r = frontStr[1::] + restStr
                    res.append(r)
                return
            l = len(restStr)
            fp_len = 1
            rp_len = l - fp_len
            while(fp_len <=3 and rp_len>=pointNum and rp_len<=(pointNum+1)*3):
                curSection = restStr[0:fp_len]  
                if self.isValidSection(curSection):
                    newFrontStr = frontStr + curSection+'.'
                    addPoint(newFrontStr,restStr[fp_len:l],pointNum-1)
                fp_len += 1
                rp_len = l-fp_len
        addPoint('.',s,3)
        return res
    def isValidSection(self, s):
        if len(s)==0 or len(s)>3 or (s[0] == '0' and len(s)!=1)or int(s)>255:
            return False
        return True

