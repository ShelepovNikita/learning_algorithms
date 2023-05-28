"""Модуль производит рассчет для решения задачи -
 "Дек" из Яндекс Контеста."""
# 87768962


class MyQueueSized:
    """Класс для создания объекта дека."""

    def __init__(self, max_size: int) -> None:
        """При инициализации создается:
        - Список для хранения элементов (дек)
        - Переменная для хранения максимального размера дека
        - Указатель головы дека
        - Указатель конца дека
        - Количество элементов в деке."""
        self.dequeue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.len = 0

    def is_empty(self) -> bool:
        """Проверка пустой ли дек."""
        return self.len == 0

    def push_front(self, item: int) -> None:
        """Добавление элемента в начало дека."""
        if self.len == self.max_size:
            print('error')
        else:
            if self.dequeue[self.head] is None:
                self.dequeue[self.head] = item
            else:
                self.head = (self.head - 1) % self.max_size
                self.dequeue[self.head] = item
            self.len += 1

    def push_back(self, item: int) -> None:
        """Добавление элемента в конец дека."""
        if self.len == self.max_size:
            print('error')
        else:
            if self.dequeue[self.tail] is None:
                self.dequeue[self.tail] = item
            else:
                self.tail = (self.tail + 1) % self.max_size
                self.dequeue[self.tail] = item
            self.len += 1

    def pop_front(self) -> str:
        """Удаление элемента из начала дека."""
        if self.is_empty():
            return 'error'
        element = self.dequeue[self.head]
        self.dequeue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.len -= 1
        if self.is_empty():
            self.head = self.tail = 0
        return str(element)

    def pop_back(self) -> str:
        """Удаление элемента из конца дека."""
        if self.is_empty():
            return 'error'
        element = self.dequeue[self.tail]
        self.dequeue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_size
        self.len -= 1
        if self.is_empty():
            self.head = self.tail = 0
        return str(element)


def main(command: str) -> None:
    """Главная функция на запуск модуля."""
    if 'push_front' in command:
        command, item = command.split()
        dequeue.push_front(int(item))
    if 'push_back' in command:
        command, item = command.split()
        dequeue.push_back(int(item))
    elif command == 'pop_front':
        print(dequeue.pop_front())
    elif command == 'pop_back':
        print(dequeue.pop_back())


if __name__ == '__main__':
    amount_commands = int(input())
    max_size = int(input())
    dequeue = MyQueueSized(max_size)
    for _ in range(amount_commands):
        main(input())
