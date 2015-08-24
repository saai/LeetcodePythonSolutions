class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 0
        num = '1'
        for i in range(1,n):
            new_num = ''
            j = 0
            while(j<len(num)):
                count = 1
                while j+1 < len(num) and num[j+1] == num[j]:
                    j += 1
                    count += 1
                new_num += str(count) + str(num[j])
                j += 1
            num = new_num
        return num
                    