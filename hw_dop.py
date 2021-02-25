def n_arr(widths):
    if len(widths) == 1:
        return ['' for _ in range(widths[0])]
    return [n_arr(widths[1:])] * widths[1]


print(n_arr([2, 2, 3]))
