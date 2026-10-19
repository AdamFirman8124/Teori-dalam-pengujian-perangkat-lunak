

# Generated at 2022-06-13 17:49:47.874930
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    grammar = Grammar()
    grammar.load('Grammar.txt')

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:49:55.606419
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io
    import sys

    if sys.version_info < (3, 0):
        f = io.BytesIO()
    else:
        f = io.StringIO()

    g = Grammar()
    g.loads(f.read())
    g.load("not_a_file")

    with open("temp.pkl", "wb") as f2:
        g.dump(f2.name)
    with open("temp.pkl", "rb") as f3:
        g.load(f3.name)

    os.remove("temp.pkl")

# Generated at 2022-06-13 17:50:04.683636
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    The method load of class Grammar loads the grammar tables from a pickle file.
    Before loading the grammar, the instance variables should be empty.
    After loading, they should be filled with the data written to the file.
    """
    import os
    import pickle
    import pprint
    import tempfile
    import sys
    import unittest

    class GrammarTestCase(unittest.TestCase):
        def check(self, g: Grammar) -> None:
            self.assertEqual(
                len(g.symbol2number),
                3,
                msg="symbol2number should contain 3 entries",
            )
            self.assertEqual(
                len(g.number2symbol),
                3,
                msg="number2symbol should contain 3 entries",
            )
            self.assertEqual

# Generated at 2022-06-13 17:50:16.534711
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import tempfile
    g = Grammar()
    g.symbol2number = {'A': 256, 'B': 257}
    g.dfas = {256: ([[(1, 257)]], {1: 0}), 257: ([[(0, 257)]], {0: 1})}
    g.labels = [(0, None), (257, None)]
    g.keywords = {}
    g.tokens = {}
    g.symbol2label = {'A': 1, 'B': 2}
    g.start = 256
    g.states = [[[(1, 257)], [(0, 257)]], [[(2, 257), (0, 257)]]]
    f = tempfile.NamedTemporaryFile(mode="w", delete=False)
    f.close()
    g

# Generated at 2022-06-13 17:50:17.118730
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()



# Generated at 2022-06-13 17:50:18.705566
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test dump of Grammar class."""
    g = Grammar()
    try:
        g.dump("/dev/null")
    except Exception as e:
        raise AssertionError("exception raised: {}".format(e))

# Generated at 2022-06-13 17:50:28.012471
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest.mock as mock

    table_file = mock.Mock()
    table_file.read = mock.Mock(return_value=b"test_data")
    with mock.patch('builtins.open', return_value=table_file) as mock_open:
        g = Grammar()
        g.loads = mock.Mock()
        g.load("dummy_file")
    mock_open.assert_called_with("dummy_file", "rb")
    table_file.read.assert_called_with()
    g.loads.assert_called_with(b"test_data")

