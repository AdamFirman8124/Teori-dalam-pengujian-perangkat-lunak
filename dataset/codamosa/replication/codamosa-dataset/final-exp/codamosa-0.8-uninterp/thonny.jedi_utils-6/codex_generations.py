

# Generated at 2022-06-14 11:21:38.091825
# Unit test for function get_definitions
def test_get_definitions():
    class JediDefinition:
        def __init__(self, description):
            self._description = description

        def get_line_code(self):
            return self._description

    def_1 = JediDefinition("def f(a,b): return a+b")
    def_2 = JediDefinition("class A: a=0")

    definitions = [
        def_1,
        def_2
    ]

    assert get_definitions("from math import *; f(0,0)", 1, 7, "") == definitions
    assert get_definitions("from math import *; f(0,0)", 0, 1, "") == []
    assert get_definitions("from math import *; f(0,0)", 1, 0, "") == definitions

# Generated at 2022-06-14 11:21:47.803478
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api.project import Project as JediProject, get_system_environment
    from jedi.api.environment import InterpreterEnvironment
    from jedi.api import Script
    from thonny.misc import running_on_mac_os

    # Test using older jedi
    versions = [
        "0.13.2",
        "0.14.1",
        "0.15.1",
        "0.16.0",
        "0.17.2",
        "0.18.1",
        "0.19.0",
        "0.20.0",
        "0.21.1",
        "0.22.0",
        "0.23.2",
    ]

    for version in versions:
        run_test_with(version)



# Generated at 2022-06-14 11:21:52.980460
# Unit test for function get_definitions

# Generated at 2022-06-14 11:22:04.754510
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api import Interpreter
    import jedi

    source = "a = 'abracadabra'"
    namespaces = [Interpreter(source, []).locals]
    if _using_older_jedi(jedi):
        try:
            completions = get_interpreter_completions(source, namespaces, sys_path=["/"])
        except Exception as e:
            completions = get_interpreter_completions(source, namespaces)
    else:
        completions = get_interpreter_completions(source, namespaces)
    assert completions[0].name == "a"
    assert completions[0].complete == "a"


# Generated at 2022-06-14 11:22:09.629803
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import get_runner
    from thonny.languages import tr

    def get_completions(code):
        return get_script_completions(code, len(code.splitlines()), len(code.splitlines()[-1]), "/my/test.py")


# Generated at 2022-06-14 11:22:23.243300
# Unit test for function get_definitions
def test_get_definitions():
    import jedi
    #definitions = get_definitions("import re\nre.compile(r'abc')", 2, 12, "test.py")
    #definitions = get_definitions("import re, sys\nre.compile(r'abc')", 2, 12, "test.py")
    #definitions = get_definitions("import tkinter\ntkinter.Frame()", 2, 12, "test.py")
    definitions = get_definitions("import this", 2, 12, "test.py")

    for d in definitions:
        print(d.type)
        print(d.name)
        print(d.full_name)
        print(d.docstring())
        print(d.is_stub())
        print(d.line)



# Generated at 2022-06-14 11:22:34.257540
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase

    # Using older versions
    jedi.__version__ = "0.17.0"

    class MyTestCase(TestCase):
        def test_complete(self):
            source = "a = 2\n"
            namespaces = [{"a": 3}]
            completions = get_interpreter_completions(source, namespaces)
            self.assertListEqual(
                [c.name for c in completions], ["abs", "all", "any", "ascii", "bin", "bool"]
            )
            self.assertListEqual(
                [c.type for c in completions],
                ["function", "function", "function", "function", "function", "type"],
            )

    MyTestCase().test_complete()

    # Using new versions
    j

# Generated at 2022-06-14 11:22:41.194388
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    namespaces = [{"a": 1}]

    assert len(get_interpreter_completions(source=None, namespaces=namespaces)) > 0
    assert len(get_interpreter_completions(source="a", namespaces=namespaces)) == 0
    assert get_interpreter_completions(source="a", namespaces=namespaces)[0].name == "a="

# Generated at 2022-06-14 11:22:52.927516
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import sys

    sys.path.append(r"/usr/local/lib/python3.8/dist-packages/jupyter_client/")
    sys.path.append(r"/usr/local/lib/python3.8/dist-packages/ipython/")
    sys.path.append(r"/usr/local/lib/python3.8/dist-packages/pexpect/")
    sys.path.append(r"/usr/local/lib/python3.8/dist-packages/")

    from jedi import Interpreter
    source = "from jupyter_client.kernelspec import KernelSpecManager\n"
    interpreter = Interpreter(source, [])
    completions = interpreter.complete()
    if completions:
        print(completions[0].complete)
        assert comple

