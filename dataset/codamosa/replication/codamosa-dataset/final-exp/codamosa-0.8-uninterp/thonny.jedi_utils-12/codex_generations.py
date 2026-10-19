

# Generated at 2022-06-14 11:21:20.406572
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    print(get_interpreter_completions('1+1', [{"imported module": {"__builtins__": __builtins__}}]))
    print(get_interpreter_completions('1+1', [{"imported module": {"__builtins__": __builtins__}}], []))
    print(get_interpreter_completions('1+1', [{"imported module": {"__builtins__": __builtins__}}], [""]))

# Generated at 2022-06-14 11:21:34.692263
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions("from datetime import", [{}])[0].name == "datetime"
    assert get_interpreter_completions("import datetime\ndatetime.", [{}])[0].name == "date"
    assert get_interpreter_completions("from datetime import", [{}])[0].name == "datetime"
    assert get_interpreter_completions("datetime", [{}])[0].name == "datetime"
    assert get_interpreter_completions("import datetime\ndatetime.", [{}])[0].name == "date"
    assert get_interpreter_completions("from datetime import", [{"datetime": datetime}])[0].name == "date"
    assert get_interpreter

# Generated at 2022-06-14 11:21:47.854863
# Unit test for function get_script_completions
def test_get_script_completions():
    import unittest

    import jedi
    import parso
    import jedi.parser
    import jedi.parser_utils

    class TestCase(unittest.TestCase):
        def test_always_returns_list(self):
            self.assertIsInstance(completions, list)
        def test_completion_len(self):
            self.assertGreater(len(completions), 0)
        def test_completion_type(self):
            for completion in completions:
                self.assertIsInstance(completion, (jedi.Completion,ThonnyCompletion))
        def test_completion_name(self):
            for completion in completions:
                self.assertIsInstance(completion.name, str)

# Generated at 2022-06-14 11:21:58.611619
# Unit test for function get_script_completions
def test_get_script_completions():
    # test for 0.16
    completions = get_script_completions(
        source="import os\nos.path.j", row=1, column=13, filename="stdlib.py"
    )
    names = [c.name for c in completions]
    assert "join" in names

    # test for 0.18
    completions = get_script_completions(
        source="import os\nos.path.j", row=1, column=12, filename="stdlib.py"
    )
    names = [c.name for c in completions]
    assert "join" in names



# Generated at 2022-06-14 11:22:06.105925
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.python.parser import ParserSyntaxError
    import jedi
    from jedi.api.project import ProjectEnvironmentError
    from thonny.globals import get_runner, get_current_script_path
    from thonny.running import SubprocessFrontend
    runner = get_runner()

    runner.start()

# Generated at 2022-06-14 11:22:12.585866
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions(
        "import sys\nsys.stderr.f", 0, 18, "test.py"
    )
    assert isinstance(completions, list)
    assert len(completions) >= 1
    for completion in completions:
        # assert completion["name"] == completion["complete"]
        assert completion["type"] == "function"
        assert completion["description"]
        assert completion["parent"]
        assert "__builtin__" not in completion["full_name"]



# Generated at 2022-06-14 11:22:25.118818
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    from jedi.api.classes import Completion  # pylint: disable=no-name-in-module

    dummy_namespaces = [
        {"os": "mod"},
        {"os.path": "mod"},
        {"os.path.join": "func"},
        {"os.listdir": "func"},
    ]

    dummy_results = [
        ("os.", ["path"]),
        ("os.path.", ["join"]),
        ("os.path.join.", []),
        ("os.", ["path", "listdir"]),
    ]
    for dummy_source, expected_names in dummy_results:
        print("source:", dummy_source)
        results = get_interpreter_completions(dummy_source, dummy_namespaces)

# Generated at 2022-06-14 11:22:35.242700
# Unit test for function get_definitions
def test_get_definitions():
    """
    Thonny takes care of using correct Jedi version, so this test needs to be run with
    different versions.
    """
    import os
    import sys

    # jedi 0.13
    sys.path.insert(0, os.path.expanduser("~/.vim/bundle/jedi-vim/jedi-0.13.2/jedi"))
    import jedi
    print("jedi 0.13")
    print_definitions(get_definitions("a", 0, 1, "test"), jedi)

    # jedi 0.14
    sys.path.insert(0, os.path.expanduser("~/.vim/bundle/jedi-vim/jedi-0.14.0/jedi"))
    import jedi
    print("jedi 0.14")
    print_definitions

