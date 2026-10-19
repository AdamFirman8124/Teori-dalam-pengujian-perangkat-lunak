

# Generated at 2022-06-13 17:49:54.876833
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest
    from . import conv
    from . import S

    sample = """
    a: A b B
    b: C x | D y
    x: E
    y: x | F
    """

    p = conv.Converter()
    p.parse_grammar(sample)
    g = p.grammar

    # n2s and s2n should be the same.
    for k, v in g.symbol2number.items():
        assert g.number2symbol[v] == k

    # labels
    assert g.labels[0] == (0, "EMPTY")
    assert g.labels[-1] == (token.NAME, "F")
    assert g.labels[-2] == (g.symbol2number["x"], None)
    assert g.labels

# Generated at 2022-06-13 17:50:03.440025
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'foo': 2}
    g.number2symbol = {3: 'bar'}
    g.states = [[(1,2), (3,4)]]
    g.labels = [('a', None), 'b', (b'c', 'd')]

    f = './Grammar_dump.txt'
    g.dump(f)
    h = Grammar()
    h.load(f)
    assert g.symbol2number == h.symbol2number
    assert g.number2symbol == h.number2symbol
    assert g.states == h.states
    assert g.labels == h.labels


# Generated at 2022-06-13 17:50:06.522045
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    fd, fname = tempfile.mkstemp()
    os.close(fd)
    try:
        g.dump(fname)
    finally:
        os.remove(fname)

# Generated at 2022-06-13 17:50:17.943434
# Unit test for method dump of class Grammar
def test_Grammar_dump():

    import unittest
    import warnings
    import os
    import sys
    import pickle
    import tempfile
    import shutil

    class TestGrammar_dump(unittest.TestCase):

        def setUp(self):
            self.work_dir = tempfile.mkdtemp(prefix="test_Grammar_dump")
            self.grammar_file = os.path.join(self.work_dir,"grammar.pkl")

        def tearDown(self):
            shutil.rmtree(self.work_dir)

        def test_Grammar_dump(self):
            self.assertTrue(False)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestGrammar_dump)
    unittest.TextTestRunner().run(suite)



# Generated at 2022-06-13 17:50:25.305555
# Unit test for method load of class Grammar
def test_Grammar_load():
    import ast
    import io

    # Initialize symbols and keywords
    symbols = ["STRING", "NAME"]
    keywords = ast.__dict__.copy()
    for name in dir(token):
        if name.isupper():
            value = getattr(token, name)
            if value <= token.NT_OFFSET:
                keywords[name.lower()] = value

    # Create a grammar object
    grammar = Grammar()
    grammar.symbol2number = {symbol: n for n, symbol in enumerate(symbols)}
    for n, symbol in enumerate(symbols, grammar.start):
        grammar.number2symbol[n] = symbol
    for k, v in keywords.items():
        grammar.symbol2label[k] = v

# Generated at 2022-06-13 17:50:27.720465
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__.rstrip("c") + "pickle")
    return g

# Generated at 2022-06-13 17:50:35.061718
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    "Unit test for method dump of class Grammar"

    import unittest
    import ast, astroid
    class TestGrammarDumpCase(unittest.TestCase):
        def setUp(self):
            self.g=Grammar()
            self.g.start=1
            self.g.states=[['a','b'],['c','d']]
            self.g.keywords=ast.literal_eval('{"a":1,"b":1,"c":1,"d":1}')
            self.g.dfas={"b.B":(['c','d'],"b.B")}
            self.g.number2symbol=ast.literal_eval('{"b.B":2}')

# Generated at 2022-06-13 17:50:43.979935
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import unittest
    import warnings

    msg = r"unsupported Python 3\.8 features.*"
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", msg, category=DeprecationWarning)
        import pgen2.grammar

    class TestGrammar(pgen2.grammar.Grammar):

        def __init__(self) -> None:
            super().__init__()
            self.test_attr = "test"

    class GrammarDumpTests(unittest.TestCase):

        grammar = TestGrammar()

        def setUp(self) -> None:
            self.grammar.dump("/tmp/test.pickle")

        def tearDown(self) -> None:
            os.remove("/tmp/test.pickle")