# Generated at 2022-06-14 11:23:00.405487
# Unit test for function get_definitions
def test_get_definitions():
    if not hasattr(test_get_definitions, "jedi"):
        try:
            import jedi

            test_get_definitions.jedi = jedi
        except ImportError:
            return

    jedi = test_get_definitions.jedi

    logger.debug("Using jedi %s", jedi.__version__)

    def test(source, pos, expect_num_definitions, first_type=None, first_full_name=None):
        defs = get_definitions(source, pos[0], pos[1], "dummy.py")
        assert len(defs) == expect_num_definitions
        if expect_num_definitions > 0:
            if first_type is not None:
                assert defs[0].type == first_type

# Generated at 2022-06-14 11:23:19.529329
# Unit test for function get_script_completions
def test_get_script_completions():
    # taken from https://github.com/davidhalter/jedi/blob/d2f45e1c7462f3daf6dd8e2f38b0e41b99894123/jedi/api/refactoring.py#L379
    code = """
import json
json.lo"""

    from jedi import Script

    completions0 = Script(code).completions()
    completions1 = get_script_compl

# Generated at 2022-06-14 11:23:23.703809
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.globals import get_workbench

    for path in get_workbench().get_editor_notebook().get_paths():
        get_script_completions(code, row, column, path)



# Generated at 2022-06-14 11:23:32.164448
# Unit test for function get_definitions
def test_get_definitions():
    """
    Using the test file test_definitions.py, tests whether get_definitions()
    works as expected, particularly with the new jedi version.
    """
    test_dir = os.path.dirname(__file__)
    test_file = os.path.join(test_dir, "test_definitions.py")

    with open(test_file) as fp:
        test_file_lines = fp.readlines()

    test_file_lines = [line.rstrip("\n") for line in test_file_lines]

    # list of test cases

    # 1) spot the 'a' in the line "a = 1" -- has to be a variable, should be defined in the current module
    # 2) spot the the method name "add" in the line "m.add(12)" -- has to be

# Generated at 2022-06-14 11:23:42.524942
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    source = """
import sys
x = sys
sys.stdout.write("abc")
    """
    completions = get_script_completions(
        source=source, row=3, column=5, filename=None, sys_path=["./"]
    )

    assert "sys" in [c.name for c in completions]
    assert "sys=" not in [c.name for c in completions]
    assert "sys" in [c.complete for c in completions]
    assert "sys=" not in [c.complete for c in completions]



# Generated at 2022-06-14 11:23:52.485634
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.plugins.jedi_utils import get_script_completions
    from jedi import common
    from types import ModuleType
    import time
    import os

    res_1 = get_script_completions('import os; os.pa', 0, 15, '/tmp/completion.py')
    res_2 = get_script_completions('os.path.exp', 0, 12, '/tmp/completion.py')

    assert len(res_1) == 1
    assert len(res_2) == 1
    assert res_1[0].name == res_2[0].name
    assert res_1[0].name == 'path'
    assert isinstance(res_1[0].parent, ModuleType)
    assert res_1[0].parent == res_1[0].get_parent_

# Generated at 2022-06-14 11:24:01.668031
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    source = "a = os.walk("

    completions = get_script_completions(source, 0, len(source), "test.py")

    assert len(completions) == 1
    assert completions[0].name == "topdown="
    assert completions[0].complete == "topdown="
    assert completions[0].type == "param"
    assert completions[0].description == "Whether to yield tuples in top-down or bottom-up order."
    assert completions[0].parent.name == "os.walk"



# Generated at 2022-06-14 11:24:08.825645
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    if _using_older_jedi(jedi):
        assert [c.name for c in get_script_completions('import os', 2, 1, 'test.py')] == ["open", "pathsep"]
    else:
        assert [c.name for c in get_script_completions('import os', 2, 1, 'test.py')] == ["abort", "open"]

