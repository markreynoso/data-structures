"""Sort a list with radix method."""
import time
from random import randint


def radix_sort(num_list):
    """Radix sort a list."""
    if len(num_list) > 1:
        buckets = [[] for x in range(10)]
        arrange = num_list
        output = []
        rounds = 0
        max_rounds = len(str(max(num_list)))
        while max_rounds > rounds:
            for number in arrange:
                if len(str(number)) >= rounds + 1:
                    for bucket_num in range(10):
                        idx = number // 10**rounds % 10
                        if idx == bucket_num:
                            buckets[bucket_num].append(number)
                            break
                else:
                    output.append(number)
            arrange = []
            for bucket in buckets:
                arrange += bucket
            buckets = [[] for x in range(10)]
            rounds += 1
        output += arrange
        return output
    else:
        return num_list


if __name__ == '__main__':
    print('\nCASE 1: A small list to be sorted:\n'
          '[45, 25, 80, 3, 6, 19, 400, 34]\n')
    start_simple = time.time()
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # test = [45, 25, 80, 3, 6, 19, 400, 34]
    print(radix_sort(test))
    solve_simple = (time.time() - start_simple)
    print('\nSorted using radix_sort() in {} seconds.'.format(solve_simple))

    print('\nCASE 2: A list of 100 numbers:\n')
    hundred = [randint(1, 100000) for x in range(100)]
    print(test)
    start_hundred = time.time()
    print(radix_sort(hundred))
    solve_hundred = (time.time() - start_hundred)
    print('\nSorted using radix_sort() in {} seconds.'.format(solve_hundred))

    print('\nCASE 3: A list of 1,000 random numbers:')
    thousand = [randint(1, 100000) for x in range(1000)]
    print(thousand)
    start_thousand = time.time()
    print(radix_sort(thousand))
    solve_thousand = (time.time() - start_thousand)
    print('\nSorted using radix_sort() {} seconds'.format(solve_thousand))

    print('\nCASE 4: A list of 10,000 numbers (not shown):\n')
    ten = [randint(1, 100000) for x in range(10000)]
    start_ten = time.time()
    print(radix_sort(ten))
    solve_ten = (time.time() - start_ten)
    print('\nSorted using radix_sort() in {} seconds.'.format(solve_ten))

    # print('\nCASE 5: A list of 100,000 words:\n')
    # mil = [randint(1, 100000) for x in range(100000)]
    # start_mil = time.time()
    # print(radix_sort(mil))
    # solve_mil = (time.time() - start_mil)
    # print('\nSorted using radix_sort() in {} seconds.'.format(solve_mil))