# Generated at 2022-06-13 17:50:55.064214
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    filename = os.path.join(tempfile.gettempdir(),"_tmp_grammar.pkl")

# Generated at 2022-06-13 17:50:58.401306
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Make an empty grammar
    from . import grammar
    from .conv import gen_pygram

    g = gen_pygram.make_py_grammar(grammar.pygram,{})
    g.dump(os.devnull)
    g.load(os.devnull)

# Generated at 2022-06-13 17:51:16.017456
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join(os.path.dirname(__file__), '../Grammar.dat'))

# Generated at 2022-06-13 17:51:24.786138
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import tokenize
    from .parse import Parser

    # Create a Grammar instance for Python 2
    with open("Parser/Grammar2.pickle", "rb") as f:
        py34grammar = pickle.load(f)

    # Create a Parser instance
    parser = Parser(py34grammar)

    # Create a grammar instance for Python 3
    p = Grammar()
    p.load("Parser/Grammar3.5.pickle")

    # Parse "if True: x = 42"
    # This example comes from the file Parser/parser3.4.out
    # which was generated by the command
    # Python3.4 -m test.parsertest -g 3.4
    parser.setup("if True: x = 42", "exec")

# Generated at 2022-06-13 17:51:32.873526
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # arbirtrary dummy file to pass
    f = "test"
    g = Grammar()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        g.dump(f.name)
        g.load(f.name)
        assert g.symbol2number == {}
        assert g.number2symbol == {}
        assert g.states == []
        assert g.labels == [(0, "EMPTY")]
        assert g.keywords == {}
        assert g.tokens == {}
        assert g.symbol2label == {}
        assert g.start == 256

# Generated at 2022-06-13 17:51:33.376235
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    pass

# Generated at 2022-06-13 17:51:34.636180
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("/tmp/grammar.pkl")

# Generated at 2022-06-13 17:51:40.754768
# Unit test for method load of class Grammar
def test_Grammar_load():
    # pylint: disable=protected-access
    g = Grammar()
    assert g.keywords == {}
    assert g.tokens == {}
    assert g.symbol2label == {}
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert g.async_keywords == False
    assert g.labels == [(0, "EMPTY")]
    assert g.states == []
    assert g.start == 256
    assert g.dfas == {}
    # pylint: enable=protected-access

# Generated at 2022-06-13 17:51:50.411982
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.symbol2number = {"EMPTY": 0}
    grammar.number2symbol = {0: ["EMPTY"]}
    grammar.states = [[]]
    grammar.dfas = {}
    grammar.labels = [(0, "EMPTY")]
    grammar.keywords = {}
    grammar.tokens = {}
    grammar.symbol2label = {}
    grammar.start = 256
    grammar.async_keywords = False
    filename = tempfile.mktemp()
    grammar.dump(filename)
    g = Grammar()
    g.load(filename)
    assert(g.symbol2number == grammar.symbol2number)
    assert(g.number2symbol == grammar.number2symbol)
    assert(g.states == grammar.states)

# Generated at 2022-06-13 17:51:57.441461
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    print(g.__dict__)
    assert g.__dict__ == {
        "symbol2number": {},
        "number2symbol": {},
        "states": [],
        "dfas": {},
        "labels": [(0, "EMPTY")],
        "keywords": {},
        "tokens": {},
        "symbol2label": {},
        "start": 256,
        "async_keywords": False,
    }



# Generated at 2022-06-13 17:52:01.226353
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("test/23grammar.pickle")
    g.load("test/23grammar.pickle")

# Generated at 2022-06-13 17:52:06.485082
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    s = "abc"
    assert s in grammar.symbol2number
    assert grammar.number2symbol[1] == "abc"
    assert grammar.dfas[2] == ((), {})
    assert grammar.labels[3] == (4, "keywords")
    assert grammar.keywords["keywords"] == 5
    assert grammar.tokens[6] == 7
    assert grammar.symbol2label["symbol2label"] == 8
    assert grammar.start == 9
    assert not grammar.async_keywords

if __name__ == "__main__":
    import pytest

    pytest.main()

