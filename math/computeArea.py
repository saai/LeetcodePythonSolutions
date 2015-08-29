class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rec = (C-A)*(D-B) + (G-E)*(H-F)
        left = max(E,A)
        right = max(min(G,C),left)
        bottom = max(B,F)
        top = max(min(D,H),bottom)
        rec -=(right-left)*(top-bottom)
        return rec