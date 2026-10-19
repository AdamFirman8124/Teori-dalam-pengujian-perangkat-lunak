

# Generated at 2022-06-14 11:21:38.091909
# Unit test for function get_definitions
def test_get_definitions():
    assert get_definitions("import json", 0, 0, "").__class__.__name__ == "Definitions"

    defs = get_definitions("import json", 0, 0, "")
    for def_obj in defs:
        assert def_obj.module_name == "json" or def_obj.module_name == "builtins"
        assert def_obj.line is not None
        assert def_obj.column is not None
        assert def_obj.in_builtin_module() in [True, False]

    assert get_definitions("json.loads()", 0, 0, "").__class__.__name__ == "Definitions"

    defs = get_definitions("json.loads()", 0, 0, "")

# Generated at 2022-06-14 11:21:47.804303
# Unit test for function get_script_completions
def test_get_script_completions():
    def get_completions(source, row, column):
        completions = []
        for completion in get_script_completions(source, row, column, "main"):
            completions.append(
                {
                    "name": completion.name,
                    "complete": completion.complete,
                    "type": completion.type,
                    "description": completion.description,
                    "parent": completion.parent,
                    "full_name": completion.full_name,
                }
            )
        return completions

    # Empty source, jedi returns only builtin completions

# Generated at 2022-06-14 11:21:58.579530
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    completions = get_interpreter_completions("import os", [], sys_path=["/"])

    assert any("os.environ" == c.name for c in completions)
    assert any("os.path" == c.name for c in completions)

    if _using_older_jedi(jedi):
        assert any("os.path.join(" == c.complete for c in completions)
    else:
        assert any("os.path.join(" == c.name for c in completions)


if __name__ == "__main__":
    test_get_interpreter_completions()

# Generated at 2022-06-14 11:22:09.008900
# Unit test for function get_script_completions
def test_get_script_completions():
    from tkinter import Tk

    from thonny import get_workbench
    from thonny.shell import ShellCodeView
    from thonny.plugins.cpython.backend import BackendProxy

    bp = BackendProxy()
    bp.initialize({})
    get_workbench().set_debugger_backend(bp)
    bp.start_backend()

    root = Tk()
    root.withdraw()
    cv = ShellCodeView(root)
    cv.text.insert("end", "import numpy\n" "numpy.sqrt()")
    cv.text.mark_set(cv.INSERT, "2.0")
    source = cv.text.get("1.0", "end")


# Generated at 2022-06-14 11:22:15.725664
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter

    interpreter = Interpreter("import sys; sys.p", [], sys_path=["."])
    completions = get_interpreter_completions(
        interpreter.source, interpreter.namespaces, ["."]
    )
    assert len(completions) != 0



# Generated at 2022-06-14 11:22:24.600511
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import tkinter\ntkinter."
    completions = get_interpreter_completions(source, [])
    completion_names = [c.name for c in completions]
    assert "Tk" in completion_names
    assert "Tkinter" in completion_names
    assert "Entry" in completion_names
    assert "Canvas" in completion_names
    assert "Frame" in completion_names
    assert "Button" in completion_names

if __name__ == '__main__':
    test_get_interpreter_completions()

# Generated at 2022-06-14 11:22:35.058579
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest

    class TestCase(unittest.TestCase):
        def test_bunch_of_cases(self):
            script = """
                import sys

                class X:
                    def __init__(self):
                        self.instance_attr = 1

                    @staticmethod
                    def static_attr():
                        pass
                    str
                    
                    class Nes
                    class Nested:
                        def nested_method(self):
                            pass
                        
                        class NoClass
                """
            namespaces = [
                dict(
                    globals=dict(
                        sys=sys,
                        X=X,
                        a_local_var=True,
                        a_local_func=lambda: 1,
                    )
                )
            ]
            completions = get_interpreter_completions(script, namespaces)