# Generated at 2022-06-14 11:22:44.416470
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    source = """
    name = "My name is Thonny"
    """

    namespaces = [dict(name="main", path="<stdin>", source=source)]
    completions = get_interpreter_completions(source, namespaces)
    assert completions == [
        ThonnyCompletion(
            name="name",
            complete="name",
            type=jedi.api.classes.Name,
            description="str",
            parent=jedi.api.classes.Module,
            full_name="main.name",
        )
    ]

# Generated at 2022-06-14 11:22:55.002156
# Unit test for function get_script_completions
def test_get_script_completions():
    from importlib import invalidate_caches
    invalidate_caches()
    from jedi import __version__

    jedi_version = tuple(int(i) for i in __version__.split("."))
    print("Jedi version", jedi_version)

    import jedi
    source = 'import os; from os import path; from os.path import (abspath, join)\nos.path.abspath'
    filename = 'test.py'

    if jedi_version >= (0, 16):
        source = source.replace('path', 'pathdd')

    completions = get_script_completions(source, len(source.split('\n')), 100, filename)
    expected = 'abspath'
    if jedi_version < (0, 16):
        expected = 'abspath='


# Generated at 2022-06-14 11:23:18.578770
# Unit test for function get_definitions
def test_get_definitions():
    import unittest
    import os
    import pathlib

    def test_definitions(source: str, row: int, column: int, expected: List[str]):
        # print("Testing ", quote(source))

        definitions = get_definitions(source, row, column, "myfile.py")
        paths = [d.module_path for d in definitions]
        paths_as_str = [str(p) for p in paths]
        # print("   actual ", paths_as_str)

        expected_paths = []
        for p in expected:
            # convert /something to C:\something on Windows
            # otherwise some library and some test paths won't match
            expected_paths.append(str(pathlib.Path(p).resolve()))

        # print("   expected ", expected_paths)

# Generated at 2022-06-14 11:23:22.745182
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase

    class Test(TestCase):
        def test_simple(self):
            a = get_interpreter_completions("name_", [{"name_": "value"}], sys_path=[])
            self.assertEqual(a[0].name, "name_")

    Test().test_simple()

# Generated at 2022-06-14 11:23:31.677448
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso import tree
    from parso.python import tree
    from jedi.evaluate import Context, ModuleContext, ClassContext, FunctionContext, compiled
    from jedi.parser_utils import _copy_of_get_statement_of_position
    from jedi.evaluate import tree_name
    from jedi.evaluate.compiled import fake
    from jedi.evaluate.context.module import ModuleContext
    from jedi.evaluate.representation import AbstractCompiledObject, AbstractDefinition, \
    TreeInstance, AbstractInstance, CompiledInstance, RepresentationMixin, CompiledValueSet
    from jedi.evaluate.context import compile_path
    from jedi.evaluate.param import CompiledParam
    from jedi.evaluate.base_context import ValueSet
    from jedi.evaluate.helpers import FakeStatement

# Generated at 2022-06-14 11:23:35.117836
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions("""from math import *\nfloo""", 0, 8, "")[0].name == "floor"

# Generated at 2022-06-14 11:23:45.945512
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import get_workbench, get_shell

    completions = get_script_completions("func(agr)", 3, 5, "test.py")
    assert len(completions) > 0

    get_workbench().set_option("editor.jedi.sys_path", [])

    completions = get_script_completions("func(agr)", 3, 5, "test.py")
    assert len(completions) > 0

    get_workbench().set_option("editor.jedi.sys_path", ["/usr/local/lib/python3.5"])

    completions = get_script_completions("func(agr)", 3, 5, "test.py")
    assert len(completions) > 0


# Generated at 2022-06-14 11:23:48.277868
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert len(get_interpreter_completions("int", [{}])) > 20

# Generated at 2022-06-14 11:24:01.585091
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    import sys
    import os

    completions = get_script_completions(
        "import sys\nsys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))\nimport turtl",
        3,
        33,
        "",
        sys.path,
    )

    for completion in completions:
        print(completion.name)

    assert len(completions) > 0
    if _using_older_jedi(jedi):
        assert "forward" in [c.name for c in completions]
        assert "dot" in [c.name for c in completions]
    else:
        assert "forward" not in [c.name for c in completions]

