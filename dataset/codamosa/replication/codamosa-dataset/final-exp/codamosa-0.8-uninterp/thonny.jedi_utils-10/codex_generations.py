

# Generated at 2022-06-14 11:21:38.091275
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions("import io; io.", [])[0]["name"] == "StringIO"

# Generated at 2022-06-14 11:21:50.995245
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    from jedi.api import classes
    from jedi.api.helpers import get_script

    class FakeNameCompletion(classes.NameDefinition):
        def __init__(self, name, description, type, parent, full_name):
            self.name = name
            self.description = description
            self.type = type
            self.parent = parent
            self.full_name = full_name

    class FakeScriptCompletion(object):
        def __init__(self, completions):
            self.completions = completions

        def __iter__(self):
            return iter(self.completions)

    class FakeNameDefinition(object):
        def __init__(self, name, description, type, parent, full_name):
            self.name = name
            self.description = description
            self

# Generated at 2022-06-14 11:21:54.000787
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    sys.path.insert(0, "/myhome/myproject")
    source = "import d"
    completions = get_script_completions(source, 0, len(source), "/myhome/myproject/x.py")
    assert len(completions) == 1


# Generated at 2022-06-14 11:22:04.689228
# Unit test for function get_script_completions
def test_get_script_completions():
    source = """
    
    def func():
        import re
        re.p
        """
    filename = "script.py"
    script_completions = get_script_completions(
        source, row=3, column=9, filename=filename, sys_path=[filename]
    )
    assert len(script_completions) == 1
    assert script_completions[0].name == "escape"
    assert script_completions[0].complete == "escape"

# Generated at 2022-06-14 11:22:11.987810
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    jedi_version = jedi.__version__
    # Hardcode here the responses from jedi from different versions

# Generated at 2022-06-14 11:22:24.326604
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:22:33.477806
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    namespace = [
        {
            "name": "__builtins__",
            "type": "module",
            "isinstance": True,
            "getattr": True,
            "safe_value": True,
            "value": "builtins",
            "is_namespace": True,
            "children": [
                {"name": "None", "type": "NoneType", "isinstance": True, "safe_value": False}
            ],
        }
    ]
    source = "def f():\n    pass\nf(None"
    completions = get_interpreter_completions(source, namespace)
    assert len(completions) == 1

# Generated at 2022-06-14 11:22:43.370604
# Unit test for function get_script_completions
def test_get_script_completions():
    comp = get_script_completions(
        "pass",
        1,
        4,
        filename="<test_get_script_completions>",
        sys_path=["/my/home/dir"],
    )
    assert len(comp) > 0


if __name__ == "__main__":
    # test_get_script_completions()
    x = get_script_completions(
        "os.listdir", 2, 5, "<test_get_script_completions>", sys_path=["/home/pontus/github/jedi/jedi"]
    )
    print(x)

# Generated at 2022-06-14 11:22:52.972011
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    assert _using_older_jedi(jedi)
    import textwrap

    source = textwrap.dedent(
        """\
    class Foo():
        def bar(self, arg):
            arg.
    """
    )
    completions = get_script_completions(
        source, row=4, column=13, filename="test_get_script_completions.py"
    )
    assert len(completions) > 0
    for completion in completions:
        assert completion.name in ("upper", "lower", "startswith", "endswith", "replace")

# Generated at 2022-06-14 11:23:00.405018
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    from unittest.mock import Mock

    jedi.Interpreter = Mock()
    jedi.Interpreter.infer = Mock()

    class Completion:
        name = "name"
        complete = "complete"
        type = "type"
        description = "description"
        parent = "parent"
        full_name = "full_name"

    jedi.Interpreter.infer.return_value = [Completion()]
    result = get_interpreter_completions(None, None, None)

    assert result[0].name == "name"
    assert result[0].complete == "complete"
    assert result[0].type == "type"
    assert result[0].description == "description"
    assert result[0].parent == "parent"

# Generated at 2022-06-14 11:23:28.606497
# Unit test for function get_definitions
def test_get_definitions():
    import jedi

    if not _using_older_jedi(jedi):
        assert get_definitions(source="from math i", row=1, column=7, filename=__file__)


if __name__ == "__main__":
    test_get_definitions()