# Generated at 2022-06-14 11:22:47.540684
# Unit test for function get_script_completions
def test_get_script_completions():
    import importlib
    import os
    import tempfile
    import unittest

    try:
        script_directory = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        script_directory = os.path.join(
            os.path.dirname(os.path.abspath(__package__)), "backend"
        )
    fixture_directory = os.path.join(script_directory, "..", "test", "fixtures")
    jedi_path = os.path.join(fixture_directory, "jedi")
    os.environ["PYTHONPATH"] = jedi_path

    with tempfile.TemporaryDirectory() as d:
        os.environ["PYTHONPATH"] = jedi_path + os.pathsep + d

# Generated at 2022-06-14 11:22:53.779597
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api import Interpreter

    compl = get_interpreter_completions("""
if False:
    from foo import """, [Interpreter.get_namespaces()[0]])
    assert compl == [
        ThonnyCompletion(
            name="foo",
            complete="foo",
            type="module",
            description="Module foo",
            parent=None,
            full_name="foo",
        )
    ]

# Generated at 2022-06-14 11:23:00.834389
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import time

    jedi.settings.case_insensitive_completion = True

    start = time.time()
    for i in range(1000):
        get_interpreter_completions(
            "import math\nprint(int('f', 16))\nmath.frexp(42)", [{"math": math}]
        )
    print(time.time() - start)

    start = time.time()
    for i in range(1000):
        jedi.Interpreter(
            "import math\nprint(int('f', 16))\nmath.frexp(42)", [{"math": math}]
        ).complete()
    print(time.time() - start)


if __name__ == "__main__":
    test_get_interpreter_completions()

   

# Generated at 2022-06-14 11:23:19.478892
# Unit test for function get_script_completions
def test_get_script_completions():
    import os
    import sys

    # get location of the test file relative to current dir
    filename = os.path.relpath(os.path.join(os.path.dirname(__file__), "testfiles", "source.py"))

    with open(filename, "r", encoding="utf-8") as source_file:
        source = source_file.read()
        row, column = 2, 23
        completions = get_script_completions(source, row, column, filename, sys_path=sys.path)
        completions_str = [str(c) for c in completions]
        if "module_1_1" in completions_str:
            # with jedi>=0.17.0, I expected the completions include only "module_1_1"
            assert "module_1" not in comple

# Generated at 2022-06-14 11:23:24.107620
# Unit test for function get_definitions
def test_get_definitions():
    result = get_definitions(
        "import sys\nsys\n", 1, 3, ""
    )  # sys should point to sys module
    assert len(result) == 1
    assert "sys" in result[0].description
    assert result[0].type == "module"

# Generated at 2022-06-14 11:23:32.354286
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from types import SimpleNamespace
    import json

    source = "import random"
    namespaces = [{"a": SimpleNamespace(a=1, b=2)}]
    json_data = json.dumps(get_interpreter_completions(source, namespaces))
    assert (
        json_data
        == '[{"name": "a", "complete": "a", "type": "instance", "description": "", "parent": "", "full_name": ""}, {"name": "b", "complete": "b", "type": "instance", "description": "", "parent": "", "full_name": ""}, {"name": "None", "complete": "None", "type": "instance", "description": "", "parent": "", "full_name": ""}]'
    )



# Generated at 2022-06-14 11:23:44.596476
# Unit test for function get_definitions
def test_get_definitions():
    # test.py
    #
    #     def aaa():
    #         pass
    #
    #     bbb = aaa
    #
    # ccc = aaa()
    #
    # bbb()
    #
    # import test
    # test.aaa()
    # test.bbb()

    print(get_definitions("test.py", 6, 4, "test.py"))  # should be 2 items: def aaa and def bbb
    print(get_definitions("test.py", 10, 4, "test.py"))  # should be 2 items: def aaa and def bbb

    print(get_definitions("test.py", 1, 6, "test.py"))  # should be 1 item: def aaa

