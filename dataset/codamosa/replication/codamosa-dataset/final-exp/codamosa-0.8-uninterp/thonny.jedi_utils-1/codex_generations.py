

# Generated at 2022-06-14 11:21:38.120650
# Unit test for function get_script_completions
def test_get_script_completions():
    """Tests if all supported versions of Jedi returns the same set of completions."""
    import jedi
    import sys

    assert sys.version_info[0] == 3, "tests only work with python3"

    # All the supported versions of Jedi
    jedi_versions = [
        "0.13.2",
        "0.14.0",
        "0.15.2",
        "0.16.0",
        "0.17.0",
        "0.18.0",
        "0.19.1",
    ]

    # String and position of cursor in line
    code = "import sys; sys.ge"
    column = len(code)
    row = 1
    filename = "test_file.py"

    # Get list of completions for all supported versions
    completions_list = []

# Generated at 2022-06-14 11:21:51.045281
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:21:56.979392
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    print(jedi.__version__)
    source = """
from ai import Ai
from ai import A
"""
    completions = get_script_completions(source, 0, 8, "test.py", sys_path=["path:."])
    for completion in completions:
        print(completion.name)


if __name__ == "__main__":
    test_get_script_completions()

# Generated at 2022-06-14 11:22:01.944751
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny import get_workbench

    get_workbench().set_option("shell.spyder_compat", False)

# Generated at 2022-06-14 11:22:04.051529
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny import get_runner

    runner = get_runner()
    runner.write_cmd(["import sys", "sys."])
    runner.write_cmd(["import stats", "stats."])

# Generated at 2022-06-14 11:22:11.847789
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import mock

    with mock.patch("jedi.api.interpreter.Interpreter.complete") as complete_mock:
        # mock jedi's completion
        comp1 = mock.Mock(name="comp1", complete="complete1", description="desc1")
        comp2 = mock.Mock(name="comp2", complete="complete2", description="desc2")
        complete_mock.return_value = [comp1, comp2]

        completions = get_interpreter_completions("source", [{}])
        assert len(completions) == 2
        assert completions[0].name == "comp1"
        assert completions[1].name == "comp2"
        assert completions[0].complete == "complete1"
        assert completions[1].complete == "complete2"

# Generated at 2022-06-14 11:22:24.655635
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("for i in range(1, 10): pass", 1, 7, "<string>")
    assert len(completions) == 1
    assert completions[0].name == "range"

    completions = get_script_completions("def f(x): pass\nx.", 2, 2, "<string>")
    assert len(completions) == 1
    assert completions[0].name == "x"

    completions = get_script_completions("for i in range(1, 10): pass\nrange.", 2, 7, "<string>")
    assert any(x.name == "range" for x in completions)

    completions = get_script_completions("def f(x): pass\nf(", 2, 4, "<string>")
    assert any

# Generated at 2022-06-14 11:22:29.093739
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    try:
        jedi.Interpreter("", []).completions()
        has_completions = True
    except AttributeError:
        has_completions = False
    assert has_completions == _using_older_jedi(jedi)

# Generated at 2022-06-14 11:22:32.308568
# Unit test for function get_script_completions
def test_get_script_completions():
    result = get_script_completions(
        "import builtins as mod;mod.r", 0, 18, "/home/foo.py"
    )
    assert result[0].name == "range"



# Generated at 2022-06-14 11:22:44.642308
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase, main

    from thonny import get_workbench

    class ThonnyCompletionsTest(TestCase):
        def test_completions(self):
            from jedi import Interpreter

            code = "print('hello')"

            # jedi 0.16.0
            completions = get_interpreter_completions(code, [])
            completions = list(completions)
            self.assertEqual(len(completions), 1)
            self.assertEqual(completions[0].name, "print")
            self.assertEqual(completions[0].complete, "print(")

            # jedi 0.17.0
            completions = get_interpreter_completions(code, [])

# Generated at 2022-06-14 11:23:06.158534
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    from typing import List

    completions = get_interpreter_completions("p", [{"a": jedi.Interpreter("2")}])

    assert isinstance(completions, List)
    assert completions[0].name == "print"
    assert completions[0].complete == "print"



