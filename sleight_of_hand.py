"""Модуль производит рассчет для решения задачи -
 "Ловкость рук" из Яндекс Контеста."""
# ID решения 87448759

import sys


def read_lines(numbers_of_lines=4) -> list[str]:
    """Чтение строк из тренажера."""
    type_of_simulator = []
    for _ in range(numbers_of_lines):
        line = list(sys.stdin.readline().rstrip())
        type_of_simulator += line
    return type_of_simulator


def count_wins(type_of_simulator: list[str], number_of_players=2) -> int:
    """Подсчет количества побед."""
    result = 0
    previous = set()
    for key in type_of_simulator:
        if key not in previous and key != '.':
            if type_of_simulator.count(key) <= (number_of_keys *
                                                number_of_players):
                result += 1
            previous.add(key)
    return result


def main() -> int:
    """Главная функция на запуск модуля."""
    type_of_simulator = read_lines()
    result = count_wins(type_of_simulator)
    return result


if __name__ == '__main__':
    number_of_keys = int(input())
    print(main())