# Generated at 2022-06-13 17:52:15.997948
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver
    from .parse import ParserError

    import unittest.mock

    tmpfile = tempfile.mktemp(prefix="pyparse", suffix=".pkl")
    with unittest.mock.patch("pyparse.parse.ParserError", ParserError):
        try:
            driver.parse_grammar("python3.6.grammar", save=tmpfile, optimize=True)
        except ParserError:
            # Ignore parser errors
            pass
    try:
        os.unlink(tmpfile)
    except FileNotFoundError:
        # Ignore errors due to tempfile errors
        pass

# Generated at 2022-06-13 17:52:18.022373
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.txt")
g = Grammar()
test_Grammar_load()

# Generated at 2022-06-13 17:52:27.709792
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = { "expr": 256, "foo": 257 }
    g.number2symbol = { 256: "expr", 257: "foo" }
    g.states = [ [ [(34, 5)], [] ] ]
    g.dfas = { 256: ([[(34, 5)]], { 5 : 1 }) }
    g.labels = [ (0, "EMPTY"), (34, None) ]
    g.start = 256
    g.keywords = { "y": 34 }
    g.tokens = { 2: 34 }

    def normalize(s: bytes) -> bytes:
        return s.replace(b"\r\n", b"\n").replace(b"utc_offset=0, dst_offset=0", b"")


# Generated at 2022-06-13 17:52:30.991384
# Unit test for method load of class Grammar
def test_Grammar_load():
    '''
    This is a unit test of the Grammar load method.
    It tests that the method can be called and that the
    various attributes are set.
    '''

    class GrammarSubclass(Grammar):
        pass

    # pylint: disable=unused-variable
    g = GrammarSubclass()

# Generated at 2022-06-13 17:52:39.290345
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g1 = Grammar()
    g1.start = 5
    g1.tokens = {1: 2, 3: 4}
    g1.keywords = {'a': 6, 'b': 7}
    g1.labels = [(0, 'EMPTY'), (1, None), (2, 'a'), (3, None), (4, None),
                 (5, None), (6, 'a'), (7, 'b')]
    g1.states = [[(6, 1), (7, 2)], [(0, 1)], [(0, 2)]]

# Generated at 2022-06-13 17:52:42.916974
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver

    grammar = driver.load_grammar("Python.asdl", "Python/graminit.c")
    grammar.dump("tests/test_Grammar.dump")



# Generated at 2022-06-13 17:52:53.422285
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Tests the method Grammar.load."""
    g = Grammar()
    with open("Grammar/Grammar.txt", "r") as f:
        picklestring = "\n".join(f.readlines())
        unpickled = pickle.loads(picklestring.encode("utf-8"))
    g._update(unpickled)
    assert g.number2symbol[4] == '"or_test"'
    assert g.number2symbol[1] == '"dictorsetmaker"'
    assert g.symbol2number["or_test"] == 4
    assert g.symbol2number["dictorsetmaker"] == 1

# Generated at 2022-06-13 17:52:56.141313
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pgen2

    g = Grammar()
    g.load(pgen2.grammar_file)

# Generated at 2022-06-13 17:53:01.512282
# Unit test for method load of class Grammar
def test_Grammar_load():
    try:
        os.remove("grammar.pickle")
    except:
        pass

    g = Grammar()
    g.dump("grammar.pickle")
    g.load("grammar.pickle")
    g.dump("grammar2.pickle")
    os.remove("grammar.pickle")
    os.remove("grammar2.pickle")

# Generated at 2022-06-13 17:53:07.480746
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Unit test for method load of class Grammar."""
    def foo():
        grammar = Grammar()
        grammar.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))

    # mypyc only works with Python 3.8 and above, so this test will only run
    # there.
    if hasattr(importlib, "util"):
        foo()

# Generated at 2022-06-13 17:53:13.567097
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    Grammar().dump('dump')


# Generated at 2022-06-13 17:53:18.379421
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    filename = 'test_pickle'
    # TBD: Need to create a Grammar object and populate it with
    # reasonable data.
    grammar = Grammar()
    grammar.dump(filename)
    os.remove(filename)

