

# Generated at 2022-06-13 20:05:18.029366
# Unit test for function work_in_progress
def test_work_in_progress():
    pass

# Generated at 2022-06-13 20:05:23.607713
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return sum(1 for _ in f)

    obj = load_file(__file__)
    expected = """Loading file... done. (0.00s)"""
    assert expected == capsys.readouterr().out

    with work_in_progress("Saving file"):
        pass
    expected = """Saving file... done. (0.00s)"""
    assert expected == capsys.readouterr().out

# Generated at 2022-06-13 20:05:26.956589
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(0.3)
    try:
        with work_in_progress("Saving file"):
            time.sleep(0.4)
            raise Exception()
    except AssertionError:
        pass
    except Exception:
        return True
    return False

# Generated at 2022-06-13 20:05:35.002391
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test the function work_in_progress
    """

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    print()
    print("Testing function work_in_progress...\n")
    print(">>> @work_in_progress(\"Loading file\")")
    print("... def load_file(path):")
    print("...     with open(path, \"rb\") as f:")
    print("...         return pickle.load(f)")
    print()
    print(">>> obj = load_file(\"/path/to/some/file\")")
    with work_in_progress("Loading file"):
        obj = load_file("/path/to/some/file")
    print()

# Generated at 2022-06-13 20:05:42.157982
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    path = Path("/path/to/some/file")
    obj = load_file(path)

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:47.255501
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path: str, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    obj = list(range(1000000))
    save_file("./test.pkl", obj)
    obj = load_file("./test.pkl")

# Generated at 2022-06-13 20:05:52.459970
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("test"):
        time.sleep(1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:05:58.658056
# Unit test for function work_in_progress
def test_work_in_progress():
    # noinspection PyUnusedLocal
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(3.5)
        return True

    # noinspection PyUnusedLocal
    with work_in_progress("Saving file"):
        time.sleep(3.7)

# Generated at 2022-06-13 20:06:07.364747
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Wait 0.1 secs"):
        time.sleep(0.1)
    with work_in_progress("Wait 0.23 secs"):
        time.sleep(0.23)
    with work_in_progress("Wait 0.3 secs"):
        time.sleep(0.3)
    with work_in_progress("Wait 0.45 secs"):
        time.sleep(0.45)
    with work_in_progress("Wait 1 sec"):
        time.sleep(1)
    with work_in_progress("Wait 2.3 secs"):
        time.sleep(2.3)
    with work_in_progress("Wait 4 secs"):
        time.sleep(4)
    with work_in_progress("Wait 15 secs"):
        time.sleep

# Generated at 2022-06-13 20:06:09.340930
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)


# Generated at 2022-06-13 20:06:13.530603
# Unit test for function work_in_progress
def test_work_in_progress():
    arr = [random.randint(-100, 100) for _ in range(1000000)]
    with work_in_progress("Sorting array"):
        arr.sort()


# Generated at 2022-06-13 20:06:24.158767
# Unit test for function work_in_progress

# Generated at 2022-06-13 20:06:32.508501
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    import tempfile

    def write_file(path: str, data: bytes):
        with open(path, "wb") as f:
            f.write(data)

    def read_file(path: str) -> bytes:
        with open(path, "rb") as f:
            return f.read()

    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "test")
        with work_in_progress("Writing file"):
            write_file(f, b"test")

        with work_in_progress("Reading file"):
            data = read_file(f)
        assert data == b"test"

    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "test")

# Generated at 2022-06-13 20:06:34.898615
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test"):
        time.sleep(1.0)


# Generated at 2022-06-13 20:06:45.597658
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

    a = list(range(30000000))
    b = a[:]

    path = "test.pkl"
    save_file(path, a)
    b = load_file(path)
    assert b == a
    os.remove(path)

# Unit test suite

# Generated at 2022-06-13 20:06:50.776675
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        x = [i for i in range(1000000)]
    with work_in_progress("Loading file"):
        x = [i for i in range(1000000)]
    with work_in_progress("Sorting file"):
        x = [i for i in range(1000000)]
        x.sort()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:02.766780
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Calculating SVD")
    def calc_svd(A):
        U, s, V = np.linalg.svd(A, full_matrices=True)
        return U, s, V

    A = np.random.randn(100, 10)
    U, s, V = calc_svd(A)
    assert U.shape[0] == A.shape[0]
    assert s.shape[0] == A.shape[1]
    assert V.shape[1] == A.shape[1]


if __name__ == "__main__":
    # Run all functions with an "test_" prefix
    import doctest

    doctest.testmod()

# Create a short alias for this module
import sys
sys.modules["toolbox"] = sys.modules

# Generated at 2022-06-13 20:07:08.028862
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3)

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)


# Generated at 2022-06-13 20:07:12.102722
# Unit test for function work_in_progress
def test_work_in_progress():
    start_time = time.time()
    time.sleep(1.23)
    with work_in_progress():
        time.sleep(1.56)
    end_time = time.time()
    assert abs(end_time - start_time - 2.79) < 1e-2

# Generated at 2022-06-13 20:07:15.892205
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    with work_in_progress("Loading test file"):
        for i in range(99999):
            load_file("test_file.pickle")

# Generated at 2022-06-13 20:07:29.304310
# Unit test for function work_in_progress
def test_work_in_progress():
    def do_something():
        time.sleep(0.5)

    with work_in_progress("Testing function work_in_progress"):
        do_something()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:41.029610
# Unit test for function work_in_progress
def test_work_in_progress():
    from .testing import TestCase
    from .testing import TestCase

    class TestWorkInProgress(TestCase):
        def setUp(self):
            self.time_period_list = []

        def process(self, desc):
            with work_in_progress(desc) as w:
                time.sleep(0.5)

        def test_work_in_progress_1(self):
            self.process("test_work_in_progress_1")

        def test_work_in_progress_2(self):
            self.process("test_work_in_progress_2")

        def test_work_in_progress_3(self):
            self.process("test_work_in_progress_3")

    test_work_in_progress = TestWorkInProgress()
    test_work_in_progress.run()

# Generated at 2022-06-13 20:07:48.742968
# Unit test for function work_in_progress
def test_work_in_progress():
    from .function_runner import run_function_in_subprocess
    run_function_in_subprocess(
        work_in_progress,
        (
            test_run_sub_sub_process,
            ("Test that subprocesses are supported by work_in_progress",),
            3,
        ),
        {"desc": "Test that subprocesses are supported by work_in_progress"},
        expected_outputs=(
            "Test that subprocesses are supported by work_in_progress... ",
            "Test that subprocesses are supported by work_in_progress... done.",
            "Test that subprocesses are supported by work_in_progress... done.",
            "Test that subprocesses are supported by work_in_progress... done. (3.00s)"
        )
    )


# Generated at 2022-06-13 20:07:58.383174
# Unit test for function work_in_progress
def test_work_in_progress():
    try:
        @work_in_progress("Hello world")
        def foo():
            time.sleep(0.1)
        try:
            foo()
        except Exception:
            messages = io.StringIO()
            traceback.print_exc(file=messages)
            assert False, messages.getvalue()
    except Exception:
        messages = io.StringIO()
        traceback.print_exc(file=messages)
        assert False, messages.getvalue()


if __name__ == '__main__':
    test_work_in_progress()
    print("All unit tests successfull.")

# Generated at 2022-06-13 20:07:59.621542
# Unit test for function work_in_progress
def test_work_in_progress():
    print(work_in_progress)

# Generated at 2022-06-13 20:08:04.803848
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Initialising data"):
        time.sleep(0.2)

    array = None
    with work_in_progress("Loading file"):
        array = np.load("/path/to/some/large/file.npy")

    with work_in_progress("Saving file"):
        np.save("/path/to/a/new/file.npy", array)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:06.497969
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing function work_in_progress"):
        time.sleep(5)

# Generated at 2022-06-13 20:08:08.935551
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Performing some operations"):
        time.sleep(0.5)

    @work_in_progress("Performing some other operations")
    def c():
        time.sleep(0.6)
    c()

# Generated at 2022-06-13 20:08:13.247962
# Unit test for function work_in_progress
def test_work_in_progress():
    from tests import *
    with work_in_progress("Loading file"):
        with open(TEST_FILE_PATH, "rb") as f:
            assert pickle.load(f) == TEST_OBJ
    with work_in_progress("Saving file"):
        with open(TEST_FILE_PATH, "wb") as f:
            pickle.dump(TEST_OBJ, f)
    print("test_work_in_progress success")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:23.847109
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving file")
    def save_file(path, data):
        with open(path, "wb") as f:
            pickle.dump(data, f)

    with open("work_in_progress_test.pickle", "rb") as f:
        assert pickle.load(f) == load_file("work_in_progress_test.pickle")

    obj = {
        "key": "value"
    }
    save_file("work_in_progress_test.pickle", obj)

# Generated at 2022-06-13 20:08:44.039616
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(sleep_time):
        time.sleep(sleep_time)
        return 0
    def save_file(sleep_time):
        with work_in_progress():
            time.sleep(sleep_time)
    import random
    for i in range(5):
        load_file(random.random())
        save_file(random.random())


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:47.264259
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work in progress")
    def __test():
        time.sleep(0.01)
        return 123

    assert __test() == 123

# Generated at 2022-06-13 20:08:51.541695
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

# Generated at 2022-06-13 20:08:53.522694
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress"):
        time.sleep(0.1)



# Generated at 2022-06-13 20:08:57.330892
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    with work_in_progress("Loading file"):
        with open("benchmark/ratings.pkl", "rb") as f:
            obj = pickle.load(f)

# Generated at 2022-06-13 20:09:00.558590
# Unit test for function work_in_progress
def test_work_in_progress():
    import random

    with work_in_progress("Test the function work_in_progress"):
        time.sleep(random.random())


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:05.988243
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Testing function work_in_progress...")

    print("Testing context manager:")
    with work_in_progress("Waiting 0.5s"):
        time.sleep(0.5)

    print("Testing function decorator:")
    @work_in_progress("Waiting 0.5s")
    def wait():
        time.sleep(0.5)
    wait()
    print("Done!")

# Generated at 2022-06-13 20:09:15.762978
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(os.path.join(os.path.dirname(__file__), "data", "sample.pkl"))

    with work_in_progress("Saving file"):
        with open("sample.pkl", "wb") as f:
            pickle.dump(obj, f)

    os.remove("sample.pkl")


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:09:22.661119
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.2345)
    with work_in_progress("Saving file"):
        time.sleep(2.3456)
    @work_in_progress("Loading file")
    def load_file():
        time.sleep(3.4567)
        return
    load_file()

if __name__ == '__main__':
    # Unit test for function work_in_progress
    test_work_in_progress()

# Generated at 2022-06-13 20:09:26.861170
# Unit test for function work_in_progress
def test_work_in_progress():
    def test_function(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Loading file")
    def test_decorator_function(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    def test_context_manager(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    assert test_function(__file__) == test_decorator_function(__file__)
    assert test_function(__file__) == test_context_manager(__file__)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:53.548546
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import sys
    import subprocess

    cmd = f"python {os.path.abspath(__file__)}"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"{cmd} failed with code {proc.returncode}"
    assert b"Work in progress... done. (1.00s)" in stdout

# Usage example of work_in_progress
if __name__ == "__main__":
    with work_in_progress():
        time.sleep(1)

# Generated at 2022-06-13 20:10:00.312003
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.5)
    print()
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    load_file("/path/to/file")
    print()
    with work_in_progress("Saving file"):
        with open("/path/to/file", "wb") as f:
            pickle.dump({"a": 1, "b": 2}, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:03.048712
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress('Testing work_in_progress')
    def test():
        time.sleep(0.5)

    test()


# Generated at 2022-06-13 20:10:05.987703
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Sleeping for a second"):
        time.sleep(1)


if __name__ == "__main__":
    test_logger()
    test_work_in_progress()

# Generated at 2022-06-13 20:10:10.588075
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.25)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("../../test/test.txt")


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:14.484995
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Function: work_in_progress")
    with work_in_progress("Sleep 1 second"):
        time.sleep(1)
    with work_in_progress("Sleep 2 seconds"):
        time.sleep(2)
    with work_in_progress("Sleep 3 seconds"):
        time.sleep(3)
    @work_in_progress("Sleep 4 seconds")
    def sleep():
        time.sleep(4)
    sleep()
    print("Done.")

# Generated at 2022-06-13 20:10:19.305594
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Test for work in progress"):
        time.sleep(3)
    assert True

if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-13 20:10:27.752059
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

    obj = [5, 6, 7, 8, 9, 10]
    save_file("/tmp/test_work_in_progress", obj)
    obj2 = load_file("/tmp/test_work_in_progress")
    if obj2 != obj:
        raise AssertionError("work_in_progress is broken")
    os.unlink("/tmp/test_work_in_progress")

# Generated at 2022-06-13 20:10:36.415991
# Unit test for function work_in_progress
def test_work_in_progress():
    import tempfile

    obj = {'parameter': 1.23}
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "obj.pickle")
        @work_in_progress(f"Load file to {path}")
        def load_file():
            with open(path, "rb") as f:
                return pickle.load(f)

        @work_in_progress(f"Save file {path}")
        def save_file():
            with open(path, "wb") as f:
                pickle.dump(obj, f)

        save_file()
        ret_obj = load_file()
    assert obj == ret_obj


# Generated at 2022-06-13 20:10:40.568304
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Test work in progress")
    def _test_work_in_progress():
        time.sleep(1)

    _test_work_in_progress()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:22.104379
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Testing function 'work_in_progress'... ", end='')
    with work_in_progress("Loading file"):
        time.sleep(0.1)
    print("done.")

# Generated at 2022-06-13 20:11:26.353432
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1.5)

    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(2)

    load_file("path")

# Generated at 2022-06-13 20:11:28.133440
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:30.213602
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress(desc="Testing work_in_progress"):
        time.sleep(1.34)


# Generated at 2022-06-13 20:11:33.083367
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress."""
    with work_in_progress("Saving file"):
        pass

