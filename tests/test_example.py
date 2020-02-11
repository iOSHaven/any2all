import pytest

def f():
    return 3

def test_if_f_works():
    assert f() == 3