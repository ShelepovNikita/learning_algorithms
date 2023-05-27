"""Модуль производит рассчет для решения задачи -
 "Факторизация" из Яндекс Контеста."""
# 87561814


def factorization(num: int) -> list:
    """Поиск простых делителей."""
    result = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            result.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        result.append(num)
    return result


def main() -> None:
    """Главная функция на запуск модуля."""
    print(*factorization(num))


if __name__ == '__main__':
    num = int(input())
    main()
