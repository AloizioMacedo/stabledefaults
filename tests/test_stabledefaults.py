from stabledefaults import stabledefaults


@stabledefaults()
def function_with_kwargs(
    x,
    y=[],
    z={"a": 1},
    *,
    kwarg1=2,
    kwarg2=[10, 20],
    kwarg3=[5, 7, 30],
    kwarg4={7: 5}
):
    y.append(x)
    z["b"] = x + x
    kwarg2.append(kwarg1)
    return y, z, kwarg2


@stabledefaults()
def function_without_kwargs(x, y, z, a=[], b=2, c="a", d={}):
    a.append(x)
    a.append(y)
    a.append(z)
    d[c] = b
    return a, d


@stabledefaults(deep=True)
def function_with_nested_lists(x, y, z, a=[[2]]):
    a.append(x)
    return a


@stabledefaults()
def function_without_defaults(x, y, z):
    return None


def test_basic_no_alteration():
    y, z, kwarg2 = function_with_kwargs(10)
    function_with_kwargs(30)
    assert y == [10]
    assert z == {"a": 1, "b": 20}
    assert kwarg2 == [10, 20, 2]


def test_function_with_nested_lists():
    a = function_with_nested_lists(10, 30, 50)
    function_with_nested_lists(111, 222, 333)
    assert a == [[2], 10]


def test_function_without_defaults():
    function_without_defaults(0, 0, 0)
