class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        sumGas = 0
        sumCost = 0
        start = 0
        tank = 0
        for i in xrange(n):
            sumGas += gas[i]
            sumCost += cost[i]
            tank += gas[i]-cost[i]
            if tank < 0:
                start = i+1
                tank = 0
        if sumGas-sumCost < 0:
            return -1
        else:
            return start

    def canCompleteCircuitSlow(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        gains = [gas[i]-cost[i] for i in xrange(n)]
        i = 0
        while(i < n):
            if gains[i]<0:
                i += 1
                continue
            tank = 0
            step = 0
            while(step<n and tank >= 0):
                cur = (i + step)%n
                tank += gains[cur]
                step += 1
            if step == n and tank >= 0:
                return i
            i += step 
        return -1