# Generated at 2022-06-14 11:23:41.953867
# Unit test for function get_definitions
def test_get_definitions():
    import sys
    import jedi
    from jedi.parser_utils import get_statement_of_position
    sys.path.append(".")
    # Make sure that jedi.__version__ matches the order of unit test cases
    assert(jedi.__version__ == "0.17.1")
    source = "from my_module import a, b\n"
    source += "a=1\na=2\n"
    source += "def func():\n return 0\n"
    source += "class MyClass:\n def __init__(self):\n self.a=0\n"
    source += "def my_func(a,b,c):\n return 0\n"

    source += "def func2():\n return 0\n"
    source += "func2()\n"

# Generated at 2022-06-14 11:23:52.070502
# Unit test for function get_definitions
def test_get_definitions():
    def check(source, row, column, filename, expected):
        result = get_definitions(source, row, column, filename)
        actual = [x.line for x in result]
        assert actual == expected, repr([source, row, column, filename, expected, result])

    check(
        "r  = R\\\nclass A: pass",
        1,
        3,
        "foo.py",
        [1, 1],
    )

    # https://bitbucket.org/plas/thonny/issues/386/debugger-show-local-variables-does-not-work

# Generated at 2022-06-14 11:24:01.417161
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import Mock

    def test_case(code: str, row: int, column: int, expected: list):
        ns = [{"x": Mock()}]
        completions = get_interpreter_completions(code, ns, [])

        assert [c.name for c in completions] == expected

    test_case('x.spli', 4, 11, ["split"])
    test_case('x.split', 4, 12, ["split"])
    test_case('x.split(', 4, 13, ["split"])

# Generated at 2022-06-14 11:24:02.563783
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # TODO: implement this
    pass

# Generated at 2022-06-14 11:24:05.838979
# Unit test for function get_script_completions
def test_get_script_completions():
    assert len(get_script_completions("import math;math.", 0, 14, "test.py")) > 0


# Generated at 2022-06-14 11:24:17.774951
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "backend"))
    from _utils import substring_matching
    from jedi_utils import get_script_completions

    source = """import subprocess

subprocess.Popen(["ls"], self.get_popen_kwargs({"pipeline_logging_path": self.pipeline_logging_path}))
"""
    completions = get_script_completions(source, 2, 28, "test.py")
    completions = substring_matching.apply(completions, "se")
    assert len(completions) == 1
    assert completions[0].name == "self"
    assert completions[0].complete == "self."

# Generated at 2022-06-14 11:24:23.975325
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import tkinter"
    namespaces = []
    sys_path = ['.']
    completions = get_interpreter_completions(source,namespaces,sys_path)
    assert(len(completions) == 1)
    assert(completions[0].name == 'tkinter')
    assert(completions[0].complete == 'tkinter')
    assert(completions[0].type == 'import')
    assert(completions[0].description == 'tkinter')
    assert(completions[0].parent == None)
    assert(completions[0].full_name == None)

# Generated at 2022-06-14 11:24:35.931871
# Unit test for function get_script_completions
def test_get_script_completions():
    import sys
    # In older version of jedi, completing "pri" in a print statement will return
    # "print" and "private", but in the newer ones it won't return the "private"
    # In older version of jedi, completing "pri" in a
    # "with open('test.txt') as f:"
    # will return "print" and "private", but in the newer ones it won't return the "private"
    # In older version of jedi, completing "pri" in a
    # "import math"
    # will return "print" and "private", but in the newer ones it won't return the "private"

# Generated at 2022-06-14 11:24:41.479120
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.api.classes import Completion
    from parso.python import tree

    def check_result(source, namespaces, expected_completions):

        def fake_evaluator(source, namespaces, sys_path=None):
            if sys_path is not None:
                raise Exception("Unexpected sys_path")

            # This is a very incomplete substitute for jedi.evaluate.Evaluator.
            # We only implement those things which are used by get_interpreter_completions.

            class V:
                def __init__(self, name):
                    self.name = name

                def py__class__(self):
                    if self.name == "None":
                        return V("NoneType")
                    else:
                        return V("Type")


# Generated at 2022-06-14 11:25:12.608691
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    jedi.set_debug_function()

    expected_objects = {"__builtins__", "__name__", "__doc__", "__package__", "a"}

    src = "a = 5"
    completions = get_interpreter_completions(src, [{}])
    names = set(c.name for c in completions)

    assert names <= expected_objects

    src = "b = [1, 2, 3]"
    completions = get_interpreter_completions(src, [{}])
    names = set(c.name for c in completions)

    assert names <= expected_objects

    src = "a = lambda x: 5"
    completions = get_interpreter_completions(src, [{}])

