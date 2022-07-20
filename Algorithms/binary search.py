# def binary_search(lst, item):
#     low = 1
#     high = len(lst)
#
#     while low <= high:
#         mid = (low + high)//2
#         guess = lst[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# my_lst = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# print(binary_search(my_lst, 0))


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high)//2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_lst = [1, 2, 3, 6, 7, 9, 10, 23, 45, 67, 99]
print(binary_search(my_lst, 9))

