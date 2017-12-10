"""Merge sort a list."""
import time
from random import randint


def merge_sort(list_in):
    """Sort a list using the merge sort method."""
    if len(list_in) > 1:
        half = len(list_in) // 2
        list_a = list_in[0:half]
        list_b = list_in[half:]
        left = merge_sort(list_a)
        right = merge_sort(list_b)
        output = []
        l_idx = 0
        r_idx = 0
        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] < right[r_idx]:
                output.append(left[l_idx])
                l_idx = l_idx + 1
            else:
                output.append(right[r_idx])
                r_idx = r_idx + 1
        while l_idx < len(left):
            output.append(left[l_idx])
            l_idx = l_idx + 1
        while r_idx < len(right):
            output.append(right[r_idx])
            r_idx = r_idx + 1
        return output
    else:
        return list_in


if __name__ == '__main__':
    print('\nCASE 1: A small list to be sorted:\n'
          '[45, 25, 80, 3, 6, 19, 400, 34]\n')
    start_simple = time.time()
    test = [45, 25, 80, 3, 6, 19, 400, 34]
    print(merge_sort(test))
    solve_simple = (time.time() - start_simple)
    print('\nSorted using merge_sort() in {} seconds.'.format(solve_simple))

    print('\nCASE 2: A list of 100 numbers:\n')
    hundred = [randint(1, 100000) for x in range(100)]
    print(test)
    start_hundred = time.time()
    print(merge_sort(hundred))
    solve_hundred = (time.time() - start_hundred)
    print('\nSorted using merge_sort() in {} seconds.'.format(solve_hundred))

    print('\nCASE 3: A list of 1,000 random numbers:')
    thousand = [randint(1, 100000) for x in range(1000)]
    print(thousand)
    start_thousand = time.time()
    print(merge_sort(thousand))
    solve_thousand = (time.time() - start_thousand)
    print('\nSorted using merge_sort() {} seconds'.format(solve_thousand))

    print('\nCASE 4: A list of 10,000 numbers (not shown):\n')
    ten = [randint(1, 100000) for x in range(10000)]
    start_ten = time.time()
    print(merge_sort(ten))
    solve_ten = (time.time() - start_ten)
    print('\nSorted using merge_sort() in {} seconds.'.format(solve_ten))

    print('\nCASE 5: A list of 100,000 words:\n')
    mil = [randint(1, 100000) for x in range(100000)]
    start_mil = time.time()
    print(merge_sort(mil))
    solve_mil = (time.time() - start_mil)
    print('\nSorted using merge_sort() in {} seconds.'.format(solve_mil))
