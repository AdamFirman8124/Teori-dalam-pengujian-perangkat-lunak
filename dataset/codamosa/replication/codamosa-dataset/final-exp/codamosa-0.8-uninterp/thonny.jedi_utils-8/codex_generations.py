

# Generated at 2022-06-14 11:21:09.631395
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    print(jedi.__version__)

    my_ns = list({'foo': 'bar'})
    print(get_interpreter_completions('foo', my_ns))
    my_ns = list({'foo_bar': 'bar_foo'})
    print(get_interpreter_completions('foo', my_ns))

# Generated at 2022-06-14 11:21:20.742066
# Unit test for function get_script_completions
def test_get_script_completions():
    # Test with jedi == 0.13.0 :
    print("------------------[TEST] get_script_completions() ------------------")
    result_13 = get_script_completions("fro", 0, 0, "test")
    print("------------------[RESULT-JEDI13]------------------")
    if len(result_13) > 0:
        print("= completion.name pour " + result_13[0].name)
        print("= completion.complete pour " + result_13[0].complete)
        print("= completion.type pour " + str(result_13[0].type))
        print("= completion.description pour " + str(result_13[0].description))
        print("= completion.parent pour " + str(result_13[0].parent))

# Generated at 2022-06-14 11:21:29.007394
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():

    source = """
    import json
    json.load"""

    namespaces = [{"json": {"__builtin__": None}}]

    completions = get_interpreter_completions(source, namespaces)

    assert len(completions) == 1
    assert completions[0]["name"] == "json.loads"
    assert completions[0]["complete"] == "json.loads"

# Generated at 2022-06-14 11:21:50.994899
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    from jedi.api.classes import Completion
    from unittest.mock import patch
    source = "import sys\n"
    namespaces = [{'__name__': '__console__', '__doc__': None, 'sys': sys}]
    # Mock out jedi.Interpreter

# Generated at 2022-06-14 11:21:59.841288
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    jedi_version = jedi.__version__[:4]
    if jedi_version in ["0.13", "0.14", "0.15", "0.16", "0.17"]:
        source = "import os\nos."
        row = 2
        column = 4
        filename = "sample.py"
        sys_path = ["/home/user/sample/", "/usr/lib/python3.8/"]

        script = jedi.Script(source, row, column, filename, sys_path=sys_path)
        completions = script.completions()
        tweak_completions = _tweak_completions(completions)
        print(tweak_completions)

# Generated at 2022-06-14 11:22:09.390526
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    import os

    test_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "test"))
    test_file = os.path.join(test_folder, "data", "test_get_completions.py")
    script_completions = get_script_completions(open(test_file).read(), 3, 3, test_file)

    assert test_file in str(type(script_completions[0]))
    assert "completions" in dir(script_completions[0])
    assert "type" in dir(script_completions[0])
    assert "line" in dir(script_completions[0])

# Generated at 2022-06-14 11:22:22.957050
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.misc_utils import running_on_mac_os

    assert len(get_script_completions("", 1, 1, "")) != 0
    # TODO: this doesn't work on mac
    assert (len(get_script_completions("import sys", 1, 9, "")) > 100) != running_on_mac_os()
    assert get_script_completions("import sys", 1, 9, "")[0].name == "sys"

# Generated at 2022-06-14 11:22:34.215476
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.python_shell import MockIPythonInterpreter
    from unittest.mock import MagicMock

    mock_namespaces = ["", "", "", "", "", ""]
    mock_namespaces[0] = MagicMock()
    mock_namespaces[0].keys.return_value = ["abc", "abcdefg"]

    mock_namespaces[1] = MagicMock()
    mock_namespaces[1].keys.return_value = ["abcd", "abcdefg", "abcdefghijklmnoprstuvwxyz"]

    mock_namespaces[2] = MagicMock()
    mock_namespaces[2].keys.return_value = ["abcd", "abcdefghijklmnoprstuvwxyz"]

    mock_namespaces[3] = MagicMock

