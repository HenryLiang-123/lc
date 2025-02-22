class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def dfs(path, start):
            # if path not in result:
            result.append(path[:])

            for i in range(start, n):
                curr = nums[i]
                path.append(curr)
                dfs(path, i+1)
                path.pop()
                
                    

        dfs([], 0)
        return result