"""Test radix sort."""
from random import randint

from radix_sort import radix_sort


def test_radix_sort_on_empty_list_returns_empty():
    """Test radix sort on empty list retruns empty list."""
    test = []
    assert radix_sort(test) == []


def test_radix_sort_on_list_of_three():
    """Test radix sort on list of three retuned sorted."""
    test = [6, 8, 2]
    assert radix_sort(test) == [2, 6, 8]


def test_radix_sort_with_sorted_list_no_change():
    """Test radix sort with sorted list returns no change."""
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert radix_sort(test) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_radix_sort_on_reverse_sort_returns_sorted():
    """Test radix sort with reverse sort returns sorted."""
    test = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert radix_sort(test) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_radix_sort_on_list_of_100_rand_int_returns_sorted():
    """Test random list of 100 returns sorted."""
    test = [randint(1, 10000) for x in range(100)]
    assert radix_sort(test) == sorted(test)


def test_radix_sort_on_list_of_1000_rand_int_returns_sorted():
    """Test random list of 1000 returns sorted."""
    test = [randint(1, 10000) for x in range(1000)]
    assert radix_sort(test) == sorted(test)


def test_radix_sort_of_all_nums_same_returns_same():
    """Test radix sort if all nums same returns the same."""
    test = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert radix_sort(test) == test


def test_radix_sort_with_one_variant_returns_sorted():
    """Test radix sort with one variant returns sorted."""
    test = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    assert radix_sort(test) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
