class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        l = len(digits) 
        if l== 0:
            return [1]
        last = digits[l-1]
        last += 1
        if last < 10:
            return digits[0:l-1]+[last]
        else:
            last -=10
            return self.plusOne(digits[0:l-1])+[last]
            