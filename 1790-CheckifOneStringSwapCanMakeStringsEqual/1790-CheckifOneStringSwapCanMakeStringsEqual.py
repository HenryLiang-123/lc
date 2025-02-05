class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        swap_map = {} #s1 to s2
        swaps_needed = 0
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            else:
                swaps_needed += 1
                swap_map[s1[i]] = s2[i]


        if swaps_needed == 0:
            return True

        if swaps_needed != 2:
            return False

        if len(swap_map) != 2:
            return False

        keys = list(swap_map.keys())

        print(swap_map)
        
        if swap_map[keys[0]] != keys[1] or keys[0] != swap_map[keys[1]]:
            return False

        return True