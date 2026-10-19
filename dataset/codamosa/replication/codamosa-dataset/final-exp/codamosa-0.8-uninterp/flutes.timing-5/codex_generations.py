

# Generated at 2022-06-13 20:05:23.607449
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(1)
    with work_in_progress("Test one"):
        time.sleep(1)
    assert True
    print()

    @work_in_progress("Test two")
    def test_work_in_progress_helper():
        time.sleep(1)
    test_work_in_progress_helper()
    assert True


if __name__ == "__main__":
    import pytest
    pytest.main(sys.argv)

# Generated at 2022-06-13 20:05:24.625112
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("This is a test"):
        time.sleep(3)

# Generated at 2022-06-13 20:05:29.599621
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Discarding dummy data"):
        time.sleep(0.52)
    print()

    @work_in_progress("Generating dummy data")
    def generate_dummy_data(n: int = 1000000):
        return [x for x in range(n)]

    data = generate_dummy_data()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:40.149410
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    mnist = load_file("tests/mnist.pkl")

    with work_in_progress("Saving file"):
        save_file(mnist, "tests/mnist2.pkl")

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    assert mnist == load_file("tests/mnist2.pkl")
    os.remove("tests/mnist2.pkl")

# Generated at 2022-06-13 20:05:48.875086
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile

    temp_file_path = tempfile.mktemp()

    with work_in_progress("Loading file") as progress:
        pass

    with work_in_progress("Saving file"):
        with open(temp_file_path, "w") as temp_file:
            temp_file.write("Hello, World!")

    with work_in_progress("Loading file"):
        with open(temp_file_path, "r") as temp_file:
            temp_file.read()

# Code profiling:
#     import cProfile, pstats
#     cProfile.run("test_work_in_progress()", filename="profile.stats")
#     p = pstats.Stats("profile.stats")
#     p.strip_dirs().sort_stats("cumulative").print_stats()

# Generated at 2022-06-13 20:05:57.091488
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

# Generated at 2022-06-13 20:06:06.837687
# Unit test for function work_in_progress
def test_work_in_progress():

    # Example 1
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
    obj = load_file("/path/to/some/file")

    # Example 2
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:06:15.472677
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = load_file("/path/to/some/file")
    save_file("/path/to/other/file", obj)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:22.119796
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(1)
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        time.sleep(1)
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:06:24.193428
# Unit test for function work_in_progress
def test_work_in_progress():
    import random

    @work_in_progress("Testing work_in_progress")
    def test():
        time.sleep(random.randint(1, 5))

    test()