# Generated at 2022-06-13 17:53:19.303284
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__)

# Generated at 2022-06-13 17:53:24.312972
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Issue #21788: dump() should not write to the current working
    # directory by default.
    import tempfile
    original_cwd = os.getcwd()
    tmp_dir = tempfile.mkdtemp()
    os.chdir(tmp_dir)
    try:
        g = Grammar()
        g.dump("some_file")
        assert os.path.abspath("some_file") != os.path.join(original_cwd, "some_file")
        os.remove("some_file")
    finally:
        os.chdir(original_cwd)

# Generated at 2022-06-13 17:53:30.680994
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import grammar as grammar_mod
    from .conv import pgen

    # Make sure we can pickle, load and re-pickle the grammar
    g1 = grammar_mod.Grammar()
    pgen.make_grammar(g1)
    fd, fn = tempfile.mkstemp()
    os.close(fd)
    g1.dump(fn)
    g2 = pgen.load_grammar(fn)
    assert g1 == g2
    g3 = grammar_mod.Grammar()
    g3.load(fn)
    assert g1 == g3
    os.unlink(fn)

# Generated at 2022-06-13 17:53:33.283463
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    filename = os.path.join(os.path.dirname(__file__), "Grammar.dat.pickle")
    grammar.load(filename)


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:53:40.098471
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen.conv, pgen.pgen, os, os.path, shutil, tempfile

    # 1. Create a pgen.pgen.Grammar object
    pgen_grammar = pgen.pgen.Grammar()

    # 2. Use it to create an empty pgen.conv.Grammar object
    conv_grammar = pgen.conv.Grammar(pgen_grammar)

    # 3. Create a temporary directory for the dump
    tempfile_tempdir_context = tempfile.TemporaryDirectory()
    tempfile_tempdir = tempfile_tempdir_context.name

    # 4. Save the empty grammar to this directory
    grammar_file = os.path.join(tempfile_tempdir, 'grammar.pickle')
    conv_grammar.dump(grammar_file)



# Generated at 2022-06-13 17:53:49.201227
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io

    s = io.BytesIO()

    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), "Grammar.txt"))
    g.dump(s)
    s.seek(0)

    g2 = Grammar()
    g2.loads(s.read())
    assert g.states == g2.states
    assert g.keywords == g2.keywords
    assert g.tokens == g2.tokens


if __name__ == "__main__":
    import sys

    g = Grammar()
    g.load(sys.argv[1])
    g.report()

# Generated at 2022-06-13 17:54:01.863603
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.states = [[[(1, 2)], [(0, 1)]]]
    g.symbol2number = {'foo': 1}
    g.number2symbol = {1: 'foo'}
    g.dfas = {1: (g.states[0], {})}
    g.labels = [(1, 'foo'), (0, 'EMPTY')]
    g.start = 1

    with tempfile.NamedTemporaryFile(delete=False) as f:
        g.dump(f.name)

    g1 = Grammar()
    g1.load(f.name)
    assert g.states == g1.states
    assert g.symbol2number == g1.symbol2number
    assert g.number2symbol == g1.number2symbol


# Generated at 2022-06-13 17:54:12.657604
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g1 = Grammar()
    g1.symbol2number['a'] = 10
    g1.number2symbol[10] = 'a'
    g1.states = [[[(1, 2)], [(1, 3)]]]
    g1.dfas[20] = (g1.states[0], {1: 1})
    g1.labels = [(0, 'EMPTY'), (1, None)]
    g1.start = 256
    g1.keywords[1] = 1
    g1.tokens[1] = 1
    g1.symbol2label[1] = 1

    g1.dump("test_Grammar_dump.pkl")
    g2 = Grammar()
    g2.load("test_Grammar_dump.pkl")
    assert g1

# Generated at 2022-06-13 17:54:19.329647
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = "./grammar.pkl"
    grammar = Grammar()
    grammar.load(filename)
    grammar.report()

if __name__ == '__main__':
    test_Grammar_load()

# Generated at 2022-06-13 17:54:21.921715
# Unit test for method load of class Grammar
def test_Grammar_load():
    class Dummy:
        def __init__(self): pass
    x = Dummy()
    y = Grammar()
    y.load(x)
    return y


