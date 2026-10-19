

# Generated at 2022-06-14 11:21:25.785928
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    text = "def f(a): pass\nf("
    completions = get_interpreter_completions(text, [{}])
    assert completions[0].name == "a="

# Generated at 2022-06-14 11:21:37.055908
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Test simple import
    code = "import sys"
    completions = get_interpreter_completions(code, [])
    assert len(completions) == 1
    assert completions[0]["name"] == "sys"

    # Test simple variable
    code = "x = 10"
    completions = get_interpreter_completions(code, [])
    assert len(completions) == 1
    assert completions[0]["name"] == "x"

    # Test instance variable
    code = "x = 10\n" * 5 + "x"
    completions = get_interpreter_completions(code, [])
    assert len(completions) == 1
    assert completions[0]["name"] == "x"

    # Test import and variable

# Generated at 2022-06-14 11:21:43.408000
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi.api

    if _using_older_jedi(jedi.api):
        print("Using pre-0.18 jedi")
        assert get_script_completions("", 0, 0, "")[0].name == "abs"
        assert get_script_completions("1 + abs(", 4, 7, "")[0].name == "abs"
        assert get_script_completions("", 0, 0, "", sys_path=["/home/user/testproject"])[0].name == "abs"
        assert get_script_completions("1 + abs(", 4, 7, "", sys_path=["/home/user/testproject"])[0].name == "abs"

# Generated at 2022-06-14 11:21:49.136010
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from thonny.shell import jedi_utils
    from thonny.languages import tr

    def get_completions(code_lines, cursor_pos, namespaces):
        code = "\n".join(code_lines)
        line = len(code_lines)
        column = len(code_lines[-1])+1
        return jedi_utils.get_interpreter_completions(
            code, namespaces, cursor_pos=cursor_pos, line=line, column=column
        )

    def assert_equal_completions(expected_completions, actual_completions):
        expected_names = set([c.name for c in expected_completions])
        actual_names = set([c.name for c in actual_completions])

# Generated at 2022-06-14 11:21:56.094927
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions(
        "import sys; sys.stdout.write", row=0, column=28, filename="test.py"
    )
    assert "write" in [c.name for c in completions]
    assert "seek" not in [c.name for c in completions]

# Generated at 2022-06-14 11:22:09.008960
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    from jedi.evaluate.names import ValueNameWrapper
    import parso
    import ast

    def list_completions(source):
        completions = get_interpreter_completions(source, [])
        return list(set([c["name"] for c in completions]))

    source = "import sys"
    completions = list_completions(source)
    assert "sys" in completions

    source = "import sys\ndef f(a=sys.modules):\n    pass"
    completions = list_completions(source)
    assert "sys" in completions

    # TODO: fix, current version of jedi does not support this
    #source = "import sys\nimport os\ndef f(a=sys.path):\n    pass\ndef f2

# Generated at 2022-06-14 11:22:14.958101
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = 'print("He"\n'
    namespaces = [{"__builtins__": __builtins__}]
    completions = get_interpreter_completions(source, namespaces)
    assert completions[0].name == "Hello"
    assert completions[0].complete == "llo"

# Generated at 2022-06-14 11:22:21.301850
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import sys
    import os
    import json

    from test.config import test_dir
    from thonny.globals import get_workbench

    sys.path = [os.path.join(test_dir, "lib")]
    line_no = 2
    col = 6
    interpreter_code = "def f(x):"

    completions = get_interpreter_completions(
        interpreter_code, [], sys_path=get_workbench().get_editor_notebook().get_sys_path()
    )
    assert len(completions) > 0
    completion_dict = dict([(x["name"], x) for x in completions])

    assert "f" in completion_dict
    assert completion_dict["f"]["line"] == line_no

# Generated at 2022-06-14 11:22:24.773753
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("""
a = "Hello "
b = "world"
a + b.""", 4, 1, "test.py")
    assert len(completions) == 1
    assert completions[0].complete == "str"


