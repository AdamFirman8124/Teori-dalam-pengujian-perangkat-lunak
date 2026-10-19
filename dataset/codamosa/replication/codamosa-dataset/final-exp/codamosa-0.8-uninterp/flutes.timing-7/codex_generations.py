

# Generated at 2022-06-13 20:05:17.122273
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Testing"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:21.270178
# Unit test for function work_in_progress
def test_work_in_progress():
    from contextlib import contextmanager
    from time import sleep

    @work_in_progress
    def sleepy():
        sleep(1)

    @contextmanager
    def sleepy_context():
        sleep(1)
        yield

    with sleepy_context() as x:
        assert x is None
    sleepy()

# Generated at 2022-06-13 20:05:31.188296
# Unit test for function work_in_progress
def test_work_in_progress():
    def count_to(n):
        for i in range(n):
            pass
        return i

    # Demonstrate work_in_progress being used as a decorator
    @work_in_progress("Counting to a million")
    def count_to_a_million():
        return count_to(1_000_000)

    # Demonstrate work_in_progress being used as a context manager
    with work_in_progress("Counting to a billion"):
        count_to(1_000_000_000)

    with work_in_progress("Counting to a billion and half"):
        count_to(1_500_000_000)

    # Demonstrate counting to a million
    i = count_to_a_million()
    assert i == 999_999

# Generated at 2022-06-13 20:05:33.651732
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def work():
        time.sleep(0.5)
    work()

# Generated at 2022-06-13 20:05:34.850549
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(.5)

# Generated at 2022-06-13 20:05:42.352218
# Unit test for function work_in_progress
def test_work_in_progress():
    with assert_stdout(out="Loading file... done. (3.52s)\n"):
        @work_in_progress("Loading file")
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        obj = load_file("/path/to/some/file")

    with assert_stdout(out="Saving file... done. (3.78s)\n"):
        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)

# Generated at 2022-06-13 20:05:50.346792
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    for _ in range(2):
        time.sleep(0.05)
        import math
        with work_in_progress("Calculating sin of pi"):
            math.sin(math.pi)
        with work_in_progress("Calculating cos of pi"):
            math.cos(math.pi)
        with work_in_progress("Calculating log(e)"):
            math.log(math.e)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:05:54.752886
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.234)
    with work_in_progress("Saving file"):
        time.sleep(4.567)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:05:59.586249
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    import time
    import random
    from .timeit_context import timeit_context

    def consume_time():
        time.sleep(random.random())

    # Test 1: Test default description
    with timeit_context("Test 1: Test default description"):
        with work_in_progress():
            consume_time()

    # Test 2: Test custom description
    with timeit_context("Test 2: Test custom description"):
        with work_in_progress("custom description"):
            consume_time()

    # Test 3: Test contextlib.redirect_stdout method

# Generated at 2022-06-13 20:06:05.433930
# Unit test for function work_in_progress
def test_work_in_progress():
    import os

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    path = os.path.join(os.path.dirname(__file__), "data", "test.pickle")
    obj = load_file(path)
    assert obj == {'a': 1, 'b': 2, 'c': 3, 'd': 'ciao'}

    @work_in_progress("Saving file")
    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    path = os.path.join(os.path.dirname(__file__), "data", "test.pickle")
    save_file

# Generated at 2022-06-13 20:06:12.441454
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert "Loading file... done. (" in obj


# Generated at 2022-06-13 20:06:23.290191
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

# Generated at 2022-06-13 20:06:25.737810
# Unit test for function work_in_progress

# Generated at 2022-06-13 20:06:38.492935
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    import hashlib
    import os

    def calc_md5(path: str) -> str:
        """Calculate md5 checksum of a file."""
        md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                md5.update(chunk)
        return md5.hexdigest()

    file_path = os.path.join(os.path.expanduser("~/Downloads"),
                             "pytorch-1.1.0-cp36-cp36m-linux_x86_64.whl")
    old_md5 = calc_md5(file_path)

# Generated at 2022-06-13 20:06:41.813456
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Test"):
        time.sleep(2)
    assert True

# Generated at 2022-06-13 20:06:45.699801
# Unit test for function work_in_progress
def test_work_in_progress():
    print(f"Testing {__name__}.{test_work_in_progress.__name__}")
    with work_in_progress("Testing"):
        time.sleep(0.5)

