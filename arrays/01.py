# Given an array arr[] of n integers and a target value, check if there exists a pair whose sum equals the target. This is a variation of the 2-Sum problem.

# Examples: 

# Input: arr[] = [0, -1, 2, -3, 1], target = -2
# Output: true
# Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

# Input: arr[] = [1, -2, 1, 0, 5], target = 0
# Output: false
# Explanation: There is no pair with sum equals to given target.


def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    arr1 = [0, -1, 2, -3, 1]
    target1 = -2
    print(has_pair_with_sum(arr1, target1))  # Output: True

    arr2 = [1, -2, 1, 0, 5]
    target2 = 0
    print(has_pair_with_sum(arr2, target2))  # Output: False