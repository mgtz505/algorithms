print("Implementation of Shell Sort")
test_data = [3,11,4,0,7,2,12,7,9,6,5,10,3,14,8,5]


def shellSort(N):
    gap = len(N) // 2

    while gap > 0:
        i, j = 0, gap

        while j < len(N):

            if N[i] > N[j]:
                N[i], N[j] = N[j], N[i]
            
            i += 1
            j += 1

        while i - gap != -1:
            if N[i - gap] > N[i]:
                N[i - gap], N[i] = N[i], N[i - gap]
            
            i -=1
        
        gap //= 2

shellSort(test_data)
print(test_data)  #[0, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 12, 14]
