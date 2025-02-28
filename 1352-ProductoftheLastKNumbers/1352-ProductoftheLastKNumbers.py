// Last updated: 2/28/2025, 3:37:34 PM
class ProductOfNumbers:

    def __init__(self):
        self.running_prod = [1]

    def add(self, num: int) -> None:
        if num != 0:
            to_add = num * self.running_prod[-1]
            self.running_prod.append(to_add)
        else:
            self.running_prod = [1]

    def getProduct(self, k: int) -> int:
        # print(self.running_prod)
        if k > len(self.running_prod)-1:
            return 0

        n = len(self.running_prod)-1

        return int(self.running_prod[-1] / self.running_prod[n-k])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)