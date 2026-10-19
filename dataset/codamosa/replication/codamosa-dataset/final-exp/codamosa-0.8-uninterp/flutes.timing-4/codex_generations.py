

# Generated at 2022-06-13 20:05:19.070983
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Doing something..."):
        time.sleep(1)

# Generated at 2022-06-13 20:05:25.786240
# Unit test for function work_in_progress
def test_work_in_progress():
    start_time = time.time()
    with work_in_progress("Waiting"):
        time.sleep(1)
    time_consumed = time.time() - start_time
    assert time_consumed > 1 and time_consumed < 2
    try:
        load_file("_aa")
    except FileNotFoundError:
        pass

# Generated at 2022-06-13 20:05:34.130240
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import tempfile

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, data):
        with open(path, "wb") as f:
            return pickle.dump(data, f)

    data = range(10000)
    with tempfile.TemporaryDirectory() as temp_dir:
        path_in = os.path.join(temp_dir, "data.pkl")
        path_out = os.path.join(temp_dir, "check_data.pkl")
        save_file(path_in, data)
        loaded_data = load_file(path_in)
       

# Generated at 2022-06-13 20:05:41.747247
# Unit test for function work_in_progress
def test_work_in_progress():
    def test_loading():
        @work_in_progress()
        def load_file(path):
            time.sleep(2)
            with open(path, "rb") as f:
                return pickle.load(f)

        path = "C:/Users/liuxc/Desktop/dataset/bdd100k/bdd100k.zip"
        obj = load_file(path)
        assert obj is not None

    def test_saving():
        path = "C:/Users/liuxc/Desktop/dataset/bdd100k/bdd100k.zip"
        with work_in_progress():
            time.sleep(2)
            with open(path, "rb") as f:
                obj = pickle.load(f)
        assert obj is not None

# Generated at 2022-06-13 20:05:44.356610
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress('Testing context manager')
    def sleep():
        time.sleep(1)
    sleep()

# Generated at 2022-06-13 20:05:55.420450
# Unit test for function work_in_progress
def test_work_in_progress():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    import pickle
    import time

    with TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "test_file"

        obj = dict(a=[1, 2, 3], b=[4, 5, 6], c=[7, 8, 9])

        @work_in_progress("Saving")
        def save(path, obj):
            time.sleep(0.05)
            with open(path, "wb") as f:
                pickle.dump(obj, f)

        save(path, obj)
        assert path.is_file()

        @work_in_progress("Loading")
        def load(path):
            time.sleep(0.05)

# Generated at 2022-06-13 20:05:57.260611
# Unit test for function work_in_progress
def test_work_in_progress():
    def test():
        with work_in_progress("test"):
            time.sleep(1)

    test()

# Generated at 2022-06-13 20:06:00.908361
# Unit test for function work_in_progress
def test_work_in_progress():
    # Perform a short task:
    with work_in_progress("Doing a short task"):
        time.sleep(1)
    # Perform a long task:
    with work_in_progress("Doing a long task"):
        time.sleep(10)

# Generated at 2022-06-13 20:06:09.199304
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("This is a test"):
        time.sleep(1)
        # at this point, the time since the beginning of the block is 1 second
        # the assert below is only useful if we do not touch anything else until the end of the block
        assert time.time() - 1 < 1

    obj = {
        "a": 1,
        "b": 2,
        "c": 3,
    }

    @work_in_progress("This is another test")
    def test(obj):
        time.sleep(3)
        return obj

    assert test(obj) == obj

# Generated at 2022-06-13 20:06:20.543499
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    from sklearn.metrics import roc_auc_score
    from sklearn.datasets import load_digits

    X, y = load_digits(return_X_y=True)

    @work_in_progress("Generating model")
    def model(X, y):
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression(random_state=0, solver='lbfgs',
                                 multi_class='multinomial').fit(X, y)
        return clf

    with work_in_progress("Generating predictions"):
        y_pred = model(X, y).predict_proba(X)


