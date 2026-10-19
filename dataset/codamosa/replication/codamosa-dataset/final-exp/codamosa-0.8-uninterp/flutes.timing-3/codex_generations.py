

# Generated at 2022-06-13 20:05:25.241522
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Writing to file")
    def save_file():
        with open("/tmp/new_file", "wb") as f:
            pickle.dump(load_file("/tmp/my_file"), f)

    with work_in_progress("Saving file"):
        with open("/tmp/new_file", "wb") as f:
            pickle.dump(load_file("/tmp/my_file"), f)

    with work_in_progress("Saving file and loading file"):
        save_file()



# Generated at 2022-06-13 20:05:31.189021
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("./file.pickle")
    del obj

    with work_in_progress("Saving file"):
        with open("./file.pickle", "wb") as f:
            pickle.dump({'a': 1}, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:05:34.943756
# Unit test for function work_in_progress
def test_work_in_progress():
    test_pass = True

    def foo():
        time.sleep(0.05)

    with work_in_progress("A fake test"):
        foo()

    return test_pass

if __name__ == "__main__":
    test_imported_module()
    test_work_in_progress()

# Generated at 2022-06-13 20:05:43.453558
# Unit test for function work_in_progress
def test_work_in_progress():
    # With function
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    data = load_file(os.path.join(os.path.dirname(__file__), "data.pkl"))
    assert type(data) == dict
    assert "a" in data

    # With block
    with work_in_progress("Saving file"):
        data["a"] = "b"
        with open(os.path.join(os.path.dirname(__file__), "data_modified.pkl"), "wb") as f:
            pickle.dump(data, f)


# Generated at 2022-06-13 20:05:48.416142
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Dummy task")
    def do_nothing():
        time.sleep(2.5)
    do_nothing()

    with work_in_progress("Dummy task"):
        time.sleep(2.5)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:05:53.149404
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Saving file")
    def f(path):
        time.sleep(1)
        print(f"Path: {path}")
        time.sleep(2)

    f("/path/to/some/file")

# Generated at 2022-06-13 20:05:58.265244
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(1)
        with work_in_progress("Loading module"):
            time.sleep(1)
    with work_in_progress("Saving file"):
        time.sleep(1)
        with work_in_progress("Saving module"):
            time.sleep(1)

# Test for function work_in_progress
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:04.003733
# Unit test for function work_in_progress
def test_work_in_progress():
    # Write file
    with work_in_progress("Saving file"):
        time.sleep(0.5)

    # Load file
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(0.5)
        return None

    obj = load_file("/path/to/some/file")


# Run tests
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:07.235725
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def dummy():
        time.sleep(0.5)
    dummy()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:12.972297
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

# Generated at 2022-06-13 20:06:17.275030
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress()
    def f():
        time.sleep(1.23)
    f()

# Generated at 2022-06-13 20:06:18.579691
# Unit test for function work_in_progress

# Generated at 2022-06-13 20:06:22.732203
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1)
    with work_in_progress("Testing work_in_progress"):
        time.sleep(2)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:06:32.036428