# Generated at 2022-06-14 11:23:53.809578
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if hasattr(jedi.Interpreter, "completions"):
        # up to jedi 0.17
        output = get_interpreter_completions(
            "import math\nmath.pi", [{}]
        )
        assert output[0].name == "pi"

        # argument completions
        output = get_interpreter_completions("str(1.1)", [{}])
        assert output[0].name == "base"

        # from import completions
        output = get_interpreter_completions("from tkinter import *", [{}])
        assert output[0].name == "Canvas"

        # from import completions part 2 (test for #1200)

# Generated at 2022-06-14 11:24:00.736528
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock

    def get_script_completions_mock(source, row, column, filename, sys_path=None):
        completion = Mock()
        completion.name = "name"
        completion.complete = "complete"
        completion.type = 1
        completion.description = "description"
        completion.parent = "parent"
        completion.full_name = "full_name"
        return [completion]

    completions = get_script_completions_mock("source", 10, 20, "filename", sys_path=[])

    assert completions[0]["name"] == "name"
    assert completions[0]["complete"] == "complete"
    assert completions[0]["type"] == 1
    assert completions[0]["description"] == "description"
    assert comple

# Generated at 2022-06-14 11:24:04.914891
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.helper import jedi_completion_samples
    sample_completions = jedi_completion_samples.sample_completions
    source = "import dateti"
    namespaces = [{"__name__": "__main__", "__builtins__": __builtins__}]
    sys_path = ["/home/user/folder1", "/home/user/folder2"]
    completions = get_interpreter_completions(source, namespaces, sys_path)

    # Test get_completions:
    assert len(sample_completions) == len(completions)
    assert sample_completions[0].name == completions[0].name
    assert sample_completions[0].complete == completions[0].complete

# Generated at 2022-06-14 11:24:15.653407
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.parser_utils import get_statement_of_position
    from parso.python.tree import ExprStmt, Name, KeywordStatement
    from jedi.evaluate.representation import KeywordArgument

    source = """
import sys
sys.path[-1] = '1'
sys.path[-2] = '2'
sys.pa
    """

    namespaces = [
        {"sys": sys},
        {"sys": sys},
    ]

    defs = get_interpreter_completions(source, namespaces, ["path"])[0]
    assert defs.description == "sys.path: List[str]"



# Generated at 2022-06-14 11:24:23.738384
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    import sys

    __module__ = get_script_completions
    comp = get_script_completions("import sys", 0, 8, "completions_test.py", sys_path=[])
    comp2 = get_script_completions("import sys", 0, 8, "completions_test.py", sys_path=None)
    comp3 = get_script_completions("import sys", 0, 8, "completions_test.py", sys_path=[__file__])
    comp4 = get_script_completions("import sys", 0, 8, "completions_test.py", sys_path=[""])

# Generated at 2022-06-14 11:24:33.648254
# Unit test for function get_definitions
def test_get_definitions():
    defs = get_definitions("import os", 0, 10, "<stdin>")
    assert len(defs) == 1
    def0 = defs[0]
    assert def0.type == "module"
    assert def0.name == "os"
    assert def0.module_name == "os"
    assert def0.line is None
    assert def0.column is None
    assert def0.module_path == "os"


if __name__ == "__main__":
    import pytest

    pytest.main(["jedi_utils.py"])

# Generated at 2022-06-14 11:24:58.420788
# Unit test for function get_script_completions
def test_get_script_completions():
    import os
    import sys
    import unittest

    version = sys.version_info[0]

    # test for use of jedi version 0.17.2
    class TestGetScriptCompletions(unittest.TestCase):
        def test_get_script_completions(self):
            # test get_script_completions function
            # saves location of script directory
            test_path = os.path.dirname(__file__)
            if version == 2:
                test_path = test_path.encode("utf-8")

            # path of python test file
            path = os.path.join(test_path, "test_get_script_completions.py")

            # get completions from jedi
            completions = get_script_completions('os.path.join("", "')

# Generated at 2022-06-14 11:25:10.261130
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.globals import get_workbench
    from thonny.plugins.jedi_utils import get_interpreter_completions
    NBTestRunner = get_workbench().get_plugin("nbtestrunner")
    test = "import os\n"
    completions = get_interpreter_completions(test, [], sys_path=NBTestRunner.sys_path)
    assert(len(completions) == 0)
    test = "import sys\n"
    completions = get_interpreter_completions(test, [], sys_path=NBTestRunner.sys_path)
    assert(len(completions) > 0)
    # Test completion for new jedi version
    test = "import sys\n"