# Generated at 2022-06-14 11:24:19.122405
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.python.tree import Leaf
    import pythoncom
    from jedi.evaluate import compiled
    from jedi.evaluate.context import ContextSet, ClassContext, FunctionContext

    # jedi 0.17
    def get_interpreter_completions_old(source: str, namespaces: List[Dict], sys_path=None):
        import jedi

        interpreter = jedi.Interpreter(source, namespaces)
        completions = interpreter.completions()
        return _tweak_completions(completions)

    # jedi 0.18
    def get_interpreter_completions_new(source: str, namespaces: List[Dict], sys_path=None):
        import jedi

        interpreter = jedi.Interpreter(source, namespaces)

# Generated at 2022-06-14 11:24:32.619750
# Unit test for function get_script_completions
def test_get_script_completions():
    import os

    import jedi

    if _using_older_jedi(jedi):
        old_jedi = True
    else:
        old_jedi = False

    # Load the source file for testing
    dirname = os.path.dirname(os.path.abspath(__file__))
    parser_test_file = os.path.join(dirname, "parser_test.py")
    with open(parser_test_file) as f:
        source = f.read()

    if old_jedi:
        results = get_script_completions(source, row=4, column=22, filename=parser_test_file)

# Generated at 2022-06-14 11:24:38.512749
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    utils_obj = get_interpreter_completions(
        "import numpy as np\nnp.random", [{"numpy": "numpy"}]
    )
    assert (
        len(utils_obj) > 0
    ), "get_interpreter_completions: completions for numpy should be greater than 0"

# Generated at 2022-06-14 11:24:59.746883
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions('[x for x in "1"][0].u','[{}]', sys_path=["/home/user/projects/thonny"]) == \
        [ThonnyCompletion(name="upper", complete='upper', type='method', description='upper()', parent='str',
                          full_name='str.upper')]

    assert get_interpreter_completions('"1".up', '[{}]', sys_path=["/home/user/projects/thonny"]) == \
        [ThonnyCompletion(name="upper", complete='upper', type='method', description='upper()', parent='str',
                          full_name='str.upper')]


# Generated at 2022-06-14 11:25:07.289439
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    jedi_version = jedi.__version__
    logger.info("Testing get_script_completions with jedi version: " + jedi_version)
    source = "import sys"
    row = 0
    column = 5
    assert get_script_completions(source, row, column, "")[0] == "sys"
    logger.info("get_script_completions test passed")



# Generated at 2022-06-14 11:25:21.367276
# Unit test for function get_definitions
def test_get_definitions():
    # if jedi version is older than 0.18, test is skipped
    try:
        from jedi import Script
        from jedi import __version__
        if _using_older_jedi(jedi):
            return
    except ImportError:
        return
        
    # test file
    import unittest
    import os
    from jedi._compatibility import force_unicode

    test_dir = os.path.dirname(unittest.__file__)
    test_file = os.path.join(test_dir, "test_unittest.py")
    source = open(test_file).read()
    source = force_unicode(source)
    script = Script(source, 4, 7, test_file)

# Generated at 2022-06-14 11:25:26.060655
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import os"
    namespaces = []
    result = get_interpreter_completions(source, namespaces)
    assert result[0].name == "os"
    assert result[0].type == "module"
    assert result[0].complete == "os."
    assert result[0].description.startswith("Module os")


# Generated at 2022-06-14 11:25:39.754090
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.codeview import parse_source

    source = '''
    from math import pi
    class Foo:
        def __init__(self, x):
            self.x = x
        def bar(self):
            return self.x * pi
    '''
    root = parse_source(source)
    found = False
    for stmt in root.iter_subtrees():
        if stmt.type == "funcdef" and stmt.get_name() == "bar":
            found = True
            break
    if not found:
        raise RuntimeError("Unit test needs to be updated")

    completions = get_script_completions(source, 2, 12, "", [])

# Generated at 2022-06-14 11:25:45.848710
# Unit test for function get_definitions
def test_get_definitions():
    import os

    def get_definitions_in_file(filename):
        jedi_proposals = get_definitions(
            open(filename).read(), 3, 3, os.path.basename(filename)
        )
        return [p.desc_with_module for p in jedi_proposals]

    assert get_definitions_in_file(__file__) == [
        "functools.partial(__builtin__.callable, obj, *args, **keywords)"
    ]



# Generated at 2022-06-14 11:25:48.048469
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions(
        """
    import abc
    abc. 
    """,
        row=2,
        column=7,
        filename="myfile.py",
    )

# Generated at 2022-06-14 11:25:58.646121
# Unit test for function get_script_completions
def test_get_script_completions():
    import unittest
    import jedi

    def get_completions(_source, _pos):
        return get_script_completions(_source, 1, _pos + 1, "/my/file.py")

    # Test from jedi.Script