# Generated at 2022-06-14 11:22:35.843424
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:22:48.126820
# Unit test for function get_definitions
def test_get_definitions():
    # Test when the cursor is on top of an identifier
    result = get_definitions("""if True:
    prev_line = "second"    
    curr_line = "first"
    print(curr_line)
    print(prev_line)""", 2, 24, "")
    assert result[0].line == 3
    assert result[1].line == 2

    # Test when the cursor is on top of a string literal
    result = get_definitions("""if True:
    prev_line = "second"    
    curr_line = "first"
    print(curr_line)
    print(prev_line)""", 2, 45, "")
    assert result[0].line == 3
    assert result[1].line == 2

    # Test when the cursor is on top of a keyword

# Generated at 2022-06-14 11:23:17.210720
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    test_value = "import r"
    completions = get_interpreter_completions(
        test_value, [{"random": "random"}]
    )
    assert len(completions) > 0, "Failed to get completions"
    test_value = "import rr"
    completions = get_interpreter_completions(
        test_value, [{"random": "random"}]
    )
    assert len(completions) == 0, "Completions not found"
    test_value = "from r"
    completions = get_interpreter_completions(
        test_value, [{"random": "random"}, {"r123": "r123"}]
    )
    assert len(completions) > 0, "Completions not found"



# Generated at 2022-06-14 11:23:24.208267
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import sys\n"
    namespaces=[{
         "argv": [], 
         "builtins": {"__name__": "__builtins__"}, 
         "modules": {"sys": sys}, 
         "namespace_type": "dict"}, 
         {"__name__": "__main__", 
         "argv": [], 
         "modules": {}, 
         "namespace_type": "dict"}]
    completions=get_interpreter_completions(source, namespaces)
    assert any("sys" in c.name for c in completions)

# Generated at 2022-06-14 11:23:28.973792
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate.names import ValueName
    completions = get_interpreter_completions('foo', [{'__name__': '__main__'}])
    assert len(completions) == 1
    assert completions[0].name == "foo"
    assert isinstance(completions[0].parent, ValueName)



# Generated at 2022-06-14 11:23:42.304993
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.pgen2.grammar import Grammar
    from parso import parse
    import json

    # Build a parser out of the latest Python 3 grammar.
    with open("testdata/Python.gram", 'rb') as f:
        # Python.gram is provided by parso
        grammar_text = f.read()
        grammar = Grammar(grammar_text)

    # The parser expects a Python code as bytes.
    source = b'import json; json.l'

    # Parse the code
    tree = parse(source, version='3.7')
    #print(str(tree))

    # Get completions at the cursor (position of l in json.l)
    result = get_interpreter_completions(source.decode(), [{"json": json}])

    for res in result:
        print

# Generated at 2022-06-14 11:23:44.517642
# Unit test for function get_definitions
def test_get_definitions():
    assert get_definitions("os.path.abspath", 0, 0, "").type == 'module'

# Generated at 2022-06-14 11:23:58.186146
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    code = "import os\nos.path.join"

    def get_full_names(source):
        completions = get_interpreter_completions(
            # jedi.api.Interpreter is different in 0.14 and 0.15
            source, [{"__builtins__": __builtins__, "os": os}]
        )
        full_names = [c.full_name for c in completions]
        return full_names

    print("Testing jedi 0.14+")
    result = get_full_names(code)

# Generated at 2022-06-14 11:24:08.396743
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock

    jedi = Mock()
    jedi.__version__ = "0.17.2"
    source = "import math\nmath."

    class FakeInterpreter:
        def __init__(self, _, namespaces):
            self.namespaces = namespaces

        def completions(self):
            return [FakeCompletion(c) for c in ["exp", "exp2"]]

    class FakeCompletion:
        def __init__(self, name):
            self.name = name
            self.complete = name
            self.type = "func"
            self.description = "something"
            self.parent = None
            self.full_name = name

    def _get_interpreter(_, namespaces):
        return FakeInterpreter(_, namespaces)

    j

# Generated at 2022-06-14 11:24:16.960709
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    completions = get_interpreter_completions('import re; re.sub(', [{}])
    assert len(completions) == 2
    assert [c.name for c in completions] == ["sub", "subn"]
    if _using_older_jedi(jedi):
        assert [c.complete for c in completions] == ["sub =", "subn ="]
    else:
        assert [c.complete for c in completions] == ["sub(", "subn("]

# Generated at 2022-06-14 11:24:22.591954
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    
    # Test edge cases
    assert len(get_interpreter_completions("", [], None)) == 0, "Fail to handle empty source"
    namespaces = [{"a": 1}, {"a": 2}]
    assert len(get_interpreter_completions("a", namespaces, None)) == 2, "Fail to handle multiple namespaces"
    
    # Test normal cases