# Generated at 2022-06-13 17:54:32.286094
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    class Dummy:
        def __init__(self):
            self.symbol2number = {'foo': 1}
            self.number2symbol = {1: 'foo'}
            self.states = ['bar']
            self.dfas = {1: 'baz'}
            self.labels = [('a', 'b'), ('c', 'd')]
            self.start = 15

    g._update(Dummy())

    f = tempfile.TemporaryFile(mode='w+b')
    g.dump(f)
    f.seek(0)
    loaded = pickle.load(f)

# Generated at 2022-06-13 17:54:42.677593
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest

    # Create a test grammar
    class TestGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__()
            self.symbol2number = {"ROOT": 1}
            self.number2symbol = {1: "ROOT"}
            self.states = []
            self.dfas = {1: ([[(1, 1)]], set()), 2: ([[(2, 2)]], set())}
            self.labels = [(1, "EMPTY")]
            self.keywords = {}
            self.tokens = {}
            self.symbol2label = {}
            self.start = 256

    # Serialize the test grammar

# Generated at 2022-06-13 17:54:50.539615
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class GrammarTest(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.a = "a"
            self.b = "b"

    my_grammar = GrammarTest()
    with tempfile.TemporaryDirectory() as tmp_dirname:
        filename = os.path.join(tmp_dirname, "grammar_test.pickle")
        my_grammar.dump(filename)
        with open(filename, "rb") as handle:
            data = pickle.load(handle)
        assert data == my_grammar.__dict__

# Generated at 2022-06-13 17:54:52.018086
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("filename.txt")

# Generated at 2022-06-13 17:54:56.274101
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.dat")
    assert(g.number2symbol[256] == 'single_input')
    assert(g.number2symbol[257] == 'file_input')
    assert(g.number2symbol[258] == 'eval_input')

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:54:58.362376
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    filename = "grammar.pickle"
    grammar.dump(filename)
    with open(filename, "rb") as f:
        d = pickle.load(f)
    assert len(d) == 10

# Generated at 2022-06-13 17:55:09.325477
# Unit test for method load of class Grammar
def test_Grammar_load():
  import io
  import unittest.mock

  A = 'A'
  B = 'B'
  C = 'C'

# Generated at 2022-06-13 17:55:15.508068
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    s = """{'symbol2number': {'start': 256, 'foo': 257}, 'number2symbol': {256: 'start', 257: 'foo'}, 'states': [[[(1, 1)]]], 'dfas': {256: ([[(1, 1)]], {}), 257: ([[(1, 1)]], {})}, 'labels': [(0, 'EMPTY'), (1, None)], 'keywords': {}, 'tokens': {}}"""
    g.loads(s.encode())
    assert g.symbol2number['foo'] == 257
    assert g.symbol2number['start'] == 256



# Generated at 2022-06-13 17:55:25.462201
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    filename = "Grammar.dump.pickle"
    # Test for missing file
    try:
        os.remove(filename)
    except OSError:
        pass
    else:
        raise RuntimeError(f"{filename} exists in the current directory")
    # Test for creating proper dump
    G = Grammar()
    G.symbol2number = {'var': 256, 'expr': 257}
    G.number2symbol = {256: 'var', 257: 'expr'}
    G.keywords = {'True': 258, 'False': 259}
    G.tokens = {1: 260, 2: 261}

# Generated at 2022-06-13 17:55:32.885207
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import convert

    # Create a grammar object for 'fake' Python
    python = convert(open("Grammar", "r"), "Grammar.pickle")

    # This test is only possible on Python versions that have the pathlib
    # module available.
    try:
        from pathlib import Path
    except ImportError:
        return

    # Use a temporary directory for all the tests.
    import tempfile

    tempdir = tempfile.TemporaryDirectory()
    path = Path(tempdir.name)
    # Create temporary file.
    fname = path.joinpath("test.Grammar")
    # Call dump() on created object.
    python.dump(fname)

    # Create new object.
    python2 = convert(open("Grammar", "r"), "Grammar.pickle")
    #

# Generated at 2022-06-13 17:55:34.498771
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__[:-1] + "pkl")


