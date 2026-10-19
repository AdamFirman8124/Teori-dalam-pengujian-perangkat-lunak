

# Generated at 2022-06-14 11:21:24.958239
# Unit test for function get_script_completions
def test_get_script_completions():
    from types import ModuleType
    from unittest.mock import MagicMock

    # Create a mock module
    example_module = ModuleType("example")
    example_module.__doc__ = "Example module"
    example_module.var1 = MagicMock()
    example_module.var1.__doc__ = "Example variable"
    example_module.var1.__name__ = "var1"
    example_module.some_function = MagicMock()
    example_module.some_function.__doc__ = "example function"
    example_module.some_function.__name__ = "some_function"
    example_module.__name__ = "example"

    # Import the module in globals
    global_namespace = {}
    local_namespace = {}

# Generated at 2022-06-14 11:21:29.451701
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import patch

    with patch("thonny.jediutils.get_script_completions") as mocked_get_script_completions:
        mocked_get_script_completions.return_value = ["a", "b"]
        assert(get_script_completions("", 0, 0, "") == ["a", "b"])


# Generated at 2022-06-14 11:21:50.995898
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api.script import Script
    from jedi.api.classes import Completion
    from unittest.mock import MagicMock
    from unittest.mock import patch
    # noinspection PyTypeChecker
    import jedi.api.classes

    source = "def a():\n    pass"
    row = 0
    column = 4
    filename = "dummy"

    with patch('jedi.api.classes.Script', autospec=True):
        Script.return_value.completions.return_value = [Completion(
            name="a",
            complete="a",
            type=Completion.FUNCTION,
            description="function",
            parent=None,
            full_name="a"
        )]

# Generated at 2022-06-14 11:21:59.841026
# Unit test for function get_definitions
def test_get_definitions():
    import unittest.mock
    # mock jedi for testing
    jedi = unittest.mock.MagicMock()

    class Definition:
        def __init__(self, get_parent):
            self.get_parent = get_parent

    class MockDefinitionParams:
        def __init__(self, value):
            self.get_parent = lambda: value

    class MockDefinition:
        def __init__(self, value):
            self.definition = Definition(MockDefinitionParams(value))

    # def test_get_definitions_one(self):
    #     jedi.api.definition.Definition

    def test_get_definitions_multiple(self):
        def multiple_return_value(*args, **kwargs):
            return [MockDefinition("1"), MockDefinition("2")]

        j

# Generated at 2022-06-14 11:22:01.277674
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    import os

    import jedi


# Generated at 2022-06-14 11:22:06.050779
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = 'from collections import namedtuple\n'
    source += 'Point = namedtuple("Point", [])\n'
    source += 'p = Point()\n'
    source += 'p.'

    from jedi import Interpreter
    namespaces = [{"type": "module", "module_path": "module", "name": "__main__"}]
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) == 6

# Generated at 2022-06-14 11:22:09.008528
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import numpy; numpy.a"
    assert len(get_interpreter_completions(source, [])) > 0

# Generated at 2022-06-14 11:22:13.984986
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    result = get_interpreter_completions("random.R", [])
    assert len(result) == 2
    assert result[0].name == "random"
    assert result[1].name == "random("


# Generated at 2022-06-14 11:22:25.651092
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.jediutils import get_script_completions
    from thonny.plugins.micropython.completion import MicroPythonCompletionProvider

    def complete_code(text):
        provider = MicroPythonCompletionProvider()
        completions = get_script_completions(text, 0, len(text), "/somepath/foo.py", [])
        return [c.complete for c in completions]

    assert "def " in complete_code("def fun")
    assert "fun(" in complete_code("def fun()\nfun(")

    assert "lambda " in complete_code("lambda ")
    assert "lambda x: " in complete_code("lambda x:")

    assert "import " in complete_code("import ")
    assert "import a" in complete_code("import a")

# Generated at 2022-06-14 11:22:28.943536
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("import math\nmath.", 0, 7, "test")
    assert len(completions) > 0
    assert any("pi" in c.complete for c in completions)