# Generated at 2022-06-14 11:25:18.963618
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock
    import jedi

    script = Mock()
    script.completions = Mock()
    jedi.Script = Mock(return_value=script)

    source = "import"
    row = 1
    column = 7

    get_script_completions(source, row, column)
    jedi.Script.assert_called_with(source, row, column, None)
    script.completions.assert_called()



# Generated at 2022-06-14 11:25:28.268269
# Unit test for function get_definitions
def test_get_definitions():
    expected = [
        Completion(name="_inspect", complete="_inspect", type="", description="", parent="", full_name=""),
        Completion(name="inspect", complete="inspect", type="", description="", parent="", full_name=""),
        Completion(name="sys", complete="sys", type="", description="", parent="", full_name=""),
        Completion(name="thread", complete="thread", type="", description="", parent="", full_name=""),
        Completion(name="time", complete="time", type="", description="", parent="", full_name=""),
        Completion(name="types", complete="types", type="", description="", parent="", full_name=""),
    ]
    source = "import inspect, sys, thread, time, types"

# Generated at 2022-06-14 11:25:40.871720
# Unit test for function get_definitions
def test_get_definitions():
    from jedi import Script
    from jedi.api import classes
    
    for jedi_version in ["0.13", "0.14", "0.15", "0.16", "0.17", "0.18"]:
        print("Running test with jedi version " + jedi_version)
        source = '''
            import unittest
            class Test(unittest.TestCase):
                def test(self):
                    pass
        '''
        row = 4
        col = 12
        filename = ""
        definitions = get_definitions(source, row, col, filename)
        assert(isinstance(definitions, list))
        assert(isinstance(definitions[0], classes.Definition))
        assert(len(definitions) == 1)
        assert(definitions[0].name == "self")
       

# Generated at 2022-06-14 11:25:43.103062
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    from jedi.parser import tree
    from jedi.parser_utils import get_statement_of_position


# Generated at 2022-06-14 11:25:56.482632
# Unit test for function get_definitions
def test_get_definitions():
    import jedi
    from jedi.api.classes import Namespace

    assert len(get_definitions("a = 1\na", 1, 1, "dummy.py")) == 0
    assert len(get_definitions("a = 1\na", 1, 2, "dummy.py")) == 0

    assert len(get_definitions("b = 1\nb", 1, 1, "dummy.py")) == 0
    assert len(get_definitions("b = 1\nb", 1, 2, "dummy.py")) == 0

    # Only jedi-0.17 supports assignment completion
    if _using_older_jedi(jedi):
        assert len(get_definitions("b = 1\nb", 1, 3, "dummy.py")) == 0

# Generated at 2022-06-14 11:26:04.845550
# Unit test for function get_script_completions
def test_get_script_completions():
    script = """
import subprocess
subprocess.run(["ls", "--none", "-la"])
"""
    completions = get_script_completions(script, 2, 22, "")
    assert any((c.name == "args" and c.complete == "args=") for c in completions)


if __name__ == "__main__":
    test_get_script_completions()

# Generated at 2022-06-14 11:26:14.691266
# Unit test for function get_script_completions
def test_get_script_completions():
    assert len(get_script_completions("", 0, 0, "")) > 200
    assert len(get_script_completions("import os", 0, 0, "")) > 2
    assert len(get_script_completions("import os", 0, 0, "", sys_path=["/nonexistent_path"])) > 200
    assert len(get_script_completions("import datetime", 0, 0, "", sys_path=["/usr/local/bin"])) > 2

    assert any(c.name == "datetime" for c in get_script_completions("datet", 0, 0, ""))