# Generated at 2022-06-13 17:50:30.222067
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test the dump method of class Grammar"""
    gram = Grammar()
    gram.dump(tempfile.gettempdir() + '/test_gram_dump')


# Generated at 2022-06-13 17:50:36.395107
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Setup
    g = Grammar()

# Generated at 2022-06-13 17:50:39.635666
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickle

    class A():
        pass
    d = {"b":A(), "c":1}
    data = pickle.dumps(d, pickle.HIGHEST_PROTOCOL)
    g = Grammar()
    g.loads(data)
    assert g.b.__name__ == "A"
    assert g.c == 1

# Generated at 2022-06-13 17:50:44.381612
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class TestGrammar(Grammar):
        pass
    TestGrammar().dump("testgrammar.pkl")



# Generated at 2022-06-13 17:50:50.052898
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.foo = 1
    with tempfile.NamedTemporaryFile(delete=False) as f:
        g.dump(f.name)
    with open(f.name, "rb") as f:
        d = pickle.load(f)
    assert d == {"foo": 1}
    os.unlink(f.name)

# Generated at 2022-06-13 17:50:52.459695
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    p = Grammar()
    p.dump("foo")  # Should be silent
    assert os.path.exists("foo")

# Generated at 2022-06-13 17:51:01.556287
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Setup
    g = Grammar()
    g.states = [[[], [], []], [[], [], []]]
    g.dfas = {1: ([[]], {"a": 1})}
    g.labels = [(1, "a"), (2, "b"), (3, "c")]
    g.symbol2number = {"s1": 1, "s2": 2}
    g.number2symbol = {1: "s1", 2: "s2"}
    g.keywords = {"a": 3, "b": 4}
    g.tokens = {1: 5, 2: 6}
    g.symbol2label = {"a": 7, "b": 8}

    # Exercise primary load path

# Generated at 2022-06-13 17:51:08.569229
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(__file__.replace('.py', '.pickle'))
    assert grammar.symbol2number['TYPE_IGNORE'] == 258
    assert grammar.number2symbol[259] == 'funcdef'
    assert len(grammar.states) == 6
    assert len(grammar.states[0]) == 2
    assert len(grammar.states[0][0]) == 2
    assert grammar.states[0][0][0] == (257, 1)
    assert grammar.dfas == {}
    assert grammar.labels == [(0, 'EMPTY')]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.symbol2label == {}

# Generated at 2022-06-13 17:51:20.688192
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .parse import ParserError
    from .conv import convert_pygram

    # not sure what to do here, but at least make sure it doesn't crash
    convert_pygram.convert("python")
    g = convert_pygram.convert("Grammar")
    g.dump("/tmp/xxx")
    with open("/tmp/xxx") as f:
        g2 = pickle.load(f)

    from .oparser import create_parser
    # a temporary version of load that uses the pickle module
    g.load = lambda s: g._update(pickle.load(open(s, "rb")))
    p = create_parser(g)

    ps = "def __str__(self):\n    return 'Foo(%s)' % self.name"
    # first test that the error messages look

# Generated at 2022-06-13 17:51:31.924798
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def get_Grammar_dump(data_filename: str) -> None:
        data_filename = os.path.join(os.path.dirname(__file__), data_filename)
        g = Grammar()
        g.load(data_filename)
        g.dump(data_filename + ".pickle")
        g2 = Grammar()
        g2.load(data_filename + ".pickle")
        assert g.states == g2.states

    get_Grammar_dump("Grammar.dump.data.cfg")
    get_Grammar_dump("Grammar.dump.data.py")
    get_Grammar_dump("Grammar.dump.data.py3")


# Generated at 2022-06-13 17:51:38.566374
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest.mock
    import py._path.local
    import sys

    f = py._path.local.LocalPath("foo.pkl")
    m = unittest.mock.mock_open()
    with unittest.mock.patch("%s.open" % __name__, m, create=True):
        g = Grammar()
        g.dump(f)
        handle = m()
        handle.write.assert_called_with(
            pickle.dumps(g.__getstate__(), pickle.HIGHEST_PROTOCOL)
        )

    # XXX how to test for proper file deletion and replacement?
    # XXX how to test for any error condition?


# Generated at 2022-06-13 17:51:48.683063
# Unit test for method load of class Grammar
def test_Grammar_load():
  import inspect
  import os
  import sys
  import unittest

  # Define a test case class
  class TestGrammar(unittest.TestCase):
    grammar = None
    g_file = 'Python.grammar.pickle'
    other_file_prefix = 'Other.'

    def setUp(self):
      self.module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
      self.old_cwd = os.getcwd()
      self.tmpdir = tempfile.mkdtemp()
      os.chdir(self.tmpdir)
      if not self.grammar:
        self.grammar = Grammar()

# Generated at 2022-06-13 17:51:58.549867
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import tempfile
    from . import pgen2
    from . import finder

    def test_file(filename: Path) -> None:
        f = finder.Finder()
        g = pgen2.Driver(f.grammar(filename) + "\n", f).grammar
        temp = tempfile.TemporaryFile()
        g.dump(temp)
        temp.seek(0)
        g2 = Grammar()
        g2.load(temp)
        assert g.keywords == g2.keywords
        assert g.start == g2.start
        assert g.tokens == g2.tokens
        assert g.symbol2label == g2.symbol2label
        assert g.symbol2number == g2.symbol2number
        assert g.dfas == g2.dfas


# Generated at 2022-06-13 17:52:11.004406
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def _run(obj, expected_attr_names):
        # type: (Grammar, Tuple[str, ...]) -> None
        obj.dump("/tmp/grammar")
        with open("/tmp/grammar", "rb") as f:
            d = pickle.load(f)
        assert set(d) == set(expected_attr_names)

    _run(Grammar(), ("symbol2number", "number2symbol", "states", "dfas",
                     "labels", "keywords", "tokens", "start",
                     "symbol2label"))

    _run(Grammar(), ("symbol2number", "number2symbol", "states", "dfas",
                     "labels", "keywords", "tokens", "start",
                     "symbol2label"))

#

# Generated at 2022-06-13 17:52:21.545872
# Unit test for method load of class Grammar
def test_Grammar_load():
    gram = Grammar()

# Generated at 2022-06-13 17:52:24.318973
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pgen2.pgen
    g = pgen2.pgen.Grammar()
    g.load('Grammar.pickle')

# Generated at 2022-06-13 17:52:33.946863
# Unit test for method dump of class Grammar
def test_Grammar_dump():

    # test with the grammar from the pickle file (i.e. generate a copy)
    g = Grammar()
    g.load(__file__.replace(".py", ".pkl"))
    g1 = Grammar()
    g1.dump(tempfile.mktemp(suffix=".pkl"))
    g1.load(g1.dump.__defaults__[0])
    for attr in g.__dict__:
        assert getattr(g, attr) == getattr(g1, attr)

    # test with a simple grammar
    g = Grammar()
    g.symbol2number = {"test0": 256, "test1": 257, "test2": 258}
    g.number2symbol = {256: "test0", 257: "test1", 258: "test2"}
    g

# Generated at 2022-06-13 17:52:44.779028
# Unit test for method load of class Grammar
def test_Grammar_load():
    class A:
        def __getstate__(self):
            return {"x": "y"}

    def test_with_getstate(g):
        for i in range(2):
            g.load(f)
            assert g.x == "y"

    def test_no_getstate(g):
        for i in range(2):
            g.load(f)
            assert g.x == "y"

    f = tempfile.NamedTemporaryFile()
    filename = f.name

    g = Grammar()
    g.x = "z"
    g.dump(filename)
    test_no_getstate(g)

    g = A()
    g.dump(filename)
    test_with_getstate(g)

    g = Grammar()
    g.x = "z"
   

# Generated at 2022-06-13 17:52:54.617422
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert2py
    from .pgen import generate_grammar

    input_files = [
        "Grammar/Grammar"
        if os.path.exists("Grammar/Grammar")
        else "Lib/lib2to3/Grammar.txt"
    ]
    g = Grammar()
    convert2py(input_files, g, None)
    generate_grammar(g)

    # pickle to string, load pickled string
    s = pickle.dumps(g, pickle.HIGHEST_PROTOCOL)
    g2 = Grammar()
    g2.loads(s)

    # pickle to temporary file, load file

# Generated at 2022-06-13 17:53:04.707301
# Unit test for method load of class Grammar
def test_Grammar_load():
    def verify(s: str) -> None:
        f = tempfile.NamedTemporaryFile()
        f.write(s)
        f.flush()
        try:
            g = Grammar()
            g.load(f.name)
            g.report()
        finally:
            f.close()

    verify(b"cos\nsystem\n")

# Generated at 2022-06-13 17:53:15.168252
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pgen2
    from . import pytree

    def check_grammar(p: Grammar) -> None:
        assert p.symbol2number["encoding_decl"] == 258
        assert p.number2symbol[258] == "encoding_decl"
        assert p.start == 256
        assert p.symbol2number["funcdef"] == 261
        assert len(p.number2symbol) == 337
        assert 35 < len(p.labels) < 100
        assert len(p.tokens) < 20
        assert len(p.states) == len(p.dfas) == len(p.symbol2number) - 256

    filename = os.path.join(os.path.dirname(__file__), "Grammar.pickle")

# Generated at 2022-06-13 17:53:25.336217
# Unit test for method load of class Grammar
def test_Grammar_load():
    # uses token_to_pickle_map
    g = Grammar()
    g.symbol2number = {"file_input": 257, "stmt": 258, "compound_stmt": 259}
    g.number2symbol = {257: "file_input", 258: "stmt", 259: "compound_stmt"}
    g.states = [[(257, 1)], [(258, 2), (0, 1)], [(259, 3), (0, 2)], [(0, 3)]]
    g.dfas = {
        257: (g.states[0], {1: 1}),
        258: (g.states[1], {1: 1, 258: 1}),
        259: (g.states[2], {1: 1, 258: 1, 259: 1}),
    }
    g

# Generated at 2022-06-13 17:53:32.940486
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.pkl")

# Generated at 2022-06-13 17:53:45.874722
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import tempfile
    from pgen2.grammar import Grammar
    from pgen2.token import generate_tok_name

    filename = tempfile.mktemp()

# Generated at 2022-06-13 17:53:49.593807
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.txt")

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:53:55.035032
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.dump("test.pickle")
    with open("test.pickle", "rb") as fp:
        d = pickle.load(fp)
    assert 'number2symbol' in d
    # clean up
    os.remove("test.pickle")

# Generated at 2022-06-13 17:54:03.341899
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import token

    gram = Grammar()
    gram.symbol2number = {
        "and": 257,
        "except": 258,
        "lambda": 259,
        "or": 260,
        "try": 261,
    }
    gram.number2symbol = {v: k for k, v in gram.symbol2number.items()}

# Generated at 2022-06-13 17:54:07.717155
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class MyGrammar(Grammar):
        def __init__(self, filename: Path) -> None:
            super().__init__()
            self.load(filename)
            self.dump(filename)

    MyGrammar("Grammar.txt")



# Generated at 2022-06-13 17:54:12.477428
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:54:19.716263
# Unit test for method load of class Grammar
def test_Grammar_load():
    pgen_grammar = Grammar()

    # Load test grammar
    pgen_grammar.load(r"/usr/lib/python3.6/lib2to3/Grammar.pkl")

    # Check symbol and number both ways
    for name, number in pgen_grammar.symbol2number.items():
        assert name == pgen_grammar.number2symbol[number]

    for number, name in pgen_grammar.number2symbol.items():
        assert number == pgen_grammar.symbol2number[name]

# Generated at 2022-06-13 17:54:30.513156
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Test load method of Grammar class.

    This test should not fail, but it currently fails with

    # mypyc.foo.py.potential
    # Could not generate mypyc stub for module None
    # Error: Could not find module None listing file

    """
    # pylint: disable=unused-variable
    import pickle

    class A:
        foo: int = 1

    class B(A):
        pass

    a = A()
    b = B()
    # mypyc.foo.py.potential
    # Could not generate mypyc stub for module None
    # Error: Could not find module None listing file
    baz: bytes = pickle.dumps(b, pickle.HIGHEST_PROTOCOL)  # type: ignore