# Generated at 2022-06-14 11:23:07.948077
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:23:18.541917
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.python.tree import Module
    from parso.python import tree
    # from parso.python.parser import Parser
    from parso.python import parse as parso_parse
    import jedi

    # Quick and dirty way to generate a valid namespace to test get_completions
    module_code = "a = 1\na = 2\ndef func(a):\n    a = 3\n"
    tree = parso_parse(module_code)

    # TODO: 2.7-compatible way to generate namespace
    namespace = {}
    # module = Parser().parse(module_code)
    module = Module(tree)
    # module.namespaces = []
    # module.namespaces.append(namespace)
    NamespaceFinder().find_namespaces(module, namespace)

    # module.names

# Generated at 2022-06-14 11:23:29.165025
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api import Script
    from jedi.parser import Parser
    from jedi import settings
    import jedi
    from parso import parse
    
    source = """
import numpy, sys
a = 1
a = 2 + 3
from math import sin, tan"""
    orig_settings = settings.fast_parser
    settings.fast_parser = False
    pos = (3, 8)
    node = parse(source)
    script = Script(source, pos[0], pos[1], "test.py", line_offset=0, column_offset=0)
    parser = Parser(None)
    stmt = get_statement_of_position(node, (pos[0] + 1, pos[1]))
    names = parser.find_assignments(stmt, pos)
    results = []
   

# Generated at 2022-06-14 11:23:34.927569
# Unit test for function get_script_completions
def test_get_script_completions():
    # Spot check
    completions = get_script_completions("sorted(l, ke", 2, 10, "")
    assert len(completions) == 2
    assert completions[0].name == "key="
    assert completions[1].name == "key=None"



# Generated at 2022-06-14 11:23:41.342473
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import re\ncount = re.findall"
    namespaces = [{"count": 42}]

    x = get_interpreter_completions(source, namespaces)
    assert len(x) > 0
    assert x[0].name == "re.findall"
    assert len(x[0].full_name) == 0



# Generated at 2022-06-14 11:23:51.860495
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from . import jedi_utils

    jedi_utils.get_interpreter_completions("import datetime", [])
    jedi_utils.get_interpreter_completions("from datetime import ", [])
    jedi_utils.get_interpreter_completions("from datetime import date", [])
    jedi_utils.get_interpreter_completions("from datetime import date\ndate.is", [])
    jedi_utils.get_interpreter_completions("from datetime import *\ndate.is", [])
    jedi_utils.get_interpreter_completions("from datetime import *\ndate\n", [])

# Generated at 2022-06-14 11:23:56.132822
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("import tek", 1, 7, "dummy.py")
    assert completions[0].name == "tkinter"
    assert completions[0].type in ("import", "module")
   

# Generated at 2022-06-14 11:24:05.000147
# Unit test for function get_script_completions
def test_get_script_completions():
    from test.test_jedi_utils import run_script

    row, column = run_script(
        "def f():\n"
        "    pass\n"
        "\n"
        "f(<|>)",
        globals(),
    )
    assert row == 2 and column == 4

    completions = get_script_completions(
        "def f():\n"
        "    pass\n"
        "\n"
        "f(<|>)",
        row,
        column,
        filename="test.py",
    )

    assert len(completions) == 1 and completions[0].name == "self" and completions[0].type == 'param'



# Generated at 2022-06-14 11:24:17.342413
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    from parso.python.tree import Module
    from parso.python import tree

    def create_interpreter(source, namespaces):
        return jedi.Interpreter(source, namespaces)

    source = "from typing import List\n" "new_list = [1, 2, 3]\n" "new_list."
    position = (2, len(source))  # 2 = line number
    namespaces = []
    interpreter = create_interpreter(source, namespaces)
    completions = interpreter.complete(2, position[1])
    if not completions:
        return

    source = source[:position[1]] + completions[0].name + source[position[1]:]
    module = Module(parse_source(source), source)

# Generated at 2022-06-14 11:24:36.504773
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    if sys.version_info[0] == 2:
        import unittest2 as unittest
    else:
        import unittest
    from unittest.mock import MagicMock

    class TestCase(unittest.TestCase):
        def assert_completions_equal(self, completions, expected_completions):
            self.assertEqual({c.name for c in completions}, set(expected_completions))

        def test_jedi_17(self):
            jedi_mock = MagicMock()
            jedi_mock.__version__ = "0.17"

