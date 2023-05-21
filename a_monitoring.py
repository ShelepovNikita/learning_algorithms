"""Модуль производит рассчет для решения задачи -
 "Мониторинг" из Яндекс Контеста."""
# 87548263


def transpose_matrix(matrix: list[list]):
    """Транспонирование матрицы."""
    for i in range(columns):
        result = ''
        for line in matrix:
            result += line[i] + ' '
        print(result)


def main():
    """Главная функция на запуск модуля."""
    transpose_matrix(matrix)


if __name__ == '__main__':
    lines, columns = int(input()), int(input())

    matrix = []
    for _ in range(lines):
        matrix.append(input().split())

    main()
