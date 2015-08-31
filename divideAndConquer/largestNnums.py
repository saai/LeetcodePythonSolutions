class Solution:
	def largetstNnumber(self, nums, n):
		if len(nums) <= n:
			return nums
		self.largetstNnumberHelper(nums,n, 0,len(nums)-1)
		return nums[:n]

	def largetstNnumberHelper(self, nums,n,sidx,eidx):
		print n, sidx,eidx
		if n == 0 or (eidx-sidx+1)<n:
			return 
		i = sidx
		j = eidx
		pivot = nums[(sidx+eidx)/2]
		while(i<=j):
			while(nums[i]>pivot):
				i += 1
			while(nums[j]<pivot):
				j -= 1
			if (i<=j):
				t = nums[i]
				nums[i]= nums[j]
				nums[j] = t 
				i += 1
				j -= 1
		l = 0
		if i > sidx :
			l = i-sidx
		if l == n:
			return 
		elif l < n:
			m = n - l 
			self.largetstNnumberHelper(nums,m, i,eidx)
		else:
			self.largetstNnumberHelper(nums,n,sidx,i-1)