# Generated at 2022-06-14 11:22:35.169487
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import tempfile, os, shutil
    import io
    import unittest
    import sys
    import importlib
    import traceback

    class GetInterpreterCompletionsTests(unittest.TestCase):

        def setUp(self):
            tmp_dir_path = tempfile.mkdtemp()
            self.addCleanup(shutil.rmtree, tmp_dir_path, ignore_errors=True)

            self.sys_path = [tmp_dir_path]
            self.sys_path.extend(sys.path)

            self.test_subdir_path = tmp_dir_path + "/test_module"
            os.mkdir(self.test_subdir_path)

            test_module_path = self.test_subdir_path + "/test_module.py"
            test_

# Generated at 2022-06-14 11:22:52.327609
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock

    def _make_completion(
        name: str,
        complete: str,
        type=None,
        description=None,
        parent=None,
        full_name=None,
    ):
        return Mock(
            name=name,
            complete=complete,
            type=type,
            description=description,
            parent=parent,
            full_name=full_name,
        )

    def _add_completions_result(jedi_mock, completions):
        script_mock = Mock(return_value=None)
        script_mock.completions.return_value = completions
        jedi_mock.Script.return_value = script_mock

    # NB!
    # jedi 0.17.x contains functions from jedi

# Generated at 2022-06-14 11:22:55.764663
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("\"".encode(), 1, 2)
    assert len(completions) > 0
    assert (
        all(isinstance(c, ThonnyCompletion) for c in completions)
    )  # TODO: check type jedi.api_classes.Completion



# Generated at 2022-06-14 11:23:09.509646
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    from unittest import TestCase

    sample = """
    from math import sin, cos
    from math import tan, sqrt as root
    from abc import A, B, C, D

    """

    namespaces = [{"x": 42}, {"y": 3.14}]

    if _using_older_jedi(jedi):
        script = jedi.Interpreter(sample, namespaces)
        completions = script.completions()
    else:
        script = jedi.Interpreter(source=sample, namespaces=namespaces)
        completions = script.complete()

    assert len(completions) == 5, "there are only five modules imported"

    for completion in completions:
        assert completion.name == "sin" or completion.name == "cos"
        assert completion.complete

# Generated at 2022-06-14 11:23:15.523206
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import sys

    # Generating example code in current interpreter
    code = "def f():pass\n"
    exec(code)

    completions = get_interpreter_completions(
        code, [{"vars": dir(sys)}, {"vars": dir()}]
    )
    assert "f" in [c.name for c in completions]
    assert "print" in [c.name for c in completions]

# Generated at 2022-06-14 11:23:23.872505
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.evaluate.cache import memoize_default

    assert _using_older_jedi(memoize_default)
    completions = get_script_completions(
        source="""
c = range(
""",
        row=1,
        column=11,
        filename="Hello world.py",
    )
    assert len(completions) > 0
    assert completions[0].complete == "range(stop, start=0, step=1,"

    assert _using_older_jedi(parse_source)

# Generated at 2022-06-14 11:23:33.110455
# Unit test for function get_definitions
def test_get_definitions():
    names = "from tkinter import *"
    source = names + """\ndef f():\n    Button["""
    expected_line = names.count("\n") + 3
    expected_column = len(source.splitlines()[-1]) - 1
    defs = get_definitions(source, len(source.splitlines()), len(source.splitlines()[-1]), "test.py")
    got_line = defs[0].line
    got_column = defs[0].column
    assert got_line == expected_line
    assert got_column == expected_column


if __name__ == "__main__":
    test_get_definitions()
    print("OK")

# Generated at 2022-06-14 11:23:45.066263
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    # Saving the old version
    old_version = jedi.__version__

    # Setting the version to 0.16
    jedi.__version__ = "0.16.0"
    # Checking that get_script_completions is returning the right version
    sources = [
        "",
        "a = str.cap",
        "import os\nos.path.",
        "import os.path\nos.path.",
    ]
    answers = [
        ["str"],
        ["capitalize", "center", "capitalize"],
        ["curdir", "pardir", "sep"],
        ["curdir", "pardir", "sep"],
    ]