# Generated at 2022-06-14 11:24:47.891394
# Unit test for function get_definitions
def test_get_definitions():
    from unittest.mock import patch
    from unittest import TestCase

    class TestGetDefinitions(TestCase):
        def test_get_definitions_for_import_statements(self):
            import jedi
            filename = "untitled"
            with open(filename, "w") as f:
                f.write(
                    """
import sys as sy # cursor here
print(sy.version_info)"""
                )
            source = open(filename, "r").read()
            row = 3
            column = 10
            definitions = get_definitions(source, row, column, filename)
            if _using_older_jedi(jedi):
                self.assertEqual(len(definitions), 1)

# Generated at 2022-06-14 11:24:58.121242
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import __file__ as jedi_source
    from os.path import dirname
    from os.path import join

    new_jedi_completions = get_script_completions(
        "import j; j", 11, 8, join(dirname(jedi_source), "__init__.py")
    )

    assert any(
        "JediDebugger" in c.full_name for c in new_jedi_completions
    ), "Could not find new jedi completions, please update test"

    old_jedi_completions = get_script_completions(
        "import j; j", 11, 8, join(dirname(jedi_source), "__init__.py")
    )


# Generated at 2022-06-14 11:25:10.109350
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.environment import get_environment
    from jedi.api.interpreter import Interpreter
    from jedi.evaluate.compiled.context import LazyContext
    env = get_environment()
    interpreter = Interpreter("some_module", [{"x": "123", "y" : "456"}], env)
    
    completions = get_interpreter_completions("", interpreter.namespaces, interpreter.env.get_sys_path())
    assert len(completions) == 2
    assert "x" in [c.name for c in completions]
    assert "y" in [c.name for c in completions]
    
    completions = get_interpreter_completions("x", interpreter.namespaces, interpreter.env.get_sys_path())

# Generated at 2022-06-14 11:25:11.828521
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:25:24.833165
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.jedi_utils import get_interpreter_completions
    
    from unittest.mock import patch
    import jedi
    mock_interpreter = {"a": 1, "b": "2", "c": False}
    with patch('jedi.api.Interpreter') as mock_Interpreter:
        mock_Interpreter.return_value.complete.return_value = [
        jedi.api_classes.Completion('a', 1, "int"),
        jedi.api_classes.Completion('b', 1, "str"),
        jedi.api_classes.Completion('c', 1, "bool")]
        completions = get_interpreter_completions("abc", [mock_interpreter])


# Generated at 2022-06-14 11:25:38.548860
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.parser.python import ParserSyntaxError

    def get_completions(source, row, column):
        from jedi.api.environment import find_virtualenvs, get_system_environment

        system_paths = get_system_environment().get_pythons()
        if not system_paths or not system_paths[0]:
            sys_paths = []
        else:
            sys_paths = find_virtualenvs(system_paths[0].binary)
            sys_paths = [item.path for item in sys_paths]
        return get_script_completions(source, row, column, "", sys_paths)

    def test_completions(source, row, column, names):
        completions = get_completions(source, row, column)
       

# Generated at 2022-06-14 11:25:45.814057
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    jedi.settings.case_insensitive_completion=False
    return_value = get_interpreter_completions("dummy_source", [{'__builtins__': __builtins__}], ['dummy_sys_path'])
    assert len([v for v in return_value if v.name=='object'])==1
    assert len([v for v in return_value if v.name=='abs'])==1
    assert len([v for v in return_value if v.name=='__doc__'])==1


# Generated at 2022-06-14 11:25:47.186024
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:25:58.154187
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.evaluate.python_values import CompiledValue
    from jedi import Script
    
    source = """
    from datetime import datetime
    datetime.
    """
    
    import jedi
    if _using_older_jedi(jedi):
        for class_name in ['date', 'time', 'timedelta']:
            assert any(map(lambda completion: completion.name == class_name, get_script_completions(source, row=3, column=10, filename="test_get_script_completions.py")))
    else:
        script = Script(source=source, path="test_get_script_completions.py")
        completions = script.complete()

# Generated at 2022-06-14 11:26:34.267233
# Unit test for function get_definitions
def test_get_definitions():
    """
    Tests if we can reliably find the definition of a variable
    """
    # pylint: disable=undefined-variable
    script = "import _io\nfrom typing import IO\nx: IO = _io.StringIO()"
    jedi_defs = get_definitions(script, 3, 5, "script.py")
    assert len(jedi_defs) == 1
    assert jedi_defs[0].module_name == "_io"
    assert jedi_defs[0].type == "type"
    assert jedi_defs[0].full_name == "StringIO"
    assert jedi_defs[0].name == "StringIO"

