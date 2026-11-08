

def merge_sort(numbers_list, left, right):

    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(numbers_list, left, mid)
    merge_sort(numbers_list, mid + 1, right)

    merge(numbers_list, left, right, mid)


def merge(numbers_list, left, right, mid):

    left_copy = numbers_list[left:mid+1]
    right_copy = numbers_list[mid + 1:right + 1]

    l_counter, r_counter = 0, 0
    sorted_counter = left

    while l_counter < len(left_copy) and r_counter < len(right_copy):
        if left_copy[l_counter] <= right_copy[r_counter]:
            numbers_list[sorted_counter] = left_copy[l_counter]
            l_counter += 1
        else:
            numbers_list[sorted_counter] = right_copy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_copy):
        numbers_list[sorted_counter] = left_copy[l_counter]
        l_counter += 1
        sorted_counter += 1

    while r_counter < len(right_copy):
        numbers_list[sorted_counter] = right_copy[r_counter]
        r_counter += 1
        sorted_counter += 1

