def sort_insert(array):
    for i in range (1, len (array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def binary_search(array, element, left, right):
    if left > right:
        # если левая граница превысила правую, значит элемент отсутствует
        return False, False

    middle = (right + left) // 2  # находим середину
    if array[middle] >= element and array[middle - 1] < element:
        # если элемент в середине, возвращаем индексы числа меньше числа и равным числу
        return middle - 1, middle
    elif element < array[middle]:
        # если элемент меньше элемента в середине, то рекурсивно ищем в левой половине
        return binary_search (array, element, left, middle - 1)
    else:                          # иначе в правой
        return binary_search (array, element, middle + 1, right)


while True:
    try:
        L = list(map(float, input('Please input number sequence by using gap: ').split()))
        # Если ошибка, будет вызвано исключение:
    except Exception:
        # Цикл будет повторяться до правильного ввода:
        print("<<Error!>> input sequence by using gap, e.g. 13 4 -5 23 55 7 98")
    else:
        break
# L = list(map(float, input('Please input number sequence by using gap (e.g. 13 4 -5 23 55 7 98): ').split()))

while True:
    try:
        element = float(input('Please input any number for search: '))
        # Если ошибка, будет вызвано исключение:
    except ValueError:
        # Цикл будет повторяться до правильного ввода:
        print(f"<<Error!>> input number must be '>' {min(list(L))} and '<=' {max(list(L))}!!!")
    else:
        break

# element = float(input('Please input any number for search: '))

# L = [13, 4, -5, 23, 55, 7, 98]
# element = 7

print(f'Sorted list: {sort_insert(L)}\n'
      f'Input number: {element}\n')

if element <= L[0] or element > L[len(L) - 1]:
    # проверка на соблюдение условий вхождения значения элемента в массив
    x, y = False, False
else:
    x, y = binary_search(L, element, 0, len(L) - 1)  # len(L) - 1)

if x is False and y is False:
    print("Condition isn't executed!!!")
else:
    print(f'Position of element " < " input number = {x}\n'
          f'Position of element "> =" input number = {y}\n')
