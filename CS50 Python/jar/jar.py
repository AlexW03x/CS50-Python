class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity Too Low!")
        self._capacity = capacity
        self._jar_size = 0

    def __str__(self):
        string = ""
        for i in range(0, self._jar_size):
            string = string + "🍪"
        return string

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("Capacity Too High!")
        elif self._jar_size + n > self._capacity:
            raise ValueError("Too Many Deposited!")
        else:
            self._jar_size += n

    def withdraw(self, n):
        if n > self._jar_size:
            raise ValueError(f"There isn't {n} cookies left in the jar!")
        else:
            self._jar_size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._jar_size