# Generated at 2022-06-13 17:55:41.098595
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Unit test for method dump of class Grammar.
    """
    # This test is platform-dependent, because it relies on the
    # exact format of the output produced by pickle.dump().  That
    # output changes from version to version, so this test will
    # fail if run using the wrong version of Python.

    import pickle as pickle_module
    import os
    import sys

    fn = tempfile.mktemp()
    g = Grammar()
    g.symbol2number = {"foo": 2, "bar": 3}
    g.number2symbol = {2: "foo", 3: "bar"}
    g.states = [
        [(1, 1), (1, 2)],
        [(2, 3), (2, 4), 0, 5]
    ]

# Generated at 2022-06-13 17:55:51.314572
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def test_grammar(*rules):
        """
        Create a very simple grammar.

        *rules* is a list of strings where each string is composed of a
        rule name followed by a sequence of rule names as its
        rhs. Rhs rule names are separated by spaces.

        The method returns a Grammar object whose dfas attribute is a
        dictionary mapping the rule names to dfas where the name
        'start' is the start symbol.

        Example:

        >>> p = test_grammar('start', 'A B')
        >>> p.dfas
        {'A': ([[(1, 2)]], {1: 0, 2: 1}), 'B': ([[(3, 4)]], {3: 2, 4: 3}), 'start': ([[(5, 6)]], {5: 4, 6: 5})}

        """


# Generated at 2022-06-13 17:55:59.917502
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    f = "foo.tmp"

# Generated at 2022-06-13 17:56:04.641682
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:56:07.296643
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("data/grammar.pkl")
    assert g.async_keywords == False


# Generated at 2022-06-13 17:56:12.074103
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    path = "Grammar.test_Grammar_load.pkl"
    try:
        grammar.dump(path)
    except Exception as e:
        print(e)
    grammar_loaded = Grammar()
    grammar_loaded.load(path)
    os.remove(path)

# Generated at 2022-06-13 17:56:17.716771
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver

    with driver.parse_grammar(debug=0) as g:
        filename = os.path.join(os.path.dirname(__file__), "Grammar.test")
        g.dump(filename)
        with open(filename, "rb") as f:
            pickle.load(f)
        try:
            os.unlink(filename)
        except OSError:
            pass

# Generated at 2022-06-13 17:56:30.829493
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number['foo'] = 1
    grammar.number2symbol[256] = 'start'
    grammar.states.append([])
    grammar.states.append([[(1, 1)], [(2, 2)]])
    grammar.dfas[256] = (grammar.states[0], {1: 1})
    grammar.labels.append((1, 'foo'))
    grammar.labels.append((2, 'bar'))
    grammar.keywords['foo'] = 1
    grammar.tokens[token.NUMBER] = 1
    grammar.symbol2label['start'] = 256
    grammar.start = 256
    grammar.async_keywords = True

# Generated at 2022-06-13 17:56:40.327083
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 1

    with tempfile.NamedTemporaryFile(delete=False) as f:
        g.dump(f.name)
    with open(f.name, "rb") as f:
        pickle_data = f.read()
    os.unlink(f.name)

    h = Grammar()
    h.loads(pickle_data)

    assert h.start == 1
    assert h.symbol2number == {}
    assert h.number2symbol == {}
    assert h.states == []
    assert h.dfas == {}
    assert h.labels == [(0, "EMPTY")]
    assert h.keywords == {}
    assert h.tokens == {}
    assert h.symbol2label == {}
    assert h.start == 256


# Generated at 2022-06-13 17:56:49.983925
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 10
    g.keywords[":"] = 10
    g.symbol2number["x"] = 10
    g.tokens[10] = 100
    g.labels[100] = (10, ":")
    f = tempfile.NamedTemporaryFile()
    f.close()
    try:
        g.dump(f.name)
        g2 = Grammar()
        g2.load(f.name)
        assert g == g2
    finally:
        os.unlink(f.name)


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:56:59.485777
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.symbol2number = {"type_ignore": 0, "x": 1}
    g.number2symbol = {0: "type_ignore", 1: "x"}
    g.states = [[[(0, 0)], [(0, 1)]], [[(0, 1)]]]
    g.dfas = {0: (1, {"": 1})}
    g.labels = [(0, "EMPTY")]
    g.keywords = {"x": 0}
    g.tokens = {"x": 0}
    g.symbol2label = {"y": 1}
    g.start = 2
    g.async_keywords = True

    with tempfile.NamedTemporaryFile() as f:
        g.dump(f.name)
        g2 = Grammar

# Generated at 2022-06-13 17:57:04.684003
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import glob
    import os
    import pickle
    import sys
    import unittest

    from .conv import convert

    try:
        import importlib
    except ImportError:
        importlib = None

    # Use the grammar file at the top of the directory.
    cur_dir = os.path.split(__file__)[0]
    sys.path.insert(0, cur_dir)
    try:
        mod = importlib.import_module("Grammar")
    finally:
        del sys.path[0]

    g = convert(mod)
    g.dump(os.path.join(cur_dir, "Grammar.pickle"))

    # load the pickle file and test that it matches the original Grammar

# Generated at 2022-06-13 17:57:06.243894
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.txt")


# Generated at 2022-06-13 17:57:19.262438
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import io
    filename="test_Grammar_dump.pkl"

    g = Grammar()

    g.symbol2number = {'check_name': 258, 'NAME': 256, 'end_int': 261, 'int': 260, 'end_check_name': 259}
    g.number2symbol = {256: 'NAME', 258: 'check_name', 260: 'int', 261: 'end_int', 259: 'end_check_name'}

# Generated at 2022-06-13 17:57:25.304811
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    d = tempfile.mkdtemp()
    f = os.path.join(d, 'pickle')
    g.start = 1
    g.dump(f)
    h = Grammar()
    h.load(f)
    assert h.start == 1

# Generated at 2022-06-13 17:57:35.905029
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pickletools
    from .astcompat import cmp
    from .pgen2 import tokenize
    from .python import tokenizer

    # Compare with tokens generated by calling tokenize() directly
    g = Grammar()
    g.load("Grammar.pkl")

    def get_tokens(s: str) -> List[tokenize.TokenInfo]:
        # The 'pgen' implementation of the tokenizer doesn't attach
        # line numbers to tokens, so the test below would always fail
        tokens = tokenize.generate_tokens(iter(s).__next__)
        return [t[:6] for t in tokens]

    assert cmp(tokenizer.generate_tokens(iter("").__next__, g), get_tokens("")) == 0

# Generated at 2022-06-13 17:57:42.047636
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("pgen_test.pickle")
    with open("pgen_test.pickle", "rb") as f:
        d = pickle.load(f)
    assert d["async_keywords"] == False
    assert d["keywords"] == {}
    assert d["labels"] == [(0, "EMPTY")]
    assert d["number2symbol"] == {}
    assert d["start"] == 256
    assert d["states"] == []
    assert d["symbol2number"] == {}
    assert d["symbol2label"] == {}
    assert d["tokens"] == {}
    assert d["dfas"] == {}


# Generated at 2022-06-13 17:57:58.593874
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:58:01.199863
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    # should not raise exception
    g.dump(tempfile.mktemp())

# Generated at 2022-06-13 17:58:16.972165
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Verify that Grammar.dump can create a file on the filesystem"""
    def _check_dump():
        filename = "Grammar_dump.tmp"
        g = Grammar()
        g.dump(filename)
        os.remove(filename)

    #
    # Ensure that Grammar.load() does not trigger any permission errors
    #
    if hasattr(os, "geteuid") and hasattr(os, "getegid"):
        # We have POSIX-like uid/gid calls
        saved_euid = os.geteuid()
        saved_egid = os.getegid()

