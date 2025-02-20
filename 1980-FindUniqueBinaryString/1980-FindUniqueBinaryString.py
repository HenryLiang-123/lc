class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        result = []
        def dfs(path):
            if len(path) == n:
                if "".join(path[:]) not in nums:
                    result.append("".join(path[:]))
                    return True
                return False

            
            for element in ["0", "1"]:
                path.append(element)
                if dfs(path):
                    return True
                path.pop()

            return False

        dfs([])
        return result[0]

