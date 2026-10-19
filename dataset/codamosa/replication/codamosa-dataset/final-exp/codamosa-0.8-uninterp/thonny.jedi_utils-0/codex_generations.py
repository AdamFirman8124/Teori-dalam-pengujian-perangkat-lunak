

# Generated at 2022-06-14 11:21:38.091934
# Unit test for function get_script_completions
def test_get_script_completions():
    def _check(expected, input, row, column, filename, sys_path=None):
        assert expected == get_script_completions(input, row, column, filename, sys_path)

    _check(["s", "sys"], "s=2; s", 0, 1, "<string>")
    _check(["s", "sys"], "s=2; s", 0, 2, "<string>")
    _check([], "s=2; s", 0, 3, "<string>")
    _check([], "s=2; s", 1, 0, "<string>")


del test_get_script_completions

# Generated at 2022-06-14 11:21:43.407885
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import __version__
    if __version__[:4] in ["0.13", "0.14", "0.15", "0.16", "0.17"]:
        import sys
        sys.path.insert(0, "/my/dir")
        completions = get_script_completions("import os; os.path.jo", 0, 23, "x.py")
        assert len(completions) > 0
        assert completions[0].name == "join"
        assert completions[0].complete == "join("
        assert completions[0].description == "join(path, *paths) -> str\n"
        assert completions[0].parent == "<class 'os.PathLike'>"
        assert completions[0].full_name == "os.path.join"

# Generated at 2022-06-14 11:21:53.835437
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock, patch
    from jedi import Interpreter, Script, Jedi
    from jedi._compatibility import unicode

    old_jedi_version = True

    def _fake_interpreter(source, namespaces=None, sys_path=None):
        if sys_path:
            raise AssertionError("Can't send sys_path to Interpreter")
        return Interpreter(source, namespaces)

    def _fake_script(source, row, column, filename, sys_path=None):
        if sys_path:
            raise AssertionError("Can't send sys_path to Script")

        script = Script(source, row, column, filename)
        _fake_jedi.completions = script.completions
        return script


# Generated at 2022-06-14 11:22:08.219300
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert len(get_interpreter_completions("open(", [{"name":"open", "type":"function"}])) == 1
    assert len(get_interpreter_completions("open(", None)) == 1

    assert len(get_interpreter_completions("sys.path", [{"name":"sys", "type":"module"}])) == 1
    assert len(get_interpreter_completions("sys.path", None)) == 1

    assert len(get_interpreter_completions("open(", [{"name":"open", "type":"class"}])) == 0
    assert len(get_interpreter_completions("sys.path", [{"name":"sys", "type":"function"}])) == 0

# Generated at 2022-06-14 11:22:12.099301
# Unit test for function get_definitions
def test_get_definitions():
    import unittest


# Generated at 2022-06-14 11:22:24.846032
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate.__init__ import Interpreter
    import jedi
    if _using_older_jedi(jedi):
        print("Jedi version too old. Skipping.")
        return
    from jedi.evaluate.__init__ import InterpreterState
    from jedi.evaluate.__init__ import CompiledObject
    import parso

    src = """import datetime
print(datetime.__dict__.keys())
print(datetime.datetime.__dict__.keys())
"""
    tree = parso.parse(src)
    namespace = {}
    interpreter = Interpreter(tree, [namespace])
    result = interpreter.eval_element(tree)
    # print(result)
    #
    print(namespace["__builtins__"]["__dict__"].keys())
    #


# Generated at 2022-06-14 11:22:35.169327
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    from thonny.jedi_utils import get_script_completions
    import thonny

    script = 'import math\n\rmath.'

    version0_15 = '0.15.2'
    version0_16 = '0.16.0'
    version0_17 = '0.17.2'

    def get_completions_for_version(version):
        thonny.jedi_utils._jedi_version = version
        return get_script_completions(script, 2, 6, '')

    assert get_completions_for_version(version0_15)[0].name == 'acos'
    assert get_completions_for_version(version0_16)[0].name == 'acos'
    assert get_completions_for_version

