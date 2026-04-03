def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
                
        if min_index != i:
            nums[i], nums[min_index]= nums[min_index], nums[i]
    return nums
                
print(selection_sort([33, 1, 89, 2, 67, 245]))
