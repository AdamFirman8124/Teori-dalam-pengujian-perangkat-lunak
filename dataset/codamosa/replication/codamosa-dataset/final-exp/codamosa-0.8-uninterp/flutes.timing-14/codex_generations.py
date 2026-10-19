

# Generated at 2022-06-13 20:05:20.501334
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Testing function work_in_progress...", end='', flush=True)
    with work_in_progress("Testing function work_in_progress"):
        pass
    print(" done.")

# Update module docstring with current __all__
__update_all__(__name__)

# Unit test
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:25.512210
# Unit test for function work_in_progress
def test_work_in_progress():
    # Note: not unit testing. Just a demonstration how to use.
    @work_in_progress()
    def func1():
        time.sleep(0.1)
    func1()

    with work_in_progress():
        time.sleep(0.1)

# Generated at 2022-06-13 20:05:33.900275
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    path = "test_file.pickle"

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = {
        "hello": "world"
    }
    with open(path, "wb") as f:
        pickle.dump(obj, f)
    obj_loaded = load_file(path)
    assert obj == obj_loaded

    time.sleep(0.2)
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    os.remove(path)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:36.261953
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(2)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:05:42.814491
# Unit test for function work_in_progress
def test_work_in_progress():
    from time import sleep

    with work_in_progress("Testing function"):
        sleep(1)

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress
    def load_file2(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    obj = load_file2("/path/to/some/file")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:53.976876
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import tempfile
    import random

    data = {
        "data": [random.randint(0, 100) for _ in range(1000)],
        "pi": 3.1415,
        "answer": 42,
    }

    def dump_data(path, data=data):
        with work_in_progress(f"Saving data to {path}"):
            with open(path, "wb") as f:
                pickle.dump(data, f)

    def load_data(path):
        with work_in_progress(f"Loading data from {path}"):
            with open(path, "rb") as f:
                return pickle.load(f)

    with tempfile.TemporaryDirectory() as tempdir:
        path = tempdir + "/data.pickle"
        dump_data

# Generated at 2022-06-13 20:05:57.079570
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    with work_in_progress():
        time.sleep(random.uniform(3, 4))
    time.sleep(random.uniform(1, 2))

# Generated at 2022-06-13 20:06:01.198240
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test function `work_in_progress`.
    """
    @work_in_progress("Loading file")
    def load_file():
        time.sleep(0.1)

    load_file()

    with work_in_progress("Saving file"):
        time.sleep(0.1)

# Generated at 2022-06-13 20:06:07.050747
# Unit test for function work_in_progress
def test_work_in_progress():
    from doctest import testmod
    _, total_failed, _ = testmod()
    if total_failed == 0:
        print("All tests passed.")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:13.511269
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import time
    import pickle
    # mock function
    def mock_function(data):
        picked_data = pickle.dumps(data)
        time.sleep(random.random())
        return pickle.loads(picked_data)
    # mock data
    data = list(range(10))
    # run the test
    with work_in_progress("Mocking function"):
        result = mock_function(data)
    assert data == result

# Generated at 2022-06-13 20:06:19.875812
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress"):
        time.sleep(1.23)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:23.550591
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    # Test as a function decorator
    @work_in_progress("Function decorator test")
    def testing():
        time.sleep(1)

    testing()

    # Test as a with statement
    with work_in_progress("With statement test"):
        time.sleep(1)

# Generated at 2022-06-13 20:06:28.477152
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Task")
    def task(time_sleep=0.5):
        time.sleep(time_sleep)

    task()
    task(1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:34.303752
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress('Loading file'):
        time.sleep(2)
    time.sleep(1)
    with work_in_progress('Saving file'):
        time.sleep(3)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:44.821616
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Testing function work_in_progress...")
    print("execute with a context manager...")
    with work_in_progress("Test work in progress"):
        time.sleep(1.23456789)
    print("execute as a decorator...")
    @work_in_progress("Test work in progress")
    def func():
        time.sleep(2.345678901)
    func()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:49.356339
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:06:59.566592
# Unit test for function work_in_progress
def test_work_in_progress():
    for i in range(1000):
        x = 5
    with work_in_progress("without file i/o"):
        for i in range(1000):
            x = 5
    with work_in_progress("with file i/o"):
        with open("test.txt", "w") as f:
            print("This is a test", file=f)
        with open("test.txt", "r") as f:
            _ = f.read()
        os.remove("test.txt")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:03.629596
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress
    def test_function(a):
        time.sleep(a)

    test_function(0.01)
    test_function(0.1)
    test_function(1)

    with work_in_progress():
        time.sleep(3)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:09.648211
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def func():
        time.sleep(1)
        print("Doing something...")
        time.sleep(1)
    func()

    class ContextManager:
        def __enter__(self):
            self.begin_time = time.time()
        def __exit__(self, exc_type, exc_value, exc_tb):
            print(time.time() - self.begin_time)
    with work_in_progress("Test 2"), ContextManager():
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:17.628690
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
    save_file("/path/to/another/file", obj)

    with work_in_progress("Another saving file"):
        save_file("/path/to/another/file", obj)

# Generated at 2022-06-13 20:07:31.334050
# Unit test for function work_in_progress
def test_work_in_progress():
    print("=" * 20)
    print("Testing function work_in_progress:")
    print("=" * 20)

    def run_work_in_progress(is_in_progress):
        with work_in_progress("Test 1"):
            time.sleep(1)
        if is_in_progress:
            print("Test 2...")
            with work_in_progress("Test 2"):
                time.sleep(1)
            print("Test 2... done.")
        else:
            work_in_progress("Test 3")(time.sleep)(1)

    run_work_in_progress(True)
    print()
    run_work_in_progress(False)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:41.569668
# Unit test for function work_in_progress
def test_work_in_progress():
    """Check if the execution is delayed by the specified time."""

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    patcher = patch("time.time")
    mock_time = patcher.start()
    begin_time = mock_time()

    with work_in_progress("Loading file"):
        time.sleep(1)

    mock_time.assert_called_with()
    assert mock_time() - begin_time == 1

    patcher.stop()

    with work_in_progress("Loading file"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:45.563248
# Unit test for function work_in_progress
def test_work_in_progress():
    work_in_progress("Task 1")
    with work_in_progress("Task 2"):
        with work_in_progress("Task 3"):
            time.sleep(3.2)
        time.sleep(1.0)
    time.sleep(2.9)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:59.066363
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile
    import numpy as np
    import pickle

    a = np.random.randn(10000, 10000)

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "temporary_object.pkl")
        save_file(a, path)
        with work_in_progress("Loading file"):
            obj = load_file(path)
        assert np.all(a == obj)


# Generated at 2022-06-13 20:08:00.857841
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(0.01)

# Generated at 2022-06-13 20:08:05.466191
# Unit test for function work_in_progress
def test_work_in_progress():
    """
    Unit test for function work_in_progress.
    """
    import doctest
    mode = doctest.ELLIPSIS
    doctest.testmod(optionflags=mode)
    mode |= doctest.REPORT_NDIFF
    doctest.testmod(optionflags=mode)

# Generated at 2022-06-13 20:08:12.511538
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile
    import pickle

    with tempfile.TemporaryDirectory() as tmp_dir:
        path = os.path.join(tmp_dir, "test_file.pkl")

        # Check pickle load with context
        obj = {"key": "value"}
        with open(path, "wb") as f:
            pickle.dump(obj, f)

        with work_in_progress("Loading file"):
            with open(path, "rb") as f:
                loaded_obj = pickle.load(f)
        assert loaded_obj == obj

        # Check pickle save with context
        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)
        with open(path, "rb") as f:
            loaded

# Generated at 2022-06-13 20:08:15.680645
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:18.247524
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Doing something"):
        time.sleep(0.5)

if __name__ == '__main__':
    import nose
    nose.runmodule()

# Generated at 2022-06-13 20:08:27.345955
# Unit test for function work_in_progress
def test_work_in_progress():
    import os

    with work_in_progress():
        pass
    with work_in_progress("This is a test"):
        pass

    @work_in_progress("Loading file")
    def load_file(fname):
        with open(fname, "rb") as f:
            return f.read()

    with work_in_progress("Creating file"):
        with open("/tmp/test.file", "w") as f:
            f.write("a" * (1<<20))

    for i in range(3):
        load_file("/tmp/test.file")

    os.unlink("/tmp/test.file")



# Generated at 2022-06-13 20:08:44.072324
# Unit test for function work_in_progress
def test_work_in_progress():
    import unittest

    class TestWorkInProgress(unittest.TestCase):
        def test_work_in_progress_normal(self):
            begin_time = time.time()
            with work_in_progress(desc="Normal work"):
                time.sleep(0.2)
                self.assertGreaterEqual(time.time(), begin_time)
        def test_work_in_progress_exception(self):
            with self.assertRaises(ZeroDivisionError):
                with work_in_progress(desc="Exception work"):
                    1/0

    unittest.main()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:53.223192
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Processing file")
    def process_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    import tempfile
    path = tempfile.mkstemp()[1]

# Generated at 2022-06-13 20:09:00.773055
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

# Generated at 2022-06-13 20:09:08.913832
# Unit test for function work_in_progress
def test_work_in_progress():

    # Use the function as a decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    mock_path = "/path/to/some/file"
    mock_object = object()
    with mock.patch("builtins.open", mock.mock_open(read_data=mock_object)):
        with mock.patch("time.time", mock.Mock(side_effect=[1, 5])):
            result = load_file(mock_path)

    assert result == mock_object

    # Use the function as a context

# Generated at 2022-06-13 20:09:12.044842
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sleeping for 3 seconds")
    def foo():
        time.sleep(3)

    foo()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:24.247817
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Time the execution time of a code block or function.

    .. code:: python

        >>> @work_in_progress("Loading file")
        ... def load_file(path):
        ...     with open(path, "rb") as f:
        ...         return pickle.load(f)
        ...
        ... obj = load_file("/path/to/some/file")
        Loading file... done. (3.52s)

        >>> with work_in_progress("Saving file"):
        ...     with open(path, "wb") as f:
        ...         pickle.dump(obj, f)
        Saving file... done. (3.78s)

    :param desc: Description of the task performed.
    """
    print(desc + "... ", end='', flush=True)
    begin_time = time.time

# Generated at 2022-06-13 20:09:31.773891
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import pickle
    import numpy as np
    import scipy.signal
    import os

    def simulate_task(idx):
        """A random Numpy computation"""
        y = np.random.randn(1e8)
        y = scipy.signal.hann(10_000)
        y = y + np.random.randn(10_000)
        y = scipy.signal.filtfilt(*scipy.signal.butter(16, 0.12), y)
        y = np.random.randn(1e2, 3)
        y = y.sum(axis=0)
        return idx, y


# Generated at 2022-06-13 20:09:33.350919
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    @work_in_progress("Test work_in_progress")
    def fn(s):
        time.sleep(s)
    fn(1)

# Generated at 2022-06-13 20:09:36.016306
# Unit test for function work_in_progress
def test_work_in_progress():
    def my_function(num: int):
        with work_in_progress("Testing"):
            for _ in range(num):
                time.sleep(0.01)

    my_function(10)

# Generated at 2022-06-13 20:09:43.084563
# Unit test for function work_in_progress
def test_work_in_progress():
    def func(a, b, c=1):
        CURRENT_MODULE.test_var = locals()
        time.sleep(1)
        return a + b + c
    with work_in_progress():
        assert func(1, 2, 3) == 6
        assert CURRENT_MODULE.test_var == {
           'a': 1,
           'b': 2,
           'c': 3,
        }

# TODO: Use logging module to log the task information
# import logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(
#    level=logging.DEBUG,
#    format='(%(threadName)-10s) %(message)s',
# )
# logger.info()

# Generated at 2022-06-13 20:09:49.631778
# Unit test for function work_in_progress
def test_work_in_progress():
    def time_consuming_function(n):
        time.sleep(10 + n)
    for _ in range(2):
        print("-"*20)
        for n in range(4):
            with work_in_progress(f"Task {n}"):
                time_consuming_function(n)

# Generated at 2022-06-13 20:09:56.245025
# Unit test for function work_in_progress
def test_work_in_progress():
    from pytest import raises
    import os

    # Create a dummy file to test with
    path = "/tmp/file.pkl"
    with open(path, "wb") as f:
        f.write(os.urandom(654321))  # Write ~650 kB of random data

    # Test basic functionality
    with work_in_progress("Loading file"):
        with open(path, "rb") as f:
            f.read()

    # Test as a decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            f.read()

    load_file(path)

    # Test as a generator

# Generated at 2022-06-13 20:10:05.615426
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test function
    @work_in_progress("Function decorator")
    def foo_function(delay=1, print_msg='foo'):
        time.sleep(delay)
        print(print_msg)

    # Test context manager
    @contextlib.contextmanager
    def foo_context_manager(delay=1, print_msg='foo'):
        time.sleep(delay)
        print(print_msg)
        yield

    with work_in_progress("Context manager"):
        foo_function(0.5)
        foo_context_manager(0.2)

    foo_function(1, "bar")


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:13.187534
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = temp_dir + '/work_in_progress.pickle'

        # Test function
        @work_in_progress()
        def load_work_in_progress(file_path):
            with open(file_path, 'rb') as f:
                return pickle.load(f)

        # Test context manager
        with work_in_progress('Dump'):
            with open(file_path, 'wb') as f:
                pickle.dump({'test': True}, f)

        obj = load_work_in_progress(file_path)
        assert obj['test']


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:20.329867
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
    save_file("/path/to/some/file", obj)

# Generated at 2022-06-13 20:10:24.761400
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading files")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving files"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:10:30.255287
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import os
    import numpy as np

    def load_file(path):
        """Load a file."""
        with work_in_progress("Loading file"):
            with open(path, "rb") as f:
                return pickle.load(f)

    def save_file(path):
        """Save a file."""
        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(np.random.random((100, 100)), f)

    if os.path.exists("a_file.pickle"):
        os.remove("a_file.pickle")

    save_file("a_file.pickle")
    load_file("a_file.pickle")

# Generated at 2022-06-13 20:10:35.654738
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # Test the contextmanager.
    obj = load_file(__file__)
    assert obj

    # Test the function.

# Generated at 2022-06-13 20:10:40.418260
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3.52)
    with work_in_progress("Saving file"):
        time.sleep(3.78)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    test_work_in_progress()