# Generated at 2022-06-14 11:26:11.980351
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    import shutil
    import os
    from pathlib import Path
    from thonny.codeview import JediCodeView

    test_folder = Path(__file__).parent / "jedi_versions"
    cur_loc = os.getcwd()
    new_loc = test_folder / "get_script_comp"

# Generated at 2022-06-14 11:26:22.947201
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import MagicMock
    from jedi.api.classes import Script, Interpreter
    from jedi.api.project import Project

    # No need for actual namespaces, just create mock objects
    namespaces = [MagicMock() for _x in range(2)]
    result = get_interpreter_completions(source="", namespaces=namespaces)
    assert result == []

    # Test completion with non-empty list of namespaces
    namespaces = [MagicMock() for _x in range(3)]
    namespaces[1].get_defined_names.return_value = ["a", "b", "c"]
    namespaces[2].get_defined_names.return_value = ["A", "B", "C"]

# Generated at 2022-06-14 11:26:55.071939
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api.classes import Script as ScriptClass

    from jedi.api_classes import Script, Interpreter

    with open("jedi_get_script_completions.py") as fp:
        source = fp.read()

    assert type(get_script_completions(source, 5, 1, "jedi_get_script_completions.py")) == ScriptClass



# Generated at 2022-06-14 11:27:11.102418
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions(source='a.upper()',
        namespaces=[{'a': 'string'}])
    assert completions[0].name == 'upper'
    assert completions[0].complete == 'upper('
    assert completions[0].type == 'function'
    assert completions[0].description == 'S.upper() -> str\n\nReturn a copy of S converted to uppercase.'
    assert completions[0].parent == 'builtins.str'
    assert completions[0].full_name == 'builtins.str.upper'

    assert completions[1].name == 'upper'
    assert completions[1].complete == 'upper()'
    assert completions[1].type == 'instance'

# Generated at 2022-06-14 11:27:22.197907
# Unit test for function get_script_completions
def test_get_script_completions():
    """
    This function tests the function get_script_completions with different parameters

    Args:
        len(sys_path): an integer specifies the length of sys_path
        sys_path: a list of strings that specify the project path

    Returns:
        True: if the test runs successfully
        False: if the test does not run successfully
    """
    import jedi

    def run(source: str, row: int, column: int, filename: str, sys_path=None):
        script = jedi.Script(source, row, column, filename, sys_path=sys_path)
        completions = script.completions()

        return completions

    main_input = """
if __name__ == "__main__":
    if abcd.abc == 1:
        print("hello")
    """
    main_input_

# Generated at 2022-06-14 11:27:24.677277
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert (
        get_interpreter_completions("import this; this.r", [])[0].complete
        == "this.reduce("
    )



# Generated at 2022-06-14 11:27:35.665809
# Unit test for function get_definitions
def test_get_definitions():
    def do_test(code, row, column, path="test.py", expected_module_paths=None):
        probes = get_definitions(code, row, column, path)

        results = []
        for p in probes:
            if expected_module_paths and p.module_path not in expected_module_paths:
                continue
            results.append(
                {
                    k: getattr(p, k)
                    for k in [
                        "module_path",
                        "line",
                        "column",
                        "get_line_code",
                        "description",
                        "name",
                        "type",
                    ]
                }
            )

        assert results == expected_module_paths

    # do_test("from math import exp", 6, 0,
    #     expected_module_paths=[{"line

# Generated at 2022-06-14 11:27:49.393977
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    assert jedi.__version__ >= "0.17"

    some_namespace = [{"thonny": {"__name__": "thonny", "__loader__": "loader"}}]
    interpreter = jedi.Interpreter("thonny.run_file(", some_namespace)
    completions = interpreter.complete()
    assert len(completions) == 1, completions
    assert completions[0].name == "run_file"
    # assert completions[0].complete == "run_file("
    assert completions[0].parent() == "thonny"
    assert completions[0].type == "function"
    assert completions[0].description == "Runs a Python file"

    completion = completions[0]

    # NB! Can't get docstring of interpreter comple

