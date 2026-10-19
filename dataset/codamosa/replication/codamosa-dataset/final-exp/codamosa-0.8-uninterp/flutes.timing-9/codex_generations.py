

# Generated at 2022-06-13 20:05:20.788116
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress"):
        time.sleep(2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:22.465041
# Unit test for function work_in_progress
def test_work_in_progress():
    pass


if __name__ == '__main__':
    import pytest
    pytest.main(['-v', __file__])

# Generated at 2022-06-13 20:05:25.711831
# Unit test for function work_in_progress
def test_work_in_progress():
    def _test():
        for i in range(10):
            time.sleep(0.1)
    with work_in_progress("Testing work in progress"):
        _test()

# Generated at 2022-06-13 20:05:28.330619
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:29.876224
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Just a test"):
        time.sleep(1.5)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:40.225246
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    assert work_in_progress.__doc__ is not None

    begin_time = time.time()
    with work_in_progress("Task 1"):
        time.sleep(1.23)
    assert time.time() - begin_time >= 1.2

    begin_time = time.time()
    with work_in_progress("Task 2"):
        time.sleep(2.34)
    assert time.time() - begin_time >= 2.3

    begin_time = time.time()
    with work_in_progress("Task 3"):
        time.sleep(3.45)
    assert time.time() - begin_time >= 3.4

    begin_time = time.time()
    @work_in_progress("Task 4")
    def foo():
        time.sleep(4.56)

# Generated at 2022-06-13 20:05:45.936246
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = os.path.join(tmpdir, 'test_file')
        with work_in_progress("Saving file"):
            with open(tmp_path, "wb") as f:
                pickle.dump(range(100000), f)
        with work_in_progress("Loading file"):
            with open(tmp_path, "rb") as f:
                pickle.load(f)

# test_work_in_progress()

# Generated at 2022-06-13 20:05:56.567117
# Unit test for function work_in_progress
def test_work_in_progress():
    from functools import partial
    from unittest import mock
    with mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        with work_in_progress("Loading file"):
            time.sleep(0.05)
            print("Message 1")
            time.sleep(0.1)
            print("Message 2")
        assert mock_stdout.getvalue() == "Loading file... Message 1\nMessage 2\ndone. (0.15s)\n"

# Generated at 2022-06-13 20:06:00.541190
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test Work in Progress")
    def test():
        time.sleep(1)
        print("hi")
    test()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:02.251794
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress"):
        time.sleep(0.15)

# Generated at 2022-06-13 20:06:09.963545
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for work_in_progress.
    
    Returns:
        [bool]: True if the test is passed, False otherwise.
    """
    from random import random
    from subprocess import Popen, PIPE
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp_dir:
        obj = random()
        with work_in_progress("Test work_in_progress()"):
            with open(os.path.join(tmp_dir, "test"), "wb") as fout:
                pickle.dump(obj, fout)
            time.sleep(1)
            with open(os.path.join(tmp_dir, "test"), "rb") as fin:
                assert pickle.load(fin) == obj


# Generated at 2022-06-13 20:06:12.018558
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(1)


# Generated at 2022-06-13 20:06:15.397655
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

# Generated at 2022-06-13 20:06:25.019351
# Unit test for function work_in_progress
def test_work_in_progress():

    with work_in_progress() as pbar:
        time.sleep(1)
    assert len(pbar.__repr__()) == 6

    with work_in_progress("Testing progress bar") as pbar:
        time.sleep(3)
    assert len(pbar.__repr__()) == 25

    with work_in_progress() as pbar:
        time.sleep(1)
    assert len(pbar.__repr__()) == 6

    with work_in_progress() as pbar:
        time.sleep(1)
    assert len(pbar.__repr__()) == 6

    @work_in_progress()
    def test():
        time.sleep(1)
    assert len(test.__repr__()) == 6

if __name__ == "__main__":
    test_

# Generated at 2022-06-13 20:06:32.698530
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function work_in_progress
    
    .. code:: python

        >>> @work_in_progress("Loading file")
        ... def load_file(path):
        ...     with open(path, "rb") as f:
        ...         return pickle.load(f)
        ...
        >>> with open("./test.pkl", "wb") as f:
        ...     pickle.dump([["a", 1], ["b", 2]], f)
        ...
        >>> obj = load_file("./test.pkl")
        Loading file... done. (0.00s)
        >>> print(obj)
        [['a', 1], ['b', 2]]
    """

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:38.162280
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Debugging function"):
        time.sleep(1)

    @work_in_progress("Debugging function")
    def func():
        time.sleep(1)

    func()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:41.468271
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(3.78)

# Generated at 2022-06-13 20:06:51.571505
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            return pickle.dump(obj, f)

    path = "test.pkl"

    with open(path, "wb") as f:
        pickle.dump(dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9), f)

    obj = load_file(path)