# Generated at 2022-06-14 11:22:54.309889
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import time
    t0 = time.time()
    if _using_older_jedi(jedi):
        namespaces = [
            {"type": 'module', "description": 'sys', "name": 'sys', "full_name": 'sys'}
        ]
    else:
        namespaces = [
            jedi.Interpreter("", [{"type": 'module', "description": 'sys', "name": 'sys', "full_name": 'sys'}]),
        ]
    completions = get_interpreter_completions("s", namespaces)
    t1 = time.time()
    print("time=", t1 - t0)
    print("completions=", completions)
    assert len(completions) > 0
    assert completions[0].name == "sys"

# Generated at 2022-06-14 11:23:08.505618
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest.mock as mock
    from unittest import TestCase

    class DummyInterpreter:
        def __init__(self, completions):
            self.completions = completions

        def complete(self):
            return self.completions

    class MockJedi:
        def __init__(self):
            self.Interpreter = mock.Mock(wraps=DummyInterpreter)
            self.Interpreter.side_effect = lambda source, namespaces: self.Interpreter(
                [{"name": "foo", "complete": "foo"}]
            )

    import jedi

    _new_jedi = jedi
    jedi = MockJedi()

# Generated at 2022-06-14 11:23:18.877740
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:23:25.622860
# Unit test for function get_script_completions
def test_get_script_completions():

    source = """def test_function(x: str, y: str):
    x.
    y.
"""
    completions = get_script_completions(source, 3, 3, "test.py")
    assert set(c.complete for c in completions) == {"startswith", "endswith"}

    completions = get_script_completions(source, 4, 3, "test.py")
    assert set(c.complete for c in completions) == {"startswith", "endswith"}



# Generated at 2022-06-14 11:23:28.646529
# Unit test for function get_definitions
def test_get_definitions():
    defi = get_definitions("max(5, M)" , 0, 8, "test.py")
    assert defi[0].full_name == "__builtin__.max"


# Generated at 2022-06-14 11:23:42.012740
# Unit test for function get_definitions
def test_get_definitions():
    assert get_definitions(source='range(5)', row=0, column=0, filename='<stdin>') == []
    assert get_definitions(source='range(5)', row=0, column=0, filename='<st>') == []

    assert get_definitions(source='range(5).summ', row=0, column=0, filename='<st>') == []
    assert get_definitions(source='range(5).summ', row=0, column=0, filename='<stdin>') == []

    if get_definitions(source='range(5).summ', row=0, column=9, filename='<stdin>'):
        assert get_definitions(source='range(5).sum', row=0, column=9, filename='<stdin>')
    assert get_def

# Generated at 2022-06-14 11:23:52.110388
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest
    import sys
    import os

    # NB! Need to be in the same directory as test_utils.py
    sys.path.append(os.path.join(os.path.dirname(__file__), "micropipenv", "helpers", "vendor"))

    class TestGetInterpreterCompletions(unittest.TestCase):
        def test_get_interpreter_completions(self):
            import parso
            from jedi.common import SourceLine

            source = 'import json; json.l'
            namespaces = [{'json': parso.parse('{"a": 3}').children[0]}]
            completions = get_interpreter_completions(source, namespaces)

            self.assertEqual(len(completions), 3)

# Generated at 2022-06-14 11:23:56.228328
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.config import get_python_exe_prefix
    from thonny import get_runner
    import sys
    import os

    # Create a test python file for completion
    test_source_file = os.path.join(os.path.dirname(__file__), "test_file.py")
    file = open(test_source_file, "w")

# Generated at 2022-06-14 11:23:59.034751
# Unit test for function get_definitions
def test_get_definitions():
    import jedi

    script = jedi.Script(
        "import sys\nsys.stdout.write('')",
        row=1,
        column=14,
        filename="",
    )
    result = script.goto_definitions()
    assert result[0].description == "write(...)"

# Generated at 2022-06-14 11:24:10.041893
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    # test with jedi 0.14 (python3.4.3)
    if jedi.__version__.startswith("0.14"):
        from unittest import TestCase

        source = "import math as m; m.pow(2, 10)"
        completions = get_script_completions(source, 2, 8, "test.py")
        assert len(completions) == 1
        completion = completions[0]
        assert completion["complete"] == "pow"
        assert "pow" in completion["name"]

    # test with jedi 0.15 (python3.7.3)
    if jedi.__version__.startswith("0.15"):
        from unittest import TestCase


