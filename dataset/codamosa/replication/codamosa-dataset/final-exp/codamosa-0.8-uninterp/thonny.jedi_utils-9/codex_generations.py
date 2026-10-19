

# Generated at 2022-06-14 11:21:09.418506
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    pass

# Generated at 2022-06-14 11:21:17.655383
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import __version__
    if __version__[:4] in ["0.13", "0.14", "0.15", "0.16", "0.17"]:
        get_script_completions('import numpy\nnumpy.', 2, 9, "test.py")
    else:
        get_script_completions('import numpy\nnumpy.', 2, 9, "test.py")


if __name__ == '__main__':
    test_get_script_completions()

# Generated at 2022-06-14 11:21:28.621254
# Unit test for function get_script_completions
def test_get_script_completions():
    source = "import datetim"
    completions = get_script_completions(source, 0, len(source), "test")
    assert len(completions) == 1
    completion = completions[0]
    assert completion.type == "module"
    assert completion.name == "datetime"
    assert completion.complete == "datetime"
    assert completion.description == "Built-in module"



# Generated at 2022-06-14 11:21:50.995043
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.python.tree import PythonNode

    import jedi

    # Setting up a namespace
    ns = [{"a": 1, "b": 2}]

    # Testing the basic case
    source = 'a.'
    expected_completions = [ThonnyCompletion(name="a", complete="a", type=False, description="int", parent=None, full_name="a")]
    assert expected_completions == get_interpreter_completions(source, ns)

    # Testing many namespaces
    ns = [{"a": 1, "b": 2}, {"c": 7}, {"d": {"e": 2}}]
    source = 'd.'

# Generated at 2022-06-14 11:21:55.169414
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "range("
    namespaces = [{"range"}, {}]
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) == 1
    assert completions[0].complete == "range("



# Generated at 2022-06-14 11:22:03.005149
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = 'with open("path") as f: print f.'
    namespaces = [{'f': {'__class__': 'file', 'read': 'file.read'}}]
    expected = ['read']
    assert str_to_python(get_interpreter_completions(source, namespaces)) == expected


# Generated at 2022-06-14 11:22:08.550032
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = 'from fractions import *\n'
    namespaces = [{"gcd": 2, "fractions": 3}]

    completions = get_interpreter_completions(source, namespaces)

    assert len(completions) > 0
    assert "gcd" in [c.name for c in completions]
    assert "fractions" in [c.name for c in completions]

# Generated at 2022-06-14 11:22:12.718320
# Unit test for function get_definitions
def test_get_definitions():
    defs = get_definitions("print(", 0, 6, "")
    assert len(defs) == 1
    def0 = defs[0]
    assert def0.type == "statement"


# Generated at 2022-06-14 11:22:24.434440
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    version = jedi.__version__
    if version[:3] == "0.2" or version >= "0.21":
        # jedi 0.2 and newer can't handle text starting with newline
        source = """if 0:

    def testfunction(a, b):
        return a * b
    
    print(testfunction(2, 3))"""
    else:
        source = """


    def testfunction(a, b):
        return a * b
    
    print(testfunction(2, 3))"""

    res = get_script_completions(source, 5, 12, "test.py")
    assert "testfunction" in [v["complete"] for v in res]



# Generated at 2022-06-14 11:22:32.608303
# Unit test for function get_script_completions
def test_get_script_completions():
    from tkinter import Tk
    import threading
    import time
    import queue
    import jedi
    import os
    import tempfile
    import sys

    # TODO: use unittest.TestCase
    # TODO: test also with jedi 0.15 and 0.16

    app = Tk()
    app.withdraw()

    # save test script
    (_, filename) = tempfile.mkstemp(suffix=".py", text=True)

# Generated at 2022-06-14 11:23:00.474239
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    import os.path
    import sys
    sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..")))
    from tokenize import untokenize

    def run_test(source, row, column, filename, result):
        if isinstance(source, bytes):
            source = untokenize(source).decode("utf-8")
        output = get_script_completions(source, row, column, filename)
        if not isinstance(result, list):
            result = [result]
        assert len(output) == len(result)
        for item in result:
            assert item in output

    # Test case 1
    source = b"import sys;sys.\x80"
    row = 0

# Generated at 2022-06-14 11:23:13.421982
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.parse import tree

    def check_attrs(completion, name, complete, type, description, full_name, parent=None):
        assert completion.name == name
        assert completion.complete == complete
        assert completion.type == type
        assert completion.description == description
        assert completion.full_name == full_name
        assert completion.parent == parent

    # No namespace in scope
    completions = get_script_completions(source="", row=0, column=1, filename="")
    assert len(completions) == 0

    # Namespace in scope
    completions = get_script_completions(source="a", row=0, column=1, filename="")
    assert len(completions) == 1