# Generated at 2022-06-14 11:23:56.927469
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.interpreter import Interpreter
    from jedi.parser import ParserSyntaxError
    from unittest.mock import MagicMock

    spy = MagicMock()
    old_init = Interpreter.__init__
    Interpreter.__init__ = lambda *args, **kwargs: spy(args, kwargs)
    get_interpreter_completions("import fob", [], None)
    assert spy.called
    Interpreter.__init__ = old_init

    with pytest.raises(ParserSyntaxError):
        get_interpreter_completions("a b", [], None)

# Generated at 2022-06-14 11:24:06.020905
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:24:17.869446
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    import itertools
    import unittest.mock as mock
    # Sort the completions in order to get predictable results.
    # See https://github.com/davidhalter/jedi/issues/1735
    # We use string.ascii_lowercase.index to sort the results
    # Therefore, we need to mock this method to return a predictable ordering
    # And we need to do this before the jedi import, because jedi's import
    # string may pick up mock.ascii_lowercase

    before_jedi_import = itertools.count()
    with mock.patch("string.ascii_lowercase.index") as mock_index:
        mock_index.side_effect = lambda x: next(before_jedi_import)

        import thonny

# Generated at 2022-06-14 11:24:34.935401
# Unit test for function get_definitions
def test_get_definitions():
    import sys
    import jedi
    import os.path

    # Load some random module. Because of the way the main function of jedi works, we need to make sure that
    # that directory is in sys.path
    sys.path.append(os.path.dirname(os.path.abspath(jedi.__file__)))
    source = 'from jedi import Script\nScript("", 0, 0)\n'
    definitions = get_definitions(source, 2, 10, "")
    assert len(definitions) == 1
    assert definitions[0].name == "Script"


# Generated at 2022-06-14 11:24:46.794263
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    assert (
        get_script_completions(
            "import sys; sys.pa", 2, 14, filename="/tmp/untitled", sys_path=["./"]
        )[1].name
        == "path"
    )
    assert (
        get_script_completions(
            "import sys; sys.pa", 2, 14, filename="/tmp/untitled", sys_path=["./"]
        )[1].complete
        == "path="
    )
    assert (
        get_script_completions(
            "import sys; sys.pa", 2, 14, filename="/tmp/untitled", sys_path=["./"]
        )[1].type
        == "attribute"
    )

# Generated at 2022-06-14 11:24:54.092068
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "a = 1;a"
    parser = parse_source(source)
    namespaces = [{"a":parser.get_leaf_for_position((2, 0)).parent.children[0].value}]
    completions = get_interpreter_completions(source, namespaces)
    assert completions[0].name == "a="
    assert completions[0].complete == "a"


# Generated at 2022-06-14 11:24:58.454064
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    imports = [{'a': 'a_module'}]
    completions = get_interpreter_completions("a.a_mod", imports)
    assert completions[0].name == 'a_module'

# Generated at 2022-06-14 11:25:10.297958
# Unit test for function get_definitions
def test_get_definitions():
    def check(code, expected_result = None, column = None, row = None, filename = None):
        from thonny.jedi_utils import ThonnyCompletion, get_definitions

        definitions = get_definitions(code, row, column, filename)
        if expected_result is None:
            assert len(definitions) == 1
            assert isinstance(definitions[0], ThonnyCompletion)
        else:
            assert len(definitions) == len(expected_result)
            for expected_res in expected_result:
                is_found = False
                for defi in definitions:
                    if defi.complete == expected_res:
                        is_found = True
                        break
                assert is_found, "Could not find expected completion: " + expected_res

    check("y = x", "x")
    check

# Generated at 2022-06-14 11:25:23.810074
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # check if we have to fall back to old jedi
    import jedi
    if _using_older_jedi(jedi):
        logger.debug("jedi old version found, need to use the old fallback")
        return True

    # check if we can use the new jedi.
    import _ast
    import importlib.util

    # create dummy module
    module_name = "_test_jedi_overlay_module"
    info = importlib.util.spec_from_loader(module_name, importlib.util.SourceFileLoader(module_name, "/tmp/test_jedi_overlay_module.py"))
    f = info.loader.get_filename(module_name)
    importlib.util.module_from_spec(info)
    info.loader.exec_module(f)
    # create dummy ast

# Generated at 2022-06-14 11:25:25.367171
# Unit test for function get_definitions
def test_get_definitions():
    print(get_definitions("a = 3; a",1,3,"test.py"))

