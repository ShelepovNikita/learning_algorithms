"""Модуль производит рассчет для решения задачи -
 "Пузырёк" из Яндекс Контеста."""
# 88033803


def comparator(number1: str, number2: str) -> bool:
    """Функция сравнения двух чисел"""
    if len(number1) == len(number2):
        return int(number1) < int(number2)
    else:
        return int(number2+number1) > int(number1+number2)


def main() -> None:
    """"Главная функция на запуск модуля."""
    flag = True
    while flag:
        for i in range(1, amount_of_numbers):
            if comparator(numbers[i-1], numbers[i]):
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
        flag = False
        for i in range(1, amount_of_numbers):
            if comparator(numbers[i-1], numbers[i]):
                flag = True
    print(''.join(numbers))


if __name__ == '__main__':
    amount_of_numbers = int(input())
    numbers = input().split()
    main()
