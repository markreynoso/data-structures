"""Test binary search tree."""
import pytest


def test_initialize_bst_returns_empty_bst(bst):
    """Test initialize empty bst returns empty bst."""
    assert bst.root is None


def test_initialize_bst_iteratble_returns_size_n():
    """Test initialize with iterable returns proper size tree."""
    from bst import Bst
    tree = Bst([2, 6, 3, 7, 8, 1])
    assert tree._size == 6


def test_initialize_bst_iteratble_root_is_first_item():
    """Test initialize with iterable root is first item in."""
    from bst import Bst
    tree = Bst([2, 6, 3, 7, 8, 1])
    assert tree.root.data == 2


def test_size_returns_0_if_bst_is_empty(bst):
    """Test size method returns 0 on empty tree."""
    assert bst.size() == 0


def test_size_returns_appropriate_size_after_iterable():
    """Test size returns proper size when initiated by iterable."""
    from bst import Bst
    tree = Bst([2, 6, 3, 7, 8, 1])
    assert tree.size() == 6


def test_size_returns_10_if_insert_manually_10_items(bst_big):
    """Test if 10 items inserted that size is 10."""
    assert bst_big.size() == 10


def test_insert_10_items_returns_first_in_as_root(bst_big):
    """Test that root is first in if 10 items inserted."""
    assert bst_big.root.data == 50


def test_insert_identicle_values_raise_valueerror(bst):
    """Test insert same values raises value error."""
    bst.insert(1)
    with pytest.raises(ValueError):
        bst.insert(1)


def test_insert_non_int_raises_valueerror(bst):
    """Test insert non number raises value error."""
    with pytest.raises(ValueError):
        bst.insert('howdy')


def test_insert_iterable_raises_valueerror(bst):
    """Test insert iterable raises appropriate error."""
    with pytest.raises(ValueError):
        bst.insert([1, 3, 5, 9])


def test_search_node_on_empty_tree_returns_none(bst):
    """Test search on empty tree returns none."""
    assert bst.search(10) is None


def test_search_node_not_in_tree_returns_none(bst_full):
    """Test search for node not in tree returns none."""
    assert bst_full.search(1) is None


def test_search_for_non_int_returns_non(bst_full):
    """Test search for non number returns none."""
    assert bst_full.search('cake') is None


def test_search_val_in_tree_returns_node(bst_full):
    """Test search for val in tree returns node."""
    bst_full.insert(5)
    assert isinstance(bst_full.search(5), object)


def test_search_val_in_tree_retruns_node_with_data(bst_full):
    """Test search for val in tree returns node with data of val."""
    bst_full.insert(5)
    assert bst_full.search(5).data == 5


def test_depth_returns_int_of_total_depth_of_tree(bst_full):
    """Test depth returns integer of depth of tree."""
    assert bst_full.depth() == 2


def test_depth_empty_tree_returns_none(bst):
    """Test depth on epmty tree returns None."""
    assert bst.depth() == 0


def test_depth_on_large_tree_returns_full_size(bst_big):
    """Test depth on large tree returns actual size."""
    assert bst_big.depth() == 4


def test_depth_of_tree_with_only_root_is_0(bst):
    """Test if only root in tree that depth is 0."""
    bst.insert(1)
    assert bst.depth() == 0


def test_contains_returns_false_if_val_not_in_tree(bst_big):
    """Test contains returns false if val not in tree."""
    assert bst_big.contains(102948686) is False


def test_contains_returns_false_if_non_int_entered(bst_big):
    """"Test contains returns false if non int entered."""
    assert bst_big.contains('pie') is False


def test_contains_returns_true_if_val_in_tree(bst_big):
    """Test contains returns true if val in tree."""
    assert bst_big.contains(40) is True
    assert bst_big.contains(50) is True
    assert bst_big.contains(68) is True


def test_balance_returns_string_if_bst_is_empty(bst):
    """Test balance returns none if bst is empty."""
    assert bst.balance() == 'There are no nodes in this tree.'


def test_balance_returns_int(bst_big):
    """Test balancde returns int.."""
    assert isinstance(bst_big.balance(), int)


def test_balance_returns_int_of_r_minus_l_of_tree(bst_big):
    """Test balance returns int of left minus right sides of tree."""
    assert bst_big.balance() == -1


def test_balance_returns_int_of_r_minus_l_of_tree_two(bst_full, bst):
    """Test balance returns int of left minus right sides of tree."""
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert bst.balance() == 0
    assert bst_full.balance() == -2


def test_balance_returns_int_of_r_minus_l_of_tree_three(bst):
    """Test balance returns int of left minus right sides of tree."""
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    assert bst.balance() == -6
