

# Generated at 2022-06-14 11:21:40.832954
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock

    from jedi._compatibility import use_metaclass
    from jedi.api.names import Name
    from jedi.api.classes import Completion
    class FakeInterpreter:
        def __init__(self, source, namespaces):
            self.source = source
            self.namespaces = namespaces

        def complete(self):
            return [FakeCompletion("ABC$")]

    class FakeCompletion(Completion):
        def __init__(self, name):
            self.name = name
            self.complete = name
            self.type = "class"
            self.description = "abc"
            self.parent = Mock()
            self.full_name = "abc"

    interpreter = FakeInterpreter("aaa.bbb", [])
    completions = get_

# Generated at 2022-06-14 11:21:52.903707
# Unit test for function get_script_completions
def test_get_script_completions():
    candidates = get_script_completions(
        "pri", 1, 3, filename="/home/user/test.py", sys_path=[]
    )
    assert candidates[0].name == "print"
    assert candidates[0].full_name == "print"


if __name__ == "__main__":
    import os
    import sys

    _p = os.path.expanduser("~/Tests/Python/Python")
    sys.path.insert(0, _p)
    os.environ["PYTHONPATH"] = _p
    candidates = get_script_completions(
        "import tests.objects\ntests.objects.q", 5, 2, filename="/home/user/test.py",
    )

# Generated at 2022-06-14 11:22:05.990031
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    Test case for function get_interpreter_completions. This file is not a unittest module,
    so running it directly will not run this test.
    """
    import os
    import sys

    from mypy.api import run

    source = """\
import math
import numpy

math.
numpy.

"""

    # We need to set a temporary path to the current directory because the current working directory
    # will not be in jedi's sys path.
    test_path = os.path.abspath(os.getcwd())
    sys.path.append(test_path)

    # Run mypy to get the namespaces.

# Generated at 2022-06-14 11:22:12.471563
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate.names import ParamName
    from jedi.parser_utils import get_statement_of_position

    from thonny.jedi_utils import get_interpreter_completions, ThonnyCompletion

    namespaces = [{'__builtins__': {'sorted': sorted,
                   'list': list,
                   'set': set,
                   'tuple': tuple}}]
    code = 'import sys\nimport builtins\nsorted(list(set(tuple())))'

    completions = get_interpreter_completions(code, namespaces)

    assert len(completions) == 3
    assert [item.name for item in completions] == ['sorted', 'list', 'set']


# Generated at 2022-06-14 11:22:25.053393
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # test with sys_path
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sys.path.append(os.path.join(os.path.dirname(__file__), "jedi_test_path"))
    print(sys.path)
    completions = get_interpreter_completions('from datetime import d', [{'d': datetime.datetime(2020, 1, 1)}], sys.path)
    assert len(completions) == 4
    assert set(['datetime', 'date', 'time', 'timedelta']) == {completion.name for completion in completions}

    # test without sys_path
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

# Generated at 2022-06-14 11:22:35.208878
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import mock
    from jedi.api.application import Interpreter
    from jedi.api import classes
    from parso.python.tree import Module
    from parso.python.parser import ParserSyntaxError
    from jedi import __version__ as jedi_version
    jedi_version = jedi_version[:4]


# Generated at 2022-06-14 11:22:47.633490
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    completions = get_interpreter_completions("import os", [], sys_path=[])[:3]
    assert len(completions) == 3
    assert completions[0].name == "os"
    assert completions[1].name == "os.O_APPEND"
    assert completions[2].name == "os.O_ASYNC"

    completions_including_dot0 = get_interpreter_completions("import os.p", [], sys_path=[])
    assert len(completions_including_dot0) > len(completions)
    assert completions_including_dot0[0].complete == "os.path"

    completions_including_dot1 = get_interpreter_completions("import os.path", [], sys_path=[])


# Generated at 2022-06-14 11:22:54.720784
# Unit test for function get_definitions
def test_get_definitions():
    source = 'def func(x, y, z=2):\n pass\n\nclass A: pass\n\nvar1, var2, var3 = "a", "b", "c"'
    definitions = get_definitions(source, 2, 0, 'source.py')
    assert len(definitions) == 3
    assert definitions[0].description == "def func(x, y, z=2)"
    assert definitions[1].description == "class A"
    assert definitions[2].description == "str"

# Generated at 2022-06-14 11:23:08.754662
# Unit test for function get_script_completions
def test_get_script_completions():
    """
    This function tests whether ThonnyCompletion is a suitable class to be used in
    place of jedi.api.classes.Completion
    """
    import jedi

    if _using_older_jedi(jedi):
        sample_completion = jedi.Script("import math").completions()[0]
    else:
        project = _get_new_jedi_project(["."])
        sample_completion = jedi.Script("import math", project=project).complete()[0]


# Generated at 2022-06-14 11:23:19.019466
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """Ensures that the custom module is imported in the interpreter."""
    interp_completions = get_interpreter_completions(
        "import my_module\nmy_module.",
        namespaces=[{"locals": {}, "globals": {}, "builtins": {}}],
        sys_path=["."],
    )
    # Test that we have completions available
    assert len(interp_completions) >= 1
    assert interp_completions[0].name == "my_func"
    assert interp_completions[0].complete == "my_func()"
    assert interp_completions[0].type == "function"
    assert interp_completions[0].parent == "my_module"
    assert interp_completions[0].full_name

# Generated at 2022-06-14 11:23:37.116335
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():

    import jedi
    script = """
