def letters_range(start, stop, step=1):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    start = letters.index(start)
    stop = letters.index(stop)
    return letters[start:stop:step]


print(letters_range('b', 'w', 2))
print(letters_range('a', 'g'))
print(letters_range('g', 'p'))
print(letters_range('p', 'g', -2))
print(letters_range('a', 'a'))
