class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        elements = [(position[i], speed[i]) for i in range(n)] 
        elements.sort(reverse=True)

        time = (target - elements[0][0]) / elements[0][1]
        print(elements)
        result = 1

        for i in range(1, n):
            curr_position, curr_speed = elements[i]
            curr_time = (target - curr_position) / curr_speed
            if curr_time > time:
                result += 1
                time = curr_time

        return result