# Generated at 2022-06-14 11:25:25.261596
# Unit test for function get_definitions
def test_get_definitions():
    """ Unit test for function get_definitions
    """
    import os
    import unittest
    import sys
    import jedi
    import thonny._vendor.jedi
    from thonny.jedi_utils import get_definitions

    test_dir = os.path.dirname(os.path.abspath(__file__))
    file_to_test = os.path.join(test_dir, "test_jedi_utils.py")
    with open(file_to_test) as fp:
        source = fp.read()
    row = 2
    column = 9
    result = []
    if _using_older_jedi(jedi):
        result_expected = [(row, column, "test_jedi_utils")]

# Generated at 2022-06-14 11:25:35.730771
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    interpreter = jedi.Interpreter(
        "imp", [{"type": "statement", "module_path": ["sys"], "names": ["sys"]}]
    )
    completions = interpreter.complete()
    assert len(completions) == 1
    assert completions[0].name == "import"
    assert completions[0].complete == "import "


if __name__ == "__main__":
    import sys

    test_get_interpreter_completions()
    print("All ok")
    sys.exit(0)

# Generated at 2022-06-14 11:25:37.567313
# Unit test for function get_definitions
def test_get_definitions():
    source = "import sys"
    script = get_definitions(source, 0, 0, "")
    assert script[0].name == "sys"



# Generated at 2022-06-14 11:25:43.239028
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import unittest\nu = unittest.TestCase()\nu."
    namespaces = []
    completions = get_interpreter_completions(source=source, namespaces=namespaces, sys_path=[])
    assert len(completions) == 83
    assert "assertEqual" in [c.name for c in completions]

# Generated at 2022-06-14 11:25:51.948036
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    interpreter = jedi.Interpreter("import sys; sys.version_info", [])
    completions = interpreter.complete()
    assert completions[0].complete == 'version_info'
    assert completions[0].name == 'version_info'
    assert completions[0].type == 'module'
    assert completions[0].description == 'version_info'
    assert completions[0].parent.type == 'module'

# Generated at 2022-06-14 11:25:57.755712
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    has_version = hasattr(jedi, "__version__")
    has_project = hasattr(jedi.Script, "path")
    has_project = False
    logger.info(
        "Using jedi %s, Project %s",
        jedi.__version__ if has_version else "?",
        jedi.__version__ if has_project else "?",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test_get_script_completions()

# Generated at 2022-06-14 11:26:06.465554
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    source = 'fun_name("para_name"\n'
    row = 1
    column = 6
    filename = "test.py"

    completions = get_script_completions(source, row, column, filename)
    assert_one_completion_in(completions, "fun_name")
    assert_one_completion_in(completions, "param_name")



# Generated at 2022-06-14 11:26:10.639931
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = """
import os

os.path.abspath("")
"""
    source = source.encode("utf-8")
    completions = get_interpreter_completions(source, [], sys_path=[])
    assert len(completions) > 100



# Generated at 2022-06-14 11:26:22.274482
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import Script

    def _test(code, column, expected):
        completions = get_script_completions(code, 1, column, "test.py")
        completions = [c.complete for c in completions]
        assert completions == expected

    _test("", 0, ["import ", "from ", "def "])
    _test("import ", 7, ["os", "sys", "time"])
    _test("from ", 5, ["os", "sys"])
    _test("import os", 7, ["as ", "."])
    _test("from os.path", 12, ["import ", "."])
    _test("from os.path import ", 19, ["isfile"])
    _test("from os import path", 15, ["."])

# Generated at 2022-06-14 11:27:17.588672
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    # To get the completions of a variable "abc" in the source code (that is already being executed):
    source = "abc."
    row = 0
    column = len(source) - 1
    namespaces = []
    # Here, variable abc must be already assigned in the local namespace.
    # This is a python shell embedded in a program that handles the user input
    # and runs the commands, so it will be alright for me.
    # This is the case for the following, for example:
    # abc = 10
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) > 0



# Generated at 2022-06-14 11:27:26.152195
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter

    import thonny
    from thonny.plugins.jedi_backend import _tweak_completions, get_interpreter_completions

    assert Interpreter
    assert thonny

    source = "".join(
        [
            'import unittest\n',
            'a = unittest.mock.Mock()\n',
            'a.method_a().mock_\n',
            'a.method_b(1, 2, 3).mock_',
        ]
    )