# Generated at 2022-06-14 11:23:25.945068
# Unit test for function get_script_completions
def test_get_script_completions():
    from os.path import realpath, dirname, join
    from thonny.misc_utils import running_on_windows

    if running_on_windows():
        expected = [
            "print()",
            "print(1, 2, 3, sep=' ', end='\\n', file=sys.stdout, flush=False)",
        ]
        result = get_script_completions(
            "print", 3, 5, realpath(join(dirname(__file__), "..", "..", "..", "thonny.py"))
        )
        assert [c.name for c in result] == expected

    expected = [
        "print()",
        "print(1, 2, 3, sep=' ', end='\\n', file=sys.stdout, flush=False)",
    ]
    result = get_script

# Generated at 2022-06-14 11:23:33.048411
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    assert jedi.__version__[:4] in ["0.13", "0.14", "0.15", "0.16", "0.17"], "This test is only relevant for jedi versions 0.13-0.17"

    code = """
import sys
sys.path.
    """
    completions = get_script_completions(code, 3, 12, filename="dummy.py")
    assert len(completions) > 20

    for completion in completions:
        assert isinstance(completion, ThonnyCompletion)

# Generated at 2022-06-14 11:23:37.274180
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.evaluate import representation as er

    result = get_script_completions('"Hello'.splitlines(), 1, 7, "<fake-path>")
    assert len(result) == 1
    assert result[0].name == 'strip'

    # on older jedi (e.g. 0.13) we get results
    if len(result[0].infer()) == 1:
        assert isinstance(result[0].infer()[0], er.Instance)
    else:
        assert isinstance(result[0].infer()[0], er.KnownValue)

    # on newer jedi (e.g. 0.17)

# Generated at 2022-06-14 11:23:46.645537
# Unit test for function get_definitions
def test_get_definitions():
    from jedi import Script
    from thonny import get_workbench
    from thonny.shell import Shell
    from thonny.languageserver import jedi_utils
    from thonny.ui_utils import get_ui_for_buffer
    import os, shutil, sys
    workbench = get_workbench()
    workbench.create_environment()
    workbench.create_editor("HelloWorld.py")
    
    def create_temp_dir(dir_name):
        temp_dir = os.path.join(os.path.expanduser("~"), dir_name)
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.mkdir(temp_dir)
        return temp_dir
    
    temp_dir = create_temp_

# Generated at 2022-06-14 11:23:49.050466
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api import Interpreter


# Generated at 2022-06-14 11:24:01.792299
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    assert _using_older_jedi(jedi) == False

    source = "import os\n"
    filename = "test.py"
    row = 2
    column = 1

    # Test case 1, completion of 'o'
    completion = get_script_completions(source, row, column, filename)
    if completion != []:
        assert completion[0]["name"] == "os"
        assert completion[0]["complete"] == "os."

    # Test case 2, completion of 'os.'
    completion = get_script_completions(source, row, 2, filename)
    if completion != []:
        assert completion[0]["name"] == "getcwd"
        assert completion[0]["complete"] == "getcwd()"

    # Test case 3, completion of 'os

# Generated at 2022-06-14 11:24:15.037177
# Unit test for function get_script_completions
def test_get_script_completions():
    from parso.python import tree

    copts = get_script_completions("", 0, 0, "some_file_name.py")
    assert copts == []

    copts = get_script_completions("def func(a,b,c):\n  pass\nfunc(", 1, 9, "some_file_name.py")
    # TODO: There are 5 completions in jedi 0.15.0
    assert len(copts) > 3
    # TODO: FunctionParameter types seem to disappear in jedi 0.16.0
    # assert copts[0].type == "FunctionParameter"

    copts = get_script_completions(
        "from collections import ", 0, 24, "some_file_name.py"
    )
    assert len(copts) > 3

# Generated at 2022-06-14 11:24:23.241658
# Unit test for function get_definitions
def test_get_definitions():
    import test_runner
    import jedi
    jedi.settings.case_insensitive_completion = False

    script = """
    class A:
        def foo(self):
            pass
    """

    script_file = "test.py"
    defs = get_definitions(script, 2, 7, script_file)
    # Only one definition is available for the word 'foo' in the class definition
    assert len(defs) == 1
    # Check the type of the definition
    assert defs[0].type == 'function'
    # Check the full name of the definition
    assert defs[0].full_name == 'A.foo'
    # Check the line and column of the definition
    assert defs[0].line == 2
    assert defs[0].column == 7
    # Check the description of the definition