import os
import hashlib
"""
    completions = get_interpreter_completions(script, [], sys_path=[])
    assert any(completion.complete == "os" for completion in completions), "os module should be in completions"



# Generated at 2022-06-14 11:23:45.920324
# Unit test for function get_script_completions
def test_get_script_completions():
    print(get_script_completions(source="t", row=1, column=1, filename="dummy.py"))
    print(get_script_completions(source="t.", row=1, column=2, filename="dummy.py"))
    print(get_script_completions(source="time.", row=1, column=5, filename="dummy.py"))
    print(get_script_completions(source='time.strftime("', row=1, column=15, filename="dummy.py"))
    print(get_script_completions(source='time.strftime("%', row=1, column=16, filename="dummy.py"))

# Generated at 2022-06-14 11:23:59.656926
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.plugins.jedi_backend import get_script_completions

    code = '"Hello" + "world"'
    completions = get_script_completions(code, 1, 7)
    assert len(completions) == 1
    assert completions[0]["name"] == "lower"
    assert completions[0]["complete"] == "lower()"
    assert completions[0]["type"] == "function"
    assert completions[0]["description"]
    assert completions[0]["parent"] == "str"
    assert completions[0]["full_name"] == "str.lower"

    completions = get_script_completions("import ma", 1, 8)
    assert len(completions) == 2

# Generated at 2022-06-14 11:24:11.299396
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions("import sys\nsys.", 4, 4, "sample.py")
    assert get_script_completions("import time\ntime.", 4, 5, "sample.py")
    assert get_script_completions("import time as t\nt.", 4, 2, "sample.py")
    assert get_script_completions("import sys\nprint(sys.p", 4, 10, "sample.py")
    assert get_script_completions("from time import time\ntime.", 4, 5, "sample.py")
    assert get_script_completions("from time import time as t\nt.", 4, 2, "sample.py")
    assert get_script_completions("import os.path\nos.path.", 4, 9, "sample.py")
    assert get_

# Generated at 2022-06-14 11:24:19.761626
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.evaluate import compiled
    compiled.builtin = compiled.builtins.builtin

    # Test functions
    def test_function(source: str, row: int, column: int, expected_complete: str, expected_module_name: str):
        definitions = get_definitions(source, row, column, "test_file")
        assert len(definitions) != 0
        assert definitions[0].complete == expected_complete and definitions[0].module_name == expected_module_name

    # Test function definitions
    test_function("def f():\n    pass\n\nf", 3, 0, "def f():", "test_file")

    # Test builtin functions

# Generated at 2022-06-14 11:24:33.091396
# Unit test for function get_script_completions
def test_get_script_completions():
    def run_test(source_lines, row, column, expected_completions):
        source = "\n".join(source_lines)
        actual_completions = get_script_completions(source, row, column, "test.py")
        completions = sorted([c.name for c in actual_completions])
        assert completions == expected_completions

    run_test(
        ["def f(x, y=1,"],
        1,
        9,
        ["z", "y", "x", "self"],
    )

    run_test(
        ["class Base:", "    def m(self, x, y=1,"],
        2,
        10,
        ["z", "y", "x", "self"],
    )


# Generated at 2022-06-14 11:24:45.576741
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    def check_completions(code, expected_items):
        completions = get_interpreter_completions(code, [])
        actual_items = sorted(item["name"] for item in completions)
        if actual_items != expected_items:
            raise AssertionError(
                "Code:\n"
                + code
                + "\nexpected:\n"
                + pprint.pformat(expected_items)
                + "\nactual:\n"
                + pprint.pformat(actual_items)
            )

    check_completions("", ["__annotations__", "__builtins__"])

    check_completions("2+2", ["__add__", "__radd__", "__class__", "__contains__"])


# Generated at 2022-06-14 11:24:54.920120
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest import TestCase, main

    class Test(TestCase):
        def test_simple(self):
            source = "a = 1\n"
            completions = get_script_completions(
                source, row=0, column=1, filename="<input>"
            )
            self.assertEqual(len(completions), 0)

            # should not crash
            completions = get_script_completions("import something.really.nesting\n", 0, 0, "")

    main()



# Generated at 2022-06-14 11:25:04.952337
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    test_input = r"""
import math

