## Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

We should build a minstack to maintain the minimum element

```python
class MinStack:

    def __init__(self):
        self.stock = []
        self.minstock = []

    def push(self, val: int) -> None:
        self.stock.append(val)
        if (self.minstock == []):
            self.minstock.append(val)
            return 
        if (val < self.minstock[-1]):
            self.minstock.append(val)
        else:
            self.minstock.append(self.minstock[-1])

    def pop(self) -> None:
        self.stock.pop(-1)
        self.minstock.pop(-1)
    def top(self) -> int:
        return self.stock[-1]

    def getMin(self) -> int:
        return self.minstock[-1]

```

