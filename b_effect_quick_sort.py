"""Модуль производит рассчет для решения задачи -
 "Поиск в сломанном массиве" из Яндекс Контеста."""
# 88114046


def partition(members: list, left: int, right: int) -> int:
    '''Поиск индекса опорного элемента в общем массиве.'''
    pivot = (members[left])
    i = left + 1
    j = right - 1
    while True:
        if (i <= j and members[j] > pivot):
            j -= 1
        elif (i <= j and members[i] < pivot):
            i += 1
        if i <= j:
            members[i], members[j] = members[j], members[i]
        else:
            members[left], members[j] = members[j], members[left]
            return j


def quick_sort(members: list, left: int, right: int) -> None:
    '''Разбивает массив по опорному элементу и вызывает сортировку.'''
    if ((right - left) > 1):
        p = partition(members, left, right)
        quick_sort(members, left, p)
        quick_sort(members, p + 1, right)


def main() -> None:
    """Главная функция на запуск модуля."""
    quick_sort(members_list, 0, len(members_list))
    print(*(list(zip(*members_list))[2]), sep="\n")


if __name__ == '__main__':
    members_list = []
    number = int(input())
    for _ in range(number):
        string = input().split()
        string[1] = (-1) * int(string[1])
        string[2] = int(string[2])
        members_list.append([string[1], string[2], string[0]])
    main()
