

# Generated at 2022-06-14 11:21:38.092095
# Unit test for function get_definitions
def test_get_definitions():
    import unittest
    import jedi

    source = 'import sys\nimport os\nprint(sys.path)\n'
    row = 3
    column = 7

    result = get_definitions(source, row, column, None)
    # Test that all elements are of correct type
    assert(all(isinstance(obj, jedi.api_classes.BaseDefinition) for obj in result))
    # Test that the list is lengthy
    assert(len(result) > 1)


# Generated at 2022-06-14 11:21:43.408168
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    def get_completions(code):
        result = []
        for c in get_interpreter_completions(code, [{}]):
            result.append(c.name)
        return result

    s = Interpreter("2+2", [{}])
    assert get_completions("2+2") == s.complete() # The old method should work


# Generated at 2022-06-14 11:21:47.447360
# Unit test for function get_definitions
def test_get_definitions():
    def get_definitions(source, row, column):
        return jediutils.get_definitions(source, row, column, "testfile")


# Generated at 2022-06-14 11:21:59.841986
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.api import inspectors

    source = """
import os
import sys

os.remove("somefile")
sys.remove("somefile")
sys.exit()
"""
    lines = source.split("\n")
    for line_no in range(1, len(lines) + 1):
        parts = lines[line_no - 1].split(".")
        for end_col in range(len(parts[-1]) + 1, len(parts[-1]) + 3):
            # print("Checking line %d, col %d" % (line_no, end_col))
            definitions = get_definitions(source, line_no, end_col, "test.py")
            if line_no == 3:
                assert len(definitions) == 3

# Generated at 2022-06-14 11:22:09.390162
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    # Test for jedi < 0.18
    if _using_older_jedi(jedi):
        namespaces = [{
            "__name__": "__main__",
            "__doc__": None,
            "__package__": None,
            "__loader__": None,
            "__spec__": None,
            "__annotations__": {},
            "__builtins__": {},
            "__file__": __file__,
            "__cached__": None,
            "a": 1,
            "aaa": 2
        }]
        completions = get_interpreter_completions("a", namespaces, [])
        assert len(completions) == 1
        assert completions[0].name == "aaa"

        completions = get_interpreter_

# Generated at 2022-06-14 11:22:13.457964
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    line = 'import re\nre.ma.'
    assert get_interpreter_completions(line, [], sys_path=[])


# Generated at 2022-06-14 11:22:18.860365
# Unit test for function get_definitions
def test_get_definitions():
    defs = get_definitions(
        "import json\n"
        "x = json.load\n"
        "^\n"
        "\n",
        3, 1, ""
    )
    assert len(defs) == 1

# Tests for get_script_completions

# Generated at 2022-06-14 11:22:27.253745
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi
    import parso
    import sys
    filename = "/home/thonny/myfile.py"

    def check_completions(source, row, column, exp_completions):
        completions = get_script_completions(source, row, column, filename)

        completions_names = [cmp.name for cmp in completions]
        if not exp_completions:
            assert completions_names == []
        else:
            for exp in exp_completions:
                assert exp in completions_names

    # 1. check if jedi version is 0.18 or higher
    if _using_older_jedi(jedi):
        print("jedi version is older than 0.18")
    else:
        print("jedi version is 0.18 or higher")

    # 2.

# Generated at 2022-06-14 11:22:36.326122
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import os
    import unittest
    import jedi
    from jedi.api import Interpreter

    if isinstance(jedi, Interpreter):
        jedi = jedi.completions()
    thonny_completions = _tweak_completions(jedi)
    assert thonny_completions[0].complete == 'os'

    current_dir = os.getcwd()
    dir_name = os.path.basename(current_dir)
    thonny_completions = get_interpreter_completions(
        source='',
        namespaces=[{'locals': {'os': os}},
                      {'globals': {'os': os}}
                      ],
    )
    assert thonny_completions[0].complete == 'os'



# Generated at 2022-06-14 11:22:48.438138
# Unit test for function get_script_completions
def test_get_script_completions():
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from jedi.script import get_script_completions, Script

    completions = get_script_completions("import os", 1, 1)
    assert len(completions) > 0

    # result order has changed in jedi 0.17
    completions = get_script_completions("import os", 1, 1)
    assert completions[0].name == "os" or completions[1].name == "os"

    completions = get_script_completions("import os\nos.", 1, 1)
    assert completions[0].name == "os" or completions[1].name == "os"

    # 0.18
    completions = get_

