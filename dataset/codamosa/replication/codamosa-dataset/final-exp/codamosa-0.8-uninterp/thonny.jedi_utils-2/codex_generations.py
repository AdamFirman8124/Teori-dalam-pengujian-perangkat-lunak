

# Generated at 2022-06-14 11:21:38.091858
# Unit test for function get_definitions
def test_get_definitions():
    assert "param" in get_definitions("def foo(param):\n    pass\n\nfoo('hey')", 3, 5, "dummy.py")[0].description
    assert "int" in get_definitions("def foo(param):\n    pass\n\nfoo(123)", 3, 5, "dummy.py")[0].description

# Generated at 2022-06-14 11:21:43.381341
# Unit test for function get_script_completions
def test_get_script_completions():
    if _using_older_jedi(jedi):
        completions = get_script_completions(
            "import tkinter as tk\nroot = tk.Tk()\nroot.title",
            3,
            18,
            "/tra/la/la.py",
        )
    else:
        completions = get_script_completions(
            "import tkinter as tk\nroot = tk.Tk()\nroot.title",
            3,
            18,
            "/tra/la/la.py",
        )
    assert len(completions) == 2
    assert completions[0].complete == "title"
    assert completions[1].complete == "title("


if __name__ == "__main__":
    test_get_script_completions

# Generated at 2022-06-14 11:21:53.347595
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest
    import jedi

    class TestCompletion(unittest.TestCase):

        def test_completions(self):
            source = 'import sys'
            namespace = [{'name': 'sys', 'value': sys}]
            completions = get_interpreter_completions(source, namespace)
            self.assertTrue(completions)
            has_exit = any(comp.name == 'exit' for comp in completions)
            self.assertTrue(has_exit)

    unittest.main(module=__name__, argv=['<test_get_interpreter_completions>'])


if __name__ == '__main__':
    test_get_interpreter_completions()

# Generated at 2022-06-14 11:21:55.081461
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:22:09.469458
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script
    from jedi.evaluate.representation import Instance
    from jedi import __version__

    if __version__[0] == "0":
        print("Skip jedi 0.x version in test_get_script_completions()")
        return


# Generated at 2022-06-14 11:22:23.015875
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import json
    import tempfile
    import os.path
    import sys

    dirname = tempfile.mkdtemp()
    fpath = os.path.join(dirname, "test_script.py")
    with open(fpath, "w") as f:
        f.write(
            """def test_func():
    """
        )
    sys.path.append(dirname)

    assert [] == get_interpreter_completions(
        "import test_script\ntest_script.", [[], []]
    )
    assert [] == get_interpreter_completions(
        "import test_script\ntest_script", [[], []]
    )


# Generated at 2022-06-14 11:22:30.007122
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.unittest_backend import BackendTest
    from unittest import TestCase

    from thonny import get_interpreter_completions


# Generated at 2022-06-14 11:22:41.247296
# Unit test for function get_script_completions
def test_get_script_completions():
    s = "import os; os.pa"
    assert [x.name for x in get_script_completions(s, len(s.split("\n")) - 1, len(s) - 1, "")]
    # assert [x.name for x in get_script_completions(s, len(s.split("\n")) - 1, len(s) - 1, "", sys_path = ["/usr/lib/python3.8"])]
    assert [
        x.name for x in get_script_completions(s, len(s.split("\n")) - 1, len(s) - 1, "", sys_path=[])
    ] == ["os.path"]



# Generated at 2022-06-14 11:22:48.216409
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = """class A:
    def __init__(self):
        self.x = 1
    def _get_result(self):
        return self.x

a = A()
a.x"""
    completions = get_interpreter_completions(source, [{}])
    assert len(completions) == 2
    assert completions[0].name + "=" == "x="
    assert completions[1].name == "x"

# Generated at 2022-06-14 11:22:54.588195
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock, patch
    from jedi import Script
    from thonny.jedi_utils import get_script_completions

    completions = get_script_completions(
        source="import sys\nsys.\n", row=2, column=6, filename="<string>"
    )

    assert len(completions) == 12
    for c in completions:
        assert isinstance(c, ThonnyCompletion)



