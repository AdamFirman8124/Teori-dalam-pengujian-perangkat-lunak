

# Generated at 2022-06-13 20:05:22.608652
# Unit test for function work_in_progress
def test_work_in_progress():

    from io import StringIO

    class MyClass:
        pass

    output = StringIO()
    with contextlib.redirect_stdout(output):
        with work_in_progress("Testing work_in_progress()"):
            time.sleep(1)
    
    assert "Testing work_in_progress" in output.getvalue()

# Generated at 2022-06-13 20:05:24.591475
# Unit test for function work_in_progress
def test_work_in_progress():
    from tempfile import NamedTemporaryFile
    from pathlib import Path

    with NamedTemporaryFile(mode="w+b") as tmpf:
        filepath = Path(tmpf.name)

        with work_in_progress("Testing work_in_progress"):
            # Simulate relatively long work
            with filepath.open("wb") as f:
                f.write(b"Foobar")
                time.sleep(0.1)

# Generated at 2022-06-13 20:05:31.548113
# Unit test for function work_in_progress
def test_work_in_progress():
    # Load a file
    path = "/path/to/file"

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(path)
    # Loading file... done. (3.52s)
    time.sleep(3)

    # Save a file
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    # Saving file... done. (3.78s)
    time.sleep(3)

# Generated at 2022-06-13 20:05:36.301809
# Unit test for function work_in_progress
def test_work_in_progress():
    from os import makedirs, rmdir
    from pathlib import Path
    from shutil import rmtree
    from tempfile import TemporaryDirectory
    tmp = TemporaryDirectory()
    try:
        with work_in_progress("Creating directory"):
            makedirs(Path(tmp.name, "a", "b", "c", "d", "e"), exist_ok=True)
        with work_in_progress("Removing directory"):
            rmdir(Path(tmp.name, "a", "b", "c", "d", "e"))
        with work_in_progress("Recursively removing directory"):
            rmtree(Path(tmp.name, "a"))
    finally:
        tmp.cleanup()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:05:39.918888
# Unit test for function work_in_progress
def test_work_in_progress():
    from tempfile import NamedTemporaryFile

    def func(path: str, delay: float):
        with open(path, "wb") as f:
            time.sleep(delay)
            pickle.dump("test", f)

    with NamedTemporaryFile() as f:
        with work_in_progress("Saving file"):
            func(f.name, 0.2)
        with work_in_progress("Loading file"):
            pickle.load(f)

# Generated at 2022-06-13 20:05:42.266142
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Counting to 100"):
        print(sum(range(100)))

import logging

__all__ = [
    "with_logging",
]



# Generated at 2022-06-13 20:05:46.936187
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Sleep for a while"):
        time.sleep(3.5)
    print()
    @work_in_progress("Load file")
    def load_file():
        time.sleep(3.5)
    load_file()

# Generated at 2022-06-13 20:05:57.091789
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(2)
    @work_in_progress("Computing value")
    def compute_value():
        time.sleep(0.5)
    compute_value()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:05.646827
# Unit test for function work_in_progress
def test_work_in_progress():
    def func1():
        with work_in_progress("Loading file"):
            time.sleep(1.0)

    try:
        func1()
    except Exception as e:
        print(e)
    finally:
        pass
    try:
        with work_in_progress("Loading file"):
            time.sleep(1.0)
    except Exception as e:
        print(e)
    finally:
        pass

    def func2(path):
        with work_in_progress("Loading file"):
            time.sleep(1.0)

    try:
        func2("/path/to/file")
    except Exception as e:
        print(e)
    finally:
        pass


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:14.802500
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/home/xinya/Documents/courses/ling572/nltktest/test.pickle")
    print(obj)

    with work_in_progress("Saving file"):
        with open("/home/xinya/Documents/courses/ling572/nltktest/test.pickle", "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:26.554223
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    path = "/tmp/python_util_test_work_in_progress.bin"

    print("Testing work_in_progress decorator...")
    start_time = time.time()
    obj = load_file(path)
    print(f"Loading time: {time.time() - start_time:.2f}s")

    start_time = time.time()
    save_file(path, obj)

# Generated at 2022-06-13 20:06:34.105444
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test a function using work_in_progress
    @work_in_progress("Running function")
    def function():
        time.sleep(0.5)

    function()

    # Test a code block
    with work_in_progress("Running code block"):
        time.sleep(0.5)

    # Test description with quotes
    with work_in_progress("Running \"code block\""):
        time.sleep(0.5)

# Generated at 2022-06-13 20:06:41.869634
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.5)

    @work_in_progress("Saving file")
    def save_file():
        time.sleep(0.5)
    save_file()


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:50.174874
# Unit test for function work_in_progress