# Generated at 2022-06-14 11:25:27.560176
# Unit test for function get_script_completions
def test_get_script_completions():
    print(get_script_completions("l", 0, 0, 1, [])[0]["type"])

# Generated at 2022-06-14 11:25:28.385164
# Unit test for function get_definitions

# Generated at 2022-06-14 11:25:31.949669
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate import Interpreter
    from jedi.parser_utils import get_root_scope


# Generated at 2022-06-14 11:26:00.203504
# Unit test for function get_script_completions
def test_get_script_completions():
    print("Testing get_script_completions...", end="")
    source = """x = "Lorem ipsum dolor"
        
    if True:
        x = "Lorem ipsum dolor"
    """
    completions = get_script_completions(source, 1, 0, "example.py")
    assert len(completions) == 1
    completion = completions[0]
    assert completion["name"] == "True"
    assert completion["complete"] == "True"
    assert completion["type"] == "statement"
    assert completion["description"] == "True"
    assert completion["parent"] == "bool"
    assert completion["full_name"] == "True"
    print("OK")



# Generated at 2022-06-14 11:26:08.741210
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert len(get_interpreter_completions("", [{}], [__file__])) > 0
    assert len(get_interpreter_completions("3", [{}], [__file__])) == 0
    assert len(get_interpreter_completions("a.", [{}], [__file__])) > 0
    assert len(get_interpreter_completions("a.co", [{}], [__file__])) > 0

# Generated at 2022-06-14 11:26:09.905190
# Unit test for function get_definitions

# Generated at 2022-06-14 11:26:20.403928
# Unit test for function get_script_completions
def test_get_script_completions():
    assert isinstance(get_script_completions("import sys\nsys", 0, 0, ""), list)
    #assert not get_script_completions("import sys\nsys.exi", 0, 0, "")
    assert isinstance(get_script_completions("import sys\nsys.path", 0, 0, ""), list)
    #assert not get_script_completions("import sys\nsys.path.", 0, 0, "")
    assert not get_script_completions("i", 0, 0, "")
    assert not get_script_completions("", 0, 0, "")

# Generated at 2022-06-14 11:26:32.103269
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase

    class MyTestCase(TestCase):
        def run_assertions(self, result, ok_names, not_ok_names):
            for name in ok_names:
                if name not in result:
                    raise AssertionError(
                        "Expected " + name + " to be in " + str(result)
                    )
            for name in not_ok_names:
                if name in result:
                    raise AssertionError(
                        "Didn't expect " + name + " to be in " + str(result)
                    )

    import jedi

    jedi.__version__ = "0.13.3"
    source = "def foo(): pass\n"
    namespaces = [{"foo": foo}]

# Generated at 2022-06-14 11:26:35.961757
# Unit test for function get_definitions
def test_get_definitions():
    """
    >>> from jedi.api.environment import get_default_environment
    >>> from jedi.api.project import Project

    >>> env = get_default_environment()
    >>> project = Project(env)
    >>> script = project.get_script('import numpy as np\\ndataset = np.arange(5)')
    """
    pass
    # return script.get_definitions() # jedi 0.16 or earlier



# Generated at 2022-06-14 11:26:44.556484
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.globals import get_workbench

    get_workbench().set_option("editor.python_version", "3.5")
    source = """
import dbm
dbm.os
"""
    completions = get_script_completions(
        source=source, row=2, column=18, filename="t.py"
    )
    assert len(completions) == 2
    assert completions[0].name == "open"
    assert completions[1].name == "whichdb"

# Generated at 2022-06-14 11:26:50.732575
# Unit test for function get_definitions
def test_get_definitions():
    results = get_definitions('a = [1, 2, 3]\na[1]', 3, 1, "/tmp/test.py")
    if not results:
        raise AssertionError("Expected to find definition for a[1]")
    defs = results[0]
    if defs.line != 1 or defs.column + 1 != 5:
        from jedi.api.classes import Definition
        raise AssertionError("Expected definition to be 'a[1]' at line 1 and column 5, but got: %s" % Definition.to_string(defs))

