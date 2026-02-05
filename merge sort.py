def merge_sort(arr):
    if len(arr) <= 1:
        return arr   # already sorted

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # break left
    right = merge_sort(arr[mid:])  # break right

    return merge(left, right)      # join


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


print(merge_sort([6,3,9,2]))
