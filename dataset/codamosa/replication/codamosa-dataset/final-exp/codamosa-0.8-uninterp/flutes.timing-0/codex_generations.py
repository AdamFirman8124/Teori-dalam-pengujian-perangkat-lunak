

# Generated at 2022-06-13 20:05:22.608530
# Unit test for function work_in_progress
def test_work_in_progress():
    def delayed_time(t: float):
        time.sleep(t)
        return t

    with work_in_progress("Waiting 10 seconds..."):
        assert delayed_time(10) == 10

    @work_in_progress("Waiting 20 seconds...")
    def foo():
        return delayed_time(20)

    assert foo() == 20

# Generated at 2022-06-13 20:05:25.704947
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:05:27.999223
# Unit test for function work_in_progress
def test_work_in_progress():
    def func(*args, **kwargs):
        yield
        time.sleep(1)

    g = func()
    with work_in_progress("test"):
        next(g)

# Generated at 2022-06-13 20:05:32.017269
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import random
    import tempfile
    @work_in_progress("Computing...")
    def compute():
        total = 0
        for _ in range(10000):
            total += random.random() ** random.random()
        return total
    compute()

    @work_in_progress("Dumping...")
    def dump():
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        print(tmp_file.name)
        os.remove(tmp_file.name)
    dump()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:33.464779
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:05:35.685614
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("My test"):
        time.sleep(1.5)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:43.798600
# Unit test for function work_in_progress
def test_work_in_progress():
    # Work in progress with default description and loading function
    def test_load(path):
        with open(path, "wb") as f:
            data = bytearray(100000)
            f.write(data)
        return data

    with work_in_progress():
        test_load("./temp_work_in_progress_file")

    # Work in progress with saving function
    def test_save(path):
        with open(path, "rb") as f:
            data = f.read()
        return data

    with work_in_progress("Saving file"):
        test_save("./temp_work_in_progress_file")
        
    os.remove("./temp_work_in_progress_file")


if __name__ == '__main__':
    test_work_in_