math.sq"""

    completions = get_interpreter_completions(
        source=test_input,
        namespaces=[
            {"type": "statement", "module_path": None, "namespaces": [], "is_analysis": True}
        ],
    )
    names = [c["name"] for c in completions]
    assert "sqrt" in names
    assert "power" in names
    assert "fsum" in names
    assert "e" not in names

# Generated at 2022-06-14 11:25:12.739135
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    from jedi.evaluate import representation as er

    source = '"foo".upper'
    result = get_interpreter_completions(source, [])
    assert [c.name for c in result] == ["upper"]
    assert [c.complete for c in result] == ["upper"]
    assert [c.type for c in result] == ["function"]
    assert [c.description for c in result] == [
        "upper(${1:self}) method of builtins.str instance\nConvert a string into all uppercase."
    ]
    assert [isinstance(c.parent, er.Instance) for c in result]
    assert [c.full_name for c in result] == ["str.upper"]

    result = get_interpreter_completions("print.", [])

# Generated at 2022-06-14 11:25:40.145754
# Unit test for function get_script_completions
def test_get_script_completions():
    """
    Test for function get_script_completions()
    """
    import jedi
    if _using_older_jedi(jedi):
        expected_name = "print("
        expected_complete = "print("
    else:
        expected_name = "print"
        expected_complete = "print("

    expected_type = "statement"
    expected_description = "<built-in function print>"
    expected_parent = "builtins"
    expected_full_name = "builtins.print"
    completions = get_script_completions("print", 1, 1, "dummy_file")
    assert len(completions) == 1
    assert completions[0].name == expected_name
    assert completions[0].complete == expected_complete
    assert completions[0].type == expected_type


# Generated at 2022-06-14 11:25:43.544663
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    code = "import re\nre.ma"
    completions = get_interpreter_completions(code, [{}])
    completion_names = [c["complete"] for c in completions]
    assert completion_names == ["re.match"]

# Generated at 2022-06-14 11:25:56.193019
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Taken from jedi/tests/test_interpreter.py, https://github.com/davidhalter/jedi/blob/0.12.1/jedi/tests/test_interpreter.py
    # See also https://github.com/davidhalter/jedi/blob/0.12.1/CHANGELOG.md
    code = "import datetime; datetime.da"
    completions = get_interpreter_completions(code, [{}])
    assert len(completions) > 0
    completion = completions[0]
    assert completion.name == "date" and completion.complete == "date"
    assert completion.description.startswith("datetime.date")



# Generated at 2022-06-14 11:26:10.424035
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import get_completions
    import jedi
    from thonny.plugins.micropython.backend import MicroPythonProxy
    from thonny.languages.jedi_utils import ThonnyCompletion

    assert _using_older_jedi(jedi) == True

    sys_path = ["/home/user/.thonny/BundledMicroPython/esp32-1.12.0-222-g7f2cb2cb3.zip/lib"]

# Generated at 2022-06-14 11:26:22.128820
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock

    namespaces = [
        {"a": 1, "b": 2},
        {"c": 3, "d": 4},
    ]

    # Up to jedi 0.16
    completion_a = Mock()
    completion_b = Mock()
    completion_c = Mock()
    completion_d = Mock()
    completion_a.name = "a=1"
    completion_b.name = "b=2"
    completion_c.name = "c=3"
    completion_d.name = "d=4"
    completion_a.type = ""
    completion_b.type = ""
    completion_c.type = ""
    completion_d.type = ""
    completion_a.description = ""
    completion_b.description = ""

# Generated at 2022-06-14 11:26:33.155416
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter

    completions = get_interpreter_completions(
        '"".up',
        [
            Interpreter(
                'import json',
                [
                    {
                        "type": "module",
                        "name": "json",
                        "docstring": "The json module implements JSON encoders and decoders [{"
                    }
                ],
            ).namespace_packages(),
            Interpreter('json.loads("")', [{"foo": "bar"}]).namespace_packages(),
        ],
    )


# Generated at 2022-06-14 11:26:43.474471
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # This test may fail if jedi version is not 0.14.1
    source = "import sys; sys.se"
    completions = get_interpreter_completions(source, [dict()])
    assert len(completions) > 2
    names = [c.complete for c in completions]
    assert "sys.setdefaultencoding(" in names
    assert "sys.setprofile(" in names
    assert "sys.setrecursionlimit(" in names
    assert "sys.settrace(" in names

if __name__ == "__main__":
    test_get_interpreter_completions()

# Generated at 2022-06-14 11:26:44.405690
# Unit test for function get_definitions

# Generated at 2022-06-14 11:26:49.469049
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    source = "import pandas as pd\npd.DataFrame([1,2,3])\npd.DataFrame([1,2,3]).head(10)"
    namespaces = [Interpreter(source, []).namespace]
    results = get_interpreter_completions(source, namespaces, sys_path=["thonny_test"])
    assert len(results) > 0
    assert any([r.complete == "head()" for r in results])

# Generated at 2022-06-14 11:27:02.526331
# Unit test for function get_script_completions
def test_get_script_completions():
    # We deliberately use an older Jedi version here to detect differences
    # that would cause wrong completions
    import sys
    import os
    import site
    import jedi
    original_path = sys.path.copy()
    site.ENABLE_USER_SITE = False
    sys.path.insert(0, os.path.expandvars("$HOME/.local/lib/python3.7/site-packages"))
    sys.path.insert(0, os.path.expandvars("$HOME/.local/lib/python3.6/site-packages"))
    sys.path.insert(0, os.path.expandvars("$HOME/.local/lib/python3.5/site-packages"))

# Generated at 2022-06-14 11:27:32.079367
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import sys
    import unittest


# Generated at 2022-06-14 11:27:38.557395
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest.mock

    sys_path = ['/some/path']
    source_text = 'import math\nmath.sq'
    namespaces = [{'x': 1}]
    def _get_namespaces():
        return namespaces
    with unittest.mock.patch('jedi.Interpreter.get_namespaces'):
        completions = get_interpreter_completions(source_text, None, sys_path)
    assert [completion.name for completion in completions] == ['sqrt']


# Generated at 2022-06-14 11:27:39.820271
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:27:51.578220
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:28:05.390688
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import sys
    from jedi import Interpreter
    from jedi.api.project import Project

    sys.path.append("/tmp")

    # NB! This test assumes that this file is located at thonny/plugins/jedi_utils.py
    # in the project root, or change the path in the open call below
    source = open("/tmp/thonny/plugins/jedi_utils.py").read()
    namespaces = [{"a": 1, "b": 2}]

    completions = get_interpreter_completions(source, namespaces)

    assert len(completions) > 500

    project = Project(path="/tmp")
    interpreter1 = Interpreter(source, namespaces, project=project)
    completions1 = interpreter1.complete()

# Generated at 2022-06-14 11:28:12.734814
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    assert jedi.__version__
    print(jedi.__version__)
    source = "import os"
    namespaces = [{}]
    completions = get_interpreter_completions(source, namespaces)
    assert completions
    assert len(completions) > 10
    for completion in completions:
        assert "os" in completion.complete
        assert "." in completion.complete
        assert completion.name
        assert completion.type
    assert "os.path" in [comp.complete for comp in completions]

# Generated at 2022-06-14 11:28:18.576562
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("im", 0, 2, "?")
    assert len(completions) > 0
    completion = completions[0]
    assert isinstance(completion, ThonnyCompletion)
    assert completion.full_name == "import"

# Generated at 2022-06-14 11:28:30.303035
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import math
    import urllib.request
    import http.server

    import jedi

    comps = get_interpreter_completions(
        source="",
        namespaces=[
            {"math": math},
            {"urllib.request": urllib.request},
            {"http.server": http.server},
        ],
    )

    # jedi 0.16 has a bug with getting completions from sys.modules
    # https://github.com/davidhalter/jedi/issues/1843
    if _using_older_jedi(jedi):
        assert len(comps) > 1500
    else:
        assert len(comps) > 2000

    # from jedi import *

# Generated at 2022-06-14 11:28:30.814875
# Unit test for function get_definitions

# Generated at 2022-06-14 11:28:36.287703
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    Create a SimpleNamespace object using the built-in function `vars` and
    pass it as a namespaces object to `get_interpreter_completions`.
    """
    from jedi import Interpreter

    foo = SimpleNamespace()  # type: ignore
    foo.bar = 1
    n = vars(foo)
    completions = get_interpreter_completions("n.ba", [n])
    assert [c.name for c in completions] == ["bar"]



