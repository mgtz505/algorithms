print("Implementation of Insertion Sort")
test_data = [3,11,4,0,7,2,12,7,9,6,5,10,3,14,8,5]


def insertionSort(N):
    indexing_length = range(1, len(N))
    for i in indexing_length:
        value_to_sort = N[i]

        while N[i - 1] > value_to_sort and i > 0:
            N[i], N[i - 1] = N[i - 1], N[i]
            i -= 1

    return N        



print(insertionSort(test_data))  #[0, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 12, 14]