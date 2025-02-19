class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(left_count, right_count, path):
            if left_count == right_count == n:
                result.append("".join(path[:]))
                return

            if left_count < n:
                path.append("(")
                dfs(left_count + 1, right_count, path)
                path.pop()

            if right_count < left_count:
                path.append(")")
                dfs(left_count, right_count + 1, path)
                path.pop()

        dfs(0, 0, [])
        return result
