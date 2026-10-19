

# Generated at 2022-06-13 20:05:25.058049
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with open(__file__, "rb") as f:
        pickle_data = pickle.dumps(f.read())
        temp_file_path = tempfile.mktemp()
        with open(temp_file_path, "wb") as ft:
            ft.write(pickle_data)
        obj = load_file(temp_file_path)
        os.remove(temp_file_path)
        os.remove(temp_file_path + 'c')

    with work_in_progress("Saving file"):
        temp_file_path = tempfile.mktemp()

# Generated at 2022-06-13 20:05:33.504039
# Unit test for function work_in_progress
def test_work_in_progress():
    from os.path import join
    from tempfile import mkstemp
    import random
    import pickle
    from .context import ctx, log, warn, error
    from . import Str, Path, TxtFile, PyFile, ctx
    from .test import test_in_tmpdir
    from .test import skip_if, skip_unless

    # TODO: check stdout
    def test_work_in_progress_context_manager(ctx):

        with ctx.cd(TmpDir):

            Path("A.txt").touchn()
            Path("A.py").touchn()

            with work_in_progress("Printing file status"):
                Str(ctx.cmd("du --human-readable A.txt A.py")).to_file("status.txt")


# Generated at 2022-06-13 20:05:37.459610
# Unit test for function work_in_progress
def test_work_in_progress():
    test_desc = "Test Work in progress"

    def test_function():
        with work_in_progress(test_desc):
            time.sleep(3)
    def test_context_manager():
        with work_in_progress(test_desc):
            time.sleep(3)

    test_function()
    test_context_manager()

# Generated at 2022-06-13 20:05:40.545469
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test function ``work_in_progress``"""
    def test_deco():
        @work_in_progress("Decorator")
        def test_work_deco():
            time.sleep(0.125)

        test_work_deco()

    def test_block():
        with work_in_progress("Block"):
            time.sleep(0.125)

    test_deco()
    test_block()

# Generated at 2022-06-13 20:05:52.505389
# Unit test for function work_in_progress
def test_work_in_progress():
    tmpfile = os.path.join(os.path.dirname(__file__), "tmpfile.pkl")
    with work_in_progress("Deleting file") as _:
        try:
            os.remove(tmpfile)
        except:
            pass

    # Test context manager
    with work_in_progress("Working..."):
        time.sleep(1.5)

    # Test decorator
    @work_in_progress("Working...")
    def _(x):
        time.sleep(1.5)
        return x * 2
    _(1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:01.735954
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    import tempfile
    tmp_dir = tempfile.gettempdir()
    file_path = os.path.join(tmp_dir, "test_work_in_progress.pickle")
    with work_in_progress("Creating some file"):  # doctest: +SKIP
        with open(file_path, "wb") as f:
            pickle.dump(object(), f)  # Create a file

# Generated at 2022-06-13 20:06:05.916817
# Unit test for function work_in_progress
def test_work_in_progress():
    path = "./test_work_in_progress.pickle"

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    with contextlib.suppress(FileNotFoundError):
        os.remove(path)

    obj = load_file(path)
    save_file(path)
    obj = load_file(path)
    os.remove(path)

# Generated at 2022-06-13 20:06:10.405434
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpfile = os.path.join(tmpdir, f"{int(time.time())}.txt")
        with open(tmpfile, "w") as f:
            f.write("Hello world!")
        with work_in_progress("Reading file"):
            with open(tmpfile, "r") as f:
                s = f.read()
        assert s == "Hello world!", "The file was read incorrectly."

# Execute doctest if executed from commandline
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:06:12.770982
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Test work_in_progress()"
    with work_in_progress(desc):
        time.sleep(1)
    assert True

# test_work_in_progress()

# Generated at 2022-06-13 20:06:17.088501
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
        with work_in_progress("Loading another file"):
            time.sleep(2)
    with work_in_progress("Loading yet another file"):
        time.sleep(3)

# Generated at 2022-06-13 20:06:23.696078
# Unit test for function work_in_progress
def test_work_in_progress():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        with work_in_progress("Loading file"):
            time.sleep(0.0014)
        buf.flush()
        assert buf.getvalue() == "Loading file... done. (0.00s)\n"


# Generated at 2022-06-13 20:06:32.482929
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Just a unit test for this function.
    """
    import pickle


    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)


    class SomeClass():
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)


    with open("/tmp/test_wip.pkl", "wb") as f:
        pickle.dump(SomeClass(**{
            "a": 1,
            "b": 2,
            "c": 3,
        }), f)

    obj = load_file("/tmp/test_wip.pkl")