# Generated at 2022-06-14 11:26:28.443041
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    result = get_interpreter_completions("[].sort", [], sys_path=[
        "/home/user/.local/lib/python3.6/site-packages",
        "/home/user/thonny/venv/lib/python3.6/site-packages",
        "/home/user/thonny/venv/lib/python3.6",
        "/home/user/thonny/venv/lib/python3.6/lib-dynload",
        "/usr/lib/python3.6",
        "/usr/lib/python3.6/lib-dynload",
        "/usr/lib/python3.6/site-packages"
    ])
    assert result == get_interpreter_completions("[].sort", [], sys_path=None)
   

# Generated at 2022-06-14 11:27:00.494286
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    import jedi

    if _using_older_jedi(jedi):
        interpreter = Interpreter("import math; math.", [])
        assert interpreter.completions()[0].name == "math"
    else:
        interpreter = jedi.Interpreter("import math; math.", [])
        print(interpreter.complete())
        assert interpreter.complete()[0].name == "math"

# Generated at 2022-06-14 11:27:17.375556
# Unit test for function get_script_completions
def test_get_script_completions():
    from parso.tree import SearchResult
    from parso.python.tree import Function, Class, Import, ImportFrom, Name, Keyword, Param, Arguments, AssignName

    def check_get_script_completions(src, row, column, filename, names):
        from jedi.api.classes import Completion
        completions = get_script_completions(src, row, column, filename)
        names = set([c.name for c in completions])
        assert names == set(names)

    src = "from base64 import b32decode, b32encode\n"
    check_get_script_completions(src, 1, 0, "test.py", ["b32decode", "b32encode"])

# Generated at 2022-06-14 11:27:25.994201
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    def test_script_completions(source, expected_completions):
        completions = get_script_completions(source, 1, 1, "<stdin>")
        completions = [c.name for c in completions]
        assert completions == expected_completions

    test_script_completions('print("Hello")', ["print", "hell", "hello"])
    test_script_completions('s = "Hello"', ["s", "str", "hello"])
    test_script_completions('s = "Hello"\nprint(', ["print", "hell", "hello"])
    test_script_completions('s = "Hello"\nprint(h', ["hell", "hello"])

# Generated at 2022-06-14 11:27:37.046450
# Unit test for function get_definitions
def test_get_definitions():
    from os.path import dirname, join

    def check_definitions(filename, row, col, expected_def_file, expected_def_row, expected_def_col):
        source = open(join(dirname(__file__), filename)).read()
        definitions = get_definitions(source, row, col, filename)

        if len(definitions) == 0:
            raise AssertionError("get_definitions returned an empty list")

        expected = (expected_def_file, expected_def_row, expected_def_col)
        actual = (definitions[0].module_path, definitions[0].line, definitions[0].column)
        if expected != actual:
            raise AssertionError("get_definitions returned %s, but should have returned %s" % (actual, expected))


# Generated at 2022-06-14 11:27:50.117347
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    namespaces = [
        {
            "B": ["C"],
            "D": ["E"],
            "other": [
                "SomethingElse",
            ],
        }
    ]

    completions = get_interpreter_completions("B", namespaces)
    assert len(completions[0]) == 4
    assert completions[0]["name"] == "C"
    assert completions[0]["complete"] == "C"
    assert completions[0]["type"] == "class"
    assert completions[0]["full_name"] == "B.C"

    completions = get_interpreter_completions("D", namespaces)
    assert len(completions[0]) == 4
    assert completions[0]["name"] == "E"

# Generated at 2022-06-14 11:28:03.609390
# Unit test for function get_script_completions
def test_get_script_completions():
    from inspect import cleandoc
    from jedi import __version__

    source = cleandoc(
        '''
        import string
        print(string)
        string
        '''
    )
    row = 2
    column = 5
    filename = "bogus.py"

    if __version__ >= "0.18.0":
        sys_path = ["/usr/local/lib/python3.7/dist-packages/jedi", "/usr/lib/python3.7"]
        completions = get_script_completions(source, row, column, filename, sys_path=sys_path)

        assert len(completions) == 1
        assert completions[0].name == "string"
        assert completions[0].complete == "string."
        assert completions[0].type == "module"


