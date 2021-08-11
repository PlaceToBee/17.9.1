a = input("Введите числа через пробел:")
b = int(input("Введите еще одно число:"))
a = a.split()
a.append(b)
numbers = a
int_numbers = [int(x) for x in numbers]
for i in range(1, len(int_numbers)):
    x = int_numbers[i]
    idx = i
    while idx > 0 and int_numbers[idx-1] > x:
        int_numbers[idx] = int_numbers[idx-1]
        idx -= 1
    int_numbers[idx] = x
print(int_numbers)

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
element = b
array = [i for i in range(1, 100)]
print(binary_search(array, element, 0, 99))