# Generated at 2022-06-13 20:05:49.164471
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        with work_in_progress("Fake loading file"):
            time.sleep(1)
        with work_in_progress("Fake saving file"):
            time.sleep(2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:05:54.935140
# Unit test for function work_in_progress
def test_work_in_progress():
    def dummy_function(arg):
        time.sleep(0.1)
        return arg

    obj = dummy_function("test")
    assert obj == "test"
    assert True

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:06.347217
# Unit test for function work_in_progress
def test_work_in_progress():
    from contextlib import contextmanager

    @contextmanager
    def none():
        yield
    # Test unit
    assert none().__enter__().__exit__(None, None, None) == None

    # Test normal usage
    @work_in_progress("Load a file")
    def load_file(path):
        with open(path, "r") as file:
            print(file.read(), end='')
    load_file("resources/jupyter_lab/test_work_in_progress.txt")
    print()

# Generated at 2022-06-13 20:06:19.536986
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(2)
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(obj, path):
        time.sleep(3)
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    test_path = "test.pickle"
    test_data = {"test": "test"}

    save_file(test_data, test_path)
    test_data_loaded = load_file(test_path)
    assert test_data == test_data_loaded

# Generated at 2022-06-13 20:06:24.840774
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    class A:
        pass

    a = A()
    with open("test.pickle", "wb") as f:
        pickle.dump(a, f)

    with work_in_progress("Loading file"):
        with open("test.pickle", "rb") as f:
            a = pickle.load(f)

    assert isinstance(a, A)

if __name__ == '__main__':
    r"""
    CommandLine:
        python -m xdoctest.utils.progress work_in_progress
    """
    import xdoctest
    xdoctest.doctest_module(__file__)

# Generated at 2022-06-13 20:06:27.139519
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        pass

# Generated at 2022-06-13 20:06:32.114572
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work in progress") as ctx:
        time.sleep(1)
        assert isinstance(ctx, contextlib.AbstractContextManager)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:35.551881
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Run test"):
        time.sleep(0.1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:45.305776
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

# vim: nu ft=python columns=120 :

# Generated at 2022-06-13 20:06:51.425871
# Unit test for function work_in_progress
def test_work_in_progress():

    # Time a block of code
    with work_in_progress("Sorting list"):
        l = [random.random() for _ in range(1000)]
        l.sort()

    # Decorator for timing functions
    @work_in_progress("Sorting list")
    def sort_list():
        l = [random.random() for _ in range(1000)]
        l.sort()
        return l

    sort_list()

    return 0

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:56.610599
# Unit test for function work_in_progress
def test_work_in_progress():
    random_num = random.uniform(1, 10)
    with work_in_progress(desc="Some task"):
        time.sleep(random_num)
    with work_in_progress(desc="Other task"):
        time.sleep(random_num)

# Generated at 2022-06-13 20:07:00.494963
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

# Generated at 2022-06-13 20:07:11.337637
# Unit test for function work_in_progress
def test_work_in_progress():

    import inspect
    import tempfile
    import pickle

    def load(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    @work_in_progress("Loading file")
    def load_file(path):
        return load(path)

    def save_file(path, obj):
        with work_in_progress("Saving file"):
            save(path, obj)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test")

# Generated at 2022-06-13 20:07:20.944776
# Unit test for function work_in_progress
def test_work_in_progress():
    # In Python, we cannot raise exceptions from functions decorated by contextmanager.
    # This makes the testing of work_in_progress() a little difficult.
    # There are two ways to test it:
    # 1. Manually check the output in the terminal
    # 2. Obtain the output stream and verify it.
    with open(os.devnull, "w") as out:
        with contextlib.redirect_stdout(out):
            @work_in_progress("Test")
            def test():
                time.sleep(1)

            test()


if __name__ == "__main__":
    test_work_in_progress()
    exit()

# Generated at 2022-06-13 20:07:30.040705
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    path = os.path.join(os.path.dirname(__file__), "data.bin")
    obj = load_file(path)

    with work_in_progress("Saving file"):
        path = os.path.join(os.path.dirname(__file__), "data.bin")
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:07:37.979421
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function work_in_progress."""
    # Test code block context manager
    with work_in_progress("Doing some work"):
        time.sleep(0.5)

    # Test function decorator
    @work_in_progress("Doing some work")
    def do_some_work(a, b):
        time.sleep(a / b)
        return a / b

    do_some_work(0.5, 2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:46.152934
# Unit test for function work_in_progress
def test_work_in_progress():
    with pytest.raises(FileNotFoundError):
        with work_in_progress("Loading file"):
            pickle.load(open("/dev/null", "rb"))

    with work_in_progress("Loading file"):
        obj = pickle.load(open(__file__, "rb"))

    with work_in_progress("Saving file"):
        with tempfile.TemporaryFile() as f:
            pickle.dump(obj, f)

    @work_in_progress("Loading file")
    def load_file(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)


# Generated at 2022-06-13 20:07:55.392458
# Unit test for function work_in_progress
def test_work_in_progress():
    func_name = "test_work_in_progress"
    create_test_file(func_name)
    time_consumed_1 = test_fun_1()
    time_consumed_2 = test_fun_2()
    print(f"Time consumed: {time_consumed_1:.4f}/{time_consumed_2:.4f}")
    os.remove(get_test_file_path(func_name))


# Testing for working_in_progress

# Generated at 2022-06-13 20:07:58.915834
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:07.335090
# Unit test for function work_in_progress
def test_work_in_progress():
    import datetime
    from .out import out

    # -- Standard mode
    with work_in_progress("Loading file"):
        time.sleep(0.5)
    assert out.getvalue() == "Loading file... done. (0.50s)\n"
    out.truncate(0)

    # -- Context manager
    with work_in_progress("Loading file") as obj:
        time.sleep(0.5)
        obj = "foo"
    assert out.getvalue() == "Loading file... done. (0.50s)\n"
    out.truncate(0)

    # -- Decorator
    @work_in_progress("Loading file")
    def loading_file():
        time.sleep(0.5)

    loading_file()

# Generated at 2022-06-13 20:08:08.870626
# Unit test for function work_in_progress
def test_work_in_progress():
    def f():
        time.sleep(0.1)
    with work_in_progress("Sleeping"):
        f()

# Generated at 2022-06-13 20:08:14.253341
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    with work_in_progress("Do nothing"):
        time.sleep(1)

    time.sleep(1)
    print("Hello")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:19.107016
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import os

    # Test file saving with 'with' context
    with work_in_progress("Saving file") as context:
        with open("./__test_work_in_progress_file__.pkl", "wb") as f:
            pickle.dump(range(100), f)
    print(context)
    os.remove("./__test_work_in_progress_file__.pkl")

    # Test file loading with function decorator
    @work_in_progress("Loading file")
    def load_file(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)


# Generated at 2022-06-13 20:08:26.069589
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Unit test"
    with work_in_progress(desc) as work:
        time.sleep(0.2)
        assert work is None

# Generated at 2022-06-13 20:08:30.475627
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

# ------------------------------------------------------------------


# Generated at 2022-06-13 20:08:34.063360
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(5)

# Execute unit tests if this file is executed as a standalone program
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:40.440313
# Unit test for function work_in_progress
def test_work_in_progress():
    a = []
    with work_in_progress("Adding elements to a"):
        for i in range(10):
            time.sleep(.1)
            a.append(i)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:44.484957
# Unit test for function work_in_progress
def test_work_in_progress():
    def foo(name):
        time.sleep(1)

    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(1)

    with work_in_progress("Saving file"):
        time.sleep(1)

# Generated at 2022-06-13 20:08:50.825348
# Unit test for function work_in_progress
def test_work_in_progress():
    # Setup
    desc = "Test"
    print(desc + "... ", end='', flush=True)

    # Execute
    begin_time = time.time()
    for i in range(10000):
        str(i)
    time_consumed = time.time() - begin_time

    # Verify
    assert time_consumed > 0, "time_consumed is not greater than zero."

    # Cleanup
    print(f"done. ({time_consumed:.2f}s)")

# Generated at 2022-06-13 20:08:53.401845
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing function work_in_progress"):
        time.sleep(0.1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:57.670186
# Unit test for function work_in_progress
def test_work_in_progress():
    def w(desc, sleep_seconds):
        with work_in_progress(desc):
            time.sleep(sleep_seconds)

    w("Hello", 0.123)
    w("World", 0.321)

# Unit test

# Generated at 2022-06-13 20:08:58.847197
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3)

# Generated at 2022-06-13 20:09:04.100100
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path) as f:
            return pickle.load(f)

    with open("work_in_progress.pickle", "wb") as f:
        pickle.dump(list(range(1000000)), f)

    obj = load_file("work_in_progress.pickle")
    assert obj == list(range(1000000))
    os.remove("work_in_progress.pickle")

# Generated at 2022-06-13 20:09:17.330800
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("counting from 1 to 20"):
        for i in range(20):
            time.sleep(0.1)

test_work_in_progress()

# Generated at 2022-06-13 20:09:28.242760
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    import random

    # Unit test with context manager
    with work_in_progress("Loading file"):
        with open(os.path.expanduser("~/.bash_history"), "rb") as f:
            assert len(pickle.load(f)) >= 0

    # Unit test with function decorator
    @work_in_progress("Computing prime numbers")
    def compute(routine):
        current, total = 2, 0
        while total < routine:
            if all(current % x != 0 for x in range(2, current)):
                yield current
                total += 1
            current += 1

    numbers = tuple(compute(random.randint(1000, 2000)))

# Generated at 2022-06-13 20:09:38.479672
# Unit test for function work_in_progress
def test_work_in_progress():
    class A(object):
        def __init__(self):
            self.data = []
        def append(self, x):
            time.sleep(0.01)
            with work_in_progress(f"Append {x}"):
                self.data.append(x)
        def sort(self):
            time.sleep(0.01)
            with work_in_progress("Sorting"):
                self.data.sort()
        def __repr__(self):
            return f"A{'(%s)' % ', '.join(map(str, self.data)) if self.data else ''}"
    a = A()
    for i in range(5):
        a.append(i)
    print(a)
    a.sort()
    print(a)
    print()

# Generated at 2022-06-13 20:09:43.194464
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

# Generated at 2022-06-13 20:09:52.928947
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with open("tmp.pkl", "wb") as f:
        pickle.dump(range(1000000), f)
    obj = load_file("tmp.pkl")
    # Loading file... done. (0.19s)

    with work_in_progress("Saving file"):
        with open("tmp.pkl", "wb") as f:
            pickle.dump(obj, f)
        time.sleep(1)
    # Saving file... done. (1.00s)
    os.remove("tmp.pkl")

    # Test failure

# Generated at 2022-06-13 20:09:57.082472
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    # Test work_in_progress with decorator
    obj = load_file(__file__)

    # Test work_in_progress with context manager
    with work_in_progress("Saving file"):
        save_file(__file__, obj)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:06.648214
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # Test that file is loaded correctly
    obj = load_file("../tests/data/some_file")
    assert obj == "Hello, world!"

    with work_in_progress("Saving file"):
        with open("../tests/data/some_file.copy", "wb") as f:
            pickle.dump(obj, f)

    time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:09.756419
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test function work_in_progress behavior.
    """
    @work_in_progress()
    def _do_nothing():
        time.sleep(1)

    _do_nothing()

    with work_in_progress():
        time.sleep(1)

# Generated at 2022-06-13 20:10:20.129951
# Unit test for function work_in_progress
def test_work_in_progress():
    from os import remove
    from os.path import join
    from tempfile import gettempdir
    from time import sleep

    @work_in_progress("Saving file")
    def save_binary_file(path):
        with open(path, "wb") as f:
            for i in range(10000):
                f.write(bytes([i % 0x100]))

    @work_in_progress("Loading file")
    def load_binary_file(path):
        with open(path, "rb") as f:
            while True:
                read_result = f.read(1024 * 1024)
                if not read_result:
                    break


# Generated at 2022-06-13 20:10:23.003463
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress"):
        time.sleep(0.7)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:53.801858
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # @work_in_progress("Loading file")
    # def load_file_with_time(path):
    #     time.sleep(1)
    #     return os.path.getmtime(path)

    # time_loaded = load_file_with_time("test_work_in_progress.py")
    # assert time_loaded > 0

    obj = load_file("test_work_in_progress.py")
    assert obj


if __name__ == "__main__":
    test_work_in_progress()
    test_work_in_progress_with_time()

# Generated at 2022-06-13 20:10:59.497739
# Unit test for function work_in_progress
def test_work_in_progress():
    import random

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
    obj = load_file("/path/to/some/file")
    time.sleep(random.uniform(0, 10))

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    time.sleep(random.uniform(0, 10))

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:03.227235
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def slow_task():
        time.sleep(3)

    slow_task()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:04.820493
# Unit test for function work_in_progress
def test_work_in_progress():
    pass


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:12.204383
# Unit test for function work_in_progress
def test_work_in_progress():
    from io import BytesIO
    from contextlib import redirect_stdout
    from io import StringIO

    fake_stdout = s = StringIO()
    with redirect_stdout(fake_stdout):
        with work_in_progress("Dummy task"):
            time.sleep(0.2)
    assert s.getvalue() == "Dummy task... done. (0.20s)\n"

    @work_in_progress("Dummy task")
    def sleep_and_return(x):
        time.sleep(0.2)
        return x
    fake_stdout = s = StringIO()
    with redirect_stdout(fake_stdout):
        x = sleep_and_return(3)
        assert x == 3

# Generated at 2022-06-13 20:11:14.277186
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def sleep():
        time.sleep(1)
    sleep()

# Generated at 2022-06-13 20:11:15.761745
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:19.153840
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def test():
        time.sleep(1)
    try:
        test()
    except:
        raise AssertionError("work_in_progress decorator did not work")

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:22.101619
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function **work_in_progress**.

    .. code:: python

        >>> import doctest
        >>> doctest.run_docstring_examples(work_in_progress, globals())
    """
    pass



# Generated at 2022-06-13 20:11:26.005079
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import random
    try:
        import pytest
    except ImportError:
        return
    @pytest.mark.parametrize("n", range(5))
    def test(n):
        n2 = random.random()
        with work_in_progress(f"The current time is {n}"):
            time.sleep(n2)
    test(5)

# Generated at 2022-06-13 20:12:09.276935
# Unit test for function work_in_progress
def test_work_in_progress():
    pass

# Generated at 2022-06-13 20:12:17.146395
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import os

    def assert_equal(actual, desired):
        assert actual == desired, actual

    def captured_print(*args, **kwargs):
        captured_print.text += ' ' + ' '.join(args)
        captured_print.current_line_size = len(captured_print.text.splitlines()[-1])
        captured_print.current_line_size += sum(
            len(repr(arg)) for arg in args
        )

    def captured_print_reset():
        captured_print.text = ''
        captured_print.current_line_size = 0

    captured_print.text = ''
    captured_print.current_line_size = 0

    def sleep(n: float):
        time.sleep(n)
        print(f"Capture output: {n}")

   

# Generated at 2022-06-13 20:12:19.333471
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        time.sleep(1)
        return

    with work_in_progress("test"):
        load_file("data/test")


# Generated at 2022-06-13 20:12:21.902121
# Unit test for function work_in_progress
def test_work_in_progress():
    begin_time = time.time()
    with work_in_progress("Test passage"):
        time.sleep(0.5)
    assert (time.time() - begin_time) >= 0.5

# Generated at 2022-06-13 20:12:28.422298
# Unit test for function work_in_progress
def test_work_in_progress():
    print(">>> @work_in_progress(\"Loading file\")")
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    print(">>> obj = load_file(\"/path/to/some/file\")")
    obj = load_file("/path/to/some/file")

    print(">>> with wok_in_progress(\"Saving file\"):")
    print("...     with open(path, \"wb\") as f:")
    print("...         pickle.dump(obj, f)")
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)


# Generated at 2022-06-13 20:12:36.651628
# Unit test for function work_in_progress
def test_work_in_progress():
    # This should not print anything.
    with work_in_progress("Foo"):
        pass

    # This should print "...... done. (?)"
    with work_in_progress("Bar"):
        time.sleep(0.3)

    @work_in_progress("Fn1")
    def fn1():
        time.sleep(0.3)

    @work_in_progress("Fn2")
    def fn2():
        time.sleep(0.3)

    fn1()
    fn2()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:41.876708
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    from contextlib import contextmanager

    @contextmanager
    def test_case(to_sleep):
        with work_in_progress() as work_in_progress_info:
            time.sleep(to_sleep)

    test_case(1)

# Unit test when imported as a module
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:44.617621
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.5)
    with work_in_progress("Saving file"):
        time.sleep(1.5)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:51.216713
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)

    with work_in_progress("Saving file"):
        time.sleep(2)

    @work_in_progress("Test")
    def _():
        time.sleep(3)

    _()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:57.020487
# Unit test for function work_in_progress
def test_work_in_progress():
    txt = """
    >>> with work_in_progress("Dummy task"):
    ...     pass
    Dummy task... done. (0.00s)
    """
    doctest.testmod(verbose=False, optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-13 20:14:25.893143
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    for _ in range(10):
        random.seed()
        with work_in_progress():
            time.sleep(random.random())

# Generated at 2022-06-13 20:14:28.732711
# Unit test for function work_in_progress
def test_work_in_progress():
    def test_function(x):
        with work_in_progress("Sleep for {} seconds".format(x)):
            time.sleep(x)

    test_function(1)
    test_function(3)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:32.315252
# Unit test for function work_in_progress
def test_work_in_progress():
    from time import sleep
    with (work_in_progress("Unit test")):
        sleep(1.75)
    assert True

test_work_in_progress()


#
#
#    END OF FILE
#
#

# Generated at 2022-06-13 20:14:43.832207
# Unit test for function work_in_progress
def test_work_in_progress():
    """
    Unit test that checks that work_in_progress correctly displays
    the time taken by a code block.

    :return: True if the test is completed successfully, False otherwise.
    """
    import time

    # Test case 1: regular code block
    with work_in_progress("Test case 1"):
        time.sleep(0.1)
    # Test case 2: function
    @work_in_progress("Test case 2")
    def f():
        time.sleep(0.1)
    f()
    # Test case 3: nested
    @work_in_progress("Test case 3")
    def g():
        @work_in_progress("Nested case 1")
        def h():
            time.sleep(0.1)

# Generated at 2022-06-13 20:14:48.122036
# Unit test for function work_in_progress
def test_work_in_progress():
    from tempfile import NamedTemporaryFile
    import pickle
    import numpy as np

    def load_file():
        with NamedTemporaryFile() as f:
            obj = np.random.rand(10, 10)
            with work_in_progress("Saving file"):
                pickle.dump(obj, f)
                f.flush()
            with work_in_progress("Loading file"):
                pickle.load(f)

    load_file()



# Generated at 2022-06-13 20:14:53.626555
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    @work_in_progress("Test 1")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    assert load_file("utils.py") is not None

    with work_in_progress("Test 2"):
        with open("utils.py", "rb") as f:
            pickle.load(f)

# Generated at 2022-06-13 20:15:02.469263
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
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

# Generated at 2022-06-13 20:15:04.539263
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing"):
        time.sleep(1)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:15:10.663710
# Unit test for function work_in_progress
def test_work_in_progress():
    try:
        with work_in_progress("Loading file"):
            with open("/tmp/test.pkl", "rb") as f:
                obj = pickle.load(f)
    except FileNotFoundError:
        pass
    else:
        assert obj == 0

    with work_in_progress("Saving file"):
        with open("/tmp/test.pkl", "wb") as f:
            pickle.dump(0, f)

# Generated at 2022-06-13 20:15:22.505015
# Unit test for function work_in_progress
def test_work_in_progress():

    # Time a function while loading a file
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    # Time a code block while saving a file
    path = "test_object.pkl"
    obj = ["test", 42, False]
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    # Test the loading function
    test_obj = load_file("test_object.pkl")
    assert test_obj == obj

    # Clean up
    os.remove("test_object.pkl")

# Work in progress main
if __name__ == '__main__':
    test_work_