# Generated at 2022-06-14 11:29:06.900845
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import misc_utils

    from importlib import resources

    source = resources.read_text(__name__, "sample.py")
    row = 6
    column = 12
    filename = "sample.py"

    completions = get_script_completions(source, row, column, filename)

    for item in completions:
        print(item.name)
    print("--------")
    assert "cal" in [item.name for item in completions]
    assert "callable" in [item.name for item in completions]


# Generated at 2022-06-14 11:29:21.382028
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest

    class TestBase(unittest.TestCase):
        def verify(self, source, namespaces, expected):
            actual = get_interpreter_completions(source, namespaces)
            self.assertEqual(len(actual), len(expected))
            for a, e in zip(actual, expected):
                self.assertEqual(a.name, e[0])
                self.assertEqual(a.type, e[1])

    class Test(TestBase):
        def test_syntax_error(self):
            self.verify("syntax_error", [{}], [])


# Generated at 2022-06-14 11:29:34.373097
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script, Interpreter

    def equal_completions(completions1, completions2):
        def get_vars(completions):
            return set(c.name for c in completions)

        return get_vars(completions1) == get_vars(completions2)

    sys_path = ["/home/foo", "/home/bar"]

    # test new jedi
    script1_completions = Script(
        code="import json\njson.", path="test.py", project=_get_new_jedi_project(sys_path)
    ).complete()

