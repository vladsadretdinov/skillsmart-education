def helper(arr, index, result):
    arr_length = len(arr)
    if arr_length == 1:
        result[index] = arr[0]
    else:
        middle = arr_length // 2
        result[index] = arr[middle]

        left_index = 2 * index + 1
        right_index = left_index + 1

        helper(arr[:middle], left_index, result)
        helper(arr[middle + 1:], right_index, result)
    return result


def GenerateBBSTArray(a):
    if a is None:
        return None

    arr_length = len(a)

    if arr_length == 0:
        return None
    elif arr_length == 1:
        return a

    sorted_arr = sorted(a)
    result = [None] * arr_length

    return helper(sorted_arr, 0, result)

