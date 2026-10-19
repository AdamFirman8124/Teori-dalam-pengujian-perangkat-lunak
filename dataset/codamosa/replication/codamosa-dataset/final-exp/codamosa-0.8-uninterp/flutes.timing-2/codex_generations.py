

# Generated at 2022-06-13 20:05:18.844797
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    with work_in_progress("Sleeping for 1 sec"):
        time.sleep(1)

# Generated at 2022-06-13 20:05:24.959169
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test work_in_progress

    The test code is as follows:

    >>> @work_in_progress("Loading file")
    ... def load_file(path):
    ...     with open(path, "rb") as f:
    ...         return pickle.load(f)
    ...
    ... obj = load_file("/path/to/some/file")
    ...
    >>> with work_in_progress("Saving file"):
    ...     with open(path, "wb") as f:
    ...         pickle.dump(obj, f)
    # the code itself does not test for the correctness of
    # the function
    """

# Generated at 2022-06-13 20:05:28.860299
# Unit test for function work_in_progress
def test_work_in_progress():
    work_in_progress("Testing work in progress")
    with work_in_progress("In progress"):
        time.sleep(0.1)
    with work_in_progress("In progress 2"):
        time.sleep(0.2)
    with work_in_progress("In progress 3"):
        time.sleep(0.3)

# Generated at 2022-06-13 20:05:35.107240
# Unit test for function work_in_progress
def test_work_in_progress():
    print('Test: function `work_in_progress`')

    # Test for `with` mode
    with work_in_progress('Task #1'):
    # do something
        time.sleep(1)
    # Task #1... done. (1.00s)

    # Test for `decorator` mode
    @work_in_progress('Task #2')
    def func1():
    # do something
        time.sleep(2)
    func1()
    # Task #2... done. (2.00s)

    print('Test completed')


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:40.963808
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

# Generated at 2022-06-13 20:05:48.418752
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

    # Loading a file
    obj = load_file("./data/my.pickle")
    assert(isinstance(obj, dict))
    assert(obj["a"] == 1)
    assert(obj["b"] == 2)

    # Saving a file
    save_file("./data/test.pickle", {"name": "John"})
    assert(os.path.isfile("./data/test.pickle"))


# Unit

# Generated at 2022-06-13 20:06:00.668873
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    time.sleep(1)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        time.sleep(1)


if __name__ == '__main__':
    # Unit test
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:06:09.874603
# Unit test for function work_in_progress
def test_work_in_progress():
    import os

    # Create a file
    path = "/tmp/testfile"
    with open(path, "w") as f:
        f.write("Hello world!\n")
    assert os.path.exists(path)

    # Remove file in a work_in_progress with a for-loop
    for i in range(10):
        with work_in_progress(f"Removing {path}"):
            os.remove(path)
        assert not os.path.exists(path)

    # Remove file in a work_in_progress with a while-loop
    while True:
        with work_in_progress(f"Removing {path}"):
            os.remove(path)
        assert not os.path.exists(path)
        break


# Generated at 2022-06-13 20:06:20.115845
# Unit test for function work_in_progress
def test_work_in_progress():
    def run(clock=time.process_time):
        @work_in_progress("Loop 1000 times")
        def loop():
            for i in range(1000):
                continue

        begin = clock()
        loop()
        end = clock()
        print(f"Elapsed time: {end - begin}")
        print("=" * 80)

    # 1. Example of context manager
    print("Context manager:")
    run()

    # 2. Example of decorator
    print("Decorator:")

    @work_in_progress("Loop 1000 times")
    def loop():
        for i in range(1000):
            continue

    run()

    print("=" * 80)


# test_work_in_progress()

# Generated at 2022-06-13 20:06:22.524375
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:31.836533
# Unit test for function work_in_progress
def test_work_in_progress():
    """
    Unit test for function work_in_progress.
    """
    import pickle
    import os
    with work_in_progress("Generating random data"):
        data = [random.randint(0, 100) for _ in range(10**6)]
    path = "test-wip.tmp"
    with work_in_progress("Saving data"):
        with open(path, "wb") as f:
            pickle.dump(data, f)
    with work_in_progress("Loading data"):
        with open(path, "rb") as f:
            loaded_data = pickle.load(f)
    # os.remove(path)

# Generated at 2022-06-13 20:06:45.119250
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            r = pickle.load(f)
            time.sleep(0.5)
            return r

    obj = load_file("/path/to/some/file")


# -----------------------------------------------------------------------------
# Copyright (C) 2019 Angelos Evripiotis.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANT

# Generated at 2022-06-13 20:06:48.285093
# Unit test for function work_in_progress
def test_work_in_progress():
    for function in [
        lambda: time.sleep(1),
        lambda: time.sleep(2),
        lambda: time.sleep(3),
        lambda: time.sleep(4),
        lambda: time.sleep(5),
    ]:
        with work_in_progress(f"Executing {function}"):
            function()
        time.sleep(0.1)

# Generated at 2022-06-13 20:06:51.932038
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def function_with_work_in_progress():
        time.sleep(1)
        return "Done"

    with work_in_progress("Testing work in progress"):
        time.sleep(1)

    ret = function_with_work_in_progress()

    assert ret == "Done"


# Generated at 2022-06-13 20:06:57.131208
# Unit test for function work_in_progress
def test_work_in_progress():
    n = 10000
    sleep_time = 1

    def do_work(n: int):
        for _ in range(n):
            time.sleep(sleep_time)
            yield

    with work_in_progress("Critically important work"):
        for _ in do_work(n):
            pass

# Generated at 2022-06-13 20:07:02.385948
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test function decorator
    @work_in_progress("Testing function decorator")
    def foo():
        time.sleep(1)

    foo()

    # Test with statement
    with work_in_progress("Testing with statement"):
        time.sleep(2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:11.673830
# Unit test for function work_in_progress
def test_work_in_progress():
    with contextlib.redirect_stdout(StringIO()):
        with work_in_progress():
            time.sleep(1.0)
            raise Exception()
        raise Exception()
    assert "done." not in sys.stdout.getvalue()

    with contextlib.redirect_stdout(StringIO()):
        with work_in_progress():
            time.sleep(1.0)
    assert "done." in sys.stdout.getvalue()

    @work_in_progress
    def saving_file():
        time.sleep(1.0)
    saving_file()
    assert "done." in sys.stdout.getvalue()

# vim:sw=4:et:

# Generated at 2022-06-13 20:07:20.714125
# Unit test for function work_in_progress
def test_work_in_progress():
    import contextlib
    import time

    # Test the function as a context manager
    with work_in_progress("Task 1"):
        time.sleep(1)

    with work_in_progress("Task 2"):
        time.sleep(2)

    # Test the decorator
    @work_in_progress()
    def func_1():
        time.sleep(1)

    func_1()
    with work_in_progress("Task 3"):
        @work_in_progress("Inner task 1")
        def func_2():
            time.sleep(2)

        func_2()

    # Test the decorator when used as a context manager
    @contextlib.contextmanager
    @work_in_progress()
    def func_3():
        time.sleep(3)


# Generated at 2022-06-13 20:07:29.304464
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


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:07:36.201662
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving file"):
        with open("foo.bin", "wb") as f:
            pickle.dump("Hello World!", f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:43.127943
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Fibonacci series")
    def test_func(n):
        a, b = 0, 1
        while n:
            a, b = b, a + b
            n -= 1

    test_func(100)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:46.615487
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(0.5)

    @work_in_progress("Loading file")
    def _():
        time.sleep(0.5)
    _()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:55.858001
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

# Generated at 2022-06-13 20:08:00.914471
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:01.834168
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:08:03.384419
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Doing 1, 2, 3"):
        time.sleep(0.1)
    assert True  # make pytest happy

# Generated at 2022-06-13 20:08:14.968918
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    from contextlib import redirect_stdout

    class Object:
        pass

    f = io.StringIO()
    with redirect_stdout(f):
        with work_in_progress("Loading"):
            obj = Object()
    assert f.getvalue() == 'Loading... done. (0.00s)\n'

    f = io.StringIO()
    with redirect_stdout(f):
        @work_in_progress("Saving")
        def save(obj):
            pass

        save(obj)
    assert f.getvalue() == 'Saving... done. (0.00s)\n'

# Generated at 2022-06-13 20:08:16.419466
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:08:23.110382
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

# Generated at 2022-06-13 20:08:27.345625
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Testing work_in_progress"
    begin_time = time.time()
    with work_in_progress(desc):
        time_spent = time.time() - begin_time
    assert time_spent > 0.1 and time_spent < 0.15
    print("Test successful")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:43.876461
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

    obj = load_file("/tmp/test.pkl")
    save_file(obj, "/tmp/test2.pkl")

    with work_in_progress("Deleting file") as w:
        pass

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:47.144675
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:57.844586
# Unit test for function work_in_progress
def test_work_in_progress():
    import os, tempfile, subprocess

    script = tempfile.NamedTemporaryFile(mode="w+")
    script.write("""
