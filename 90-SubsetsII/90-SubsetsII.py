// Last updated: 2/21/2025, 6:05:58 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # nums_set = set(nums)
        n = len(nums)
        result = []
        def dfs(path, start):
            result.append(path[:])


            for i in range(start, n):
                if i != start and nums[i] == nums[i-1]:
                    continue
                # if nums[i] not in path:
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()


        dfs([], 0)
        return result
