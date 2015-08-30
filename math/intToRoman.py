class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = ['','I','II','III','IV','V','VI','VII','VIII','IX',\
                  '','X','XX','XXX','XL','L','LX','LXX','LXXX','XC',\
                  '','C','CC','CCC','CD','D','DC','DCC','DCCC','CM',\
                  '','M','MM','MMM','MMM']
        return romans[(num/1000)+30]+romans[(num/100)%10 + 20]+romans[(num/10)%10+10]+romans[num%10] 