# Generated at 2022-06-13 20:11:37.249451
# Unit test for function work_in_progress
def test_work_in_progress():
    def dummy_func():
        with work_in_progress("Performing some tasks"):
            time.sleep(2)
        with work_in_progress("Performing some other tasks"):
            time.sleep(3)
    dummy_func()


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:42.356397
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing function \"work_in_progress\"")
    def foo(x, y, z):
        time.sleep(1)
        return x + y + z

    assert foo(1, 2, 3) == 6
    print("done")


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:45.254381
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(3)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:51.983553
# Unit test for function work_in_progress
def test_work_in_progress():
    success = True
    begin_time = time.time()
    with work_in_progress("Loading file"):
        time.sleep(1)
    assert (time.time() - begin_time) > 1
    begin_time = time.time()
    @work_in_progress("Saving file")
    def save_file():
        time.sleep(1)
    save_file()
    assert (time.time() - begin_time) > 1
    return success

if __name__ == '__main__':
    assert test_work_in_progress()

# Generated at 2022-06-13 20:12:01.748714
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle
    import tempfile

    @work_in_progress("Picking the object")
    def pickle_obj(obj):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = str(tmpdir) + os.sep + "obj"
            with open(file_path, "wb") as f:
                pickle.dump(obj, f)

    @work_in_progress("Unpicking the object")
    def unpickle_obj(obj):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = str(tmpdir) + os.sep + "obj"
            with open(file_path, "rb") as f:
                obj_ = pickle.load(f)
        return obj_