# Generated at 2022-06-14 11:24:39.761532
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    import sys
    import os

    jedi.settings.additional_dynamic_modules = [
        "test_jedi_utils.test_module_1",
        "test_jedi_utils.test_module_2",
    ]

    sys.path.append(os.path.dirname(__file__))

    script = "import test_jedi_utils.test_module_1 as tm\ntm.tes"
    completions = get_script_completions(script, 2, 11, filename=__file__)
    assert [c["complete"] for c in completions] == ["test_jedi_utils.test_module_1."]

    script = "import test_jedi_utils.test_module_1 as tm\ntm.test_func("
    completions = get

# Generated at 2022-06-14 11:24:43.557491
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi, sys
    c = get_interpreter_completions(
        "import sys \nsys.",
        [
            {
                "name": "sys",
                "path": sys.executable,
                "builtin": False,
                "namespace": None,
                "typeshed": False,
            }
        ],
    )

    d = {c.name for c in jedi.Interpreter("import sys \nsys.").completions()}
    assert d == {c.name for c in c}



# Generated at 2022-06-14 11:24:45.807435
# Unit test for function get_script_completions
def test_get_script_completions():
    result = get_script_completions('import os\nos.p', 0, 5, '')
    assert len(result) == 1
    assert result[0].complete == "path"

# Generated at 2022-06-14 11:24:57.471308
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():

    from jedi.api.shell import Completion

    def _test_one(source: str, namespaces: List[Dict], expected):
        result = get_interpreter_completions(source, namespaces)
        assert [c.name for c in result] == expected

    _test_one("print(", [{"__name__" : "__main__", "__builtins__" : __builtins__}], ["print"])
    _test_one("'a'.up", [{}], ["upper"])
    if hasattr(Completion, "name"):
        _test_one("'a'.upper(", [{}], ["return"])
    else:
        _test_one("'a'.upper(", [{}], ["return"])

# Generated at 2022-06-14 11:25:09.718190
# Unit test for function get_script_completions
def test_get_script_completions():
    # for code "impor"
    code = """from tkinter import *
impo"""
    completions = get_script_completions(code, 1, 8, "test.py")
    assert len(completions) == 2
    assert completions[0]["name"] == "importlib"
    assert completions[0]["complete"] == "importlib.__import__"
    assert completions[0]["type"] == "module"
    assert completions[0]["description"] == "importlib"
    assert completions[0]["full_name"] == "importlib"
    assert completions[1]["name"] == "importlib.abc"
    assert completions[1]["complete"] == "importlib.__import__"
    assert completions[1]["type"] == "module"

# Generated at 2022-06-14 11:25:23.341335
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    namespaces = [{"a": "aaa"}]
    completions = get_interpreter_completions("a.", namespaces)
    assert isinstance(completions, list)
    assert len(completions) == 1
    assert completions[0].complete == "aaa"
    assert completions[0].type == "statement"
    assert completions[0].description == "aaa"
    assert completions[0].parent == "<module>"

    # Other variations of test
    namespace = {"a": {"b": "bbb"}, "c": "ccc"}
    namespaces = [namespace]
    completions = get_interpreter_completions("a.", namespaces)
    assert len(completions) == 2

# Generated at 2022-06-14 11:25:37.231839
# Unit test for function get_script_completions
def test_get_script_completions():
    '''
    Test script completions through jedi lib
    '''
    # Arrange
    import sys
    import os
    import jedi
    import parso
    #sys.path.append('/home/nauckalo/jedi')
    path = sys.path

    # Act
    source = 'from jedi.api import Interpreter'
    row = 0
    column = 10
    filename = 'test_file.py'
    completions = get_script_completions(source, row, column, filename, sys_path=path)
    snippet = completions[0].complete

    # Assert
    assert completions != []
    assert 'jedi' == completions[0].name
    assert 'Interpreter(' in snippet
    assert 1 == len(completions)


