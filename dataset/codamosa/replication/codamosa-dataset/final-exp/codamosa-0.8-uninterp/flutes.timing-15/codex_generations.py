

# Generated at 2022-06-13 20:05:25.392777
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with tempfile.NamedTemporaryFile(mode="wb") as tmp_file:
        tmp_file.write(b"Hello World")
        tmp_file.seek(0)
        obj = load_file(tmp_file.name)
        # Prevent "ValueError: I/O operation on closed file"
        tmp_file.close()
        assert obj == "Hello World"


# Generated at 2022-06-13 20:05:29.687609
# Unit test for function work_in_progress
def test_work_in_progress():
    task_time = 3

    @work_in_progress("Testing work_in_progress")
    def foo():
        time.sleep(task_time)

    foo()
    with work_in_progress("Testing work_in_progress"):
        time.sleep(task_time)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:36.580068
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def test_work_in_progress():
        """Verification of work_in_progress."""
        time.sleep(0.01)

    test_work_in_progress()
    print("## Validation of work_in_progress is done.")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:43.801334
# Unit test for function work_in_progress
def test_work_in_progress():
    class Counter:
        def __init__(self, initial: int = 0):
            self._counter = initial
        
        @property
        def value(self) -> int:
            return self._counter
        
        def increment(self, by: int = 1):
            self._counter += by
    
    # Use context manager
    count = Counter()
    with work_in_progress(desc="Incrementing counter"):
        count.increment(10)
    assert count.value == 10, "Counter must be 10."

    # Use decorator
    count2 = Counter()
    @work_in_progress(desc="Incrementing counter")
    def increment2():
        count2.increment(10)
    
    increment2()
    assert count2.value == 10, "Counter must be 10."

# Generated at 2022-06-13 20:05:46.979419
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Some task"):
        time.sleep(0.125)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:51.169869
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.23)

# Generated at 2022-06-13 20:06:07.435221
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile
    import shutil
    import os.path as path
    import pickle
    import random
    import string

    def temp_file(obj=None):
        _, name = tempfile.mkstemp(
            prefix="work_in_progress", suffix=".tmp"
        )
        if obj is not None:
            with open(name, "wb") as f:
                pickle.dump(obj, f)
        return name


# Generated at 2022-06-13 20:06:14.679247
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

# Generated at 2022-06-13 20:06:20.735493
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Doing some work")
    def _do_some_work():
        time.sleep(1.2)
    _do_some_work()

    with work_in_progress("Doing some other work"):
        time.sleep(1.2)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:26.495088
# Unit test for function work_in_progress
def test_work_in_progress():
    # Example 1
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    # Loading file... done. (3.52s)

    # Example 2
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    # Saving file... done. (3.78s)

# Generated at 2022-06-13 20:06:36.385018
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

# Generated at 2022-06-13 20:06:47.766827
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    from tempfile import NamedTemporaryFile

    # Save obj to a file, using the given description to describe the task.
    def save(path, obj, desc="Saving obj"):
        with work_in_progress(desc):
            with open(path, "wb") as f:
                pickle.dump(obj, f)

    # Do something
    with NamedTemporaryFile(mode="wb") as tmpfile:
        save(tmpfile.name, {"a": 1, "b": 2}, "Testing work_in_progress")
    assert os.path.exists(tmpfile.name)

# Generated at 2022-06-13 20:06:52.491874
# Unit test for function work_in_progress
def test_work_in_progress():

    def sleep(secs: float):
        time.sleep(secs)
        return secs

    def load_file(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Testing work_in_progress")
    def load_file2(path):
        return load_file(path)

    @work_in_progress("Testing work_in_progress")
    def sleep2(secs):
        return sleep(secs)

    with work_in_progress("Testing work_in_progress"):
        load_file2(__file__)

    with work_in_progress("Testing work_in_progress") as work:
        for i in range(10):
            sleep2(0.2)

# Generated at 2022-06-13 20:07:00.551075
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(3)
        return

    load_file("/path/to/file")

    with work_in_progress("Waiting") as bar:
        time.sleep(5)
        bar.update(2)
        time.sleep(5)
        bar.update(2)
    print()


# TESTING CODE
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:03.745764
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("testing"):
        time.sleep(0.5)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:04.921637
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test time") as t:
        time.sleep(1)


# Generated at 2022-06-13 20:07:07.097654
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Something")
    def something():
        time.sleep(.5)
        # Something takes about one second to finish
    something()

# Generated at 2022-06-13 20:07:12.172541
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("A")
    def a():
        time.sleep(1)
    @work_in_progress("B")
    def b():
        with work_in_progress("C"):
            time.sleep(1)
    with work_in_progress("D"):
        time.sleep(1)
    a()
    b()

# Generated at 2022-06-13 20:07:18.037707
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file():
        time.sleep(0.5)
        with open("/path/to/some/file", "rb") as f:
            return pickle.load(f)

    obj = load_file()
    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)