# Generated at 2022-06-13 17:54:31.808158
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load('Grammar')

# Generated at 2022-06-13 17:54:36.870115
# Unit test for method load of class Grammar
def test_Grammar_load():
    import os, unittest
    from pickle import dumps
    from pickle import loads
    from pickle import HIGHEST_PROTOCOL

    import pickletools
    import pickletools

    class Grammar__load(unittest.TestCase):

        def setUp(self):
            import typing
            self.maxDiff = None

# Generated at 2022-06-13 17:54:41.569051
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("my.pickle")
    assert os.path.exists("my.pickle")
    os.remove("my.pickle")



# Generated at 2022-06-13 17:54:51.802992
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import shutil
    import tempfile
    from . import pgen2
    from .tokenize import detect_encoding, TokenError

    # Issue3737: We don't want default encoding to be anything else
    # than the default 'ascii' to reproduce Issue3737 and make sure
    # that it is fixed.
    old_stdin = os.dup(0)
    old_stderr = os.dup(2)

# Generated at 2022-06-13 17:54:58.548894
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gram = Grammar()

# Generated at 2022-06-13 17:55:09.405742
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver

    parsed = driver.parse_grammar("Python", "Grammar.txt")
    assert parsed.version == "3.7"
    assert parsed.start == "file_input"
    assert parsed.grammar["file_input"].exprs == [("NEWLINE",), ("stmt", "file_input")]

    # ast.Grammar is not in Python 3
    if hasattr(token, "NEWLINE"):
        assert parsed.symbols["single_input"].type == "ast.Grammar"

    # mypyc generates objects that don't have a __dict__, but they
    # do have __getstate__ methods that will return an equivalent
    # dictionary
    if hasattr(parsed, "__dict__"):
        d = parsed.__getstate__()