# Generated at 2022-06-14 11:25:43.927160
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    assert not _using_older_jedi(jedi)
    source = "import math\n\ndef f():\n    math.sq"
    completions = get_script_completions(source, 3, 12, "test.py")
    assert len(completions) > 0
    # without path
    completions = get_script_completions(source, 3, 12, None)
    assert len(completions) > 0

# Generated at 2022-06-14 11:25:49.622656
# Unit test for function get_definitions
def test_get_definitions():
    res = get_definitions("import sys\nsys.", 0, 8, "<stdin>")
    assert len(res) == 1
    res = get_definitions("sys.", 0, 4, "<stdin>")
    assert len(res) == 1

# Generated at 2022-06-14 11:25:59.265641
# Unit test for function get_script_completions
def test_get_script_completions():
    def get_cpl(source, row, col, file_name):
        return get_script_completions(source, row, col, file_name)

    assert len(get_cpl('"'.encode(), 0, 0, '')) > 0
    assert len(get_cpl('"'.encode(), 0, -1, '')) == 0
    assert len(get_cpl('"'.encode(), 1, 0, '')) == 0
    assert len(get_cpl('"'.encode(), 0, 1, '')) == 0
    assert len(get_cpl('"'.encode(), 0, 2, '')) == 0
    assert len(get_cpl('"'.encode(), 0, 3, '')) == 0

    assert len(get_cpl('"a'.encode(), 0, 1, ''))

# Generated at 2022-06-14 11:27:02.907761
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Simple example with a single valid completion
    result = get_interpreter_completions("str.", [{'str': str}])
    assert len(result) == 1
    first_compl = result[0]
    assert first_compl.name == "capitalize"
    assert first_compl.complete == "capitalize("
    assert first_compl.type == "function"
    assert first_compl.description == "S.capitalize() -> str\n\nReturn a capitalized version of S"
    assert first_compl.full_name == "str.capitalize"
    assert first_compl.parent == str

    import os
    assert len(get_interpreter_completions("os.", [{'os': os}])) > 100

    # Example with two completions, but validating only one
    result = get_inter

# Generated at 2022-06-14 11:27:06.689193
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test_utils import parse_text, get_position


# Generated at 2022-06-14 11:27:07.732230
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:27:18.147279
# Unit test for function get_script_completions
def test_get_script_completions():
    
    import sys
    import os
    import re
    import tempfile
    
    s = """
from tkinter import Tk, Label, Button

root = Tk()
my_label = Label(root, text="Hello World!")
my_button = Button(root, text="Click Me!", command=root.destroy)
"""

    completions = get_script_completions(s, 9, 15, "test.py", [os.path.dirname(__file__)])
    
    # Uncomment this to get all completions
    for c in completions:
        print(c)

    names = [c.name for c in completions]
    
    assert "Tk" in names
    assert "Label" in names
    assert "Button" in names
    assert "destroy" in names

# Generated at 2022-06-14 11:27:30.842271
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    import os
    import unittest

    sys.path.insert(0, os.path.dirname(__file__))

    ###########################################################################
    # Test data
    ###########################################################################

    # script is a python script, completions is a list of completions that
    # jedi should return for the script. Positions are line, column. Completion
    # description and parent are strings, type is an int

# Generated at 2022-06-14 11:27:39.537225
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    result = get_script_completions("print('hel')", 0, 9, '__main__', sys_path=['.'])
    assert result[0].name == 'print' and result[0].complete == 'print('

    Completion = jedi.api.classes.Completion
    result = get_script_completions("help(", 0, 5, '__main__', sys_path=['.'])
    assert isinstance(result[0], Completion)
    assert result[0].name == 'help'
    assert result[0].complete == 'help('

    result = get_script_completions("'hel' + 'lo'[0]", 0, 11, '__main__', sys_path=['.'])
    assert isinstance(result[0], Completion)

# Generated at 2022-06-14 11:27:51.417931
# Unit test for function get_definitions
def test_get_definitions():
    assert (get_definitions("x = 1", 0, 0, "") == [])
    assert (get_definitions("x = 1", 0, 3, "") == [])