# Generated at 2022-06-14 11:22:47.633341
# Unit test for function get_script_completions
def test_get_script_completions():
    # Tests with valid sys_path. Should not raise exception.
    source = "import sys; sys.fob"
    get_script_completions(source, 1, len(source), "test.py", sys_path=["/"])
    # Tests with invalid sys_path. Should not raise exception.
    get_script_completions(source, 1, len(source), "test.py", sys_path=["/non/existing/path"])
    # Tests with no sys_path. Should not raise exception.
    get_script_completions(source, 1, len(source), "test.py")
    # Tests with source None. Should not raise exception.
    get_script_completions(None, 1, len(source), "test.py", sys_path=["/"])

# Generated at 2022-06-14 11:22:56.862132
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonnycontrib.jedi_utils import get_interpreter_completions
    import jedi
    from pprint import pprint as pp

    # namespaces is a list of dict objects for the test.
    # the dict object is a namespace dictionary
    
    namespaces = [{}] # empty namespace
    completions = get_interpreter_completions('print("Hello, world!")', namespaces)
    assert "print" in [c["name"] for c in completions], "print is missing!"

    namespaces = [{'a': 1, 'b': 2}]
    completions = get_interpreter_completions('print(a+', namespaces)
    assert "a" in [c["name"] for c in completions], "a is missing!"

# Generated at 2022-06-14 11:23:01.755658
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions("", [{"x": "5"}])[0]["name"] == "x"
    assert get_interpreter_completions("x", [{"x": "5"}])[0]["name"] == "x"

# Generated at 2022-06-14 11:23:25.929383
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from pathlib import Path as pathlib_Path
    from importlib import import_module as importlib_import_module

    def create_namespace(dic, parent=None):
        res = {}
        for key, val in dic.items():
            if key.endswith("__builtins__"):
                res[key] = {}
            else:
                res[key] = val
        return res

    # Create namespaces from the modules in sys.modules
    import sys as sys
    namespaces = []
    for key in sys.modules:
        if "." not in key:
            namespace = create_namespace(sys.modules[key].__dict__)
            namespace["__name__"] = key

# Generated at 2022-06-14 11:23:33.017081
# Unit test for function get_script_completions
def test_get_script_completions():
    results = get_script_completions("import string; string.", 1, 16, "<string>")
    assert len(results) >= 10
    assert results[0].name == "ascii_letters"

    results = get_script_completions("string.", 1, 7, "<string>")
    assert len(results) >= 10
    assert results[0].name == "ascii_letters"

    results = get_script_completions("string.ascii_", 1, 18, "<string>")
    assert len(results) >= 1
    assert results[0].name == "ascii_letters"

    results = get_script_completions("from string import ascii_", 1, 29, "<string>")
    assert len(results) >= 1

# Generated at 2022-06-14 11:23:34.379942
# Unit test for function get_definitions
def test_get_definitions():
    import jedi

# Generated at 2022-06-14 11:23:45.638423
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api import get_script_completions
    from jedi.parser_utils import get_cached_code

    source = '''
            class Foo:
              def __init__(self, x, y='default'):
                self._x = x
                self._y = y
                
            foo = Foo()
            x = foo.x'''
    completions = get_script_completions(source, 5, 9, filename='<source>')
    assert completions
    assert not any(c.complete == '_x' for c in completions)

    # Checking that completions are cached
    # This should not create a new ParseTree
    assert len(get_cached_code()) == 1
    completions = get_script_completions(source, 5, 9, filename='<source>')


# Generated at 2022-06-14 11:23:53.799197
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    print(_using_older_jedi(jedi))
    source = '''
    import sys
    with open("t.txt", "w") as f:
        f.write("hello")
    '''
    result = get_script_completions(source, 2, 9, "test.py")
    assert result[0].name == "sys"
    assert result[1].name == "open"


