import pytest

from add import add


@pytest.mark.parametrize(
    argnames="a, b, expected",
    argvalues=[
        (1, 2, 3),
        (4, 6, 10),
        (-3, 2, -1),
        (8, -8, 0),
    ],
)
def test_add(a, b, expected):
    res = add(a=a, b=b)
    assert res == expected, f"{expected=}, {res=}"
