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
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__len = 0

    def is_empty(self) -> bool:
        """Проверка пустой ли дек."""
        return self.__len == 0

    def push_front(self, item: int) -> None:
        """Добавление элемента в начало дека."""
        if self.__len == self.__max_size:
            raise DequeFull
        else:
            if self.__dequeue[self.__head] is None:
                self.__dequeue[self.__head] = item
            else:
                self.__head = (self.__head - 1) % self.__max_size
                self.__dequeue[self.__head] = item
            self.__len += 1

    def push_back(self, item: int) -> None:
        """Добавление элемента в конец дека."""
        if self.__len == self.__max_size:
            raise DequeFull
        else:
            if self.__dequeue[self.__tail] is None:
                self.__dequeue[self.__tail] = item
            else:
                self.__tail = (self.__tail + 1) % self.__max_size
                self.__dequeue[self.__tail] = item
            self.__len += 1

    def pop_front(self) -> None:
        """Удаление элемента из начала дека."""
        if self.is_empty():
            raise DequeEmpty
        element = self.__dequeue[self.__head]
        self.__dequeue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__len -= 1
        if self.is_empty():
            self.__head = self.__tail = 0
        print(element)

    def pop_back(self) -> None:
        """Удаление элемента из конца дека."""
        if self.is_empty():
            raise DequeEmpty
        element = self.__dequeue[self.__tail]
        self.__dequeue[self.__tail] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__len -= 1
        if self.is_empty():
            self.__head = self.__tail = 0
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
