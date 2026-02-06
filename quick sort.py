def quick_sort(arr, pivot_index):
    # base case
    if len(arr) <= 1:
        return arr

    pivot = arr[pivot_index]

    left = []
    right = []

    for i in range(len(arr)):
        if i == pivot_index:
            continue  # skip the pivot element

        if arr[i] < pivot: # smaller than pivot → goes left
            left.append(arr[i])
        else: # greater than or equal → goes right
            right.append(arr[i])

    return quick_sort(left, len(left)//2) + [pivot] + quick_sort(right, len(right)//2)

arr = [6, 3, 9, 2, 4]
print(quick_sort(arr, 3))

