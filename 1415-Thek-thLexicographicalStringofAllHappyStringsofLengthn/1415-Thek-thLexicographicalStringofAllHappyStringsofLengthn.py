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
        def dfs(path):
            if len(path) == n:
                result.append("".join(path[:]))
                return
            
            for letter in ["a", "b", "c"]:
                if letter != path[-1]:
                    path.append(letter)
                    dfs(path)
                    path.pop()

        dfs(start_path)
        idx = k % (2**(n-1)) - 1
        print(result, idx)
        return result[idx]