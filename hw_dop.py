def n_arr(widths, step=None):
    """
    Создается n-мерный список в следующем порядке - список из n пустых строк, где n это первый элемент из width
    """
    if step == None:

        step = len(widths)
    if len(widths) == 1:
        return ['' for _ in range(widths[0])]
    return [n_arr(widths[len(widths) - step + 1:], step - 1) for _ in range(widths[len(widths) - step])]


x = n_arr([2, 2, 3])
print(x)
x[0][1][2] = 3
print(x)