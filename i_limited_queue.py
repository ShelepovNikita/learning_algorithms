
class MyQueueSized:

    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def push(self, item):
        if self.queue[self.tail] is None:
            self.queue[self.tail] = item
            self.len += 1
            if self.tail != self.max_size - 1:
                self.tail += 1
        else:
            print('error')

    def pop(self) -> str:
        if self.is_empty():
            return 'None'
        if self.queue[self.tail] is not None:
            element = self.queue[self.head]
            self.len -= 1
            self.queue[self.head] = None
        if self.head != self.max_size - 1:
            self.head += 1
        return str(element)

    def peek(self) -> str:
        if self.is_empty():
            return 'None'
        return str(self.queue[self.head])

    def size(self):
        return self.len


def main(command: str) -> None:
    """Главная функция на запуск модуля."""
    if 'push' in command:
        x = command.split()
        queue.push(int(x[1]))
    elif command == 'pop':
        print(queue.pop())
    elif command == 'peek':
        print(queue.peek())
    elif command == 'size':
        print(queue.size())


if __name__ == '__main__':
    amount_commands = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for _ in range(amount_commands):
        main(input())