# Generated at 2022-06-14 11:23:14.424872
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.jedi_utils import get_script_completions
    import jedi

    if jedi.__version__[:4] in ["0.13", "0.14"]:
        script = "import os\n" "os."
        completions = get_script_completions(script, 1, 5, "test.py")
        assert len(completions) > 0
        assert completions[0].name == "name"

        script = "import string\n" "string."
        completions = get_script_completions(script, 1, 10, "test.py")
        assert len(completions) > 0
        assert completions[0].name == "ascii_letters"


# Generated at 2022-06-14 11:23:26.683457
# Unit test for function get_script_completions
def test_get_script_completions():
    import unittest
    import jedi
    import sys
    import os.path
    import traceback

    class Tests(unittest.TestCase):

        def setUp(self):
            # Determine the path to the test source code
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.test_filename = os.path.join(script_dir, "jedi_utils_test.py")
            with open(self.test_filename) as fd:
                self.test_source = fd.read()

        def test_3rd_position(self):
            completions = get_script_completions(self.test_source, 9, 3, self.test_filename)
            self.assertEqual(len(completions), 1)

# Generated at 2022-06-14 11:23:35.057443
# Unit test for function get_definitions
def test_get_definitions():
    import unittest.mock as mock
    from textwrap import dedent

    # test_data is list of tuples (source, (row, column), expected_results):

# Generated at 2022-06-14 11:23:45.919536
# Unit test for function get_definitions
def test_get_definitions():
    # This function will fail if Jedi is not up-to-date
    import jedi

    assert jedi.__version__[0] == "0"
    source = "import os\n" + "os.\n"
    definitions = get_definitions(source, 2, 3, "untitled")
    assert definitions
    assert definitions[0].line == 5

    source = "import os\n" + "os.path.\n"
    definitions = get_definitions(source, 2, 10, "untitled")
    assert definitions
    assert definitions[0].line == 15
    assert definitions[0].name == "join"

    source = "import os\n" + "os.path.join.\n"
    definitions = get_definitions(source, 2, 14, "untitled")
    assert definitions

# Generated at 2022-06-14 11:23:59.655994
# Unit test for function get_definitions
def test_get_definitions():
    import sys

    def _get_definitions(source: str, row: int, column: int, filename: str):
        from thonny import jedi_utils

        return jedi_utils.get_definitions(source, row, column, filename)

    if sys.version_info < (3, 7):
        assert _get_definitions("\"foo\"", 1, 1, "test.py")[0].type == "str"
        assert _get_definitions("\"foo\"", 1, 2, "test.py")[0].type == "str"
        assert _get_definitions("\"foo\"", 1, 4, "test.py")[0].type == "str"
        assert len(_get_definitions("\"foo\"", 1, 3, "test.py")) == 3

# Generated at 2022-06-14 11:24:07.489361
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script
    import jedi

    if _using_older_jedi(jedi):
        def make_expected_result(completions):
            return [res.name for res in completions]

        def check(source, row, column, expected):
            actual = get_script_completions(source, row, column, filename="")
            assert make_expected_result(actual) == expected


        check("str.i", 0, 4, ["islower", "isnumeric", "isdecimal"])
        check("str.is", 0, 5, ["islower", "isnumeric", "isdecimal"])
        check("str.isl", 0, 6, ["islower"])
        check("str.islo", 0, 7, ["islower"])

# Generated at 2022-06-14 11:24:17.608979
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import unittest

    if _using_older_jedi(jedi):
        import jedi.api.classes as classes

        class TestCompletion(classes.Complete):
            def __init__(self, name, complete, type="value"):
                pass

    else:
        class TestCompletion:
            def __init__(self, name, complete, type="value"):
                self.name = name
                self.complete = complete
                self.type = type

    # 0.19 might start including this, so it's safer to exclude it
    def exclude_type_completion(completions):
        return [
            c for c in completions if not (c.type == "keyword" and c.name == "type")
        ]


# Generated at 2022-06-14 11:24:24.907435
# Unit test for function get_definitions
def test_get_definitions():
    import tempfile
    import shutil
    import os
    
    def_dir = os.path.dirname(os.path.realpath(__file__)) + "/../../../data/jedi_definitions"
    temp_dir = tempfile.mkdtemp()
    shutil.copytree(def_dir, temp_dir + "/jedi_definitions")
    
    # test 1: import file
    source = "from jedi_definitions import my_func, MyClass\n"
    print(get_definitions(source, 1, 28, temp_dir + "/jedi_definitions/__init__.py"))
    
    # test 2: import package
    source = "import jedi_definitions\n"

