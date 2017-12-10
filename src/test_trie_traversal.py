"""Test trie traversal."""
import inspect

import pytest


def test_trie_traversal_returns_generator(trie):
    """Test trie traversal returns a generator object."""
    g = trie.trie_traversal
    assert inspect.isgeneratorfunction(g)


def test_trie_traversal_no_input_returns_all_letters(trie):
    """Test trie traversal on empty trie returns no letters."""
    trie.insert('go')
    trie.insert('code')
    trie.insert('seattle')
    trie.insert('goes')
    g = trie.trie_traversal()
    output = []
    for count in range(15):
        output.append(next(g))
    exp = ['c', 'g', 's', 'e', 'o', 'o', 'a', 'e',
           'd', 'e', 's', 't', 't', 'l', 'e']
    assert sorted(output) == sorted(exp)


def test_trie_traversal_generates_letters_after_input(trie_10_words):
    """Test trie traversal generates only letters following input."""
    g = trie_10_words.trie_traversal('stock')
    output = []
    for num in range(3):
        output.append(next(g))
    assert output == ['i', 'n', 'g']


def test_trie_returns_all_branches_following_input(trie):
    """Test trie returns all branches following input."""
    trie.insert('water')
    trie.insert('waste')
    trie.insert('washer')
    trie.insert('washing')
    trie.insert('washington')
    trie.insert('wasup')
    g = trie.trie_traversal('wa')
    output = []
    for num in range(17):
        output.append(next(g))
    exp = ['s', 't', 'e', 't', 'h', 'r', 'u', 'p', 'i',
           'e', 'e', 'r', 'n', 'g', 't', 'o', 'n']
    assert sorted(output) == sorted(exp)


def test_trie_stops_if_letter_not_found(trie):
    """Test trie stops if input letter not found."""
    trie.insert('python')
    g = trie.trie_traversal('pickle')
    output = None
    try:
        output = next(g)
    except StopIteration:
        output = 'not found'
    assert output == 'not found'


def test_trie_stops_if_next_called_beyond_depth(trie):
    """Test trie stops when full depth reached."""
    trie.insert('python')
    g = trie.trie_traversal('python')
    output = None
    try:
        output = next(g)
    except StopIteration:
        output = 'not found'
    assert output == 'not found'


def test_trie_traversal_raises_type_error_if_input_not_string(trie):
    """Test trie traversal returns type error if input not a string."""
    g = trie.trie_traversal(5)
    with pytest.raises(TypeError):
        next(g)
