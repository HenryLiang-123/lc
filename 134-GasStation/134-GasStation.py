class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        deficit = [gas[i] - cost[i] for i in range(n)]
        result = 0
        curr_deficit = 0
        if sum(deficit) < 0:
            return -1

        for i in range(n):
            curr_deficit += deficit[i]
            if curr_deficit < 0:
                result = i + 1
                curr_deficit = 0

        return result