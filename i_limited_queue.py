"""Модуль производит рассчет для решения задачи -
 "Ограниченная очередь" из Яндекс Контеста."""
# 87725640


class MyQueueSized:
    """Класс для создания объекта ограниченной очереди."""

    def __init__(self, max_size) -> None:
        """При инициализации создается:
        - Список для хранения элементов
        - Переменная для хранения максимального размера очереди
        - Указатель головы очереди
        - Указатель конца очереди
        - Количество элементов в очереди."""
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.len = 0

    def is_empty(self) -> bool:
        """Проверка пустая ли очередь."""
        return self.len == 0

    def push(self, item) -> None:
        """Добавление элемента в очередь."""
        if self.size() == self.max_size:
            print('error')
        else:
            self.queue[self.tail] = item
            self.len += 1
            self.tail = (self.tail + 1) % self.max_size

    def pop(self) -> str:
        """Удаление элемента из очереди."""
        if self.is_empty():
            return 'None'
        element = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.len -= 1
        return str(element)

    def peek(self) -> str:
        """Вывести первое число в очереди."""
        if self.is_empty():
            return 'None'
        return str(self.queue[self.head])

    def size(self) -> int:
        """Вывести количество элементов в очереди."""
        return self.len


def main(command: str) -> None:
    """Главная функция на запуск модуля."""
    if 'push' in command:
        element = command.split()
        queue.push(int(element[1]))
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