# Generated at 2022-06-13 17:58:20.894341
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    d = {'a': 1, 'b': 2}
    with tempfile.TemporaryFile() as f:
        pickle.dump(d, f)
        f.seek(0)
        g.loads(f.read())
    assert g.a == 1
    assert g.b == 2

# Generated at 2022-06-13 17:58:30.945560
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    if not hasattr(os, "PathLike"):
        # Skip if os.PathLike.__fspath__ not available (Python < 3.6)
        return
    test_file = os.fspath(tempfile.NamedTemporaryFile(delete=False))
    g = Grammar()
    g.dump(test_file)
    with open(test_file, "rb") as f:
        d = pickle.load(f)
    assert d["states"] == g.states
    assert d["keywords"] == g.keywords
    assert d["tokens"] == g.tokens
    assert d["labels"] == g.labels
    assert d["symbol2label"] == g.symbol2label
    assert d["symbol2number"] == g.symbol2number

# Generated at 2022-06-13 17:58:40.688942
# Unit test for method load of class Grammar
def test_Grammar_load():
    try:
        import py_compile
    except ImportError:
        raise unittest.SkipTest("need py_compile")

    # Create a pgen file and compile it
    pgen = os.path.join(os.path.dirname(__file__), "Python.pgen")
    pgenc = os.path.join(os.path.dirname(__file__), "Python.pgenc")
    if not os.path.isfile(pgenc) or os.stat(pgen).st_mtime > os.stat(pgenc).st_mtime:
        py_compile.compile(pgen, cfile=pgenc)

    # Load the file and check that the tables are loaded correctly
    g = Grammar()
    g.load(pgenc)
    assert "atom"