# Generated at 2022-06-13 20:13:29.556793
# Unit test for function work_in_progress
def test_work_in_progress():
    import random
    from hashlib import md5

    print(md5(b"unit test for function work_in_progress").hexdigest())
    with work_in_progress("Sort some numbers"):
        sorted([random.random() for i in range(100000)])
    

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:39.154047
# Unit test for function work_in_progress
def test_work_in_progress():
    print("Test work_in_progress:", end="")

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    print("Loading file... done. (3.52s)")

    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    print("Saving file... done. (3.78s)")

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:47.158106
# Unit test for function work_in_progress
def test_work_in_progress():
    # Standard output
    def func1(a, b):
        with work_in_progress("Wait 1 second"):
            time.sleep(1)

    # Redirected output
    import io
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        def func2(a, b):
            with work_in_progress("Wait 1 second"):
                time.sleep(1)

    if __name__ == '__main__':
        # Calling from the command line
        func1(1, 2)
        assert f.getvalue() == ""
    else:
        # Calling from the unit test
        func2(1, 2)
        assert f.getvalue() == "Wait 1 second... done. (1.00s)\n"


# Generated at 2022-06-13 20:13:53.335899
# Unit test for function work_in_progress
def test_work_in_progress():
    from argparse import Namespace
    import uuid
    # Create a random file and save it.
    filepath = f'/tmp/{uuid.uuid4()}'
    data = {
        "int": 1,
        "float": 3.14,
        "str": "Hello",
        "list": [1, 2, 3],
        "dict": {"a": 1, "b": 2, "c": 3},
    }
    with work_in_progress("Creating file"):
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
    # Load the file.
    with work_in_progress("Loading file"):
        with open(filepath, 'rb') as f:
            data_loaded = pickle.load(f)
    # Compare.