import time

time.sleep(1)
    """)
    script.flush()

    with tempfile.TemporaryDirectory() as temp_dir:
        stdout_file = os.path.join(temp_dir, "stdout.log")
        stderr_file = os.path.join(temp_dir, "stderr.log")

        with open(stdout_file, "w") as stdout, open(stderr_file, "w") as stderr:
            subprocess.run(
                ["python", "-u", script.name],
                stdout=stdout,
                stderr=stderr,
            )


# Generated at 2022-06-13 20:09:02.066738
# Unit test for function work_in_progress
def test_work_in_progress():

    begin_time = time.time()
    with work_in_progress("Testing"):
        time.sleep(0.5)
    print(f"Time consumed: {time.time()-begin_time:.2f}s")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:05.236240
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("test"):
        time.sleep(3)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:14.763122
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(2)
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert isinstance(obj, type(None)), \
    "Make sure the description is printed before the execution of the block."

    import pickle
    with work_in_progress("Saving file"):
        time.sleep(2)
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(None, f)

# Generated at 2022-06-13 20:09:20.247262
# Unit test for function work_in_progress
def test_work_in_progress():
    test_file = "/tmp/work_in_progress_test.pickle"

    with work_in_progress("Loading file"):
        with open(test_file, "rb") as f:
            obj = pickle.load(f)

    with work_in_progress("Saving file"):
        with open(test_file, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:09:27.095267
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    import sys
    import pytest
    from unittest.mock import patch

    @work_in_progress("This is a test")
    def temp_function():
        return None

    with patch.object(sys, 'stdout', new=io.StringIO()) as fake_stdout:
        temp_function()
    assert("This is a test... Done. (0.00s)" in fake_stdout.getvalue())

# Generated at 2022-06-13 20:09:36.597646
# Unit test for function work_in_progress
def test_work_in_progress():
    path = "/dev/null"
    data = b"DATA"
    with open(path, "wb") as f:
        f.write(data)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return f.read()

    obj = load_file(path)
    assert data == obj

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            f.write(obj)
    with open(path, "rb") as f:
        new_obj = f.read()

    assert data == new_obj

# Generated at 2022-06-13 20:09:39.394596
# Unit test for function work_in_progress
def test_work_in_progress():
    try:
        with work_in_progress("Loading file"):
            time.sleep(1)
        with work_in_progress("Saving file"):
            time.sleep(3)
    except KeyboardInterrupt:
        pass

# Generated at 2022-06-13 20:09:43.122629
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Random task"):
        time.sleep(0.5)

# Generated at 2022-06-13 20:09:45.542608
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Work in progress"):
        time.sleep(3)

# Test with pytest

# Generated at 2022-06-13 20:09:48.254138
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing...")
    def _test_work_in_progress():
        time.sleep(0.2)
    _test_work_in_progress()

# Generated at 2022-06-13 20:09:53.091771
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Numerical integration of e^(2*x) from {} to {}")
    def integrate(arg1, arg2):
        def f(x):
            return 2 * x * np.exp(2 * x)
        return quad(f, arg1, arg2)[0]

    z = integrate(0, 1)

if __name__ == "__main__":
    # Unit test for function work_in_progress
    test_work_in_progress()

# Generated at 2022-06-13 20:09:56.174690
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

# Generated at 2022-06-13 20:09:57.124127
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:10:00.431355
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Working in progress"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:09.132111
# Unit test for function work_in_progress
def test_work_in_progress():
    import pathlib
    import pickle

    path = pathlib.Path("/tmp") / "test.pickle"

    @work_in_progress("Writing file")
    def write_file():
        with path.open("wb") as f:
            pickle.dump("Hello, world!", f)

    @work_in_progress("Reading file")
    def read_file():
        with path.open("rb") as f:
            return pickle.load(f)

    @work_in_progress("Deleting file")
    def delete_file():
        path.unlink()

    write_file()
    assert read_file() == "Hello, world!"
    delete_file()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:14.678663
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test function :py:func:`work_in_progress`.
    """
    import pickle

    with work_in_progress("Loading file"):
        with open("/path/to/file", "rb") as f:
            obj = pickle.load(f)
    with work_in_progress("Saving file"):
        with open("/path/to/file", "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:10:21.959906
# Unit test for function work_in_progress
def test_work_in_progress():
    def f(a, c, b):
        return a + c - b

    with work_in_progress("Testing work_in_progress"):
        assert 1 - f(10, 100, 5) == -94


# Run the test automatically, if the module is not imported by others
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:34.102473
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle

    tmp_dir = 'temp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    try:
        with work_in_progress("Creating file"):
            with open(os.path.join(tmp_dir, "test_file.pkl"), "wb") as f:
                pickle.dump(os, f)

        with work_in_progress("Loading file"):
            with open(os.path.join(tmp_dir, "test_file.pkl"), "rb") as f:
                loaded_obj = pickle.load(f)
        assert loaded_obj is os
    finally:
        os.remove(os.path.join(tmp_dir, "test_file.pkl"))

# Generated at 2022-06-13 20:10:37.478975
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1)
    # Test for decorator
    @work_in_progress("Testing decorator")
    def slow_func():
        time.sleep(1)
    slow_func()
    print("test_work_in_progress passed.")


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:43.276315
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

