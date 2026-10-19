

# Generated at 2022-06-14 11:21:23.262460
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if jedi.__version__[:4] not in ["0.13", "0.14", "0.15", "0.16", "0.17"]:
        return

    from unittest import TestCase, main

    class TestGetInterpreterCompletion(TestCase):
        def test_get_completions(self):
            completions = get_interpreter_completions(
                "import itertools\nitertools.",
                [{"x": "stuff"}],
                sys_path=["/home/timo/workspace"],
            )

            self.assertTrue(len(completions) > 0)
            self.assertTrue(all([c.name.startswith("itertools.") for c in completions]))

    main()

# Generated at 2022-06-14 11:21:36.119513
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    namespaces = [
        {"a": 1},
    ]

    def assert_interpreter_completions(code, expectedCompletions):
        completions = get_interpreter_completions(code, namespaces)
        # print("completions %s" % completions)
        numCompletions = len(completions)
        assert numCompletions == len(expectedCompletions)
        for i in range(numCompletions):
            c = completions[i]
            ec = expectedCompletions[i]
            assert (
                c.name == ec["name"] and c.complete == ec["complete"] and c.type == ec["type"]
            )


# Generated at 2022-06-14 11:21:45.266717
# Unit test for function get_definitions
def test_get_definitions():
    # given
    source = "from time import sleep"
    row = 0
    column = 5

    # when
    defs = get_definitions(source, row, column, "dummy.py")

    # then
    assert len(defs) == 1
    assert "import sleep from" in defs[0].description


if __name__ == "__main__":
    test_get_definitions()

# Generated at 2022-06-14 11:21:51.732028
# Unit test for function get_definitions
def test_get_definitions():
    from jedi import api


# Generated at 2022-06-14 11:21:59.898866
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.parser_utils import get_cached_code
    from jedi.api.classes import Completion
    from jedi.evaluate.compiled import CompiledObject
    from jedi.api.names import AbstractNameDefinition, NameWrapper

    source = get_cached_code("import arrow; arrow")
    completions = get_script_completions(source, 0, 16, "/Users/mvr/src/arrow.py")
    assert len(completions) == 3
    assert completions[1].name == "arrow"
    assert completions[1].complete == "arrow"
    assert completions[1].type == "module"

    assert completions[2].name == "datetime"
    assert completions[2].complete == "datetime"
    assert completions[2].type == "module"

    expected

# Generated at 2022-06-14 11:22:09.428586
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from parso.python.tree import Leaf
    from thonny.backend import runfile
    from thonny.config import get_curdir_preference

    # Check if the path to the test script is correct
    assert get_curdir_preference() == "."

    # Test script with import statement
    test_script = """
    import os
    os.
    """
    # Run the test script
    test_backend = runfile("test_utils_jedi.py", [test_script])
    test_namespaces = [
        {
            "name": ":test_backend",
            "get_namespace": (lambda: test_backend.locals),
        }
    ]
    completions = get_interpreter_completions(test_script, test_namespaces)
    comple

# Generated at 2022-06-14 11:22:14.464876
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions("import sys\nsys.", [], [])
    assert completions == get_interpreter_completions("import sys\nsys.", [], None)
    assert completions

# Generated at 2022-06-14 11:22:19.259192
# Unit test for function get_definitions
def test_get_definitions():
    import doctest
    import jedi

    import thonny.globals

    for jedi_version in ["0.13", "0.14", "0.15", "0.16", "0.17", "0.18", "0.19", "0.20"]:
        thonny.globals.set_jedi_version(jedi_version)
        failures, _ = doctest.testmod(jedi)
        if failures == 0:
            print("jedi", jedi_version, "OK")
        else:
            print("jedi", jedi_version, "FAILED")

# Generated at 2022-06-14 11:22:22.665678
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.plugins.jedi_plugin import _get_module_path
    _get_module_path()
    source = "import sys\nsys.s"
    completions = get_interpreter_completions(source, [{"name": "sys", "path": "sys"}])
    assert len(completions) == 2
    assert set([completion.name for completion in completions]) == {"stdout", "stdin"}



# Generated at 2022-06-14 11:22:28.943081
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    if jedi.__version__[:4] in ["0.13", "0.14"]:
        script = jedi.Script("", 1, 1, "")
        assert len(script.completions()) == 0

    else:
        completions = get_script_completions("", 1, 1, "")
        assert len(completions) == 0

# Generated at 2022-06-14 11:22:38.260533
# Unit test for function get_script_completions
def test_get_script_completions():
    import parso
    import jedi
    import sys


# Generated at 2022-06-14 11:22:49.684442
# Unit test for function get_definitions
def test_get_definitions():
    definitions = get_definitions("print", 1, 6, "")
    assert len(definitions) == 1
    assert str(definitions[0]).startswith("<Definition print@builtins")

    definitions = get_definitions("time.sleep(", 1, 18, "")
    assert len(definitions) == 1
    assert str(definitions[0]).startswith("<Definition sleep@time")

    definitions = get_definitions("def foo(): pass", 1, 22, "")
    assert len(definitions) == 1
    assert str(definitions[0]).startswith("<Definition foo@")

    definitions = get_definitions("def foo(): pass\nfoo", 2, 4, "")
    assert len(definitions) == 1
    assert str(definitions[0]).startswith("<Definition foo@")

# Generated at 2022-06-14 11:22:58.220654
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    code = """\
import tkinter
window = tkinter.Tk()

button = tkinter.Button(window, text="Hello World")
button.pack()
window.mainloop()
"""
    namespace = {}
    interpreter = Interpreter(code=code, namespaces=[namespace])

    # sanity check
    assert interpreter.completions()
    assert interpreter.complete()
    assert interpreter._inference_state is None

    # after first call the state is saved
    completions = interpreter.completions()
    assert completions
    assert interpreter._inference_state

    # if state is empty, then the completions should be None
    interpreter._inference_state = {}
    assert interpreter.completions() is None
    assert interpreter.complete() is None


# Unit test

# Generated at 2022-06-14 11:23:02.779918
# Unit test for function get_definitions
def test_get_definitions():
    from types import SimpleNamespace
    from jedi import Interpreter
    import parso
    from os.path import join, dirname

    project_dir = join(dirname(__file__), "micropython")

# Generated at 2022-06-14 11:23:13.552634
# Unit test for function get_script_completions
def test_get_script_completions():
    if __name__ == "__main__":
        path = "."
    else:
        import os
        import inspect
        import sys

        path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        sys.path.insert(0, path)

    source = """def foo(a, b):
    pass
foo(a"""
    result = get_script_completions(source, 3, 11, "test.py", [path])
    assert len(result) == 1
    assert result[0].name == 'a'


if __name__ == "__main__":
    test_get_script_completions()

# Generated at 2022-06-14 11:23:20.088864
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    print(get_interpreter_completions("glu", [{}], sys_path=["/usr/lib/python3.6"]))
    print(get_interpreter_completions("froz", [{}]))
    print(get_interpreter_completions("froz", [{}], sys_path=["/usr/lib/python3.6"]))

# Generated at 2022-06-14 11:23:30.690715
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    user_namespace = [{
        '__name__': '__main__',
        'x': 1,
        'r': range(10),
        's': set([1, 2, 3]),
        'l': [1, 2, 3],
        't': (1, 2, 3),
        'd': {1: 1, 2: 2},
        'f': lambda x: x,
        'cls': TestClass(),
        'inst': TestClass(),
    }]

    completions = get_interpreter_completions('range(10).', user_namespace)
    assert completions[0].name == "count"

    completions = get_interpreter_completions('set([1, 2, 3]).', user_namespace)
    assert completions[0].name == "clear"



# Generated at 2022-06-14 11:23:35.755421
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.globals import get_workbench

    get_workbench().bind("ToplevelResponse", lambda event: None)
    get_interpreter_completions("2+2", [], [])

# Generated at 2022-06-14 11:23:46.181087
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import get_workbench

    get_workbench().set_option("editor.jedi_enable_docstring_preview", False)
    assert len(get_script_completions('import s', 1, 1, 'sample.py')) == 1
    assert len(get_script_completions('import sys', 1, 1, 'sample.py')) == 1
    assert len(get_script_completions('sys.getrefcount', 1, 1, 'sample.py')) == 1
    assert len(get_script_completions('sys.', 1, 1, 'sample.py')) > 5
    assert len(get_script_completions('sys.getre', 1, 1, 'sample.py')) == 1

# Generated at 2022-06-14 11:23:52.709919
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import os
    import jedi.api

    source = "import os"
    namespaces = [jedi.api.InterpreterNamespace(os, "os")]
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) > 0
    assert completions[0].complete == "path"

# Generated at 2022-06-14 11:24:04.930032
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import parser_utils
    from jedi.parser.tree import ImportFrom, ImportName

    source = "import datetime"
    row = 0
    column = 7
    filename = __file__
    script_completions = get_script_completions(source, row, column, filename)
    assert script_completions != []
    assert len(script_completions) == 1

    # As of jedi 0.16, the name attribute of the first completion will be 'datetime='
    # In jedi 0.15 and earlier, the name attribute will be 'datetime'
    assert script_completions[0].name in ('datetime', 'datetime=')
    assert script_completions[0].complete == 'datetime'
    assert script_completions[0].type == 'module'

# Generated at 2022-06-14 11:24:14.429555
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from inspect import Signature, Parameter

    from thonny.plugins.jedi_utils import get_interpreter_completions

    signature = Signature(
        [
            Parameter("x", Parameter.POSITIONAL_OR_KEYWORD, default=5),
            Parameter("y", Parameter.POSITIONAL_OR_KEYWORD, default=5),
            Parameter("z", Parameter.POSITIONAL_OR_KEYWORD, default=5),
        ]
    )
    param_names = [param.name for param in signature.parameters.values()]
    # must be sorted!
    assert param_names == ["x", "y", "z"]
    completion = get_interpreter_completions("sorted(", [])
    sorted_completion = [x.name for x in completion]


# Generated at 2022-06-14 11:24:16.119887
# Unit test for function get_definitions
def test_get_definitions():
    definitions = get_definitions('import math\nmath.pi', 0, 0, 'dummy.py')
    assert len(definitions) == 1

# Generated at 2022-06-14 11:24:17.845871
# Unit test for function get_definitions
def test_get_definitions():
    import unittest
    import unittest.mock
    import jedi


# Generated at 2022-06-14 11:24:31.081492
# Unit test for function get_definitions
def test_get_definitions():
    from thonny.config import get_python_exe

    c = get_definitions("a.b", 0, 0, "test_file")
    assert len(c) == 1
    c = get_definitions("a.b", 0, 0, "test_file", sys_path=[get_python_exe()])
    assert len(c) == 1
    assert isinstance(c[0].module_path, str)

    if get_python_exe().endswith("python3.exe"):
        c = get_definitions("x = {}", 0, 0, "test_file", sys_path=[get_python_exe()])
        assert len(c) == 2  # see https://bugs.python.org/issue31083
        assert c[0].module_path == "builtins"

# Generated at 2022-06-14 11:24:40.232765
# Unit test for function get_script_completions
def test_get_script_completions():
    import os

    def validate(res):
        if not isinstance(res, list):
            raise AssertionError("Result must be list of completions")
        for comp in res:
            if not isinstance(comp.name, str):
                raise AssertionError("Completion name must be string")
            if not isinstance(comp.complete, str):
                raise AssertionError("Completion complete must be string")
            if not isinstance(comp.type, str):
                raise AssertionError("Completion type must be string")
            if not isinstance(comp.description, str):
                raise AssertionError("Completion description must be string")
            if not isinstance(comp.parent, str):
                raise AssertionError("Completion parent must be string")

# Generated at 2022-06-14 11:24:50.283119
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    namespaces = [{"a": 2}]
    completions = get_interpreter_completions("a", namespaces)
    assert completions == [ThonnyCompletion("a", "a", "statement", "int", "", "a")]

    # Ensure that completions don't depend only on namespaces, but also on code
    completions = get_interpreter_completions("", namespaces)
    assert completions == []
    # Even weird things like a comment as code should not cause problems
    completions = get_interpreter_completions("#", [])
    assert completions == []

    # Ensure that completions can handle a FunctionDefinition
    completions = get_interpreter_completions("def f():\n\tpass", [])

# Generated at 2022-06-14 11:24:53.910771
# Unit test for function get_definitions
def test_get_definitions():
    import sys, os

    print(os.getcwd())
    print(sys.path)
    print(os.listdir())
    print(get_definitions("open(\"xy.txt\")", 0, 17, "test.py"))

# Generated at 2022-06-14 11:24:57.379390
# Unit test for function get_definitions
def test_get_definitions():
    import parso
    from parso.python import tree
    import jedi
    import jedi.parser_utils


# Generated at 2022-06-14 11:25:09.638434
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script

    script = Script("""\
    import os, sys
    os
    """, 1, 2, "a.py")
    completions = script.completions()
    assert len(completions) == 2
    assert completions[0].name == "os"
    assert completions[1].name == "sys"
    completions = script.completions()
    assert len(completions) == 2
    assert completions[0].name == "os"
    assert completions[1].name == "sys"

# Generated at 2022-06-14 11:25:26.125792
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import unittest

    class TestCase(unittest.TestCase):
        def test_get_interpreter_completions(self):
            # Test whether it's possible to get completions for the interpreter
            # with jedi versions that support the new API.
            if getattr(jedi, '__version__', '0.0') >= '0.18':
                result = get_interpreter_completions(source=None, namespaces=None)
                if result != []:
                    self.fail("get_interpreter_completions does not handle jedi 0.18 correctly")

    test_case = TestCase()
    test_case.test_get_interpreter_completions()

# Generated at 2022-06-14 11:25:39.792394
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase, main

    class TestGetInterpreterCompletions(TestCase):
        def test_jedi_0_10(self):
            def _mock_complete():
                class Terminator:
                    def __init__(self):
                        self.name = ""
                        self.complete = ""
                        self.type = ""
                        self.description = ""
                        self.parent = ""
                        self.full_name = ""

                return [Terminator() for i in range(4)]

            import jedi

            original_complete = jedi.Interpreter.complete


# Generated at 2022-06-14 11:25:41.405838
# Unit test for function get_definitions
def test_get_definitions():
    from parso.python.tree import Leaf


# Generated at 2022-06-14 11:25:55.292798
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.plugins.jedi_utils import get_script_completions
    from thonny.languages.utils import get_module_source_code
    import sys
    import os

    dir = os.path.dirname(os.getcwd())
    new_path = list(sys.path)
    new_path.append(dir)

    name = "unittest"
    source = get_module_source_code(name)
    source = source.replace("\r\n", "\n").replace("\r", "\n")

    completions = get_script_completions(source, 0, 0, name, new_path)

    # Completions exist
    assert completions != None
    assert isinstance(completions, list)
    assert len(completions) > 0

    # Test

# Generated at 2022-06-14 11:26:01.284318
# Unit test for function get_definitions
def test_get_definitions():
    import pathlib
    from thonny import get_workbench
    from thonny.shell import Shell
    
    test_root = pathlib.Path(__file__).parent
    source = (test_root / "testdata" / "get_definitions_test.py").read_text()
    get_workbench().set_editor_content(source)
    Shell().send_current_file()
    assert len(get_definitions(source, row=1, column=25, filename="get_definitions_test.py")) == 1
    
    
if __name__ == "__main__":
    test_get_definitions()

# Generated at 2022-06-14 11:26:13.381407
# Unit test for function get_definitions
def test_get_definitions():
    result = get_definitions('import math\ns = math.sin\nmath.sin', 3, 9, '')
    assert len(result) == 1
    result = get_definitions('def f(p):\n    p', 1, 6, '')
    assert len(result) == 1
    result = get_definitions('def f():\n    pass\n\nf()', 4, 1, '')
    assert len(result) == 1
    result = get_definitions('def f():\n    pass\n\nf()', 5, 1, '')
    assert len(result) == 1
    result = get_definitions('class C:\n    def foo(self):\n        pass\nc = C()\nc.foo', 5, 5, '')
    assert len(result) == 1



# Generated at 2022-06-14 11:26:14.611252
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import get_runner, jedi_utils


# Generated at 2022-06-14 11:26:28.317791
# Unit test for function get_definitions
def test_get_definitions():
    import sys
    from jedi.api.classes import Definition

    assert sys.path[0] == '/usr/lib'
    source = """
    import sys
    sys.path.append('.')
    def a_func(x):
        return x+1
    """

    row, column = 3, 10

    definitions = get_definitions(source, row, column, "<stdin>")
    assert [d.desc_with_module for d in definitions] == [
        'sys: sys',
        'ImportError: sys',
        'ImportWarning: sys',
        'SystemExit: sys',
    ]

    row, column = 4, 10
    definitions = get_definitions(source, row, column, "<stdin>")

# Generated at 2022-06-14 11:26:40.552673
# Unit test for function get_definitions
def test_get_definitions():
    source = """
    class SomeClass:
        def __init__(self):
            self.x = 42
            self.y = 0
    
    def some_function(x):
        x.y = x.x + 1
        return x.x
    
    some_function(SomeClass())
    """
    source += "\n" * 100
    from parso.python.tree import Leaf, Name
    from parso.python.token import TokenType

    class SomeClass(object):
        pass

    class SomeFunction(object):
        pass

    class X(object):
        pass

    class Y(object):
        pass


# Generated at 2022-06-14 11:26:44.771680
# Unit test for function get_definitions
def test_get_definitions():
    source = "for i in range(10):\n    print(i)\n"
    result = get_definitions(source, 1, 10, "")
    assert result[0].description == "builtin function range"



# Generated at 2022-06-14 11:27:07.644038
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock
    import jedi
    old_Script = jedi.Script
    jedi.Script = Mock()

# Generated at 2022-06-14 11:27:18.081929
# Unit test for function get_definitions
def test_get_definitions():
    import inspect
    import textwrap
    import jedi

    script = jedi.Script(
        textwrap.dedent(inspect.getsource(test_get_definitions))
    )
    definitions = script.infer(11, 4)
    assert len(definitions) == 1
    definition = definitions[0]
    assert definition.description == """\
    test_get_definitions()
    
    Unit test for function get_definitions"""
    assert definition.full_name == 'test_get_definitions'
    assert definition.line == 1
    assert definition.column == 4
    assert definition.path == '<string>'
    assert definition.name == 'test_get_definitions'
    assert definition.module_path == '<string>'
    assert definition.type == 'function'
    assert definition.in_

# Generated at 2022-06-14 11:27:30.755688
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi.evaluate
    namespaces = [{
        "x": jedi.evaluate.Instance(None, is_class=True, status="executed"),
        "y": "text",
        "z": jedi.evaluate.Instance(None, is_class=True, status="executed"),
        "zz": "text",
    }]
    assert get_interpreter_completions("zz", namespaces) == [{
        "name": "zz",
        "complete": "zz",
        "type": "statement",
        "description": "",
        "parent": "",
        "full_name": "zz",
    }]

# Generated at 2022-06-14 11:27:35.292717
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions("print(", [{'x': 1}])
    assert len(completions) > 0
    # TODO: this is not necessarily true
    # assert completions[0].name == 'print'

# Generated at 2022-06-14 11:27:49.052521
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions("str((12, )", 0, 20, "test.py") == []
    assert get_script_completions("str((12, )", 0, 10, "test.py")[0].name == "str"
    assert get_script_completions("str((12, )", 0, 9, "test.py")[0].name == "str"
    assert get_script_completions("str((12, )", 0, 11, "test.py") == []
    assert get_script_completions("str((12, )", 0, 11, "test.py") == []
    assert get_script_completions("str((12, )", 0, 12, "test.py")[0].name == "str"

# Generated at 2022-06-14 11:27:53.259567
# Unit test for function get_script_completions
def test_get_script_completions():
    def check(source, row, column, expected_completions):
        from jedi import Script

        completions = Script(source, row, column).completions()
        actual_completions = [
            (c.name, c.complete, c.type, c.description, c.full_name) for c in completions
        ]
        assert actual_completions == expected_completions


# Generated at 2022-06-14 11:28:02.472228
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("""import math
math.sqrt(
""", 2, 8, "")
    if len(completions) < 10:
        raise AssertionError("Less than 10 completions")
    if ("ge" in [c.complete for c in completions]) or (
        "ceil" in [c.complete for c in completions]
    ):
        raise AssertionError("Bad completions")


if __name__ == "__main__":
    test_get_script_completions()

# Generated at 2022-06-14 11:28:12.387805
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    import jedi
    # set up a namespace
    namespace = {'pi': 3.14, 'pow': pow}
    #create Interpreter object using source and namespace
    interpreter = Interpreter('import math', [namespace])

    #check completions
    # NB! Can't send project for Interpreter in 0.18
    # https://github.com/davidhalter/jedi/pull/1734
    completions = interpreter.complete()
    assert completions[0].name == 'math'

    completions = get_interpreter_completions('import math', [namespace], sys_path=sys_path)
    assert completions[0].name == 'math'

# Generated at 2022-06-14 11:28:15.200507
# Unit test for function get_definitions

# Generated at 2022-06-14 11:28:17.802575
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:28:40.897617
# Unit test for function get_script_completions
def test_get_script_completions():
    # Test function on first line (x = "")
    assert get_script_completions(
        """
x = ""
""", 0, 2, "", sys_path=[]) == []

    # Test function on second line

# Generated at 2022-06-14 11:28:43.992059
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions('"something".co', [{}]) == []

# Generated at 2022-06-14 11:28:47.430457
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions("os.chmod(", 3, 8, "")[0].name == "chmod"

# Generated at 2022-06-14 11:28:51.470784
# Unit test for function get_script_completions
def test_get_script_completions():
    source = """import sys
sys.std
"""
    sys_path = None
    completions = get_script_completions(source, 2, 8, "test.py", sys_path)
    assert len(completions) > 10



# Generated at 2022-06-14 11:28:59.483484
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    >>> from test.jedi_tester import get_interpreter_completions
    >>> from test.jedi_tester import ThonnyCompletion
    >>> imports_namespace = [{"type": "module", "full_name": "time"}]
    >>> completions = get_interpreter_completions("im", imports_namespace)
    >>> type(completions[0]) is ThonnyCompletion
    True
    >>> completions[0]
    ThonnyCompletion(name='imp', complete='imp', type='module', description='None', parent='builtin', full_name='imp')
    >>> completions[1]
    ThonnyCompletion(name='importlib', complete='importlib', type='module', description='None', parent='builtin', full_name='importlib')
    """

# Generated at 2022-06-14 11:29:11.622225
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    import os
    import jedi

    dir_name = os.path.dirname(os.path.dirname(os.path.dirname(jedi.__file__)))
    sys_path = [dir_name, os.path.join(dir_name, "tests")]
    completions = get_script_completions("import base64", 1, 10, "", sys_path)
    assert len(completions) == 2
    assert completions[0].name == "base64"
    assert completions[1].name == "basestring"

    completions = get_script_completions("from jedi.parser_utils import get_statement_of_position", 1, 10, "", sys_path)
    assert len(completions) == 1

# Generated at 2022-06-14 11:29:26.311492
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.jedi_utils import PROGRAM_TEXT
    from thonny.jedi_utils import get_script_completions

    # Should return completions
    res = get_script_completions(PROGRAM_TEXT, 1, 11, "")
    assert len(res) == 31

    # Should return completions
    res = get_script_completions(PROGRAM_TEXT, 1, 12, "")
    assert len(res) == 31

    # Should return completions
    res = get_script_completions(PROGRAM_TEXT, 1, 12, "", sys_path=["does_not_exist"])
    assert len(res) == 31

    # Should return completions

# Generated at 2022-06-14 11:29:32.288119
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    script = get_script_completions(
        "import string\nstring.", 7, 12, filename="foo.py", sys_path=[__file__]
    )
    assert "string" in [completion.name for completion in script]

    if not _using_older_jedi(jedi):
        script = get_script_completions(
            "import string\nstring.lower(", 7, 21, filename="foo.py", sys_path=[__file__]
        )
        assert "lower" in [completion.name for completion in script]



# Generated at 2022-06-14 11:29:34.068421
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions("abs('a').upper().", 3, 13, "test.py") != None

# Generated at 2022-06-14 11:29:47.663603
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    jedi_version = jedi.__version__
    if jedi_version[:4] == "0.13":
        source = "from datetime import *\ntimedelta."
        result = get_script_completions(source, 2, len("timedelta."), "test.py", sys_path=[])
        assert result[0].name == "days"
    elif jedi_version[:4] == "0.14":
        source = "from datetime import *\ntimedelta."
        result = get_script_completions(source, 2, len("timedelta."), "test.py", sys_path=[])
        assert result[0].name == "days"

# Generated at 2022-06-14 11:30:12.778032
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import unittest.mock as mock
    from jedi import Interpreter as jediInterpreter
    from jedi import Script as jediScript
    with mock.patch('jedi.Script') as mockScript:
        mockScript.side_effect = jediScript
        with mock.patch('jedi.Interpreter') as mockInterpreter:
            mockInterpreter.side_effect = jediInterpreter
            # Testing with jedi > 0.17
            if hasattr(jediInterpreter, 'completions'):
                completions = get_interpreter_completions('print(a', [])
                assert len(completions) is not 0
                completions = get_interpreter_completions('import my_module', [])
                assert len(completions) is not 0

            #

# Generated at 2022-06-14 11:30:17.685746
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script

    source = """
