import pytest

def get_human_age(cat_age, dog_age):
    def calculate(age, ratio):
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // ratio

    return [calculate(cat_age, 4), calculate(dog_age, 5)]

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