# Generated at 2022-06-13 20:06:49.317136
# Unit test for function work_in_progress
def test_work_in_progress():
    def function_in_progress():
        time.sleep(0.5)
        return True

    assert function_in_progress()
    assert work_in_progress("This is a test")

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:55.863667
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Starting the server"):
        time.sleep(1)
    time.sleep(1)

    with work_in_progress("Stopping the server"):
        time.sleep(1)
    time.sleep(1)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:07:03.323207
# Unit test for function work_in_progress
def test_work_in_progress():
    from .utility import unit_test
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(1)
        with open(path, "rb") as f:
            return pickle.load(f)

    with unit_test():
        obj = load_file("/path/to/some/file")
        print(obj)

    with work_in_progress("Saving file"):
        time.sleep(1)
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:07:09.074392
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod(
        name="work_in_progress",
        optionflags=doctest.NORMALIZE_WHITESPACE
    )


if __name__ == "__main__":
    test_work_in_progress()
    import doctest
    doctest.testmod(
        name="work_in_progress",
        optionflags=doctest.NORMALIZE_WHITESPACE
    )

# Generated at 2022-06-13 20:07:17.446952
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress(desc="Loading file"):
        time.sleep(1.2)
    with work_in_progress(desc="Loading file"):
        time.sleep(3.5)
    with work_in_progress(desc="Loading file"):
        time.sleep(6.0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    test_work_in_progress()

# Generated at 2022-06-13 20:07:19.724520
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3.52)
    with work_in_progress("Saving file"):
        time.sleep(3.78)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:23.722115
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Doing dummy work"
    with work_in_progress(desc):
        time.sleep(0.2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:30.258974
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Long computation"):
        time.sleep(0.5)
    with work_in_progress("Loading file"):
        time.sleep(0.5)
    with work_in_progress("Computing 2 + 2"):
        time.sleep(0.5)


if __name__ == "__main__":
    # Run test for work_in_progress
    test_work_in_progress()

# Generated at 2022-06-13 20:07:41.522787
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    with mock.patch('sys.stdout') as mock_stdout:
        mocked_stdout_fd = io.StringIO()
        mock_stdout.return_value = mocked_stdout_fd
        mock_stdout = mock_stdout.return_value
        # Mock a slow file I/O section
        with work_in_progress("Loading file"):
            time.sleep(0.1)
            print("Loaded file")
        # Check the output of mocked stdout

# Generated at 2022-06-13 20:07:45.481439
# Unit test for function work_in_progress
def test_work_in_progress():
    import pathlib
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = pathlib.Path(d) / 'test'
        with work_in_progress('Doing something'):
            time.sleep(1)
        assert path.exists()
        with open(path, 'rb') as f:
            data = pickle.load(f)

# Generated at 2022-06-13 20:07:47.774920
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def test():
        time.sleep(3)
    test()

# Generated at 2022-06-13 20:07:53.438877
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import random
    for _ in range(10):
        rand_time = random.randint(0, 3)
        with work_in_progress("Sleeping for {} seconds".format(rand_time)):
            time.sleep(rand_time)


# Generated at 2022-06-13 20:08:04.223880
# Unit test for function work_in_progress
def test_work_in_progress():
    import io

    class fake_stdout:
        def __init__(self):
            self.message = io.StringIO()

        def __enter__(self):
            self.original_stdout = sys.stdout
            sys.stdout = self.message
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout = self.original_stdout
            self.message.seek(0)

        @property
        def getvalue(self):
            return self.message.getvalue()

    with fake_stdout() as fake_stdout_1:
        with work_in_progress():
            time.sleep(0.02)

    assert "done. (0.02s)" in fake_stdout_1.getvalue()


# Generated at 2022-06-13 20:08:15.876408
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    if not os.path.exists("/tmp"):
        return
    with work_in_progress("Test work_in_progress"):
        with open("/tmp/test.pkl", "wb") as f:
            pickle.dump(["a", "b", "c"], f)
        with open("/tmp/test.pkl", "rb") as f:
            print(pickle.load(f))
        os.remove("/tmp/test.pkl")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:27.412605
# Unit test for function work_in_progress
def test_work_in_progress():

    # Check that it works when used as a function decorator.

    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(0.02)
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/dev/null")

    # Check that it works when used as a context manager.

    with work_in_progress("Saving file"):
        with open("/dev/null", "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:31.246139
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress") as w:
        time.sleep(1)
        assert w == None, "work_in_progress() shoule return None."
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(test_work_in_progress())

# Generated at 2022-06-13 20:08:34.100612
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    with work_in_progress("Testing work_in_progress()"):
        for _ in range(100000):
            random.random()


# Generated at 2022-06-13 20:08:43.421443
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def load_file2(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress()
    def load_file3(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress
    def load_file4(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    str_to_print = "Loading file... done. (0.00s)"

    with mock.patch('builtins.print') as mocked_print:
        load

# Generated at 2022-06-13 20:08:49.694479
# Unit test for function work_in_progress
def test_work_in_progress():
    # Decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    # Context manager
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:08:54.272472
# Unit test for function work_in_progress
def test_work_in_progress():
    def foo():
        time.sleep(0.5)

    with work_in_progress("Loading file"):
        foo()
    print(f"Loading file... done. ({time_consumed:.2f}s)")

    with work_in_progress("Saving file"):
        foo()
    print(f"Saving file... done. ({time_consumed:.2f}s)")


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:09:00.272397
# Unit test for function work_in_progress
def test_work_in_progress():
    import unittest
    import io
    from contextlib import redirect_stdout

    class WorkInProgressTestCase(unittest.TestCase):
        def test_work_in_progress(self):
            f = io.StringIO()
            with redirect_stdout(f):
                with work_in_progress("Doing nothing"):
                    time.sleep(2)

            self.assertEqual(f.getvalue(), "Doing nothing... done. (2.00s)\n")

    unittest.main(module=__name__, argv=[__file__])

# Generated at 2022-06-13 20:09:02.503313
# Unit test for function work_in_progress
def test_work_in_progress():

    with work_in_progress("Test work_in_progress"):
        time.sleep(1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:07.486842
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    pass

# Generated at 2022-06-13 20:09:13.773551
# Unit test for function work_in_progress
def test_work_in_progress():
    from time import sleep
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)

    with work_in_progress("Saving file"):
        sleep(0.5)



# Generated at 2022-06-13 20:09:31.831346
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test function work_in_progress."""

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("test_data.pkl")
    assert obj == [1, 2, 3]

    with work_in_progress("Saving file"):
        with open("test_data.pkl", "wb") as f:
            pickle.dump(obj, f)

    with open("test_data.pkl", "rb") as f:
        assert pickle.load(f) == obj

    # Remove temporary file
    try:
        os.remove("test_data.pkl")
    except FileNotFoundError:
        pass

    return True

# Generated at 2022-06-13 20:09:39.892859
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(os.path.join(os.path.dirname(__file__), "__init__.py"))
    # print(obj)

    with work_in_progress("Saving file"):
        with open(os.path.join(os.path.dirname(__file__),
                               "__init__.py.bak"), "wb") as f:
            pickle.dump(obj, f)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:09:41.753211
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress"""
    with work_in_progress("Test work_in_progress"):
        time.sleep(0.5)

# Generated at 2022-06-13 20:09:51.819700
# Unit test for function work_in_progress
def test_work_in_progress():
    assert 'Loading file' in f"""
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    time.sleep(1)
    obj = load_file("/path/to/some/file")
    """

    assert 'done. (1.00s)' in f"""
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    time.sleep(1)
    obj = load_file("/path/to/some/file")
    """


# Generated at 2022-06-13 20:09:58.917917
# Unit test for function work_in_progress
def test_work_in_progress():
    def func(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = os.path.join(temp_dir, "test")
        with open(temp_path, "wb") as f:
            pickle.dump(1234567890, f)
        with work_in_progress("Loading file"):
            assert func(temp_path) == 1234567890

# Generated at 2022-06-13 20:09:59.744131
# Unit test for function work_in_progress
def test_work_in_progress():
    pass

# Generated at 2022-06-13 20:10:05.403364
# Unit test for function work_in_progress
def test_work_in_progress():
    from contextlib import suppress

    with suppress(SyntaxError):
        with work_in_progress("Loading file"):
            with open("some_file", "rb") as f:
               f.read()
    with suppress(SyntaxError):
        with work_in_progress("Saving file"):
            with open("some_other_file", "wb") as f:
                f.write(b"I'm a file.")


# Generated at 2022-06-13 20:10:11.485187
# Unit test for function work_in_progress
def test_work_in_progress():
    import fpe
    import time

    @fpe.work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            time.sleep(3.5)
            return pickle.load(f)

    with fpe.work_in_progress("Saving file"):
        with open(path, "wb") as f:
            time.sleep(3.78)
            pickle.dump(obj, f)

    assert os.path.exists(path)
    assert pickle.load(open(path, "rb")) == obj

# Generated at 2022-06-13 20:10:14.508649
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work in progress"):
        time.sleep(1)
    assert True


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:19.786762
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(1.23)

    @work_in_progress("Loading file")
    def load_file(path: str):
        time.sleep(1.89)
        return True

    assert load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        time.sleep(3.78)

# Generated at 2022-06-13 20:10:44.443122
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress():
        time.sleep(1)
    with work_in_progress("Printer"):
        time.sleep(1)
    @work_in_progress()
    def test_fn(x):
        time.sleep(1)
        return x
    assert test_fn(1) == 1

# Generated at 2022-06-13 20:10:53.628678
# Unit test for function work_in_progress
def test_work_in_progress():

    print(work_in_progress.__doc__)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/home/hongyuan/git/datastructure/datastructure/basic_datastructure/Stack.p")
    print(obj)

    with work_in_progress("Saving file"):
        with open("/home/hongyuan/git/datastructure/test_wip.p", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:55.060306
# Unit test for function work_in_progress
def test_work_in_progress():
    assert True

# Generated at 2022-06-13 20:11:00.804027
# Unit test for function work_in_progress
def test_work_in_progress():
    def foo():
        time.sleep(1)

    def bar():
        with work_in_progress():
             time.sleep(1)

    print(foo)
    print(work_in_progress(bar))


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:09.395262
# Unit test for function work_in_progress
def test_work_in_progress():
    test_obj = {}
    for i in range(100000):
        test_obj[i] = i

    actual_return_value = None

    @work_in_progress("Loading file")
    def load_file(path):
        nonlocal actual_return_value
        with open(path, "rb") as f:
            actual_return_value = pickle.load(f)

    load_file("some_nonexistent_file")

    assert actual_return_value is None

    with work_in_progress("Reading testing object"):
        test_obj_copy = pickle.loads(pickle.dumps(test_obj))
        assert test_obj == test_obj_copy

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:15.629669
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    with open("one_hundred_thousand_integers_between_one_and_one_million", "wb") as f:
        pickle.dump(list(range(1, 1_000_000)), f)
    l = load_file("one_hundred_thousand_integers_between_one_and_one_million")
    assert len(l) == 999_999
    with open("one_hundred_thousand_integers_between_one_and_one_million", "rb") as f:
        l2 = pickle.load(f)
    assert l == l2


# Generated at 2022-06-13 20:11:16.002858
# Unit test for function work_in_progress
def test_work_in_progress():
    assert True

# Generated at 2022-06-13 20:11:19.493094
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test 1")
    def func1():
        time.sleep(1.5)

    with work_in_progress("Test 2"):
        time.sleep(1.5)

    func1()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:25.613663
# Unit test for function work_in_progress
def test_work_in_progress():

    print("Testing function work_in_progress...")

    # Test with decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)
    assert obj is not None

    # Test with context manager
    with work_in_progress("Saving file"):
        with open(__file__, "wb") as f:
            pickle.dump(obj, f)

    print("Success.\n\n")

test_work_in_progress()

# Generated at 2022-06-13 20:11:27.447801
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(0.2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:18.157406
# Unit test for function work_in_progress
def test_work_in_progress():

    def do_something(size):
        return [str(i) for i in range(size)]

    print("=== Testing work_in_progress ===")
    print("--- Default settings ---")
    with work_in_progress():
        l = do_something(10000000)
    print()

    print("--- Custom message text ---")
    with work_in_progress("Processing data"):
        l = do_something(10000000)
    print()

    print("--- Disable message text ---")
    with work_in_progress("") as ctx:
        l = do_something(10000000)
        ctx.desc = ""
    print()

    print("--- Custom error message ---")
    with work_in_progress("Loading file") as ctx:
        raise RuntimeError("File is not readable")
    print()

# Generated at 2022-06-13 20:12:21.210276
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress(desc="Testing work_in_progress")
    def test():
        time.sleep(2)

    test()
    assert True

# Generated at 2022-06-13 20:12:27.670655
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Load data")
    def load_data():
        with open("/path/to/data", "rb") as f:
            return pickle.load(f)

    load_data()
    assert True


if __name__ == '__main__':
    # Unit test
    test_work_in_progress()

# Generated at 2022-06-13 20:12:33.637203
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path) as f:
            return pickle.load(f)
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    @work_in_progress("Loading file")
    def load_file_with_message(path):
        with open(path) as f:
            return pickle.load(f)
    @work_in_progress("Saving file")
    def save_file_with_message(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = dict(a=1, b=2)
    path = "test.pkl"
    save_file(path, obj)

# Generated at 2022-06-13 20:12:37.108838
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Cleaning..."):
        time.sleep(0.5)
    @work_in_progress("Creating object")
    def create_object():
        time.sleep(0.8)
        return object()
    create_object()

# Generated at 2022-06-13 20:12:45.628838
# Unit test for function work_in_progress
def test_work_in_progress():
    """
    >>> print(test_work_in_progress.__doc__)
    (<function work_in_progress.<locals>.<lambda> at 0x7f3d2c4ed510>, None, None)
    >>> with work_in_progress("Simple test") as value:
    ...     time.sleep(1.57)
    Simple test... done. (1.57s)
    >>> value
    >>> @work_in_progress("Test with returns")
    ... def test_with_returns(x):
    ...     time.sleep(0.74)
    ...     return x
    ...
    ... value = test_with_returns(42)
    Test with returns... done. (0.74s)
    >>> value
    42
    """
    func = None

# Generated at 2022-06-13 20:12:52.983567
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-13 20:12:56.792313
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test preparation")
    def prepare():
        time.sleep(1)

    prepare()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:03.009280
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)

    with work_in_progress("Saving file"):
        with open(__file__, "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:07.529675
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test context manager
    with work_in_progress("Please wait"):
        time.sleep(1)

    # Test decorator
    @work_in_progress("Please wait")
    def foo(a, b):
        time.sleep(1)
        return a + b
    foo(1, 2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:33.964647
# Unit test for function work_in_progress
def test_work_in_progress():
    class xxx:
        @work_in_progress("working")
        def slow_method(self):
            time.sleep(0.1)
    x = xxx()
    x.slow_method()
    with work_in_progress("Working"):
        time.sleep(0.1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:44.114388
# Unit test for function work_in_progress
def test_work_in_progress():
    from io import StringIO
    import sys

    stdout = sys.stdout
    sys.stdout = stdout = StringIO()

    # Test for context manager
    with work_in_progress("Saving file"):
        time.sleep(0.1)

    # Test for decorator
    @work_in_progress("Loading file")
    def load_file():
        time.sleep(0.1)

    load_file()

    assert stdout.getvalue() == "Saving file... done. (0.10s)\nLoading file... done. (0.10s)\n"
    stdout.close()


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:46.573737
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sleeping for a bit")
    def foo():
        time.sleep(4)
    foo()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:56.241007
# Unit test for function work_in_progress
def test_work_in_progress():
    print("\n{}".format(work_in_progress.__doc__))
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)


# Generated at 2022-06-13 20:14:58.374593
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Sample"):
        time.sleep(2)

# Generated at 2022-06-13 20:15:03.468283
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert obj is not None

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:15:08.433457
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def test_work_in_progress_with_desc():
        with open('../README.rst', 'r', encoding='utf-8') as readme:
            readme_content = readme.read()
        return readme_content

    with work_in_progress():
        with open('../README.rst', 'r', encoding='utf-8') as readme:
            readme_content = readme.read()
    return readme_content


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:15:18.227468
# Unit test for function work_in_progress
def test_work_in_progress():
    descriptions = [
        "Doing some stuff",
        "Doing more stuff",
        "Doing even more stuff",
    ]
    with work_in_progress("Testing work_in_progress") as w:
        for d in descriptions:
            with work_in_progress(d):
                time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()