# Generated at 2022-06-13 20:07:00.958610
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test the function work_in_progress"""

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

# Generated at 2022-06-13 20:07:05.755003
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Initializing"):
        time.sleep(1)
    with work_in_progress("Loading data"):
        time.sleep(2)
    with work_in_progress("Processing data"):
        time.sleep(3)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:17.874743
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


# Run the unit test if executed
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:21.494229
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


# Unit test
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:25.809781
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    class Struct(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    obj = Struct(name="python", version="3.8.1")
    with open("test.pickle", "wb") as f:
        pickle.dump(obj, f)
    print(load_file("test.pickle"))

# Generated at 2022-06-13 20:07:32.344149
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("test_work_in_progress.pkl")
    assert isinstance(obj, list)
    assert len(obj) == 1000

    path = "test_work_in_progress_0.pkl"
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:07:34.527376
# Unit test for function work_in_progress
def test_work_in_progress():
    from src import w_in_p
    with w_in_p("Test"):
        pass

# Generated at 2022-06-13 20:07:39.540203
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert hasattr(obj, "__len__")



# Generated at 2022-06-13 20:07:44.224897
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

# Generated at 2022-06-13 20:07:51.132797
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.run_docstring_examples(work_in_progress, globals())

#------------------------------------------------------------------------------
# Copyright (C) 2020 João Pedro Rodrigues <joao.rodrigues@cern.ch>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program

# Generated at 2022-06-13 20:07:56.709244
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress()
    def slow_log():
        for i in range(int(1e8)):
            math.log(i)

    slow_log()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:02.928891
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test that the decorator is working."""
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:08:16.975236
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(1)
    print()
    with work_in_progress("Doing nothing"):
        time.sleep(1)
    print()



# Generated at 2022-06-13 20:08:20.763795
# Unit test for function work_in_progress
def test_work_in_progress():

    # Testing with a context manager
    with work_in_progress("Loading file"):
        time.sleep(1)
    # Loading file... done. (1.00s)

    time.sleep(2)

    # Testing with a deco

# Generated at 2022-06-13 20:08:26.727765
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    with work_in_progress("Saving file"):
        with open("/path/to/another/file", "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:29.000861
# Unit test for function work_in_progress
def test_work_in_progress():
    from doctest import testmod
    failures, tests = testmod(optionflags=doctest.ELLIPSIS)
    assert failures == 0

# Generated at 2022-06-13 20:08:44.606214
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    from contextlib import ExitStack

    # Tests the use of the context manager
    dummy_object = "Hello World!"
    with ExitStack() as es:
        # Set up the mock functions
        mock_open_f = es.enter_context(
            unittest.mock.patch("builtins.open",
                                unittest.mock.MagicMock(name="open_f")))
        mock_open_f.return_value = unittest.mock.MagicMock(name="file_obj")
        mock_dump_f = es.enter_context(unittest.mock.patch("pickle.dump"))
        mock_load_f = es.enter_context(unittest.mock.patch("pickle.load"))
        mock_load_f.return_value = dummy_object

# Generated at 2022-06-13 20:08:47.376117
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress.

    The test passes if the following is printed:

    >>> test_work_in_progress()
    Work in progress... done. (0.02s)

    If it prints anything else, the test fails.
    """
    with work_in_progress("Work in progress"):
        time.sleep(0.01)

# Generated at 2022-06-13 20:08:51.963262
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Saving file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Loading file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:08:53.233369
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Calling function"):
        time.slee

# Generated at 2022-06-13 20:09:00.821030
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

# Generated at 2022-06-13 20:09:10.353902
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    if "work_in_progress" not in globals():
        from .util import work_in_progress

    with work_in_progress("Testing") as w:
        time.sleep(1)
        w()
        time.sleep(1)
        w()
        time.sleep(1)
        w()

test_cases['test_work_in_progress'] = test_work_in_progress
__test__ = {
    "test_work_in_progress": test_work_in_progress,
}

if __name__ == "__main__":
    import sys
    test_case = sys.argv[1] if len(sys.argv) > 1 else None
    if test_case:
        test_cases[test_case]()

# Generated at 2022-06-13 20:09:36.932426
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Running test_work_in_progress"):
        time.sleep(0.1)
    with work_in_progress("Running test_work_in_progress"):
        time.sleep(0.1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:40.651757
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for the work_in_progress function."""
    @work_in_progress("Test function")
    def sleep():
        time.sleep(1)

    sleep()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:

# Generated at 2022-06-13 20:09:51.215765
# Unit test for function work_in_progress
def test_work_in_progress():
    print("\nTesting function work_in_progress:")

    # Test case 1
    print("\tCase 1")
    s = "This is a test for work_in_progress"
    with work_in_progress("This is a test for work_in_progress"):
        time.sleep(3.123)
    print("\t\t", s) # Work in progress... done. (3.12s)

    # Test case 2
    print("\tCase 2")
    @work_in_progress("This is a test for work_in_progress")
    def test_func():
        time.sleep(2.566)
        return "This is a test for work_in_progress"
    print(test_func()) # This is a test for work_in_progress

# Generated at 2022-06-13 20:09:56.855955
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1.22)
    def f():
        time.sleep(2.34)
    f = work_in_progress("Testing work_in_progress 2")(f)
    f()