# Generated at 2022-06-14 11:24:02.773007
# Unit test for function get_script_completions
def test_get_script_completions():
    source = "import os\n"
    source += "i = os.path.join('a', 'b')\n"
    source += "i."

    row = 2; column = 10
    completions = get_script_completions(source, row, column, "test.py")

    assert len(completions) > 0
    for completion in completions:
        print(completion.name)
        assert completion.complete == completion.name
        assert len(completion.name) > 0
        assert completion.type == "instance"
        assert len(completion.description) > 0



# Generated at 2022-06-14 11:24:06.607164
# Unit test for function get_script_completions
def test_get_script_completions():
    from parso.python import tree

    def parse(source):
        return tree.parse(source, error_recovery=True)


# Generated at 2022-06-14 11:24:11.846688
# Unit test for function get_definitions
def test_get_definitions():
    a = get_definitions("import os.path\nfrom os import ", 2, 21, "<string>")
    assert a[0].module_name == "os.path"
    assert a[0].module_path.endswith("os/path.py")
    assert len(a) == 1

# Generated at 2022-06-14 11:24:20.326180
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Run test if the tested function exists
    if get_interpreter_completions.__module__ == "thonny.jediutils":
        # Check for completions of math module
        completions = get_interpreter_completions("import math", [{}])

        # NB! Result depends on interpreter used
        # 3.2-3.4 = log
        # 3.5 = log1p
        # 3.6+ = log10, log1p
        assert "log" in [c.name for c in completions] or "log10" in [
            c.name for c in completions
        ], completions

        # Check for completions of builtin module
        completions = get_interpreter_completions("import builtins", [{}])

# Generated at 2022-06-14 11:24:28.441917
# Unit test for function get_definitions
def test_get_definitions():
    import os

    # we just test that we do not get errors
    # TODO: jedi does not provide error message in such cases
    for i in range(1, 6):
        path = os.path.join(os.path.dirname(__file__), "def_error_%d.py" % i)
        with open(path) as fp:
            source = fp.read()
        get_definitions(source, 5, 9, path)



# Generated at 2022-06-14 11:24:49.859252
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import datetime; datetime.da"
    namespaces = [{"datetime": datetime}]
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) == 158
    assert "datetime.datetime" in (c.name for c in completions)

# Generated at 2022-06-14 11:24:59.045514
# Unit test for function get_definitions
def test_get_definitions():
    source = 'import sys\nprint(sys.path)'
    assert len(get_definitions(source, 1, 8, 'test.py')) == 1
    assert len(get_definitions(source, 1, 5, 'test.py')) == 1
    assert len(get_definitions(source, 1, 5, 'test.py')) == 1
    assert len(get_definitions(source, 0, 5, 'test.py')) == 1
    assert len(get_definitions(source, 1, 5, 'test.py')) == 1
    assert len(get_definitions(source, 1, 5, 'test.py')) == 1
    assert len(get_definitions(source, 1, 5, 'test.py')) == 1

# Generated at 2022-06-14 11:25:06.836490
# Unit test for function get_definitions
def test_get_definitions():
    import unittest
    import jedi.api

    class TestGetDefinitions(unittest.TestCase):
        def test_method_name(self):
            defs = get_definitions("class X:\n    def foo(self): pass\nX.", 3, 8, "")
            self.assertEqual(1, len(defs))
            self.assertIsInstance(defs[0], jedi.api.Class)



# Generated at 2022-06-14 11:25:20.672070
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    def _check_completions(completions):
        completions = [c.name for c in completions]
        assert "str" in completions
        assert "builtins" in completions
        assert "sys.path" in completions
        assert "__main__" in completions
        assert "valid_namespace_attribute" in completions

    namespaces = [
        {
            "x": "valid_namespace_attribute"
        },
        {}
    ]
    completions = get_interpreter_completions("str + builtins.str", namespaces)
    _check_completions(completions)
    _check_completions(get_interpreter_completions("str + builtins.str", namespaces, sys_path=["/tmp"]))