# Generated at 2022-06-13 20:10:50.834972
# Unit test for function work_in_progress
def test_work_in_progress():
    from os import makedirs
    from os.path import join, exists
    from shutil import rmtree
    from tempfile import TemporaryDirectory

    # Generate two fake files
    with TemporaryDirectory() as tmpdir:
        file1 = join(tmpdir, "file1")
        with open(file1, "w") as f:
            f.write("This is file 1")

        file2 = join(tmpdir, "file2")
        with open(file2, "w") as f:
            f.write("This is file 2")

        # Make a new directory and copy the files there
        dest = join(tmpdir, "dest")
        src = join(tmpdir, "src")
        makedirs(src)


# Generated at 2022-06-13 20:11:03.390926
# Unit test for function work_in_progress
def test_work_in_progress():
    from pathlib import Path
    import pickle
    import numpy as np

    n = 1000000
    a = np.random.rand(n, n)
    path = Path("a.pkl")

    with work_in_progress("Generating random matrix"):
        a = np.random.rand(n, n)

    if path.is_file():
        with work_in_progress("Loading the matrix"):
            with open(path, "rb") as f:
                a = pickle.load(f)

    else:
        with work_in_progress("Saving the matrix"):
            with open(path, "wb") as f:
                pickle.dump(a, f)

    with work_in_progress("Matrix multiplication"):
        b = a @ a


