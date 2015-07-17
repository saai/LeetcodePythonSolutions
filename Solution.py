class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n < 1: return [0,]
        if n == 1: return [0,1]
        pre_bit = 1<<(n-1)
        lower = self.grayCode(n-1)
        return lower + [(pre_bit|i) for i in reversed(lower)]
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == 0: 
            return True
        dict1 = {s[0]:t[0],}
        dict2 = {t[0]:s[0],}
        for i in range(1,len(s)):
            if s[i] in dict1:
                vi = dict1[s[i]]
                if vi != t[i]:
                    return False
            else:
                if t[i] in dict2:
                    return False
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
        return True
    def permuteUnique(self, nums):
        if nums==None:
            return None
        if len(nums)==0:
            return None
        if len(nums)==1:
            return [nums,]
        first=nums[0]
        result=[]
        reduce_nums=nums[1:]
        perm_result = self.permuteUnique(reduce_nums)
        for i in range(0,len(perm_result)):
            for j in range(0, len(perm_result[i])+1):
                if (j-1>=0)&(first==perm_result[i][j-1]):
                   continue
                perm=[it for it in perm_result[i]]
                perm.insert(j,first)
                if perm not in result:
                    result.append(perm)
        return result
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
    def searchInsert(self, nums, target):
        n = len(nums)
        m = n/2
        if n==0:
            return 0
        if n==1:
            if nums[0]>=target:
                return 0
            else:
                return 1
        if nums[m]==target:
            return m
        elif nums[m]>target:
            return self.searchInsert(nums[0:m],target)
        else:
            if (m+1)==n:
                return n
            else:
                return (m+1)+self.searchInsert(nums[m+1:n],target)
                
    def numDistinct(self, s, t):
        m = len(t)
        n = len(s)
        #init mem matrix
        mem = []
        for i in range(0,m+1):
            row = []
            for j in range(0,n+1):
                row.append(0)
            mem.append(row)
        #set first line
        for j in range(0,n+1):
            mem[0][j] = 1
        for i in range(0,m):
            for j in range(0,n):
                if s[j]==t[i]:
                    mem[i+1][j+1] = mem[i+1][j] + mem[i][j]
                else:
                    mem[i+1][j+1] = mem[i+1][j]
        return mem[m][n]
    def level(self, n):
        m = n
        l = 0
        while(m>1):
            m = m/2
            l+=1
        return l
    def hammingWeight(self, n):
        if n == 0:
            return 0
        hw = 0
        while (n != 0) :
            if n&1 == 1:
                hw+=1
            n=n>>1        
        return hw
    def numTrees(self, n):
        if n == 0 : 
            return 0
        if n == 1:
            return 1
        c = [0,1]
        for i in range(2,n+1):
            count_ci = 0
            for j in range(0,i):
                l = j
                r = i-j-1
                if c[l]!=0 and c[r]!=0:
                    count_ci += c[l]*c[r]
                else:
                    count_ci += c[l]+c[r]
            c.append(count_ci)
                
        return c[n]
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(0,numCourses)]
        visit = [0 for _ in range(0, numCourses)]
        for prr in prerequisites:
            graph[prr[0]].append(prr[1])
            
        def dfs(i):
            if visit[i]==-1:
                return False
            elif visit[i]==1:
                return True
            visit[i]=-1
            for j in graph[i]:
                if dfs(j)== False:
                    return False
            visit[i]=1
            return True
        for i in range(0,numCourses):
            if dfs(i)==False:
                return False
        return True
    
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        order = []
        def dfs(i):
            if visit[i]==-1:
                return None
            if visit[i]==1:
                return order
            visit[i]=-1
            for j in graph[i]:
                r = dfs(j)
                if r == None:
                    return None
            visit[i]=1
            order.append(i)
            return order
        for i in xrange(numCourses):
            r = dfs(i) 
            if r == None:
                return []
        return order

    def sortedArrayToBST(self, nums):
        n = len(nums)
        if n == 0 :
            return None
        if n == 1:
            return TreeNode(nums[0])
        m = n/2
        left_nums = nums[0:m]
        right_nums = nums[m+1:n]
        left_node = self.sortedArrayToBST(left_nums)
        right_node = self.sortedArrayToBST(right_nums)
        node = TreeNode(nums[m])
        node.left = left_node
        node.right = right_node
        return node
        
    def sortedListToBST(self, head):
        if head == None:
            return None
        arr = []
        while (head != None):
            arr.append(head.val)
            head = head.next
        return self.sortedArrayToBST(arr)
        
    def sLToBST(self,head, n):
        if head==None:
            return None
        if n == 0:
            return None
        if n == 1:
            return TreeNode(head.val)
        m = n/2
        i = 0
        p = head
        while i<m:
            p = p.next
            i+=1
        node = TreeNode(p.val)
        node.left = self.sLToBST(head,m)
        node.right = self.sLToBST(p.next,n-m-1)
        return node
    def twoSum(self, nums, target):
        n = len(nums)
        dict = {}
        for i in xrange(n):
            t = target - nums[i]
            if t in dict:
                return [dict[t]+1,i+1]
            dict[nums[i]] = i
        return []

   #check the value in i, j is valid
    def isValidSudoku(self, board,i,j):
        v = board[i][j]
        if v == '.':
            return True
        if int(v)>9:
            return False
        for n in xrange(9):
            c_hor = board[i][n]
            if c_hor == v and n != j:
                return False
            c_ver = board[n][j]
            if c_ver == v and n != i:
                return False
        for n in xrange(3):
            for m in xrange(3):
                i_hor = (i/3)*3+n
                j_ver = (j/3)*3+m
                c_temple = board[i_hor][j_ver]
                if c_temple == v and (i !=i_hor or j !=j_ver):
                    return False
        return True
                
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        indexes = []
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    index= i*9+j
                    indexes.append(index)
        l = len(indexes)
        p = 0
        while (p >= 0 and p < l):
            index = indexes[p]
            i = index/9
            j = index%9
            if board[i][j] == '.':
                # fill new 
                for q in range(1,10):
                    board[i][j] = str(q)
                    if self.isValidSudoku(board, i,j) == True:
                        break
                    else :
                        board[i][j] = '.'
                if board[i][j] == '.':
                    p-=1 # back trace
                else:
                    p+=1 # next
            else:
                if board[i][j]=='9':
                    board[i][j] = '.'
                    p -= 1
                    continue
                #else
                board[i][j] = str(int(board[i][j]) + 1)
                while(self.isValidSudoku(board,i,j)==False):
                    if board[i][j] == '9':
                        break
                    else:
                        board[i][j] = str(int(board[i][j])+1)
                if self.isValidSudoku(board, i, j):
                    p +=1 #next
                else:
                    board[i][j] = '.'
                    p -=1 # back trace
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
    