# Generated at 2022-06-13 20:06:37.417073
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit testing for function `work_in_progress`.
    """
    import os

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    path = 'test_work_in_progress.pickle'
    if os.path.exists(path):
        os.remove(path)

    with open(path, "wb") as f:
        pickle.dump(range(100), f)

    with open(path, "rb") as f:
        pickle.load(f)
    os.remove(path)

# Generated at 2022-06-13 20:06:47.110944
# Unit test for function work_in_progress
def test_work_in_progress():
    import random

    # Test a decorated function
    @work_in_progress("My in-progress work")
    def wait():
        time.sleep(random.uniform(0.5, 3))

    wait()

    # Test a with context manager
    with work_in_progress("My in-progress work"):
        time.sleep(random.uniform(0.5, 3))


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:51.788357
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Work in progress"
    with work_in_progress(desc):
        time.sleep(1)

    print(desc + "... ", end='', flush=True)
    begin_time = time.time()
    time.sleep(1)
    time_consumed = time.time() - begin_time
    print(f"done. ({time_consumed:.2f}s)")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:56.252114
# Unit test for function work_in_progress
def test_work_in_progress():
    for method, count in (
        (print, 10_000),
        (time.sleep, 1),
    ):
        with work_in_progress("Running test"):
            for _ in range(count):
                method(".")

# Generated at 2022-06-13 20:07:05.486827
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        """Helper function."""
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def load_with_wip(path):
        return load_file(path)

    with tempfile.NamedTemporaryFile() as tmpfile:
        obj = [1, 2, 3, 4, 5]
        pickle.dump(obj, tmpfile)
        tmpfile.seek(0)
        assert load_file(tmpfile.name) == obj
        assert load_with_wip(tmpfile.name) == obj

    with tempfile.NamedTemporaryFile() as tmpfile:
        obj = [1, 2, 3, 4, 5]

# Generated at 2022-06-13 20:07:15.522669
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    with work_in_progress("Loading file"):
        obj = load_file("tests/data/example.jpg")
    with work_in_progress("Saving file"):
        with open("tests/data/example.jpg_copy.jpg", "wb") as f:
            pickle.dump(obj, f)
    with work_in_progress("Loading file without function"):
        obj = load_file("tests/data/example.jpg")
    with open("tests/data/example.jpg_copy.jpg", "rb") as f:
        obj_copy = pickle.load(f)
    assert obj == obj_copy



# Generated at 2022-06-13 20:07:21.104264
# Unit test for function work_in_progress
def test_work_in_progress():

    def test_function():
        time.sleep(0.1)
        return 1

    assert list(map(test_function, range(5))) == [1, 1, 1, 1, 1]

    @work_in_progress("Computing")
    def test_function():
        time.sleep(0.1)
        return 1

    assert list(map(test_function, range(5))) == [1, 1, 1, 1, 1]

    with work_in_progress("Computing"):
        time.sleep(0.1)



# Generated at 2022-06-13 20:07:23.371909
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def test():
        time.sleep(0.001)
    test()

# Generated at 2022-06-13 20:07:25.202270
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Testing"):
        time.sleep(5)

# Generated at 2022-06-13 20:07:33.186500
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Loading file"
    path = "/path/to/some/file"
    # Test function decorator
    @work_in_progress(desc)
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # Test context-manager
    def save_file(path):
        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)

    obj = load_file(path)
    save_file(path)
    return True

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:42.616100
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("test/test.pickle")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:07:50.293118
# Unit test for function work_in_progress
def test_work_in_progress():
    # A coroutine that yields periodically (approximately once every 0.5 s)
    @contextlib.contextmanager
    def sleeping_coroutine():
        while True:
            yield time.time()
            time.sleep(0.5)

    # Testing the function
    sc = sleeping_coroutine()
    with work_in_progress("Loading pickled data"):
        print("Data loaded...")
        t1 = next(sc)
        time.sleep(1.5)
        print("Data processed...")
        t2 = next(sc)
        time.sleep(2)
        print("Data saved...")
        t3 = next(sc)
    assert t1 < t2 < t3 < t3 + 0.01
    print("All tests passed")

if __name__ == '__main__':
    test_work_in

# Generated at 2022-06-13 20:07:59.186214
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    # Test function
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("pickle_file")

    # Test context manager
    with work_in_progress("Saving file"):
        with open("pickle_file", "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:08:05.661679
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(1.2)
        return "Done"
    obj = load_file("/path/to/some/file")
    assert obj == "Done"

    class SomeClass:
        def __init__(self):
            self.value = ""

        def set_value(self, value):
            self.value = value

    my_obj = SomeClass()
    with work_in_progress("Saving file"):
        time.sleep(2.1)
        my_obj.set_value("Done")
    assert my_obj.value == "Done"

# Generated at 2022-06-13 20:08:09.484716
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test as a context manager
    with work_in_progress("Loading file"):
        time.sleep(3.52)
    # Test as a decorator
    @work_in_progress("Saving file")
    def save_file(path):
        time.sleep(3.78)
    save_file("/path/to/some_file")



# Generated at 2022-06-13 20:08:14.931950
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test the function work_in_progress above."""
    def f1():
        with work_in_progress("f1"):
            time.sleep(0.5)

    def f2():
        @work_in_progress("f2")
        def ff():
            time.sleep(0.5)
        ff()

    def f3():
        with work_in_progress("f3"):
            ff()
        @work_in_progress("f4")
        def ff():
            time.sleep(0.5)

    f1()
    f2()
    f3()


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:21.368855
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(2)
        return path

    @work_in_progress("Saving file")
    def save_file(path):
        time.sleep(2)
        return path

    assert load_file("/path/to/some/file") == "/path/to/some/file"
    assert save_file("/path/to/some/file") == "/path/to/some/file"

