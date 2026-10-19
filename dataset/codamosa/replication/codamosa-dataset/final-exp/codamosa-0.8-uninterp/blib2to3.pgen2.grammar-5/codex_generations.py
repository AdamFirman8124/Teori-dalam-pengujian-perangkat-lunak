

# Generated at 2022-06-13 17:49:59.432917
# Unit test for method load of class Grammar
def test_Grammar_load():
    def assert_grammar_loaded(g: Grammar) -> None:
        assert g.symbol2number, "Variable symbol2number contains no data."
        assert g.number2symbol, "Variable number2symbol contains no data."
        assert g.states, "Variable states contains no data."
        assert g.dfas, "Variable dfas contains no data."
        assert g.keywords, "Variable keywords contains no data."
        assert g.tokens, "Variable tokens contains no data."
        assert g.labels, "Variable labels contains no data."
        assert g.symbol2label, "Variable symbol2label contains no data."
        assert g.start, "Variable start contains no data."

    from . import conv

    gr_file = "Grammar.pkl"
    conv.parse_grammar(gr_file)


# Generated at 2022-06-13 17:50:02.116534
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gr = Grammar()
    fname = "../Grammar.pkl"
    gr.dump(fname)
    gr.load(fname)

# Generated at 2022-06-13 17:50:16.057616
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class MockGrammar(Grammar):
        """
        A mock grammar containing the minimum state necessary for
        the Grammar.dump() to execute.
        """
        def __init__(self):
            super().__init__()
            self.start = 10
            self.symbol2number = {':=': 5}
            self.number2symbol = {5: ':='}
            self.states = [[[]]]
            self.dfas = {5: ([[(5, 0)]] , {0: 0})}
            self.labels = [(5, ':=')]
            self.keywords = {}
            self.tokens = {}
            self.symbol2label = {':=': 5}

    grammar = MockGrammar()
    file_name = "/tmp/test"


# Generated at 2022-06-13 17:50:19.888901
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2.pgen import driver
    d = driver.Driver()
    g = d.load_grammar("./Grammar/Grammar")
    g.dump("./Grammar/Grammar.pickle")