# Generated at 2022-06-14 11:26:37.921843
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Test that an error is raised if called with no arguments
    import jedi

    source = "import re\nre.\n"
    n = 1
    column = 4
    namespaces = [{"re": re}]

    if _using_older_jedi(jedi):
        with pytest.raises(TypeError):
            get_interpreter_completions(source, n, column, namespaces)
    else:
        completions = get_interpreter_completions(source, n, column, namespaces)

# Generated at 2022-06-14 11:26:47.718650
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions("import sys\nsys.", [], sys_path=["/tmp"])
    assert completions
    assert "path" in completions[0].name
    assert "path" in completions[0].complete

    completions = get_interpreter_completions("import sys", [], sys_path=["/tmp"])
    assert completions
    assert "path" in completions[0].name
    assert "path" in completions[0].complete

    completions = get_interpreter_completions("import sys", [{"sys": "test"}], sys_path=["/tmp"])
    assert completions
    assert "platform" in completions[0].name
    assert "platform" in completions[0].complete

# Generated at 2022-06-14 11:27:00.837014
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script

    import jedi
    from jedi.api.classes import Completion

    # in jedi 0.18, module name is no longer in completion.complete
    actual_list = get_script_completions("import o", 0, 7, "")
    assert isinstance(actual_list[-1], ThonnyCompletion)

    if _using_older_jedi(jedi):
        expected_list = Script("import o", 0, 7, "").completions()
        assert len(actual_list) == len(expected_list)
        for i in range(len(actual_list)):
            if not isinstance(expected_list[i], Completion):
                assert not isinstance(actual_list[i], Completion)
            else:
                assert actual_list[i].name == expected_list

# Generated at 2022-06-14 11:27:13.507020
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.evaluate.cache import NO_DOCSTRINGS

    script_completions = get_script_completions('"".f', 1, 3, "Dummy")
    assert len(script_completions) == 0

    script_completions = get_script_completions('"".foobar', 1, 3, "Dummy")
    assert len(script_completions) == 0

    script_completions = get_script_completions('"".foobar', 1, 9, "Dummy")
    assert len(script_completions) == 0

    script_completions = get_script_completions('"".foo', 1, 5, "Dummy")
    assert len(script_completions) == 12
    assert script_completions[0].name == "format"

# Generated at 2022-06-14 11:27:18.323660
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = 'import sys\n' + \
        'sys.stdout.write("hello")\n'
    namespaces = []
    result = get_interpreter_completions(source, namespaces)
    assert result[0]['name'] == 'sys'

# Generated at 2022-06-14 11:27:26.409464
# Unit test for function get_script_completions
def test_get_script_completions():
    compls = get_script_completions("""def my_fun():
    b = []
    b.ap""", 3, 7, "")
    assert compls == [
        ThonnyCompletion(
            name="append",
            complete="append",
            type="function",
            description="append(${1:object}, /)",
            parent="list",
            full_name="list.append",
        )
    ]



# Generated at 2022-06-14 11:27:35.003884
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions("print(", [], [])[0].name == "print"
    assert get_interpreter_completions("x = 0", [], [])[0].name == "x"

    # test namespaces
    namespace = {"x": 6}
    assert get_interpreter_completions("x", [namespace], [])[0].name == "x"
    assert get_interpreter_completions("x", [namespace], [])[0].description == "int"
    assert get_interpreter_completions("y", [namespace], [])[0].name == "y"
    assert get_interpreter_completions("y", [namespace], [])[0].description == "Name"
    assert get_interpreter_completions

# Generated at 2022-06-14 11:27:48.698071
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    # The first two tests test the behavior of jedi 0.16 and newer,
    # The last two tests test the behavior of jedi before 0.16.
    completions = get_script_completions("import sys; sys.path[0]", 0, 23, "dummy.py")
    # The first element should be the only one with name "path".
    assert completions[0].name == "path"
    completions = get_script_completions("import sys; sys.path", 0, 17, "dummy.py")
    assert completions[0].name == "path"
    completions = get_script_completions("import sys; sys.path[0]", 0, 23, "dummy.py")
    completions = _tweak_completions(completions)