# Generated at 2022-06-14 11:28:13.670253
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock
    import jedi

    jedi.Interpreter = Mock(
        return_value=Mock(
            complete=Mock(return_value=[Mock(name="a", complete="a", type="a"), _a_completion()])
        )
    )
    jedi.Interpreter.Completion = _a_completion
    assert _interpreter_completions_ok(
        ["a", "A2"], ["a", "A2"], ["a", "A2"], ["a", "A2"], ["a", "A2"]
    )
    assert _interpreter_completions_ok(
        ["a", "A2"], ["a", "A2"], ["a", "A2"], ["a", "A2"], ["a", "A2"]
    )

# Generated at 2022-06-14 11:28:27.269259
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.classes import Completion
    from jedi.api.project import Interpreter

    def get_completions(ns):
        return get_interpreter_completions("import datetime\n", [ns], [])

    assert get_completions([]) == []
    ns1 = {
        "datetime": datetime,
        "recent_date": datetime.date(2019, 1, 2),
    }

# Generated at 2022-06-14 11:28:39.839031
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    jedi.__version__ = "0.18"

    data = [
        (
            'print("Hello" + nam)',
            0,
            15,
            [
                ThonnyCompletion(
                    name="name",
                    complete="name",
                    type="statement",
                    description="",
                    parent=None,
                    full_name="name",
                )
            ],
        ),
        (
            'print("Hello" + name)',
            0,
            15,
            [
                ThonnyCompletion(
                    name="name=",
                    complete="name=",
                    type="statement",
                    description="",
                    parent=None,
                    full_name="name",
                )
            ],
        ),
    ]


# Generated at 2022-06-14 11:28:47.490255
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    jedi = get_jedi_module()
    completions = get_interpreter_completions("import datetime; datetime", [], None)
    assert len(completions) > 0
    if _using_older_jedi(jedi):
        expected = ["datetime"]
    else:
        expected = ["datetime."]
    assert [c.complete for c in completions] == expected
    assert [c.name for c in completions] == expected



# Generated at 2022-06-14 11:29:29.908476
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import __version__
    jedi_versions = ["0.16.0", "0.17.0", "0.18.0", "0.19.0"]
    for version in jedi_versions:
        if version == __version__:
            break
        if version not in sys.modules:
            sys.modules["jedi"] = Mock(__version__=version)
        break
    try:
        completions = get_script_completions("from sys import pat", 0, 16, '/test_file.py')
    finally:
        if version not in sys.modules:
            del sys.modules["jedi"]
    assert completions[0].complete == 'path'



# Generated at 2022-06-14 11:29:37.521354
# Unit test for function get_definitions
def test_get_definitions():
    def get_definition_lines(source, row, column):
        if sys.version_info[0] == 2:
            source = source.decode("utf-8")

        return [
            [
                item.module_name,
                item.line,
                (item.description or "").encode("utf-8")
                if sys.version_info[0] == 2
                else (item.description or ""),
                item.type.__name__,
                (item.full_name or "").encode("utf-8")  # jedi 0.17 and earlier
                if sys.version_info[0] == 2
                else (item.full_name or ""),
            ]
            for item in get_definitions(source, row, column, "testfile.py")
        ]

    assert get_definition_lines

# Generated at 2022-06-14 11:29:50.720070
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.test_thonny.test_jedi_utils import dummy_jedi_module

    dummy_jedi_module.add_completion(
        ThonnyCompletion("foo_dummy_arg", "foo_dummy_arg", "func", "descr", "foo", "full_name")
    )
    dummy_jedi_module.add_completion(
        ThonnyCompletion("foo_dummy_arg2", "foo_dummy_arg2", "func", "descr", "foo", "full_name")
    )
    dummy_jedi_module.add_completion(
        ThonnyCompletion("foo_dummy_arg3", "foo_dummy_arg3", "func", "descr", "foo", "full_name")
    )
    dummy_jedi_