# Generated at 2022-06-13 20:11:08.788136
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


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:13.688885
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle

    # Test with @work_in_progress
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("/path/to/some/file")

    # Test with work_in_progress()
    with work_in_progress("Saving file"):
        with open("test.dat", "wb") as f:
            pickle.dump(obj, f)
    os.remove("test.dat")


# -----------------------------------------------------------------------------

# Generated at 2022-06-13 20:11:16.167087
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Work in progress"):
        time.sleep(1.5)

# if __name__ == "__main__":
#     test_work_in_progress()

# Generated at 2022-06-13 20:11:19.253529
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(2)
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("/path/to/some/file")


# Generated at 2022-06-13 20:11:21.881253
# Unit test for function work_in_progress
def test_work_in_progress():
    obj = [0] * 1000
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(3)

# Generated at 2022-06-13 20:11:25.195548
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Some work")
    def some_work():
        for i in range(1000000):
            pass

    with work_in_progress("Progress"):
        time.sleep(1.5)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:27.296583
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing the timer"):
        time.sleep(0.3)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:32.683599
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
    save_file("/path/to/save/file", obj)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:37.964279
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Some dummy work"):
        time.sleep(1)
    with work_in_progress("Another dummy work"):
        time.sleep(0.1)
    with work_in_progress():
        time.sleep(0.2)

