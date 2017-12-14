"""Quick sort a list."""
import time
from random import randint


def quick_sort(num_list):
    """Use the quick sort method to sort a list of numbers."""
    import pdb; pdb.set_trace()
    if len(num_list) > 1:

        pivot = num_list[0]
        left_mark = 1
        right_mark = len(num_list) - 1

        while left_mark <= right_mark:
            if num_list[left_mark] > pivot and num_list[right_mark] < pivot:
                num_list[left_mark], num_list[right_mark] =\
                    num_list[right_mark], num_list[left_mark]
                left_mark += 1
                right_mark -= 1
            elif num_list[left_mark] <= pivot and num_list[right_mark] < pivot:
                left_mark += 1
            elif num_list[left_mark] > pivot and num_list[right_mark] >= pivot:
                right_mark -= 1
            elif num_list[left_mark] <= pivot and num_list[right_mark] >= pivot:
                left_mark += 1
                right_mark -= 1

        num_list[0], num_list[right_mark] = num_list[right_mark], num_list[0]

        divider = right_mark + 1
        left = quick_sort(num_list[:right_mark])
        right = quick_sort(num_list[divider:])
        return left + [num_list[right_mark]] + right
    else:
        return num_list


if __name__ == '__main__':
    print('\nCASE 1: A small list to be sorted:\n'
          '[45, 25, 80, 3, 6, 19, 400, 34]\n')
    start_simple = time.time()
    test = [45, 25, 80, 3, 6, 19, 400, 34]
    print(quick_sort(test))
    solve_simple = (time.time() - start_simple)
    print('\nSorted using quick_sort() in {} seconds.'.format(solve_simple))

    print('\nCASE 2: A list of 100 numbers:\n')
    hundred = [randint(1, 100000) for x in range(100)]
    print(hundred)
    start_hundred = time.time()
    print(quick_sort(hundred))
    solve_hundred = (time.time() - start_hundred)
    print('\nSorted using quick_sort() in {} seconds.'.format(solve_hundred))

    print('\nCASE 3: A list of 1,000 random numbers:')
    thousand = [randint(1, 100000) for x in range(1000)]
    print(thousand)
    start_thousand = time.time()
    print(quick_sort(thousand))
    solve_thousand = (time.time() - start_thousand)
    print('\nSorted using quick_sort() {} seconds'.format(solve_thousand))

    print('\nCASE 4: A list of 10,000 numbers (not shown):\n')
    ten = [randint(1, 100000) for x in range(10000)]
    start_ten = time.time()
    print(quick_sort(ten))
    solve_ten = (time.time() - start_ten)
    print('\nSorted using quick_sort() in {} seconds.'.format(solve_ten))
