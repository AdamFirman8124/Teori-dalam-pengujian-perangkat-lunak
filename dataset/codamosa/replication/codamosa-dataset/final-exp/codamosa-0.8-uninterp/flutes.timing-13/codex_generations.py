

# Generated at 2022-06-13 20:05:20.905532
# Unit test for function work_in_progress
def test_work_in_progress():

    @work_in_progress("Test")
    def test():
        time.sleep(0.2)

    test()


# Generated at 2022-06-13 20:05:31.392387
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

    obj = {"foo": [1, 2, 3], "bar": [4, 5, 6]}

    with tempfile.NamedTemporaryFile(suffix=".pkl", delete=True) as f:
        save_file(f.name, obj)
        assert pickle.load(f) == obj


# Generated at 2022-06-13 20:05:33.643207
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Counting sheeps")
    def func(n):
        for i in range(n):
            for j in range(n):
                pass
    func(1000)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:39.000110
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("test/test.file")
    with work_in_progress("Saving file"):
        with open("test/test.file", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:43.117416
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function `work_in_progress`.
    """
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:05:45.625173
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert isinstance(obj, dict)

# Generated at 2022-06-13 20:05:50.347107
# Unit test for function work_in_progress
def test_work_in_progress():
    for _ in range(3):
        with work_in_progress():
            time.sleep(0.5)
            print("Hello, world!")
    with work_in_progress("In progress"):
        time.sleep(0.5)
        print("Hello, world!")

# Generated at 2022-06-13 20:05:55.721364
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



# Generated at 2022-06-13 20:05:58.875047
# Unit test for function work_in_progress
def test_work_in_progress():
    # test with a function
    @work_in_progress("Loading")
    def load():
        time.sleep(1.3)
    load()

    # test with a with statement
    with work_in_progress("Saving"):
        time.sleep(1.3)

# Generated at 2022-06-13 20:06:01.675030
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(1)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 20:06:07.789860
# Unit test for function work_in_progress
def test_work_in_progress():
    # Case 1
    with work_in_progress("Loading file"):
        time.sleep(1.5)
    # Case 2
    @work_in_progress("Saving file")
    def save_file():
        time.sleep(1.5)
    save_file()

# Generated at 2022-06-13 20:06:13.060791
# Unit test for function work_in_progress
def test_work_in_progress():
    r = [1]
    with work_in_progress("Adding number to list"):
        r.append(2)
    with work_in_progress("Adding number to list"):
        for i in range(10000):
            r.append(i)
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:17.415254
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        print("Saving the file...")
        time.sleep(1)
        print("Done.")
        time.sleep(1)
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:19.776807
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.5)

# Generated at 2022-06-13 20:06:21.965536
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing..."):
        time.sleep(1.5)


if __name__ == '__main__':
    for name, func in globals().items():
        if name.startswith("test_"):
            func()

# Generated at 2022-06-13 20:06:24.329626
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    def test_function(*args, **kwargs):
        time.sleep(1)

    with work_in_progress("Test work in progress") as _:
        test_function()

# Generated at 2022-06-13 20:06:32.532975
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import random
    import string

    def rand_string(l: int = 20) -> str:
        alpha = string.ascii_lowercase
        return ''.join(random.choice(alpha) for _ in range(l))

    def print_text(text: str, delay: float = 0.01) -> None:
        print(text, end='', flush=True)
        time.sleep(delay)
        print("\b" * len(text), end='', flush=True)

    for _ in range(10):
        text = f"[{rand_string()}]"
        print(text, end='', flush=True)
        with work_in_progress():
            print_text("a")
            print_text("b")
            print_text("c")
            print_text("d")
           

# Generated at 2022-06-13 20:06:39.424047
# Unit test for function work_in_progress
def test_work_in_progress():

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:44.027617
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing function")
    def dummy():
        time.sleep(5.0)
    dummy()
    dummy()
    dummy()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:50.840807
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import tempfile
    import time

    def _test_work_in_progress():
        with work_in_progress("Loading file"):
            time.sleep(0.2)
        with work_in_progress("Saving file"):
            time.sleep(0.3)
        with work_in_progress("Saving file"):
            pass

    def _test_work_in_progress_nested():
        with work_in_progress("Loading file"):
            with work_in_progress("Loading smaller file"):
                pass
            time.sleep(0.2)

    with tempfile.TemporaryDirectory() as base_dir:
        path = os.path.join(base_dir, "file")
        with open(path, "wb") as f:
            pass


# Generated at 2022-06-13 20:07:02.666875
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test module-level function work_in_progress.

    This function will decorate function `load_file()` with `work_in_progress`.
    """
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

    doctest.testmod()

# Generated at 2022-06-13 20:07:09.388655
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

    obj1 = load_file(__file__)
    save_file(__file__ + ".cp", obj1)

# Generated at 2022-06-13 20:07:14.903722
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

# Generated at 2022-06-13 20:07:19.021549
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("__init__.py")

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 20:07:25.615965
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    obj = {
        "name": "foo",
        "age": -1,
    }

    with work_in_progress("Loading test object"):
        obj2 = pickle.loads(pickle.dumps(obj))
        assert obj == obj2


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:30.382065
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    @work_in_progress("I'm busy")
    def a_function():
        time.sleep(1)

    with work_in_progress("I'm busy"):
        time.sleep(1)

    a_function()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:38.622747
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    """
    Loading file... done. (3.52s)
    """

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    """
    Saving file... done. (3.78s)
    """

# Generated at 2022-06-13 20:07:40.434370
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test description")
    def test():
        time.sleep(2)
    test()

# Generated at 2022-06-13 20:07:42.959382
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.34)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:07:49.856805
# Unit test for function work_in_progress
def test_work_in_progress():
    # case 1
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(1)
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert obj

    # case 2
    with work_in_progress("Saving file"):
        time.sleep(1)
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    assert True