if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 11:26:55.435305
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script

    source = "import requests\nrequests.po"
    completions = Script(source, 1, 16).completions()
    assert len(completions) > 0

# Generated at 2022-06-14 11:26:56.670586
# Unit test for function get_definitions

# Generated at 2022-06-14 11:27:51.383753
# Unit test for function get_definitions
def test_get_definitions():
    assert sys.executable is not None
    namespaces = [
        {"builtins": __builtins__, "__name__": "__main__"},
        {"__name__": "thonny.jediutils"},
        {"__name__": "thonny.workqueue"},
    ]


# Generated at 2022-06-14 11:28:00.139793
# Unit test for function get_definitions
def test_get_definitions():
    import jedi
    assert jedi.__version__[:4] == "0.18"
    from jedi.api.classes import Definition
    source = """import os, sys\n"""
    definitions = get_definitions(source, 1, 0, "test.py")
    assert len(definitions) == 2
    assert set(d.module_name for d in definitions) == set(["os", "sys"])
    assert all(isinstance(d, Definition) for d in definitions)

# Generated at 2022-06-14 11:28:11.918873
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api.classes import FunctionDefinition, Namespace
    from jedi import Interpreter

    source = """
    def my_func(a, b):
        pass

    my_func(
    """
    definitions = get_definitions(source, 4, 0, "")
    assert len(definitions) == 1
    assert isinstance(definitions[0], FunctionDefinition)
    assert definitions[0].name == "my_func"
    assert definitions[0].module_name == "test"
    assert definitions[0].description == "my_func(a, b)"

    source = """
    from os import path as Path
    Path.__getitem__
    """
    definitions = get_definitions(source, 3, 5, "")
    assert len(definitions) == 1

# Generated at 2022-06-14 11:28:26.749734
# Unit test for function get_script_completions
def test_get_script_completions():
    assert get_script_completions(
        "import datetim", 1, 1, "no_matter"
    ) == [ThonnyCompletion(name='datetime', complete='datetime', type='module', description='', parent=None, full_name='datetime')]
    assert get_script_completions(
        "import datetime\ndatetime.", 1, 1, "no_matter"
    ) == [ThonnyCompletion(name='MAXYEAR', complete='MAXYEAR', type='int', description='', parent='datetime', full_name='datetime.MAXYEAR')]

# Generated at 2022-06-14 11:28:35.336032
# Unit test for function get_definitions
def test_get_definitions():
    import unittest.mock

    source = "from math import *\ndef f():\n    return [ceil, floor]"

    defs = get_definitions(
        source, 3, 9, unittest.mock.sentinel.filename
    )  # ceil and floor are both functions
    assert isinstance(defs[0], ThonnyCompletion)
    assert defs[0].name == "ceil"
    assert defs[1].name == "floor"
    assert len(defs) == 2



# Generated at 2022-06-14 11:28:43.031308
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # Old jedi
    completions = get_interpreter_completions("print", [{}])
    assert [c.name for c in completions] == ["print"]
    assert [c.type for c in completions] == ["function"]

    # New Jedi
    completions2 = get_interpreter_completions("print", [{}], sys_path=["/usr/local/lib/python3.7"])
    assert [c.name for c in completions2] == ["print"]
    assert [c.type for c in completions2] == ["function"]


# Generated at 2022-06-14 11:28:55.560741
# Unit test for function get_definitions
def test_get_definitions():
    import unittest
    import unittest.mock

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.patcher = unittest.mock.patch("thonny.jediutils.get_definitions")
            self.mock_method = self.patcher.start()

        def tearDown(self):
            self.patcher.stop()

        def test_get_definitions_use_path(self):
            get_definitions(
                source="test = 1",
                row=0,
                column=8,
                filename="test",
            )
            self.mock_method.assert_called_once_with(
                source="test = 1", row=0, column=8, filename="test"
            )


# Generated at 2022-06-14 11:29:08.984570
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock
    import jedi

    class Completion:
        def __init__(self):
            self.name = ""
            self.complete = ""
            self.type = ""
            self.description = ""
            self.parent = ""
            self.full_name = ""

    class Script:
        def __init__(self):
            self.completions = Mock(return_value=[Completion()])

    # jedi < 0.18
    jedi.Script = Mock(return_value=Script())
    completions = get_script_completions("", 0, 0, "")
    assert completions
    assert completions[0].complete != completions[0].name

    # jedi >= 0.18
    jedi.Script = Mock(return_value=Script())