if __name__ == '__main__':
    #log = logging.getLogger(__name__)
    #log.setLevel(logging.DEBUG)
    #log_handler = logging.StreamHandler()
    #log_handler.setFormatter(logging.Formatter('[%(name)s][%(levelname)s] %(message)s'))
    #log.addHandler(log_handler)
    test_work_in_progress()

# Generated at 2022-06-13 20:11:52.450808
# Unit test for function work_in_progress
def test_work_in_progress():
    for attr in __all__:
        if attr.startswith("test_") or attr.startswith("_"):
            continue
        func = getattr(sys.modules[__name__], attr)
        if callable(func):
            setattr(sys.modules[__name__], f"test_{attr}", func)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:12:02.002324
# Unit test for function work_in_progress
def test_work_in_progress():
    with pytest.raises(ValueError):
        exit_status = subprocess.call([
            "python", "-c",
            "import sys, picksup; "
            "sys.exit(picksup.work_in_progress(1))"
        ])
        assert exit_status == 1
    with pytest.raises(ValueError):
        exit_status = subprocess.call([
            "python", "-c",
            "import sys, picksup; "
            "with picksup.work_in_progress(): sys.exit(1)"
        ])
        assert exit_status == 1

# Generated at 2022-06-13 20:12:05.270253
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file") as _:
        time.sleep(1)
    with work_in_progress("Saving file") as _:
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:06.250079
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing"):
        time.sleep(3.21)