# Generated at 2022-06-14 11:24:36.041560
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions("import os; os.path.",
                    [{"os": __import__('os')}] )
    assert completions
    assert "abspath" in [c.name for c in completions]
    assert "dirname" in [c.name for c in completions]
    
    completions = get_interpreter_completions("import os; os.",
                    [{"os": __import__('os')}] )
    assert completions
    assert "abort" in [c.name for c in completions]
    assert "path" in [c.name for c in completions]
    

if __name__ == "__main__":
    test_get_interpreter_completions()
    print("OK")

# Generated at 2022-06-14 11:24:47.485399
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase

    class MyTestCase(TestCase):
        def test_1(self):
            source = "import os\nos.path.dirna"
            namespaces = []  # type: List[Dict]
            completions = get_interpreter_completions(source, namespaces)

# Generated at 2022-06-14 11:25:08.636646
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.classes import Interpreter

    # Heavily inspired by jedi's test suite
    # https://github.com/davidhalter/jedi/blob/4bb4b4c4d4ce78f818e0a35a7f237cf9f1be8c2a/test/test_completion/base.py
    import textwrap
    import jedi


# Generated at 2022-06-14 11:25:22.528337
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase

    import jedi

    class FakeInterpreter:
        def __init__(self, completion_name):
            self.completion_name = completion_name

        def complete(self):
            return FakeCompletion(self.completion_name)

        def completions(self):
            return FakeCompletion(self.completion_name)

    class FakeCompletion:
        def __init__(self, name):
            self.name = name
            self.complete = name
            self.type = name
            self.description = name
            self.parent = name
            self.full_name = name

    class MockJedi:
        @staticmethod
        def Interpreter(_source, _namespaces):
            assert _namespaces == []

# Generated at 2022-06-14 11:25:29.618818
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    completions = get_interpreter_completions("import math", [], sys_path=["."])
    assert len(completions) > 10
    if _using_older_jedi(jedi):
        assert all(c.name != c.complete for c in completions)
    else:
        assert all(c.name == c.complete for c in completions)

    # Function completion
    completions = get_interpreter_completions("math.", [], sys_path=["."])
    assert len(completions) > 10
    if _using_older_jedi(jedi):
        assert all(c.name != c.complete for c in completions)
    else:
        assert all("(" in c.complete for c in completions)

    # Attribute completion
    comple

# Generated at 2022-06-14 11:25:33.224595
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api.project import Project

    script_path = "./jedi_test.py"

# Generated at 2022-06-14 11:25:37.419592
# Unit test for function get_definitions
def test_get_definitions():
    import parso
    import os
    defs = get_definitions(
        "import socket\n" "socket.gethostname", 0, 0, os.path.abspath(__file__)
    )
    assert len(defs) == 1
    assert isinstance(defs[0], parso.python.tree.ExprStmt)


if __name__ == "__main__":
    test_get_definitions()

# Generated at 2022-06-14 11:25:46.230355
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    if _using_older_jedi(jedi):
        source = "a = \"ab\\ncd\"\nb = a\nstr.find(b, 'c', 0, 2)\n"
        line = 3
        column = 10
        script = jedi.Script(source, line, column, 'example.py')
        completions = script.completions()
    else:
        source = "import numpy as np\nnp.ones()"
        line = 2
        column = 10
        script = jedi.Script(code=source, path='example.py')
        completions = script.complete(line=line, column=column)
    assert len(completions) > 0

# Generated at 2022-06-14 11:25:53.253902
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import time
    from thonny import get_workbench
    from thonny.shell import ShellCodeBackend
    from thontty.python_utils import get_interpreter_completions
    from thonny.shell import ShellView
    # This code to test code completion in shell
    shell_view = get_workbench().get_view("ShellView")
    get_workbench().event_generate("FocusIn", view=shell_view)
    shell = ShellView(get_workbench(), get_workbench().active_text_editor)
    get_workbench().get_option("shell.backend")
    shell.shell_backend = ShellCodeBackend(shell, shell.cancel_execute)