# Generated at 2022-06-14 11:23:12.893589
# Unit test for function get_script_completions
def test_get_script_completions():
    source = """x = "abcdef"
print(x.upper)
"""
    assert len(get_script_completions(source, row=2, column=12, filename="<input>")) > 0

# Generated at 2022-06-14 11:23:15.935838
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

# Generated at 2022-06-14 11:23:27.951472
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.test_jedi import get_completions_docstring, get_completions_docstring_local_mode

    # test mode
    if get_interpreter_completions(
        "__main__.get_completions_docstring",
        [get_completions_docstring.__dict__],
    ):
        print("Test mode enabled.")
        get_interpreter_completions("__main__.get_completions_docstring", [get_completions_docstring.__dict__])
        return
    # test mode

    get_interpreter_completions("__main__.get_completions_docstring", [get_completions_docstring.__dict__])

# Generated at 2022-06-14 11:23:41.095244
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.api.project import get_script
    from jedi.api.interpreter import get_completions
    src = '''import socket

# Request to some standard domains
socket.getaddrinfo("example.org", 80, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_
'''
    script = get_script(src, 3, len('socket.IPPROTO_'), '.', sys_path=None)
    completions = script.completions()

    # ensure we got the same completions
    assert len(completions) == 2
    assert completions[0].name == 'IPPROTO_TCP'
    assert completions[1].name == 'IPPROTO_UDP'

    # New jedi

# Generated at 2022-06-14 11:23:48.177338
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from test.jedi_fixtures import COMPLETE_EXAMPLES

    completions = []
    for source, row, column, namespace, sys_path in COMPLETE_EXAMPLES:
        completions.append(get_interpreter_completions(source, [namespace] + _get_builtins(), sys_path))

    for expected, actual in zip([example[-1] for example in COMPLETE_EXAMPLES], completions):
        assert set(expected) == set(actual)



# Generated at 2022-06-14 11:23:57.266277
# Unit test for function get_script_completions
def test_get_script_completions():
    def _check(content, row, column, expected_name):
        completions = get_script_completions(content, row, column, "")
        assert len(completions) == 1
        assert completions[0].name == expected_name

    _check("[1, 2, 3].", 0, 12, "append")
    _check("str(c for c in range(5))", 0, 9, "capitalize")
    _check("a + b", 0, 5, "__add__")

# Generated at 2022-06-14 11:24:03.723693
# Unit test for function get_script_completions
def test_get_script_completions():
    assert len(get_script_completions("pri", 0, 3, "dummy.py")) > 0
    assert len(get_script_completions("print(a)", 0, 8, "dummy.py")) > 0

    assert len(get_script_completions("dummy.py", 0, 0, "dummy.py")) == 0
    assert len(get_script_completions("dummy.py", 0, len("dummy.py"), "dummy.py")) > 0

# Generated at 2022-06-14 11:24:16.332557
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions("print(", [{}], None)[0].name == "print("
    assert get_interpreter_completions("import sys\nprint(sys.", [{}], None)[0].name == "path"
    assert get_interpreter_completions("int.", [{}], None)[0].name == "isinstance"
    assert get_interpreter_completions("from sys import ", [{}], None)[0].name == "exit"
    assert get_interpreter_completions("from sys import pat", [{}], None)[0].name == "path"


if __name__ == "__main__":
    print("With sys.path:")

# Generated at 2022-06-14 11:24:24.244652
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    source = 'import os\nimport sys\nprint("Hello world")\nos.path.join("aaa", "bbb")'
    row = 1
    column = 6
    filename = "test.py"
    sys_path = None

    completions = get_script_completions(source, row, column, filename)

    jedi_completions = jedi.Script(source, row, column, filename).completions()

    assert len(completions) == len(jedi_completions)

    assert completions[0].name == jedi_completions[0].name
    assert completions[0].complete == jedi_completions[0].complete
    assert completions[0].type == jedi_completions[0].type
    assert completions[0].description == j