# Generated at 2022-06-14 11:27:37.212473
# Unit test for function get_script_completions
def test_get_script_completions():
    source = '"".encode("ascii", errors="strict")'
    completions = get_script_completions(source, 0, len(source), "<module>")
    assert completions[0].name == "ignore"
    assert completions[1].name == "replace"
    assert completions[2].name == "backslashreplace"
    assert completions[3].name == "namereplace"
    assert completions[4].name == "xmlcharrefreplace"
    assert not completions[0].complete.endswith("=")
    assert not completions[1].complete.endswith("=")
    assert not completions[2].complete.endswith("=")
    assert not completions[3].complete.endswith("=")

# Generated at 2022-06-14 11:27:50.158788
# Unit test for function get_interpreter_completions

# Generated at 2022-06-14 11:27:58.525553
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "import turtle as t\n"
    source += "t.\n"
    completions = get_interpreter_completions(source, [{"turtle": {"Turtle": None}}])
    expected = [
        ThonnyCompletion("Turtle", "Turtle", "class", "class Turtle", "<dict>", "turtle.Turtle")
    ]

    _test_completions_equals(completions, expected)



# Generated at 2022-06-14 11:28:04.141592
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

# Generated at 2022-06-14 11:28:12.421336
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    if _using_older_jedi(jedi):
        source = "def f(x, y=1): pass\nf(1, y=2)\nf(y=2, x=1)"
        completions = get_script_completions(source, 3, 3, "")
        assert len(completions) == 3
        assert completions[0].name == "f()"
        assert completions[1].name == "x="
        assert completions[2].name == "y="
    else:
        # Given jedi version has different behaviour
        pass

# Generated at 2022-06-14 11:28:27.058319
# Unit test for function get_definitions
def test_get_definitions():
    from thonny.plugins.jedi import utils
    from jedi import Interpreter
    import os.path
    examples_dir = os.path.abspath(os.path.join(True, os.path.split(__file__)[0], "..", "examples"))
    path = os.path.join(examples_dir, "A", "a.py")
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()
    # In the middle of function f
    line = 5
    column = 9
    infos = utils.get_definitions(source, line, column, path)
    assert len(infos) == 1
    info = infos[0]
    assert info.line == 1
    assert info.column == 4

# Generated at 2022-06-14 11:28:39.564020
# Unit test for function get_script_completions
def test_get_script_completions():
    completions = get_script_completions("sorted", 1, 7, "", sys_path=["/home/me/python/packages"])
    assert isinstance(completions, list)
    assert len(completions) > 0
    for c in completions:
        assert isinstance(c.name, str)
        assert isinstance(c.complete, str)
        assert isinstance(c.type, str) and c.type in ["function", "statement", "import", "keyword"]
        # assert isinstance(c.docstring, str)
        if c.type == "function":
            assert c.complete.endswith(c.name)
        assert len(c.name) > 0
    assert len(completions) == len({c.complete: 1 for c in completions}.keys())

# Generated at 2022-06-14 11:28:50.062007
# Unit test for function get_definitions
def test_get_definitions():
    """Return a list of test cases"""
    from .backend_test_utils import get_test_base_name, run_test_case, check_test_env
    from . import EditorTestCase
    import re
    import os

    def create_test_case(path, source, expected):
        test_func = EditorTestCase.make_test_case(
            "get_definitions()",
            path=path,
            source=source,
            expected=expected,
            name_func=get_test_base_name(os.path.basename(path), re.escape(source)),
        )
        return test_func

    test_cases = []
    if not check_test_env():
        return test_cases

# Generated at 2022-06-14 11:29:51.632700
# Unit test for function get_definitions
def test_get_definitions():
    # Here we test for different version of Jedi (0.13,0.14,0.15,0.16,0.17)
    # with different versions of Python (3.3,3.4,3.5,3.6,3.7)
    # See https://github.com/davidhalter/jedi/commit/9f3a2f93c48eda24e2dcc25e54eb7cc10aa73848
    import sys
    import jedi
    print("Python:", sys.version, '\tJedi:', jedi.__version__[:4])
    source1 = """
import sys
sys.getdefaultencoding()
"""
    source2 = """
import sys
sys.version
"""
    source3 = """
import sys
sys.getprofile()
"""