# Generated at 2022-06-13 20:06:55.263773
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file():
        pass

    with work_in_progress("Loading file"):
        pass


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:00.714933
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test context manager"):
        time.sleep(1)

    @work_in_progress("Test decorator")
    def test_decorator():
        time.sleep(1)

    test_decorator()


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:07:04.229085
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Counting to 20 million"):
        a = 0
        for i in range(20_000_000):
            a += 1
    assert a == 20_000_000

# Generated at 2022-06-13 20:07:06.184539
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Dummy task"):
        pass


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:14.253699
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("test_pickle.pkl")

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    save_file("test_pickle.pkl", obj)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:20.121465
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)
    with work_in_progress("Saving file"):
        with open("/tmp/test.py", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:29.438894
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("test.pickle")
    assert isinstance(obj, np.ndarray)

    with work_in_progress("Saving file"):
        with open("test.pickle", "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:07:41.244953
# Unit test for function work_in_progress
def test_work_in_progress():
    # Imports
    import pickle
    import tempfile

    obj = {
        "a",
        (1, 2, 3),
        [4, 5, 6],
        {1, 2, 3},
        {'a': 1, 'b': 2, 'c': 3}
    }

    with tempfile.TemporaryDirectory() as temp_dir:
        path_in = Path(temp_dir) / "file.in"
        path_out = Path(temp_dir) / "file.out"
        with path_in.open("wb") as f:
            pickle.dump(obj, f)

        with work_in_progress("Loading file"):
            with path_in.open("rb") as f:
                obj_clone = pickle.load(f)


# Generated at 2022-06-13 20:07:49.011865
# Unit test for function work_in_progress
def test_work_in_progress():
    import re

    @work_in_progress()
    def inner_function():
        time.sleep(0.03)

    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        inner_function()
        assert re.match(r"Work in progress\.\.\. done\. \(0\.[0-9]+s\)", fake_out.getvalue().strip()) is not None, \
                "Failed to report correct execution time"

    @work_in_progress("Task")
    def inner_function2():
        time.sleep(0.05)

    with mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
        inner_function2()

# Generated at 2022-06-13 20:07:54.179489
# Unit test for function work_in_progress
def test_work_in_progress():
    try:
        with work_in_progress("Testing work_in_progress()") as t:
            time.sleep(1)
        print(f"Took {t.total_seconds()} seconds.")
    except AttributeError:
        print("AttributeError: 'NoneType' object has no attribute 'total_seconds'")

# Generated at 2022-06-13 20:08:00.849169
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import os
    import tempfile

    with tempfile.TemporaryDirectory(prefix="pysay-") as tempdir:
        with work_in_progress("Loading file"):
            time.sleep(0.5)
            with open(os.path.join(tempdir, "test_file.txt"), "a"):
                pass
            time.sleep(0.5)

# Generated at 2022-06-13 20:08:07.536769
# Unit test for function work_in_progress
def test_work_in_progress():
    import unittest.mock
    with unittest.mock.patch("builtins.print") as mock_print:
        with work_in_progress(desc="Test"):
            mock_time = unittest.mock.Mock(side_effect=[0, 1])
            with unittest.mock.patch("time.time", mock_time):
                time.sleep(1)
                assert mock_time.call_count == 2

    assert mock_print.call_count == 2
    assert mock_print.call_args_list[0][0] == ("Test... ",)
    assert mock_print.call_args_list[1][0][0].startswith("done. (")

# Generated at 2022-06-13 20:08:11.024190
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing function work_in_progress")
    def _test():
        time.sleep(3)
        return "This is a test"

    assert _test() == "This is a test"

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:13.038309
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)

    with work_in_progress():
        time.sleep(2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:21.604521
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test of work_in_progress."""

    # Test with context manager
    with work_in_progress("Test with context manager"):
        x = 1
        for i in range(1000000):
            x = x * 1.01

    # Test with decorator
    @work_in_progress
    def test_work_with_decorator(x):
        for i in range(1000000):
            x = x / 0.99 + 1

    test_work_with_decorator(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:27.610902
# Unit test for function work_in_progress
def test_work_in_progress():
    print("*" * 80)
    print("Unit test for function `work_in_progress`:")
    print("-" * 80)

    with work_in_progress("This is a test"):
        time.sleep(1)
    print("-" * 80)

    @work_in_progress("This is a test 2")
    def f():
        time.sleep(2)
    f()
    print("-" * 80)
    print("Test passed.")
    print("*" * 80)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:41.449075
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("A small amount of work")
    def _():
        time.sleep(0.05)
    _()

    @work_in_progress("A large amount of work")
    def _():
        time.sleep(0.2)
    _()

    @work_in_progress("A tiny amount of work")
    def _():
        pass
    _()

# Generated at 2022-06-13 20:08:51.397418
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    t = time.time()
    obj = load_file("/Users/paul/Projects/README.md")
    load_time = time.time() - t
    print(f"Load time: {load_time:.2f}s")

    t = time.time()
    save_file(obj, "test.md")
    save_time = time.time() - t

# Generated at 2022-06-13 20:08:55.879624
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        time.sleep(3.52)
        return path

    assert load_file("test") == "test"
    assert load_file("test") == "test"

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:57.949012
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(0.5)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:09:02.503106
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function work_in_progress."""
    with work_in_progress("Loading file"):
        time.sleep(0.3)
        for _ in range(1000):
            a = 0
            for _ in range(10000):
                a += 1
    print("Result:", a)


# Generated at 2022-06-13 20:09:07.711363
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert isinstance(obj, dict)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:09:11.144830
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def run():
        time.sleep(1)

    run()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:17.187809
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Step 1"):
        time.sleep(0.5)
    with work_in_progress("Step 2"):
        time.sleep(0.3)
    with work_in_progress("Step 3"):
        time.sleep(0.2)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:09:19.227948
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1)

# Generated at 2022-06-13 20:09:29.415876
# Unit test for function work_in_progress
def test_work_in_progress():
    # Prepare a test file
    _test_filename = "test_work_in_progress.pickle"
    test_data = list(range(1000))
    with open(_test_filename, "wb") as f:
        pickle.dump(test_data, f)

    # Test the context manager
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    my_list = None
    with work_in_progress("Loading file"):
        my_list = load_file(_test_filename)

    # Test the decorator
    @work_in_progress("Saving list")
    def save_list(my_list, path):
        with open(path, "wb") as f:
            pickle.dump(my_list, f)
   

# Generated at 2022-06-13 20:09:48.670599
# Unit test for function work_in_progress
def test_work_in_progress():
    path = "/path/to/some/file"
    with tempfile.TemporaryDirectory() as tempdir:
        obj = list(range(1000))
        with work_in_progress("Saving file"):
            with open(tempdir + path, "wb") as f:
                pickle.dump(obj, f)
        with work_in_progress("Loading file"):
            with open(tempdir + path, "rb") as f:
                obj_ = pickle.load(f)
        assert obj == obj_

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:51.484843
# Unit test for function work_in_progress
def test_work_in_progress():
    from . import test_helpers as helpers
    from . import test_work_in_progress as target
    with helpers.with_cli_args(["--runslow"]):
        helpers.run_tests(target, ["test_work_in_progress"])

# Generated at 2022-06-13 20:09:55.954545
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Sleeping for a second"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:00.765965
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function :py:func:`work_in_progress`"""
    import random

    @work_in_progress("Some computation")
    def my_function(x, y):
        """Some computation"""
        return x + y

    assert my_function(3, 4) == 7

# Generated at 2022-06-13 20:10:04.319837
# Unit test for function work_in_progress
def test_work_in_progress():

    @work_in_progress("Loading")
    def load_data():
        time.sleep(3)
        return "data"

    with work_in_progress("Saving"):
        time.sleep(3)

    data = load_data()
    assert data == "data"

# Generated at 2022-06-13 20:10:10.067171
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import array

    @work_in_progress("Preparing a random array")
    def make_random_array():
        arr = array.array("I")
        arr.fromlist(random.choices(range(0xFFFFFFFF), k=10000))
        return arr

    arr = make_random_array()
    with work_in_progress("Sorting array"):
        arr.sort()
    print(repr(arr[:10]))


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:12.385921
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file") as w:
        with open("test.log", "w") as f:
            f.write("Loading file... done. (3.52s)\n")
    assert w.__next__() is None

# Generated at 2022-06-13 20:10:17.344781
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

# Generated at 2022-06-13 20:10:20.406667
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Getting my money"):
        time.sleep(0.5)
    assert True

# test_work_in_progress()

# Generated at 2022-06-13 20:10:21.648965
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work in progress"):
        time.sleep(1)

# Generated at 2022-06-13 20:10:46.067036
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress context")
    def _test():
        time.sleep(0.5)

    _test()

# Generated at 2022-06-13 20:10:51.004971
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress...")
    def _work_in_progress(n):
        sum([i ** 2 for i in range(n)])
    _work_in_progress(100_000_000)
    with work_in_progress("Testing work in progress with context manager..."):
        sum([i ** 2 for i in range(100_000_000)])

# Generated at 2022-06-13 20:10:56.905212
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
    print("Test function work_in_progress done.")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:57.625067
# Unit test for function work_in_progress
def test_work_in_progress():
    assert work_in_progress()


# Generated at 2022-06-13 20:11:03.270707
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Testing function work_in_progress...")
    time.sleep(1.52)
    for i in range(3):
        with work_in_progress(f"Task {i}"):
            time.sleep(0.51)
    print("All tests passed.")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:04.804489
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(1)
    time.sleep(1)

# Generated at 2022-06-13 20:11:08.367707
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:17.114535
# Unit test for function work_in_progress
def test_work_in_progress():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as td:
        test_file_path = Path(td) / "test_file.pkl"
        with test_file_path.open("wb") as test_file:
            pickle.dump({"test_data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, test_file)
        with work_in_progress(f"Loading file {test_file_path.name}"):
            with test_file_path.open("rb") as test_file:
                obj = pickle.load(test_file)
        assert obj == {"test_data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}

# Generated at 2022-06-13 20:11:22.769827
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("data/sample.pkl")

    with work_in_progress("Saving file"):
        with open("data/sample_copy.pkl", "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:11:26.903174
# Unit test for function work_in_progress
def test_work_in_progress():
    def func(x):
        return x*2

    def slow_func(x):
        time.sleep(x)
        return func(x)

    with work_in_progress("Function called"):
        result = func(4)

    assert result == 8

    with work_in_progress("Function called"):
        result = slow_func(4)

    assert result == 8



# Generated at 2022-06-13 20:12:13.122543
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:26.192516
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            time.sleep(3)
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert type(obj) == dict

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            time.sleep(4)
            pickle.dump(obj, f)

    save_file("/path/to/some/file", obj)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:28.886370
# Unit test for function work_in_progress
def test_work_in_progress():
    begin_time = time.time()
    with work_in_progress("Testing"):
        time.sleep(3)
    assert time.time() - begin_time >= 3

# Generated at 2022-06-13 20:12:38.171608
# Unit test for function work_in_progress
def test_work_in_progress():  # pylint: disable = missing-function-docstring
    import pandas as pd
    import pandas_flavor as pf

    data = pf.read_csv("data/iris.csv")  # type: ignore

    with work_in_progress("Loading iris dataset"):
        time.sleep(3)
        data = pd.read_csv("data/iris.csv")

    @work_in_progress("Saving iris dataset")
    def save_data(path):
        time.sleep(3)
        data.to_csv(path)
    save_data("/tmp/iris.csv")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:40.966491
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(3)

test_work_in_progress()

# Generated at 2022-06-13 20:12:43.272670
# Unit test for function work_in_progress
def test_work_in_progress():
    def foo():
        with work_in_progress("Loading file"):
            time.sleep(1)
        with work_in_progress("Saving file"):
            time.sleep(2)

    foo()

# Generated at 2022-06-13 20:12:47.654572
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(2)

# if __name__ == "__main__":
#     test_work_in_progress()

# Generated at 2022-06-13 20:12:53.975741
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = load_file("/path/to/some/file")
    save_file("/path/to/some/other/file", obj)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:55.455429
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def foo():
        time.sleep(0.1)
    foo()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:58.899937
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing WIP decorator")
    def foo():
        time.sleep(1)
        return 42

    assert foo() == 42


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:39.442016
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import pickle
    import tempfile
    
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(tmpdirname+"/file", "wb") as f:
            pickle.dump(random.random(), f)
        obj = load_file(tmpdirname+"/file")

    assert(obj is not None)

    with work_in_progress("Saving file"):
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(tmpdirname+"/file", "wb") as f:
                pickle.dump(random.random(), f)

    return True

# Generated at 2022-06-13 20:14:43.170757
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:45.149168
# Unit test for function work_in_progress
def test_work_in_progress():
    a = 5
    b = 6
    with work_in_progress("Add 5 + 6"):
        a += b
    assert a == 11

# Generated at 2022-06-13 20:14:53.611428
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert obj

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:15:00.678239
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    loader = work_in_progress(lambda: load_file("tests/test_file.pkl"))
    next(loader)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:15:05.966854
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(1)
        print("This is a context.")
        time.sleep(2)
    print("Outside the context.")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:15:09.211675
# Unit test for function work_in_progress
def test_work_in_progress():
    begin_time = time.time()
    with work_in_progress("Calculating the sum"):
        time.sleep(0.5)
    assert time.time() - begin_time > 0.5

# Generated at 2022-06-13 20:15:20.061745
# Unit test for function work_in_progress
def test_work_in_progress():
    h = len(f"{time.time():.2f}")
    h = max(h, len("(3.56s)"))
    with work_in_progress("Working", end="-") as w:
        time.sleep(2.12)
    with work_in_progress("Working", end="-") as w:
        time.sleep(0.45)
    print(w)

if __name__ == "__main__":
    test_work_in_progress()