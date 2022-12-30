"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers.

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
* should be 6: [4, -1, 2, 1]
"""

# code by Tyler

def max_sequence(arr):
    max_sum = 0
    max_start = 0
    max_end = 0
    current_sum = 0
    current_start = 0

    for i, x in enumerate(arr):
        current_sum += x
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i
        elif current_sum < 0:
            current_sum = 0
            current_start = i + 1
        else:
            pass

    return arr[max_start:max_end + 1]

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
