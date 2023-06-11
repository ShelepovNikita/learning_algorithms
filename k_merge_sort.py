"""Модуль производит рассчет для решения задачи -
 "Сортировка слиянием" из Яндекс Контеста."""
# 88071604


def merge(arr: list, left: int, mid: int, right: int) -> list:
    '''Слияние двух отсортированных массивов.'''
    array_1 = arr[left: mid]
    array_2 = arr[mid: right]
    i = j = 0
    k = left

    while i < len(array_1) and j < len(array_2):
        if array_1[i] <= array_2[j]:
            arr[k] = array_1[i]
            i += 1
        else:
            arr[k] = array_2[j]
            j += 1
        k += 1

    while i < len(array_1):
        arr[k] = array_1[i]
        i += 1
        k += 1
    while j < len(array_2):
        arr[k] = array_2[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr: list, left: int, right: int):
    '''Разбивает массив на две половины и рекурсивно вызывает сортировку.'''
    if right - left <= 1:
        return
    else:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def main() -> list[int]:
    """Главная функция на запуск модуля."""
    merge_sort(arr, 0, len(arr))
    return arr


if __name__ == '__main__':
    arr = input().split()
    main()