# Generated at 2022-06-14 11:27:54.338547
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    def compare(completion1, completion2):
        completion = None

        for c in completion1:
            if c.complete == completion2.complete:
                completion = c
                break

        assert completion is not None

        if completion.complete == "__init__" and completion2.complete == "__init__":
            pass
        elif completion.complete == "__init__":
            assert completion2.complete == "init"
        elif completion2.complete == "__init__":
            assert completion.complete == "init"
        else:
            assert completion.complete == completion2.complete
        assert completion.description == completion2.description

    # ################
    # Python
    # ################
    completions = get_interpreter_completions('import os', [], [])

# Generated at 2022-06-14 11:28:08.322305
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = """
import math
print(math.exp)
"""
    expect = ["math.exp(", "math.expm1(", "math.exp2("]
    completions = get_interpreter_completions(source, [{"math": math}])
    assert completions
    assert completions[0].complete in expect
    assert completions[0].name in expect
    assert completions[0].type in ["function", "builtin"]
    assert completions[0].full_name == "math.exp"

    completions = get_interpreter_completions(
        source, [{"math": math}, {"builtins": __builtins__}]
    )
    assert completions


if __name__ == "__main__":
    import math

    test_get_interpreter_completions()

# Generated at 2022-06-14 11:28:22.826842
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import random
    import string

    def randomString():
        return "".join([random.choice(string.ascii_letters) for i in range(10)])

    completions=get_interpreter_completions("a=5", [{"a":5}], None)
    assert [c.name for c in completions] == ["a"]

    completions=get_interpreter_completions("a=5; a", [{"a":5}], None)
    assert [c.name for c in completions] == ["a"]

    completions=get_interpreter_completions("a=5; b=7; a", [{}, {"a":5, "b":7}], None)
    assert [c.name for c in completions] == ["a", "b"]

    # Function parameters


# Generated at 2022-06-14 11:28:31.319693
# Unit test for function get_script_completions
def test_get_script_completions():
    for jedi_version in ["0.13.2", "0.16.0", "0.18.0"]:
        source = "a = 5\nprint(a)"
        res = get_script_completions(source, 0, 0, "test.py")
        assert len(res) == 5
        res = get_script_completions(source, 1, 6, "test.py")
        assert len(res) == 2
        res = get_script_completions(source, 1, 6, "test.py", sys_path=["foo"])
        assert len(res) == 2



# Generated at 2022-06-14 11:29:09.039081
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.parser import load_grammar
    from jedi.parser import Parser

    # Test function definition
    def_source = 'class A:\n\tdef __init__(self):\n\t\tpass'
    grammar = load_grammar()
    parser = Parser(grammar, def_source, 'test.py')
    root_node = parser.parse()
    definitions = get_definitions(root_node, (2, 3))
    assert len(definitions) == 1
    assert definitions[0].name == 'A.__init__'
    assert definitions[0].line == 0
    assert definitions[0].column == 5

    # Test self
    def_source = 'class A:\n\tdef __init__(self):\n\t\tx = self'
    grammar = load_grammar

# Generated at 2022-06-14 11:29:21.948627
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi.api

    # In jedi before 0.18, `description` attribute didn't contain '=' for argument completions,
    # since 0.18 it does
    completions = jedi.api.get_interpreter_completions("[].","append", sys_path=())
    assert completions == [ThonnyCompletion("append=", "append=", "param", "append(${1:object})", "list", "list.append")]
    
    completions = jedi.api.get_interpreter_completions("[].append","", sys_path=())
    assert completions == [ThonnyCompletion("append=", "append=", "param", "append(${1:object})", "list", "list.append")]
    
    completions = jedi.api.get_interpre

# Generated at 2022-06-14 11:29:26.819376
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from collections import namedtuple

    completions = get_interpreter_completions(
        "import os, sys",
        namespaces=[{"__builtins__": __builtins__}, {"os": os, "sys": sys}],
    )
    assert namedtuple("Completion", ["name", "complete", "type", "description", "parent"])(
        "os\n    ", "os", "module", "", ""
    ) in completions
    assert namedtuple("Completion", ["name", "complete", "type", "description", "parent"])(
        "sys\n    ", "sys", "module", "", ""
    ) in completions



# Generated at 2022-06-14 11:29:30.489836
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions("print(", [{}])
    assert len(completions) > 10
    assert any(c.name == "print" for c in completions)

# Generated at 2022-06-14 11:29:35.921732
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if _using_older_jedi(jedi):
        return
    source = """
import os.path
os.pa""".strip()
    namespaces = [{'__name__': '__main__', '__doc__': None}]
    completions = get_interpreter_completions(source, namespaces)
    only_names = [c.name for c in completions]
    assert "os.path" in only_names



