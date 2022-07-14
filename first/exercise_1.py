def task(arr, N):
    for x, y in enumerate(arr):
        if y == N:
            return x
    return -1


s = [1, 2, 3, 4, 5, 6]
print(task(s, 3))