# Generated at 2022-06-13 17:55:16.864203
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    os.makedirs("tmp", exist_ok=True)
    from .parse import ParserGenerator

    pg = ParserGenerator("Grammar.test_Grammar_dump")
    pg.add_nonterminal("file_input", ["stmt", "NEWLINE"], True)
    pg.add_nonterminal("stmt", ["simple_stmt"], True)
    pg.add_nonterminal("simple_stmt", [])
    pg.add_terminal("NEWLINE", token.NEWLINE)
    g = pg.build()

    # make sure that we don't get a TypeError with an invalid path
    try:
        g.dump("tmp/python_Grammar_dump.pickle")
    except TypeError:
        assert False

    # make sure that we get a TypeError with an invalid path


# Generated at 2022-06-13 17:55:19.884892
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    filename = "python3.6/Grammar.pkl"
    g.dump(filename)
    print(filename, "dumped")
    g.load(filename)
    print(filename, "loaded")
    g.report()

# Generated at 2022-06-13 17:55:23.562661
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2

    gr = pgen2.driver.load_grammar(
        os.path.join(os.path.dirname(__file__), "Grammar.txt")
    )
    gr.dump(os.devnull)
    gr.loads(gr.dumps())

# Generated at 2022-06-13 17:55:31.936024
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"a": 1, "b": 2}
    g.number2symbol = {"1": "a", "2": "b"}
    g.start = 256
    g.states = [[(1, 0), (1, 1)], [(1, 1)]]
    g.dfas = {1: (g.states[0], {0: 1, 1: 1}), 2: (g.states[1], {0: 1, 1: 1})}
    g.labels = [(0, "EMPTY")]
    g.keywords = {"a": 1}
    g.tokens = {1: 1}
    g.symbol2label = {"a": 1}
    expected = Grammar()
    g.dump(".dump_file.pickle")