if __name__ == '__main__':
    import pytest
    pytest.main(["-vv", "--durations=10", __file__])

# Generated at 2022-06-13 20:08:01.039977
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path, delay = 0.2):
        with open(path, "rb") as f:
            time.sleep(delay)
            return pickle.load(f)

    with open("test.pickle", "wb") as f:
        pickle.dump([1, 2, 3], f)

    with work_in_progress("Loading file"):
        r = load_file("test.pickle")
    assert r == [1, 2, 3]

# Generated at 2022-06-13 20:08:03.768795
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def f():
        time.sleep(3.1)
    f()

# Generated at 2022-06-13 20:08:18.934187
# Unit test for function work_in_progress
def test_work_in_progress():

    import time
    import pickle

    class SomeClass:
        def __init__(self, a: int, b: int):
            self.a = a
            self.b = b

    with work_in_progress("Loading file"):
        obj = pickle.load(open("test_pickle.pkl", "rb"))

    with work_in_progress("Saving object"):
        time.sleep(2)
        with open("test_pickle.pkl", "wb") as f:
            pickle.dump(obj, f)

    with work_in_progress("Saving object"):
        time.sleep(1)
        with open("test_pickle.pkl", "wb") as f:
            pickle.dump(obj, f)


# Generated at 2022-06-13 20:08:23.508607
# Unit test for function work_in_progress
def test_work_in_progress():
    """
    Unit test for function work_in_progress. The test is simply printing
    a message with a certain time precision.
    """
    with work_in_progress("Saving file"):
        time.sleep(3.141592)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:27.898205
# Unit test for function work_in_progress
def test_work_in_progress():
    import random

    random.seed(42)
    for i in range(4):
        j = random.randint(1, 100)
        with work_in_progress(f"Iteration {i}"):
            time.sleep(j)

    time.sleep(.5)

    with work_in_progress():
        time.sleep(.5)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:36.755559
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    print()

    def sleep_for(sec):
        time.sleep(sec)

    with work_in_progress("Task 1"):
        sleep_for(1)

    print()
    with work_in_progress("Task 2"):
        sleep_for(2)


if __name__ == '__main__':
        test_work_in_progress()

# Generated at 2022-06-13 20:08:46.850590
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys
    import io
    import time
    import contextlib
    import unittest

    @contextlib.contextmanager
    def captured_output(desc):
        """Capture stdout"""
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err


# Generated at 2022-06-13 20:08:48.441492
# Unit test for function work_in_progress
def test_work_in_progress():
    assert 1==1
	
if __name__ == '__main__':
	test_work_in_progress()

# Generated at 2022-06-13 20:08:51.635929
# Unit test for function work_in_progress
def test_work_in_progress():
    def fake_fn():
        time.sleep(1)

    with work_in_progress(desc="Testing work_in_progress") as bc:
        fake_fn()
    assert(True)

# Generated at 2022-06-13 20:08:53.322125
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test function"):
        time.sleep(1)
    pass

# Generated at 2022-06-13 20:09:04.130046
# Unit test for function work_in_progress
def test_work_in_progress():
    # Setup
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        path = "file"
        obj = {0: 1, 2: 3}

        # Test saving of file
        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)

        # Test loading of file
        @work_in_progress("Loading file")
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        loaded_obj = load_file(path)

        # Assertions
        assert obj == loaded_obj

