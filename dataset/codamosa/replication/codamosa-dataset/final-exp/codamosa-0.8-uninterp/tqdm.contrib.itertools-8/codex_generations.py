

# Generated at 2022-06-14 13:12:44.589263
# Unit test for function product
def test_product():
    """Test that tqdm(product()) is equivalent to tqdm(range(n))"""
    from random import randint
    from ..utils import FormatTqdm
    # pylint: disable=missing-docstring
    class MyTqdmBar(FormatTqdm):
        def update(self, n=1, *args, **kwargs):
            # remove current tqdm line, so we can run it again
            FormatTqdm.update(self, n=n, *args, **kwargs)
            self.write('')

    # Build lists to loop over
    lens = []
    lists = []
    for _ in range(5):
        lens.append(randint(1, 10))
        lists.append(list(range(lens[-1])))

    # Compare with tqdm(range())


# Generated at 2022-06-14 13:12:53.346411
# Unit test for function product
def test_product():
    from itertools import product
    from pytest import approx

    res = list(product(range(3), range(1, 4), range(2, 5)))

# Generated at 2022-06-14 13:12:59.921581
# Unit test for function product
def test_product():
    from .utils import _range

    assert list(product(_range(1), _range(2))) == list(_range(1)) * 2
    assert list(product(_range(1), _range(2), _range(3))) == [
        (i, j, k) for i, j, k in zip(_range(1), _range(2), _range(3))]



# Generated at 2022-06-14 13:13:06.824209
# Unit test for function product
def test_product():
    iterables = [range(5), range(5)]
    assert list(product(*iterables, total=None)) == list(itertools.product(*iterables))

    # Test `total != None`
    iterables = [range(6), range(6)]
    assert list(product(*iterables, total=None)) == list(itertools.product(*iterables))


if __name__ == '__main__':
    import nose
    nose.runmodule()

# Generated at 2022-06-14 13:13:16.956246
# Unit test for function product
def test_product():
    """Test the product() function."""
    from ..utils import get_empty_bar
    try:
        from nose.tools import assert_equal
    except ImportError:
        def assert_equal(a, b):
            __tracebackhide__ = True
            assert a == b
    import sys

    try:
        # Only Python 3+ has check_output
        from subprocess import check_output
    except ImportError:
        def check_output(*args, **kwargs):
            return "\r\r"

    def get_n_cols(default=80):
        """Get terminal width or a given default value."""
        try:
            s = check_output(["tput", "cols"])
            return max(int(s) - 1, 10)
        except:
            return default

    # Just to get the line

# Generated at 2022-06-14 13:13:29.389731
# Unit test for function product
def test_product():
    """Test `tqdm.itertools.product`"""
    import numpy as np

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    from contextlib import contextmanager

    @contextmanager
    def our_file(content):
        try:
            f = StringIO(content)
            yield f
        finally:
            f.close()

    with our_file(u'X\n' * 6) as f:
        assert list(product(['a', 'b', 'c'], f)) == \
               [('a', 'X\n'), ('a', 'X\n'), ('b', 'X\n'),
                ('b', 'X\n'), ('c', 'X\n'), ('c', 'X\n')]

# Generated at 2022-06-14 13:13:37.889862
# Unit test for function product
def test_product():
    """
    Unit test for function `product`.
    """
    # Standard example
    from string import ascii_letters as letters
    from ...tests.write_and_read_values import write_and_read_values
    with write_and_read_values() as w:
        for i in product(range(4), letters[:6]):
            assert (i[0], i[1]) == i
            w(i)
    # Test as iterator
    assert [i for i in product(range(4), letters[:6])] == \
        list(product(range(4), letters[:6]))

# Generated at 2022-06-14 13:13:43.364822
# Unit test for function product
def test_product():
    """Unit test for function `itertools.product`."""
    res = map(sum, product(range(5), repeat=2))
    try:
        import numpy as np
        np.testing.assert_array_equal(
            sorted(res), sorted(range((4 ** 2) + 1)))
    except ImportError:
        return (sum(res) == (4 ** 2) * ((4 ** 2) + 1) / 2.)

# Generated at 2022-06-14 13:13:54.700566
# Unit test for function product
def test_product():
    """
    Unit test for function product
    """
    import sys
    import random as rn
    tot = 0
    norm = 0

# Generated at 2022-06-14 13:13:57.173568
# Unit test for function product
def test_product():
    iterables = [["a", "b"], [1, 2, 3], ["A", "B", "C"]]
    for i in product(*iterables):
        pass