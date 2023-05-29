"""Модуль производит рассчет для решения задачи -
 "Калькулятор" из Яндекс Контеста."""
# 87784515


def is_number(char: str) -> bool:
    """Проверка является ли строка числом."""
    try:
        float(char)
        return True
    except ValueError:
        return False


def math_operate(math_sign: str) -> int:
    """Запуск операции при появлении математического знака."""
    numbers = [stack_numbers.pop(), stack_numbers.pop()]
    if math_sign == '+':
        number = numbers[1] + numbers[0]
    if math_sign == '/':
        number = numbers[1] // numbers[0]
    if math_sign == '*':
        number = numbers[1] * numbers[0]
    if math_sign == '-':
        number = numbers[1] - numbers[0]
    return number


def main() -> None:
    """Главная функция на добавление числа в стек."""
    for char in expression:
        if is_number(char):
            stack_numbers.append(int(char))
        else:
            stack_numbers.append(math_operate(char))


if __name__ == '__main__':
    expression = input().split()
    stack_numbers = []
    main()
    print(stack_numbers.pop())