# Generated at 2022-06-14 11:26:01.016434
# Unit test for function get_script_completions
def test_get_script_completions():
    syspath = {"/Users/user/Desktop/ThonnyTestFolder/"}
    source = "import numpy as np\nprint(np.array([1, [1.1,1.2]]))\n"

    def get_completions(row, column):
        return get_script_completions(source, row, column, "", sys_path=syspath)

    completions = get_completions(0, len(source))
    assert len(completions) > 1

    completions = get_completions(0, source.find(" as ") + 1)
    assert len(completions) > 1
    for completion in completions:
        if completion["name"] == "as":
            assert completion["type"] in ("keyword", "statement")
            assert completion["description"].startswith

# Generated at 2022-06-14 11:26:13.295835
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    # jedi v0.17.1
    # Not OK: 'pri' returns ['print', 'private']
    # OK: 'pri' returns ['print'] (pri is not in keywords.kwlist)
    # OK: 'pri=' returns ['print=']
    # OK: 'if pri' returns empty list
    # OK: 'if ' returns empty list
    # imports should be handled normally
    # OK: 'im' returns ['import']
    # OK: 'im.' returns ['importlib']
    # OK: 'value = int("10")' works

    source = 'pri'
    row = 1
    column = 3
    filename = None
    completions = get_script_completions(source, row, column, filename)
    assert len(completions) == 0

    source = 'pri'
   

# Generated at 2022-06-14 11:26:24.095609
# Unit test for function get_definitions
def test_get_definitions():
    if __name__ == "__main__":
        import sys
        import os
        import jedi

        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "test-data/test-module"))
        source = """\
from test_module import TestClass
TestClass().test_method()
"""

        defs = get_definitions(source, 2, 5, "")
        if len(defs) != 1 or not isinstance(defs[0], jedi.api.classes.Class):
            raise AssertionError(
                "Unexpected number of definitions for 'test_method': " + str(defs)
            )

# Generated at 2022-06-14 11:26:44.876632
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase

    class MyTestCase(TestCase):
        def assertItemsEqual(self, a, b):
            return self.assertCountEqual(a, b)

    test = MyTestCase()

    test.assertItemsEqual(
        [
            ThonnyCompletion(
                name="c",
                complete="c",
                type="function",
                description="",
                parent="c",
                full_name="c",
            )
        ],
        get_interpreter_completions("c", [], []),
    )

# Generated at 2022-06-14 11:26:46.088260
# Unit test for function get_definitions

# Generated at 2022-06-14 11:26:59.443301
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api.environment import InterpreterEnvironment
    from jedi.api.project import Project
    from jedi.api.names import TreeNameDefinition
    from jedi.api.classes import Class
    from jedi.api.helpers import StdLibContext, PreloadLibrary

    project = Project(InterpreterEnvironment())
    project.preload_library(StdLibContext(), PreloadLibrary(project, "random"))
    definitions = get_definitions(
        "import random; random.random()", 0, 0, project=project
    )

    assert len(definitions) == 1
    assert isinstance(definitions[0], TreeNameDefinition)
    assert definitions[0].full_name == "random.random"
    assert repr(definitions[0]) == "<Definition: random.random>"

# Generated at 2022-06-14 11:27:16.314387
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Test 1
    namespaces = [{"bad": "namespace"}]
    ret = get_interpreter_completions("", namespaces)
    assert not ret

    # Test 2
    namespaces = [{"foo": "bar"}]
    ret = get_interpreter_completions("", namespaces)
    assert isinstance(ret, list)
    assert len(ret) == 2
    assert len(ret[0]) == 5
    assert ret[0]['name'] == 'foo'
    assert ret[0]['complete'] == 'foo'
    assert ret[0]['type'] == 'name'
    assert ret[0]['description'] == "str" # "str" or "namespace"
    assert ret[0]['parent'] == 'bar'

    ret = get_interpreter_completions

# Generated at 2022-06-14 11:27:17.189753
# Unit test for function get_definitions