# Unit test for function work_in_progress
def test_work_in_progress():
    class SomeObject():
        def __init__(self):
            self.a = 1
            self.b = 2

    obj = SomeObject()

    @work_in_progress("Loading some object from file")
    def load_obj(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @work_in_progress("Saving some object to file")
    def save_obj(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    print()
    save_obj(obj, "obj.pkl")
    print()
    obj2 = load_obj("obj.pkl")
    print()
    save_obj(obj2, "obj2.pkl")

# Generated at 2022-06-13 20:06:36.966474
# Unit test for function work_in_progress
def test_work_in_progress():
    try:
        with work_in_progress():
            time.sleep(0.1)
    except KeyboardInterrupt:
        print() # To make output clearer in case of a KeyboardInterrupt or SIGINT

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:06:43.644601
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Sleeping for 1 second")
    def sleep_for_one_second():
        time.sleep(1)
    sleep_for_one_second()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:06:52.382729
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys
    from io import StringIO

    path = "/tmp/random.dat"
    cls = float

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    # test decorator
    @work_in_progress("Loading file")
    def load():
        return load_file(path)

    # test context manager
    with work_in_progress("Saving file"):
        save_file(path, cls(2))

    capture = StringIO()
    sys.stdout = capture

    load()
    save_file(path, cls(1))

    sys.stdout = sys

# Generated at 2022-06-13 20:06:59.770011
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test context manager
    with work_in_progress("Testing work_in_progress()"):
        time.sleep(2.5)

    # Test with decorator
    @work_in_progress("Testing work_in_progress()")
    def assert_task():
        time.sleep(2.6)
    assert_task()

    return True

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:08.582319
# Unit test for function work_in_progress
def test_work_in_progress():
    # This function is too awkward to be tested with real code
    # So we simply check if the decorator works as intended
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file") # noqa: F841

    with work_in_progress("Saving file"):
        with open("/path/to/some/file", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:07:18.587400
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit tests for function work_in_progress"""
    import time
    import pytest

    @work_in_progress("This is a test task")
    def time_spending_task():
        time.sleep(0.5)

    before = time.time()
    time_spending_task()
    after = time.time()
    print(f"before = {before}")
    print(f"after = {after}")
    print(f"time.time = {time.time()}")
    print(f"after - before = {after - before}")

    with pytest.raises(TypeError, match=r"work_in_progress() missing 1 required positional argument: 'desc'"):
        work_in_progress()


# Generated at 2022-06-13 20:07:30.001100
# Unit test for function work_in_progress
def test_work_in_progress():
    # For these tests, we are going to just use a simple function
    @work_in_progress()
    def wait(secs: float):
        time.sleep(secs)
    # Failing because we do not specify the testing framework
    with pytest.raises(ValueError):
        wait(1)
    @work_in_progress()
    def wait(secs: float):
        time.sleep(secs)
    wait(1)

# Generated at 2022-06-13 20:07:32.856317
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file():
        time.sleep(3)
        return "Hello World"
    assert load_file() == "Hello World"


# Generated at 2022-06-13 20:07:42.291185
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(3)

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("test_resources/test.obj")
    assert obj == ["test", 3, 1.2]

    with work_in_progress("Saving file"):
        with open("test_resources/test.obj", "wb") as f:
            pickle.dump(obj, f)

    time.sleep(3)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:07:44.064921
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test work_in_progress() function."""

    @work_in_progress("Loading file")
    def load_file(path):
        time.sl

# Generated at 2022-06-13 20:07:45.928229
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        obj = 0
        for i in range(10000000):
            obj += i
    assert obj == 49999995000000

# --

# Generated at 2022-06-13 20:07:54.251917
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
        return
    # Notice the time consumed should be shorter than the real time consumed
    # because the function doesn't actually load the file but just create a new
    # file and delete it.
    obj = load_file("test_work_in_progress")

# Generated at 2022-06-13 20:07:59.377243
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.42)

if __name__ == '__main__':

    # Logging
    print("Test - work_in_progress")
    test_work_in_progress()

    print("All tests done!")

# Generated at 2022-06-13 20:08:05.478875
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    @work_in_progress("Loading file")
    def test_load_file(path):
        return load_file(path)

    obj = test_load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        save_file("/path/to/some/file")


if __name__ == "__main__":
    with work_in_progress("Loading file"):
        time.sleep(1.5)
        print("I'm loaded!")
        time.sleep(2.0)


# Generated at 2022-06-13 20:08:08.542759
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Wait for me!")
    def wait():
        time.sleep(0.4)
        return "I'm back"

    assert wait() == "I'm back"


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:08:22.425103
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys
    import time
    import io

    # Redirect stdout to buffer
    sys.stdout = buffer = io.StringIO()

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("tests/fake_data.pickle")

    with work_in_progress("Saving file"):
        with open("tests/data.pickle", "wb") as f:
            pickle.dump(obj, f)

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check if the output is valid.
    lines = buffer.getvalue().splitlines()
    assert lines[0] == "Loading file... done. (0.09s)"

# Generated at 2022-06-13 20:08:33.995847
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys

    with work_in_progress(desc="Work in progress") as _:
        time.sleep(1)
    sys.stdout.flush()

# Run tests if invoked as main module
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:08:37.671104
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Time consuming")
    def time_consuming():
        time.sleep(0.02)
    time_consuming()

# Generated at 2022-06-13 20:08:45.555845
# Unit test for function work_in_progress
def test_work_in_progress():
    global t, val1, val2, val3
    t = time.time()
    val1 = "string"
    with work_in_progress("Waiting for"):
        time.sleep(2)

    val2 = "another_string"
    with work_in_progress("Waiting for"):
        time.sleep(3)

    val3 = "wait_for_longer"
    with work_in_progress("Waiting for"):
        time.sleep(5)

# Run the unit test
test_work_in_progress()

# Generated at 2022-06-13 20:08:47.783517
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress(desc="Unit test")
    def inner():
        time.sleep(0.01)
    inner()

# Generated at 2022-06-13 20:08:54.843830
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import tempfile
    import time
    import pickle
    import contextlib

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(path, obj):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode="wb+t") as f:
        # Save an object to the file
        obj = None
        time.sleep(0.5)
        with contextlib.suppress(Exception):
            with work_in_progress("Saving file"):
                obj = {"name": "foo", "age": 23}
                f.write(pickle.dumps(obj))
            # Load

# Generated at 2022-06-13 20:08:56.716989
# Unit test for function work_in_progress
def test_work_in_progress():

    @work_in_progress("Test work_in_progress")
    def dummy_work(sleeptime):
        time.sleep(sleeptime)

    dummy_work(1)
    dummy_work(2)
    dummy_work(3)

# Generated at 2022-06-13 20:09:02.777121
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("This is a test") as _:
        time.sleep(2)
    @work_in_progress("This is another test")
    def func():
        time.sleep(2)
        return 42
    assert func() == 42


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-13 20:09:08.711997
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys

    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(2)
        return 1

    with open(sys.argv[0], "rb") as f:
        content = f.read()

    with work_in_progress("Saving file"):
        time.sleep(2)
        with open(sys.argv[0], "wb") as f:
            f.write(content)

if __name__ == '__main__':
    # python src/progress.py
    test_work_in_progress()

# Generated at 2022-06-13 20:09:13.306299
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import shutil
    
    with work_in_progress("Copying"):
        shutil.copyfile(__file__, "/tmp/__init__.py")
        
    with work_in_progress("Removing"):
        os.remove("/tmp/__init__.py")

# Generated at 2022-06-13 20:09:19.562514
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test with a function
    @work_in_progress("Loading file")
    def load_file(path: str):
        with open(path, "rb") as f:
            return pickle.load(f)

    # Test with a code block
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

# Generated at 2022-06-13 20:09:30.689953
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
    print("Loaded object:", obj)
    save_file("/path/to/some/file", obj)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:34.199639
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving foo"):
        time.sleep(0.4)

    def f():
        with work_in_progress("Saving foo"):
            time.sleep(0.4)

    f()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:09:35.476896
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test print") as w:
        time.sleep(5)

# Generated at 2022-06-13 20:09:40.784408
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test with a function
    @work_in_progress("Loading file")
    def load_file(path):
        time.sleep(3.52)
        return 0

    assert load_file("/path/to/some/file") == 0, "test_work_in_progress() failed"

    # Test with a code block
    with work_in_progress("Saving file"):
        time.sleep(3.78)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:09:47.604134
# Unit test for function work_in_progress
def test_work_in_progress():
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    with work_in_progress("Loading file"):
        obj = load_file("/path/to/some/file")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)

    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 20:09:54.591229
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

    obj = load_file("test.pkl")
    with open("test.pkl", "rb") as f:
        assert pickle.load(f) == obj

    save_file("test.pkl", obj)
    with open("test.pkl", "rb") as f:
        assert pickle.load(f) == obj


