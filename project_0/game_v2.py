"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def predict_number(number: int=1) -> int:
    """Угадываем число с помощью поска среднего между интервалами

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    left = 0 # Начальная левая границп интервала
    right = 100 # Начальная правая границп интервала
    predict_number = 100 # предполагаемое число

    while (predict_number != number):
        count += 1
        # В зависимости от условия меняем диапазоны
        if number > predict_number:
            left = predict_number
        else: 
            right = predict_number
        
        # Предполагаем, что число находится в середине диапазона
        predict_number = (left+right) // 2
    return count


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_number)