if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:50:22.869833
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Grammar.dump should create a file that is pickleable."""
    grammar = Grammar()
    grammar.dump("test_Grammar.pickle")
    grammar2 = Grammar()
    grammar2.load("test_Grammar.pickle")
    assert grammar.__dict__ == grammar2.__dict__

# Generated at 2022-06-13 17:50:25.854303
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import doctest
    import unittest
    from .pgen2 import tokenize

    class T(unittest.TestCase):
        def runTest(self):
            doctest.testmod(tokenize)

    T().runTest()

# Generated at 2022-06-13 17:50:27.804658
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest

    unittest.TestCase.assertEqual(Grammar.load, Grammar().load)

# Generated at 2022-06-13 17:50:30.968209
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    # Print dump file name on standard output
    dump_file_name = g.dump('Grammar.dmp')
    print('Dump file name:', dump_file_name)

if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:50:37.700682
# Unit test for method load of class Grammar
def test_Grammar_load():
    def foo():
        d = {}
        d["symbol2number"] = {}
        d["number2symbol"] = {}
        d["dfas"] = {}
        d["keywords"] = {}
        d["tokens"] = {}
        d["symbol2label"] = {}
        d["labels"] = [(0, "EMPTY")]
        d["states"] = []
        d["start"] = 256
        return d

    class GrammarSub(Grammar):
        def __init__(self, a: Dict[str, Any]) -> None:
            super().__init__()
            self._update(a)

    a = foo()
    g = GrammarSub(a)
    g.dump("test.pkl")
    g = GrammarSub(foo()) # init again
    g.load

# Generated at 2022-06-13 17:50:41.687469
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = os.path.join(os.path.dirname(__file__), "Grammar.test")
    g = Grammar()
    assert not g.symbol2number

    g.dump(filename)
    g = Grammar()
    assert not g.symbol2number
    g.load(filename)
    assert g.symbol2number

# Generated at 2022-06-13 17:50:55.861517
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test coverage only
    tables_path = "./test_tokenize/tokenizer_test_data/test_pgen_tables"
    import os
    import pickle
    gram = Grammar()
    gram.load(tables_path)
    gram.dump("temp")
    gram = Grammar()
    gram.load("temp")
    os.remove("temp")
    assert isinstance(gram.states, list)
    assert len(gram.symbol2number) == 51
    assert isinstance(gram.number2symbol, dict)
    assert isinstance(gram.dfas, dict)
    assert isinstance(gram.keywords, dict)
    assert isinstance(gram.tokens, dict)
    with open(tables_path, "rb") as f:
        expected = pickle.load(f)

# Generated at 2022-06-13 17:51:05.084893
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import os
    import unittest
    import pgen2
    import pgen2.parse
    import pgen2.grammar

    def remove_files(files):
        for f in files:
            # use os.path.exists, not pathlib.Path.exists
            if os.path.exists(f):
                os.remove(f)

    class Pgen2TestCase(unittest.TestCase):

        def setUp(self):
            self._stdout = sys.stdout
            sys.stdout = self._buffer = pgen2.parse.StringIO()

            self.pkl_file = 'test_pgen2.pickle'
            self.pg_file = 'test_pgen2.pg'


# Generated at 2022-06-13 17:51:17.442356
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    s = b"cos\nsystem\n(S'ls'\ntR."

    g.loads(s)
    assert g.symbol2number == {"None": 256, "False": 257, "True": 258}
    assert g.number2symbol == {256: "None", 257: "False", 258: "True"}

# Generated at 2022-06-13 17:51:25.394629
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    from test.support import run_unittest
    from .tokenize import detect_encoding, TokenInfo

    source = 'def f(x):\n return x+2\n'
    encoding = detect_encoding(source.encode())
    tokens = list(tokenize(source.encode(), encoding))
    # The tokenize test suite ensures that the tokens are generated
    # correctly.
    class TestGrammar(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.symbol2number = {'foo': 256, 'bar': 257}
            self.number2symbol = {256: 'foo', 257: 'bar'}
            self.states = [[[(257, 0), (0, 0)]]]

# Generated at 2022-06-13 17:51:28.142857
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__.replace('.py', '.pkl'))
    g.report()


# Generated at 2022-06-13 17:51:32.645088
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"a": 3}
    g.number2symbol = {1: "b", 2: "c"}
    g.states = [[[(3, 4), (3, 5)]], [[(8, 6), (8, 7)]]]

# Generated at 2022-06-13 17:51:40.755709
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickle
    from pprint import pprint

    d = {}

# Generated at 2022-06-13 17:51:44.142241
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2

    parser = pgen2.tokenize.generate_grammar()
    parser.dump("Lib/test/grammar.txt")

# Generated at 2022-06-13 17:51:53.923733
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def check_data(data, expected):  # type: (Any, Dict[str, Any]) -> None
        for k, v in expected.items():
            assert v == data[k]
        assert len(expected) == len(data)

    pkl_filename = tempfile.mktemp("g.pkl")
    orig_grammar = Grammar()
    orig_grammar.dump(pkl_filename)
    loaded_grammar = Grammar()
    loaded_grammar.load(pkl_filename)
    expected_data = vars(orig_grammar)
    actual_data = vars(loaded_grammar)
    check_data(actual_data, expected_data)

# Generated at 2022-06-13 17:52:01.944536
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pygram

    d = {"foo" : "bar"}

    with tempfile.NamedTemporaryFile() as f:
        pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
        g = pygram.python_grammar
        g.load(f.name)

    assert g.symbol2number == d

    g = pygram.python_grammar
    g.loads(pickle.dumps(d, pickle.HIGHEST_PROTOCOL))

    assert g.symbol2number == d


# Generated at 2022-06-13 17:52:14.437425
# Unit test for method load of class Grammar
def test_Grammar_load():
    tokenize = token.tokenize
    g = Grammar()
    g1 = g.copy()


# Generated at 2022-06-13 17:52:23.234566
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    from .pgen2 import driver

    g = Grammar()
    assert g.dump(os.path.join(os.path.dirname(__file__), 'Grammar.dump')) is None
    assert g.load(os.path.join(os.path.dirname(__file__), 'Grammar.dump')) is None
    os.unlink(os.path.join(os.path.dirname(__file__), 'Grammar.dump'))

    pkl = pickle.dumps(g, pickle.HIGHEST_PROTOCOL)
    g.loads(pkl)
    assert driver.completed == 0

    g.report()

# Generated at 2022-06-13 17:52:30.418151
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    from .pgen2 import driver

    driver.generate_grammar("Grammar/Grammar.test.py")

    filename = "Grammar/Grammar.test.pkl"
    if os.path.exists(filename):
        os.remove(filename)

    gr = driver.load_grammar("Grammar/Grammar.test.py")
    gr.dump(filename)

    with open(filename, "rb") as f:
        data = f.read()
    assert data

    os.remove(filename)

# Generated at 2022-06-13 17:52:35.143025
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import Convert

    g = Grammar()
    Convert(g).make_grammar(open("Grammar.txt"))
    g.report()

    filename = "Grammar.pkl"
    g.dump(filename)
    g2 = Grammar()
    g2.load(filename)
    assert g == g2
    os.remove(filename)

# Generated at 2022-06-13 17:52:39.055852
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.symbol2number = {"sym": 0}
    with tempfile.NamedTemporaryFile() as f:
        g.dump(f.name)
        g2 = Grammar()
        g2.load(f.name)
        assert g2.symbol2number == g.symbol2number
        assert g2.symbol2number is not g.symbol2number

# Generated at 2022-06-13 17:52:50.675990
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert
    g = Grammar()
    g.load = test_Grammar_load.__globals__["load"]
    g.loads = test_Grammar_load.__globals__["loads"]
    convert(g, opmap)  # Fill in some data
    f = tempfile.TemporaryFile(mode="w+b")
    g.dump(f)
    f.seek(0, 0)
    h = Grammar()
    h.load(f)
    assert g.symbol2number == h.symbol2number
    assert g.number2symbol == h.number2symbol
    assert g.states == h.states
    assert g.dfas == h.dfas
    assert g.labels == h.labels
    assert g.start == h.start


# Generated at 2022-06-13 17:52:52.937743
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    assert len(grammar.states) == 0
    grammar.load(__file__)
    assert len(grammar.states) == 0


# Generated at 2022-06-13 17:52:58.407561
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver
    from .pgen2 import tokenize
    from . import token

    from . import parsetok

    # Parse a grammar file and return a Grammar object
    def parse_grammar(filename: Path) -> Grammar:
        with open(filename, "rb") as f:
            encoding, lines = tokenize.detect_encoding(f.readline)
        f.seek(0)
        parser = driver.ParserDriver(
            parsetok.parsetok, token.tok_name, filename, encoding
        )
        return parser.parse_tokens(tokenize.generate_tokens(f.readline))

    # Test parsing a single file
    def test_grammar(filename: Path) -> None:
        grammar = parse_grammar(filename)
        grammar

# Generated at 2022-06-13 17:53:08.428308
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class CustomGrammar(Grammar):
        def __init__(self) -> None:
            self.symbol2number = {}
            self.number2symbol = {}
            self.states = []
            self.dfas = {}
            self.labels = [(0, "EMPTY")]
            self.keywords = {}
            self.tokens = {}
            self.symbol2label = {}
            self.start = 256
            self.async_keywords = False

    # Test without __dict__ attribute
    grammar = CustomGrammar()
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "custom.pgen")
        grammar.dump(filename)
        grammar2 = CustomGrammar()
        grammar2.load(filename)

# Generated at 2022-06-13 17:53:20.422027
# Unit test for method load of class Grammar
def test_Grammar_load():
    def check(pkl_file):
        g = Grammar()
        g.load(pkl_file)
        assert g.symbol2number["unary_expr"] == 258
        assert g.number2symbol[258] == "unary_expr"
        assert g.states[3][3][0][0] == token.NAME
        assert g.states[3][3][0][1] == 4
        assert g.dfas[258][1][token.NAME] == 1
        assert g.dfas[258][1][token.AWAIT] == 1
        assert g.labels[6][1] == "AWAIT"
        assert g.keywords["False"] == 8
        assert g.tokens[token.NAME] == 4
    base = os.path.dirname(__file__)
   

# Generated at 2022-06-13 17:53:29.626012
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest.mock
    import pickle
    with tempfile.NamedTemporaryFile() as f:
        with unittest.mock.patch('pickle.dump') as mock_dump:
            mock_dump.return_value = None
            Grammar.dump(None, f.name)
            mock_dump.assert_called_once()

# Generated at 2022-06-13 17:53:37.953661
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'foo': 1, 'bar': 2, 'baz': 3}
    g.number2symbol = {1: 'foo', 2: 'bar', 3: 'baz'}
    g.states = []
    g.dfas = {1: ([], {1: 1}), 2: ([], {2: 1}), 3: ([], {3: 1})}
    g.labels = [(0, 'EMPTY')]
    g.keywords = {'foo': 1, 'bar': 2, 'baz': 3}
    g.tokens = {1: 1, 2: 2, 3: 3}
    g.symbol2label = {'foo': 4, 'bar': 5, 'baz': 6}
    g.start = 96
   

# Generated at 2022-06-13 17:53:43.671414
# Unit test for method load of class Grammar
def test_Grammar_load():
    with tempfile.TemporaryDirectory() as tmpdir:
        grammar = Grammar()
        with open(os.path.join(tmpdir, "Grammar.pkl"), "wb") as pkl:
            pickle.dump(grammar.__dict__, pkl, pickle.HIGHEST_PROTOCOL)

        grammar2 = Grammar()
        grammar2.load(os.path.join(tmpdir, "Grammar.pkl"))
        assert grammar.symbol2number == grammar2.symbol2number


# Generated at 2022-06-13 17:53:52.405621
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import conv, pgen
    import contextlib
    import io

    with contextlib.redirect_stderr(io.StringIO()):
        g = conv.convert("Grammar.txt")
    g.report()
    g.dump("Grammar.pkl")
    g2 = pgen.load_grammar("Grammar.pkl")
    g2.report()


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:53:58.382657
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from tempfile import mktemp

    from . import pgen

    try:
        from test.support import temp_dir
    except ImportError:
        from test.test_support import temp_dir

    name = mktemp(dir=temp_dir)
    # Test external function dump in Grammar
    pgen.dump_grammar(name)
    # Test method dump in Grammar
    pgen.load_grammar(name).dump(name)

# Generated at 2022-06-13 17:54:07.580114
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    with tempfile.NamedTemporaryFile() as f:
        grammar.dump(f.name)
        grammar.load(f.name)
        assert grammar.symbol2number == {}
        assert grammar.number2symbol == {}
        assert grammar.states == []
        assert grammar.dfas == {}
        assert grammar.labels == [(0, "EMPTY")]
        assert grammar.keywords == {}
        assert grammar.tokens == {}
        assert grammar.symbol2label == {}
        assert grammar.start == 256
        assert grammar.async_keywords == False

# Generated at 2022-06-13 17:54:12.855863
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    if __name__ == "__main__":
        import sys
        import unittest


        class TestGrammar(unittest.TestCase):
            def test_dump(self):
                path = f"{sys.executable}-Grammar.pickle"
                try:
                    g = Grammar()
                    g.dump(path)
                finally:
                    os.remove(path)


        unittest.main()

# Generated at 2022-06-13 17:54:21.920362
# Unit test for method load of class Grammar
def test_Grammar_load():
    import os
    import pickle

    g = Grammar()
    g.loads(pickle.dumps(g))

    g.symbol2number = {0:1}
    g.number2symbol = {0:1}
    g.states = [0]
    g.dfas = {0:0}
    g.labels = [0]
    g.keywords = {"0":0}
    g.tokens = {0:0}
    g.symbol2label = {0:1}
    g.start = 1
    g.async_keywords = True
    g.dump(os.path.join(os.path.curdir, "grammar"))
    g.load(os.path.join(os.path.curdir, "grammar"))

# Generated at 2022-06-13 17:54:25.241052
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Test grammartable method dump.
    """
    st = Grammar()

    temp_file = tempfile.NamedTemporaryFile()
    st.dump(temp_file.name)