# Generated at 2022-06-13 20:09:55.686497
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress function"):
        time.sleep(3)

# Generated at 2022-06-13 20:09:57.073886
# Unit test for function work_in_progress
def test_work_in_progress():
    time.sleep(1)
    with work_in_progress("Test"):
        time.sleep(1)

# Generated at 2022-06-13 20:10:01.791372
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Testing work_in_progress() function")
    def time_consuming_function():
        time.sleep(2)

    time_consuming_function()

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:07.876689
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    #
    obj = load_file("/path/to/some/file")
    #
    with work_in_progress("Saving file"):
        with open(path, "wb") as f:
            pickle.dump(obj, f)


if __name__ == '__main__':
    test_work_in_progress()
    pass

# Generated at 2022-06-13 20:10:13.631639
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Saving file"):
        pass

# Generated at 2022-06-13 20:10:23.266427
# Unit test for function work_in_progress
def test_work_in_progress():
    import os
    import pickle

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(__file__)
    assert isinstance(obj, dict)
    assert obj["test_work_in_progress"] == test_work_in_progress

    with work_in_progress("Saving file"):
        with open(os.path.join(os.getcwd(), "test_work_in_progress_out.pickle"), "wb") as f:
            pickle.dump(obj, f)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:28.501058
# Unit test for function work_in_progress
def test_work_in_progress():
    # testing loading
    test_obj = {"a": 1, "b": 2}
    path_to_file = "/tmp/test_work_in_progress.pickle"
    with open(path_to_file, "wb") as f:
        pickle.dump(test_obj, f)

    # this should print "Loading file... done. (0.00s)"
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file(path_to_file)
    assert(obj == test_obj)

    # testing saving
    # this should print "Saving file... done. (0.00s)"