# Generated at 2022-06-13 20:07:21.721991
# Unit test for function work_in_progress
def test_work_in_progress():
    @partial(work_in_progress, "Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:07:32.167727
# Unit test for function work_in_progress
def test_work_in_progress():
    # To make unit test deterministic
    random.seed(0)

    for i in range(100):
        # Test for a block
        with work_in_progress("Loading file"):
            time.sleep(random.random())
        # Test for a function
        @work_in_progress("Loading file")
        def _():
            time.sleep(random.random())
        _()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:37.881510
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Task 1"):
        time.sleep(1)

    with work_in_progress("Task 2"):
        time.sleep(2)

    with work_in_progress("Task 3"):
        time.sleep(3)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:42.852847
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(1)
    with work_in_progress("Test function 1 (1s)"):
        time.sleep(1)

    @work_in_progress("Test function 2 (3s)")
    def func():
        time.sleep(3)
        return True

    func()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:43.699327
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:07:45.273953
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Time-consuming task"):
        time.sleep(0.51)

# Generated at 2022-06-13 20:07:49.572321
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:07:52.771789
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def _():
        with open("/dev/null", "wb") as f:
            yield f
        return

    _()

# Generated at 2022-06-13 20:08:02.230054
# Unit test for function work_in_progress
def test_work_in_progress():
    print("==== work_in_progress ====\n")

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    # Test
    test_work_in_progress()

# Generated at 2022-06-13 20:08:10.535247
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test the function work_in_progress
    """
    # Test the context manager by calculating the factorial of 0-9.
    print()
    for i in range(10):
        with work_in_progress(f"Calculating the factorial of {i}"):
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
    # Test the decorator.
    @work_in_progress("Calculating the factorials of 0-9")
    def factorials():
        """Calculate the factorials of numbers from 0 to 9.
        """
        for i in range(10):
            yield factorial

    # print(list(factorials()))

# Generated at 2022-06-13 20:08:18.371459
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import time
    from tempfile import NamedTemporaryFile

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with NamedTemporaryFile() as f:
        with work_in_progress("Saving file"):
            with open(f.name, "wb") as f2:
                pickle.dump("Hello World!", f2)
        time.sleep(0.1)
        assert load_file(f.name) == "Hello World!"

# Generated at 2022-06-13 20:08:44.580903
# Unit test for function work_in_progress

# Generated at 2022-06-13 20:08:48.409243
# Unit test for function work_in_progress
def test_work_in_progress():
    max_time = 0.1
    with work_in_progress("Counting to 1000000000"):
        i = 0
        begin_time = time.time()
        while(i < 1000000000):
            i += 1
        time_consumed = time.time() - begin_time
        assert time_consumed < max_time, f"Time consumed: {time_consumed}"

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:50.444584
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(1)

# Generated at 2022-06-13 20:08:56.614591
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import tempfile
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    with tempfile.TemporaryDirectory() as temp_path:
        save_file(temp_path + "/file.pkl", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        obj = load_file(temp_path + "/file.pkl")
    assert obj == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




# Generated at 2022-06-13 20:09:01.034038
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test function work_in_progress with a dummy function.
    """
    def dummy_function(x, y):
        time.sleep(1)
        return x + y

    result = work_in_progress("Add two numbers")(dummy_function)(1, 2)
    assert result == 3

# Generated at 2022-06-13 20:09:05.431932
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sub task")
    def sub_task():
        print("Doing sub task...")
        time.sleep(0.5)
        print("Sub task done")

    @work_in_progress("Task")
    def task():
        print("Doing task...")
        time.sleep(1.1)
        sub_task()
        print("Task done")

    task()

# Generated at 2022-06-13 20:09:17.037100
# Unit test for function work_in_progress
def test_work_in_progress():
    from .model import Model
    from .render import render_as_svg
    from .maps.tokyo import TokyoMap
    from .scenario import Scenario
    from .simulation import Simulation
    from . import plotter

    plotter.use_notebook()

    def f(**kwargs):
        map = TokyoMap(**kwargs)
        model = Model(map)
        scenario = Scenario(model, I=15)
        sim = Simulation(model, scenario)
        sim.run(200)
        print(sim.num_infected)

    f()

    with work_in_progress("Using mock parameters"):
        f(N=1000, d_min=1, d_max=5)

    with work_in_progress("Using full map"):
        f()


# Generated at 2022-06-13 20:09:19.048853
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Running unit tests"):
        time.sleep(1.5)

# Generated at 2022-06-13 20:09:29.280561
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    import tempfile
    import time

    def _test_work_in_progress(
        desc: str,
        obj,
    ):
        with tempfile.TemporaryDirectory() as tmp_dir_path:
            fpath = os.path.join(tmp_dir_path, "temp_file")

            @work_in_progress(desc)
            def do_work(_fpath, _obj):
                with open(_fpath, "wb") as f:
                    pickle.dump(_obj, f)

                with open(_fpath, "rb") as f:
                    return pickle.load(f)

            _obj = do_work(fpath, obj)
            assert _obj == obj


# Generated at 2022-06-13 20:09:39.156652
# Unit test for function work_in_progress
def test_work_in_progress():
    path = os.path.join(os.path.dirname(__file__), "test_work_in_progress")
    # Simple test case
    with work_in_progress("Write file"):
        with open(path + "_test0", "w") as f:
            for i in range(100):
                f.write(str(i) * 1024 * 1024 + "\n")
    # Test case with exception
    try:
        with work_in_progress("Write file"):
            raise RuntimeError
    except RuntimeError:
        pass
    else:
        raise AssertionError
    # Test case with multiple yield
    with work_in_progress("Write file"):
        with open(path + "_test1", "w") as f:
            for i in range(10):
                yield

# Generated at 2022-06-13 20:10:02.337857
# Unit test for function work_in_progress
def test_work_in_progress():

    with work_in_progress("Testing something"):
        time.sleep(1.6)

    @work_in_progress("Testing something")
    def test():
        time.sleep(2.4)

    test()

# Generated at 2022-06-13 20:10:10.761464
# Unit test for function work_in_progress
def test_work_in_progress():

    import tempfile
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path):
        with open(path, "wb") as f:
            pickle.dump(dict(a=8.2, b=["foo", "bar", "spam", "eggs"]), f)

    with tempfile.TemporaryDirectory() as tempdir:
        path = f"{tempdir}/file.obj"
        save_file(path)
        obj = load_file(path)

    assert obj == dict(a=8.2, b=["foo", "bar", "spam", "eggs"])

