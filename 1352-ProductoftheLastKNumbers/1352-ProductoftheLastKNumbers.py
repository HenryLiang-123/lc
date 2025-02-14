class ProductOfNumbers:

    def __init__(self):
        self.products = []
        
    def add(self, num: int) -> None:
        if not self.products and num != 0:
            self.products.append(num)
        else:
            if num != 0:
                self.products.append(self.products[-1] * num if self.products[-1] != 0 else num)
            else:
                self.products = []
            

    def getProduct(self, k: int) -> int:
        n = len(self.products)
        if k > n:
            return 0
        else:
            if n-k-1 < 0:
                result = self.products[-1]
            else:
                result = self.products[-1] / self.products[n-k-1]
            return int(result)

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)