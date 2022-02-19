import pytest

from solutions import least_common_multiple


def test_brute_force_solution_simple_cases():
    assert least_common_multiple.brute_force_solution((5, 7)) == 5 * 7
    assert least_common_multiple.brute_force_solution((5 * 2, 2 * 7)) == 5 * 2 * 7
    assert least_common_multiple.brute_force_solution((1, 1)) == 1
    assert least_common_multiple.brute_force_solution((4, 2)) == 4


def test_raise_value_error_first_number_negative():

    with pytest.raises(ValueError) as e:
        least_common_multiple.brute_force_solution((-5, 7))
    assert str(e.value) == "One of the numbers is negative or zero"


def test_raise_value_error_second_number_negative():
    with pytest.raises(ValueError) as e:
        least_common_multiple.brute_force_solution((5, -7))

    assert str(e.value) == "One of the numbers is negative or zero"


def test_raise_value_error_both_numbers_negative():
    with pytest.raises(ValueError) as e:
        least_common_multiple.brute_force_solution((-5, -7))

    assert str(e.value) == "Both numbers are negative or zero"


def test_raise_value_error_first_number_zero():
    with pytest.raises(ValueError) as e:
        least_common_multiple.brute_force_solution((2, 0))

    assert str(e.value) == "One of the numbers is negative or zero"


def test_raise_value_error_second_number_zero():
    with pytest.raises(ValueError) as e:
        least_common_multiple.brute_force_solution((0, 2))
    assert str(e.value) == "One of the numbers is negative or zero"


def test_raise_value_error_both_numbers_zero():
    with pytest.raises(ValueError) as e:
        least_common_multiple.brute_force_solution((0, 0))
    assert str(e.value) == "Both numbers are negative or zero"


def test_raise_value_error_first_number_negative_seconds_zero():

    with pytest.raises(ValueError) as e:
        least_common_multiple.brute_force_solution((-5, 0))
    assert str(e.value) == "Both numbers are negative or zero"
