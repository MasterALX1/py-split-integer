import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts",
    [
        (8, 1),
        (1236, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (7, 10),
        (3, 5),
        (128, 16)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    parts: int
) -> None:
    assert sum(split_integer(value, parts)) == value


@pytest.mark.parametrize(
    "value, parts, result",
    [
        (8, 1, 8),
        (6, 2, 3),
        (32, 8, 4),
        (128, 16, 8)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    parts: int,
    result: int
) -> None:
    assert all(part == result for part in split_integer(value, parts))


@pytest.mark.parametrize(
    "value, parts",
    [
        (8, 1),
        (1236, 1),
        (56, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        parts: int
) -> None:
    assert split_integer(value, parts) == [value]


@pytest.mark.parametrize(
    "value, parts",
    [
        (17, 4),
        (32, 6),
        (7, 10),
        (3, 5)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        parts: int,
) -> None:
    assert split_integer(value, parts) == sorted(split_integer(value, parts))


@pytest.mark.parametrize(
    "value, parts, result",
    [
        (7, 10, [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]),
        (3, 5, [0, 0, 1, 1, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        parts: int,
        result: list[int]
) -> None:
    assert split_integer(value, parts) == result