# Generated at 2022-06-13 17:55:39.867570
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver

    grammar = Grammar()
    driver.load_grammar(grammar)
    # Save the tables so we don't have to regenerate them for later runs
    driver.save_grammar(grammar, "Grammar.txt")
    # Load the tables to check them
    grammar = Grammar()
    grammar.load("Grammar.txt")
    # Add a new attribute with an integer value
    grammar.test_int = 1

    # Save the tables again and make sure they're the same
    driver.save_grammar(grammar, "Grammar2.txt")
    with open("Grammar.txt", "rb") as f:
        pkl1 = f.read()
    with open("Grammar2.txt", "rb") as f:
        pkl2 = f.read

# Generated at 2022-06-13 17:55:49.036802
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {'test': 2}
    grammar.number2symbol = {'1': 'test1'}
    grammar.states = [1, 2, 3]
    grammar.dfas = {1: (1, 2), 2: (3, 4)}
    grammar.labels = [(1, "test1")]
    grammar.keywords = {"test1": 1}
    grammar.tokens = {1: 2}
    grammar.symbol2label = {"test1": 1, "test2": 2}
    grammar.start = 4
    grammar.dump('')
    grammar.async_keywords = True
    assert grammar.async_keywords == True
    grammar.copy()

# Generated at 2022-06-13 17:55:54.367667
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver

    driver.main("Grammar.load", "Grammar.dump")