# Generated at 2022-06-13 20:08:25.040220
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import sys
    import io
    with io.StringIO() as buf, redirect_stdout(buf):
        with work_in_progress("Testing"):
            time.sleep(1)
        output = buf.getvalue()
    assert 'Testing... done' in output


# Generated at 2022-06-13 20:08:28.310806
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def foo():
        a = []
        for i in range(1, 100):
            a.append(2 ** i)
            time.sleep(0.05)
    foo()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:44.419290
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile
    import pickle
    import os
    import shutil
    import yaml

    # Environment
    tmp_path = tempfile.gettempdir()
    tmp_file_path = os.path.join(tmp_path, "test.pickle")
    tmp_file_yaml_path = os.path.join(tmp_path, "test.yaml")

    # Prepare the data
    data = {
        "data": [6, 28, 496, 8128, 33550336],
        "description": "Sums of divisors of the natural numbers",
    }

    # Dump data
    @work_in_progress("Saving file")
    def dump():
        with open(tmp_file_path, "wb") as f:
            pickle.dump(data, f)

    dump()


# Generated at 2022-06-13 20:08:52.893981
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("/path/to/some/file")
    del obj

    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)
    return

# Generated at 2022-06-13 20:08:58.767865
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

# Generated at 2022-06-13 20:09:07.166875
# Unit test for function work_in_progress
def test_work_in_progress():
    from pytest import raises
    from pathlib import Path
    from numpy import random
    
    import pickle

    pkl_file = Path(__file__).parent/'test_wip.pkl'

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, data):
        with open(path, "wb") as f:
            pickle.dump(data, f)

    with raises(FileNotFoundError):
        load_file(pkl_file)

    data_to_save = random.rand(1,10)
    save_file(pkl_file, data_to_save)
    

# Generated at 2022-06-13 20:09:16.393164
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test for function work_in_progress."""
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = load_file("/path/to/some/file")
    save_file(obj, "/path/to/some/other/file")

# Generated at 2022-06-13 20:09:20.291413
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
        with work_in_progress("Saving file"):
            time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:24.685366
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    failure_count, test_count = doctest.testmod()
    assert test_count > 0
    assert failure_count == 0


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:29.312114
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test with a function
    @work_in_progress("Testing work_in_progress()")
    def test():
        time.sleep(0.1)

    # Test with a code block
    with work_in_progress("Testing work_in_progress()"):
        time.sleep(0.1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:37.264289
# Unit test for function work_in_progress
def test_work_in_progress():
    import itertools
    import time

    # Prepare a function that will take some time to execute
    def timer_func(n):
        list(itertools.repeat(1, n))

    # Test default usage
    func_timeout = 1e-10
    with work_in_progress("Count to a big integer"):
        time.sleep(func_timeout)

    # Test function decorator
    @work_in_progress("Count to a bigger integer")
    def timer_func(n):
        list(itertools.repeat(1, n))

    timer_func(1e10)

    assert True

# Generated at 2022-06-13 20:09:41.425036
# Unit test for function work_in_progress
def test_work_in_progress():
    import textwrap
    from io import StringIO
    with contextlib.redirect_stdout(StringIO()) as stdout:
        with work_in_progress("Computing solutions of some equations"):
            time.sleep(1.23)
        assert stdout.getvalue() == textwrap.dedent("""
            Computing solutions of some equations... done. (1.23s)
        """).strip() + "\n"

# Generated at 2022-06-13 20:09:49.223892
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import pickle
    import numpy as np

    arr = np.random.rand(100, 100)

    with work_in_progress("Randomizing array"):
        arr *= random.randint(2, 3)

    with work_in_progress("Serializing"):
        arr = pickle.dumps(arr)

    with work_in_progress("Deserializing"):
        arr = pickle.loads(arr)

    assert arr.shape == (100, 100), \
        "array has wrong shape after deserialization"


# Generated at 2022-06-13 20:09:55.331671
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Running unit test")
    def test():
        time.sleep(3)

    test()

# Generated at 2022-06-13 20:09:59.820708
# Unit test for function work_in_progress
def test_work_in_progress():
    import types
    @work_in_progress("Test work_in_progress")
    def sleep(sec):
        time.sleep(sec)
    sleep(0.1)
    assert True
    assert isinstance(sleep, types.FunctionType)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:03.433015
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test function work_in_progress.

    .. code:: python
        >>> with work_in_progress("Test"):
        ...     print("hello")
        ...
        Test... hello
        done. (0.00s)
    """

