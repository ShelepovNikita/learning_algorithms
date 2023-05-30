"""Модуль производит рассчет для решения задачи -
 "Дек" из Яндекс Контеста."""
# 87823971


class DequeFull(Exception):
    """Вызывается когда дэк максимально заполнен."""
    pass


class DequeEmpty(Exception):
    """Вызывается когда дэк пустой."""
    pass


class Deque:
    """Класс для создания объекта дека."""

    def __init__(self, max_size: int) -> None:
        """При инициализации создается:
        - Список для хранения элементов (дек)
        - Переменная для хранения максимального размера дека
        - Указатель головы дека
        - Указатель конца дека
        - Количество элементов в деке."""
        self.__dequeue = [None] * max_size
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
            raise DequeFull
        else:
            if self.__dequeue[self.head] is None:
                self.__dequeue[self.head] = item
            else:
                self.head = (self.head - 1) % self.max_size
                self.__dequeue[self.head] = item
            self.len += 1

    def push_back(self, item: int) -> None:
        """Добавление элемента в конец дека."""
        if self.len == self.max_size:
            raise DequeFull
        else:
            if self.__dequeue[self.tail] is None:
                self.__dequeue[self.tail] = item
            else:
                self.tail = (self.tail + 1) % self.max_size
                self.__dequeue[self.tail] = item
            self.len += 1

    def pop_front(self) -> None:
        """Удаление элемента из начала дека."""
        if self.is_empty():
            raise DequeEmpty
        element = self.__dequeue[self.head]
        self.__dequeue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.len -= 1
        if self.is_empty():
            self.head = self.tail = 0
        print(element)

    def pop_back(self) -> None:
        """Удаление элемента из конца дека."""
        if self.is_empty():
            raise DequeEmpty
        element = self.__dequeue[self.tail]
        self.__dequeue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_size
        self.len -= 1
        if self.is_empty():
            self.head = self.tail = 0
        print(element)


def main(command) -> None:
    """Главная функция на запуск модуля."""
    try:
        getattr(dequeue, command.pop(0))(*command)
    except Exception:
        print('error')


if __name__ == '__main__':
    amount_commands: int = int(input())
    max_size: int = int(input())
    dequeue: Deque = Deque(max_size)
    for _ in range(amount_commands):
        main(input().split())