# Generated at 2022-06-14 11:24:36.041928
# Unit test for function get_definitions
def test_get_definitions():
    # Test the cases from helpers.py
    assert len(get_definitions('def f(a):\n    pass', 0, 7, '')) == 1
    if _using_older_jedi(__import__('jedi')):
        assert get_definitions('def f(a):\n    pass', 0, 7, '')[0].line == 0
    else:
        assert get_definitions('def f(a):\n    pass', 0, 7, '')[0].line == 1
    assert len(get_definitions('f(a)', 0, 1, '')) == 1
    if _using_older_jedi(__import__('jedi')):
        assert get_definitions('f(a)', 0, 1, '')[0].line == 0

# Generated at 2022-06-14 11:25:00.528523
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    assert get_interpreter_completions(
        'import datetime \ndatetime.d',
        [{"datetime": datetime}],
    )



# Generated at 2022-06-14 11:25:03.591582
# Unit test for function get_script_completions
def test_get_script_completions():
    assert len(get_script_completions("import sys;", 3, len("import sys;") + 1, "")) > 0


# Generated at 2022-06-14 11:25:04.891262
# Unit test for function get_definitions

# Generated at 2022-06-14 11:25:11.745945
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import MagicMock

    namespaces = [{"__builtins__": {"AnInBuiltin": MagicMock()}}]

    completions = get_interpreter_completions("AnInBuil", namespaces)

    assert len(completions) == 1

    completion = completions[0]
    assert completion.name == "AnInBuiltin"
    assert completion.complete == "AnInBuiltin"
    assert completion.type == "instance"
    assert completion.description == "MagicMock"
    assert completion.parent == "<module>"
    assert completion.full_name == "__builtins__.AnInBuiltin"

# Generated at 2022-06-14 11:25:24.752315
# Unit test for function get_script_completions
def test_get_script_completions():
    from parso.python.tree import Import, ExprStmt, Name, Leaf
    from parso.python.parser import PythonParser
    parser = PythonParser()

    # Test for function get_statement_of_position
    def test_get_statement_of_position(source, pos):
        try:
            parsed = parse_source(source)
        except:
            return None
        return get_statement_of_position(parsed, pos)

    assert test_get_statement_of_position("", 0) is None
    assert test_get_statement_of_position("a = 10", 4) is None
    assert test_get_statement_of_position("a = 10", 0) == parsed("a = 10")

# Generated at 2022-06-14 11:25:33.679485
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    Unit test for function `get_interpreter_completions`.
    """
    from jedi import Interpreter

    source = "import datetime\n" "datetime."
    interpreter = Interpreter(source, [{}])
    completions = interpreter.completions()
    assert completions[0].name in ["date", "datetime"]


if __name__ == "__main__":
    test_get_interpreter_completions()

# Generated at 2022-06-14 11:25:34.948234
# Unit test for function get_definitions

# Generated at 2022-06-14 11:25:42.511714
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi import Interpreter
    from jedi.api import Source
    import re

    # tests for the old jedi version
    # following code was copied from the test code for jedi.api.helpers.get_names_of_scope
    # https://github.com/davidhalter/jedi/blob/f0f7e6cba5360e1de8511c0e21a7c95875b8988d/test/api_test/test_helpers.py#L370-L389

# Generated at 2022-06-14 11:25:49.867476
# Unit test for function get_definitions
def test_get_definitions():
    jedi = __import__("jedi")
    script = jedi.Script("""