if __name__ == "__main__":
    # Test this module
    test_Grammar_load()

# Generated at 2022-06-13 17:56:01.978298
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    import tempfile
    import unittest

    # Filename for testing.
    filename = os.path.join(tempfile.gettempdir(), "test_Grammar_dump.pkl")

    class GrammarTestCase(unittest.TestCase):

        def setUp(self):
            self.g = Grammar()
            self.g.symbol2number = {"a": 1, "b": 2}
            self.g.number2symbol = {1: "a", 2: "b"}
            self.g.states = [[[(1, 1)], [(0, 2)]], [[(2, 3)]]]
            self.g.dfas = {1: (self.g.states[0], 2)}

# Generated at 2022-06-13 17:56:04.200339
# Unit test for method load of class Grammar
def test_Grammar_load():
    class Foo(_GrammarTest):
        pass

    f = Foo()
    f.load("fname")

# Generated at 2022-06-13 17:56:14.027174
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class Mock_Grammar(Grammar):
        def __init__(self):
            self.symbol2number = {'test': '1'}
            self.number2symbol = {'1': 'test'}
            self.states = ["test"]
            self.dfas = {"test": "test"}
            self.labels = ["test"]
            self.keywords = {'test': 'test'}
            self.tokens = {'test': 'test'}
            self.symbol2label = {'test': 'test'}
            self.start = 256

    mock_instance = Mock_Grammar()
    mock_instance.dump('test_Grammar_dump_filename.txt')
    assert True


# Generated at 2022-06-13 17:56:16.684436
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))

# Generated at 2022-06-13 17:56:25.438816
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    # Initialize grammar

# Generated at 2022-06-13 17:56:36.104987
# Unit test for method load of class Grammar

# Generated at 2022-06-13 17:56:44.737209
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import io
    import pickle
    import sys
    class Grammar_load_Tests(unittest.TestCase):
        """Test load."""
        def test_00(self):
            """Test Grammar.load."""
            g = Grammar()

# Generated at 2022-06-13 17:56:46.330280
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    assert grammar.dump("test") is None

# Generated at 2022-06-13 17:56:56.149065
# Unit test for method load of class Grammar

# Generated at 2022-06-13 17:57:04.687803
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Dummy data for Grammar tables.
    symbol2number = {
        "'@'": 333,
        "'='": 78,
        "'t'": 213,
        "'f'": 141,
        "'x'": 267,
        "'y'": 275,
    }
    number2symbol = {num: sym for sym, num in symbol2number.items()}
    states = [
        [
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 4),
        ],
        [
            (3, 5),
            (3, 6),
            (3, 7),
        ]
    ]

# Generated at 2022-06-13 17:57:18.214593
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    import io
    import os
    import unittest
    from typing import IO

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.test_data_dir = os.path.dirname(os.path.abspath(__file__))
            self.grammar_filename = os.path.join(self.test_data_dir, ".grammar_dump.pickle")
        
        def tearDown(self):
            if os.path.exists(self.grammar_filename):
                os.remove(self.grammar_filename)

        def test_Grammar_dump(self):
            simple_grammar = Grammar()
            with open(self.grammar_filename, "wb") as f:
                simple_grammar.dump(f)