# Generated at 2022-06-13 20:10:06.809373
# Unit test for function work_in_progress
def test_work_in_progress():
    import unittest
    import random
    import math

    def random_sleep(min_sleep, max_sleep):
        delta = max_sleep - min_sleep
        sleep_time = min_sleep + (delta * random.random())
        time.sleep(sleep_time)

    class Test(unittest.TestCase):
        def test_function(self):
            @work_in_progress("Sleeping")
            def sleep():
                random_sleep(0.5, 1.5)

            sleep()

        def test_context_manager(self):
            with work_in_progress("Sleeping"):
                random_sleep(0.5, 1.5)

    unittest.main(argv=[''], verbosity=2, exit=False)


# Generated at 2022-06-13 20:10:07.395136
# Unit test for function work_in_progress
def test_work_in_progress():
    assert True

# Generated at 2022-06-13 20:10:08.898970
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test function"):
        time.sleep(1)
    assert True

# Generated at 2022-06-13 20:10:12.317804
# Unit test for function work_in_progress
def test_work_in_progress():

    for i in range(1, 5):
        with work_in_progress(f"Looping for {i} times"):
            for j in range(1, i * 1000):
                pass

    assert 1 == 1


# Generated at 2022-06-13 20:10:16.962955
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file():
        with open("tests/fixtures/test_work_in_progress_text.txt", "r") as f:
            return f.read()

    assert work_in_progress_text == load_file()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:22.727269
# Unit test for function work_in_progress
def test_work_in_progress():
    def dummy_func():
        time.sleep(0.4)

    with work_in_progress():
        for i in range(3):
            dummy_func()

    @work_in_progress("Inner Work in Progress")
    def nested_work_in_progress():
        for i in range(3):
            dummy_func()

    nested_work_in_progress()



# Generated at 2022-06-13 20:11:12.420402
# Unit test for function work_in_progress
def test_work_in_progress():
    begin_time = time.time()
    with work_in_progress("Loading file"):
        time.sleep(0.1)
    assert time.time()-begin_time >= 0.1
    print()
    with work_in_progress("Saving file"):
        time.sleep(0.2)
    assert time.time()-begin_time >= 0.2

# Generated at 2022-06-13 20:11:16.348130
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress") as w:
        time.sleep(3)
    
    @work_in_progress("Testing work_in_progress")
    def func():
        time.sleep(3)
    
    func()


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:19.978999
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Sleep 2 secs"):
        time.sleep(2)
    # Sleep 2 secs... done. (2.01s)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # test_work_in_progress()

# Generated at 2022-06-13 20:11:30.113186
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    import tempfile

    # Generate a random filename
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    temp_file_name = temp_file.name

    # Define an object to save/load
    obj = [i for i in range(100000)]

    # Save the object
    with work_in_progress("Saving file"):
        with open(temp_file_name, 'wb') as f:
            pickle.dump(obj, f)

    # Load the object
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)


