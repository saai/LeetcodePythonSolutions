class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        h1 = {}
        n = len(secret)
        bulls = 0
        cows = 0
        for i in xrange(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                h1[secret[i]] = h1[secret[i]] + 1 if secret[i] in h1 else 1
                h1[guess[i]] = h1[guess[i]]-1 if guess[i] in h1 else -1
        for key, value in h1.iteritems():
            if value <= 0:
                # only appears in guess
                continue
            else:
                # appears in secret, and might be decreased by guess 
                cows += value
        cows = n-bulls- cows        
        return str(bulls)+'A'+str(cows)+'B'