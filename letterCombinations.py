class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        l_dict = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n = len(digits)
        res = []
        def dfs(path, digits, res, l_dict):
            if not digits:
                if len(path) > 0:
                    res.append(''.join(path[:]))
                return 
            digit = digits[0]
            ls = l_dict[digit]
            if not ls:
                dfs(path, digits[1:],res, l_dict)
                return 
            for l in ls:
                path.append(l)
                dfs(path, digits[1:],res,l_dict)
                path.pop()
        dfs([],digits, res, l_dict)    
        return res