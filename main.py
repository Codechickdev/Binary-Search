pos = -1


def binary_search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                 u = mid + 1
    return False

list = [9, 5, 1, 4, 2, 8, 0, 4]
n = [1]

if binary_search(list, n):
    print("Found at", pos + 1)
else:
    print("Not Found")