# Generated at 2022-06-14 11:27:25.859534
# Unit test for function get_definitions
def test_get_definitions():
    import jedi

    assert type(get_definitions("abc", 0, 0, "abc.py")) == list
    assert type(get_definitions("abc", 0, 0, "abc.py")[0]) == jedi.api.classes.Name
    assert type(get_definitions("import re", 0, 0, "abc.py")[0]) == jedi.api.classes.Module 
    assert type(get_definitions("import re", 1, 0, "abc.py")[0]) == jedi.api.classes.Name
    assert type(get_definitions("a[0]", 1, 0, "abc.py")[0]) == jedi.api.classes.Name
    assert type(get_definitions("a[0]", 1, 0, "abc.py")[1]) == jedi.api.classes

# Generated at 2022-06-14 11:27:36.910992
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest
    import jedi
    from unittest.mock import patch

    # run system without jedi
    try:
        import jedi
    except ImportError:
        return

    # run module without jedi
    if jedi.__version__[:4] == "0.1":
        return
    if jedi.__version__[:4] == "0.2":
        return
    if jedi.__version__[:4] == "0.3":
        return
    if jedi.__version__[:4] == "0.4":
        return
    if jedi.__version__[:4] == "0.5":
        return
    if jedi.__version__[:4] == "0.6":
        return

# Generated at 2022-06-14 11:27:44.883350
# Unit test for function get_script_completions
def test_get_script_completions():
    source = "import itertools\n"
    source += "itertools.isl"
    completions = get_script_completions(
        source=source, row=2, column=17, filename="test.py"
    )
    assert len(completions) == 1
    completion = completions[0]
    assert completion.name == "islandic"
    assert completion.complete == "islandic"



# Generated at 2022-06-14 11:27:53.822229
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi, copy
    class MockScript:
        def __init__(self, namespaces):
            self.namespaces = namespaces

    def get_namespaces(self):
        return [copy.deepcopy(space) for space in self.namespaces]

    MockScript.get_namespaces = get_namespaces

    jedi.Script = MockScript
    jedi.Interpreter = object
    row = 2
    col = 3
    code = "import os\nimport sys\nsys.path.append('path1')\n"

# Generated at 2022-06-14 11:28:07.975464
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if _using_older_jedi(jedi):
        namespaces = [{'__name__': '__main__', '__doc__': None}]  # type: ignore
    else:
        namespaces = [{'__name__': '__main__', '__doc__': None, '__package__': None}]  # type: ignore
    source = """
import json
import os
import sys
"""  # type: ignore
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) > 0
    for completion in completions:
        assert isinstance(completion.name, str)
        assert isinstance(completion.complete, str)
        assert isinstance(completion.type, str)

# Generated at 2022-06-14 11:28:28.539814
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest

    class TestGetInterpreterCompletions(unittest.TestCase):
        def test_get_interpreter_completions(self):
            import jedi

            completions = jedi.api.get_interpreter_completions(
                "import datetime; datetime.", [], ['.']
            )

            # get_interpreter_completions should return a list of completions
            self.assertTrue(isinstance(completions, list))

            # check if each completion is a subclass of JediCompletion
            for completion in completions:
                self.assertTrue(isinstance(completion, jedi.api_classes.Completion))

            # make sure the completion list is not empty
            self.assertTrue(len(completions) > 0)

            # make sure we have "

# Generated at 2022-06-14 11:28:40.846004
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    assert get_script_completions("print(", 0, 6, "test.py") == get_script_completions(
        "print(", 0, 6, "test.py"
    )

    # Different jedi versions return different number of results.
    # For older jedi, the result contains two "property" type completions,
    # for newer ones "Property" and "property". Those could be handled
    # separately (e.g. when only one is accepted, then it could be removed
    # from the result).

    # Not all jedi versions support sys_path.  When it does not work, try with None.

# Generated at 2022-06-14 11:28:48.916310
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api.project import Project
    from thonny import get_runner
    import thonny
    import os

    python_executable = get_runner.get_executable_for_script(thonny.THONNY_USER_DIR)
    project = Project(os.path.dirname(thonny.THONNY_USER_DIR), python_executable=python_executable)
    definitions = get_definitions("argv", 0, 0, "__main__.py")
    assert len(definitions) == 1
    assert definitions[0].name == "argv"
    assert definitions[0].type == "param"