# Generated at 2022-06-13 20:10:07.332974
# Unit test for function work_in_progress
def test_work_in_progress():
    begin_time = time.time()
    with work_in_progress("test"):
        time.sleep(0.5)
    end_time = time.time()
    assert (end_time - begin_time) > 0.5
    assert (end_time - begin_time) < 0.55

# Generated at 2022-06-13 20:10:08.439881
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1.1)

# Generated at 2022-06-13 20:10:19.217041
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import random
    import string
    import tempfile

    def load_file(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)

    def save_file(file_name, obj):
        with open(file_name, "wb") as f:
            pickle.dump(obj, f)

    with tempfile.TemporaryDirectory() as temp_dir:
        save_file(temp_dir + "/test.dat", "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20000000)))
        load_file(temp_dir + "/test.dat")
        print("\n")


# Generated at 2022-06-13 20:10:21.150528
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.2)

# Generated at 2022-06-13 20:10:28.730774
# Unit test for function work_in_progress
def test_work_in_progress():
    from pathlib import Path
    from .output import capture_stderr
    from .fs import rm
    from .time import sleep

    # Save file
    cwd = Path.cwd()
    with capture_stderr() as buffer:
        with work_in_progress("Saving file"):
            with Path(__file__).open("w") as f:
                f.write("hello world")
    assert buffer.getvalue().strip() == f"Saving file... done. (0.00s)"
    rm(cwd / __file__)

    # Check function output
    def dummy_fn(dur: float = 0.5):
        with work_in_progress("Doing some useless work"):
            sleep(dur)
        return 0

    with capture_stderr() as buffer:
        dummy_fn

# Generated at 2022-06-13 20:10:37.723295
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Preparing"):
        time.sleep(1.7)
    time.sleep(0.3)
    @work_in_progress("Loading")
    def load_file(path):
        time.sleep(2.1)
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving")
    def save_file(obj, path):
        time.sleep(1.3)
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    data_path = "test.data"
    with open(data_path, "wb") as f:
        pickle.dump("data", f)
    
    data = load_file(data_path)

# Generated at 2022-06-13 20:10:45.796610
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import unittest

    print("Testing `work_in_progress`...")

    # Function as context manager
    print(">> Testing function as context manager")
    @work_in_progress("Waiting for a second")
    def _():
        time.sleep(1)
    _()

    # Context Manager
    print(">> Testing context manager")
    with work_in_progress("Waiting for a second"):
        time.sleep(1)

    print("Passed.")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:51.755740
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:57.873724
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Generating a bunch of random numbers"):
        time.sleep(0.12)
    with work_in_progress("Waiting for a long time"):
        time.sleep(0.13)


# Generated at 2022-06-13 20:11:04.805137
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
    test_work_in_progress()

# Generated at 2022-06-13 20:11:14.112601
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
    test_work_in_progress()

# Generated at 2022-06-13 20:11:17.076355
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