if __name__ == "__main__":
    from pytest import main
    main([__file__])

# Generated at 2022-06-13 20:09:06.880431
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Test work_in_progress")
    with work_in_progress("Test context manager"):
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:08.880617
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing module"):
        time.sleep(1)

# Generated at 2022-06-13 20:09:12.484784
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(3)
    print("done.")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:15.906870
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("This is a test"):
        time.sleep(1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:09:17.756671
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Sleeping..."):
        time.sleep(3)
    assert True

# Generated at 2022-06-13 20:09:24.149624
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function work_in_progress.
    """
    begin_time = time.time()
    with work_in_progress("Test progress"):
        time.sleep(0.1)
    time_consumed = time.time() - begin_time
    assert time_consumed >= 0.1, "work_in_progress() does not work properly"
    print("test_work_in_progress() passed")

# Generated at 2022-06-13 20:09:29.211511
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "r") as f:
            return f.read()

    with work_in_progress("Saving file"):
        with open("/tmp/example.txt", "w") as f:
            f.write("This is a test.")

    assert load_file("/tmp/example.txt") == "This is a test."

# Generated at 2022-06-13 20:09:36.224395
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

# Generated at 2022-06-13 20:09:43.680462
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import tempfile
    import pickle
    import random
    import shutil
    import subprocess

    # Generate the random object to save
    obj = random.random()

    # Create a temporary directory and path to save the result
    temp_d = tempfile.mkdtemp()
    tmp_path = os.path.join(temp_d, "save.pkl")

    # Create the bash snippet to run in subprocess
    # It will simply run the Python built-in function `pickle.dump` in
    # "with work_in_progress" block.
    cmd = f"""
        import pickle
        with open(r"{tmp_path}", "wb") as f:
            with work_in_progress("Saving file"):
                pickle.dump({obj}, f)
    """

    #

# Generated at 2022-06-13 20:09:50.540724
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def test():
        time.sleep(2)

    test()

# Generated at 2022-06-13 20:10:00.090676
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress.

    Note:
        If the file "/path/to/some/file" does not exist,
        it will raise a FileNotFoundError.

    :return: None
    """

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:10:06.726485
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress
    """
    # Create a file on disk
    with open("test.txt", "w") as fout:
        fout.write("test")

    def read_file(path):
        with open(path, "r") as fin:
            return fin.read()

    with work_in_progress("Reading file"):
        content = read_file("test.txt")

    assert content == "test"


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:09.243939
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file") as w:
        time.sleep(1)
    with work_in_progress("Saving file") as w:
        time.sleep(1)



# Generated at 2022-06-13 20:10:13.714044
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.5)
    with work_in_progress("Saving file"):
        time.sleep(0.5)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_work_in_progress()

# Generated at 2022-06-13 20:10:21.397454
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    path = os.path.join(os.path.dirname(__file__), "..", "..", "README.rst")
    with work_in_progress("Saving file"):
        with open(path, "rb") as f:
            return pickle.load(f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:21.970186
# Unit test for function work_in_progress
def test_work_in_progress():
    pass

# Generated at 2022-06-13 20:10:25.910119
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Working"):
        time.sleep(0.5)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:31.061519
# Unit test for function work_in_progress
def test_work_in_progress():
    # save current working directory
    cwd = os.getcwd()
    # change the current working directory to the directory containing
    # the test file, so that the file created in the following functions
    # will be under the same directory and can be easily removed
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Test 1
    # create test file
    open(os.path.join(os.path.dirname(__file__), "test_work_in_progress.bin"), "wb").close()
    assert os.path.exists(os.path.join(os.path.dirname(__file__), "test_work_in_progress.bin"))
    # run function to delete the test file
    with work_in_progress("Deleting test file"):
        os

# Generated at 2022-06-13 20:10:34.180952
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Calculating pi")
    def calc_pi():
        time.sleep(.35)
    calc_pi()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:10:55.008630
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @contextlib.contextmanager
    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    path = "/tmp/work_in_progress.tmp"

    if os.path.exists(path):
        os.remove(path)


# Generated at 2022-06-13 20:11:05.107564
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile
    import pickle

    def do_work():
        data = []
        for _ in range(100):
            data.append(1)
            time.sleep(0.01)
        return data

    d = do_work()

    # Save data to temporary file
    with work_in_progress():
        f = tempfile.NamedTemporaryFile(delete=False)
        f1 = f.name
        pickle.dump(d, f)
        f.close()

    # Load data from temporary file
    with work_in_progress():
        f = open(f1, "rb")
        d1 = pickle.load(f)
        f.close()

    assert d == d1

# Generated at 2022-06-13 20:11:10.338369
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

# Generated at 2022-06-13 20:11:15.781116
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Sleeping for 2 seconds"):
        time.sleep(2)



# Script execution
if __name__ == "__main__":
    print(__doc__)
    print(f"Run \"pydoc {__file__}\" for more details.")

# Generated at 2022-06-13 20:11:22.215697
# Unit test for function work_in_progress
def test_work_in_progress():
    import pytest
    from .test_utils import capfd

    def test_function():
        time.sleep(0.2)

    with capfd.disabled():
        with work_in_progress("Testing work_in_progress"):
            test_function()

        @work_in_progress("Testing work_in_progress")
        def test_function_decorated():
            time.sleep(0.2)

        test_function_decorated()

    with capfd.disabled():
        with pytest.raises(AttributeError):
            @work_in_progress
            def test_function_no_args():
                time.sleep(0.2)
        test_function_no_args()

# Generated at 2022-06-13 20:11:29.854150
# Unit test for function work_in_progress
def test_work_in_progress():

    import filecmp
    import os
    import shutil
    import tempfile

    dest = None
    src = None

# Generated at 2022-06-13 20:11:33.439299
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Downloading file"):
        time.sleep(1.23)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:38.879782
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Testing function \"work_in_progress\"... ", end='', flush=True)
    @work_in_progress("Testing work_in_progress")
    def func1():
        time.sleep(0.3)
    func1()
    try:
        with work_in_progress("Testing work_in_progress"):
            time.sleep(0.3)
    except:
        pass
    print("done.")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:40.301332
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1.23)
    assert True

# Generated at 2022-06-13 20:11:51.202295
# Unit test for function work_in_progress
def test_work_in_progress():
    my_path = "/path/to/my/file"
    my_obj = [random.random() for i in range(10000)]

    with work_in_progress("Loading file"):
        with open(my_path, "rb") as f:
            my_obj = pickle.load(f)
    assert isinstance(my_obj, list)
    for i in range(len(my_obj)):
        assert isinstance(my_obj[i], float)

    with work_in_progress("Saving file"):
        with open(my_path, "wb") as f:
            pickle.dump(my_obj, f)
    assert isinstance(my_obj, list)
    for i in range(len(my_obj)):
        assert isinstance(my_obj[i], float)



# Generated at 2022-06-13 20:12:16.695754
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(0.6)
    with work_in_progress("Loading file"):
        time.sleep(0.6)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:22.815152
# Unit test for function work_in_progress
def test_work_in_progress():
    # fake functions
    def fake_load_file(path):
        time.sleep(1)
        return
    def fake_save_file(path):
        time.sleep(1)
        return

    # fake code blocks
    with work_in_progress("Loading file"):
        obj = fake_load_file("/path/to/some/file")
    # fake code block with callable obj
    with work_in_progress("Saving file"):
        fake_save_file("/path/to/some/file")

# Generated at 2022-06-13 20:12:28.890406
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    import pickle
    import types
    import pytest
    import tempfile

    def test_func():
        raise NotImplementedError()

    # Test context manager
    with tempfile.TemporaryDirectory() as tmpdir:
        path = tmpdir+"/test.pkl"
        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(test_func, f)
        with work_in_progress("Loading file"):
            with open(path, "rb") as f:
                func = pickle.load(f)
        with pytest.raises(NotImplementedError):
            func()
    assert isinstance(func, types.FunctionType)

    # Test decorator

# Generated at 2022-06-13 20:12:39.890180
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    from contextlib import redirect_stdout

    class Dummy:
        pass

    obj = Dummy()
    obj.x = "My name is Groot."

    with redirect_stdout(sys.stdout):
        # block
        begin_time = time.time()
        with work_in_progress("Saving file"):
            with open("./test.pkl", "wb") as f:
                pickle.dump(obj, f)
        time_consumed = time.time() - begin_time
        assert time_consumed > 0.5, f"Execution time is too short ({time_consumed:.2f}s)"

        # function
        def load_file(path):
            begin_time = time.time()

# Generated at 2022-06-13 20:12:44.262642
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Default behavior"):
        time.sleep(1)

    with work_in_progress("Before yield"):
        print("Before yield")
        time.sleep(1)

    with work_in_progress("After yield"):
        time.sleep(1)
        print("After yield")

    with work_in_progress("Custom description"):
        time.sleep(1)

# Generated at 2022-06-13 20:12:47.991612
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:50.890948
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Task 1"):
        time.sleep(0.15)
    with work_in_progress("Task 2") as w:
        for i in range(100):
            w.set_description(f"Task {i}")
            time.sleep(0.01)

#------------------------------------------------------------------------------

if __name__ == "__main__":

    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:13:02.657026
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    def test_file_loading():
        obj = load_file("/path/to/some/file")

    def test_file_saving(obj):
        save_file(obj, "/path/to/some/file")
    # -- End of function test_work_in_progress --



# Generated at 2022-06-13 20:13:10.104538
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile
    import os
    import pickle
    from .testing import timethis
    desc = "Tesing work_in_progress"
    obj = {}
    with work_in_progress(desc):
        with open(os.devnull, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    assert timethis(lambda: pickle.dump(obj, os.devnull, pickle.HIGHEST_PROTOCOL)) > 0
    with work_in_progress(desc):
        with open(os.devnull, "rb") as f:
            pickle.load(f)
    assert timethis(lambda: pickle.load(os.devnull)) > 0

# Generated at 2022-06-13 20:13:20.122476
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile

    obj = {'a': 'b'}

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'test')
        with open(path, 'wb') as f:
            pickle.dump(obj, f)
        loaded = load_file(path)
        assert loaded == obj

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path

# Generated at 2022-06-13 20:14:04.557818
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.5)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:11.490658
# Unit test for function work_in_progress
def test_work_in_progress():

    # Simple test
    with work_in_progress("Loading file"):
        with open("test/test.pkl", "rb") as f:
            pickle.load(f)

    # Test nested work_in_progress
    @work_in_progress("Nested work_in_progress")
    def nested_work_in_progress(a, b):
        with work_in_progress("Adding two numbers"):
            return a + b

    assert nested_work_in_progress(1, 2) == 3

    # Test lambda function
    @work_in_progress("Lambda function")
    def f(x):
        return lambda y: work_in_progress("Multiplying two numbers")(x * y)

    assert f(2)(3) == 6

# Generated at 2022-06-13 20:14:17.734628
# Unit test for function work_in_progress
def test_work_in_progress():
    assert "done" in work_in_progress(
        desc="Unit test for function work_in_progress").__enter__()()
    assert "done" in work_in_progress().__enter__()()


if __name__ == "__main__":
    # Run all tests
    for name, obj in globals().items():
        if name.startswith("test_") and callable(obj):
            obj()

# Generated at 2022-06-13 20:14:24.150756
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

# Generated at 2022-06-13 20:14:26.207738
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def work():
        time.sleep(0.4)
    work()

# Generated at 2022-06-13 20:14:33.444468
# Unit test for function work_in_progress
def test_work_in_progress():
    """ Unit test for function work_in_progress """
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/file")
    time.sleep(3)

    with work_in_progress("Saving file"):
        with open("/path/to/file", "wb") as f:
            pickle.dump(obj, f)
        time.sleep(3)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:38.740642
# Unit test for function work_in_progress
def test_work_in_progress():  # noqa
    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump({'a': 1, 'b': 2}, f)


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # noqa

# Generated at 2022-06-13 20:14:47.126750
# Unit test for function work_in_progress
def test_work_in_progress():
    class Foo:
        def __init__(self, path):
            self.path = path
            print(f"Loading file {path}...", end='', flush=True)
            time.sleep(1.34)
            print(f"done. ({time_consumed:.2f}s)")

    f = Foo("some_file.txt")
    assert f.path == "some_file.txt"

    path = "another_file.txt"
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(path)
    assert isinstance(obj, dict)

# Generated at 2022-06-13 20:14:59.816556
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import random

    with work_in_progress("Wait"):
        time.sleep(0.5)

    @work_in_progress("Wait")
    def wait(sec):
        time.sleep(sec)

    wait(0.5)

    @work_in_progress("Infinite loop")
    def loop():
        while True:
            pass

    try:
        loop()
    except KeyboardInterrupt:
        print("\nCaught KeyboardInterrupt. Stopping loop.")

    @work_in_progress("Random work")
    def work(sec):
        time.sleep(sec)

    work(random.random() * 0.5)


# Entry point for bingo
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:15:06.248995
# Unit test for function work_in_progress
def test_work_in_progress():
    def read_file(fn: str) -> str:
        with open(fn, "r") as f:
            return f.read()

    with work_in_progress("Reading file"):
        read_file("../LICENSE")


if __name__ == "__main__":
    test_work_in_progress()