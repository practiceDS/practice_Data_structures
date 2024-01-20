import pytest

@pytest.fixture(params=["a","b"])
def setup(request):
    print(request.param)

@pytest.mark.kushagra
def test_count(setup):
    print("count successful")

@pytest.mark.kushagra1
@pytest.mark.parametrize("a,b,final",[(2,2,4),(5,5,11)])
def test_add(a,b,final):
    assert a+b == final