# Generated at 2022-06-13 20:06:36.310937
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading data")
    def load_data(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    assert True

# Generated at 2022-06-13 20:06:41.203053
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:47.874800
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

# Generated at 2022-06-13 20:06:53.690253
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Processing file")
    def process_file(f):
        return {i: i * i for i in f}

    @work_in_progress("Saving file")
    def save_file(f, path):
        with open(path, "wb") as g:
            pickle.dump(f, g)

    with stdout_redirected():
        obj = load_file(__file__)
        with work_in_progress("Processing file"):
            obj = process_file(obj)
        save_file(obj, __file__ + ".test")

# Generated at 2022-06-13 20:06:56.347490
# Unit test for function work_in_progress
def test_work_in_progress():
    for _ in range(1000):
        with work_in_progress("Work in progress"):
            time.sleep(0.01)

# Generated at 2022-06-13 20:06:59.254868
# Unit test for function work_in_progress
def test_work_in_progress():
    print("This is a unit test for module `utils.timer`. The following message should be displayed.")
    @work_in_progress
    def do_nothing():
        pass
    do_nothing()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:00.939182
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing..."):
        time.sleep(0.5)
    assert True

# Generated at 2022-06-13 20:07:07.146141
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    def time_consuming_task():
        time.sleep(0.5)

    # Mock the stdout
    with contextlib.redirect_stdout(io.StringIO()) as buf:
        with work_in_progress("Time consuming task"):
            time_consuming_task()

    # Verify the output of work_in_progress
    assert buf.getvalue().split("... ")[0] == "Time consuming task"

# Generated at 2022-06-13 20:07:11.887680
# Unit test for function work_in_progress
def test_work_in_progress():
    done = False
    with work_in_progress():
        time.sleep(1.5)
        done = True
    assert done == True, "Test for work_in_progress not passed"


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:19.119554
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

    data = [1, 2, 3]
    name = "Test"
    path = "test.pickle"
    save_file(data, path)
    assert load_file(path) == data

test_work_in_progress()

# Generated at 2022-06-13 20:07:20.519512
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.1)

# Generated at 2022-06-13 20:07:29.119596
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test using function
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    print(f"Object type: {type(obj)}")

    # Test using context manager
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)



# Generated at 2022-06-13 20:07:31.961581
# Unit test for function work_in_progress
def test_work_in_progress():
    begin_time = time.time()
    with work_in_progress("Task"):
        time.sleep(2)
    assert time.time() - begin_time >= 2

# Generated at 2022-06-13 20:07:35.875762
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading")
    def _():
        time.sleep(3)
    _()

    with work_in_progress("Saving"):
        time.sleep(4)

# Generated at 2022-06-13 20:07:43.535754
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Conditioning data")
    def condition_data(data):
        for row in data:
            for i, el in enumerate(row):
                yield (i, el)
    list(condition_data(
            [
                [0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9],
                [10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19],
            ]
        )
    )


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:07:48.162898
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

    import os
    os._exit(0)

# Generated at 2022-06-13 20:07:55.916197
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test for a context manager
    with work_in_progress("Saving file"):
        time.sleep(1.111)
    # Test for a function decorator
    @work_in_progress("Loading file")
    def load_file():
        time.sleep(3.123)
        return "a"
    load_file()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:05.305492
# Unit test for function work_in_progress
def test_work_in_progress():
    print("=> Testing work_in_progress()...")
    fail_count = 0

    print("Case 1: TypeError in the first line of code block")
    try:
        with work_in_progress("Case 1"):
            a = 1 + "string" # TypeError
            with open("/path/to/file/that/does/not/exist", "rb") as f:
                pass
            a = 1 + "string" # TypeError
    except TypeError:
        fail_count += 1
    print("Case 1 failed: {}".format(fail_count))

    print("Case 2: FileNotFoundError in the second line of code block")

