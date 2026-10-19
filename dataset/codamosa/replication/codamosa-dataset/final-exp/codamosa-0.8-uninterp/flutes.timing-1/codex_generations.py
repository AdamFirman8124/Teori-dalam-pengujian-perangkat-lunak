

# Generated at 2022-06-13 20:05:26.180123
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    import pickle
    import tempfile

    import pytest


    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, data):
        with open(path, "wb") as f:
            pickle.dump(data, f)

    with tempfile.NamedTemporaryFile() as f:
        data = {
            "test": 1,
            "data": [1, 2, 3, 4],
        }
        save_file(f.name, data)

        # Make sure output is buffered
        with pytest.raises(IOError):
            f.flush()

        # Load data

# Generated at 2022-06-13 20:05:28.778996
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.run_docstring_examples(work_in_progress, globals(), verbose=True)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:37.649378
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)
    try:
        with work_in_progress("Saving file"):
            with open(__file__, "wb") as f:
                pickle.dump(obj, f)
    finally:
        pass

#############################################################################
#                                Unit Test
#############################################################################

if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-13 20:05:39.616399
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Start counting"):
        time.sleep(1.234)
    # 'Start counting... done. (1.23s)'


# Generated at 2022-06-13 20:05:41.812608
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(1)
    with work_in_progress("Test"):
        time.sleep(1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:47.298042
# Unit test for function work_in_progress
def test_work_in_progress():
    print(f"Testing function '{__name__}.work_in_progress'")

    import os
    import pickle
    import tempfile
    import uuid
    import warnings

    # Prepare a dummy object for testing

# Generated at 2022-06-13 20:05:52.334390
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def test():
        time.sleep(0.1)

    test()
    assert True

# Generated at 2022-06-13 20:05:54.340016
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Dummy function"):
        time.sleep(1)

# Generated at 2022-06-13 20:05:56.495037
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(2.0)
    with work_in_progress("Saving file"):
        time.sleep(2.0)
    time.sleep(2.0)
    print("Finished.")

# Generated at 2022-06-13 20:06:05.647221
# Unit test for function work_in_progress
def test_work_in_progress():
    import pandas as pd
    import random
    import tempfile

    with work_in_progress("Creating dataframe"):
        df = pd.DataFrame(data={
            "A": [random.gauss(0, 1) for _ in range(1000000)],
            "B": [random.gauss(0, 1) for _ in range(1000000)],
            "C": [random.gauss(0, 1) for _ in range(1000000)],
            "D": [random.gauss(0, 1) for _ in range(1000000)],
        })
    with work_in_progress("Saving to temporary dataframe"):
        filepath = df.to_csv(index=False)

# Run unit tests for function work_in_progress

# Generated at 2022-06-13 20:06:10.379028
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def test():
        time.sleep(3)
    test()

# Generated at 2022-06-13 20:06:14.313585
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test function")
    def func():
        time.sleep(1)
    func()

    with work_in_progress("Test context"):
        time.sleep(1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:21.897896
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

# Generated at 2022-06-13 20:06:24.016808
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test function work_in_progress
    """
    def f():
        print("I am working.")

    with work_in_progress("Testing work_in_progress"):
        f()

# Generated at 2022-06-13 20:06:32.508989
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(file_name):
        time.sleep(0.1)
        with open(file_name, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(file_name, obj):
        time.sleep(0.1)
        with open(file_name, "wb") as f:
            pickle.dump(obj, f)

    obj = load_file("test_work_in_progress.pkl")
    assert obj["test"] == "test_work_in_progress OK."
    save_file("test_work_in_progress.pkl", obj)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:43.959776
# Unit test for function work_in_progress
def test_work_in_progress():
    # TODO: Use pytest
    import pickle
    import tempfile

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = os.path.join(temp_dir, "test.pickle")
        with work_in_progress("Saving file"):
            with open(temp_path, "wb") as f:
                pickle.dump([1, 2, 3], f)

        assert load_file(temp_path) == [1, 2, 3]

# Generated at 2022-06-13 20:06:46.251999
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(3)

    load_file("/path/to/some/file")

# Generated at 2022-06-13 20:06:53.152572
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import pickle
    path = "/tmp/time_this.pickle"

    travel_time = 3.5

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path):
        time.sleep(travel_time)
        with open(path, "wb") as f:
            pickle.dump([1, 2, 3], f)

    @work_in_progress("Deleting file")
    def delete_file(path):
        import os
        os.remove(path)

    save_file(path)

    assert load_file(path) == [1, 2, 3]

    delete_

# Generated at 2022-06-13 20:06:56.241474
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Work in progress"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:59.073669
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress") as display_time:
        time.sleep(0.1)

    assert "Test work_in_progress" in display_time.getvalue()
    assert "0.10" in display_time.getvalue()

# Generated at 2022-06-13 20:07:12.215706
# Unit test for function work_in_progress

# Generated at 2022-06-13 20:07:18.418070
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

# Generated at 2022-06-13 20:07:29.823991
# Unit test for function work_in_progress
def test_work_in_progress():
    """
    Test for the function work_in_progress.

    """
    path = "/media/alex/Data/dissertation/code/thesis_alex/data/tweets/tweets-001.pkl"

    # Test case 1
    with work_in_progress("Loading file"):
        with open(path, "rb") as f:
            pickle.load(f)

    # Test case 2
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # Test case 3
    obj = load_file(path)

# Generated at 2022-06-13 20:07:31.411068
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Hello"):
        time.sleep(0.1)

# Generated at 2022-06-13 20:07:36.454939
# Unit test for function work_in_progress
def test_work_in_progress():
    # Case 1: Test the context manager
    with work_in_progress("Test"):
        time.sleep(1)
    # Case 2: Test the decorator
    @work_in_progress
    def test_func():
        time.sleep(1)
    test_func()

# Generated at 2022-06-13 20:07:45.845027
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys
    import io
    import pickle

    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        with work_in_progress("Loading file"):
            obj = pickle.load(open("example.pkl", "rb"))
        assert buf.getvalue() == "Loading file... done. (0.00s)\n"

    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        with work_in_progress("Saving file"):
            pickle.dump(obj, open("example.pkl", "wb"))
        assert buf.getvalue() == "Saving file... done. (0.01s)\n"
    
    try:
        os.remove("example.pkl")
    except FileNotFoundError:
        pass


# Generated at 2022-06-13 20:07:56.536635
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    import sys
    from contextlib import redirect_stdout

    with io.StringIO() as buf, redirect_stdout(buf):

        @work_in_progress("Work in progress")
        def foo():
            time.sleep(0.015)

        @work_in_progress("Work in progress")
        def bar():
            time.sleep(0.015)
            sys.stdout.write("\rContinue!                                          \n")

        foo()
        bar()

    assert buf.getvalue() == "Work in progress... done. (0.02s)\nWork in progress... Continue!\n"

# Generated at 2022-06-13 20:08:03.867965
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test with a function
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    # Test with a ``with`` block
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:18.412066
# Unit test for function work_in_progress
def test_work_in_progress():
    print("test_work_in_progress: Start")


    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "r") as f:
            return f.read()

    obj = load_file("/home/thiery/code/python/deep_learning/deep_learning/README.md")
    print(obj)

    with work_in_progress("Saving file"):
        with open("/home/thiery/code/python/deep_learning/deep_learning/README.test.md", "w") as f:
            f.write(obj)

    print("test_work_in_progress: End")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:22.424946
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Task description")
    def func():
        time.sleep(0.1)

    func()  # Output: Task description... done. (0.10s)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:37.900029
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import string
    import tempfile
    # Test work_in_progress as context manager
    with work_in_progress("Generating random string"):
        randstr = "".join(random.choice(string.printable) for _ in range(4096)).strip()
    with tempfile.TemporaryDirectory() as tmpdir:
        path = tmpdir + "/tmp"
        with open(path, "w") as f:
            f.write(randstr)
        with work_in_progress("Loading string"):
            with open(path, "r") as f:
                loaded_str = f.read()
        assert(loaded_str == randstr)
        with work_in_progress("Deleting string"):
            os.unlink(path)

    # Test work_in_progress as decorator

# Generated at 2022-06-13 20:08:43.809623
# Unit test for function work_in_progress
def test_work_in_progress():
    def _test_code(desc):
        with work_in_progress(desc):
            time.sleep(0.1)
        time.sleep(0.1)

    _test_code("foo")
    _test_code("bar")
    _test_code("foo")

# Generated at 2022-06-13 20:08:53.057682
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    data = list(range(10**6))
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test.pkl")
        with open(path, "wb") as f:
            pickle.dump(data, f)
        data_pkl = load_file(path)
    assert data == data_pkl

    with work_in_progress("Saving file"):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "test.pkl")

# Generated at 2022-06-13 20:08:58.962535
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

# Generated at 2022-06-13 20:09:01.086980
# Unit test for function work_in_progress
def test_work_in_progress():
    dummy_desc = "dummy"
    dummy_time = 0.5

    with work_in_progress(dummy_desc) as w:
        time.sleep(dummy_time)

# Generated at 2022-06-13 20:09:06.093170
# Unit test for function work_in_progress
def test_work_in_progress():

    def function_to_test():
        with work_in_progress("Testing function"):
            time.sleep(0.5)
    function_to_test()

    @work_in_progress("Testing decorator")
    def function_to_test_by_decorator(): 
        time.sleep(0.5)
    function_to_test_by_decorator()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:12.697926
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test function work_in_progress

    .. code:: python

        >>> with work_in_progress("Testing work_in_progress"):
        ...     time.sleep(2)
        Testing work_in_progress... done. (2.00s)
    """
    with work_in_progress("Testing work_in_progress"):
        time.sleep(2)
test_work_in_progress.__test__ = False

# Generated at 2022-06-13 20:09:18.754589
# Unit test for function work_in_progress
def test_work_in_progress():
    from nose.tools import assert_is_instance
    from nose import SkipTest
    from numpy.testing import assert_almost_equal
    tic = time.time()
    with work_in_progress("Sleeping for 1sec"):
        time.sleep(1)
    toc = time.time()
    assert_almost_equal(toc - tic, 1, decimal=1)

# Generated at 2022-06-13 20:09:29.042463
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    import sys
    import uuid

    test_out = io.StringIO()


# Generated at 2022-06-13 20:09:33.654829
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Start code block 0"):
        time.sleep(0.5)
    with work_in_progress("Start code block 1"):
        time.sleep(2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:52.796117
# Unit test for function work_in_progress
def test_work_in_progress():
    def loader(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def saver(obj, path):
        with open(path, "wb") as f:
            return pickle.dump(obj, f)

    path = "test.pickle"
    if os.path.exists(path):
        os.remove(path)

    obj = dict(zip("abcdefghijklmnop",
                   range(16)))

    with work_in_progress("Preparing data"):
        saver(obj, path)

    with work_in_progress("Loading data"):
        data = loader(path)

    assert data == obj

    os.remove(path)

# Generated at 2022-06-13 20:09:58.703741
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    # Setup
    random.seed(42)

    def run():
        time.sleep(random.uniform(0.5, 1.5))

    # Tests
    with work_in_progress("Test 1"):
        run()

    with work_in_progress("Test 2"):
        run()

    with work_in_progress("Test 3"):
        run()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:06.197496
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    # Saving file... done. (3.78s)
    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:07.433534
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 20:10:14.379139
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import time
    import numpy as np
    from contextlib import redirect_stdout

    # Setup
    a = np.random.rand(100, 100)

    # Test 1
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    path = "../data/numpy_array.pkl"
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    b = load_file(path)

    assert np.allclose(a, b)

    # Test 2
    path = "../data/numpy_array_1.pkl"

# Generated at 2022-06-13 20:10:16.787707
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Test function work_in_progress:", end="")
    with work_in_progress("Test"):
        time.sleep(1)
    print("done.")



# Generated at 2022-06-13 20:10:20.856603
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function :py:func:`work_in_progress`."""
    @work_in_progress("Testing work_in_progress")
    def _():
        time.sleep(0.5)

    _()

# Generated at 2022-06-13 20:10:24.952108
# Unit test for function work_in_progress
def test_work_in_progress():
    from random import randint
    from time import sleep
    rand_time = randint(5, 10)
    with work_in_progress(f"Sleeping for {rand_time} seconds"):
        sleep(rand_time)
    test_work_in_progress.assert_no_error()

# Generated at 2022-06-13 20:10:26.463145
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        pass

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:33.800516
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = load_file("/path/to/some/file")
    save_file("/path/to/some/file")

# Generated at 2022-06-13 20:10:51.668151
# Unit test for function work_in_progress
def test_work_in_progress():
    with open('test_file_path', 'w') as f:
        f.write('0')
    with work_in_progress("Loading file"):
        with open('test_file_path', 'r') as f:
            f.read()
    with work_in_progress("Saving file"):
        with open('test_file_path', 'w') as f:
            f.write('1')
    with open('test_file_path', 'r') as f:
        assert f.read() == '1'

# Generated at 2022-06-13 20:10:55.007781
# Unit test for function work_in_progress
def test_work_in_progress():
    def a(x):
        with work_in_progress("Sleep {} seconds".format(x)):
            time.sleep(x)

    assert a(0.1) is None
    assert a(0.5) is None
    assert a(1) is None

# Generated at 2022-06-13 20:10:59.416081
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
        with work_in_progress("Unpickle file"):
            time.sleep(2)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    assert load_file("README.md")

# if __name__ == "__main__":
#     test_work_in_progress()

# Generated at 2022-06-13 20:11:08.982301
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.23)
    with work_in_progress("Saving file"):
        time.sleep(2.34)
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

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)


# Generated at 2022-06-13 20:11:10.440675
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Time consuming task"):
        time.sleep(2)

# Generated at 2022-06-13 20:11:15.672743
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test function"):
        time.sleep(1)
    def test_work_in_progress():
        time.sleep(1)
    test_work_in_progress = work_in_progress("Test function")(test_work_in_progress)
    test_work_in_progress()


if __name__ == "__main__":
    print("testing functions...")
    test_work_in_progress()

# Generated at 2022-06-13 20:11:24.041841
# Unit test for function work_in_progress
def test_work_in_progress():
    import subprocess
    import sys

    save_file_process = subprocess.Popen(
        [sys.executable, '-c', 'import pickle\n'
                                 "from contextlib import ExitStack\n"
                                 "from contextlib_utils import work_in_progress\n"
                                 "obj = {'nested': {'test': 10}}\n"
                                 "with ExitStack() as stack:\n"
                                 "    stack.enter_context(open('/tmp/test.pkl.save', 'wb'))\n"
                                 "    stack.enter_context(work_in_progress('Saving file')):\n"
                                 "        pickle.dump(obj, sys.stdout)\n"],
        stdout=subprocess.PIPE)

# Generated at 2022-06-13 20:11:34.888946
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


# -----------------------------------------------------------------------------
# Copyright (C) 2018 Angelos Evripiotis.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing

# Generated at 2022-06-13 20:11:40.091550
# Unit test for function work_in_progress
def test_work_in_progress():
    from contextlib import redirect_stdout

    with io.StringIO() as buf, redirect_stdout(buf):
        with work_in_progress("Loading file"):
            time.sleep(3)
        assert buf.getvalue().endswith("... done. (3.00s)\n")

    with io.StringIO() as buf, redirect_stdout(buf):
        with work_in_progress("Saving file"):
            time.sleep(3.78)
        assert buf.getvalue().endswith("... done. (3.78s)\n")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:51.020696
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Function unit test.
    """
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            data = pickle.load(f)
        return data
    path = "/tmp/test_work_in_progress.pkl"
    obj = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    with open(path, "wb") as f:
        pickle.dump(obj, f)
    assert "Loading file... done. " in load_file(path)
    os.remove(path)
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:12:16.813968
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:18.198452
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Counting sheep"):
        time.sleep(3)

# Generated at 2022-06-13 20:12:26.323501
# Unit test for function work_in_progress
def test_work_in_progress():
    from io import StringIO

    class Capturing(list):
        """
        https://stackoverflow.com/a/16571630
        """

        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO()
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            sys.stdout = self._stdout

    @work_in_progress("Loading file")
    def load_file(path: str):
        time.sleep(2)
        with open(path, "rb") as f:
            return pickle.load(f)

    @contextlib.contextmanager
    def save_file(path: str):
        time.sleep(2)
       

# Generated at 2022-06-13 20:12:30.823563
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Sleeping for 1 second"):
        time.sleep(1)
    with work_in_progress("Sleeping for 2 seconds"):
        time.sleep(2)
    return True

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:38.008975
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function work_in_progress."""
    def load_file(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("tests/data/work_in_progress.pkl")
    assert isinstance(obj, dict) is True
    assert "obj1" in obj.keys() is True
    assert obj["obj1"] == "obj1"


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:44.649494
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert isinstance(obj, int)
    print()

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    print()


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:52.431184
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:01.329622
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert True

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    assert True


if __name__ == '__main__':
    test_work_in_progress()
    pass
    # import doctest
    # doctest.testmod()

# Generated at 2022-06-13 20:13:06.448801
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

# Generated at 2022-06-13 20:13:08.206788
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test with no yield
    with work_in_progress():
        pass

    with work_in_progress():
        time.sleep(0.34)

# Generated at 2022-06-13 20:13:53.645314
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        print("Test")
        time.sleep(0.5)


# Run unit test if not imported
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:01.081214
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress"""
    # test 1
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(1)

    load_file("/path/to/some/file")

    # test 2
    with work_in_progress("Saving file"):
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:02.866285
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Time spent doing nothing useful"):
        time.sleep(1)

# Generated at 2022-06-13 20:14:10.261962
# Unit test for function work_in_progress
def test_work_in_progress():
    """Tests the working of the function work_in_progress."""
    # Test - 1: For output of a function, with a yield statement.
    def exponent(base, power):
        """Returns the exponent of a given number."""
        with work_in_progress("Calculating the exponent"):
            result = base ** power
            yield result

    result = exponent(2, 7)
    assert (next(result) == 128)

    # Test - 2: For output of a code block, with no yield statement.
    with work_in_progress("Calculating the square"):
        result = 12 ** 2
    assert (result == 144)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:15.264123
# Unit test for function work_in_progress
def test_work_in_progress():
    def function(n):
        for i in range(n):
            time.sleep(1)
        return "done"

    with work_in_progress("Test for function"):
        result = function(5)
    assert result == "done"


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:21.592121
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import hashlib

    @work_in_progress("Processing file")
    def read_and_hash_file(path):
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    path = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
    read_and_hash_file(path)

# Generated at 2022-06-13 20:14:25.531249
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file():
        time.sleep(2.0)

    load_file()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:27.423472
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    time.sleep(1)

# Generated at 2022-06-13 20:14:29.681090
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(2)
    load_file(".")

    with work_in_progress("Saving file"):
        time.sleep(2)

# Generated at 2022-06-13 20:14:32.744478
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test 1")
    def test_func_1():
        time.sleep(1)

    test_func_1()
    with work_in_progress("Test 2"):
        time.sleep(1)


if __name__ == '__main__':
    test_work_in_progress()