# Generated at 2022-06-13 20:14:04.759406
# Unit test for function work_in_progress
def test_work_in_progress():
    save_path = "/tmp/tmp_work_in_progress.tmp"
    obj = list(range(1000000))
    with work_in_progress("Saving file to %s" % save_path):
        with open(save_path, "wb") as f:
            pickle.dump(obj, f)

    obj = None
    with work_in_progress("Loading file from %s" % save_path):
        with open(save_path, "rb") as f:
            obj = pickle.load(f)
    obj[0] = 9999
    assert obj[0] == 9999
    obj = None
    with work_in_progress("Saving file to %s" % save_path):
        with open(save_path, "wb") as f:
            pickle.dump(obj, f)


# Generated at 2022-06-13 20:14:13.006492
# Unit test for function work_in_progress
def test_work_in_progress():
    for verbose in True, False:
        with contextlib.redirect_stdout(None if verbose else StringIO()):
            with work_in_progress("Loading file") as p:
                assert p is None
                assert not p.verbose  # pylint: disable=no-member
                time.sleep(0.1)
            assert p.time_consumed == pytest.approx(0.1)  # pylint: disable=no-member
            with work_in_progress("Saving file"):
                time.sleep(0.1)
            with work_in_progress("Saving file to remote server"):
                time.sleep(0.1)
            assert p.desc == "Saving file to remote server"  # pylint: disable=no-member



# Generated at 2022-06-13 20:14:17.406991
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.5)
    with work_in_progress("Saving file"):
        time.sleep(1.5)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:24.578164
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

# Generated at 2022-06-13 20:14:30.954932
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    with work_in_progress("Saving file"):
        path = "mock_file"
        with open(path, "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:36.681277
# Unit test for function work_in_progress
def test_work_in_progress():
    from .print_util import format_unit_fitting

    # Check duration of the function itself.
    time_consumed = None
    with work_in_progress():
        time_consumed = time.time()

    # Check 2 decimal precision.
    assert format_unit_fitting(time_consumed, 2) == format_unit_fitting(time.time(), 2)

    # Check duration of an iterable.
    time_consumed = None
    with work_in_progress():
        with open(__file__, "rb") as f:
            f.read()
        time_consumed = time.time()

    # Check 2 decimal precision.
    assert format_unit_fitting(time_consumed, 2) == format_unit_fitting(time.time(), 2)