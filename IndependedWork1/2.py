import numpy as np

def get_numbers():
    numbers = []
    while True:
        user_input = input("Введите число: ")
        if user_input == "":
            break
        number = float(user_input)
        numbers.append(number)
    return numbers

def divide_numbers(numbers):
    average = np.mean(numbers)
    print(f"Среднее значние: {average}")

    return numbers[numbers < average], numbers[numbers == average], numbers[numbers > average]


def main():
    numbers = get_numbers()

    numbers = np.array(numbers)

    below_average, equal_average, above_average = divide_numbers(numbers)

    if below_average.size > 0:
        print("Числа ниже среднего:")
        print(below_average)
    else:
        print("Чисел ниже среднего нет.")

    if equal_average.size > 0:
        print("Числа равные среднему:")
        print(equal_average)
    else:
        print("Чисел равных среднему нет.")

    if above_average.size > 0:
        print("Числа выше среднего:")
        print(above_average)
    else:
        print("\nЧисел выше среднего нет.")

if __name__ == '__main__':
    main()