# Generated at 2022-06-13 20:11:18.079577
# Unit test for function work_in_progress
def test_work_in_progress():
    assert work_in_progress(None) is None

# Generated at 2022-06-13 20:11:20.348347
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3)
    assert True


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:20.913515
# Unit test for function work_in_progress
def test_work_in_progress():
    pass

# Generated at 2022-06-13 20:11:28.787673
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    import tempfile
    tmp_dir = tempfile.TemporaryDirectory()

    with tmp_dir as tmp_dir_pathname:
        # Loading file
        with open(os.path.join(tmp_dir_pathname, "sample_file.pickle"), "wb") as f:
            pickle.dump(((1, 2), ('a', 'b')), f)


# Generated at 2022-06-13 20:11:32.566351
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

# Generated at 2022-06-13 20:11:45.402096
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test cases for function work_in_progress"""
    from pathlib import Path
    import tempfile

    tmp_dir = Path(tempfile.mkdtemp(prefix="tmp_"))
    tmp_file = tmp_dir / "test_work_in_progress.dat"


# Generated at 2022-06-13 20:11:47.522628
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Work in progress"):
        time.sleep(0.05)

# Generated at 2022-06-13 20:11:50.749085
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading files"):
        time.sleep(1)


if __name__ == "__main__":
    # test_work_in_progress()
    """
    conda activate vit
    python -m utils.progress
    """
    pass

# Generated at 2022-06-13 20:11:57.636758
# Unit test for function work_in_progress
def test_work_in_progress():
    def should_take_around(long_seconds: float):
        with work_in_progress("Long task"):
            time.sleep(long_seconds)
    should_take_around(1)
    should_take_around(2.5)

# Test work_in_progress()
if __name__ == "__main__":
    test_work_in_progress()

# vim: ts=4 sw=4 sts=4 expandtab

# Generated at 2022-06-13 20:12:12.527365
# Unit test for function work_in_progress
def test_work_in_progress():
    from .test_utils import TestReporter
    reporter = TestReporter()

    # test function decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    print_messages = reporter.get_print_messages()
    assert len(print_messages) == 2
    assert print_messages[0] == "Loading file... "
    assert print_messages[1].startswith("Loading file... done. (")
    assert print_messages[1].endswith("s)")

    # test context manager

# Generated at 2022-06-13 20:12:26.679932
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import pickle
    # Test work in progress decorator.
    @work_in_progress("Test work in progress decorator")
    def func_test_work_in_progress_decorator():
        obj = []
        for i in range(10):
            obj.append(random.random())
            time.sleep(random.random())

        with open("/tmp/test_work_in_progress_decorator.pkl", "wb") as f:
            pickle.dump(obj, f)

    func_test_work_in_progress_decorator()

    # Test work in progress context manager.
    with work_in_progress("Test work in progress context manager"):
        obj = []
        for i in range(10):
            obj.append(random.random())

# Generated at 2022-06-13 20:12:29.094217
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        pass


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:31.427155
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing function"):
        time.sleep(1)
    # Testing function... done. (1.00s)

# Generated at 2022-06-13 20:12:39.647008
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    with work_in_progress("Saving file"):
        with open("/path/to/some/other/file", "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:12:50.290763
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path: str = "/path/to/some/file"):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file()
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:05.525620
# Unit test for function work_in_progress
def test_work_in_progress():

    def assert_msg(msg, expected, real):
        expected_str = str(expected)
        real_str = str(real)
        if expected_str != real_str:
            print(f"{msg}: expected \"{expected_str}\" "
                  f"but got \"{real_str}\"")

    def assert_work_in_progress(desc, expected_time, func):
        now = time.time()
        assert_func = func(desc)
        assert_msg(desc, expected_time, time.time() - now)
        assert_func

    assert_work_in_progress("Loading File", 0.0, lambda desc: \
        work_in_progress(desc))

# Generated at 2022-06-13 20:13:11.428291
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:13:14.098587
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def test_func():
        for i in range(0, 10**8):
            pass
    test_func()

# Generated at 2022-06-13 20:13:16.205372
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:22.051537
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test context manager
    @work_in_progress("Running test")
    def f():
        time.sleep(.5)
    # Test decorator
    @work_in_progress("Running test")
    def f():
        time.sleep(.5)
    # Test in a context manager
    with work_in_progress(desc = "Running test in a mananger"):
        time.sleep(.7)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:28.803923
# Unit test for function work_in_progress
def test_work_in_progress():
    def fact(n):
        if n <= 1:
            return 1
        return n * fact(n - 1)

    with work_in_progress("Test for work_in_progress"):
        time.sleep(0.5)
        x = fact(500)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:39.790820
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("../test_data/test.pickle")

    with work_in_progress("Saving file"):
        with open("../test_data/test_out.pickle", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:42.534313
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test work_in_progress")
    def foo():
        time.sleep(1.1)

    foo()
    assert True

if __name__ == '__main__':

    test_work_in_progress()

# Generated at 2022-06-13 20:13:45.387257
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(0.2)
    with work_in_progress("Loading file"):
        time.sleep(0.5)
    with work_in_progress():
        time.sleep(0.3)

# Generated at 2022-06-13 20:13:51.690398
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving file"):
        with open('/tmp/test', 'wb') as f:
            pickle.dump({'key': 'value'}, f)

    assert True

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:05.032677
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Starting up"):
        time.sleep(0.5)
    print()

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)
    print()

    with work_in_progress("Saving file"):
        with open(__file__, "wb") as f:
            pickle.dump(obj, f)
    return


# main
if __name__ == "__main__":
    # Unit test for function work_in_progress
    test_work_in_progress()

# Generated at 2022-06-13 20:14:09.331838
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

# Generated at 2022-06-13 20:14:15.057237
# Unit test for function work_in_progress
def test_work_in_progress():
    res = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5"}
    with work_in_progress("Loading file"):
        time.sleep(2)
    with work_in_progress("Saving file"):
        time.sleep(2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:17.036875
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Running test"):
        time.sleep(3)

# Generated at 2022-06-13 20:14:20.180368
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.5)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:30.163377
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    from contextlib import redirect_stdout, redirect_stderr

    with redirect_stdout(None), redirect_stderr(None):
        with work_in_progress("A task that waits for 5 seconds"):
            time.sleep(5)
        with work_in_progress("A task that waits for 10 seconds"):
            time.sleep(10)
        with work_in_progress("A task that waits for 15 seconds"):
            time.sleep(15)
        with work_in_progress("A task that waits for 20 seconds"):
            time.sleep(20)
        with work_in_progress("A task that waits for 25 seconds"):
            time.sleep(25)
        with work_in_progress("A task that waits for 30 seconds"):
            time.sleep(30)

# Generated at 2022-06-13 20:14:36.266283
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import os
    import random
    import tempfile
    import shutil
    import copy

    path = None
    obj = None

    def prepare():
        nonlocal path, obj

        # Prepare data for testing purpose
        obj = {
            "abc": 5,
            "cba": [i for i in range(20)],
            "bac": {i: i * i for i in range(10)},
        }

        fd, path = tempfile.mkstemp()
        try:
            with os.fdopen(fd, 'wb') as f:
                pickle.dump(obj, f)
        except:
            os.remove(path)
            raise

        # Recreate obj
        obj = None

# Generated at 2022-06-13 20:14:37.836047
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing this function"):
        time.sleep(1)

# Generated at 2022-06-13 20:14:41.528836
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    time.sleep(1)


# Generated at 2022-06-13 20:14:44.055479
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("I'm working")
    def task():
        time.sleep(1)
    task()

# Generated at 2022-06-13 20:15:05.640386
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Unit test"):
        time.sleep(0.3)

# Generated at 2022-06-13 20:15:11.397397
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    print(obj)

    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)

    print("All tests passed.")

# test_work_in_progress()

# Generated at 2022-06-13 20:15:20.126052
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