# Generated at 2022-06-13 20:10:13.273201
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Work in progress"):
        time.sleep(0.5)
    with work_in_progress():
        time.sleep(0.5)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:22.150837
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import os
    import tempfile

    # Create a temporary directory
    temp_dir = tempfile.TemporaryDirectory()

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    data = list(range(1_000_000))
    with work_in_progress("Saving file"):
        path = os.path.join(temp_dir.name, "data.pkl")
        with open(path, "wb") as f:
            pickle.dump(data, f)
    assert load_file(path) == data

# Generated at 2022-06-13 20:10:35.599510
# Unit test for function work_in_progress
def test_work_in_progress():
    import re
    import random
    import functools
    import contextlib
    import io

    # Generate a function that sleeps for a certain amount of time
    def sleep_func(time_to_sleep):
        @functools.wraps(sleep_func)
        def inner():
            time.sleep(time_to_sleep)
            return "ok"

        return inner

    # Generate a context manager that prints to a buffer
    buffer = io.StringIO()

    @contextlib.contextmanager
    def capture_print():
        with contextlib.redirect_stdout(buffer):
            yield

    # Create a function that calls sleep_func and captures its stdout

# Generated at 2022-06-13 20:10:42.767581
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    with open("tmp.obj", "wb") as f:
        pickle.dump({"foo": "bar"}, f)
    obj = load_file("tmp.obj")
    os.remove("tmp.obj")
    assert obj == {"foo": "bar"}

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:44.591210
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Load file"):
        time.sleep(2)

test_work_in_progress()

# Generated at 2022-06-13 20:10:50.266157
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

# Generated at 2022-06-13 20:10:58.414792
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle

    x = []
    for i in range(1000000):
        x.append(i)
    with work_in_progress("Generating 1,000,000 random integers"):
        pass

    @work_in_progress("Saving list of 1,000,000 integers")
    def save_list(path):
        with open(path, "wb") as f:
            pickle.dump(x, f)

    save_list(os.path.join(os.path.dirname(__file__), "data", "test.pickle"))

    @work_in_progress("Loading list of 1,000,000 integers")
    def load_list(path):
        with open(path, "rb") as f:
            return pickle.load(f)


# Generated at 2022-06-13 20:11:04.180977
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.123)

    @work_in_progress("Loading file")
    def load_file():
        time.sleep(0.123)

    load_file()