# Generated at 2022-06-14 11:29:55.579195
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.parser_utils import get_cached_code_lines

    # Issue #145
    from jedi.common import splitlines


# Generated at 2022-06-14 11:30:07.570297
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock
    code = """
if True:
    def foo():
        pass
    """
    completions = get_script_completions(code, 1, 1, "test.py")
    assert len(completions) == 3
    assert completions[0].complete == "if "
    assert completions[1].complete == "import"
    assert completions[2].complete == "def "

    completions = get_script_completions(code, 2, 8, "test.py")
    assert len(completions) == 2
    assert completions[0].complete == "foo("
    assert completions[1].complete == "False"

    completions = get_script_completions(code, 5, 1, "test.py")

# Generated at 2022-06-14 11:30:08.331182
# Unit test for function get_definitions

# Generated at 2022-06-14 11:30:21.053669
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.plugins.jedi_utils import get_script_completions

    assert get_script_completions('import math\nmath.c', 2, 7, '')

    if _using_older_jedi():
        for completion in get_script_completions('import math\nmath.ceil', 2, 7, ''):
            assert not completion.name.endswith("=")

        for completion in get_script_completions('import math\nmath.ceil(', 2, 10, ''):
            assert completion.name.endswith("=")

    else:
        for completion in get_script_completions('import math\nmath.ceil', 2, 7, ''):
            assert completion.name.endswith("=")


# Generated at 2022-06-14 11:30:26.323337
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi
    from jedi import Interpreter, Script
    interpreter = Interpreter('import builtins', [{'builtins': builtins}])
    if _using_older_jedi(jedi):
        assert interpreter.completions() == _tweak_completions(interpreter.completions())
    else:
        assert interpreter.completions() == _tweak_completions(interpreter.complete())
    interpreter = Interpreter('str.title()', [])
    completions = _tweak_completions(interpreter.complete())
    assert completions[0].name == 'title'
    assert completions[0].complete == 'title('
    assert completions[0].type == 'function'
    assert completions[0].description.startswith('S.title() -> str')

# Generated at 2022-06-14 11:30:30.916335
# Unit test for function get_definitions
def test_get_definitions():
    assert get_definitions('from math import sqrt\nsqrt(4)', 2, 5, "test")
    assert get_definitions('from math import sqrt\nsqrt  (4)', 2, 5, "test")

# Generated at 2022-06-14 11:30:40.360490
# Unit test for function get_definitions
def test_get_definitions():
    source = """def f(x): pass

f(3)
"""
    definitions = get_definitions(source, line=1, column=1, filename="")
    assert len(definitions) == 1
    assert definitions[0].type == "function"
    assert definitions[0].line == 1
    assert definitions[0].column == 0
    assert definitions[0].module_path == ""

    definitions = get_definitions(source, line=2, column=2, filename="")
    assert len(definitions) == 1
    assert definitions[0].type == "function"
    assert definitions[0].line == 1
    assert definitions[0].column == 0
    assert definitions[0].module_path == ""


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test

# Generated at 2022-06-14 11:30:53.329601
# Unit test for function get_definitions
def test_get_definitions():
    def check(source, row, column, expected):
        result = get_definitions(source, row, column, None)
        if len(result) != len(expected):
            print(
                "Expected",
                expected,
                "got",
                [
                    (
                        r.full_name,
                        r.line,
                        r.column,
                        r._definition.type,
                        r._definition.parent.name,
                    )
                    for r in result
                ],
                sep="\n",
            )
        assert len(result) == len(expected)
        result_locations = [(r.line, r.column) for r in result]
        expected_locations = [(r[0], r[1]) for r in expected]
        print("Got", result_locations)

# Generated at 2022-06-14 11:31:00.620265
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import patch, MagicMock
    from jedi import Script
    from thonny.jedi_utils import get_script_completions
    with patch("thonny.jedi_utils.Script") as script_mock:
        instance_mock = MagicMock()
        script_mock.return_value = instance_mock
        instance_mock.completions.return_value = []
        result = get_script_completions("Script", 1, 1, "")
        assert Script.call_args[0][0:4] == ("Script", 1, 1, "")
        assert get_script_completions("Script", 1, 1, "") == []
        get_script_completions("Script", 1, 1, "", "")