import math

class CustomArray:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Input data must be a list")
            
        self.data = data
        self.n = len(data)

    def dot_product(self, other):
        if self.n != other.n:
            raise ValueError("Input arrays must have the same length")
            
        return sum(x * y for x, y in zip(self.data, other.data))

    def vector_norm(self):
        return math.sqrt(sum(x**2 for x in self.data))
