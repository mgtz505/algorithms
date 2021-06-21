print("Implementation of Selection Sort")
test_data = [3,11,4,0,7,2,12,7,9,6,5,10,3,14,8,5]

def selectionSort(N):
    indexing_length = range(0, len(N) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i + 1, len(N)):
            if N[j] < N[min_value]:
                min_value = j
            
        if min_value != i:
            N[min_value], N[i] = N[i], N[min_value]

    return N

print(selectionSort(test_data))