# Generated at 2022-06-13 20:12:10.903968
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle

    # 1. Define a function
    # 1. Define a function
    @work_in_progress("Save a random array")
    def save_array(path: str):
        arr = np.random.random_integers(0, 10, (1024, 1024, 1024))
        # save the array
        with open(path, "wb") as f:
            pickle.dump(arr, f)

    # 2. Save to a file
    save_array("test1.bin")

    # 3. Verify the time consumption
    time.sleep(0.1)
    assert os.stat("test1.bin").st_mtime > time.time() - 0.2
    assert os.stat("test1.bin").st_mtime < time.time()

# Generated at 2022-06-13 20:12:15.395603
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Computing the factorial")
    def factorial(n):
        return math.factorial(n)
    f = factorial(100)
    assert f == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

# Generated at 2022-06-13 20:12:23.798254
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress():
        time.sleep(1)
    print()
    with work_in_progress("Loading file"):
        time.sleep(1)
        with work_in_progress("Loading file"):
            time.sleep(1)
    print()
    with work_in_progress():
        time.sleep(1)
        with work_in_progress():
            time.sleep(1)
    print()
    with work_in_progress("Loading file") as w:
        w.update_description("Loading file system")
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:25.225649
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Run unit test"):
        time.sleep(1)

# Generated at 2022-06-13 20:12:26.490721
# Unit test for function work_in_progress
def test_work_in_progress():

    with work_in_progress():
        time.sleep(1)


# Generated at 2022-06-13 20:12:30.267198
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)

    with work_in_progress("Saving file"):
        time.sleep(1)

# vim: ts=4 sw=4 sts=4 expandtab

# Generated at 2022-06-13 20:12:56.927531
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

    obj = load_file("/path/to/some/file")
    save_file(obj, "/path/to/some/file")