# Generated at 2022-06-14 11:24:02.743198
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:24:09.505794
# Unit test for function get_script_completions
def test_get_script_completions():
    source = 'import sys\na = sys\na'
    completions = get_script_completions(source, row=3, column=3, filename='test.py')
    assert len(completions) > 0
    assert 'sys' in [c['name'] for c in completions]
    assert 'executable' in [c['name'] for c in completions]


# Generated at 2022-06-14 11:24:18.337566
# Unit test for function get_definitions
def test_get_definitions():
    # get_definitions() should return an empty
    # list for a variable where no definition
    # can be found.
    # When running the command, python
    # should not crash without printing a
    # traceback.
    t = get_definitions("a = 1\na[0] = 2",3,1, "test_file")
    assert t == []

    # get_definitions() should return a
    # non-empty list for a variable which
    # has been defined
    t = get_definitions("x = 1\nx = 2",2,1, "test_file")
    assert t != []

# Generated at 2022-06-14 11:24:35.869312
# Unit test for function get_definitions
def test_get_definitions():
    from parso.python.tree import Module
    from parso.python.parser import Parser
    import parso
    import jedi


# Generated at 2022-06-14 11:24:36.528300
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:24:42.598829
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter

    namespaces = [
        {'a': 1},
        {'b': 'heloo'},
    ]

    completions = get_interpreter_completions('a.b.', namespaces)
    assert len(completions) == 1
    assert completions[0].name == 'b'
    assert completions[0].description == 'str'

# Generated at 2022-06-14 11:24:54.962838
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    completions = get_script_completions("import sys", 1, 7, "test")
    assert completions
    assert len(completions) > 40
    any_completion = completions[0]
    assert isinstance(any_completion, ThonnyCompletion)

    completions = get_script_completions("import sys", 0, 0, "test")
    assert not completions

    if jedi.__version__ < "0.18.0":
        script = jedi.Script("sys.", 1, 3, "test")
        assert len(script.completions()) > 40
        assert isinstance(script.completions()[0], jedi.api.classes.Completion)
    else:
        script = jedi.Script(code="sys.", path="test")
        assert len

# Generated at 2022-06-14 11:24:58.516937
# Unit test for function get_definitions
def test_get_definitions():
    import jedi
    assert get_definitions("import math\n" "math.c", row=2, column=5, filename="") == jedi.names("math")


# Generated at 2022-06-14 11:25:10.333842
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest import mock
    from thonny.jedi_utils import get_script_completions
    logger = logging.getLogger(__name__)

    source = "import "
    row = 1
    column = 9
    filename = "jedi_test.py"

    script = mock.Mock(spec=['get_completions'])

# Generated at 2022-06-14 11:25:12.613827
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import get_workbench
    wb=get_workbench()

# Generated at 2022-06-14 11:25:25.261631
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:25:36.705830
# Unit test for function get_definitions
def test_get_definitions():
    script = '''
x = "a"
x = "b"
x = 42
x''' 
    defs = get_definitions(script, 3, 3, "")
    assert len(defs) == 1
    assert defs[0].name == 'x' 
    assert defs[0].in_builtin_module()
    assert defs[0].module_name == 'builtins'
    assert defs[0].module_path is None
    assert defs[0].line is None
    assert defs[0].column is None

if __name__ == "__main__":
    test_get_definitions()

# Generated at 2022-06-14 11:25:46.334102
# Unit test for function get_script_completions
def test_get_script_completions():
    # This test checks that using sys_path with Jedi works
    # The module _io.py should contain a function "BufferedWriter"
    # Note that the function has been seen in _io.py only since Python 3.4
    # However, for some reason Jedi can't find the module _io.py
    # unless some of the standard library is added to sys_path

    source = "from _io import "
    row = 0
    column = 18
    filename = "<stdin>"

    import os
    import sys
    import jedi

    interpreter_completions = None

# Generated at 2022-06-14 11:26:13.206610
# Unit test for function get_script_completions
def test_get_script_completions():
    # Test completions of a statement
    completions = get_script_completions(
        "import sys\nsys.pa", row=1, column=12, filename="temp.py"
    )
    assert len(completions) > 0
    assert "path" in [c.complete for c in completions]
    assert "path_hooks" in [c.complete for c in completions]

    # Test completions of an expression
    completions = get_script_completions(
        "sys.pa", row=0, column=6, filename="temp.py"
    )
    assert completions is not None
    assert len(completions) > 0
    assert "path" in [c.complete for c in completions]
    assert "path_hooks" in [c.complete for c in completions]