# Generated at 2022-06-14 11:29:21.703247
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest import TestCase

    class MyTest(TestCase):
        def test_completions(self):
            from thonny.jedi_utils import get_interpreter_completions

            completions = get_interpreter_completions("import sys\n" "sys.", sys_path=["."])
            self.assertEqual(29, len(completions))  # if this fails, then jedi.sys_path has changed
            self.assertEqual("sys.__stdout__", completions[0].full_name)
            self.assertEqual("sys.stdout=", completions[0].complete)

    test = MyTest("test_completions")
    test.setUp()
    test.test_completions()

# Generated at 2022-06-14 11:29:34.590525
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = []
    source.append('import os')
    source.append('import datetime')
    source.append('os.name')
    source.append('os.path.abspath(os.path.join("home", "user", "gg"))')
    source.append('os.path.abspath(os.path.join("home", "user", "gg"))')
    namespaces = [{'os': None}]
    sys_path = []
    completions = get_interpreter_completions('\n'.join(source), namespaces, sys_path)
    # only completions from the last line
    assert len(completions) == 9

    completions = get_interpreter_completions('\n'.join(source[:-2]), namespaces, sys_path)
    # completions from

# Generated at 2022-06-14 11:30:23.531073
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter

    source = """import sys
sys.
"""
    script = Interpreter(source, [locals()])
    completions = get_interpreter_completions(source, [locals()])

    assert len(completions) == len(script.completions())
    assert set(c.name for c in completions) == set(c.name for c in script.completions())

# Generated at 2022-06-14 11:30:24.971157
# Unit test for function get_script_completions

# Generated at 2022-06-14 11:30:37.645424
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api.evaluate import Evaluator

    # We need to wrap the function in our version of jedi to use the current jedi version
    import parso
    from jedi.parser_utils import get_statement_of_position as _wrapped_get_statement_of_position

    def get_statement_of_position(node, pos):
        # Reconstruct the same code as the original get_statement_of_position to ensure that
        # the new code produces the same completions
        # https://github.com/thonny/thonny/pull/1092#issuecomment-659629003

        def get_statement_of_position_legacy(node, pos):
            import parso.python.tree


# Generated at 2022-06-14 11:30:50.014197
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.helpers import get_names_of_object
    import jedi
    import time

    start_time = time.time()
    interpreter = jedi.Interpreter("import math; math.sin", [{"math" : math}])
    interpreter_completions = get_interpreter_completions("import math; math.sin", [{"math" : math}])
    interpreter_completions = [completion[0] for completion in interpreter_completions]
    jedi_completions = [completion.name for completion in interpreter.completions()]
    assert set(jedi_completions) == set(interpreter_completions) # No need to order
    print("Test execution time: " + str(time.time() - start_time))

# Generated at 2022-06-14 11:30:55.831864
# Unit test for function get_definitions

# Generated at 2022-06-14 11:31:02.837419
# Unit test for function get_script_completions
def test_get_script_completions():
    source = """
import sys

sys.
"""
    print(get_script_completions(source, 4, 5, '<stdin>'))
    assert len(get_script_completions(source, 4, 5, '<stdin>')) > 0

if __name__ == "__main__":
    test_get_script_completions()

# Generated at 2022-06-14 11:31:09.106005
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    try:
        get_script_completions("import sys\n", 1, 10, "")
    except Exception as e:
        if (
            "Error while trying to parse file" in str(e)
            and not _using_older_jedi(jedi)
            or "Please include it in your Python version." in str(e)
            and _using_older_jedi(jedi)
        ):
            pass
        else:
            raise



# Generated at 2022-06-14 11:31:13.197674
# Unit test for function get_definitions
def test_get_definitions():
    from jedi import __version__ as jedi_version
    from parso import __version__ as parso_version

    if not jedi_version.startswith("0.1") or parso_version.startswith("0.8"):
        return
