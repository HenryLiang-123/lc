# Last updated: 4/1/2025, 4:55:37 PM
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        #check if it's a road and if it's in bounds
        def valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] <= 0

        #4 directions
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        #memo to keep track how many houses can reach this tile
        memo = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]

        #loop through the x axis of grid
        for i in range(len(grid)):
            #and y axis
            for j in range(len(grid[0])):
                #if grid isn't a house, skip to next iteration
                if grid[i][j] != 1:
                    continue
                #queue for bfs
                queue = deque([(i, j, 0)])
                #visited queue so you don't go in a circle
                visited = {(i,j)}

                #while queue isn't empty
                while queue:
                    # top of queue and how far this is from the house you started at
                    x, y, path = queue.popleft()

                    #travel all 4 directions 
                    for x_way, y_way in directions:
                        new_x, new_y = x + x_way, y + y_way

                        #check if valid and hasn't been visited
                        if valid(new_x, new_y) and not (new_x, new_y) in visited:

                            #add to queue, and increase the path value
                            queue.append((new_x, new_y, path + 1))

                            #subtract the amount of time it took to get here from the house you started at
                            # we use negative because i want to differentiate
                            #from the positive 1 and 2 of houses and obstacles
                            #if we see this via another house's bfs, then it will decrement even more,
                            #eventually giving us the total time to takes to get to this square from every house
                            grid[new_x][new_y] -= (path + 1)

                            #add to visited set for O(1) access so we don't revisit a node
                            visited.add((new_x, new_y))

                            #add 1 to the amount of houses that can reach this square
                            memo[new_x][new_y] += 1

        #gets the total number of houses in the grid
        house_number = sum([x.count(1) for x in grid])

        #sets answer to infinity
        ans = float('inf')

        #loop through the grid again
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #if the value at grid < 0, it means it's a path and has been visited by a house
                #also we want to check if it has been visited by every house, so we check if memo is the same number as house_number
                if grid[i][j] < 0 and memo[i][j] == house_number:
                    ans = min(-1 * grid[i][j], ans)
        
        #if answer is still infinity, it means that none of the road tiles can visit every house,
        #or there are no road tiles
        return ans if ans != float('inf') else -1        

