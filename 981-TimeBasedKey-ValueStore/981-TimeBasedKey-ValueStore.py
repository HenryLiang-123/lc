class TimeMap:

    def __init__(self):
        self.key_to_time = defaultdict(list)
        self.time_to_value = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_time[key].append(timestamp)
        self.time_to_value[timestamp] = value
        
    def search(self, times, target):
        n = len(times)
        left = 0 
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if times[mid] == target:
                return mid
            elif times[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left-1

    def get(self, key: str, timestamp: int) -> str:
        times = self.key_to_time[key]
        # print(times)
        if not times or timestamp < times[0]:
            return ""
        idx = self.search(times, timestamp)

        if idx >= len(times):
            return self.time_to_value[times[-1]]
        # print(times, timestamp, idx)
        valid_time = times[idx]

        return self.time_to_value[valid_time]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)