# Generated at 2022-06-13 20:08:17.622265
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test_work_in_progress.tmp")

        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump({1, 2, 3}, f)

        with work_in_progress("Loading file"):
            with open(path, "rb") as f:
                pickle.load(f)

# Generated at 2022-06-13 20:08:26.512064
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    path = "/path/to/some/file"
    obj = [2, 3, 5, 7, 11, 13, 17, 19]

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(obj):
        with open(path, "wb") as f:
            return pickle.dump(obj, f)

    obj_copy = load_file(path)
    assert obj_copy == obj
    save_file(obj)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:36.313538
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    path = os.path.abspath(os.path.join(".", "test_work_in_progress.pkl"))

    with work_in_progress("Loading file") as _:
        obj = load_file(path)
    assert obj == ["TEST", "TEST", "TEST"]

    with work_in_progress("Saving file") as _:
        save_file(["TEST", "TEST", "TEST"], path)

    os.remove(path)
    print("Passed test_work_in_progress.")




# Generated at 2022-06-13 20:08:38.222538
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Doing something"):
        time.sleep(0)

# Generated at 2022-06-13 20:08:39.805672
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)


# Generated at 2022-06-13 20:08:42.781793
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(1)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE))
    test_work_in_progress()

# Generated at 2022-06-13 20:08:46.970052
# Unit test for function work_in_progress
def test_work_in_progress():
    def f():
        time.sleep(3)

    with work_in_progress("Testing"):
        f()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:54.420148
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys
    import io
    import time
    from io import StringIO
    from os import path

    from . import work_in_progress

    class CaptureStdout(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO()
            return self
        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio    # free up some memory
            sys.stdout = self._stdout

    class CaptureStderr(list):
        def __enter__(self):
            self._stderr = sys.stderr
            sys.stderr = self._stringio = StringIO()
            return self

# Generated at 2022-06-13 20:09:00.094257
# Unit test for function work_in_progress
def test_work_in_progress():
    from test.unitest import assert_
    from time import sleep

    with work_in_progress("Task A") as work_a:
        sleep(1)
        work_a.do_something(1)
        sleep(2)

    for i in range(3):
        with work_in_progress() as work_b:
            sleep(i)
            work_b.do_something(i)

    assert_(True, "Test passed.")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:04.161681
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    assert load_file("/path/to/some/file") == pickle.reconstruct({"a": 1})

# Generated at 2022-06-13 20:09:25.769738
# Unit test for function work_in_progress
def test_work_in_progress():
    def test_func():
        with open(__file__, "rb") as f:
            data = f.read()
        return data

    with work_in_progress("Test work_in_progress"):
        result = test_func()

    assert len(result) == 2612
    assert result.startswith(b"# Unit test for function work_in_progress\n")

    @work_in_progress("Test work_in_progress")
    def test_func2():
        with open(__file__, "rb") as f:
            data = f.read()
        return data

    result = test_func2()
    assert len(result) == 2612
    assert result.startswith(b"# Unit test for function work_in_progress\n")



# Generated at 2022-06-13 20:09:30.633663
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("C:/Users/pc/Documents/Work/code/python/utils/__init__.py")

    with work_in_progress("Saving file"):
        with open("./__init__.py.bak", "wb") as f:
            pickle.dump(obj, f)



# Generated at 2022-06-13 20:09:35.610673
# Unit test for function work_in_progress
def test_work_in_progress():
    print()
    print(f"=== test_work_in_progress() ===")

    with work_in_progress("Test case 1"):
        print(1)
        time.sleep(2)
        print(2)

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Test case 2")
    def load():
        print(1)
        time.sleep(2)
        print(2)

    obj = load_file("/path/to/some/file")
    load()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:40.303483
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)
    assert isinstance(obj, list)

    with work_in_progress("Saving file"):
        with open(__file__, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:09:45.208792
# Unit test for function work_in_progress
def test_work_in_progress():
    obj = {"k": "v"}
    with work_in_progress("Saving file"):
        with open("temp", "wb") as f:
            pickle.dump(obj, f)
    assert pickle.load(open("temp", "rb")) == obj
    os.remove("temp")

# Generated at 2022-06-13 20:09:47.322617
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress"):
        time.sleep(1)

# Generated at 2022-06-13 20:09:50.339892
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Doing something")
    def do_something():
        time.sleep(1)
    do_something()

    with work_in_progress("Doing another thing"):
        time.sleep(2)

# Generated at 2022-06-13 20:09:59.585767
# Unit test for function work_in_progress
def test_work_in_progress():
    # This is not intended to be run as a unit test.
    # The code below is to visualize the usage of this function.
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = load_file(__file__)
    save_file(obj, "/tmp/test.pkl")

# Generated at 2022-06-13 20:10:02.781873
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sample task")
    def test_task():
        time.sleep(3)

    with work_in_progress("Sample task"):
        time.sleep(3)

    test_task()

# Generated at 2022-06-13 20:10:11.039856
# Unit test for function work_in_progress
def test_work_in_progress():
    import gc

    # Test 1: Test for a code block
    with work_in_progress("Test 1"):
        time.sleep(1)
    # Output: Test 1... done. (1.00s)

    # Test 2: Test for a function
    @work_in_progress("Test 2")
    def test():
        time.sleep(1)
    # Output: Test 2... done. (1.00s)
    test()

    # Test 3: Test for function with argument passed
    @work_in_progress("Test 3")
    def test(a):
        time.sleep(1)
    # Output: Test 3... done. (1.00s)
    test(3)
    
    # Test 4: Test for function with wrapped object

# Generated at 2022-06-13 20:10:40.860339
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import random
    import pathlib

    tmp_dir = pathlib.Path("tmp")

    if not tmp_dir.exists():
        tmp_dir.mkdir()

    with work_in_progress("Create a 100 MiB file"):
        with open(tmp_dir / "tmp.dat", "wb") as fout:
            for i in range(1<<17):
                fout.write(bytes(random.getrandbits(8) for _ in range(1024)))
    
    assert os.path.getsize(tmp_dir / "tmp.dat") == 104857600

    # Clean up
    os.remove(tmp_dir / "tmp.dat")
    os.rmdir(tmp_dir)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:46.161431
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Listing files"):
        time.sleep(1)
        print("Files listed")
    with work_in_progress("Sleeping"):
        time.sleep(3)

if __name__ == "__main__":
    import sys
    import doctest

    sys.exit(doctest.testmod()[0])

# Generated at 2022-06-13 20:10:53.587224
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test for function work_in_progress."""
    def f(i: int) -> int:
        time.sleep(1.0)
        return i + 1

    # Test contextlib.contextmanager
    with work_in_progress("sleep"):
        time.sleep(1)

    # Test decorator
    @work_in_progress("processing")
    def g(i: int) -> int:
        time.sleep(1.0)
        return i + 1
    g(1)


# Test
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:58.012557
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Init"):
        time.sleep(1)
        with work_in_progress("Calculation"):
            time.sleep(1)
    assert True

# Generated at 2022-06-13 20:11:05.145138
# Unit test for function work_in_progress
def test_work_in_progress():
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
    pass

# Generated at 2022-06-13 20:11:12.733009
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

# Generated at 2022-06-13 20:11:16.909310
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def test_function():
        time.sleep(1.0)
        return True

    assert test_function()

    with work_in_progress("Saving file"):
        time.sleep(1.0)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:22.214157
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test the context manager work_in_progress."""
    from contextlib import ExitStack

    with ExitStack() as stack:
        stack.enter_context(redirect_stdout(sys.stdout))
        with work_in_progress("Loading file"):
            time.sleep(0.02)
            stack.callback(print, "\n")
        stack.enter_context(redirect_stdout(sys.stderr))
        with work_in_progress("Loading file"):
            time.sleep(0.02)
            stack.callback(print, "\n")

# Generated at 2022-06-13 20:11:25.862640
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("/path/to/some/file")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:28.018810
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(2.0)


if __name__ == "__main__":
    # running test
    test_work_in_progress()
    print("Everything passed")

# Generated at 2022-06-13 20:12:14.803156
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test Script for function work_in_progress."""

    with work_in_progress("Loading file"):
        time.sleep(1)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

# Generated at 2022-06-13 20:12:17.649018
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

# Generated at 2022-06-13 20:12:25.169444
# Unit test for function work_in_progress
def test_work_in_progress():
    ret = None

    # Test with function
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    ret = load_file("/path/to/some/file")  # doctest: +ELLIPSIS

# Generated at 2022-06-13 20:12:28.249224
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Multiplying"):
        time.sleep(0.5)
    with work_in_progress("Dividing"):
        time.sleep(2)



# Generated at 2022-06-13 20:12:31.790398
# Unit test for function work_in_progress
def test_work_in_progress():
    import pytest
    with pytest.raises(Exception):
        with work_in_progress("This is an exception"):
            raise Exception("An exception")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:34.613643
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3.5)
    with work_in_progress("Saving file"):
        time.sleep(3.78)

# Generated at 2022-06-13 20:12:44.711767
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test the use of work_in_progress as context manager."""
    with work_in_progress("Counting to ten"):
        time.sleep(2)
    with work_in_progress("Counting to ten"):
        time.sleep(0.1)
    with work_in_progress("Counting to ten"):
        time.sleep(0.01)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 20:12:52.684019
# Unit test for function work_in_progress
def test_work_in_progress():
    print("test_work_in_progress")
    @work_in_progress('FooBar')
    def foobar(x, y):
        time.sleep(1)
        return x + y

    def baz(x, y):
        time.sleep(1)
        return x + y

    foobar(3, 5)
    with work_in_progress("Baz"):
        baz(3, 5)

    print("test_work_in_progress: OK")

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:55.483075
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3)