# Generated at 2022-06-13 20:10:35.349643
# Unit test for function work_in_progress
def test_work_in_progress():
    def test_decorated_function(sleep_time):
        @work_in_progress()
        def function():
            time.sleep(sleep_time)
            return
        function()

    def test_context_manager(sleep_time):
        with work_in_progress():
            time.sleep(sleep_time)
            return

    def test():
        test_decorated_function(sleep_time=0.2)
        test_context_manager(sleep_time=0.2)

    test()

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:43.316558
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file('test_data/test_file.txt')

    @work_in_progress("Saving file")
    def save_file(path, data):
        with open(path, "wb") as f:
            pickle.dump(data, f)

    save_file('test_data/test_file.txt', obj)


if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:10:48.274679
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    import subprocess
    with work_in_progress("Sleep for 5 second"):
        time.sleep(5)
    with work_in_progress("Wait for exit of sleep 5"):
        subprocess.run(["sleep", "5"])

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:10:57.067028
# Unit test for function work_in_progress
def test_work_in_progress():
    import io
    import sys

    def restore_stdout():
        sys.stdout = sys.__stdout__

    def hook_stdout(print_function=print, *args, **kwargs):
        sys.stdout = io.StringIO()
        old_print(*args, **kwargs)
        output = sys.stdout.getvalue().strip()
        sys.stdout.close()
        return output

    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    def save_file(obj, path):
        with open(path, "wb") as f:
            pickle.dump(obj, f)

    def _test():
        obj = {
            1: 2,
            3: 4,
            5: 6,
        }

# Generated at 2022-06-13 20:11:02.760215
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("test_pickle.pkl")
    assert obj == [1, 2, 3, 4, 5]

    with work_in_progress("Saving file"):
        with open("test_pickle.pkl", "wb") as f:
            pickle.dump(obj, f)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:07.983693
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading"):
        time.sleep(1)
        print("Some block")
        time.sleep(2)
    @work_in_progress("Loading")
    def _():
        time.sleep(1)
        print("Some block")
        time.sleep(2)
    _()

#----------------------------------------------------------------------------------------------------------------------#
# vim: set ft=python ts=4 sw=4 tw=0 fenc=utf-8 ff=unix :

# Generated at 2022-06-13 20:11:15.709556
# Unit test for function work_in_progress
def test_work_in_progress():
    """Test the function work_in_progress"""

    print("Testing the function work_in_progress")

    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert obj


test_work_in_progress()

