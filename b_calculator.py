"""Модуль производит рассчет для решения задачи -
 "Калькулятор" из Яндекс Контеста."""
# 87822529
import operator

ACTION = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.floordiv,
    "*": operator.mul,
}


class Stack:
    """Класс для хранения стека и методов работы с ним."""

    def __init__(self) -> None:
        """При инициализации создается:
        - Список для хранения элементов (стек)."""
        self.__stack = []

    def push(self, item: int) -> None:
        """Добавление элемента в стек."""
        self.__stack.append(item)

    def pop(self) -> int:
        """Удаление элемента из стека."""
        return self.__stack.pop()


def main() -> int:
    """Главная функция на запуск модуля."""
    for item in expression:
        if item in ACTION:
            first_item_pop = stack_numbers.pop()
            second_item_pop = stack_numbers.pop()
            stack_numbers.push(ACTION[item](second_item_pop, first_item_pop))
        else:
            stack_numbers.push(int(item))
    return stack_numbers.pop()


if __name__ == '__main__':
    expression: list[str] = input().split()
    stack_numbers: Stack = Stack()
    print(main())