# Generated at 2022-06-14 11:24:55.006283
# Unit test for function get_script_completions
def test_get_script_completions():
    def check_result(result, expected):
        result_names = [c.name for c in result]
        assert set(result_names) == set(expected), "Got " + str(result_names)

    import jedi

    if _using_older_jedi(jedi):
        source = "import sys; sys.pa"
        result = get_script_completions(source, 0, len(source), "example.py")
        check_result(result, ["path", "path_hooks", "path_importer_cache"])
    else:
        source = "import sys; sys.pa"
        result = get_script_completions(source, 0, len(source), "example.py")
        check_result(result, ["path="])

        source = "import sys; sys.pa="
        result

# Generated at 2022-06-14 11:25:08.248687
# Unit test for function get_definitions
def test_get_definitions():
    from _test_utils import test_cases
    from os.path import dirname

    for (fn, source, line, column, expected_result) in test_cases("goto-definitions"):
        if expected_result.startswith("FAIL:"):
            continue

        expected_result = expected_result.split("\t")

        got = get_definitions(source, line, column, fn)
        got_len = len(got)
        assert got_len == len(
            expected_result
        ), "Expected %d definitions but got %d" % (len(expected_result), got_len)


# Generated at 2022-06-14 11:25:22.343106
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.jedi_utils_test import assertContains
    # With empty input, no completions
    completions = get_interpreter_completions("", [])

    assertContains(completions, "name", ["abs", "help", "max", "min", "sorted"])

    # With a single letter, some completions
    completions = get_interpreter_completions("a", [])

    assertContains(completions, "name", ["abs", "all"])

    # With a longer prefix, fewer completions
    completions = get_interpreter_completions("ab", [])

    assertContains(completions, "name", ["abs"])

    # With an unknown prefix, no completions
    completions = get_interpreter_completions("abc", [])

# Generated at 2022-06-14 11:25:27.946884
# Unit test for function get_definitions
def test_get_definitions():
    tmp = get_definitions(
        "a = 1\na = a.upper()\n", 2, 5, "src/Users/file.py"
    )  # Note path since jedi checks if it's in site-packages
    assert len(tmp) == 1
    assert tmp[0].module_name == "string"
    assert tmp[0].type == "function"
    assert tmp[0].full_name == "str.upper"
    assert tmp[0].line == 1228
    assert tmp[0].column == 0

# Generated at 2022-06-14 11:25:40.719358
# Unit test for function get_script_completions
def test_get_script_completions():
    from test.test_runner import get_jedi_version

    get_script_completions(
        source="from datetime i",
        row=0,
        column=21,
        filename="test.py",
    )

    assert len(get_script_completions(
        source="from datetime import",
        row=0,
        column=21,
        filename="test.py",
    )) > 0

    assert isinstance(get_script_completions(
        source="from datetime import datetime",
        row=0,
        column=21,
        filename="test.py",
    ), list)


# Generated at 2022-06-14 11:25:48.818608
# Unit test for function get_definitions
def test_get_definitions():
    from jedi import Interpreter
    from unittest.mock import MagicMock

    class TestCompletion:
        def __init__(self, name, description):
            self.name = name
            self.description = description

    # Test jedi.Interpreter.infer
    completion1 = TestCompletion("print", "def print")
    completion2 = TestCompletion("range", "def range")
    def mock_infer(row, column):
        completions = []
        if row == 1 and column == 5:
            completions.append(completion1)
        elif row == 2 and column == 5:
            completions.append(completion2)
        return completions
    Interpreter.infer = MagicMock()
    Interpreter.infer.side_effect = mock_infer

    #

# Generated at 2022-06-14 11:25:53.143900
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if _using_older_jedi(jedi):
        return

    assert len(get_interpreter_completions("aaa.", 1, 4, None)[0]) == 7
    assert len(get_interpreter_completions("from math import *; aaa.", 1, 19, None)[0]) == 1
    assert len(get_interpreter_completions("from collections import *; aaa.", 1, 25, None)[0]) == 1

# Generated at 2022-06-14 11:25:58.680228
# Unit test for function get_definitions
def test_get_definitions():
    source = """
    class Spam:
        def __init__(self, eggs):
            self._eggs = eggs
            
        def method1(self):
            pass 
        
        def method2(self, a, b):
            pass
    """
    # test case
    result = get_definitions(source, 11, 9, "spam.py")
    assert len(result) == 2
    assert result[0].line == 5
    assert result[1].line == 8