# Generated at 2022-06-14 11:27:55.647346
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest import mock

    source = "import os\n" "os."
    row = 2
    column = 5
    filename = "dummy_test.py"

    def mock_result(code, line, column, path):
        # NB! In jedi 0.18, complete() is called with kwargs
        # see https://github.com/davidhalter/jedi/blob/master/jedi/api/helpers.py#L49
        if _using_older_jedi(jedi):
            assert line == row
            assert column == column
        else:
            assert line == row - 1
            assert column == column - 1
            assert path == filename

        return [mock.Mock(**completion) for completion in [{"name": "getlogin", "complete": "getlogin()"}]]



# Generated at 2022-06-14 11:28:59.863154
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    def get_completions(source, namespaces):
        return get_interpreter_completions(source, namespaces)

    def verify_completions(source, namespaces, expected):
        completions = get_completions(source, namespaces)
        actual = [c.name for c in completions]
        if actual != expected:
            print("Expected completions for", source, ":", expected)
            print("Actual completions for", source, ":", actual)
        assert actual == expected

    verify_completions('"".split()[0].u', [], ["upper"])
    verify_completions('"".split()[0].u', [{"__builtins__": __builtins__}], ["upper"])

    verify_completions("", [], ["None"])
    verify

# Generated at 2022-06-14 11:29:11.920341
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():

    source = "list(map(lambda x: x + 1, [1, 2, 3]))\n"

    completions = get_interpreter_completions(
        code=source, namespaces=[{"x": 3}, {"x": 4}]
    )


# Generated at 2022-06-14 11:29:27.144145
# Unit test for function get_definitions
def test_get_definitions():
    source = 'import json\nd'
    filename = '/tmp/test.py'
    # when d = {}
    completions = get_definitions(source, 2, 3, filename)
    assert len(completions) == 1
    assert completions[0].type == 'class'
    assert completions[0].description == 'type dict'
    assert completions[0].full_name == 'dict'
    # when d = json.loads()
    source = 'import json\nd = json.loads("{}")'
    completions = get_definitions(source, 2, 3, filename)
    assert len(completions) == 1
    assert completions[0].type == 'module'
    assert completions[0].description == 'json'
    # when d = other

# Generated at 2022-06-14 11:29:32.795574
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    code = """
    import sys
    import datetime as dt
    dt.tim
    """

    completions = get_interpreter_completions(code, [])

    assert len(completions) == 2
    assert completions[0].name == "date"
    assert completions[1].name == "timedelta"



# Generated at 2022-06-14 11:29:38.508411
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from IPython import get_ipython
    from jedi import Interpreter

    ipython = get_ipython()
    namespaces = ipython.execution_count
    # can't use Interpreter.eval, because it doesn't use current kernel namespace
    # so get namespaces from ipython
    # see also https://docs.python.org/3/library/jedi.html#jedi.Interpreter
    interpreter = Interpreter("", namespaces=namespaces)
    completions = interpreter.completions()
    # filter to be the same as jedi.Script.complete
    completions = [c for c in completions if c.type in ("statement", "import", "keyword")]

# Generated at 2022-06-14 11:29:44.663042
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.jedi_helper import test_resource_path
    from thonny import get_completions


# Generated at 2022-06-14 11:29:48.706043
# Unit test for function get_definitions
def test_get_definitions():
    assert get_definitions("os.path.exists", 0, 0, "test.py")
    assert get_definitions("os.path.exists", 0, 0, "test.py") == 1
    assert get_definitions("Time", 0, 0, "test.py") == 1
    assert get_definitions("Time", 0, 0, "test.py") == 1
    return


# Generated at 2022-06-14 11:29:49.364295
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

# Generated at 2022-06-14 11:29:50.686960
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import sys


# Generated at 2022-06-14 11:30:04.301515
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.evaluate.compiled import CompiledObject
    from jedi.evaluate.base_context import ContextSet
    from jedi.evaluate import analysis

    import types
    
    class MockContext(analysis.Context):
        def __init__(self, name):
            super().__init__(name, None)
            self.obj = name

    class MockModule(types.ModuleType):
        def __init__(self, name):
            self.__name__ = name
            
    class MockName:
        def __init__(self, module, name, parent):
            self.module = module
            self.name = name
            self.parent = parent

    def get_context(context: MockContext):
        context_set = ContextSet.from_sets(context)
        return context_set