# Generated at 2022-06-14 11:25:28.979682
# Unit test for function get_script_completions
def test_get_script_completions():
    """
    This function tests the get_script_completions function.
    """
    # make sure you have a file in your home directory "test.py" with the following contents
    # def add(a,b):
    #     return a + b
    #
    # def subtract(a,b):
    #     return a - b
    #
    # def multiply(a,b):
    #     return a * b
    #
    # def divide(a,b):
    #     return a / b

    completions = get_script_completions(filename="test.py", source="add(1,2)", column=8, row=0)

# Generated at 2022-06-14 11:25:34.948055
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if _using_older_jedi(jedi):
        pass
    else:
        # Completion in jedi 0.17 are much more accurate
        # https://github.com/davidhalter/jedi/issues/1752
        pass

# Generated at 2022-06-14 11:25:38.315026
# Unit test for function get_definitions
def test_get_definitions():
    print ([d.module_path for d in get_definitions("import re", 0, 1, "")])
    print ([d.module_path for d in get_definitions("def foo():\n    pass\n\nfoo", 2, 5, "")])


# Generated at 2022-06-14 11:25:47.630079
# Unit test for function get_script_completions
def test_get_script_completions():
    from parso.python.tree import Module
    

# Generated at 2022-06-14 11:25:58.404383
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    def test_func(x, y):
        print()

    namespaces = [
        {
            "a": [1, 2, 3],
            "f": [test_func],
            "m": [test_func],
            "g": [1, 2, 3],
            "x": {
                "a": [1, 2, 3],
                "f": [test_func],
                "m": [test_func],
                "g": [1, 2, 3],
            },
        }
    ]

    comps = get_interpreter_completions("a", namespaces)
    assert len(comps) == 2
    assert comps[0].name == "a"
    assert comps[1].name == "array"

    comps = get_interpreter_com

# Generated at 2022-06-14 11:26:05.214976
# Unit test for function get_script_completions
def test_get_script_completions():
    result = get_script_completions("ab.", 0, 3, "")
    assert len(result) == 1 and result[0].name == "abs"

    result = get_script_completions("abs.", 0, 4, "")
    assert len(result) > 20
    assert "abs(x)" in [c.complete for c in result]

# Generated at 2022-06-14 11:26:35.562301
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions(
        "list[0]", 0, 7, "test.py"
    )[0].complete == "len()"  # list has 'len' method

# Generated at 2022-06-14 11:26:47.091163
# Unit test for function get_definitions
def test_get_definitions():
    import unittest.mock as mock

    import jedi

    fake_def = mock.MagicMock()

    # Version <= 0.13
    fake_def.lines = [0]
    fake_def.columns = [0]
    fake_def.module_path = "test_module.py"
    fake_def.type = "module"

    result = [fake_def]

    with mock.patch("thonny.jedihacks.get_definitions") as mock_get_definitions:
        mock_get_definitions.return_value = result

        assert get_definitions("", 0, 0, "") == result

    # Version >= 0.14
    fake_def.module_path = "test_module.py"
    fake_def.line = 0
    fake_def.column = 0



# Generated at 2022-06-14 11:27:00.309403
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.environment import InterpreterEnvironment
    from jedi.api.classes import Interpreter
    from jedi import Script
    from jedi._compatibility import unicode
    import jedi
    
    script = Script('x = [1, 2, 3]\nx.app')
    completions = script.completions()
    assert unicode(completions[0].name) == 'append'
    # imports
    script = Script('import sys\nsys.pa')
    completions = script.completions()
    assert unicode(completions[0].name) == 'path'
    # code completions
    script = Interpreter('import sys', [dict()])
    completions = script.completions()
    assert unicode(completions[0].name) == 'sys'


# Generated at 2022-06-14 11:27:14.754611
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    print(get_interpreter_completions("import pylab as py", [], None))
    completions = get_interpreter_completions(
        """import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5], [1,2,3,4,5])
plt.""",
        #         'plt.plot([1,2,3,4,5], [1,2,3,4,5])'
        #         'plt.[<cursor>]'
        [],
        None,
    )
    for c in completions:
        print(c.name, c.type)