# Generated at 2022-06-13 17:57:24.989289
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import tempfile
    from typing import Any
    from .pgen2 import driver
    g = driver.load_grammar("Grammar.txt")
    with tempfile.NamedTemporaryFile("wb", delete=False) as f:
        g.dump(f.name)
    with open(f.name, "rb") as f:
        d = pickle.load(f)
    os.unlink(f.name)
    assert d.keys() == {
        "symbol2number",
        "number2symbol",
        "states",
        "dfas",
        "labels",
        "start",
    }

    # mypyc generates objects that don't have a __dict__, but they
    # are equivalent to one

# Generated at 2022-06-13 17:57:29.722141
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest.mock
    g = Grammar()
    g.dump = unittest.mock.Mock()
    g.loads(b"xyz")
    g.dump.assert_called_once_with("pgen_grammar.pickle")

# Generated at 2022-06-13 17:57:36.409927
# Unit test for method load of class Grammar
def test_Grammar_load():
    import tempfile
    import os
    from taxonomy import grammar
    testgrammar = grammar.Grammar()
    assert len(testgrammar.dfas)==0
    assert testgrammar.start == 256

    temppklpath = tempfile.mktemp()
    testgrammar.dump(temppklpath)
    testgrammar.load(temppklpath)
    assert len(testgrammar.dfas)==0
    assert testgrammar.start == 256
    os.remove(temppklpath)


# Generated at 2022-06-13 17:57:38.034875
# Unit test for method load of class Grammar
def test_Grammar_load():
    target = Grammar()
    target.test = "test"
    filename = "test_Grammar_load.pkl"
    target.dump(filename)
    new_target = Grammar()
    new_target.load(filename)
    assert new_target.test == target.test

# Generated at 2022-06-13 17:57:40.281780
# Unit test for method load of class Grammar
def test_Grammar_load():
    print("test Grammar load")
    parserGrammar = Grammar()
    parserGrammar.load("../Lib/pytest_test_grammar.txt")
    parserGrammar.report()


# Generated at 2022-06-13 17:57:53.318800
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr = Grammar()
    gr.load(os.path.join(os.path.dirname(__file__), "Grammar.txt"))
    assert gr.start == 256
    assert gr.symbol2number["single_input"] == 256
    assert gr.symbol2number["file_input"] == 257
    assert gr.symbol2number["eval_input"] == 258
    assert gr.symbol2number["decorator"] == 259
    assert gr.symbol2number["decorators"] == 260
    assert gr.symbol2number["decorated"] == 261
    assert gr.symbol2number["async_funcdef"] == 262
    assert gr.symbol2number["funcdef"] == 263
    assert gr.symbol2number["parameters"] == 264

# Generated at 2022-06-13 17:58:02.511136
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.start = 256
    g.dfas = {1: ([[(2, 3), (0, 1)]], {3: 1}), 256: ([[(1, 2), (0, 1)]], {2: 1})}
    g.symbol2label = {'NAME': 1}
    g.tokens = {3: 1}
    g.states = [[[(2, 3), (0, 1)], [(1, 2), (0, 1)], [(0, 3)]]]
    g.labels = [(0, None), (1, 'NAME'), (2, '<number>'), (3, '<number>')]
    g.number2symbol = {1: 'NAME'}
    g.symbol2number = {'NAME': 1}
    g.key

# Generated at 2022-06-13 17:58:17.228739
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    with open(os.path.join(os.path.dirname(__file__), "Grammar.txt"), "rb") as f:
        g.loads(f.read())
    assert g.symbol2number["expr"] == 258
    assert g.symbol2number["term"] == 259
    assert g.symbol2number["dotted_name"] == 260
    assert g.symbol2number["NAME"] == 262
    assert g.symbol2number["NUMBER"] == 263
    assert g.symbol2number["AT"] == 264
    assert g.symbol2number["COLON"] == 265
    assert g.number2symbol[258] == "expr"
    assert g.number2symbol[259] == "term"