# Generated at 2022-06-13 20:13:03.744565
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
    save_file(obj, "/path/to/some/other/file")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:36.817312
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test the function work_in_progress."""
    # pylint: disable = protected-access
    from .stopwatch import _stopwatch
    from .stopwatch import Stopwatch

    @work_in_progress("Work in progress")
    def _():
        with Stopwatch() as sw:
            sw.pause()
            sw.resume()
            sw.stop()

            for _ in range(10):
                time.sleep(0.1)

    _stopwatch = _stopwatch  # type: ignore # https://github.com/python/mypy/issues/1091

# Generated at 2022-06-13 20:14:41.528743
# Unit test for function work_in_progress
def test_work_in_progress():
    assert "work_in_progress" in globals()

    with work_in_progress("Test 1"):
        for i in range(1, 10000000):
            pass

    with work_in_progress("Test 2"):
        for i in range(1, 1000000):
            pass

# Generated at 2022-06-13 20:14:45.744926
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        a = 0
        for _ in range(1000):
            a += 1

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:14:49.572576
# Unit test for function work_in_progress
def test_work_in_progress():
    import random

    @work_in_progress("Waiting for a random time")
    def random_wait():
        time.sleep(random.random())

    random_wait()

# Generated at 2022-06-13 20:14:54.482742
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        print("time elapsed:", time.time() - time.time())
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:15:05.567939
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
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test_work_in_progress.pickle")
        obj = {'a': 1, 'b': 2}
        save_file(filepath, obj)
        assert load_file(filepath) == obj

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:15:08.495054
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:15:17.873815
# Unit test for function work_in_progress
def test_work_in_progress():
    from six.moves import StringIO
    from six import PY2, StringIO

    if PY2:
        StringIO = StringIO

    # Test context manager
    f = StringIO()
    with patch('sys.stdout', f):
        with work_in_progress("Test"):
            time.sleep(0.5)

    output = f.getvalue().strip()
    assert output == "Test... done. (0.50s)"

    # Test function decorator
    @work_in_progress("Test")
    def decorated():
        time.sleep(0.5)

    f = StringIO()
    with patch('sys.stdout', f):
        decorated()

    output = f.getvalue().strip()
    assert output == "Test... done. (0.50s)"