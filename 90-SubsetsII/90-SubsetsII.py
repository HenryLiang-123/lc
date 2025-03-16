// Last updated: 3/16/2025, 3:11:15 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        def dfs(start, path):
            result.append(path[:])

            for i in range(start, n):
                if i == start:
                    path.append(nums[i])
                    dfs(i +1, path)
                    path.pop()
                else:
                    if nums[i] != nums[i-1]:
                        path.append(nums[i])
                        dfs(i +1, path)
                        path.pop()

        dfs(0, [])
        return result