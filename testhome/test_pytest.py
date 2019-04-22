import pytest
from hamcrest import *

@pytest.mark.parametrize("actual,expect",[(1,2),(1,1),("aaa","aaa"),("aaa","bbb")])
def test_data(actual,expect):
    assert_that(actual,equal_to(expect))