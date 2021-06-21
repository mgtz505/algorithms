print("Implementation of Merge Sort")
test_data = [3,11,4,0,7,2,12,7,9,6,5,10,3,14,8,5]

def mergeSort(N):
    if len(N) > 1:
        mid = len(N) // 2
        left, right = N[:mid], N[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                N[k] = left[i]
                i+= 1
            else:
                N[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            N[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            N[k] = right[j]
            j += 1
            k += 1

    

mergeSort(test_data)
print(test_data)  #[0, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 12, 14]