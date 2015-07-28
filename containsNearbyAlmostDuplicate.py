class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k<1 or t<0:
            return False
        d = collections.OrderedDict()
        for n in nums:
            key = n if not t else n//t
            for m in (d.get(key-1),d.get(key),d.get(key+1)):
                if m is not None and abs(n-m)<=t:
                    return True
            if len(d)==k:
                d.popitem(False)
            d[key] = n
        return False
                
        