# Generated at 2022-06-13 20:13:01.288769
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(2)

    @work_in_progress("Loading file")
    def load_file():
        time.sleep(2)

    load_file()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:08.366765
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/home/gqf/code/geopandas/geopandas/geoseries.py")

    print()

    with work_in_progress("Saving file"):
        with open("test.pickle", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:18.782832
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
    obj = load_file("/path/to/some/file")
    assert isinstance(obj, dict)
    
    path = "/path/to/another/file"
    with work_in_progress("Creating file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    with open(path, "rb") as f:
        data = pickle.load(f)
    assert data == obj
    os.remove(path)

# Run unit tests.
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:27.977179
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Tests the function work_in_progress.
    """
    # Warm up
    import time
    for _ in range(100):
        time.sleep(0.01)
    time.time()

    import io, random
    import struct
    import pickle

    def _pickle_int(o: int):
        return struct.pack("<i", o)

    def _pickle_float(o: float):
        return struct.pack("<d", o)

    with work_in_progress():
        for _ in range(1000):
            for i in range(100):
                pickle.loads(_pickle_int(random.randint(-1000000, 1000000)))
                pickle.loads(_pickle_float(random.random() * 2 - 1))


# Generated at 2022-06-13 20:13:29.747762
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function :func:`work_in_progress`."""
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1.0)

# Generated at 2022-06-13 20:13:31.958744
# Unit test for function work_in_progress
def test_work_in_progress():
    def func():
        time.sleep(0.1)

    with work_in_progress():
        func()
# /Unit test for function work_in_progress

# Generated at 2022-06-13 20:13:42.455384
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for :func:`pymkcmd.utils.work_in_progress`."""
    begin_time = time.time()

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(os.path.expanduser("~/Downloads/PIL-1.1.7.tar.gz"))
    time_consumed = time.time() - begin_time

    assert time_consumed >= 3.0
    assert obj.__doc__ == "Pillow (PIL Fork) Documentation, Release 1.1.7"

    begin_time = time.time()


# Generated at 2022-06-13 20:13:48.149383
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
        # If you return `return pickle.load(f)` without the with block,
        # the file will be closed before any data is read from it,
        # which will result in the following error:
        # FileNotFoundError: [Errno 2] No such file or directory: '...'

    load_file("anything")

# Generated at 2022-06-13 20:13:49.573192
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("test"):
        time.sleep(1)

# Generated at 2022-06-13 20:14:30.719541
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def test_fct():
        time.sleep(0.5)
    test_fct()

# Generated at 2022-06-13 20:14:33.854585
# Unit test for function work_in_progress
def test_work_in_progress():
    sleep = lambda t: _work_in_progress_sleep(t, 100)
    with work_in_progress():
        sleep(1)
    with work_in_progress("Computing"):
        sleep(0.8)
    with work_in_progress("Computing"):
        sleep(0.115)

# Auxiliary function: Sleep for t seconds then print a progress bar

# Generated at 2022-06-13 20:14:40.290598
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

# Generated at 2022-06-13 20:14:47.754995
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    n = 1000000
    list_of_random_numbers = [random.random() for _ in range(n)]
    assert len(list_of_random_numbers) == n
    with work_in_progress("Generating random numbers"):
        list_of_random_numbers2 = [random.random() for _ in range(n)]
        assert len(list_of_random_numbers2) == n
    for elem1, elem2 in zip(list_of_random_numbers, list_of_random_numbers2):
        assert isinstance(elem1, float)
        assert isinstance(elem2, float)
        assert elem1 != elem2

# Generated at 2022-06-13 20:14:53.351148
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    path = "/tmp/test.pkl"
    with open(path, "wb") as f:
        pickle.dump(range(1024), f)

    assert load_file(path) == list(range(1024))

# Generated at 2022-06-13 20:14:59.482692
# Unit test for function work_in_progress
def test_work_in_progress():
    def slow_sum(n: int) -> int:
        time.sleep(1)
        return n + n
    with work_in_progress("Summing numbers") as f:
        f(slow_sum)
    assert True

# Generated at 2022-06-13 20:15:04.142560
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

# Generated at 2022-06-13 20:15:04.734365
# Unit test for function work_in_progress
def test_work_in_progress():
    pass  # TODO

# Generated at 2022-06-13 20:15:08.982378
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(.5)
    with work_in_progress("Saving file"):
        time.sleep(.5)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:15:18.797266
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.1)
    with work_in_progress("Updating file"):
        time.sleep(0.2)
    with work_in_progress("Saving file"):
        time.sleep(0.3)
    print("Done!")

if __name__ == "__main__":
    test_work_in_progress()