# Last updated: 4/6/2025, 5:42:27 PM
import pprint
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0] = [nums[0]]
        

        for i in range(1, n):
            # print(dp)
            curr_element = nums[i]
            max_len = 0
            curr_dp = []
            for j in range(i):
                if curr_element % nums[j] == 0:
                    candidate_len = len(dp[j])
                    if candidate_len > max_len:
                        max_len = candidate_len
                        curr_dp = dp[j][:]
            curr_dp.append(curr_element)
            dp[i] = curr_dp

        final_len = 0
        result = []
        # print(dp)
        for candidate in dp:
            curr_len = len(candidate)
            if curr_len > final_len:
                final_len = curr_len
                result = candidate

        return result

