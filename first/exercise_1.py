def task(arr, N):
    for x, y in enumerate(arr):
        if y == N:
            return x
    return -1


s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
print(task(s, 0))