# Generated at 2022-06-14 11:29:45.410711
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api import Interpreter
    import ast

    code = """import sys
sys"""
    module = ast.parse(code)
    interpreter = Interpreter(code, [])
    completions = interpreter.completions()
    result = interpreter.api_complete(module, 7, 1, '')
    if hasattr(interpreter, "completions"):
        assert set(completions) == set(result)
    else:
        assert set(completions) == set(result[0])


# Generated at 2022-06-14 11:29:50.860142
# Unit test for function get_script_completions
def test_get_script_completions():
    # import unittest

    # class TestGetScriptCompletions(unittest.TestCase):
    #     def test_get_script_completions_no_error(self):
    #         pass #call get_script_completions with a simple string

    # unittest.main()
    pass



# Generated at 2022-06-14 11:29:51.894044
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:30:01.280118
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter

    def intercept_complete_call(self, **kwargs):
        return self._get_completions(**kwargs)

    Interpreter._complete = intercept_complete_call
    result = get_interpreter_completions('a="a"\na.', [])
    assert result[0].name.startswith('capitalize')
    assert result[1].name.startswith('center')
    assert result[-1].name.startswith('zfill')

# Generated at 2022-06-14 11:30:06.230361
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    script_completions_old = lambda *args: get_script_completions(*args, sys_path=[])

    completions = get_script_completions("import dateti", 1, 9, "test.py")
    assert completions[0].name == "datetime"

    completions = script_completions_old("import dateti", 1, 9, "test.py")
    assert completions[0].name == "datetime"

    completions = script_completions_old("from datetim", 1, 11, "test.py")
    assert completions[0].name == "datetime"

    completions = script_completions_old("from datetime import ti", 1, 26, "test.py")
    assert completions[0].name == "time"

   

# Generated at 2022-06-14 11:30:40.826759
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api.refactoring import inline
    script_source = "import tkinter; root = tkinter.Tk()\n"
    assert get_script_completions(
        script_source, row=1, column=19, filename="test.py"
    )[
        0
    ].name == "Tk"  # Completion for tkinter.Tk()
    assert get_script_completions(
        script_source, row=1, column=15, filename="test.py"
    )[
        0
    ].name == "Tk"  # Completion for tkinter.Tk
    assert get_script_completions(script_source, row=2, column=4, filename="test.py")[
        0
    ].name == "Tk"  # Completion

# Generated at 2022-06-14 11:30:47.979687
# Unit test for function get_definitions
def test_get_definitions():
    source = "import sys\ndir(sys)"
    row = 2
    column = 8
    filename = "test.py"
    defs = get_definitions(source, row, column, filename)
    assert len(defs) == 1
    assert defs[0].name == "dir" and defs[0].line == 1 and defs[0].column == 6 and defs[0].module_path == "builtins"

# Generated at 2022-06-14 11:30:53.788597
# Unit test for function get_definitions
def test_get_definitions():
    # get_definitions function should return a list with all the definitions of a call
    assert len(get_definitions("print",0,5,"")) == 1
    assert len(get_definitions("import os",0,8,"")) == 1
    assert len(get_definitions("os.path",0,7,"")) == 1


# Generated at 2022-06-14 11:30:59.533429
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.python.tree import Module
    import parso
    import jedi
    source = "import math\nmath.sqrt(1)\n"
    module = parse_source(source)
    node = module.subscopes[0]
    pos = len("math")
    # Get the module or function call at the cursor.
    node = get_statement_of_position(node, pos)
    # Get the completions
    result = get_interpreter_completions(source, [{'module': node.get_parent_until(Module)}])
    assert len(result) > 0

# Generated at 2022-06-14 11:31:10.248167
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.plugins.micropython.backend import MicroPythonProxy, MicroPythonOutput
    import threading

    class TestInterpreterThread(threading.Thread):
        def __init__(self, source, namespaces):
            threading.Thread.__init__(self)
            self.source = source
            self.namespaces = namespaces
            self.completions = []

        def run(self):
            self.completions = get_interpreter_completions(self.source, self.namespaces)

    # Use MicroPython to run test of completions in interpreter
    namespace = {}
    test_source = """
    import test
    test.square
    x = 5
    """
    test_source = test_source.split("\n")

    buf = MicroPythonOutput()
    a = MicroPython