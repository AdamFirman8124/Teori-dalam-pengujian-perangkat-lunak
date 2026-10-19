

# Generated at 2022-06-14 13:12:33.855867
# Unit test for function trange
def test_trange():
    for _ in trange(2):
        pass

    for _ in trange(2, 3):
        pass

    for _ in trange(2, 3, 1):
        pass



# Generated at 2022-06-14 13:12:45.509449
# Unit test for function trange
def test_trange():
    from .std import tqdm
    list(tqdm(range(10), desc='FOO'))
    list(tqdm(range(10), ascii=True))
    list(tqdm(range(10), bar_format='{l_bar}{bar}|'))
    list(tqdm(range(10), ncols=79))
    list(tqdm(range(10), mininterval=0.1))
    list(tqdm(range(10), miniters=0.1))
    list(tqdm(range(10), mininterval=0.5, miniters=0.5))
    list(tqdm(range(10), mininterval=0.5, miniters=0.5))

# Generated at 2022-06-14 13:12:48.439893
# Unit test for function trange
def test_trange():
    for func in (tqdm, trange):
        with func(total=2) as t:
            assert t.total == 2
            t.update(1)  # pylint: disable=E1101
            t.update(1)



# Generated at 2022-06-14 13:12:50.479183
# Unit test for function trange
def test_trange():
    """Test for function `trange`"""
    from .std import tqdm  # noqa
    for _ in tqdm(trange(10)):
        pass

# Generated at 2022-06-14 13:12:57.590627
# Unit test for function trange
def test_trange():
    """Tests that trange is equivalent to tqdm(range())"""
    for _ in trange(10000):
        pass
    for _ in tqdm(range(10000)):
        pass
    for _ in tqdm(range(100000), ncols=100):
        pass
    for _ in tqdm(range(100000), desc="I'm in the progress!", ncols=100):
        pass

# Generated at 2022-06-14 13:13:09.162938
# Unit test for function trange
def test_trange():
    from .gui import trange
    from .gui import tnrange
    from .utils import format_interval

    from datetime import timedelta
    from time import sleep

    def test():
        with tnrange(10) as t:
            for i in t:
                sleep(0.01)

        with trange(10) as t:
            for i in t:
                sleep(0.01)

    # trivial test
    test()

    # test initialisation
    test()
    sleep(0.1)
    test()

    # test short initialisation
    test()
    sleep(0.01)
    test()

    # test iterable
    test()
    sleep(0.01)
    test()

    # test mininterval
    sleep(0.1)

# Generated at 2022-06-14 13:13:12.710789
# Unit test for function trange
def test_trange():
    """Test for trange().
    """
    from .std import _range
    for i in trange(_range(10)):
        assert i in _range(10)


if __name__ == "__main__":
    test_trange()

# Generated at 2022-06-14 13:13:18.846132
# Unit test for function trange
def test_trange():
    from ._utils import _range
    import time
    with trange(10) as t:
        for i in t:
            assert i == t.n
            time.sleep(0.01)
        assert t.n == 10

    with trange(5, 10) as t:
        for i in t:
            assert i == t.n
            time.sleep(0.01)
        assert t.n == 10

    with trange(5, 10, 1) as t:
        for i in t:
            assert i == t.n
            time.sleep(0.01)
        assert t.n == 10

    with trange(5, 10, 2) as t:
        for i in t:
            assert i == t.n
            time.sleep(0.01)
        assert t.n == 9

   

# Generated at 2022-06-14 13:13:27.904335
# Unit test for function trange
def test_trange():
    """Test trange shortcut function."""
    from .std import trange
    from .tqdm import tqdm
    from .utils import _range

    for loop in _range(3):
        for m in _range(0, 9):
            for unit in ("i", ("i", "B")):
                tqdm(unit=unit)

                # Check internal state reset
                t = trange(0, m, unit=unit)
                assert t._total_width == 0
                assert t.base_format == "{desc}: {rate_noinv:5.2f}/s"


# Generated at 2022-06-14 13:13:31.621910
# Unit test for function trange
def test_trange():
    from .std import trange
    from .std import tqdm
    ls = [
        tqdm(range(10)),
        tqdm(range(20)),
        trange(30),
    ]
    del ls