# Generated at 2022-06-14 11:29:48.104607
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.jedi import get_script_completions
    from jedi import __version__ as jedi_version
    from itertools import groupby
    import operator

    completions = get_script_completions("""a = 1
b = 2

plt.m""", 3, 12, "whatever.py")

    assert len(completions) > 2
    assert [c.type for c in completions] == ['function', 'function', 'function', 'module', 'keyword', 'keyword', 'keyword', 'class', 'function']

    # test if the completions are sorted in alphabetic order and have unique names
    assert completions[0].name == "matplotlib"
    assert completions[1].name == "max"
    assert completions[2].name == "mean"
    names

# Generated at 2022-06-14 11:29:54.564764
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions(
        "def foo():\n    f = ", 3, 10, "test.py"
    ) == get_script_completions(
        "def foo():\n    f = ", 3, 10, "test.py", sys_path=["."]
    )
    assert get_script_completions(
        "def foo():\n    f = ", 3, 10, "test.py"
    ) != get_script_completions(
        "def foo():\n    f = ", 3, 10, "test2.py"
    )

# Generated at 2022-06-14 11:29:58.109404
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():

    source = "import sys\nprint(sy"
    completion = get_interpreter_completions(source, [])

    assert completion[0].name == "sys"



# Generated at 2022-06-14 11:30:08.386078
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock
    from jedi.api.classes import Completion
    from parso.python.tree import ListCompFor, ListCompIf, Module, Name

    from thonny.plugins.jedi_utils import get_interpreter_completions

    def make_mock_completion(name, complete, description):
        completion = Mock(Completion)
        completion.name = name
        completion.complete = complete
        completion.description = description
        return completion

    module = Module(children=[])
    f1 = ListCompFor(children=[])
    var = Name(children=["var"], parent=f1)
    f1.children.append(var)
    cond = ListCompIf(children=[])
    f1.children.append(cond)