# Generated at 2022-06-13 20:10:50.577116
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path: str):
        time.sleep(1.0)
        return 0

    @work_in_progress("Saving file")
    def save_file(path: str, obj):
        time.sleep(3.4)

    obj = load_file("/tmp/test.tmp")
    save_file("/tmp/test.tmp", obj)
    assert True

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:56.232671
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

# Generated at 2022-06-13 20:10:58.612908
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Unit test"):
        time.sleep(0.1)


# Generated at 2022-06-13 20:11:02.963062
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Solving problem"):
        time.sleep(2.4)
    with work_in_progress():
        time.sleep(2.5)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:07.910679
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test work_in_progress decorator."""
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

# Execute test function when script is run.
if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:16.734757
# Unit test for function work_in_progress
def test_work_in_progress():
    from contextlib import redirect_stdout, redirect_stderr
    import io
    import unittest

    f = io.StringIO()

    with redirect_stdout(f), redirect_stderr(f), unittest.mock.patch("time.time", lambda: 1):
        with work_in_progress("foo"):
            time.sleep(0.1)
        assert f.getvalue() == "foo... done. (0.10s)\n"

    f = io.StringIO()
    with redirect_stdout(f), redirect_stderr(f), unittest.mock.patch("time.time", lambda: 1):
        @work_in_progress("bar")
        def foo():
            time.sleep(0.2)
        foo()

# Generated at 2022-06-13 20:11:25.339381
# Unit test for function work_in_progress
def test_work_in_progress():

    # Use function as decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    # Loading file... done. (3.52s)

    # Use function as context manager
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    # Saving file... done. (3.78s)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:39.396339
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys
    if sys.version_info < (3,5):
        return

    import io
    import contextlib
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "r") as f:
            return f.read()

    with contextlib.redirect_stdout(io.StringIO()) as buffer:
        out = load_file(__file__)

    assert out == open(__file__).read()
    assert buffer.getvalue().rstrip().endswith('Loading file... done. (0.00s)')

    with contextlib.redirect_stdout(io.StringIO()) as buffer:
        with work_in_progress("Testing"):
            time.sleep(0.01)


# Generated at 2022-06-13 20:11:43.913440
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:46.936792
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Hello"):
        time.sleep(1.5)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:54.336490
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import os

    with open("/tmp/_test_work_in_progress.pkl", "wb") as f:
        pickle.dump({0}, f)

    @work_in_progress
    def load_file():
        with open("/tmp/_test_work_in_progress.pkl", "rb") as f:
            assert pickle.load(f) == {0}

    @work_in_progress("Saving file")
    def save_file():
        with open("/tmp/_test_work_in_progress2.pkl", "wb") as f:
            pickle.dump({0}, f)

    load_file()
    save_file()

    os.remove("/tmp/_test_work_in_progress.pkl")

# Generated at 2022-06-13 20:11:57.435342
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "function work_in_progress test"
    with work_in_progress(desc):
        time.sleep(0.1)

# Generated at 2022-06-13 20:12:05.454107
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress
    def test():
        time.sleep(0.5)

    def test2(x):
        @work_in_progress
        def test3():
            time.sleep(1)
            return x**2
        return test3()
    test()
    assert test2(5) == 25

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:10.158861
# Unit test for function work_in_progress
def test_work_in_progress():
    with pytest.raises(FileNotFoundError):
        with work_in_progress("Open non-existing file"):
            with open("/file/does/not/exist") as f:
                pass

    with work_in_progress("Load pickled data"):
        with open("/dev/urandom", "rb") as f:
            pickle.load(f)

    with work_in_progress("Dump pickled data"):
        with open("/dev/urandom", "wb") as f:
            pickle.dump(b"\x00", f)

    with work_in_progress("Sleep for 2 seconds"):
        time.sleep(2)

# Generated at 2022-06-13 20:12:17.389979
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    path = "/path/to/some/pickle"
    try:
        with work_in_progress("Loading file"):
            obj = load_file(path)
        assert os.path.exists(path) and os.path.isfile(path)
    except:
        open(path, "w").close() # create placeholder
        raise
    finally:
        os.remove(path)


# Generated at 2022-06-13 20:12:23.522454
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path: str) -> float:
        """Load a file and return a float"""
        with open(path, "rb") as f:
            time.sleep(1)
            return pickle.load(f)

    with open("/tmp/dump.pkl", "wb") as f:
        pickle.dump(0.234, f)

    time_consumed = load_file("/tmp/dump.pkl")

    assert time_consumed == 0.234

# Generated at 2022-06-13 20:12:34.030518
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test function work_in_progress.
    """
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving file"):
        path = os.path.expanduser("~/.hidden/some/path")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(dict(a=1, b=2), f)

    obj = load_file("/path/to/some/file")
    print