# Generated at 2022-06-13 17:54:34.474743
# Unit test for method load of class Grammar
def test_Grammar_load():
    obj = Grammar()
    obj.load("Grammar.pickle")
    assert obj.symbol2number == {"*": 265, "*=": 265, "/": 266, "/=": 266}
    assert obj.number2symbol == {265: "*", 266: "/"}
    assert obj.states == [[[(1, 1), (2, 1)]], [[(1, 1), (0, 2)]], [[(0, 1)]]]
    assert obj.dfas == {257: ([[(1, 1), (2, 1)]], {1: 1}), 260: ([[(1, 1), (0, 2)]], {1: 1})}
    assert obj.labels == [(0, "EMPTY"), (257, "<token>"), (260, "/"), (261, "EMPTY")]
    assert obj

# Generated at 2022-06-13 17:54:54.372867
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    class TestGrammar(Grammar):
        def __init__(self, filename: Path = '/tmp/test_grammar.pkl') -> None:
            Grammar.__init__(self)
            self.filename = filename
            self.symbol2number = {'test': 256}
            self.number2symbol = {256: 'test'}
            self.states = [[[(0, 0)]]]
            self.dfas = {256: ([[(0, 0)]], {0: 'test'})}
            self.labels = [(0, 'EMPTY'), (256, 'test')]
            self.keywords = {'test': 256}
            self.tokens = {256: 256}
            self.symbol2label = {'test': 256}