# Generated at 2022-06-14 11:27:20.983284
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:27:31.825366
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate.context import get_module_context
    from jedi.evaluate.cache import evaluator_func_cache
    from jedi.evaluate import compiled
    dummy_module = compiled.builtin
    dummy_module.path = None
    dummy_module.doc = None
    dummy_module.parent_context = None
    dummy_module.code = None
    dummy_module.is_compiled = True
    dummy_module.used_names = None

    dummy_module_context = get_module_context(dummy_module)
    dummy_function = evaluator_func_cache[dummy_module_context.string_names['len']]
    get_interpreter_completions(source='', namespaces=[[dummy_function, dummy_module]])

# Generated at 2022-06-14 11:27:37.774419
# Unit test for function get_definitions
def test_get_definitions():
    def check(source, row, column, expected):
        definitions = get_definitions(source, row, column, "")
        if len(definitions) > 0:
            definiton = definitions[0]
            result = definiton.module_path
        else:
            result = None

        if expected != result:
            print("%d, %d: %s != %s" % (row, column, str(result), str(expected)))


# Generated at 2022-06-14 11:27:38.566184
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:27:50.874618
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    test_get_interpreter_completions - Unit test for function get_interpreter_completions

    Author: mouradmourafiq@gmail.com
    Date: 18.12.2017
    """

# Generated at 2022-06-14 11:28:01.078137
# Unit test for function get_definitions
def test_get_definitions():
    source = """def something(a, b):
    a + b

something(1, 2)
"""
    defs = get_definitions(source, 3, 6, filename="")
    assert len(defs) == 1
    assert defs[0].parent().type in ("funcdef", "async_funcdef")
    assert defs[0].type == "Name"
    assert defs[0].name == "something"
    assert defs[0].full_name == "something"
    assert getattr(defs[0], "description", None) is None

# Generated at 2022-06-14 11:28:40.950573
# Unit test for function get_script_completions
def test_get_script_completions():
    # check that only function definitions are returned
    source = 'def my_function():\n    pass\nmy_func'
    completions = get_script_completions(source, 2, 0, "")
    assert [c.name for c in completions] == ["my_function"]



# Generated at 2022-06-14 11:28:50.107982
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script
    from jedi import Interpreter
    from jedi import __version__

    # Path to example file
    path = r"../../../../../tests/jedi_test/student.py"

    # Read data from file
    with open(path,'r') as file:
        source = file.read()

    # Example completions

# Generated at 2022-06-14 11:28:56.479566
# Unit test for function get_definitions
def test_get_definitions():
    from _thonny.codeview import get_definitions
    import parso
    from parso.python.tree import Leaf

    s = """def f(x,y):
            if x == 5:
                pass
        g = 8
        f"""

    root = parso.parse(s)
    if isinstance(root.children[0], Leaf):
        root = root.children[0]
    if isinstance(root.children[0], Leaf):
        root = root.children[0]

    defs = get_definitions(s, root.start_pos[0], root.start_pos[1]+3, 'test2.py')
    assert len(defs) == 1


# Generated at 2022-06-14 11:29:01.366633
# Unit test for function get_script_completions
def test_get_script_completions():
    assert len(get_script_completions("import sys; sys.", 0, 10, "")) > 10
    assert len(get_script_completions("from os import path; path.", 0, 21, "")) > 10



# Generated at 2022-06-14 11:29:02.722711
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    import jedi
    from jedi import jedi as jedi2


# Generated at 2022-06-14 11:29:16.954529
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Test with empty source
    completions = get_interpreter_completions("", [])
    assert len(completions) == 0

    # Test with empty namespaces
    completions = get_interpreter_completions("im", [])
    assert len(completions) == 0

    # Test with function
    completions = get_interpreter_completions("im", [{"imp": lambda: 0}])
    assert len(completions) == 1
    assert completions[0].complete == "imp("

    # Test with class
    completions = get_interpreter_completions("im", [{"imp": type("", (), {})}])
    assert len(completions) == 2
    assert "imp(" in [c.complete for c in completions]

# Generated at 2022-06-14 11:29:32.972297
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock

    class Script:
        def __init__(self, completions: List[Dict]):
            self.completions = Mock()
            self.completions.return_value = completions

    class Interpreter:
        def __init__(self, completions: List[Dict]):
            self.completions = Mock()
            self.completions.return_value = completions

    jedi_mock = Mock()
    jedi_mock.Script = Script
    jedi_mock.Interpreter = Interpreter

    def run_test(jedi, expected):
        completions = get_script_completions("", 1, 1, "", [])
        assert len(completions) == 1
        assert completions[0].name == expected



# Generated at 2022-06-14 11:29:38.552889
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import os.path
    import tempfile

    test_dir = os.path.dirname(__file__)
    sys_path = [
        os.path.join(test_dir, "jedi_sys_path1"),
        os.path.join(test_dir, "jedi_sys_path2"),
    ]
    parser = parse_source("from math import sin, cos ; sin(cos(3))")
    source = parser.get_code()

    completions = get_interpreter_completions(
        source, [{"sin": 0.5}, {"cos": 0.1, "degrees": 1}, {"pi": 3.14}], sys_path
    )

    assert len(completions) == 2
    assert "sin=" and "cos=" in [c.complete for c in completions]

   

# Generated at 2022-06-14 11:29:44.284235
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    >>> from thonny.jedi_utils import get_interpreter_completions
    >>> get_interpreter_completions("[i for i in range(10)]\ni.", namespaces=[{}])[0].complete
    'index'
    """



