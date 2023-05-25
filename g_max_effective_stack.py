"""Модуль производит рассчет для решения задачи -
 "Стек - MaxEffective" из Яндекс Контеста."""
# 87685097


class StackMaxEffective:
    """Класс для создания стэка."""

    def __init__(self) -> None:
        """При инициализации создается два списка -
        один для хранения стэка, второй для хранения максимальных значений.
        """
        self.items = []
        self.max = []

    def isEmpty(self) -> bool:
        """Проверка пустой ли стэк."""
        return self.items == []

    def push(self, item: int) -> None:
        """Добавление значения в список стэка и
        добавление значения в список максимальных значений."""
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[-1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[-1])
        self.items.append(item)

    def get_max(self) -> str:
        """Получение максимального значения."""
        if self.isEmpty():
            return 'None'
        return str(self.max[-1])

    def pop(self) -> None:
        """Удаление значения из списка стэка и
        добавление значения в список максимальных значений."""
        if self.isEmpty():
            print('error')
        else:
            self.max.pop()
            self.items.pop()


def main(command: str) -> None:
    """Главная функция на запуск модуля."""
    if 'push' in command:
        x = command.split()
        stackmax.push(int(x[1]))
    elif command == 'pop':
        stackmax.pop()
    elif command == 'get_max':
        print(stackmax.get_max())


if __name__ == '__main__':
    stackmax = StackMaxEffective()
    n = int(input())
    for _ in range(n):
        main(input())
