#реализован бинарный поиск

a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
left = -1
right = len(a)

while right - left > 1:
    middle = (right + left) // 2
    if a[middle] == 0:
        right = middle
    else:
        left = middle

print(right)