# Generated at 2022-06-14 11:28:58.680067
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    completions = get_script_completions(
        "import sys\nsys", 2, 5, filename="<stdin>"
    )
    assert len(completions) == 1
    assert completions[0].name == "sys"

    completions = get_script_completions(
        "import sys\nsys.", 2, 6, filename="<stdin>"
    )
    assert len(completions) > 0

    assert len(get_script_completions("def foo(arg):\n    arg", 2, 8, filename="<stdin>")) > 0

    assert len(get_script_completions("\"\"\"", 1, 4, filename="<stdin>")) == 0


if __name__ == "__main__":
    test_get_script_completions()

# Generated at 2022-06-14 11:29:10.971844
# Unit test for function get_definitions
def test_get_definitions():
    import pathlib
    import importlib
    import jedi
    from jedi.api import Interpreter

    assert _using_older_jedi(jedi)

    helper_module_path = pathlib.Path(__file__).parent.joinpath("jedi_utils_test.py")
    helper_module = importlib.import_module(".jedi_utils_test", "thonny.backend")

    source = helper_module_path.read_text()
    # We need Interpreter to initialize the name spaces.
    Interpreter(source, (helper_module.__dict__,), sys_path=[str(helper_module_path.parent)])

# Generated at 2022-06-14 11:29:22.767170
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.parser_utils import get_statement_of_position

    def test(source: str, row: int, column: int, expected: List[str]):
        actual = get_interpreter_completions(source, [], sys_path=[])
        actual = [c.name for c in actual]
        if actual != expected:
            print(actual)
            print(expected)
        assert set(actual) == set(expected)

    # Simple list
    test("[1, 2, ]", 0, 4, ["append", "extend", "insert"])
    test("[1, 2, ]", 0, 5, ["append", "extend", "insert"])
    test("[1, 2, ]", 0, 6, ["append", "extend", "insert"])

    # List from generator expression
   

# Generated at 2022-06-14 11:29:29.247001
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import __version__

    if __version__ == "0.15.1":
        expected_result = [
            ThonnyCompletion(
                name="Abc",
                complete="Abc",
                type="class",
                description="class Abc",
                parent=u"",
                full_name="Abc",
            ),
            ThonnyCompletion(
                name="Xyz",
                complete="Xyz",
                type="class",
                description="class Xyz",
                parent=u"",
                full_name="Xyz",
            ),
        ]

# Generated at 2022-06-14 11:29:29.974860
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:29:37.542752
# Unit test for function get_definitions
def test_get_definitions():
    import unittest
    import jedi
    from jedi.parser_utils import get_cached_code_lines

    class TestGetDefinitions(unittest.TestCase):
        def setUp(self):
            self.jedi = jedi

        def test_top_level_function(self):
            source = 'def myfunc(): pass\nmyfunc()'
            row = 1
            column = 5
            definitions = get_definitions(source, row, column, '')
            self.assertEqual(len(definitions), 1)

            definition = definitions[0]
            self.assertEqual(definition.line, 0)
            self.assertEqual(definition.type, 'function')
            self.assertEqual(definition.full_name, 'myfunc')

# Generated at 2022-06-14 11:29:50.734758
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # This test is an attempt to understand what should be possible
    # with get_interpreter_completions.
    #
    # Current code for get_interpreter_completions is taken from
    # https://github.com/davidhalter/jedi/blob/e5aa056d9ed6f59d6c71cf6d1b0794e0d62a8706/jedi/api/__init__.py

    # Test Python code
    source = "import io; io.BytesIO"
    # These namespaces are copied from an actual debugger session
    # I don't know whether they are/should be correct or not.

# Generated at 2022-06-14 11:30:12.753582
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock
    import jedi

    def _test_case(code, namespace, sys_path, expected_completions=None, expected_err=None):
        if _using_older_jedi(jedi):
            try:
                completions = get_interpreter_completions(code, namespace, sys_path=sys_path)
            except Exception as e:
                if expected_err:
                    if not isinstance(e, expected_err):
                        raise AssertionError(
                            "Expected error: " + str(expected_err) + ", got: " + str(e)
                        )
                else:
                    raise
            else:
                if expected_err:
                    raise AssertionError("Expected error: " + str(expected_err))