a = 10
print(a)
""", 3, 1, "test.py")
    assert len(script.goto_definitions()) == 1, "There should be one definition."
    assert script.goto_definitions()[0].name == "a"

# Generated at 2022-06-14 11:25:57.669805
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import Mock

    def mock_script(source, row, column, filename, sys_path=None):
        if sys_path != None:
            raise Exception()
        return Mock(completions=lambda: [])

    def mock_script2(code, path, project):
        if path != "filename" or project != "project":
            raise Exception()
        return Mock(complete=lambda line, column: [])

    import jedi

    source = "aaa.bbb"
    row = 1
    column = 6
    filename = "filename"
    sys_path = "/home/myhome"
    jedi.Script = lambda *args, **kwargs: mock_script(*args, **kwargs)
    assert get_script_completions(source, row, column, filename, sys_path) == []

# Generated at 2022-06-14 11:26:30.630381
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from _jedi_utils import get_interpreter_completions
    from collections import namedtuple
    from unittest.mock import Mock
    completions = get_interpreter_completions(
        source="", namespaces=[], sys_path=[]
    )

# Generated at 2022-06-14 11:26:44.331859
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from unittest.mock import MagicMock

    jedi_interpreter = MagicMock()
    jedi_interpreter.complete.return_value = []
    for jedi_completion in [
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
    ]:
        jedi_completion.name = "name"
        jedi_completion.complete = "complete"
        jedi_completion.type = "type"
        jedi_completion.description = "description"
        jedi_completion.parent = "parent"
        jedi_completion.full_name = "full_name"
        jedi_interpreter.complete.return_value.append(jedi_completion)
    completions = get_interpre

# Generated at 2022-06-14 11:26:51.434777
# Unit test for function get_script_completions
def test_get_script_completions():
    if not _using_older_jedi():
        # cannot test because above implementation is for 0.18 or newer
        return

    completions = get_script_completions(
        '"".s', 1, 2, "<input>"
    )
    assert len(completions) == 122

# Generated at 2022-06-14 11:27:00.408902
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = 'class A:\n    def meth1(self, arg1):\n        return 1'
    namespaces = [
        {
            "A": {
                "__module__": "__main__",
                "__qualname__": "A",
                "__doc__": None,
                "meth1": lambda: None,
            }
        }
    ]
    result = get_interpreter_completions(source, namespaces)
    assert result[0].complete == "interface()"

# Generated at 2022-06-14 11:27:07.902596
# Unit test for function get_script_completions
def test_get_script_completions():
    source = "import os; os.path.cl"
    row = 1
    column = len(source)

    print(_get_completions(source, row, column))
    assert _get_completions(source, row, column) == ["os.path.clear()", "os.path.closerange()"]



# Generated at 2022-06-14 11:27:14.637822
# Unit test for function get_script_completions
def test_get_script_completions():
    source = "def f():\n    pass\nf("
    completions = get_script_completions(source, 2, 8, "")
    assert len(completions) == 2 #self, cls
    assert completions[0]["name"] == "self"
    assert completions[0]["complete"] == "self="
    assert completions[1]["name"] == "cls"
    assert completions[1]["complete"] == "cls="


# Generated at 2022-06-14 11:27:19.366583
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.jedi_utils import get_script_completions
    source = "class Foo: pass\nFoo().set_da" 
    completion = get_script_completions(source, 2, 15, "test.py")[0]
    assert completion.name == "set_daemon"

# Generated at 2022-06-14 11:27:21.040213
# Unit test for function get_definitions
def test_get_definitions():
    import json
    import parso


# Generated at 2022-06-14 11:27:26.783804
# Unit test for function get_script_completions
def test_get_script_completions():
    return
    # cursor here: <|>
    test_str = """
    def test_function():
        return
    """
    completions = get_script_completions(test_str, 2, 4)
    assert len(completions) > 0
    assert "test_function(" in [c["complete"] for c in completions]


# Generated at 2022-06-14 11:27:37.747740
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    """
    Test get_interpreter_completions with an Interpreter of jedi<=0.16.0
    """
    from jedi import Interpreter
    from jedi import api_classes
    import json
    import os

    test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")
    with open(test_data_dir + "/completions.json", "r") as data_file:
        comp = json.loads(data_file.read())

    source = "\n".join(comp["source"])
    # create an Interpreter object
    interpreter = Interpreter(source=source, namespace=comp["namespaces"])
    # get the completions

# Generated at 2022-06-14 11:28:10.074286
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    def check_completions(jedi_version, sys_path, expected_completions, expected_logs):
        expected_logs = [
            message.format(jedi_version=jedi_version) for message in expected_logs
        ]
        with capture_output() as (out, err):
            completions = get_script_completions(
                "x.r", 1, 2, "test.py", sys_path=sys_path
            )
            got_logs = out.getvalue().splitlines()
            assert got_logs == expected_logs
            assert [_["complete"] for _ in completions] == expected_completions

    # jedi 0.16 can't handle sys_path argument
    # jedi 0.18, 0.19 crashes with sys_path


# Generated at 2022-06-14 11:28:14.478731
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = """
import math
print(math.co)
"""
    completions = get_interpreter_completions( source, [])
    assert "pi" in [c.name for c in completions]

# Generated at 2022-06-14 11:28:27.428828
# Unit test for function get_definitions
def test_get_definitions():
    assert len(get_definitions("int()", 0, 1, None)) == 1
    assert len(get_definitions("print", 0, 1, None)) == 1
    assert len(get_definitions("print()", 0, 1, None)) == 1
    assert len(get_definitions("import sys as s", 0, 1, None)) == 1
    assert len(get_definitions("s", 0, 1, None)) == 1
    assert len(get_definitions("s.", 0, 1, None)) == 0
    assert len(get_definitions("def foo():\n  pass\n\nfoo", 0, 1, None)) == 1
    assert len(get_definitions("foo", 0, 1, None)) == 0


# Tests for function get_script_completions

# Generated at 2022-06-14 11:28:31.000614
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi import __version__
    # Testing with python 3.7 and all jedi versions since 0.13

# Generated at 2022-06-14 11:28:42.414489
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import pkgutil
    import parso
    source = textwrap.dedent("""
    import json
    json.
    """)
    namespaces = [{'json': json}]

    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) == 1
    json_module = completions[0]
    assert json_module.name == 'json'
    assert json_module.type == 'module'
    assert json_module.complete == 'json'

    source = textwrap.dedent("""
    import json
    json.loa
    """)
    completions = get_interpreter_completions(source, namespaces)
    assert len(completions) == 1
    assert completions[0].name == 'load'

# Generated at 2022-06-14 11:28:47.898411
# Unit test for function get_script_completions
def test_get_script_completions():
    from unittest.mock import patch

    jedi_versions = ["0.13", "0.14", "0.15", "0.16", "0.17", "0.18", "1.0"]


# Generated at 2022-06-14 11:28:57.814901
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if _using_older_jedi(jedi):
        import jedi.api.interpreter

        interpreter = jedi.Interpreter(
            "x = [1,2,3]\nx.",
            [
                jedi.api.interpreter.InterpreterNamespace(
                    {"x": [1, 2, 3]}, "locals", {"x": [1, 2, 3]}
                )
            ],
        )
        assert len(interpreter.completions()) > 3
    else:
        assert len(get_interpreter_completions("x = [1,2,3]\nx.", [{"x": [1, 2, 3]}])) > 3


# Generated at 2022-06-14 11:29:05.638919
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    source = "1 + "
    namespaces = []
    output = get_interpreter_completions(source, namespaces, sys_path=["<dummy>"])
    assert len(output) > 10
    assert any(d.name == "int" for d in output)
    output = get_interpreter_completions(source, namespaces)
    assert len(output) > 10
    assert any(d.name == "int" for d in output)

# Generated at 2022-06-14 11:29:14.787488
# Unit test for function get_definitions
def test_get_definitions():
    from jedi.evaluate.compiled import CompiledObject

    for jedi_version in ["0.13.2", "0.14.1", "0.15.1", "0.16.0.dev0", "0.17.2"]:
        source = (
            "import re\n"
            + "import math\n"
            + "print(re.compile())\n"
            + "print(math.factorial())\n"
            + "print(math.factorial(1)\n"
        )
        row = 4
        column = 13
        filename = "stdin"
        definitions = get_definitions(source, row, column, filename)
        assert len(definitions) == 1
        assert isinstance(definitions[0], CompiledObject)

# Generated at 2022-06-14 11:29:29.096241
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions(
        "str", [{"str": ""}, {"str": ""}]
    )
    assert get_interpreter_completions(
        "numpy.core.multiarray", [{"numpy": ""}, {"numpy": ""}]
    )
    assert get_interpreter_completions(
        "numpy.core.multiarray", [{"numpy": ""}, {"numpy": ""}]
    )
    assert get_interpreter_completions(
        "np.", [{"np": ""}, {"np": ""}]
    )

# Generated at 2022-06-14 11:29:57.781827
# Unit test for function get_script_completions
def test_get_script_completions():
    import jedi

    assert _using_older_jedi(jedi)

    completions = get_script_completions("time.", 1, 5, "foo.py")
    assert len(completions) > 0
    assert "time" in [completion.name for completion in completions]



# Generated at 2022-06-14 11:30:08.259914
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import jedi

    if jedi.__version__[:3] == "0.9":
        return

    import os.path
    import sys
    import tempfile

    tmp_dir = tempfile.mkdtemp()

    sys.path.append(tmp_dir)

    with open(os.path.join(tmp_dir, "module.py"), "w") as fp:
        fp.write("class MyClass:\n    def a_method(self):\n        pass\n\n")


# Generated at 2022-06-14 11:30:12.790923
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    completions = get_interpreter_completions(
        source="", namespaces=[{"os": __import__("os")}]
    )

    assert [c.name for c in completions]



# Generated at 2022-06-14 11:30:17.838602
# Unit test for function get_script_completions
def test_get_script_completions():
    from thonny.globals import get_workbench
    import jedi
    import unittest

    if _using_older_jedi(jedi):
        class TestCompletion(unittest.TestCase):

            def setUp(self):
                # TODO: create test_script_completions() for older Jedi
                pass

            def test_0_16(self):
                # TODO: create test_script_completions() for older Jedi
                pass

            def tearDown(self):
                pass

        return TestCompletion
    else:
        class TestCompletion(unittest.TestCase):

            def setUp(self):
                # TODO: create test_script_completions() for older Jedi
                pass


# Generated at 2022-06-14 11:30:21.302434
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    import inspect
    import sys

    assert len(
        get_interpreter_completions("import inspect; inspect", [], sys_path=sys.path)
    ) == len(dir(inspect))



# Generated at 2022-06-14 11:30:26.712745
# Unit test for function get_script_completions
def test_get_script_completions():
    from jedi.parser.python.tree import ExprStmt, Name

    source: str = "print()"
    row: int = 0
    column: int = 4
    filename: str = "test_get_script_completions.py"
    sys_path = None
    completions = get_script_completions(source, row, column, filename, sys_path)
    assert completions[0].name == "print"
    assert completions[0].complete == "print()"
    assert completions[0].type == "statement"
    assert completions[0].description is None
    assert completions[0].parent is None
    assert completions[0].full_name == "print"


# Generated at 2022-06-14 11:30:38.725657
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from jedi.evaluate import representation as er

    # jedi 0.16.0+
    if hasattr(er.Instance, "name_for_position"):
        ns = [er.Instance("sys", [("stdin", er.Instance("stdin", [])), ("stdout", None)])]
        result = get_interpreter_completions("sys.stdi", ns, [])
        assert len(result) == 2
        assert result[0].name == "stdin"
        assert result[1].name == "stdout"
        assert result[0].description.startswith("file")

        result = get_interpreter_completions("sys.stdi.", ns, [])
        assert len(result) == 2
        assert result[0].name == "read"

# Generated at 2022-06-14 11:30:48.400410
# Unit test for function get_script_completions
def test_get_script_completions():
    import unittest

    class Test(unittest.TestCase):
        def test_it(self):
            self.assertEqual(
                get_script_completions(source="import sysend", row=1, column=16, filename=""),
                [
                    ThonnyCompletion(
                        name="sys",
                        complete="sys",
                        type="module",
                        description="Built-in module",
                        parent="builtins",
                        full_name="sys",
                    )
                ],
            )

    return unittest.main(module=__name__, exit=False).result



# Generated at 2022-06-14 11:30:58.344825
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    assert get_interpreter_completions("None", [{}]) == []
    assert get_interpreter_completions("prin", [{}]) == []
    assert get_interpreter_completions("print", [{}]) == [ThonnyCompletion("print", "print", "function", "print(...)", "builtins", "builtins.print")]
    assert get_interpreter_completions("pa", [{}]) == [ThonnyCompletion("paku", "paku", "module", "", "", "paku")]
    assert get_interpreter_completions("print(", [{}]) == []

# Generated at 2022-06-14 11:31:02.210676
# Unit test for function get_interpreter_completions
def test_get_interpreter_completions():
    from help_test_utils import assert_in, assert_not_in
    from jedi.api import Interpreter
    from jedi.parser_utils import get_statement_of_position

    source = "str.upper().lower()"
    row = 0
    column = 17
    interpreter = Interpreter(source, [locals()])
    completions = get_interpreter_completions(source, [locals()])

    node = get_statement_of_position(interpreter._get_module(), (row, column))

    assert len(completions) == 2
    for c in completions:
        assert c["name"] in ("lower", "lowercase")

    assert_in({"name": "lower", "complete": "lower"}, completions)