'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, size):
    max = 0
    x = len(nums)
    arr = []
    
    for i in range(x - size + 1):
        max = nums[i]
        for y in range(1, size):
            if nums[i + y] > max:
                max = nums[i + y]
        arr.append(max)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