# Generated at 2022-06-13 17:58:48.107404
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from typing import Any

    # Initialize the grammar tables
    gram = Grammar()
    d = {}
    d["start"] = 0x0A0B
    d["async_keywords"] = False
    d["number2symbol"] = {257: 'x', 258: 'term', 259: 'factor'}
    d["labels"] = [(0, None), (1, None), (257, None), (258, None), (259, None), (260, None), (261, None), (262, None), (263, None), (264, None)]
    d["tokens"] = {257: 1, 258: 2, 259: 4}

# Generated at 2022-06-13 17:58:57.687168
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Unit test for method load of class Grammar
    """
    tokens = Grammar()
    tokens.load('Grammar.tokens')

# Generated at 2022-06-13 17:59:04.963564
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    import pickle
    from importlib.resources import path
    from . import conv, pgen
    from . import _ast

    class GrammarTest(unittest.TestCase):
        def test_dump(self) -> None:
            path_pickle = "ast_grammar.pkl"
            try:
                with path(_ast, path_pickle).open(mode="rb") as pickle_file:
                    test_pickle = pickle_file.read()
            except FileNotFoundError:
                raise unittest.SkipTest(
                    f"No prebuilt pickle file found: {path_pickle}"
                )
            grammar = Grammar()
            conv.parse_grammar(grammar, vars(_ast))
            grammar.dump(path_pickle)

# Generated at 2022-06-13 17:59:09.296252
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump('/home/shoulong/tmp/grammar.pkl')
    g.load('/home/shoulong/tmp/grammar.pkl')
    g.report()
    g.loads(g.dumps())


# Generated at 2022-06-13 17:59:25.771852
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    d = g.__dict__
    td = tempfile.gettempdir()
    fname = os.path.join(td, "grammar-data.py")
    if os.path.exists(fname):
        os.remove(fname)
    g.dump(fname)
    # test that the file does not get created if an exception gets
    # raised in dump
    try:
        g.dump("/no/such/file/name")
    except OSError:
        assert not os.path.exists(fname)
    else:
        assert 0, "OSError should be raised"
    # test that the file gets created if no exception gets raised
    assert os.path.exists(fname)
    # test that dump is able to restore the data
    g2

# Generated at 2022-06-13 17:59:36.751445
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Unit test for Grammar.dump()
    """
    gram = Grammar()
    gram.symbol2number = {'FRED': 258, 'BARNEY': 259}
    gram.symbol2number['X'] = 260
    gram.number2symbol = {258: 'FRED', 259: 'BARNEY'}
    gram.number2symbol[260] = 'X'
    gram.states = [[(0,1)],[(0,2)]]
    gram.dfas = {258: ([(0,1)],[0])}
    gram.dfas[259] = ([(0,2)],[0])
    gram.labels = [(0, 'EMPTY'), (256, 'FRED'), (257, 'BARNEY'), (258, 'X')]