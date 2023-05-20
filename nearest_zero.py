"""Модуль производит рассчет для решения задачи -
 "Ближайший ноль" из Яндекс Контеста."""
# ID решения 87440161


def find_zero_index(street: list[str]) -> list[int]:
    """Поиск индексов всех нулей в строке."""
    start_index = -1
    zeros_index = []
    for _ in range(street.count('0')):
        start_index = street.index('0', start_index + 1, length_of_street)
        zeros_index.append(start_index)
    return zeros_index


def from_left(zero_index: list[str], result: list[int]) -> list[int]:
    """Проход по массиву слева направо."""
    for i in range(zero_index[0], length_of_street):
        if street[i] == '0':
            result[i] = 0
        else:
            result[i] = result[i - 1] + 1
    return result


def from_right(zero_index: list[str], result: list[int]) -> list[int]:
    """Проход по массиву справа налево."""
    for i in range(zero_index[-1], zero_index[0] - 1, -1):
        if street[i] == '0':
            result[i] = 0
        else:
            result[i] = min(result[i], result[i+1] + 1)
    for i in range(zero_index[0] - 1, -1, -1):
        result[i] = result[i + 1] + 1
    return result


def main() -> list[int]:
    result = [0] * length_of_street
    zero_index = find_zero_index(street)
    result = from_left(zero_index, result)
    result = from_right(zero_index, result)
    return result


if __name__ == '__main__':
    length_of_street = int(input())
    street = input().split()
    print(*main())