# Generated at 2022-06-14 11:30:04.342137
# Unit test for function get_script_completions
def test_get_script_completions():
    import os
    import sys
    import jedi

    try:
        import typing
    except:
        print("Please install typing module")
    else:
        filepath = os.path.dirname(os.path.realpath(__file__))
        testscript = filepath + "/data/test_module.py"
        source = open(testscript, "r").read()

        for build in [False, True]:
            for row in range(8, 13):
                for column in range(0, 15):
                    for sys_path in [None, [filepath]]:
                        res = get_script_completions(source, row, column, testscript, sys_path)

                        if build:
                            sys.path.append(os.environ["CONDA_BUILD_SYSROOT"])

                        true_res

# Generated at 2022-06-14 11:30:10.085178
# Unit test for function get_script_completions
def test_get_script_completions():
    try:
        import parso
        import jedi
        if parso.__version__ < '0.8.0':
            return
    except ImportError:
        return
    # jedi >= 1.0.0
    if hasattr(jedi, 'Project'):
        script = '''\
x = "a"
x.'''

        assert 'capitalize' in {c.name for c in get_script_completions(script, 3, 3, 'test.py', sys_path=[''])}
        assert 'capitalize' in {c.name for c in get_script_completions(script, 3, 3, 'test.py', sys_path=[''])}

    # jedi >= 0.18

# Generated at 2022-06-14 11:30:22.560682
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions(
        "import sys; sys.",
        namespaces=[{"type": "module", "name": "sys", "module_path": sys.path[0]}],
    )

    assert completions

    names = [x.get("name") for x in completions]

    assert "path" in names
    assert "stdout" in names
    assert "executable" in names


# Generated at 2022-06-14 11:30:33.112820
# Unit test for function get_definitions
def test_get_definitions():
    defs = get_definitions(
        "import turtle\nturtle.for",
        4,
        11,
        "/home/user/test.py",
    )
    assert len(defs) == 1
    d = defs[0]
    assert d.full_name == 'turtle.TurtleScreen.register_shape'
    assert d.name == 'turtle.TurtleScreen.register_shape'
    assert d.complete == 'register_shape'
    assert d.type == 'function'
    assert d.description.strip() == 'register_shape(shape) -> str'
    assert d.parent == 'turtle.TurtleScreen'

# Generated at 2022-06-14 11:30:41.165369
# Unit test for function get_definitions
def test_get_definitions():
    """Unit test for function get_definitions

    The test is used to make sure that newer versions of Jedi return the
    same information as older versions, so that thonny can
    use the new versions of jedi.
    """
    from thonny.plugins.jedi import utils

    # Versions of jedi to test.
    # Newest should be last.
    versions = [
        "0.13.1",
        "0.14.0",
        "0.15.2",
        "0.16.0",
        "0.17.1",
        "0.18.0",
        "0.18.1",
    ]
    # This list is used to make sure that older versions of jedi return the
    # same information as newer versions.
    # 'old' is the result from an older version of

# Generated at 2022-06-14 11:30:53.730361
# Unit test for function get_definitions
def test_get_definitions():
    import os.path
    import jedi
    from pathlib import Path
    import unittest

    def test_case_path(filename):
        return os.path.join(
            Path(jedi.__file__).parent, "test", "test_jedi", "test_goto_assignments", filename
        )

    class TestGetDefinitions(unittest.TestCase):
        def test_nested_function(self):
            code = open(test_case_path("goto_nested_function.py")).read()
            definitions = get_definitions(code, row=22, column=24, filename="X.py")
            self.assertEqual(len(definitions), 1)
            self.assertEqual(definitions[0].start_pos, (10, 4))
            self.assertE

# Generated at 2022-06-14 11:30:58.464139
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    if _using_older_jedi(jedi):
        names = [c.name for c in get_script_completions("dict().", row=0, column=9, filename="")]
        assert "keys" in names
    else:  # using jedi 0.18
        names = [c.name for c in get_script_completions("dict().", row=0, column=9, filename="")]
        assert "keys" in names