# Generated at 2022-06-13 20:06:28.138101
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Counting to one million"
    with work_in_progress(desc):
        for _ in range(1000000):
            _ = _


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:29.616764
# Unit test for function work_in_progress
def test_work_in_progress():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:06:42.963111
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    # Test pickle.load
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    # Test pickle.dump
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    # Test try except as a context
    with work_in_progress("Try Except as context"):
        try:
            time.sleep(1)
            raise Exception("Test")
        except Exception as e:
            print(e)

    # Test while loop as a context
    with work_in_progress("While Loop as context"):
        i = 0
        while i < 3:
            i += 1


# Generated at 2022-06-13 20:06:52.120579
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile
    from pickle import loads, dumps
    from shutil import copyfile
    from pathlib import Path

    obj = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        src_path = tmp_dir / "src.pkl"
        dst_path = tmp_dir / "dst.pkl"

        obj_dump = dumps(obj)
        with open(src_path, "wb") as f:
            f.write(obj_dump)

        with work_in_progress("Loading file"):
            with open(src_path, "rb") as f:
                obj_load

# Generated at 2022-06-13 20:06:55.864994
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    desc = "Testing work in progress"
    with work_in_progress(desc):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:05.446882
# Unit test for function work_in_progress
def test_work_in_progress():

    import os
    import subprocess

    # Create temporary file
    tmp_file = "/tmp/test_work_in_progress_file.txt"
    with open(tmp_file, "w") as f:
        f.write("")

    # Assert no message is printed
    try:
        with work_in_progress("Test info"):
            pass
    except Exception:
        raise
    else:
        assert True

    # Assert subprocess is executed as expected
    try:
        with work_in_progress("Test info"):
            subprocess.check_call(["echo", "test", ">>", tmp_file])
    except Exception:
        raise
    else:
        assert os.path.exists(tmp_file)

    # Check file content

# Generated at 2022-06-13 20:07:09.067939
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress()
    def test():
        time.sleep(1.15)

    test()
    with work_in_progress():
        time.sleep(1.15)

# test_work_in_progress()

# Generated at 2022-06-13 20:07:12.900965
# Unit test for function work_in_progress
def test_work_in_progress():
    for i in range(10):
        with work_in_progress():
            time.sleep(1)
    for i in range(10):
        with work_in_progress("Task #%d" % i):
            time.sleep(1)

test_work_in_progress()