# Generated at 2022-06-14 11:29:45.830590
# Unit test for function get_definitions

# Generated at 2022-06-14 11:30:22.829524
# Unit test for function get_definitions

# Generated at 2022-06-14 11:30:33.757097
# Unit test for function get_definitions
def test_get_definitions():
    import sys, os
    file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend/simple_jedi.py")
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = ''.join([l[:-1] for l in lines[:len(lines) - 1]])

    defs = get_definitions(lines, len(lines.split('\n')) - 2, 0, file)
    assert len(defs) == 1
    assert defs[0].module_name == os.path.basename(file)

# Generated at 2022-06-14 11:30:41.372584
# Unit test for function get_script_completions
def test_get_script_completions():
    from _pytest.jedi import get_completion
    from thonny.plugins.micropython.backend import JEDI_BACKEND

    # version 0.16

# Generated at 2022-06-14 11:30:53.840596
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase
    import jedi
    from thonny.python_shell import get_interpreter_completions

    class Test(TestCase):
        def test_path_has_no_completion(self):
            self.assertEqual(
                get_interpreter_completions(
                    'import sys',
                    [{"namespace": sys.modules}],
                    sys_path=[
                        "/Library/Frameworks/Python.framework/Versions/3.7/bin",
                        "/Users/XXXXX/.pyenv/shims",
                    ],
                ),
                [],
            )


# Generated at 2022-06-14 11:31:00.042490
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny import jediutils

    import jedi

    source = 'import sys'
    source += '\nsys.stdout.write("Hello world!")'
    source += '\nsys.stderr.write("Error")'

    def check_completion(completions, completion_name):
        for completion in completions:
            if completion_name in completion.name:
                return True
        return False

    completions = jediutils.get_interpreter_completions(source, [])
    # Check that completion 'sys' is found
    assert check_completion(completions, 'sys'), 'Downgrade to old jedi version'

# Generated at 2022-06-14 11:31:10.546939
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    namespaces = [
        {"os": {"path": "module", "PathLike": "type"}}
    ]
    source = "import os; os.path."

# Generated at 2022-06-14 11:31:22.640839
# Unit test for function get_definitions
def test_get_definitions():
    import jedi
    test_path1 = "test.py"