# Generated at 2022-06-14 11:26:14.857511
# Unit test for function get_definitions
def test_get_definitions():
    assert len(get_definitions("import io", 0, 0, "")) == 1



# Generated at 2022-06-14 11:26:24.157133
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.globals import get_workbench

    get_workbench().set_option("jedi_sys_path", ["/usr/lib/python3.6/dist-packages"])
    assert len(get_interpreter_completions("import sys", [{"sys": sys}])) > 100
    assert len(get_interpreter_completions("import sys", [{"sys": sys}])) == 0


if __name__ == "__main__":
    test_get_interpreter_completions()

# Generated at 2022-06-14 11:26:34.302251
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny import ui_utils

    source = '''def foo(a):
    return a
    
print(foo("A"))'''

    namespaces = [{"a": "A"}]
    completions = get_interpreter_completions(source, namespaces)

    labels = set()
    for c in completions:
        labels.add((c.name, c.description))
    assert labels == {("a", ""), ("foo(a)", "foo(a)")}
    assert completions[0].parent == "foo"
    assert completions[1].parent is None

    # find correct completion
    source = """a[0].upper()"""
    namespaces = [{"a": ["a", "A"]}]
    completions = get_interpreter_completions(source, namespaces)

# Generated at 2022-06-14 11:26:39.799428
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import os"
    namespaces = [{'__name__': '__main__', '__file__': '__main__', '__package__': None}]
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) > 0

# Generated at 2022-06-14 11:26:44.555602
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    
    if jedi.__version__[:2] in ["0.", "1."]:
        version = "old"
    else:
        version = "new"
        
    assert _get_script_completions_version() == version


# Generated at 2022-06-14 11:26:48.813394
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import patch

    with patch("thonny.jediutils.get_completions", side_effect=get_interpreter_completions):
        from thonny.jediutils import get_completions, get_interpreter_completions

        assert get_completions("int", [], 1, 1) == get_interpreter_completions("int", [])

# Generated at 2022-06-14 11:26:57.783730
# Unit test for function get_script_completions
def test_get_script_completions():
    result = get_script_completions(
        ".\n", 1, 0, "", sys_path=["/home/foo/thonny"]
    )
    assert len(result) == 1
    assert result[0].name == "."
    assert result[0].complete == "."
    assert result[0].type == "statement"
    assert result[0].description == "Current module"
    assert result[0].parent == "<module>"
    assert result[0].full_name == "."


# Generated at 2022-06-14 11:27:14.151924
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import __version__ as jedi_version
    from tkinter import Tk
    from thonny.globals import get_workbench
    from thonny import running

    script = "import threading; threading.Thre"
    row = 1
    column = 32
    filename = "t.py"
    version_tuple = tuple(int(v) for v in jedi_version.split("."))

    # make root window
    root = Tk()
    root.withdraw()
    get_workbench().set_default("view.show_debug_value_tooltip_on_hover", True)
    not_thread_found = True

    # check if the right completion is provided
    # when jedi version is 0.18 and above

# Generated at 2022-06-14 11:27:16.923740
# Unit test for function get_script_completions
def test_get_script_completions():
    from parso.python.parser import PythonParser
    from parso.python import tree


# Generated at 2022-06-14 11:27:39.427569
# Unit test for function get_definitions
def test_get_definitions():
    assert get_definitions("import sys", 0, 0, "") == []
    assert get_definitions("def f(): pass\nf()", 0, 0, "") == [definitions.FunctionDefinition("f", "f", "", "")]
    assert get_definitions("def f(): pass\nf()", 1, 0, "") == [definitions.FunctionDefinition("f", "f", "", "")]
    assert get_definitions("def f(): pass\nf()", 1, 2, "") == [definitions.FunctionDefinition("f", "f", "", "")]
    assert get_definitions("import sys\nf()", 1, 0, "") == []
    assert get_definitions("f()", 0, 0, "") == []

# Generated at 2022-06-14 11:27:51.383554
# Unit test for function get_script_completions
def test_get_script_completions():
    from collections import namedtuple

    Completion = namedtuple(
        "Completion", ["name", "full_name", "type", "description", "complete"]
    )
    result = get_script_completions(
        "",
        1,
        1,
        "",
        [
            "C:\\Users\\irakli\\Downloads\\python\\Python38-32\\Lib\\site-packages",
            "C:\\Users\\irakli\\Downloads\\python\\Python38-32\\lib\\site-packages",
            "C:\\Thonny\\PythonFiles",
            "C:\\Thonny\\PythonFiles\\site-packages",
        ],
    )

