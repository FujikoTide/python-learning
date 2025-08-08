from dataclasses import dataclass


@dataclass
class MyRange:
    start: int
    stop: int
    step: int = 1

    def __iter__(self):
        return MyRangeIterator(self.start, self.stop, self.step)


class MyRangeIterator:
    def __init__(self, start, stop, step):
        self._current = start
        self._stop = stop
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= self._stop:
            raise StopIteration
        result = self._current
        self._current += self._step
        return result


my_range = MyRange(0, 10, 1)
for n in my_range:
    print(n)


for n in my_range:
    print(n)