# Generated at 2022-06-13 20:11:31.876909
# Unit test for function work_in_progress
def test_work_in_progress():
    diff = 10
    @work_in_progress("Count up")
    def count_up(to_what):
        time.sleep(diff)
    count_up(100)

# Generated at 2022-06-13 20:11:36.098520
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:43.232459
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    # Loading file... done. (3.52s)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    # Saving file... done. (3.78s)

# Generated at 2022-06-13 20:11:46.540313
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress
    def load_file():
        time.sleep(0.5)

    load_file()

# test_work_in_progress()

# Generated at 2022-06-13 20:11:48.048643
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    # -------------------------
    def slow_func(n=3):
        time.sleep(n)

    with work_in_progress("Test slow function"):
        slow_func(3)
    # -------------------------

# Generated at 2022-06-13 20:11:52.111509
# Unit test for function work_in_progress
def test_work_in_progress():
    import threading

    def print_work_in_progress():
        with work_in_progress("Test"):
            time.sleep(1)

    thread = threading.Thread(target=print_work_in_progress)
    thread.start()
    thread.join()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:31.644521
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle

    @work_in_progress("Testing work_in_progress()'s decorator")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Testing work_in_progress()'s context manager")
    def save_file(path):
        with open(path, "wb") as f:
            pickle.dump({"a": 1, "b": "hello"}, f)

    path = os.path.join(os.getcwd(), "test.pickle")
    if os.path.isfile(path):
        with open(path, "rb") as f:
            data = pickle.load(f)
            assert data == {"a": 1, "b": "hello"}


# Generated at 2022-06-13 20:13:39.623522
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        with work_in_progress(desc="Saving file"):
            path = os.path.join(tmp_dir, "file")
            with open(path, "w") as f:
                f.write("Hello World")

        with work_in_progress(desc="Loading file"):
            with open(path, "r") as f:
                print(f.read())


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:45.116565
# Unit test for function work_in_progress
def test_work_in_progress():
    @wip("Loading file")
    def load_file(path):
        time.sleep(1)
        with open(path, "rb") as f:
            time.sleep(2)
            return pickle.load(f)

    obj = load_file("test_wip.p")

    with wip("Saving file"):
        time.sleep(2)
        with open(path, "wb") as f:
            time.sleep(1)
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:13:47.024722
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress") as _:
        time.sleep(1)


# Generated at 2022-06-13 20:13:49.095608
# Unit test for function work_in_progress
def test_work_in_progress():
    def foo(n: int, sleep: float = 0.01):
        with work_in_progress("Loading file"):
            time.sleep(sleep)

    foo(0, 0.01)

# Generated at 2022-06-13 20:13:57.733629
# Unit test for function work_in_progress
def test_work_in_progress():
    output = StringIO()
    with contextlib.redirect_stdout(output):
        with work_in_progress("Loading file"):
            time.sleep(1)
        with work_in_progress("Saving file"):
            time.sleep(1)
        time.sleep(1)
    output = output.getvalue().strip().split("\n")

    assert len(output) == 2
    assert output[0].endswith("Loading file... done. (1.00s)")
    assert output[1].endswith("Saving file... done. (1.00s)")

# Generated at 2022-06-13 20:14:03.730815
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress"""
    import time

    # Unit test context manager
    @work_in_progress("Test context manager")
    def test():
        time.sleep(2)

    test()

    # Unit test decorator
    @work_in_progress("Test decorator")
    def test_decorator():
        time.sleep(1)

    test_decorator()

# Generated at 2022-06-13 20:14:05.657204
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sleeping for 1 second")
    def test_function():
        time.sleep(1)

    test_function()

# Generated at 2022-06-13 20:14:15.057184
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

    file_path = "/tmp/test_work_in_progress"
    with open(file_path, "wb") as f:
        pickle.dump({
            'a': 1,
            'b': 2,
            'c': 3,
        }, f)

    obj = load_file(file_path)
    save_file(file_path, obj)

    with open(file_path, "rb") as f:
        assert pick

# Generated at 2022-06-13 20:14:19.519358
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def _test_work_in_progress():
        time.sleep(2)

    _test_work_in_progress()

if __name__ == "__main__":
    test_work_in_progress()