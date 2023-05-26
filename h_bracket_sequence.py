"""Модуль производит рассчет для решения задачи -
 "Скобочная последовательность" из Яндекс Контеста."""
# 87697853


class StackBracket:
    """Класс для создания стэка хранения открытых скобок."""

    def __init__(self) -> None:
        """При инициализации создается список для хранения скобок."""
        self.brackets = []

    def push(self, bracket: int) -> None:
        """Добавление скобки в список."""
        self.brackets.append(bracket)

    def pop(self) -> str:
        """Удаление скобки из списка."""
        return self.brackets.pop()

    def is_empty(self) -> bool:
        """Проверка пустой ли стэк."""
        return self.brackets == []


def main() -> bool:
    """Главная функция на запуск модуля."""
    for bracket in string_bracket:
        if bracket in '({[':
            stackbracket.push(bracket)
        else:
            if stackbracket.is_empty():
                return False
            x = stackbracket.pop()
            if bracket == ']':
                bracket = '['
            if bracket == ')':
                bracket = '('
            if bracket == '}':
                bracket = '{'
            if x != bracket:
                return False
    if not stackbracket.is_empty():
        return False
    return True


if __name__ == '__main__':
    stackbracket = StackBracket()
    string_bracket = input()
    print(main())