# Generated at 2022-06-14 11:30:18.236348
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = """
import os
os.
"""[
        1:
    ]
    result = get_interpreter_completions(
        source,
        [
            {
                "__name__": "__main__",
                "os": __import__("os"),
                "__builtins__": __import__("builtins"),
            }
        ],
    )
    names = {item.name for item in result}
    assert "name" in names
    assert "path" in names
    assert "__file__" in names
    assert "__path__" not in names

# Generated at 2022-06-14 11:30:25.390107
# Unit test for function get_script_completions
def test_get_script_completions():
    def check(source, row, column, filename, expected_results):
        # expected_results is a tuple of (name, complete)
        results = get_script_completions(source, row, column, filename)
        results = [(r.name, r.complete) for r in results]
        assert results == expected_results

    check(
        "import os\n", 0, 7, "example.py", [("os", "os."), ("os.path", "os.path.")]
    )

    check(
        "import os.path\n", 0, 7, "example.py", [("os", "os"), ("os.path", "os.path.")]
    )

    check("os.path.abspat", 10, 4, "example.py", [("abspath", "abspath(")])



# Generated at 2022-06-14 11:30:37.603380
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import json
    import sys
    import os
    import traceback
    if sys.argv[1] == "test-jedi-v18":
        jedi_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "jedi_lib")
        sys.path.append(jedi_path)
        try:
            import jedi
            print(json.dumps(get_interpreter_completions(sys.argv[2], sys.argv[3], sys.argv[4])).encode('utf-8'))
            code = 0
        except Exception:
            print(traceback.format_exc())
            code = 1
    else:
        code = 2

    sys.exit(code)

# Generated at 2022-06-14 11:31:14.223258
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    if jedi.__version__[:4] in ["0.15", "0.16"]:
        print("test_get_script_completions skipped for Jedi 0.15/0.16 since the results are different")
        return
    
    completions = get_script_completions("def f(a):\n    a.appen", 3, 12, "test.py")
    assert len(completions) > 0

    completion = [c for c in completions if "append" in c.name][0]
    assert completion.description == "append(object, /)"

    assert completion.type == "function"
    assert completion.parent == "list"

    completions = get_script_completions("import sys; sys.", 4, 6, "test.py")