# Generated at 2022-06-13 20:07:15.581369
# Unit test for function work_in_progress
def test_work_in_progress():
    import time

    with work_in_progress("Test"):
        time.sleep(1)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:20.267340
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("tests/data/sample.pkl")

    with work_in_progress("Saving file"):
        with open("tests/data/sample.pkl.bak", "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:07:31.370162
# Unit test for function work_in_progress
def test_work_in_progress():
    def fake_slow_function(x, a=0.5, b=0.2, c=0.8):
        # Real computation
        time.sleep(0.2)
        time.sleep(0.1)
        time.sleep(0.3)
        time.sleep(0.12)
        time.sleep(0.05)
        time.sleep(0.25)

    with work_in_progress("fake_slow_function"):
        fake_slow_function("x")

if __name__ == '__main__':
    print("Execute test_work_in_progress... ")
    test_work_in_progress()

# Generated at 2022-06-13 20:07:42.616609
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        time.sleep(1)
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(path, obj):
        time.sleep(1)
        with open(path, "wb") as f:
            pickle.dump(obj, f)
            return True

    path = "examples/tmp.pickle"
    dic = {"a": 1, "b": 2, "c": 3}
    save_file(path, dic)

    @work_in_progress("Loading file")
    def load_file_wrapped(path):
        return load_file(path)

    a = load_file_wrapped(path)
    assert_equal(a, dic)


# Generated at 2022-06-13 20:07:48.777632
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import pickle
    time.sleep(0.1)
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    time.sleep(0.1)
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:07:56.478186
# Unit test for function work_in_progress
def test_work_in_progress():
    source_pathes = [__file__, "WORK_IN_PROGRESS.md"]
    for source_path in source_pathes:
        with work_in_progress(f"Counting the lines of {source_path}"):
            with open(source_path) as f:
                line_count = sum(1 for _ in f)
        print(line_count)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:00.330995
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("This is a unit test of work_in_progress"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:06.678814
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
    obj = load_file("tests/testfile.pickle")
    assert obj == "Successful load."

    with work_in_progress("Saving file"):
        with open("tests/testfile.pickle", "wb") as f:
            pickle.dump(obj, f)
    with open("tests/testfile.pickle", "rb") as f:
        assert pickle.load(f) == "Successful load."


# Generated at 2022-06-13 20:08:16.493077
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import tempfile
    import pickle
    import sys

    with tempfile.TemporaryDirectory() as tmpdir:
        test_data = {
            "key_0": 0,
            "key_1": 1,
        }

        def _dump_data(path):
            with open(path, "wb") as f:
                pickle.dump(test_data, f)

        def _load_data(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        test_file_path = os.path.join(tmpdir, "test")

        with work_in_progress("Saving data"):
            _dump_data(test_file_path)

        saved_data = _load_data(test_file_path)


# Generated at 2022-06-13 20:08:25.798169
# Unit test for function work_in_progress
def test_work_in_progress():
    import unittest

    import io
    import sys

    class TestWorkInProgress(unittest.TestCase):
        def test_work_in_progress(self):
            with io.StringIO() as buf, contextlib.redirect_stdout(buf):
                # contextlib.redirect_stdout(buf)  # Python3
                with work_in_progress("Loading file") as wip:
                    time.sleep(0.11)
                    wip()  # Re-enter the context.
            self.assertIn("Loading file... done. (0.11s)", buf.getvalue())

    unittest.main(module="__main__", exit=False, verbosity=2)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:29.098586
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Dummy task")
    def task():
        time.sleep(1)

    task()


if __name__ == "__main__":
    print("Running doctest...")
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:08:33.744493
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing")
    def some_task(a):
        time.sleep(13)
        return a

    result = some_task(2)

# Generated at 2022-06-13 20:08:38.138246
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("foo"):
        time.sleep(1)

# Generated at 2022-06-13 20:08:43.729347
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("test_work_in_progress loading file"):
        time.sleep(2)
    with work_in_progress("test_work_in_progress saving file"):
        time.sleep(3)
    @work_in_progress("test_work_in_progress loading file")
    def load_file(path):
        time.sleep(2)

    load_file(None)

    @work_in_progress("test_work_in_progress saving file")
    def save_file(path):
        time.sleep(3)

    save_file(None)

# Generated at 2022-06-13 20:08:50.980078
# Unit test for function work_in_progress
def test_work_in_progress():
    # Capture the current stdout.
    stdout = sys.stdout
    #  We will redirect to a StringIO.
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    try:
        with work_in_progress("Saving file"):
            time.sleep(0.5)
        new_stdout.seek(0)
        assert new_stdout.read() == "Saving file... done. (0.50s)\n"
    finally:
        # Restore the previous stdout
        sys.stdout = stdout

# Generated at 2022-06-13 20:09:00.558553
# Unit test for function work_in_progress
def test_work_in_progress():
    print("*" * 80)
    print("Unit test for function work_in_progress:")
    print("-" * 80)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
        time.sleep(4)

    obj = load_file("/path/to/some/file")
    assert obj == "dummy_data"

    with work_in_progress("Saving file"):
        time.sleep(4)

    print("-" * 80)

if __name__ == "__main__":
    import pickle
    import time

    test_work_in_progress()

# Generated at 2022-06-13 20:09:01.826779
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(0.5)

# Generated at 2022-06-13 20:09:07.241866
# Unit test for function work_in_progress
def test_work_in_progress():
    import os

    @work_in_progress("Removing test file")
    def _del_file(path):
        os.remove(path)

    path = "test_work_in_progress.txt"
    with open(path, "wb") as f:
        f.write(b"\x01\x02\x03\x04")
    try:
        _del_file(path)
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:14.288522
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

# Generated at 2022-06-13 20:09:19.604123
# Unit test for function work_in_progress
def test_work_in_progress():
    N = 100
    print("Testing whether work_in_progress function is correct...", end='', flush=True)
    for n in range(1, N + 1):
        time.sleep(.01)
        with work_in_progress("Test"):
            pass
    print(" done.")


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:09:29.445751
# Unit test for function work_in_progress
def test_work_in_progress():
    import shutil
    import tempfile
    import pickle

    fd, path = tempfile.mkstemp()

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = {"a": 1, "b": 2, "c": 3}
    save_file(path, obj)
    assert load_file(path) == obj
    os.remove(path)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:31.649321
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
        with work_in_progress("Saving file"):
            time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:40.854841
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import pickle
    import os

    with work_in_progress("Saving file"):
        with open("/tmp/test_work_in_progress.pkl", "wb") as f:
            pickle.dump(random.random(), f)

    with work_in_progress("Loading file"):
        with open("/tmp/test_work_in_progress.pkl", "rb") as f:
            obj = pickle.load(f)

    os.remove("/tmp/test_work_in_progress.pkl")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:43.617287
# Unit test for function work_in_progress
def test_work_in_progress():
    desc = "Unit test for function work_in_progress"
    with work_in_progress(desc) as w:
        time.sleep(1)
    assert w is None

# Generated at 2022-06-13 20:09:45.963001
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import contextlib

# Generated at 2022-06-13 20:09:49.180358
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress function"):
        time.sleep(0.2)

# Unit test entry.
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:51.635204
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Executing some task"):
        time.sleep(random.uniform(0.5, 1))

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:59.128316
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open("/path/to/other/file", "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:07.601157
# Unit test for function work_in_progress
def test_work_in_progress():
    from sys import argv
    if len(argv) == 2 and argv[1] == 'test':
        @work_in_progress("Loading file")
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        @work_in_progress("Saving file")
        def save_file(path, obj):
            with open(path, "wb") as f:
                pickle.dump(obj, f)

        obj = load_file("/tmp/test.cpickle")
        save_file("/tmp/test2.cpickle", obj)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:09.546057
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress()
    def foo():
        time.sleep(1)

    foo()


# Generated at 2022-06-13 20:10:11.480945
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work in progress"):
        time.sleep(1)



# Generated at 2022-06-13 20:10:21.928768
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress"""
    import types

    # Define a dummy function
    def dummy_function(a, b):
        time.sleep(0.5)
        return a + b

    # Define another dummy function
    @work_in_progress("Adding two numbers")
    def dummy_function_add(a, b):
        time.sleep(0.5)
        return a + b

    # Check function type
    assert isinstance(dummy_function, types.FunctionType)
    assert isinstance(dummy_function_add, types.FunctionType)

    # Call the original dummy function
    result = dummy_function(5, 5)
    assert isinstance(result, int)
    assert result == 10

    # Call the decorated dummy function
    result = dummy_function_add(5, 5)

# Generated at 2022-06-13 20:10:27.940047
# Unit test for function work_in_progress
def test_work_in_progress():
    original_time_sleep = time.sleep

    def _time_sleep(x):
        original_time_sleep(x / 10)

    time.sleep = _time_sleep
    map(list, [range(100000)])
    work_in_progress("Time after map")
    list(map(list, [range(100000)]))
    work_in_progress("Time after list(map)")
    time.sleep = original_time_sleep

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:29.945455
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress function"):
        time.sleep(0.25)

# Generated at 2022-06-13 20:10:32.124061
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress():
        time.sleep(0.5)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:35.465420
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        time.sleep(1)
        with work_in_progress("Loading file"):

            time.sleep(2)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:38.371492
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    desc = "Test work in progress"
    with work_in_progress(desc):
        time.sleep(3)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:44.153939
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

# Generated at 2022-06-13 20:10:51.224422
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("test1"):
        time.sleep(1)
    time.sleep(0.01)
    def simple_lambda():
        with work_in_progress("test2 (lambda)"):
            time.sleep(0.01)
    simple_lambda()
    time.sleep(0.1)
    def test3():
        with work_in_progress("test3"):
            time.sleep(0.05)
    test3()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:53.927589
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test")
    def _():
        time.sleep(1.2)
    _()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:58.610212
# Unit test for function work_in_progress
def test_work_in_progress():
    text = "work_in_progress"
    with work_in_progress(desc=text):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:02.151246
# Unit test for function work_in_progress
def test_work_in_progress():
    print("\nTest work_in_progress")
    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.1)

# test_work_in_progress()

# Generated at 2022-06-13 20:11:10.166228
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Task 1") as _:
        time.sleep(1.5)

    print()

    @work_in_progress("Task 2")
    def task():
        time.sleep(1.5)

    task()

# Generated at 2022-06-13 20:11:14.404386
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def test():
        time.sleep(0.5)

    test()
    with work_in_progress("Testing contextlib.contextmanager"):
        time.sleep(0.5)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:17.577291
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(1)


# Invoking the unit test
if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:25.194572
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    import time

    arr = []
    for _ in range(int(1e2)):
        arr.append(random.random())

    with work_in_progress("Sorting numbers"):
        arr.sort()

    with work_in_progress("Reversing numbers"):
        arr.reverse()

    with work_in_progress("Counting numbers"):
        time.sleep(0.2)
        n = len(arr)

    with work_in_progress("Dumping into file"):
        with open("./test.pickle", "wb") as f:
            pickle.dump(arr, f)

    print(f"Array of size {n} dumped")


if __name__ == "__main__":
    with work_in_progress("Running unit test"):
        test_work_

# Generated at 2022-06-13 20:11:27.692449
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.15)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:31.334627
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file") as w:
        with open("path/to/some/file", "rb") as f:
            pickle.load(f)
    assert w is None

# Generated at 2022-06-13 20:11:34.780886
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    import doctest
    doctest.testmod(verbose=0)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:40.225940
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    import sys

    class Capturing(list):
        """Capture the value sent to stdout"""
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = io.StringIO()
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio    # free up some memory
            sys.stdout = self._stdout

    with Capturing() as output:
        with work_in_progress("Testing work_in_progress"):
            time.sleep(1)
    assert len(output) == 1
    assert "Testing work_in_progress... done" in output[0]
    assert "s" in output[0]

# Generated at 2022-06-13 20:11:45.502810
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading data")
    def load_data():
        pass

    load_data()
    with work_in_progress("Saving data"):
        pass

# Run unit test
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:48.346671
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    with work_in_progress("Saving file..."):
        time.sleep(2)


# Main function for testing module.

# Generated at 2022-06-13 20:12:04.455017
# Unit test for function work_in_progress
def test_work_in_progress():
    path = "test.json"
    data = {"foo": "bar", "baz": (1, 2, 3)}

    with work_in_progress("Saving file"):
        with open(path, "w") as f:
            json.dump(data, f)

    assert os.path.exists(path)

    with work_in_progress("Loading file"):
        with open(path, "r") as f:
            read_data = json.load(f)

    assert read_data == data

    os.remove(path)


if __name__ == "__main__":
    test_work_in_progress()

    # Example test

# Generated at 2022-06-13 20:12:12.871449
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    def load_file(path: str):
        @work_in_progress("Loading file")
        def _load_file(path: str):
            with open(path, "rb") as f:
                return pickle.load(f)
        return _load_file(path)

    def save_file(path: str, obj):
        @work_in_progress("Saving file")
        def _save_file(path: str, obj):
            with open(path, "wb") as f:
                pickle.dump(obj, f)
        return _save_file(path, obj)

    # Testing work_in_progress as a decorator of function
    obj = load_file("unit_test/test_psd.pkl")

    # Testing work_in_progress as a context manager
    save

# Generated at 2022-06-13 20:12:16.899910
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test function
    @work_in_progress("Test")
    def test():
        time.sleep(1)

    # Test context manager
    with work_in_progress("Test"):
        time.sleep(2)

# Generated at 2022-06-13 20:12:27.316556
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    with open("test.pickle", "wb") as f:
        pickle.dump((1, 2, 3), f)

    load_file("test.pickle")
    print()

    with work_in_progress("Saving file"):
        with open("test.pickle", "wb") as f:
            pickle.dump((1, 2, 3), f)

# Generated at 2022-06-13 20:12:34.366830
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.5)
    with work_in_progress("Saving file"):
        time.sleep(2.5)
    with work_in_progress():
        time.sleep(3)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("Start testing")
    test_work_in_progress()
    print("Finish testing")

# Generated at 2022-06-13 20:12:42.260880
# Unit test for function work_in_progress
def test_work_in_progress():
    def with_file():
        with open("test_work_in_progress.txt", "w") as f:
            f.write("test")

    @work_in_progress("Testing work in progress")
    def job_with_file():
        with_file()

    @work_in_progress("Testing work in progress")
    def job_with_meta():
        time.sleep(1)  # Make it slower than job_with_file

    job_with_file()
    job_with_meta()


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:44.427925
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def foo():
        time.sleep(1)

    foo()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:53.656189
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    cwd = os.getcwd()
    test_data_dir = os.path.join(cwd, "test_data")
    file_path = os.path.join(test_data_dir, "test_data.pkl")

    obj = load_file(file_path)

    with work_in_progress("Saving file"):
        with open(file_path, "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:12:56.512892
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test progress")
    def dummy():
        # Simulate a long task
        time.sleep(0.5)

    dummy()

# Generated at 2022-06-13 20:13:02.745977
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)

    with work_in_progress("Saving file"):
        with open("test.py", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:30.110554
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle

    def test_work_in_progress_decorator(desc: str):
        @work_in_progress(desc)
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        obj = load_file("test_file.pickle")

    test_work_in_progress_decorator("Loading file")

    with work_in_progress("Saving file"):
        with open("test_file.pickle", "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:40.362728
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys

    class Mock(object):
        def __init__(self, *args):
            self.args = args

        def write(self, line):
            self.args += (line, )

        def flush(self):
            pass

    # Test without context manager
    sys.stdout = Mock()
    work_in_progress("TEST").__exit__(None, None, None)
    assert ('TEST... ', ' done. (0.00s)\n', ) == sys.stdout.args

    # Test with context manager
    sys.stdout = Mock()
    with work_in_progress("TEST"):
        pass
    assert ('TEST... ', ' done. (0.00s)\n', ) == sys.stdout.args

    # Restore stdout
    sys.stdout = sys.__stdout

# Generated at 2022-06-13 20:13:44.147264
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:51.495711
# Unit test for function work_in_progress
def test_work_in_progress():
    from datetime import timedelta
    from .logger import set_loglevel

    with set_loglevel(20):
        with work_in_progress("Loading file"):
            time.sleep(timedelta(seconds=1).total_seconds())

        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        @work_in_progress("Loading file")
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        with work_in_progress("Loading file"):
            load_file("/path/to/some/file")

        obj = load_file("/path/to/some/file")


# Generated at 2022-06-13 20:13:55.736865
# Unit test for function work_in_progress
def test_work_in_progress():
    def wait(seconds=1.0):
        time.sleep(seconds)
        return "done"

    with work_in_progress("This is a test"):
        wait(2)

    wait(0.5)
    work_in_progress("This is a test")(wait)(1)

# Generated at 2022-06-13 20:14:00.586353
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test work_in_progress function."""
    with work_in_progress("Testing work_in_progress function"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:07.062230
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Fetching sample data")
    def fetch_sample_data(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = fetch_sample_data("/path/to/some/file")
    assert isinstance(obj, pd.DataFrame)

    with work_in_progress("Saving sample data"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:17.787006
# Unit test for function work_in_progress
def test_work_in_progress():
    from io import BytesIO

    def save(obj, path, *, overwrite=False, desc=None):
        with open(path, 'wb') as f:
            if desc is not None:
                with work_in_progress(desc):
                    pickle.dump(obj, f)
            else:
                pickle.dump(obj, f)

    def load(path, *, desc=None):
        with open(path, 'rb') as f:
            if desc is not None:
                with work_in_progress(desc):
                    obj = pickle.load(f)
            else:
                obj = pickle.load(f)
        return obj

    def test(obj):
        # Test dump and load
        path = "./test_object.pkl"
        save(obj, path, overwrite=True)


# Generated at 2022-06-13 20:14:27.377160
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    logging.warning("Skip test_work_in_progress")


# Execute this module as a script.
if __name__ == "__main__":
    try:
        if len(sys.argv) == 0:
            raise ValueError

        if sys.argv[1] == "test":
            test_work_in_progress()

        else:
            raise ValueError

    except ValueError:
        print(f"usage: {sys.argv[0]} test", file=sys.stderr)
        sys.exit(1)

    except KeyboardInterrupt:
        sys.exit(1)

    sys.exit(0)

# Generated at 2022-06-13 20:14:29.583305
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress(desc="Sleeping"):
        time.sleep(.1)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:15:17.829339
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    from pytest import raises

    def f():
        with raises(ZeroDivisionError):
            1 / 0

    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.2)
        f()


if __name__ == '__main__':
    test_work_in_progress()