# Generated at 2022-06-14 11:28:05.386311
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if _using_older_jedi(jedi):
        return

    completions = get_interpreter_completions("import datetime; datetime.", {}, [])
    assert len(completions) == 3
    assert any(c.name == "datetime.datetime" for c in completions)
    assert any(c.name == "datetime.date" for c in completions)
    assert any(c.name == "datetime.time" for c in completions)

    completions = get_interpreter_completions("import", {}, [])
    assert len(completions) == 1
    assert completions[0].name == "import"
    assert completions[0].type == "keyword"


# Generated at 2022-06-14 11:28:11.639873
# Unit test for function get_definitions
def test_get_definitions():
    source = "def foo(): pass\nfoo()"

    definitions = get_definitions(source, 2, 4, "test_file")
    assert type(definitions) is list
    assert len(definitions) == 1
    assert definitions[0].line == 1

    definitions = get_definitions(source, 1, 5, "test_file")
    assert len(definitions) == 1
    assert definitions[0].line == 1

# Generated at 2022-06-14 11:28:26.532675
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import parso
    import random
    import time
    from thonny.misc_utils import running_on_windows

    if running_on_windows():
        env = {
            "PYTHONIOENCODING": "utf-8",
            "PYTHONUTF8": "1",
            "LANG": "en_US.UTF-8",
            "LC_ALL": "en_US.UTF-8",
        }
    else:
        env = {}

    test_success = False
    for test_count in range(100):
        test_success = False

# Generated at 2022-06-14 11:30:18.998073
# Unit test for function get_script_completions
def test_get_script_completions():
    for i in range(10):
        get_script_completions("if ", 1, 3, "stdin", sys_path=[])
        get_script_completions("if \n", 2, 1, "stdin", sys_path=[])
        get_script_completions("if Fo", 1, 4, "stdin", sys_path=[])
        get_script_completions("if Fob", 1, 5, "stdin", sys_path=[])
    return True


# Generated at 2022-06-14 11:30:25.930222
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    completions = get_script_completions(
        "import sys\nsys.stdou", 10, 6, "/tmp/foo.py"
    )
    assert completions == jedi.Script(
        "import sys\nsys.stdou", 10, 6, "/tmp/foo.py"
    ).completions()

    # Only in older versions
    if _using_older_jedi(jedi):
        completions = get_script_completions(
            "import sys\nsys.stdou", 10, 6, "/tmp/foo.py", ['/usr/local/lib/python3.7']
        )

# Generated at 2022-06-14 11:30:38.401750
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.plugins.backend import BackendProxy
    import sys
    import os
    import tkinter as tk
    import traceback
    from thonny import get_workbench
    from thonny.globals import get_runner
    from thonny.ui_utils import CommonDialog, SubprocessDialog
    from thonny.common import InlineCommand
    from thonny.languages import tr
    import thonny.ui as ui
    from thonny.ui_utils import askopenfilename, askdirectory
    from thonny.ui_utils import showwarning
    from thonny.ui_utils import lazy_call
    from thonny.shell import ShellEditor
    from thonny import tktextext
    from thonny.misc_utils import running_on_mac_os

# Generated at 2022-06-14 11:30:51.260671
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest

    class Test(unittest.TestCase):
        def test_count(self):
            namespaces = [{}]
            source = "class Foo:\n    def bar(self):\n        pass"
            completions = get_interpreter_completions(source, namespaces)
            self.assertEqual(len(completions),  4)

        def test_type(self):
            namespaces = [{}]
            source = "class Foo:\n    def bar(self):\n        pass"
            completions = get_interpreter_completions(source, namespaces)
            self.assertEqual(completions[0].type, "class")
            self.assertEqual(completions[1].type, "function")

# Generated at 2022-06-14 11:30:51.925657
# Unit test for function get_definitions

# Generated at 2022-06-14 11:30:56.731615
# Unit test for function get_definitions
def test_get_definitions():
    """
    Correctness of definition getting is checked by Jedi's own tests (which are called by travis)
    Here I just want to be sure we don't get ParseError in Jedi
    (can happen if source contains syntax error)
    """
    source = "def f(x): pass f(1"
    get_definitions(source, 3, 5, "<string>")

# Generated at 2022-06-14 11:31:00.229199
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock
