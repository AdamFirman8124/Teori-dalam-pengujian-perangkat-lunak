

# Generated at 2022-06-14 11:21:23.007869
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    from unittest import TestCase, main

    class _Tests(TestCase):
        def test_get_script_completions_builtins(self):
            completions = get_script_completions("", 1, 0, "")
            self.assertEqual(len(completions), 9098)

            defs = [c.name for c in completions]
            self.assertIn("BaseException", defs)
            self.assertIn("object", defs)
            self.assertIn("print", defs)
            self.assertIn("dict", defs)
            self.assertIn("list", defs)
            self.assertIn("Text", defs)
            self.assertIn("Thread", defs)
            self.assertIn("quit", defs)

# Generated at 2022-06-14 11:21:29.542644
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    if _using_older_jedi(jedi):
        script = jedi.Interpreter("", [])
        completions = script.completions()
    else:
        script = jedi.Interpreter("")
        completions = script.complete()

    assert len(completions) > 0


# Generated at 2022-06-14 11:21:41.740556
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api.classes import Completion
    from jedi import Script

    src = "import json\njson."
    completions = get_script_completions(src, 2, len(src), "")
    assert completions
    assert all([isinstance(c, Completion) for c in completions])
    assert all([isinstance(c, ThonnyCompletion) for c in completions])

    assert Script(src, 2, len(src), "").completions() == completions



# Generated at 2022-06-14 11:21:50.123372
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.interpreter import Interpreter
    from jedi import settings
    settings.additional_dynamic_modules = ["win32com"]
    interpreter = Interpreter("import win32com.client; win32com.client.gen")
    completions = interpreter.completions()
    # jedi.show_api(completions)
    assert [c.name for c in completions] == ['Dispatch', 'gencache', 'GetEvents', 'makepy']



# Generated at 2022-06-14 11:21:51.781194
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:21:59.899850
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    if _using_older_jedi(jedi):
        try:
            # The naming convention for the variable is not used elsewhere
            # But it's easier to understand _0.17_module_name is from jedi 0.17
            # and _0.18_module_name is from jedi 0.18
            _0_17_module_name = "subprocess"
            _0_18_module_name = "subproces"
            _0_17_module = __import__(_0_17_module_name)
            _0_18_module = __import__(_0_18_module_name)
        except ImportError:
            # No subprocess module
            # This test is not runnable
            return

# Generated at 2022-06-14 11:22:04.329741
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("import sys\nsys.", 1, 5, '')
    assert len(completions) == 1
    assert completions[0].name == "sys"
    assert completions[0].complete == "sys"
    assert completions[0].type is not None

# Generated at 2022-06-14 11:22:13.145312
# Unit test for function get_definitions
def test_get_definitions():
    from types import FunctionType
    from typing import List
    from test.test_jedi_integration import _create_test_cases
    _test_cases = _create_test_cases("get_definitions")
    for test_case in _test_cases:
        location = test_case["location"]
        result = get_definitions(location["source"], location["row"], location["column"], location["path"])
        assert isinstance(result, List), "Result must be list for test case '{}'".format(test_case["name"])
        for pos, expected_result in enumerate(test_case["expected_result"]):
            assert isinstance(result[pos], FunctionType), "Must be of type FunctionType"

# Generated at 2022-06-14 11:22:21.497965
# Unit test for function get_definitions
def test_get_definitions():
    from parso.python.tree import Function, Class
    definitions = get_definitions("def do_it(): pass\n\ndo_it()", 1, 8, "main.py")
    assert len(definitions) == 1
    assert isinstance(definitions[0].parent, (Function, Class))
    assert definitions[0].name == "do_it"
    assert definitions[0].module_name == "main"
    assert definitions[0].line == 0
    assert definitions[0].column == 4

# Generated at 2022-06-14 11:22:32.349228
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import parso

    # Create interpreter
    code = "a = 3\nb = [1, 2, 3]\nc = b[2]\n"
    namespaces = [{"a": 3, "b": [1, 2, 3]}]
    interpreter = jedi.Interpreter(code, namespaces)

# Generated at 2022-06-14 11:22:51.845427
# Unit test for function get_definitions
def test_get_definitions():
    import sys
    import os
    import jedi
    
    def check_results(results, result_names):
        names = [x.description.split(' ')[0] for x in results]
        names.sort()
        result_names.sort()
        if names != result_names:
            print('Mismatch in definitions')
            print('Expected:', result_names)
            print('Found:   ', names)
            print('Please report this at https://bitbucket.org/plas/thonny/issues/')
            print('Test directory:', path)
            sys.exit(2)


    path = os.path.dirname(__file__)
    path = os.path.join(path, 'jedi_tests')

# Generated at 2022-06-14 11:22:58.912236
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api import Interpreter

    ns = [{"a": {"b": {"c": 1}}}, {"d": {"e": {"f": 2}}}, {"d": {"e": 3, "x": "value"}}]

    result = get_interpreter_completions("", ns, [])
    assert len(result) == 3, len(result)
    keys = [c["name"] for c in result]
    assert "a" in keys
    assert "d" in keys
    assert "d.e" not in keys

    result = get_interpreter_completions("d.", ns, [])
    assert len(result) == 5
    keys = [c["name"] for c in result]
    assert "e" in keys
    assert "e.f" in keys
    assert "x" in keys



# Generated at 2022-06-14 11:23:12.046885
# Unit test for function get_definitions
def test_get_definitions():
    from jedi import Script
    import unittest.case

    class TestDefinitions(unittest.case.TestCase):
        def setUp(self):
            self.script = None

        def test_goto1(self):
            source = '''def func():
                pass
            func()'''
            self.script = Script(source, 2, len('func'), 'example.py')
            definitions = self.script.goto_definitions()
            self.assertEqual(1, len(definitions))
            self.assertEqual('def func', definitions[0].description)

    suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(TestDefinitions)])
    unittest.TextTestRunner().run(suite)

# Generated at 2022-06-14 11:23:15.235294
# Unit test for function get_script_completions
def test_get_script_completions():
    source = "import os\nos.path"
    print(get_script_completions(source, 1, 10))


if __name__ == "__main__":
    test_get_script_completions()  # pragma: no cover

# Generated at 2022-06-14 11:23:27.473978
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import sys

    source = "import sys; sys."
    namespaces = [{"__name__": "__main__"}]
    # sys_path = ['/Users/armeria/Documents/code/github/thonny/thonny/plugins']
    sys_path = None

    old_path = sys.path

# Generated at 2022-06-14 11:23:31.374932
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import sys\n"
    source += "def f():\n"
    source += "    sys.std"

    completions = get_interpreter_completions(source, [{}])
    assert "stdout" in [c.name for c in completions]
    assert "stdin" in [c.name for c in completions]

# Generated at 2022-06-14 11:23:34.993014
# Unit test for function get_definitions
def test_get_definitions():
    assert get_definitions('import sys\nsys.stdout.write("hello")', 2, 23, "test.py")[0].line == 1

# Generated at 2022-06-14 11:23:45.893833
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter

    completions = get_interpreter_completions('"".', [])
    assert len(completions) > 0
    assert completions[0].name == 'capitalize'

    completions = get_interpreter_completions('"".', [])
    assert len(completions) > 0
    assert completions[0].name == 'capitalize'

    interpreter = Interpreter('help(', [])
    completions = get_interpreter_completions('help(', [])
    assert len(completions) > 0
    assert completions[0].name == 'help'

    completions = get_interpreter_completions('from os import ', [])
    assert len(completions) > 0

# Generated at 2022-06-14 11:23:53.925225
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from textwrap import dedent
    from jedi.api.environment import get_system_environment

    source = dedent(
        """\
    import math
    math.\
    """
    )

    result = get_interpreter_completions(source=source, namespaces=[], sys_path=[])
    assert "acos" in result[0].complete
    assert "abs" in result[1].complete



# Generated at 2022-06-14 11:23:55.714202
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.parser.python import tree


# Generated at 2022-06-14 11:24:17.374030
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:24:25.401345
# Unit test for function get_definitions
def test_get_definitions():
    from parso.python.tree import Function

    defs = get_definitions(
        "import sys\n"
        "s = sys.ex"  # sys.ex will be used for testing
        "\n",
        2,
        13,
        "dummy.py",
    )
    assert len(defs) == 1, defs
    assert isinstance(defs[0], Function), type(defs[0])
    assert defs[0].name == "exit"



# Generated at 2022-06-14 11:24:33.083595
# Unit test for function get_definitions
def test_get_definitions():
    definitions = get_definitions(source="", row=0, column=0, filename="")
    assert len(definitions) > 1000
    assert all(hasattr(d, "description") for d in definitions)
    assert all(hasattr(d, "line") for d in definitions)
    assert all(hasattr(d, "type") for d in definitions)
    assert all(hasattr(d, "module_path") for d in definitions)

# Generated at 2022-06-14 11:24:36.085268
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:24:47.537305
# Unit test for function get_definitions
def test_get_definitions():
    assert len(get_definitions("def func(x):\n    x.foo\n    x.f", 2, 10, "fake_filename")) == 1
    assert len(get_definitions("import random\nrandom.f", 2, 10, "fake_filename")) == 1
    assert len(get_definitions("import random\nrandom.foo", 2, 10, "fake_filename")) == 0
    assert len(get_definitions("import random\nrandom.randint(", 2, 19, "fake_filename")) == 1
    assert len(get_definitions("from random import randint\nrandint(", 2, 10, "fake_filename")) == 1
    assert len(get_definitions("from random import randint", 1, 18, "fake_filename")) == 1

# Generated at 2022-06-14 11:24:58.048715
# Unit test for function get_definitions
def test_get_definitions():

    def _check(source, expected_full_name):
        result = get_definitions(source, row=1, column=1, filename="test.py")
        assert len(result) == 1
        assert result[0].full_name == expected_full_name

    _check("a", "builtins.name")
    _check("a+1", "builtins.int")

    _check("a = 1\na", "builtins.int")
    _check("a = 1.0\na", "builtins.float")
    _check("a = 'a'\na", "builtins.str")

    _check("import module", "module")

    _check("import module.submodule", "module.submodule")
    _check("import module.submodule.name", "module.submodule.name")

    _check

# Generated at 2022-06-14 11:25:01.334209
# Unit test for function get_definitions
def test_get_definitions():
    from unittest import TestCase


# Generated at 2022-06-14 11:25:11.014227
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate.compiled.python_values import PythonModule
    from jedi.evaluate.compiled.builtin_namespace import ModuleNamespace
    from thonny.globals import get_runner
    import sys

    source = "import sys"
    namespaces = [PythonModule(sys_path=[sys.path[0]], full_name=get_runner().get_module_name())]
    completions = get_interpreter_completions(source, namespaces, sys_path=sys.path)
    assert len(completions) > 0
    assert all(c.parent is namespaces[0] for c in completions)
    assert any(isinstance(c.parent, ModuleNamespace) for c in completions)

# Generated at 2022-06-14 11:25:17.750235
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions(
        source="abs",
        row=0,
        column=3,
        filename="testfile.py",
        sys_path=["/some/path"],
    )

    assert len(completions) == 1
    assert completions[0].complete == "abs"



# Generated at 2022-06-14 11:25:26.615175
# Unit test for function get_definitions
def test_get_definitions():
    import os
    module = "test_get_definitions"
    source = "import re\nre.search('')\n"
    filename = module + ".py"
    this_dir = os.path.dirname(__file__)
    path = [os.path.join(this_dir, "../../../thonny/")]
    d = get_definitions(source, 2, 9, filename, path)
    assert len(d) == 1
    assert d[0].module_name == "re"
    assert d[0].line == 0
    assert d[0].column == 0

if __name__ == '__main__':
    test_get_definitions()

# Generated at 2022-06-14 11:25:56.154873
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase
    import sys

    class Test(TestCase):
        def runTest(self):
            # Test older versions of jedi, which have function `Interpreter.completions`
            old_jedi_path = os.path.dirname(sys.executable) + "/lib/python3.6/site-packages/jedi"
            if os.path.exists(old_jedi_path):
                sys.path.append(old_jedi_path)
                import jedi

                self.assertEqual(jedi.__version__, "0.17.2")

                import jedi_utils as jedi_utils_test

                completions = jedi_utils_test.get_interpreter_completions(
                    '"".s', [], sys_path=None
                )

# Generated at 2022-06-14 11:26:10.314393
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import patch
    import jedi

    jedi.__version__ = "0.14"
    assert _using_older_jedi(jedi)
    completions = get_script_completions("import sys", 0, 7, "")
    assert completions == [
        ThonnyCompletion(name="sys", complete="sys", type="module", description="", parent="", full_name="sys")
    ]

    jedi.__version__ = "0.15"
    assert _using_older_jedi(jedi)
    completions = get_script_completions("import sys", 0, 7, "")
    assert completions == [
        ThonnyCompletion(name="sys", complete="sys", type="module", description="", parent="", full_name="sys")
    ]

# Generated at 2022-06-14 11:26:18.097316
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import datetime"
    namespaces = [{}]
    completions = get_interpreter_completions(source, namespaces)
    assert(len(completions) == 2)
    assert(completions[0].name == "datetime")
    assert(completions[1].name == "date")

# Generated at 2022-06-14 11:26:30.879378
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    from jedi.api.environment import InterpreterEnvironment
    from jedi.evaluate.imports import Importer

    def create_script(source, row, column):
        return jedi.Script(source, row, column, "/tmp/test.py")

    def create_interpreter_completions(source, namespaces):
        return InterpreterEnvironment(
            Importer(), source, namespaces
        ).get_completions()

    assert get_script_completions("import ", 0, 7, "/tmp/test.py") == create_script(
        "import ", 0, 7
    ).completions()
    assert get_script_completions("import ", 1, 7, "/tmp/test.py") == []

# Generated at 2022-06-14 11:26:44.500214
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions("def f(par1) : par1 - 1", 0, 0, "") == []
    assert get_script_completions("def f(par1) : par1 - 1", 0, 12, "") == []
    assert get_script_completions("def f(par1) : par1 - 1", 1, 4, "") == [ThonnyCompletion(name='par1=', complete='par1', type='param', description='param', parent=None, full_name='par1')]
    assert get_script_completions("def f(par1) : par1 - 1", 1, 5, "") == [ThonnyCompletion(name='par1=', complete='par1', type='param', description='param', parent=None, full_name='par1')]
   

# Generated at 2022-06-14 11:26:51.527437
# Unit test for function get_definitions
def test_get_definitions():
    import unittest
    import jedi

    class TestScript(unittest.TestCase):
        def test_goto_definitions(self):
            source = "import math\nprint(math.cos(0) + math.sin(0))\n"
            if _using_older_jedi(jedi):
                result = get_definitions(source, 1, 6, "test_goto_definitions.py")
            else:
                result = get_definitions(source, 2, 9, "test_goto_definitions.py")

            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].type, "module")


# Generated at 2022-06-14 11:26:58.683369
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions("print(", [])
    completions = [c.name for c in completions]
    assert "print(" in completions

    completions = get_interpreter_completions("import sys", [])
    completions = [c.name for c in completions]
    assert "sys" in completions



# Generated at 2022-06-14 11:26:59.679126
# Unit test for function get_definitions

# Generated at 2022-06-14 11:27:16.618422
# Unit test for function get_definitions
def test_get_definitions():
    _test_get_definitions(
        source="def goo(x, y=1):\n    pass\ngoo(2, 3)",
        filename="test.py",
        completion_source="go",
        completion_row=1,
        completion_col=4,
        expected_type="definition",
        expected_full_name="goo",
        expected_compile_name="def goo(x, y=1):\n    pass",
    )


# Generated at 2022-06-14 11:27:25.436852
# Unit test for function get_definitions
def test_get_definitions():
    import tempfile
    import os
    import ast
    import jedi
    from thonny.globals import get_workbench
    def test_file():
        _, name = tempfile.mkstemp()
        os.remove(name)
        return name

    def create_file(name, content= "def test(): pass\n"):
        if not os.path.exists(name):
            with open(name, "w") as f:
                f.write(content)

    def clean_file(name):
        if os.path.exists(name):
            os.remove(name)

    def parse_code(code):
        return ast.parse(code).body[0]

    def test_definitions(filename, source, expected_defs):
        file = test_file()
        create_file

# Generated at 2022-06-14 11:28:10.246272
# Unit test for function get_definitions
def test_get_definitions():
    def check(source, expected):
        import jedi

        Script = jedi.Script
        script = Script(source)

        def _check(source, expected, script):
            # Check if all the expected defintions are inferred.
            def_s = sorted(str(definition) for definition in script.goto_definitions())
            assert def_s == sorted(expected), (def_s, expected)

        for i in range(0, len(source)):
            try:
                _check(source[:i], expected, script)
            except jedi.NotFoundError:
                # If a definition is not found, that is not a fail.
                pass

    check('import argparse\nint(7)\nargparse.ArgumentPar', ['int', 'argparse'])



# Generated at 2022-06-14 11:28:18.053405
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.python_shell import PythonShell

    shell = PythonShell(None)
    shell.process = "test"

    sys_path = ["c:\\test\\b"]
    result = list(_get_interpreter_completions("import math\nmath.", [], sys_path))
    assert len(result) > 0
    assert all(["e" in r.name for r in result])



# Generated at 2022-06-14 11:28:29.430902
# Unit test for function get_script_completions
def test_get_script_completions():
    # This may fail when tested outside of Thonny environment
    from thonny import get_workbench
    from thonny.ui_utils import get_source_editor_font
    from thonny.plugins.jedi_support.utils import get_script_completions, ThonnyCompletion
    import tkinter as tk
    import os

    root = tk.Tk()
    root.option_add('*tearOff', False)
    workbench = get_workbench()

    # Start a temporary text editor
    editor = workbench.create_editor_in_container(root)
    editor.text.tag_config("name", font=get_source_editor_font())

    # Load test file

# Generated at 2022-06-14 11:28:38.462135
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    if _using_older_jedi(jedi):
        from jedi.api.classes import Script

        script = Script("import  sys\n sys", 4, 1, "")
        completions = script.completions()
    else:
        from jedi.api.project import Project

        script = jedi.Script("import  sys\n sys", 4, 1, "")
        completions = script.complete(line=4, column=1)
    assert len(completions) == 1
    assert completions[0].name == "sys"

# Generated at 2022-06-14 11:28:50.061875
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from pathlib import Path
    import jedi

    if jedi.__version__[:4] not in ["0.13", "0.14", "0.15", "0.16", "0.17"]:
        return

    old_get_interpreter_completions = jedi.api.interpreter.Script._get_interpreter_completions
    old_get_completions = jedi.api.Script._get_completions
    old_key = "Script._get_completions"
    old_val = getattr(jedi.api.Script, "_get_completions", None)

    jedi.api.Script._get_completions = old_get_completions
    jedi.api.interpreter.Script._get_interpreter_completions = old_get

# Generated at 2022-06-14 11:28:56.415854
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    from jedi.api.project import jedi_definition
    from jedi.parser import ParserSyntaxError
    import sys
    from unittest.case import skip

    sys.path =[]
    result = get_interpreter_completions(source="sin(", namespaces=[{}])
    assert len(result) == 1
    assert result[0].complete == "sin("
    assert result[0].type == "function"
    assert result[0].name == "sin"

    source = "global x; x = 5"
    result = get_interpreter_completions(source=source, namespaces=[{}])
    assert len(result) == 0

    source = "x = 5"

# Generated at 2022-06-14 11:29:09.546920
# Unit test for function get_definitions
def test_get_definitions():
    filename = "/home/user/module.py"
    source1 = "import module\nmodule.something"
    source2 = "import module\nmodule2.someotherthing"
    source3 = "def a():\n  x = 5\n  x = 6"
    source4 = "import module\nmodule.something.blabla\nmodule2.someotherthing.bla"

    if _using_older_jedi(_):
        expected_result1 = [Definition(module, 1, len("module."), filename, None)]
        expected_result2 = [Definition(module, 1, len("module2."), filename, None)]
        expected_result3 = [Definition(int, 1, len("x"), filename, None)]

# Generated at 2022-06-14 11:29:22.167256
# Unit test for function get_script_completions
def test_get_script_completions():
    old_get_script_completions = get_script_completions

    def get_script_completions(source, row, column, filename, sys_path=None):
        return old_get_script_completions(source, row, column, filename, sys_path=sys_path)

    from jedi.api.classes import Script, Interpreter

    # 0.17

# Generated at 2022-06-14 11:29:34.860815
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.interpreter import Interpreter
    #from jedi.evaluate import imports
    import unittest.mock
    import jedi
    import sys

    with unittest.mock.patch.object(jedi, 'api', autospec=True) as api_mock:
        #call the function under test
        get_interpreter_completions('sys', [dict(a=1)])
        #ensure that this will be called in case of jedi <= 0.16.0
        api_mock.Interpreter.assert_any_call('sys', [dict(a=1)])
        #ensure that this will be called in case of jedi > 0.16.0

# Generated at 2022-06-14 11:29:36.547066
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny import get_completions