# Generated at 2022-06-14 11:24:33.805356
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    namespaces = [{"x": 1, "y": 2}]
    completions = get_interpreter_completions("x", namespaces)
    assert len(completions) == 1
    assert completions[0].name == "x"

    completions = get_interpreter_completions("y", namespaces)
    assert len(completions) == 1
    assert completions[0].name == "y"

    completions = get_interpreter_completions("from math", namespaces)
    assert len(completions) > 1
    assert any(c.complete == "from math import " for c in completions)


# Generated at 2022-06-14 11:25:00.144731
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if jedi.__version__[:5] >= "0.17.":
        ne_namespace = {"name": "__main__", "description": "", "docstring": "", "type": "module"}
        params = [ne_namespace, []]
        completions = get_interpreter_completions("print", params)
        assert completions[0].name == "print"

    else:
        ne_namespace = {"type": "module", "name": "__main__", "docstring": "", "description": ""}
        params = [ne_namespace, []]
        completions = get_interpreter_completions("print", params)
        assert completions[0].name == "print="

    return True



# Generated at 2022-06-14 11:25:10.919595
# Unit test for function get_definitions
def test_get_definitions():
    def check(source, row, column, expected_defs):
        defs = get_definitions(source, row, column, filename="test.py")
        if len(expected_defs) != len(defs):
            raise AssertionError(
                "Wrong number of definitions (expected %s, got %s)"
                % (len(expected_defs), len(defs))
            )

        defs_by_desc = {}
        for def_ in defs:
            defs_by_desc[def_.description] = def_

        for expected_def in expected_defs:
            if expected_def not in defs_by_desc:
                raise AssertionError("Expected definition %s missing" % expected_def)


# Generated at 2022-06-14 11:25:11.631831
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:25:17.872383
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    if _using_older_jedi(jedi):
        assert get_script_completions('import sys\nsys.exit', 'sys.exit', 1, 2)
    else:
        assert get_script_completions('import sys\nsys.exit', 'sys.exit', 1, 2)

# Generated at 2022-06-14 11:25:24.170634
# Unit test for function get_definitions
def test_get_definitions():
    def check(source, line_number, column, should_find):
        found_names = [d.full_name for d in get_definitions(source, line_number, column, None)]
        if should_find:
            assert should_find in found_names
        else:
            assert not found_names

    check("x = 42", 1, 6, "int")
    check("x = [42, 77]", 1, 10, "int")
    check("x = {1:2, 2:4}", 1, 12, "int")
    check("def f(): pass", 1, 18, "f")
    check("def f(): pass\nf()", 2, 2, "f")
    check("x = f", 1, 8, "f")

