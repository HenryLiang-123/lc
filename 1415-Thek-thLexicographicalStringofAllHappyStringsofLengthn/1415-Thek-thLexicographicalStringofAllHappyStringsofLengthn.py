// Last updated: 2/19/2025, 2:23:28 PM
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_elements = 3 * 2**(n-1)
        if total_elements < k:
            return ""

        num_to_start = {
            1: ["a"],
            2: ["b"],
            3: ["c"]
        }


        start_path = num_to_start[math.ceil(k / (2**(n-1)))]
        result = []
        needed =  k % (2**(n-1))
        if needed == 0:
            needed = k

        def dfs(path):
            nonlocal needed
            if needed > 0:
                if len(path) == n:
                    result.append("".join(path[:]))
                    needed -= 1
                    return 
                
                for letter in ["a", "b", "c"]:
                    if letter != path[-1] :
                        path.append(letter)
                        dfs(path)
                        path.pop()
                        
        dfs(start_path)
        
        return result[-1]
