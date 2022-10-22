def quickSort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high and high - low > 16:
        p = partition(array, low, high)
        quickSort(array, low, p)
        quickSort(array, p + 1, high)

    return insertSort(array, low, high)
    
def partition(array, low, high):
    pivot = array[(high + low) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


def insertSort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    for i in range(low + 1, high + 1):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array
