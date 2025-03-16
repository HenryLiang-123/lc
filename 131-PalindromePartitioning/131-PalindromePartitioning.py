class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pali(substr):
            return substr == substr[::-1]

        result = []
        n = len(s)
        def dfs(start, path):
            if start == n:
                result.append(path[:])
                return

            for i in range(start, n):
                substr = s[start:(i+1)]
                if is_pali(substr):
                    path.append(substr)
                    dfs(i+1, path)
                    path.pop()

        
        dfs(0, [])

        return result