"""Модуль производит рассчет для решения задачи -
 "Пузырёк" из Яндекс Контеста."""
# 88021185


def bubble_search() -> None:
    """Сортировка списка пузырьком с выводом промежуточного результата."""
    flag = True
    while flag:
        for i in range(count_nums - 1):
            if int(nums[i]) > int(nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        print(' '.join(nums))
        flag = False
        for j in range(count_nums-1):
            if int(nums[j]) > int(nums[j+1]):
                flag = True


def main() -> None:
    """"Главная функция на запуск модуля."""
    bubble_search()


if __name__ == '__main__':
    count_nums = int(input())
    nums = input().split()
    main()
