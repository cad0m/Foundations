class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        if (n + self.size) > self.capacity:
            raise ValueError("out of jar size")
        self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("not enough cockies :(")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) <= 0:
            raise ValueError("Invalid input")
        self._capacity = int(capacity)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if int(size) < 0 or self._capacity < size:
            raise ValueError("Invalid input")
        self._size = int(size)