# Generated at 2022-06-14 11:26:05.868995
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import threading; threading.T"
    res = get_interpreter_completions(source, [], sys_path=["/usr/lib"])
    assert len(res) > 1
    assert res[0].name == "threading"


if __name__ == "__main__":
    test_get_interpreter_completions()

# Generated at 2022-06-14 11:26:15.066620
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter, Script

    s = "import abc; abc.ABC."
    c1 = get_interpreter_completions(s, [])
    c2 = Interpreter(s, []).complete()
    assert c1 == c2

    s = "abc."
    c1 = get_interpreter_completions(s, [])
    c2 = Interpreter(s, []).complete()
    assert c1 == c2

    s = "abc = None; abc."
    c1 = get_interpreter_completions(s, [])
    c2 = Interpreter(s, []).complete()
    assert c1 == c2

    # test with source code
    s = "import abc; abc.ABC."
    c1 = get_script_

# Generated at 2022-06-14 11:27:07.064453
# Unit test for function get_script_completions
def test_get_script_completions():
    """This function will show Thonny IDE how to mock
    get_script_completions function to check if your code is correct."""
    x = get_script_completions("froz", 1, 5, "test.py")
    import re

    assert x[0].name == "frozenset", re.sub("^\n*", "", x[0].name)
    assert x[0].complete == "frozenset("
    assert x[0].type == "class"
    return


# Generated at 2022-06-14 11:27:20.587854
# Unit test for function get_script_completions
def test_get_script_completions():
    import tempfile
    import shutil
    import sys
    import os

    import jedi


# Generated at 2022-06-14 11:27:31.975753
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Add local jedi folder to sys.path to import jedi
    import sys
    import os
    local_jedi_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'jedi'))
    sys.path.append(local_jedi_folder)

    import jedi

    source = "import sys\nsys.pa"
    namespaces = [{"name":"sys", "path": os.path.join(local_jedi_folder, "tests")}]
    completions = get_interpreter_completions(source, namespaces)
    # Check that "path" is in the completions
    assert [comp.name for comp in completions].count("path") == 1



# Generated at 2022-06-14 11:27:36.219044
# Unit test for function get_script_completions
def test_get_script_completions():
    _test_get_script_completions(get_script_completions, 'f1 = open("test.py", "', 4, 2)
    _test_get_script_completions(get_interpreter_completions, "open", 1, 0)



# Generated at 2022-06-14 11:27:49.903536
# Unit test for function get_script_completions
def test_get_script_completions():
    # Test that a bare jedi.Script works in both Jedi versions
    _jedi_test_both_versions(
        "im",
        source="",
        row=1,
        column=1,
        filename=__file__,
        expected_completion_texts=[
            'import',
            'imaginary',
        ],
    )
    _jedi_test_both_versions(
        "imp",
        source="",
        row=1,
        column=1,
        filename=__file__,
        expected_completion_texts=[
            'import',
        ],
    )

    # Test that sending sys_path works

# Generated at 2022-06-14 11:28:03.419430
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    def _validate_completions(completions):
        assert len(completions) == 2
        assert completions[0].name == "max"
        assert completions[0].complete == "max"
        assert completions[0].description == "Help on built-in function max in module builtins:\n\nmax(...)\n    max(iterable, *[, default=obj, key=func]) -> value\n    max(arg1, arg2, *args, *[, key=func]) -> value\n    \n    With a single iterable argument, return its largest item. The\n    default keyword-only argument specifies an object to return if\n    the provided iterable is empty.\n    With two or more arguments, return the largest argument.\n    "  # noqa

# Generated at 2022-06-14 11:28:13.579020
# Unit test for function get_script_completions
def test_get_script_completions():
    import unittest
    import jedi
    import jedi.evaluate.helpers

    class TestCase(unittest.TestCase):
        def setUp(self):
            # Workaround for Jedi issue #1466
            cached_filenames = jedi.evaluate.helpers._cached_filenames
            jedi.evaluate.helpers._cached_filenames = {}

        def tearDown(self):
            # Workaround for Jedi issue #1466
            jedi.evaluate.helpers._cached_filenames = cached_filenames

        def test_get_script_completions(self):
            completions = get_script_completions(
                source="[1, 2, 3] + ", row=0, column=9, filename=__file__
            )

