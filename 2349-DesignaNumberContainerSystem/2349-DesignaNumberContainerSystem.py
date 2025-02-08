from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.number_to_index = defaultdict(SortedSet)
        self.index_to_num = {}
        

    def change(self, index: int, number: int) -> None:
        # print(index, number)
        # print(self.number_to_index)
        # number at index
        if index not in self.index_to_num:
            self.index_to_num[index] = number
            self.number_to_index[number].add(index)
        else:
            original = self.index_to_num[index]
            self.index_to_num[index] = number
            self.number_to_index[original].remove(index)
            self.number_to_index[number].add(index)
            

    def find(self, number: int) -> int:
        # return smallest index of number
        result = self.number_to_index[number]
        if not result:
            return -1
        return result[0]     


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)