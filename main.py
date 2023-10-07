import argparse


def set_sum(init, final, interval, arr):
    current_sum = 0
    max_sum = float('-inf')
    for i in range(init, final - 1, interval):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sum


def max_subarray_divide_conquer(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_max = max_subarray_divide_conquer(arr, low, mid)
    right_max = max_subarray_divide_conquer(arr, mid + 1, high)

    left_sum = set_sum(mid, low, -1, arr)
    right_sum = set_sum(mid + 1, high + 1, +1, arr)
    cross_max = left_sum + right_sum

    return max(left_max, right_max, cross_max)


def find_max_subarray(arr):
    return max_subarray_divide_conquer(arr, 0, len(arr) - 1)


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Max Subarray Calculator')
    parser.add_argument('--array', '-a', type=int, nargs='*', help='Array', required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = init_args()
    arr = args.array
    result = find_max_subarray(arr)
    print("A soma do maior subconjunto é: ", result)