# Generated at 2022-06-13 17:55:03.083150
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    assert grammar
    s2n = {"a": 1, "b": 2, "c": 3}
    grammar.symbol2number = s2n
    assert grammar.symbol2number is s2n

    filename = os.path.join(tempfile.gettempdir(), "grammar.pkl")
    try:
        grammar.dump(filename)
        grammar2 = Grammar()
        grammar2.load(filename)
        assert grammar2.symbol2number == s2n
    finally:
        try:
            os.remove(filename)
        except EnvironmentError:
            pass

# Generated at 2022-06-13 17:55:12.615327
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickletools
    import py_compile
    from parse_tree import pytree
    from compile import compile
    from grammar_parser import grammar

    g = grammar()
    g.parse_grammar("""
      calc: atom {print("atom")}
           | atom "+" calc {print("add")}
           | atom "-" calc {print("sub")}
           | calc "*" calc {print("mul")}
           | calc "/" calc {print("div")}
      atom: "(" calc ")"
           | "[" calc "]"
           | "{" calc "}"
           | "(" calc ")" calc
           | num
      num: /\d+/ {print("num")}
    """)
    g.start = "calc"
    g.calc_parse_table()
    grammar_file

# Generated at 2022-06-13 17:55:21.798734
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    import tempfile

    class GrammarTest(unittest.TestCase):

        def test_dump(self):
            grammar = Grammar()
            grammar.symbol2number = {
                'foo': 257,
                'bar': 258,
                'foobar': 259,
            }
            grammar.number2symbol = {
                257: 'foo',
                258: 'bar',
                259: 'foobar'
            }
            grammar.states = [
                [
                    [(256, 257), (0, 1)],
                    [(257, 2), (0, 1)],
                    [(0, 3)],
                ],
            ]

