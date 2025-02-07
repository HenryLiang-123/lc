class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        color_to_freq = {}
        ball_to_color = {}
        result = []
        for ball, color in queries:
            if ball not in ball_to_color:
                ball_to_color[ball] = color
                color_to_freq[color] = color_to_freq.get(color, 0) + 1
            else:
                original_color = ball_to_color[ball]
                ball_to_color[ball] = color
                color_to_freq[original_color] -= 1
                if color_to_freq[original_color] == 0:
                    del color_to_freq[original_color]
                color_to_freq[color] = color_to_freq.get(color, 0) + 1
            result.append(len(color_to_freq))
        
        return result

