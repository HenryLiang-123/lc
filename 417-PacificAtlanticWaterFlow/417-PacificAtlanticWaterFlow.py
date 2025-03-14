from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # flow backwards fro P and A
        possible_dir = [(1,0), (-1,0), (0,-1), (0,1)]
        n = len(heights)
        m = len(heights[0])

        def bfs(q, seen):
            while q:
                x,y = q.popleft()
                for dx, dy in possible_dir:
                    nx, ny = x+dx, y+dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in seen and heights[nx][ny] >= heights[x][y]:
                        seen.add((nx, ny))
                        q.append((nx, ny))

            return seen

        q_pac = deque([])
        q_atl = deque([])

        seen_pac = set()
        seen_atl = set()

        for i in range(n):
            q_pac.append((i, 0))
            seen_pac.add((i, 0))
            q_atl.append((i, m-1))
            seen_atl.add((i, m-1))

        for i in range(m):
            q_pac.append((0, i))
            seen_pac.add((0, i))
            q_atl.append((n-1, i))
            seen_atl.add((n-1, i))

        seen_pac = bfs(q_pac, seen_pac)
        seen_atl = bfs(q_atl, seen_atl)

        return list(seen_pac & seen_atl)


                
            