# Generated at 2022-06-13 17:55:30.683399
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import graminit

    g = graminit.Grammar()

    def load():
        g.load(TESTFN)

    def loads():
        g.loads(pkl)

    pkl = g.dumps()

# Generated at 2022-06-13 17:55:31.824059
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("/tmp/Grammar")


# Generated at 2022-06-13 17:55:33.795251
# Unit test for method load of class Grammar
def test_Grammar_load():
    gram = Grammar()
    gram.load(os.path.join(os.path.dirname(__file__), 'Grammar.pkl'))

# Generated at 2022-06-13 17:55:35.423871
# Unit test for method load of class Grammar
def test_Grammar_load():
    import ast
    import io
    import pickle
    import sys

    _Grammar_load()


# Generated at 2022-06-13 17:55:39.370655
# Unit test for method load of class Grammar
def test_Grammar_load():
    # test_Grammar_load_non_existing
    # This is supposed to throw an IOError
    grammar = Grammar()
    grammar.load('non-existing')

# Generated at 2022-06-13 17:55:41.080212
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump('test.pkl')

# Generated at 2022-06-13 17:55:55.206904
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import sys
    from io import StringIO
    from contextlib import redirect_stdout

    class TestGrammar(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.symbol2number = {'NAME': 26, 'NUMBER': 7, 'STRING': 8}
            self.number2symbol = {26: 'NAME', 7: 'NUMBER', 8: 'STRING'}

# Generated at 2022-06-13 17:56:02.592798
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pgen2
    from . import tokenize
    from .pgen2 import pgen

    g = pgen2.driver.load_grammar(pgen.GRAMMAR_FILE)

    grammar = Grammar()
    grammar.load(g)

    endmarker = grammar.number2symbol[1]

    assert isinstance(endmarker, str)

    start = grammar.number2symbol[256]

    assert isinstance(start, str)

    dfas = grammar.dfas
    start_dfa, firsts = dfas[256]
    assert start_dfa[0][0][1] == 4

    # Check token behavior is correct

# Generated at 2022-06-13 17:56:13.524321
# Unit test for method load of class Grammar

# Generated at 2022-06-13 17:56:22.741985
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test that Grammar.dump() generates a pickle file for the given object."""
    import io
    import pickle
    from ast import ClassDef

    g = Grammar()
    g.tokens[token.NAME] = 0
    g.tokens[token.NL] = 1
    assert g.tokens == {token.NAME: 0, token.NL: 1}

    with io.BytesIO() as f:
        g.dump(f)
        pickle_content = f.getvalue()

    loaded_g = pickle.loads(pickle_content)
    assert loaded_g.tokens == {token.NAME: 0, token.NL: 1}

    # Make sure this round-trips with pgen:
    from .pgen2 import tokenize


# Generated at 2022-06-13 17:56:29.845651
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import grammar
    from . import pgen2
    from . import pgen

    g = pgen2.driver.load_grammar(grammar.grammar)
    pp = pprint.PrettyPrinter(width=70, compact=True)

    def show(obj, name=""):
        print(name, "=")
        pp.pprint(obj)
        print()

    show(g.symbol2number, "Symbol2number")
    show(g.number2symbol, "Number2symbol")
    show(g.labels, "Labels")
    show(g.start, "Start")
    show(g.states, "States")
    show(g.dfas, "Dfas")

    g.report()
    pkl = g.dumps()
    pg = pgen.G

# Generated at 2022-06-13 17:56:33.394627
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Grammar.dump(str) should create a pickle.
    """
    grammar = Grammar()
    path = './dump_test.pkl'
    grammar.dump(path)
    assert os.path.exists(path)
    os.remove(path)

# Generated at 2022-06-13 17:56:39.650352
# Unit test for method dump of class Grammar
def test_Grammar_dump():

    def dump(cls: type) -> None:
        g = cls()
        g.dump("Grammar.dump")
        print(cls.__name__, ":", open("Grammar.dump", "rb").read())

    from . import pgen

    class PgenGrammar(pgen.Generator):
        pass

    dump(PgenGrammar)
    dump(Grammar)


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:56:47.518535
# Unit test for method load of class Grammar
def test_Grammar_load():
    g1 = Grammar()
    g1.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))

    assert g1.symbol2number
    assert g1.number2symbol
    assert g1.dfas
    assert g1.keywords
    assert g1.tokens
    assert g1.labels
    assert g1.states
    assert g1.symbol2label

