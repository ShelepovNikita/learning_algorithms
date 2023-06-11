"""Модуль производит рассчет для решения задачи -
 "Поиск в сломанном массиве" из Яндекс Контеста."""
# 88010043


def broken_search(nums: list[int], target: int) -> int:
    '''Поиск в сломанном массиве.'''
    head = 0
    tail = len(nums) - 1
    while head <= tail:
        mid = (head + tail) // 2
        if nums[mid] == target:
            return mid
        if nums[head] <= nums[mid]:
            if nums[head] <= target < nums[mid]:
                tail = mid - 1
            else:
                head = mid + 1
        else:
            if nums[mid] < target <= nums[tail]:
                head = mid + 1
            else:
                tail = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12, 13, 14, 15, 16]
    assert broken_search(arr, 5) == 6, 'Тест не пройден'
    return 'Тест пройден'


def main() -> int:
    """Главная функция на запуск модуля."""
    # return broken_search(nums, target)
    return test()


if __name__ == '__main__':
    # count_nums = int(input())
    # target: int = int(input())
    # nums: list[int] = input().split()
    print(main())
