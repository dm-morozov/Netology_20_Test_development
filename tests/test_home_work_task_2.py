import pytest
from home_work_task_2_palindrome import solve


@pytest.mark.parametrize(
    'phrases, expected',
    [
        (["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза", \
        "а собака боса", "тонет енот", "карман мрак", "пуст суп"], \
        ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза", \
        "а собака боса", "тонет енот", "пуст суп"]),
    ]
)
def test_solve(phrases, expected):
    result = solve(phrases)

    assert expected == result