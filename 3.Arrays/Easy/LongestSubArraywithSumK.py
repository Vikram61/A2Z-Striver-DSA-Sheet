def longest_subarray_sum_k(nums, k):
    prefix_sums = {0: -1}  
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        current_sum += num

        if (current_sum - k) in prefix_sums:
            max_len = max(max_len, i - prefix_sums[current_sum - k])

        if current_sum not in prefix_sums:
            prefix_sums[current_sum] = i

    return max_len

# Driver Code
nums = [1, -1, 5, -2, 3]
k = 3
print("Length of the longest subarray:", longest_subarray_sum_k(nums, k))
