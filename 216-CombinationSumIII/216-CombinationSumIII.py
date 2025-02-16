class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        seen = set()
        possible_values = [i for i in range(1, 10)]
        def dfs(path, path_sum, start):
            if len(path) == k and path_sum == n:
                res.append(path[:])
                return

            if len(path) < k and path_sum > n:
                return

            
            for i in range(start, len(possible_values)):    
                curr = possible_values[i]
                path.append(curr)
                path_sum += curr      
                dfs(path, path_sum, i+1)
                path.pop()
                path_sum -= curr

            

        dfs([], 0, 0)
        return res

        
            