import os
import sys

os.popen("")

a1 = os.path.abspath("...")
a2 = os.path.abspath("...")
a3 = os.path.abspath("...")
a4 = os.path.abspath("...")
# end of source
"""
    script = Script(source, 1, 4, "")
    completions = script.completions()
    assert len(completions) == 3
    assert "os" in [c.name for c in completions]
    assert "sys" in [c.name for c in completions]

    script = Script(source, 3, 13, "")
    assert len(script.completions()) == 2

# Generated at 2022-06-14 11:30:22.923594
# Unit test for function get_definitions
def test_get_definitions():
    source = "import os\n"
    source += "os.path.isdir("
    result = get_definitions(source, 2, 20, filename='file.py')
    assert len(result) == 1
    assert result[0].line == 11
    assert result[0].module_name == 'os.path'
    assert result[0].description == 'isdir(path) -> bool\n\n'

# Generated at 2022-06-14 11:30:35.613892
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    namespaces = [{
        '__name__': '__main__',
        '__doc__': None,
        '__package__': None,
        '__loader__': None,
        '__spec__': None,
        '__annotations__': {},
        '__builtins__': __builtins__,
        '__file__': 'thonny/ui_utils.py',
        '__cached__': None,
    }]

    if _using_older_jedi(jedi):
        completions = get_interpreter_completions('open', namespaces)

        assert completions
        assert completions[0].name == 'open'

# Generated at 2022-06-14 11:30:45.884849
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api import Script
    from jedi import __version__
    import parso
    # Creating the script for the version used in the IDE.
    if __version__[:4] in ["0.13", "0.14", "0.15", "0.16", "0.17"]:
        script = Script('import unittest')
    else:
        script = Script(code='import unittest', path='')
    
    # Getting the definitions
    dataset = script.infer(line=1, column=11)
    # If no definitions are found, the empty list is returned.
    assert len(dataset) != 0


# Generated at 2022-06-14 11:30:49.788247
# Unit test for function get_definitions
def test_get_definitions():
    if __name__ == "__main__":
        res = get_definitions("import os\nos.path.jo", 2, 6, "test.py")
        for d in res:
            print(d)

# Generated at 2022-06-14 11:30:50.588344
# Unit test for function get_definitions

# Generated at 2022-06-14 11:30:55.870351
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    test_source = """
    def f(x):
        pass
    def g():
        pass
    h = 1
    f.
    """
    completions = list(get_interpreter_completions(test_source, []))
    assert completions[0].name == '__call__'
    assert completions[1].name == '__name__'

# Generated at 2022-06-14 11:31:08.196607
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate.context.module import ModuleContext
    from jedi.evaluate import compiled

    script_code = "aaaa"
    script_name = '<unknown>'
    namespaces = [
        {
            'a': ModuleContext(compiled.CompiledObject(None), 'AAAA', None, None),
            'b': ModuleContext(compiled.CompiledObject(None), 'BBBB', None, None),
        },
        {
            'c': ModuleContext(compiled.CompiledObject(None), 'CCCC', None, None),
        },
    ]
    completions = get_interpreter_completions(script_code, namespaces, [])