def quick_sort(nums):
    if len(nums) <= 0:
        return nums
    pivot = nums[-1]

    left_list = []
    right_list = []

    for num in nums[:-1]:
        if num < pivot:
            left_list.append(num)
        else:
            right_list.append(num) 
        
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

print(quick_sort([20, 3, 14, 1, 5]))
    