# Generated at 2022-06-14 11:28:05.386600
# Unit test for function get_definitions
def test_get_definitions():
    # type: () -> None
    assert isinstance(get_definitions("soma = sum", 0, 0, ""), list)
    assert isinstance(get_definitions("soma = sum", 0, 0, "")[0], ThonnyCompletion)
    assert get_definitions("soma = sum", 0, 0, "")[0].name == "sum"
    assert get_definitions("soma = sum", 0, 0, "")[0].complete == "sum("
    assert get_definitions("soma = sum", 0, 0, "")[0].type == "function"
    assert get_definitions("soma = sum", 0, 0, "")[0].description == "sum(iterable) -> value"
    assert get_definitions("soma = sum", 0, 0, "")[0].parent

# Generated at 2022-06-14 11:28:12.487999
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api.classes import Definition
    from thonny import get_workbench
    from thonny.ui_utils import BackendEventLoop
    import os

    old_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Generated at 2022-06-14 11:28:27.057627
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api import Script
    from jedi.parser_utils import get_statement_of_position

    source = '''def foo():
    """foo docstring"""
    
    return
'''

    completions = get_script_completions(source, 4, 3, "foo.py")
    assert len(completions) > 5
    assert any(completion.complete == "foo" for completion in completions)
    assert any(completion.complete == "foo " for completion in completions)

    script = Script(source, 4, 3, "foo.py")
    # TODO: split in a subtest

# Generated at 2022-06-14 11:28:33.839842
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.jedi_utils import ThonnyCompletion

    completions = get_script_completions("v", 1, 1, "file.py")

    assert len(completions) > 0
    assert all(isinstance(c, ThonnyCompletion) for c in completions)

    names = [c.name for c in completions]
    assert "v" in names



# Generated at 2022-06-14 11:28:42.549172
# Unit test for function get_script_completions
def test_get_script_completions():
    expected_completions = [
        ThonnyCompletion(name="2", complete="2", type="int", description="int", parent=None, full_name="int"),
        ThonnyCompletion(name="print", complete="print", type="func", description="def print", parent=None, full_name="builtins.print"),
        ThonnyCompletion(name="print(", complete="print(", type="func", description="def print", parent=None, full_name="builtins.print"),
    ]
    assert get_script_completions("pri", 0, 3, "<stdin>") == expected_completions

# Generated at 2022-06-14 11:28:44.412916
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:28:55.518370
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    import sys
    majorv = sys.version_info.major
    minorv = sys.version_info.minor
    if majorv == 3:
        if minorv == 6:
            code = "import datetime\ndatetime.datetime."
        elif minorv == 7:
            code = "import datetime\ndatetime.datetime."
        elif minorv == 8:
            code = "import datetime\ndatetime.datetime."
    completions = get_script_completions(code, 2, 26, 'fake.py')
    assert isinstance(completions, list)
    assert isinstance(completions[0], ThonnyCompletion)

# Generated at 2022-06-14 11:29:08.981984
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.helper import assert_equals
    from jedi.api.interpreter import Interpreter

    completions = get_interpreter_completions("name",[])
    assert_equals(len(completions), 0)

    completions = get_interpreter_completions("None",[])
    assert_equals(len(completions), 0)

    completions = get_interpreter_completions("type(",[])
    assert_equals(len(completions), 0)

    completions = get_interpreter_completions("type(1",[])
    assert_equals(len(completions), 1)
    assert_equals(completions[0].name, "class 'int'")

    completions = get_interpreter_complet

# Generated at 2022-06-14 11:29:35.588017
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.python.tree import Name, ImportFrom, Leaf, ImportName, Node
    from parso.python.parser import ParserSyntaxError

    imports = [
        ImportName("os", None, None, None),
        ImportFrom("sys", [ImportName("path", None, None, None)], None, None),
        ImportFrom("tkinter", [ImportName("*", None, None, None)], None, None),
        ImportFrom("tkinter.ttk", [ImportName("Style", None, None, None)], None, None),
    ]

    source = "from sys import path\nfrom tkinter import *\nfrom tkinter.ttk import Style\nfrom abc import "

    completions = get_interpreter_completions(source, [imports])

# Generated at 2022-06-14 11:29:39.261294
# Unit test for function get_definitions
def test_get_definitions():
    from parso.python import tree

