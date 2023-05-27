"""Модуль производит рассчет для решения задачи -
 "Списочная форма" из Яндекс Контеста."""
#


def main() -> list[str]:
    """Главная функция на запуск модуля."""
    return list(str((number_2 + int("".join(list_of_number_1)))))


if __name__ == '__main__':
    size = int(input())
    list_of_number_1 = input().split()
    number_2 = int(input())
    print(*main())