# Generated at 2022-06-14 11:25:37.872596
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    jedi_version = jedi.__version__
    print("Testing jedi version: " + jedi_version)
    assert jedi_version[:3] in ["0.1", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7"]
    if jedi_version[:3] in ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7"]:
        completions = get_script_completions("import s", 0, 7, None)
    else:
        completions = get_script_completions("import s", 0, 7, None, [])

# Generated at 2022-06-14 11:25:47.282663
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest
    from unittest.mock import patch
    import jedi
    # we have to mock to have older jedi versions
    with patch('jedi.__version__', '0.13.0'):
        completions = get_interpreter_completions('import sys\nsys.', [{'sys': sys}], [sys.path[0]])
        for completion in completions:
            assert completion.type != 'namespace'
    with patch('jedi.__version__', '0.17.0'):
        completions = get_interpreter_completions('import sys\nsys.', [{'sys': sys}], [sys.path[0]])
        for completion in completions:
            assert completion.type != 'namespace'

# Generated at 2022-06-14 11:25:48.981955
# Unit test for function get_script_completions
def test_get_script_completions():
    res = get_script_completions("import os", 0, 0, "test", sys_path=["/usr/bin"])
    res[0].name

# Generated at 2022-06-14 11:25:52.778004
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions(
        "from unittest import TestCase\nTestCase.as",
        [{"TestCase": TestCase}],
        sys_path=["from unittest import TestCase"],
    )
    assert len(completions) > 50
    assert any([c.name == "assert_" and c.type == "function" for c in completions])



# Generated at 2022-06-14 11:25:58.924019
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from _test_utils import get_test_configuration
    from thonny.backend_utils import is_same_path
    from thonny.config import get_runner_python_path
    interpreter_completions = get_interpreter_completions(
        "import pandas as pd\npd.",
        [],
        sys_path=[get_test_configuration().get_interpreter_path()],
    )
    assert is_same_path(
        interpreter_completions[0].parent.py__file__(), get_runner_python_path()
    )



# Generated at 2022-06-14 11:26:32.103950
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.python_shell import PythonShell
    from thonny.shell import RunningShell

    def get_completions(text, namespaces):
        return get_interpreter_completions(
            text, namespaces=namespaces, sys_path=["/home/user/myproject"]
        )

    shell = PythonShell(RunningShell(master=None, config=None))
    shell.namespace = {"a": 3}
    shell.namespace["b"] = 4
    shell.namespace["c"] = 5

    completions = get_completions("a", [shell.namespace])
    assert completions[0].parent == "int"
    assert completions[0].full_name == "int"

    completions = get_completions("b", [shell.namespace])
    assert completions

# Generated at 2022-06-14 11:26:33.016268
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:26:37.691304
# Unit test for function get_definitions
def test_get_definitions():
    # Just test that there are no AttributeErrors or such
    source = "import builtins\nbuiltins.abs(<1>)"
    assert len(get_definitions(source, 2, 10, "test.py")) == 1

# Generated at 2022-06-14 11:26:42.069924
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("import os; os.", 0, 10, "")
    assert len(completions) > 0
    assert "listdir" in [comp["name"] for comp in completions]



# Generated at 2022-06-14 11:26:43.653411
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    # Test jedi >= 0.18
    assert "get_script_completions" in dir(jedi.utils)

    # Test jedi 0.16, 0.17
    assert "get_script_completions" in globals()



# Generated at 2022-06-14 11:26:51.049449
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock
    from parso import parse
    from jedi.parser_utils import get_statement_of_position
    from jedi.evaluate.representation import ModuleContext

    def get_completions_mock(code, pos, parse_module=None, path=None):
        if parse_module is None:
            node = parse(code)
        else:
            node = parse_module
        complete_node = get_statement_of_position(node, pos)
        if complete_node is None:
            return []
        else:
            return [(complete_node.name, complete_node.type)]
        
    prefix = "import math, sys\ndef fun(a): pass\nx = fun\nprint(math"
    pos = len(prefix) - 1
    suffix = ")"


# Generated at 2022-06-14 11:26:59.100011
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.codeview import CodeViewText

    expected_completions = ["code", "complete", "description", "docstring", "full_name", "get_line_code"]
    source = CodeViewText("complete", "\n")
    completions = get_script_completions(source.value, 1, 9, "")
    assert all(completion.complete in expected_completions for completion in completions)



# Generated at 2022-06-14 11:27:12.135020
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:27:22.875436
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import MagicMock
    import jedi
    jedi.Interpreter = MagicMock(
        name="Interpreter", return_value=MagicMock(complete=MagicMock())
    )
    get_interpreter_completions("toto", [{}], sys_path=None)
    jedi.Interpreter.assert_called_once_with("toto", [{}], sys_path=None)
    assert (
        not jedi.Interpreter.return_value.complete.called
    ), "completions should have been returned"
    # Check too that with new versions of jedi, the enclosing function is called
    jedi.Interpreter.return_value.complete.side_effect = AttributeError

# Generated at 2022-06-14 11:27:29.508850
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate.compiled import CompiledObject

    def dict_to_namespace(d):
        return CompiledObject(d)

    results = get_interpreter_completions("import sys\nsys.", [dict_to_namespace({"sys": 1})])
    assert results, results
    assert "path" in [result.name for result in results]
    assert all(result.type == "module" for result in results), results



# Generated at 2022-06-14 11:28:25.964402
# Unit test for function get_definitions
def test_get_definitions():
    from parso.python.tree import Module, Name
    from parso.python.tree import Function, Class
    from parso import parse
    import re
    import types

    # a function
    source = "def foo(): pass\nfoo()"
    tree = Module(parse(source))
    name = Name("foo", (1, 5))
    result = get_definitions(source, row = 1, column = 5, filename = "")
    assert len(result) == 1
    assert isinstance(result[0], Function) and result[0].name.value == "foo"

    # a function call
    source = "def foo(): pass\nfoo()"
    tree = Module(parse(source))
    name = Name("foo", (1, 5))

# Generated at 2022-06-14 11:28:34.117310
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    This test makes sure that the six different jedi versions, that thonny
    supports, all return the same result. The test will be run if you run
    'python3 -m thonny.jediutils'
    """
    import sys
    import os.path

    sys.path.append(os.path.dirname(__file__))
    import thonnycontrib.jedi_completion_backend

    jedi_versions = ["0.13.1", "0.14.0", "0.15.1", "0.16.0", "0.17.1", "0.18.1"]
    for version in jedi_versions:
        sys.path.insert(0, version)
        jedi_old = importlib.import_module("jedi")
        result_old = get_inter

# Generated at 2022-06-14 11:28:43.754816
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script
    import textwrap
    s = "def foo(a):\n    print(a)"
    script = Script(s, 2, 6)
    completions = script.complete()
    assert len(completions) >= 1
    assert completions[0].module_name == ""
    assert completions[0].type == "param"
    assert completions[0].name == "a"
    assert completions[0].complete == "a"
    assert completions[0].description == ""

    s = "def foo(a"
    script = Script(s, 1, 8)
    completions = script.complete()
    assert completions[0].type == "param"
    assert completions[0].name == "a"
    assert completions[0].complete == "a"

# Generated at 2022-06-14 11:28:56.283881
# Unit test for function get_definitions
def test_get_definitions():
    import unittest

    class TestCase(unittest.TestCase):
        def test_get_definitions(self):
            # Tests the functionality of get_definitions.
            self.assertEqual(get_definitions("s = 'jedi'", 0, 0, ""), [])
            self.assertEqual(get_definitions("s = 'jedi'", 1, 0, ""), [])
            self.assertEqual(get_definitions("s = 'jedi'", 0, 4, ""), [])
            self.assertEqual(get_definitions("s = 'jedi'", 1, 5, ""), [])
            self.assertEqual(get_definitions("s = 'jedi'", 0, 1, ""), [])

# Generated at 2022-06-14 11:29:03.256257
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    assert get_interpreter_completions("1 + int(", [], sys_path=[]).count("__init__") > 0
    assert "__init__" in [c.name for c in jedi.Interpreter("1 + int(", []).complete()]
    # TODO: add more tests for other methods


# Generated at 2022-06-14 11:29:07.004288
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if _using_older_jedi(jedi):
        return

    assert len(get_interpreter_completions("abs", [])) > 0
    assert any("int(" in c.name for c in get_interpreter_completions("int.to_bytes", []))

# Generated at 2022-06-14 11:29:20.647951
# Unit test for function get_script_completions
def test_get_script_completions():
    src = "def func(x, y): return x + y\nfunc(1, 3)"

    assert get_script_completions(src, 1, 5, "/home/user/prog.py") == [
        {"name": "func", "type": "function", "description": "func(x,y) -> value"},
        {"name": "func", "type": "function", "description": "func(x,y) -> value"},
    ]
    assert get_script_completions(src, 2, 6, "/home/user/prog.py") == [
        {"name": "func", "type": "function", "description": "func(x,y) -> value"},
    ]



# Generated at 2022-06-14 11:29:33.915287
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("x", 0, 1)

    assert len(completions) == 0

    completions = get_script_completions("x = 42", 0, 3)

    assert len(completions) == 1
    assert completions[0].name == "x"
    assert completions[0].complete == "x = 42"

    completions = get_script_completions("x toto", 0, 3)
    assert len(completions) == 0

    completions = get_script_completions("import sys", 0, 7)
    assert len(completions) == 0
    completions = get_script_completions("import sys", 0, 8)
    assert len(completions) != 0

# Generated at 2022-06-14 11:29:40.879851
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("""
import json
json.dumps
""", 2, 5, "foo.py")
    assert len(completions) > 1
    assert completions[0].name == "dumps"
    assert completions[0].complete == "dumps("
    assert completions[0].parent == "json"


# Generated at 2022-06-14 11:29:45.144401
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.plugins.jedi_backend.utils import get_interpreter_completions

    assert get_interpreter_completions("import os;os.", [])[0].name == "name"