# Generated at 2022-06-13 17:56:49.446206
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))

# Generated at 2022-06-13 17:56:58.695437
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    >>> paths = [os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Lib', 'asdl')]
    >>> grammar = Grammar()
    >>> grammar._update(Converter("Grammar.tx", "Grammar.asdl", paths).run())
    >>> grammar.startSymbol = "file_input"
    >>> grammar.async_keywords = True
    >>> if sys.version_info[:2] >= (3, 5):
    ...     f = open(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Lib', 'grammar.py'), 'rb')
    ...     grammar.load(f)
    ...     f.close()
    """
    pass


# Generated at 2022-06-13 17:57:19.447802
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 1
    g.dfas = {1: ([[(1, 2)], [(1, 3)]], [])}
    g.tokens = {1: 1}
    g.labels = [(1, "one"), (2, "two"), (3, "three")]
    g.states = [[[(1, 1), (2, 2)], [(3, 3)]], [[(1, 1), (2, 2)]]]
    g.keywords = {"one": 1}
    g.symbol2number = {"one": 2}
    g.number2symbol = {1: "one", 2: "two"}
    g.symbol2label = {"one": 1, "two": 2}

    g2 = Grammar()
    g2.start = 1


# Generated at 2022-06-13 17:57:26.892777
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Tests Grammar.dump()
    import copy
    import tempfile
    import tokenize
    import parse
    import pickle
    import io
    import sys
    import os

    class TestGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.symbol2number = {"":""}
            self.number2symbol = {"":""}
            self.states = [""]
            self.labels = [("", "")]
            self.start = 256

    tg = TestGrammar()
    p = parse.Parser(copy.deepcopy(tg))
    with tempfile.TemporaryDirectory() as tmpdirname:
        token_gen = tokenize.tokenize(io.BytesIO(b"1+1").readline)
        # Check that changing the grammar of

# Generated at 2022-06-13 17:57:36.373455
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    import tempfile
    import pickletools


# Generated at 2022-06-13 17:57:40.379578
# Unit test for method load of class Grammar
def test_Grammar_load():
    class T(Grammar):
        pass

    t = T()
    t.start = 0
    t.number2symbol = {0: "foo"}
    t.dump("tmp.txt")
    t1 = T()
    t1.load("tmp.txt")
    assert t1.start == 0
    assert t1.number2symbol == {0: "foo"}

# Generated at 2022-06-13 17:57:48.892021
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr = Grammar()
    gr.load("Grammar.txt")
    print("s2n")
    print(gr.symbol2number)
    print("n2s")
    print(gr.number2symbol)
    print("states")
    print(gr.states)
    print("dfas")
    print(gr.dfas)
    print("labels")
    print(gr.labels)
    print("start", gr.start)


# Generated at 2022-06-13 17:57:53.651108
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test the method Grammar.dump"""
    filename = os.path.join(tempfile.gettempdir(), "grammar_dump.pickle")
    grammar = Grammar()
    grammar.dump(filename)

# Generated at 2022-06-13 17:58:02.661365
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2.parse
    import sys
    import shutil
    fname = "Grammar.dump.tmp"
    pgen2.parse.compile_grammar(sys.argv[1], test_Grammar_dump)
    for g in pgen2.parse.grammar:
        g.dump(fname)
    with open(fname, "rb") as f:
        pkl = f.read()
    g2 = Grammar()
    g2.loads(pkl)
    if not g2.states:
        raise AssertionError("parsing grammar not loaded")
    os.remove(fname)

if __name__ == "__main__":
    import pgen2.parse
    import sys

# Generated at 2022-06-13 17:58:16.571795
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Unit test for method dump of class Grammar"""
    g = Grammar()
    g.dump("/tmp/Grammar_unittest.pkl")
    g2 = Grammar()
    g2.load("/tmp/Grammar_unittest.pkl")
    assert g2.symbol2number == {}
    assert g2.number2symbol == {}
    assert g2.states == []
    assert g2.dfas == {}
    assert g2.labels == [(0, "EMPTY")]
    assert g2.keywords == {}
    assert g2.tokens == {}
    assert g2.symbol2label == {}
    assert g2.start == 256

# Generated at 2022-06-13 17:58:19.036912
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import Conv
    from .pgen import generate_grammar

    # Create a grammar
    g = Conv(generate_grammar()).grammar

    # Dump it
    g.dump('grammar.pickle')


# Generated at 2022-06-13 17:58:29.895734
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2
    import test.test_grammar
    test.test_grammar.parse_grammar(pgen2.Grammar())
    import filecmp
    import os
    import shutil
    import tempfile
    tmpdir = os.path.join(tempfile.gettempdir(), "test_Grammar_dump")
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)
    os.mkdir(tmpdir)
    testfilename = os.path.join(tmpdir, "testgrammar.pickle")
    g = pgen2.Grammar(start="file_input")
    g.dump(testfilename)
    picklename = os.path.join(os.path.split(__file__)[0], "Grammar.pickle")


# Generated at 2022-06-13 17:58:47.695418
# Unit test for method load of class Grammar
def test_Grammar_load():
    import doctest
    doctest.testmod()


# Generated at 2022-06-13 17:58:57.088429
# Unit test for method load of class Grammar
def test_Grammar_load():
    gram = Grammar()
    gram.load(os.path.join(
        os.path.dirname(__file__), "Grammar.pkl"
    ))
    assert gram.number2symbol[256] == 'fas'
    assert gram.number2symbol[257] == 'fas1'
    assert gram.number2symbol[258] == 'fas2'
    assert gram.number2symbol[259] == 'fas3'
    assert gram.number2symbol[260] == 'fas4'
    assert gram.number2symbol[261] == 'fas5'
    assert gram.number2symbol[262] == 'fas6'
    assert gram.number2symbol[263] == 'fas7'

# Generated at 2022-06-13 17:59:04.525657
# Unit test for method dump of class Grammar

# Generated at 2022-06-13 17:59:09.318667
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickletools

    g = Grammar()
    g.symbol2number = {"foo": 1, "bar": 2}
    g.number2symbol = {1: "foo", 2: "bar"}
    g.states = [[(257, [258, 259]), (260, 1)]]
    g.dfas = {1: (0, {257: 1})}
    g.labels = [(0, "EMPTY"), (257, None), (258, None), (259, None), (260, None)]
    g.keywords = {"foo": 257}
    g.tokens = {1: 260}
    g.symbol2label = {"foo": 257}
    g.start = 1


# Generated at 2022-06-13 17:59:14.264896
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # If a grammar file does not exist, dump() should raise FileNotFoundError
    grammar = Grammar()
    fn = "grammar_non_existing.pkl"
    try:
        grammar.dump(fn)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("FileNotFoundError not raised for non-existing grammar file")

# Generated at 2022-06-13 17:59:25.991368
# Unit test for method load of class Grammar
def test_Grammar_load():
    #The Grammar class is only for internal use by the tokenizer, but it
    #is tested here to have 100% branch coverage of its load method.
    from types import ModuleType
    mod = ModuleType("tokenize_grammar")
    g = Grammar()

    #Test branch where the loaded module has a __dict__ attribute
    mod.__dict__ = {"symbol2number":{}, "number2symbol":{},
                    "states":[], "dfas":{}, "labels":[], "keywords":{},
                    "tokens":{}, "symbol2label":{}, "start":256}
    Grammar.load(g, mod)
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert g.states == []
    assert g.dfas == {}

# Generated at 2022-06-13 17:59:28.766043
# Unit test for method load of class Grammar
def test_Grammar_load():
    try:
        import parser
    except ImportError:
        import _parser as parser

    g = parser.Grammar()
    g.load(os.path.join(os.path.dirname(__file__), "Grammar.pickle"))

# Generated at 2022-06-13 17:59:39.757852
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io
    import os
    import pickle
    import sys

    from .pgen2 import driver

    # this routine also tests the driver module's function load_grammar()
    def do_test(grammar_file: Path, pickle_file: Path) -> None:
        if os.path.exists(pickle_file):
            os.unlink(pickle_file)
        driver.load_grammar(grammar_file)
        if not os.path.exists(pickle_file):
            raise RuntimeError(f"{pickle_file!r} not created")
        with open(pickle_file, "rb") as f:
            d1 = pickle.load(f)
        f = io.BytesIO()

# Generated at 2022-06-13 17:59:43.757223
# Unit test for method load of class Grammar
def test_Grammar_load():
    class MyGrammar(Grammar):
        def __init__(self):
            super(MyGrammar, self).__init__()
            self.hello = "Hello World!"

    s = MyGrammar()
    with tempfile.TemporaryFile() as f:
        s.dump(f)
        f.seek(0)
        s2 = MyGrammar()
        s2.load(f)
        assert s.hello == s2.hello

# Generated at 2022-06-13 17:59:48.723352
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import tempfile
    import contextlib

    class CustomGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.a = '\0'
            self.b = "\x03"
            self.c = b"\x03"

    temp_dir = tempfile.gettempdir()
    g = CustomGrammar()
    g.dump(os.path.join(temp_dir, 'test_dump'))
    with contextlib.suppress(FileNotFoundError):
        os.remove(os.path.join(temp_dir, 'test_dump'))