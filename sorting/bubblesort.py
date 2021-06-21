print("Implementation of Bubble Sort")
test_data = [3,11,4,0,7,2,12,7,9,6,5,10,3,14,8,5]

def bubbleSort(N):
    indexing_length = len(N) - 1
    sorted_var = False

    while not sorted_var:
        sorted_var = True
        for i in range(0, indexing_length):
            if N[i] > N[i + 1]:  #Change the comparison operator for asc vs desc
                sorted_var = False
                N[i], N[i + 1] = N[i + 1], N[i]

    return N

print(bubbleSort(test_data))  #[0, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 12, 14]