# Generated at 2022-06-13 20:12:42.297774
# Unit test for function work_in_progress
def test_work_in_progress():
    assert work_in_progress.__name__ == "work_in_progress"
    assert work_in_progress.__doc__ is not None


if __name__ == "__main__":
    print(work_in_progress.__doc__)
    test_work_in_progress()

# Generated at 2022-06-13 20:12:46.460586
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

    obj = load_file("/tmp/test.pkl")
    save_file("/tmp/test.pkl")

# Generated at 2022-06-13 20:12:57.197414
# Unit test for function work_in_progress
def test_work_in_progress():
    # Generate a random string
    s = "".join(random.sample(string.ascii_lowercase, k=10))
    print(f"Random string = {s}")
    # Write to a file
    fname = f"test_{s}.txt"
    with work_in_progress(f"Writing to file {fname!r}"):
        with open(fname, "w+") as f:
            f.write(s)
    # Read from a file
    with work_in_progress(f"Reading from file {fname!r}"):
        with open(fname, "r") as f:
            assert s == f.read()
    # Delete the file
    with work_in_progress(f"Deleting file {fname!r}"):
        os.remove(fname)

# Generated at 2022-06-13 20:13:05.054011
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with work_in_progress("Loading file"):
            with open(path, "rb") as f:
                return pickle.load(f)

    obj = load_file(__file__)

    def save_file(path):
        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)

    save_file(__file__)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:06.642868
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:13:10.103410
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    #TODO: Fix the unit test
    #obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:13:14.443155
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sleeping for a second")
    def sleep_for_a_second():
        time.sleep(1)
    sleep_for_a_second()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:22.572226
# Unit test for function work_in_progress
def test_work_in_progress():
    test_obj = [1, 2, 3, 4, 5]
    begin_time = time.time()
    time.sleep(0.1)
    with work_in_progress("Loading file"):
        with open("./load_file.txt", "wb") as f:
            pickle.dump(test_obj, f)
        with open("./load_file.txt", "rb") as f:
            test_obj = pickle.load(f)
        assert test_obj == [1, 2, 3, 4, 5]
    time_consumed = time.time() - begin_time
    assert time_consumed >= 0.1


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:27.602984
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("file.pkl")

# Generated at 2022-06-13 20:13:35.811660
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress().
    """
    desc = "Test"
    print(desc + "... ", end='', flush=True)
    begin_time = time.time()
    time.sleep(1)
    time_consumed = time.time() - begin_time
    assert time_consumed >= 1
    print(f"done. ({time_consumed:.2f}s)")

# Generated at 2022-06-13 20:13:41.933835
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(3.5)

# Generated at 2022-06-13 20:13:44.934575
# Unit test for function work_in_progress
def test_work_in_progress():
    cached_pairs = dict()

    with work_in_progress("Caching pairs"):
        for i in range(10000):
            cached_pairs[i] = i + 1


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:13:49.233768
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3.52)
    with work_in_progress("Saving file"):
        time.sleep(3.78)

# The following two lines are only to be used when debugging this module.
# Suggestion: run with `python -m isbnlib._test_work_in_progress`
if __name__ == "__main__": # pragma: nocover
    test_work_in_progress()

# Generated at 2022-06-13 20:13:52.536457
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.52)


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 20:13:56.747941
# Unit test for function work_in_progress
def test_work_in_progress():
    return True

if __name__ == "__main__":
    r"""CommandLine:
        python -m kwcoco.util.progress all
    """
    import xdoctest as xdoc
    xdoc.doctest_module(__file__)

# Generated at 2022-06-13 20:14:07.321731
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress()
    def count_lines(path):
        n_lines = 0
        with open(path) as f:
            for _ in f:
                n_lines += 1
        return n_lines

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    FILE_NAME = "__testfile.txt"
    with open(FILE_NAME, "w") as f:
        f.write("Test\n" * 1000)

    n_lines = 0

# Generated at 2022-06-13 20:14:17.909736
# Unit test for function work_in_progress
def test_work_in_progress():
    obj = {'a': [1, 2, 3], 'b': True}

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    path = "/tmp/work_in_progress_test.pickle"
    if os.path.exists(path):
        os.remove(path)
    save_file(path, obj)
    o = load_file(path)

# Generated at 2022-06-13 20:14:20.304787
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def test_function():
        time.sleep(0.5)

    test_function()

# Generated at 2022-06-13 20:14:21.591994
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Wait for 5 seconds"):
        time.sleep(5)

# Generated at 2022-06-13 20:14:26.250143
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Waiting")
    def test_wait():
        time.sleep(1)

    with work_in_progress("Waiting"):
        time.sleep(1)
    test_wait()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:42.208836
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    with work_in_progress("Loading file"):
        time.sleep(1)

# Generated at 2022-06-13 20:14:57.033082
# Unit test for function work_in_progress
def test_work_in_progress():
    # Make class
    class A:
        pass

    # Make a random object
    a = A()

    # Test decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # Test context manager
    with work_in_progress("Saving file"):
        with open("__temp_test_file", "wb") as f:
            pickle.dump(a, f)
        a2 = load_file("__temp_test_file")

    print("Timed execution of printing for 15 seconds. (15s)")
    for i in range(15):
        time.sleep(1)
        print("\r" + "█ " * (i + 1), end='')

    os

# Generated at 2022-06-13 20:15:02.698352
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

# Generated at 2022-06-13 20:15:09.106366
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    obj = {
        "a": [1,2,3,4,5,6,7],
        "b": [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    }

    @work_in_progress("Loading data")
    def load_data(data):
        with open("testdata.dat", "wb") as f:
            pickle.dump(data, f)

    @work_in_progress("Saving data")
    def save_data():
        with open("testdata.dat", "rb") as f:
            data = pickle.load(f)

    load_data(obj)
    save_data()

    return True

if __name__ == "__main__":
    import doctest
    doct

# Generated at 2022-06-13 20:15:20.060270
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Unit test for function work_in_progress")
    with work_in_progress("Test 1"):
        try:
            raise Exception("Test")
        except Exception:
            pass

    @work_in_progress("Test 2")
    def test_func():
        return 3 + 3

    assert test_func() == 6

    with work_in_progress("Test 3"):
        pass

    with work_in_progress("Test 4"):
        pass
    print("Done")