print("Implementation of Quicksort")
test_data = [3,11,4,0,7,2,12,7,9,6,5,10,3,14,8,5]

def quickSort(N):
    length = len(N)
    if length <= 1:
        return N
    else:
        larger, smaller = [], []
        pivot = N.pop()
        for num in N:
            if num < pivot:
                smaller.append(num)
            else:
                larger.append(num)
        return quickSort(smaller) + [pivot] + quickSort(larger)


print(quickSort(test_data))  #[0, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 12, 14]
