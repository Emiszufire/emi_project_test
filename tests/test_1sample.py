import pytest


@pytest.fixture
def one():
    return 1


@pytest.fixture
def two():
    return 3


def test_pass(one):
    actual = one
    expected = 1
    assert actual == expected, "Actual value does not match expected value"


def test_fail(two):
    actual = two
    expected = 1
    assert actual == expected, "Actual value does not match expected value"