if __name__ == "__main__":
    test_work_in_progress()

########################################################################################################################
# Utility functions
########################################################################################################################



# Generated at 2022-06-13 20:11:51.204472
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

# Generated at 2022-06-13 20:11:55.015025
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(60)

    @work_in_progress("Saving file")
    def save_file():
        time.sleep(60)

    save_file()

# Generated at 2022-06-13 20:11:59.457077
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    test_work_in_progress()

# Generated at 2022-06-13 20:12:01.489422
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.1)

# Generated at 2022-06-13 20:12:03.620185
# Unit test for function work_in_progress
def test_work_in_progress():
    def func():
        time.sleep(1)

    with work_in_progress():
        func()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:07.577275
# Unit test for function work_in_progress
def test_work_in_progress():
    def fake_file_loading():
        time.sleep(1)

    def fake_file_saving():
        time.sleep(1.5)

    with work_in_progress("Unit test") as t:
        fake_file_loading()
        fake_file_saving()
    assert 1, t
    print(f"Time consumed: {t}")

test_work_in_progress()

# Generated at 2022-06-13 20:12:13.461851
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

# Generated at 2022-06-13 20:12:16.071872
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing function work_in_progress"):
        time.sleep(3)

# Generated at 2022-06-13 20:12:22.265445
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
    save_file("/path/to/some/other/file", obj)

# Generated at 2022-06-13 20:12:26.454229
# Unit test for function work_in_progress
def test_work_in_progress():
    from time import sleep

    @work_in_progress("Loading file")
    def load_file(path):
        sleep(1)
        return 0

    data = load_file("/path/to/nonexist/file")
    assert data == 0

    with work_in_progress("Saving file"):
        sleep(1)



# Generated at 2022-06-13 20:14:03.357464
# Unit test for function work_in_progress
def test_work_in_progress():
    import numpy as np

    # Test function
    @work_in_progress("Testing work_in_progress")
    def demo():
        # Doing something here
        arr = np.random.randn(1000, 1000)
        res = np.linalg.det(arr)
        return res

    # Test method
    class MyClass:
        def __init__(self):
            self.arr = np.random.randn(1000, 1000)

        @work_in_progress("Testing work_in_progress")
        def demo(self):
            res = np.linalg.det(self.arr)
            return res

    res1 = demo()
    obj = MyClass()
    res2 = obj.demo()

    # Test context manager

# Generated at 2022-06-13 20:14:08.834781
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert obj

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    assert os.path.exists(path)

# Generated at 2022-06-13 20:14:12.321780
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress():
        time.sleep(2)
    with work_in_progress("Saving file"):
        time.sleep(3)
    with work_in_progress("Loading file"):
        time.sleep(4)
    with work_in_progress():
        time.sleep(5)
    with work_in_progress("Saving file"):
        time.sleep(6)

# Generated at 2022-06-13 20:14:15.309166
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sleeping for a while before returning")
    def sleep_first():
        time.sleep(2)
        return "sleep"

    assert sleep_first() == "sleep"

# Generated at 2022-06-13 20:14:23.594652
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test the function load_file
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Loading file"):
        load_file("/path/to/some/file")

    # Test the with syntax
    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:24.769102
# Unit test for function work_in_progress

# Generated at 2022-06-13 20:14:30.271287
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        with open("/path/to/some/file", "rb") as f:
            obj = pickle.load(pickle.load(f))

    @work_in_progress("Saving file")
    def load_file(path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        return obj

    obj = load_file("/path/to/some/file")

# Generated at 2022-06-13 20:14:36.346843
# Unit test for function work_in_progress
def test_work_in_progress():
    from unittest.mock import Mock
    from unittest import TestCase
    from io import StringIO

    # Capture print()'s stdout
    captured_output = StringIO()                  # Create StringIO object
    sys.stdout = captured_output                 # and redirect sys.stdout.
    # Test execution of a code block
    with work_in_progress():
        time.sleep(2)
    TestCase().assertEqual(captured_output.getvalue(), "Work in progress... done. (2.00s)\n")
    # Test execution of a function
    mock = Mock(return_value=None)
    @work_in_progress
    def work():
        mock()
    work()

# Generated at 2022-06-13 20:14:41.955320
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:14:56.741848
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("../tests/test_work_in_progress.pkl")

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    save_file("../tests/test_work_in_progress_out.pkl", obj)


if __name__ == "__main__":
    test_work_in_progress()
    """
    Loading file... done. (0.01s)
    Saving file... done. (0.00s)
    """