# Generated at 2022-06-14 11:29:45.357717
# Unit test for function get_definitions
def test_get_definitions():
    from thonny.jedi_utils import get_definitions
    from parso.python.tree import Module
    from types import ModuleType

    class MyModule(ModuleType):
        def __init__(self, name):
            self.__name__ = name

    import parso

# Generated at 2022-06-14 11:29:53.579741
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions('a.ctime', [dict()])[0].full_name == 'time.ctime'
    assert get_interpreter_completions('a.ctime.w', [dict()])[0].full_name == 'datetime.timedelta.weeks'
    assert get_interpreter_completions('a.ctime.w', [dict()])[0].name == 'weeks'
    assert get_interpreter_completions('a.ctime.w', [dict()])[0].description == '7'

    module = {'hello': 'world'}
    assert get_interpreter_completions('a.hello.u', [module])[0].full_name == 'hello.u'
    assert get_interpreter_completions

# Generated at 2022-06-14 11:30:06.491511
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import sys
    import unittest

    class TestGetInterpreterCompletions(unittest.TestCase):
        def test_no_namespaces(self):
            result = get_interpreter_completions('"".up', [], sys_path=[])
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].name, "upper")

        def test_with_namespaces(self):
            result = get_interpreter_completions('"".up', [{"x": 1000}], sys_path=[])
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0].name, "upper")
            self.assertEqual(result[1].name, "x")

    suite = unittest.TestLoader().loadT

# Generated at 2022-06-14 11:30:12.753771
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.codeview.completion_test_data import get_data

    for example in get_data():
        if example.get("only_jedi_newer_than"):
            import jedi

            if jedi.__version__ < example["only_jedi_newer_than"]:
                continue

        from thonny.misc_utils import running_on_mac_os

        if example.get("skip_on_mac_os") and running_on_mac_os():
            continue

        completions = get_interpreter_completions(
            example["input"], example["namespaces"], example.get("sys_path")
        )

        assert completions == example["expected_completions"], "Failed on " + repr(example)

# Generated at 2022-06-14 11:30:23.326018
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions("", 1, 1, "fake") == []
    assert get_script_completions("from t ", 1, 7, "fake") == ["from tkinter import", "from threading import"]
    assert get_script_completions("import thonny ", 1, 12, "fake") == ["import thonny", "import thonny.plugins"]
    assert get_script_completions("", 9, 9, "fake") == []
    assert get_script_completions("from dateti", 1, 10, "fake") == ["from datetime import"]
    assert get_script_completions("from dateti", 1, 10, "fake") == ["from datetime import"]
    assert get_script_completions("import threading", 1, 18, "fake") == []


# Generated at 2022-06-14 11:30:35.942833
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import os.path

    testfile_path = os.path.join(os.path.dirname(__file__), "..", "..", "tests", "testdata.py")
    with open(testfile_path) as fp:
        test_code = fp.read()

    namespaces = [{"a": 1, "b": "other"}]
    # print(get_interpreter_completions(test_code, namespaces))
    assert "a" in [c.name for c in get_interpreter_completions(test_code, namespaces)]
    assert "b" in [c.name for c in get_interpreter_completions(test_code, namespaces)]

# Generated at 2022-06-14 11:30:48.400108
# Unit test for function get_definitions
def test_get_definitions():
    from unittest.mock import patch

    source = """def foo():
    pass
foo()"""
    row = 2
    column = 1
    filename = "<untitled>"

    expected_completions = [
        ThonnyCompletion(
            name="foo",
            complete="foo",
            type="function",
            description="foo()",
            parent="builtins",
            full_name="builtins.foo",
        ),
    ]

    with patch("thonny.plugins.jedi_utils.jedi") as mock:
        mock.__version__ = "0.13.0"

        result = get_definitions(source, row, column, filename)
        assert result == expected_completions


# Generated at 2022-06-14 11:30:58.309288
# Unit test for function get_script_completions
def test_get_script_completions():
    import os
    import unittest

    path = os.path.dirname(os.path.abspath(__file__))
    sys_path = [path, os.path.join(path, "data")]
    completions = get_script_completions("from tes", 0, 7, filename="a.py", sys_path=sys_path)
    assert len(completions) == 1
    assert completions[0].name == "test_get_script_completions"

    completions = get_script_completions("from tes import test_get_script_completions", 0, 42, filename="a.py", sys_path=sys_path)
    assert len(completions) == 1
    assert completions[0].name == "test_get_script_completions"
   