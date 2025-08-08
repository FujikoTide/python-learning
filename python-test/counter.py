class Counter:
    def __init__(self):
        self._count = 0

    def __repr__(self):
        return f"Counter(count={self._count})"

    def increment(self):
        self._count += 1

    def decrement(self):
        self._count -= 1

    @property
    def count(self):
        return self._count


counter = Counter()
print(counter)
counter.increment()
counter.increment()
counter.decrement()
counter.increment()
counter.increment()
counter.decrement()
counter.decrement()
counter.decrement()
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
counter.increment()
counter.increment()
counter.increment()
print(counter)
print(counter.count)