# Generated at 2022-06-14 11:30:16.490796
# Unit test for function get_script_completions
def test_get_script_completions():
    with open("./test.txt", "r") as f:
        source = f.read()
    completions = get_script_completions(source, 8, 3, "./test.txt")
    assert completions
    for completion in completions:
        assert completion.name
        assert completion.complete
        assert completion.type
        # Completion.description can be an empty string
        # assert completion.description
        assert completion.parent
        assert completion.full_name


if __name__ == "__main__":
    test_get_script_completions()

# Generated at 2022-06-14 11:30:17.981861
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:30:25.266299
# Unit test for function get_definitions
def test_get_definitions():
    def test(source, row, column, count, first_type=None):
        import jedi

        if _using_older_jedi(jedi):
            res = jedi.Script(source, row, column, "").goto_definitions()
        else:
            res = jedi.Script(code=source, path="").infer(line=row, column=column)

        assert len(res) == count
        if count > 0:
            assert res[0].type == first_type

    test("import os", 0, 7, 1, "module")
    test("import os\nos.path", 1, 1, 4)
    test("import os\nos.path.join()", 1, 7, 1, "function")
    test("from os.path import join", 0, 24, 1, "function")

# Generated at 2022-06-14 11:30:34.036075
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.parser import tree as pt

    source = "import os\n"
    namespaces = [{"name": "__main__", "type": "module", "path": "__main__"}]
    completions = get_interpreter_completions(
        source=source, namespaces=namespaces, sys_path=[os.getcwd()]
    )
    assert completions
    for comp in completions:
        assert type(comp) is ThonnyCompletion



# Generated at 2022-06-14 11:30:41.455184
# Unit test for function get_script_completions
def test_get_script_completions():
    import parso
    from parso.python.tree import NodeOrLeaf
    from parso.python.parser import ParserSyntaxError

    def _test(script, line, column):
        parse_tree = parse_source(script)
        script_completions = get_script_completions(script, line, column, "test.py")
        assert len(script_completions) > 0

        node = get_statement_of_position(parse_tree, (line, column))
        assert isinstance(node, NodeOrLeaf)
        assert node.type != "error_leaf"
        return (script_completions, node)

    # print(_test("import os.path.", 1, 14))
    # print(_test("import os.path.", 1, 15))

    # 1. completions for import statement
   

# Generated at 2022-06-14 11:30:46.321535
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    jedi.__version__ = "0.17.1"
    script = """
x = "hello"
x
"""
    completions = get_script_completions(script, 1, 2, "test.py")
    assert len(completions) > 0, "Did not receive completions"

# Generated at 2022-06-14 11:30:57.279889
# Unit test for function get_definitions
def test_get_definitions():
    class _TestTree:
        def __init__(self, start_pos, end_pos):
            self.start_pos = start_pos
            self.end_pos = end_pos

    import unittest

    from jedi.parser_utils import get_statement_of_position

    class TestGetStatementOfPosition(unittest.TestCase):
        def test_function(self):
            node = _TestTree((1, 0), (2, 0))
            func = _TestTree((1, 0), (1, 10))
            node.children = [func]
            self.assertEqual(get_statement_of_position(node, (1, 3)), func)

        def test_class(self):
            node = _TestTree((1, 0), (2, 0))

# Generated at 2022-06-14 11:31:08.956700
# Unit test for function get_script_completions
def test_get_script_completions():
    from parso.tree import Leaf

    # test 0-sys.path
    result = get_script_completions("import sys; sys.p", row=1, column=15, filename="")
    assert result == []

    # test 1-sys.path
    result = get_script_completions("import sys; sys.path", row=1, column=18, filename="")
    assert result == []

    # test 2-sys.path
    result = get_script_completions("import sys; sys.path", row=1, column=18, filename="")
    assert result == []

    # test 3-sys.path
    result = get_script_completions(
        "import sys; sys.path", row=1, column=18, filename="", sys_path=[""]
    )

# Generated at 2022-06-14 11:31:15.184427
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock

    namespaces = [
        {},
        {
            "x": "3",
            "y": "4",
            "b": "5",
            "l": "[4, 5, 6]",
            "t": "('a')",
            "d": "{'c': 3, 'b': 2}",
            "s": "set([2, 3, 4])",
            "p": "__main__.Person",
        },
    ]

    source = "x"
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) == 1
    assert completions[0].name == "x"
    assert completions[0].complete == "x"

    source = "x + "
    completions = get_