# Generated at 2022-06-13 17:58:25.848101
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import io
    sys.stdout = io.StringIO()
    g = Grammar()
    g.dump("test")
    sys.stdout.getvalue()
    assert sys.stdout.getvalue() == ""
    sys.stdout = sys.__stdout__

# Generated at 2022-06-13 17:58:32.892109
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Test method load of class Grammar
    """
    import pickle
    import unittest

    class TestGrammar(unittest.TestCase):
        def test_load(self):
            # Test loading a pickled Grammar object is the same as
            # building a Grammar from scratch
            from .pgen2 import driver

            g = Grammar()
            pkl = pickle.dumps(g)
            g2 = Grammar()
            g2.loads(pkl)
            gp = driver.load_grammar("Grammar/Grammar.txt")
            self.assertEqual(g2.start, gp.start)
            self.assertEqual(g2.states, gp.states)
            self.assertEqual(g2.dfas, gp.dfas)

# Generated at 2022-06-13 17:58:41.779581
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pprint
    from .tok_name import tok_name

    # This is a bootstrap test, since this module itself is loaded
    # from a pickle file by the Grammar class.
    #
    # Also, the tables were originally written by Python 2.2, so this
    # test ensures that the tables can still be used by Python 2.1.

# Generated at 2022-06-13 17:58:48.995023
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    c = Grammar()
    c.number2symbol = {1: "test"}
    c.symbol2number = {"test": 1}
    c.states = [[(1, 2), (2, 0)]]
    c.dfas = {1: (0, {1: 2})}
    c.labels = [(1, "test")]
    c.keywords = {"test": 1}
    c.tokens = {1: 2}
    c.symbol2label = {"test": 1}
    c.start = 1
    with tempfile.NamedTemporaryFile() as f:
        c.dump(f.name)
        with open(f.name, "rb") as g:
            d = pickle.load(g)

# Generated at 2022-06-13 17:58:58.865719
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'.': 256}
    g.number2symbol = {256: '.'}
    g.states = [
        [
            [(0, 1)],  # state 0
            [(0, 2)]  # state 1
        ]
    ]
    g.dfas = {256: (0, {1: 1})}
    g.labels = [
        (0, 'EMPTY'),
        (1, None),
        (1, 'a')
    ]
    g.start = 256
    g.keywords = {'a': 2}
    g.tokens = {1: 2}
    g.symbol2label = {'.': 256}
    with open('temp.txt', 'r+b') as file:
        g.dump

# Generated at 2022-06-13 17:59:04.286366
# Unit test for method load of class Grammar
def test_Grammar_load():

    # Create a file containing test data
    with open("test.pickle", "wb") as f:
        pickle.dump({"data": 100}, f)

    # Load the test data
    g = Grammar()
    g.load("test.pickle")

    # Check that the loaded data is valid
    assert(g.data == 100)

# Generated at 2022-06-13 17:59:07.185728
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert Grammar().load.__doc__ == """Load the grammar tables from a pickle file."""

# Generated at 2022-06-13 17:59:16.599270
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import pytree
    from .python import PythonParser
    from .pgen2 import tokenize

    class PythonGrammarTest(unittest.TestCase):
        def test_single_input(self):
            parser = PythonParser()
            filename = "test.py"
            file_contents = "print('test')\n"
            lexer = tokenize.generate_tokens(file_contents.__iter__().__next__)
            tree = parser.parse(lexer, debug=False)
            self.assertTrue(isinstance(tree, pytree.Node))

    suite = unittest.TestLoader().loadTestsFromTestCase(PythonGrammarTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 17:59:28.116343
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:59:29.378024
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    assert g.dump("foo") == None