# Generated at 2022-06-14 11:28:27.183747
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    from jedi.api import Script
    from thonny.jedi_utils import get_interpreter_completions

    source = "import os\nos.walk"
    namespaces = []
    namespaces.append({"__name__": "__main__", "__doc__": None, "__package__": None})
    interpreter = Interpreter(source, namespaces)
    comp = interpreter.complete()
    assert len(comp) == 1

    comp2 = get_interpreter_completions(source, namespaces)
    assert len(comp2) == 1
    assert comp2[0].name == comp[0].name

    comp3 = Script(source).complete()
    assert len(comp3) == 1
    assert comp3[0].name == comp[0].name



# Generated at 2022-06-14 11:28:38.802915
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    sys_path = [".", ".."]
    source = '"a".st'
    row, column = 0, 9
    filename="foo.py"
    script = jedi.Script(source, row, column, filename, sys_path=sys_path)
    script_completions = script.completions()
    assert script_completions[0].name == "startswith"

    source = '"a".st'
    row, column = 0, 9
    filename="foo.py"
    script = jedi.Script(source, row, column, filename)
    script_completions = script.completions()
    assert script_completions[0].name == "startswith"

# Generated at 2022-06-14 11:28:45.586814
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import patch

    def _patch_function(module, func_name, new_func):
        class _FakeModule:
            def __call__(self, *args, **kwargs):
                return new_func(*args, **kwargs)

        full_name = "thonny.plugins.jedi_utils." + func_name
        if isinstance(module, str):
            module_name = module
        else:
            module_name = module.__name__

        _prefix = module_name + "."
        if full_name.startswith(_prefix):
            func_name = full_name[len(_prefix) :]
        else:
            raise RuntimeError("Cannot find func_name in module name!")

        setattr(module, func_name, _FakeModule())


# Generated at 2022-06-14 11:30:16.902546
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    text = "import numpy as np; np.arange("
    namespaces = [{"foo": "bar"}]
    interpreter = Interpreter(text, namespaces)
    completions = get_interpreter_completions(text, namespaces)
    assert not completions
    assert interpreter.completions()

# Generated at 2022-06-14 11:30:24.864850
# Unit test for function get_script_completions
def test_get_script_completions():
    def assert_result(result, expected, expected_len):
        assert len(result) == expected_len
        for i in range(expected_len):
            assert result[i].name == expected[i]

    result = get_script_completions("foobar(", 0, 7, "<string>")
    assert_result(result, ["foo", "foobar"], 2)

    result = get_script_completions("foobar(", 1, 7, "<string>")
    assert_result(result, [], 0)

    result = get_script_completions("foobar(x=123,y=1", 0, 17, "<string>")
    assert_result(result, ["y"], 1)


# Generated at 2022-06-14 11:30:37.539493
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import sys
    import jedi
    import os
    import importlib
    from thonny.plugins.micropython.repl import REPL_INPUT_VAR
    from test.common import running_on_pi
    from thonny.plugins.micropython.mpfshell_backend import reset_device
    from thonny.plugins.micropython.utils import get_mpfshell_path
    from test.common import set_test_cwd
    from test.common import disable_backend_popups
    from thonny.plugins.micropython import MicroPythonProxy

    set_test_cwd()
    disable_backend_popups()
    reset_device()

    # Disable micropython if not running on rpi
    if not running_on_pi():
        return

    path = get_mpfshell

# Generated at 2022-06-14 11:30:46.655711
# Unit test for function get_script_completions
def test_get_script_completions():
    source = "import sys; sys.p"
    location = (2, 10)
    sys_path = ["temp"]
    completions = get_script_completions(
        source, location[0], location[1], filename="test.py", sys_path=sys_path
    )

    # Check number of completions
    assert len(completions) == 2

    # Check completions
    assert completions[0].name == "path"
    assert completions[1].name == "path_hooks"

    # Check sys.path was passed to Jedi
    assert completions[0].description == "list of strings"

# Generated at 2022-06-14 11:30:57.479524
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    from jedi.api.environment import get_chosen_interpreter_sys_path

    def completion_summaries(completions):
        return (c.name for c in completions)

    assert jedi.__version__ >= "0.13.0"

    source = """
import sys
sys.
"""
    completions = get_script_completions(source, 1, 8, "")
    assert completion_summaries(completions) == ["__displayhook__", "__doc__", "__excepthook__"]

    completions = get_script_completions(source, 1, 9, "")
    assert completion_summaries(completions) == ["__displayhook__", "__doc__", "__excepthook__"]

    completions = get_