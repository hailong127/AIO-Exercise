class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise StackUnderflowError("Underflow: Stack is empty")
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Overflow: Stack is full")
        self.__queue.append(value)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.__queue[0]


queue1 = MyQueue(capacity=5)

queue1.enqueue(1)

queue1.enqueue(2)

print(queue1.is_full())

print(queue1.front())

print(queue1.dequeue())

print(queue1.front())

print(queue1.dequeue())

print(queue1.is_empty())

queue2 = MyQueue(capacity=2)

queue2.enqueue(1)

queue2.enqueue(2)

print(queue2.front())

print(queue2.is_full())

print(queue2.dequeue())

print(queue2.dequeue())

print(queue2.is_empty())

queue1 = MyQueue(capacity=2)

queue1.enqueue(1)

queue1.enqueue(2)

queue1.enqueue(2)