# Generated at 2022-06-13 20:11:23.566716
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Test for function :func:`work_in_progress`."""
    print(__doc__, end='')
    with work_in_progress("Testing function work_in_progress"):
        time.sleep(0.02)

# Generated at 2022-06-13 20:11:27.587283
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

# Generated at 2022-06-13 20:11:32.022746
# Unit test for function work_in_progress
def test_work_in_progress():
    for desc in ["Loading file", "Saving file"]:
        for i in range(3):
            with work_in_progress(desc):
                time.sleep(1)
            

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:11:38.058567
# Unit test for function work_in_progress
def test_work_in_progress():
    def _test(seconds: float):
        @work_in_progress("This is just a test")
        def inner_test():
            time.sleep(seconds)
        inner_test()
    _test(0.5)
    _test(1.0)
    _test(2.0)
    with work_in_progress("This is a test"):
        time.sleep(3.0)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:45.850803
# Unit test for function work_in_progress
def test_work_in_progress():
    # Test for context manager
    with work_in_progress("Creating a string"):
        s = "a" * 1000
    # Test for decorator
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    obj = load_file("tests/unittest_work_in_progress.pkl")
    assert obj == "abcd"


# Module Test
if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:11:53.914972
# Unit test for function work_in_progress
def test_work_in_progress():
    import unittest
    import pickle
    import tempfile
    import os
    import random

    class TestWorkInProgress(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.data_size = 1024*1024*10 # 10Mb
            cls.data = b"".join([random.choice(b"0123456789").to_bytes(1, "big") for _ in range(cls.data_size)])
        def test_work_in_progress(self):
            with tempfile.TemporaryDirectory() as dir_path:
                path = os.path.join(dir_path, "test.data")
                with open(path, "wb") as f:
                    f.write(TestWorkInProgress.data)

# Generated at 2022-06-13 20:12:02.055073
# Unit test for function work_in_progress
def test_work_in_progress():
    file_content = {
        "Key1": "Value1",
        "Key2": "Value2",
        "Key3": "Value3",
    }
    with work_in_progress("Saving file"):
        with tempfile.TemporaryFile(mode="w+b") as f:
            pickle.dump(file_content, f)

    with work_in_progress("Loading file"):
        with tempfile.TemporaryFile(mode="w+b") as f:
            pickle.dump(file_content, f)
            f.seek(0)
            loaded_content = pickle.load(f)
    assert loaded_content == file_content

# Generated at 2022-06-13 20:12:09.217188
# Unit test for function work_in_progress
def test_work_in_progress():
    import sys
    import os

    parser = argparse.ArgumentParser(description="Unit test for function work_in_progress.")
    parser.add_argument("--mode", action="store", default="both", 
                        choices=["both", "decorator", "context"],
                        help="Mode of demonstration.")
    args = parser.parse_args()

    print("Compute a 3 million-by-3 million matrix multiplication. (Expect to take at least several minutes.)")
    if args.mode == "both" or args.mode == "decorator":
        @work_in_progress("Computing with decorator")
        def compute_matrix_decorator():
            a = np.random.rand(3000000, 3)
            b = np.random.rand(3000000, 3)
            return a @ b
        c = compute

# Generated at 2022-06-13 20:12:12.090834
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(10)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:12:16.368469
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Test work_in_progress function"):
        print("Test work_in_progress function")


if __name__ == '__main__':
    # Test
    test_work_in_progress()

# Generated at 2022-06-13 20:12:27.310413
# Unit test for function work_in_progress
def test_work_in_progress():
    def test_f():
        time.sleep(0.1)

    with work_in_progress("test_work_in_progress"):
        test_f()

# Generated at 2022-06-13 20:12:35.862816
# Unit test for function work_in_progress
def test_work_in_progress():
    """Unit test for function work_in_progress.

    .. note::

        This unit test is executed only if the pytest module is available.
    """

    def square(x: int) -> int:
        """Return x square."""
        return x ** 2

    with work_in_progress("Testing function work_in_progress"):
        assert square(100) == 10000
    assert True == True

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "--capture=sys", "-s", "--durations=0", __file__])

# Generated at 2022-06-13 20:12:44.742713
# Unit test for function work_in_progress
def test_work_in_progress():
    logging.getLogger().setLevel(logging.DEBUG)
    file_path = "/tmp/_file_save_test.pkl"

    save_obj = {"a": ["b", "c"], "d": [1, 2, 3, 4]}

    with work_in_progress("Saving file"):
        with open(file_path, "wb") as f:
            pickle.dump(save_obj, f)
    assert os.path.isfile(file_path)

    with work_in_progress("Loading file"):
        with open(file_path, "rb") as f:
            load_obj = pickle.load(f)
    assert save_obj == load_obj

    # Delete the file
    os.remove(file_path)

# Generated at 2022-06-13 20:12:54.141079
# Unit test for function work_in_progress
def test_work_in_progress():
    import subprocess
    import io

    def capture_output(command: str, cwd: str = os.getcwd(), input: str = None):
        """Capture output of a program through its stdout and stderr."""
        if input:
            process = subprocess.Popen(command, cwd=cwd,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            out, err = process.communicate(input.encode('utf-8'))
        else:
            process = subprocess.Popen(command, cwd=cwd,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            out, err = process.communicate()


# Generated at 2022-06-13 20:12:57.285240
# Unit test for function work_in_progress
def test_work_in_progress():
    import time
    with work_in_progress("Testing work_in_progress"):
        time.sleep(0.1)

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:13:02.040138
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Saving file")
    def save(path):
        with open(path, "wb") as f:
            f.write(b"a" * (1 << 20))
    save("/tmp/temp_file")

if __name__ == '__main__':
    test_work_in_progress()

# Generated at 2022-06-13 20:13:04.585201
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(2)
# test_work_in_progress()

# Generated at 2022-06-13 20:13:14.578316
# Unit test for function work_in_progress
def test_work_in_progress():
    def call(func):
        from io import BytesIO
        buf = BytesIO()

        def bytes_print(*args, **kwargs):
            print(*args, file=buf, **kwargs)

        with contextlib.redirect_stdout(buf):
            return func(), buf.getvalue()

    import sys
    import io
    import tempfile

    def test_work_in_progress():
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            with work_in_progress("Test"):
                time.sleep(0.1)
                print("OK")
            assert buf.getvalue() == "Test... OK\ndone. (0.10s)\n"


# Generated at 2022-06-13 20:13:19.053404
# Unit test for function work_in_progress
def test_work_in_progress():
    r"""Unit test for function work_in_progress."""
    total_consumed = 0.0
    for i in range(3):
        with work_in_progress(f"Test #{i + 1}"):
            time.sleep(1.0)
            total_consumed += 1.0
    assert round(total_consumed, 1) == 3.0

# Generated at 2022-06-13 20:13:21.488046
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(2)
    time.sleep(2)
    with work_in_progress("Loading file"):
        time.sleep(2)


# Generated at 2022-06-13 20:13:45.347971
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

# Generated at 2022-06-13 20:13:48.079810
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Testing work_in_progress"):
        time.sleep(1)

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:13:53.191746
# Unit test for function work_in_progress
def test_work_in_progress():
    from .context import work_in_progress
    from random import randint

    with work_in_progress("Sleeping"):
        time.sleep(3)

    @work_in_progress("A function with a return")
    def add(a, b):
        time.sleep(randint(1, 4))
        return a + b

    assert add(3, 5) == 8
    time.sleep(1)

# Generated at 2022-06-13 20:13:57.866729
# Unit test for function work_in_progress
def test_work_in_progress():
    import math
    from my_package.measure_time import work_in_progress
    with work_in_progress("Calculating pi"):
        for i in range(100000000):
            q = math.sqrt(i)

# test_work_in_progress()

# Generated at 2022-06-13 20:14:05.268496
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Loading file")
    def load_file(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")

    with work_in_progress("Saving file"):
        with open("/path/to/some/other/file", "wb") as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:11.455225
# Unit test for function work_in_progress
def test_work_in_progress():
    import pickle
    import tempfile
    obj = object()

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "obj.pkl")

        with work_in_progress("Saving file"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)

        @work_in_progress("Loading file")
        def load_file(path):
            with open(path, "rb") as f:
                return pickle.load(f)

        obj2 = load_file(path)
        assert obj is obj2

if __name__ == "__main__":
    test_work_in_progress()

# Generated at 2022-06-13 20:14:14.367885
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("Work in progress")
    def test_function():
        time.sleep(0.1)
        return 0

    assert test_function() == 0

# Generated at 2022-06-13 20:14:18.771058
# Unit test for function work_in_progress
def test_work_in_progress():
    begin_time = time.time()
    time.sleep(1)
    with work_in_progress("Testing"):
        time.sleep(0.3)
    time_consumed = time.time() - begin_time
    assert time_consumed > 1.3

# Generated at 2022-06-13 20:14:29.188989
# Unit test for function work_in_progress
def test_work_in_progress():
    with work_in_progress("Loading file"):
        time.sleep(0.5)


if __name__ == "__main__":
    # Display doc of functions and classes
    import os
    import sys
    import inspect

    # Do not run if this file is imported
    if __package__ is None:
        # If this file is run directly, enter the parent directory
        # Then import all modules
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        for _, module_name, is_pkg in pkgutil.walk_packages(
                ['.'], prefix=__package__ + '.'):
            if is_pkg:
                continue
            module = importlib.import_module(module_name)

# Generated at 2022-06-13 20:14:37.059634
# Unit test for function work_in_progress
def test_work_in_progress():
    @work_in_progress("loading file")
    def load_file(path: str):
        time.sleep(2.34)
        with open(path, "rb") as f:
            return pickle.load(f)

    obj = load_file("/path/to/some/file")
    assert isinstance(obj, dict)

    with work_in_progress("saving file"):
        time.sleep(5.67)
        with open(path, "wb") as f:
            pickle.dump(obj, f)