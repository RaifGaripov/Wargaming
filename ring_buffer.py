class RingBuffer:

    def __init__(self, size):
        self.max = [0] * size
        self.index = 0
        self.size = size

    def append(self, append_item):
        self.max[self.index] = append_item
        self.index = (self.index + 1) % self.size


b = RingBuffer(1000)
for i in range(10000):
    b.append(i)
# called 200 times, this lasts 1.097 second on my laptop

print(b)
from collections import deque
b = deque( [], 1000 )
for i in range(10000):
    b.append(i)
# called 200 times, this lasts 0.211 second on my laptop
print(b)
