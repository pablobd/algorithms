import pytest

from solutions.greedy.fractional_knapsack.item import Item


def test_item_is_greater_than_other():
    item1 = Item(value=1, weight=3)
    item2 = Item(value=2, weight=3)
    assert item2 > item1


def test_item_is_less_than_other():
    item1 = Item(value=1, weight=3)
    item2 = Item(value=2, weight=3)
    assert item1 < item2


def test_item_is_greater_or_equal_to_other():
    item1 = Item(value=1, weight=3)
    item2 = Item(value=2, weight=3)
    assert item2 >= item1


def test_item_is_less_or_equal_to_other():
    item1 = Item(value=1, weight=3)
    item2 = Item(value=2, weight=3)
    assert item1 <= item2


def test_item_is_equal_to_other():
    item1 = Item(value=2, weight=3)
    item2 = Item(value=2, weight=3)
    assert item1 == item2


def test_item_is_greater_than_other_raises_type_error():
    item1 = Item(value=1, weight=3)
    item2 = 3
    with pytest.raises(TypeError) as e:
        assert item2 > item1
    assert str(e.value) == "'>' not supported between instances of 'int' and 'Item'"


def test_item_is_less_than_other_raises_type_error():
    item1 = Item(value=1, weight=3)
    item2 = 3
    with pytest.raises(TypeError) as e:
        assert item2 < item1
    assert str(e.value) == "'<' not supported between instances of 'int' and 'Item'"


def test_item_is_greater_or_equal_to_other_raises_type_error():
    item1 = Item(value=1, weight=3)
    item2 = 3
    with pytest.raises(TypeError) as e:
        assert item2 >= item1
    assert str(e.value) == "'>=' not supported between instances of 'int' and 'Item'"


def test_item_is_less_or_equal_to_other_raises_type_error():
    item1 = Item(value=1, weight=3)
    item2 = 3
    with pytest.raises(TypeError) as e:
        assert item2 <= item1
    assert str(e.value) == "'<=' not supported between instances of 'int' and 'Item'"


def test_item_is_equal_to_other_raises_type_error():
    item1 = Item(value=2, weight=3)
    item2 = 3
    assert not item2 == item1
