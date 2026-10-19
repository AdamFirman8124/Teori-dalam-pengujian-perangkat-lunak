

# Generated at 2022-06-13 17:49:49.215316
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Grammar.load(filename) should load the grammar tables from a pickle
    file.  Grammar.loads(string) should load from an 8-bit string.
    """
    import pickletools

    # Build a sample grammar.
    grammar = Grammar()
    grammar.symbol2number = {"foo": 256, "bar": 257, "baz": 258}
    grammar.number2symbol = {256: "foo", 257: "bar", 258: "baz"}

# Generated at 2022-06-13 17:49:54.672902
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("dump_test.pkl")
    os.remove("dump_test.pkl")


if __name__ == "__main__":
    g = Grammar()
    g.dump("dump_test.pkl")
    os.remove("dump_test.pkl")
    test_Grammar_dump()

# Generated at 2022-06-13 17:49:58.918961
# Unit test for method load of class Grammar
def test_Grammar_load():
    import sys, pickle
    g = Grammar()
    with open(sys.argv[1], "rb") as f:
        d = pickle.load(f)
    g.load(d)

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:50:09.364719
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import tempfile
    import unittest

    # move to a temporary directory so we don't pollute the working
    # directory with files for the test
    old_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)

        # check the dump of a small grammar
        with open('grammar.pkl', 'wb') as f:
            g = Grammar()
            g.symbol2number = {'foo': 1, 'bar': 2, 'baz': 3}
            g.number2symbol = {1: 'foo', 2: 'bar', 3: 'baz'}
            g.start = 1
            g.dump(f)

        # check that the grammar was dumped

# Generated at 2022-06-13 17:50:19.739364
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # test_Grammar_dump_method.py
    # This unit test checks the Grammar method dump
    import unittest

    import os
    import pickle
    import tempfile

    from parser_test_helper import ParserTestMixin

    class TestGrammarDumpMethod(ParserTestMixin, unittest.TestCase):

        def setUp(self):
            self.thisdir = os.path.abspath(os.path.dirname(__file__))
            self.t_path = os.path.join(self.thisdir, "temp")
            self.pickle_file = os.path.join(self.t_path, 'py_grammar.py.pkl')
            self.set_grammar(self.pickle_file)
            self.maxDiff = None


# Generated at 2022-06-13 17:50:25.736363
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io
    from . import pgen2

    with io.BytesIO() as f:
        g = pgen2.load_grammar()
        g.dump(f)
        f.seek(0)
        g2 = Grammar()
        g2.loads(f.read())
        assert g2.symbol2number == g.symbol2number
        assert g2.number2symbol == g.number2symbol
        assert g2.states == g.states
        assert g2.dfas == g.dfas
        assert g2.labels == g.labels
        assert g2.keywords == g.keywords
        assert g2.tokens == g.tokens
        assert g2.symbol2label == g.symbol2label
        assert g2.start == g.start
       

# Generated at 2022-06-13 17:50:29.825701
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = "test/test_grammar.pkl"
    g = Grammar()
    g.load(filename)
    assert g.start == 256
    assert g.number2symbol[256] == "file_input"
    assert g.number2symbol[258] == "stmt"



# Generated at 2022-06-13 17:50:37.750635
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Create a Grammar instance
    inst = Grammar()

    # Save the instance to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as f:
        inst.dump(f.name)

    # Load the instance from the temporary file
    inst2 = Grammar()
    inst2.load(f.name)

    # Remove the temporary file
    os.remove(f.name)

    # Test that the loaded instance is the same as the original
    if inst2.symbol2number != inst.symbol2number:
        raise AssertionError()
    if inst2.number2symbol != inst.number2symbol:
        raise AssertionError()
    if inst2.states != inst.states:
        raise AssertionError()

# Generated at 2022-06-13 17:50:39.665738
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), 'Grammar.pkl'))

# Generated at 2022-06-13 17:50:40.962950
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()

    # Not implemented yet
    pass

# Generated at 2022-06-13 17:50:54.390435
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    class X(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.x = "x"
            self.y = "y"
    g = X()
    g.dump("pgen_dump_test")
    d = pickle.load(open("pgen_dump_test", "rb"))
    os.remove("pgen_dump_test")
    assert d["x"] == "x"
    assert d["y"] == "y"
    assert d["symbol2number"] == {}
    assert d["number2symbol"] == {}
    assert d["keywords"] == {}
    assert d["tokens"] == {}
    assert d["symbol2label"] == {}
    assert d["states"] == []

# Generated at 2022-06-13 17:51:03.077462
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.dump("Grammar.dump")
    with open("Grammar.dump", "rb") as f:
        d = pickle.load(f)
    # The pickled values are different from the actual values
    # because when the Grammar was pickled, it was done before
    # the asdl package was compiled, so the values changed
    assert d["symbol2number"] == {"BinOp": 257, "UnaryOp": 258}
    assert d["number2symbol"] == {257: "BinOp", 258: "UnaryOp"}
    assert d["states"] == [[(1, 2), (257, 3), (258, 4)]]

# Generated at 2022-06-13 17:51:14.650557
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # N.B.: We test a few attributes but not all, since they are
    # pickled, and it's hard to interpret the pickled data.
    g = Grammar()
    g.symbol2number = {'foo': 1}
    g.number2symbol = {1: 'foo'}
    g.dfas = {1: ([[], [], [], [], [], [], []], {'foo': 2})}
    g.keywords = {'foo': 1}
    g.tokens = {1: 1}
    g.symbol2label = {'foo': 1}
    g.labels = [(1, 'foo')]

# Generated at 2022-06-13 17:51:20.811708
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join(
        os.path.dirname(__file__),
        "..", "python-grammar.pickle"
    ))
    assert len(grammar.states) == 2076
    assert len(grammar.symbol2number) == 1037
    assert len(grammar.number2symbol) == 1037
    assert len(grammar.dfas) == 1037

# Generated at 2022-06-13 17:51:32.617548
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import convert
    from .pgen import driver
    path = driver.parse_grammar(convert)
    g = Grammar()
    g.load(path)
    assert repr(g) # repr()
    assert isinstance(g.symbol2number, dict)
    assert isinstance(g.number2symbol, dict)
    assert isinstance(g.states, list)
    assert isinstance(g.dfas, dict)
    assert isinstance(g.labels, list)
    assert isinstance(g.keywords, dict)
    assert isinstance(g.tokens, dict)
    assert isinstance(g.symbol2label, dict)
    assert isinstance(g.start, int)
    assert isinstance(g.async_keywords, bool)
    assert g.async_

# Generated at 2022-06-13 17:51:33.121260
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    pass

# Generated at 2022-06-13 17:51:39.313563
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import sys
    import tokenize
    from .parse import Parser

    tests = [
        """
x = -1
""",
        """
y = ~1
""",
        """
z = not 1
""",
        """
x = -1
y = ~1
z = not 1
""",
    ]

    def run(grammar, s):
        for opname in ["uminus", "invert", "not"]:
            g = grammar.copy()
            g.symbol2number["expr"] = 256
            g.number2symbol[256] = "expr"
            g.symbol2number[opname] = 257
            g.number2symbol[257] = opname
            lhs = grammar.symbol2label["NAME"]
            rhs = grammar.symbol2label

# Generated at 2022-06-13 17:51:49.286530
# Unit test for method load of class Grammar
def test_Grammar_load():
    import textwrap
    input_py = textwrap.dedent("""
    if True:
      pass
    """)
    from . import tokenize
    from . import pygram
    from . import pytree
    from .pgen2.parse import ParseError
    from .py3_parse import PythonParser
    pgen = pygram.python_grammar_no_print_statement
    pgen.check_consistency()
    tokens = tokenize.generate_tokens(input_py.__iter__().__next__)
    parser = PythonParser(pgen)
    try:
        node = parser.parse_tokens(tokens)
    except ParseError as pe:
        if pe.__cause__ is not None:
            raise pe.__cause__
        raise

    pytree.assert_parse

# Generated at 2022-06-13 17:51:52.513626
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump(b'pickletest.pkl')
    os.remove(b'pickletest.pkl')


# Generated at 2022-06-13 17:52:03.581805
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    x = Grammar()
    x.start = 0
    x.dfas = {1: ([[(0, 1)]], {0: 1, 1: 2})}
    x.number2symbol = {1: 'test'}
    x.labels = [(1, None), (1, 'test')]
    x.symbol2label = {'test': 1}
    x.symbol2number = {'test': 1}
    x.states = [[[(0, 1)]]]
    x.tokens = {1: 1}
    x.keywords = {'test': 1}
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io

# Generated at 2022-06-13 17:52:08.953320
# Unit test for method load of class Grammar
def test_Grammar_load():
    # pylint: disable=import-outside-toplevel,unused-variable
    from . import grammar

    s3 = Grammar()
    s3.load(grammar.__file__)
    s3.report()

# Generated at 2022-06-13 17:52:17.255571
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class TestGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.symbol2number = {'a': 10, 'b': 20}
            self.number2symbol = {10: 'a', 20: 'b'}
            self.states = [
                [],
                [(0, 7), (3, 6), (4, 5), (10, 0), (20, 1)],
                [],
                [(0, 7), (3, 8)],
                [(0, 3)],
                [(0, 3)],
                [(0, 6), (10, 1)],
                [(0, 7), (3, 9)],
                [(0, 7), (3, 10)],
                [(0, 8)],
                [(0, 10)],
            ]

# Generated at 2022-06-13 17:52:27.116231
# Unit test for method load of class Grammar
def test_Grammar_load():
    def assert_load(pkl: bytes, expected: Dict[str, Any]) -> None:
        grammar = Grammar()
        grammar.loads(pkl)
        for k, v in expected.items():
            assert getattr(grammar, k) == v


# Generated at 2022-06-13 17:52:28.809314
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump(b"foo")

# Generated at 2022-06-13 17:52:37.675217
# Unit test for method load of class Grammar
def test_Grammar_load():
    def check_state(g: Grammar, s: DFA) -> None:
        for i, arcs in enumerate(s):
            for _, succ in arcs:
                assert 0 <= succ < len(g.states), "Invalid state %d" % succ

    def check_dfa(g: Grammar, dfa: DFA) -> None:
        for state in dfa:
            for i, _ in state:
                assert 0 <= i < len(g.labels), "Invalid arc label %d" % i

    def check_dfas(g: Grammar, dfas: Dict[int, DFAS]) -> None:
        for _, (dfa, _) in dfas.items():
            check_dfa(g, dfa)

    g = Grammar()
    g.load("Grammar.pickle")

# Generated at 2022-06-13 17:52:49.573954
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"name" : 256}
    g.number2symbol = {256 : "name"}
    g.states = [[["state 1"]]]
    g.dfas = {256 : ("dfa", 256)}
    g.labels = [("labels", "label 1")]
    g.keywords = {"keyword 1" : "label 1"}
    g.tokens = {256 : "label 1"}
    g.symbol2label = {"symbol 2" : 256}
    g.start = 256
    # End instance attributes

    # Python 3.7+ parses async as a keyword, not an identifier
    g.async_keywords = False

    temp = tempfile.mktemp(".py")
    g.dump(temp)
    g2 = Gram

# Generated at 2022-06-13 17:52:54.239025
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    class A(object):
        def __init__(self, x: Dict[str, str]) -> None:
            self.__dict__ = x
    g.test = A({'y': 'z'})
    g.dump(__file__)

# Generated at 2022-06-13 17:52:58.840883
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pgen.pgen
    gram = pgen.pgen.Grammar()
    gram.load('Grammar.pickle')
    gram.report()

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:53:07.694011
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test dump and loads
    import shutil
    import sys
    from unittest import mock

    g = Grammar()
    if sys.platform.startswith("win"):
        out_file = r"C:\TEMP\\test.pkl"
    else:
        out_file = "/tmp/test.pkl"

    try:
        g.dump(out_file)
        with mock.patch("builtins.open", open) as m:
            g.load(out_file)
            m.assert_called_with(out_file, "rb")
    finally:
        if os.path.exists(out_file):
            os.remove(out_file)

# Generated at 2022-06-13 17:53:20.221055
# Unit test for method load of class Grammar
def test_Grammar_load():
    from pgen2.pgen import Grammar as PgenGrammar
    import sys

    test_grammar = Grammar()
    pgen = PgenGrammar()

    test_grammar.load(sys.executable)

    assert sorted(pgen.labels) == sorted(test_grammar.labels)
    assert sorted(pgen.tokens) == sorted(test_grammar.tokens)
    assert sorted(pgen.keywords) == sorted(test_grammar.keywords)
    assert pgen.start == test_grammar.start
    assert sorted(pgen.symbol2number) == sorted(test_grammar.symbol2number)
    assert sorted(pgen.number2symbol) == sorted(test_grammar.number2symbol)
    assert pgen.states == test

# Generated at 2022-06-13 17:53:22.986659
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert 1==1

# Generated at 2022-06-13 17:53:24.506950
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Issue 11671
    g = Grammar()
    g.dump(b"/tmp/shelve-test")

# Generated at 2022-06-13 17:53:32.283699
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    import shutil
    import io
    import tempfile
    from .pgen2 import driver

    class TestGrammarMethods(unittest.TestCase):

        def setUp(self):
            self.temp_dir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.temp_dir)

        def test_dump(self):
            gramfname = os.path.join(self.temp_dir, "Grammar.txt")
            gfname = os.path.join(self.temp_dir, "Grammar_py3.6.pkl")
            g = Grammar()
            driver.load_grammar(gramfname, g)
            g.dump(gfname)

# Generated at 2022-06-13 17:53:36.052089
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Test the method load of Grammar.
    """
    t = Grammar()
    t_str = b'\x80\x04\x95@\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x12symbol2number\x94\x8c\x0e' \
            b'number2symbol\x94\x8c\x06states\x94\x93\x94)\x94\x8c\x04dfas\x94}\x94(\x8c\x06' \
            b'labels\x94]\x94(K\x00\x94\x86\x94(\x8c\x07keywords\x94}\x94(\x8c\x06tokens\x94'

# Generated at 2022-06-13 17:53:46.331200
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar_name = "GrammarGrammar"
    grammar = Grammar()
    grammar.symbol2number = {grammar_name: 256}
    grammar.number2symbol = {256: grammar_name}
    grammar.start = 256
    grammar.states = [[]]
    grammar.labels = [(0, None)]
    grammar.dfas = {256: (grammar.states[0], grammar.labels[0][0])}
    grammar.keywords = {}
    grammar.tokens = {}

    grammar.dump("GrammarGrammar.pickle")
    grammar2 = Grammar()
    grammar2.load("GrammarGrammar.pickle")
    assert grammar2.symbol2number == {grammar_name: 256}

# Generated at 2022-06-13 17:53:50.771834
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import pgen

    parse_grammar = Grammar()
    pgen.make_parse_table(parse_grammar)
    parse_grammar.dump(os.path.join(os.path.dirname(__file__), "Grammar.dat"))


# Generated at 2022-06-13 17:53:53.090515
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest.mock

    grammar = Grammar()
    grammar.load(unittest.mock.sentinel.filename)

# Generated at 2022-06-13 17:53:54.633387
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load()

# Generated at 2022-06-13 17:54:03.113963
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    filename = os.path.join(os.path.dirname(__file__), "Grammar.pkl")
    g.load(filename)
    assert g.number2symbol[257] == "single_input"
    assert g.symbol2number["single_input"] == 257
    assert g.symbol2label["single_input"] == 3
    assert g.dfas[257] == (
        [[(8, 258), (9, 260), (0, 259)], [(4, 261), (0, 262)]],
        {8: 1, 9: 1, 4: 1},
    )
    assert g.states[0] == [[(1, 1), (3, 2)]]

# Generated at 2022-06-13 17:54:05.908538
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(__file__)
    assert grammar.labels == [(0, 'EMPTY')]

# Generated at 2022-06-13 17:54:09.394418
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load("Grammar.pickle")


# Generated at 2022-06-13 17:54:15.352276
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Unit test for method load of class Grammar"""
    from . import pgen2
    from . import pygram
    from . import python_grammar_no_print_statement

    file_name = "Python37.pgen"
    pgen2.generate_grammar_tables(python_grammar_no_print_statement, file_name)

    g = Grammar()
    g.load(file_name)

    assert len(g.dfas) == len(pygram.python_grammar.dfas)
    assert len(g.states) == len(pygram.python_grammar.states)

# Generated at 2022-06-13 17:54:23.166334
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number['foo'] = 1
    g.number2symbol[1] = 'foo'
    g.states = [[('start', 1), ('end', 2)]]
    g.dfas[1] = ([(1, 1)], {1: 1})
    g.labels = [(1, None), (2, None)]
    g.keywords = {}
    g.tokens = {1: 1}
    g.symbol2label = {}
    g.start = 256
    g.dump('/tmp/testdump')
    g_copy = Grammar()
    g_copy.load('/tmp/testdump')
    assert g_copy.symbol2number == {'foo': 1}

# Generated at 2022-06-13 17:54:33.233683
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Test method load of class Grammar.

    This test verifies that a grammar created by Grammar() has the
    same attributes after loading the resulting pickle.  This is
    necessary because some of the grammar's attributes are dictionaries
    or lists and dictionaries, and by default pickle gives us another
    reference to the same object instead of a true copy.

    """
    g = Grammar()
    with tempfile.NamedTemporaryFile() as f:
        g.dump(f.name)
        g2 = Grammar()
        g2.load(f.name)
    assert g.__dict__ == g2.__dict__, "Grammar().dump() and Grammar().load() don't match"
    # The line above may fail even if dump() and load() don't change
    # the stored object, because load() modifies

# Generated at 2022-06-13 17:54:38.210119
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle

    class G(Grammar):
        def __init__(self):
            super().__init__()

    g = G()
    g.start = 5
    d = g.dump(pickle.dumps(g.__dict__))



# Generated at 2022-06-13 17:54:44.540136
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import convert

    g = Grammar()
    convert(g, [0], [0], [[0, token.INDENT, 0, token.DEDENT, 0]])
    assert len(g.states) == 1
    assert not hasattr(g, "__dict__")  # use fake class without a __dict__

    _, filename = tempfile.mkstemp()
    try:
        g.dump(filename)
        g2 = Grammar()
        g2.load(filename)
        assert len(g2.states) == 1
    finally:
        os.unlink(filename)

# Generated at 2022-06-13 17:54:47.809154
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    foo = "test.pkl"
    g.dump(foo)
    assert os.path.exists(foo)
    os.remove(foo)


# Generated at 2022-06-13 17:54:53.157274
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Unit test for method `load` of class `Grammar`
    """
    from .conv import Conv
    from .pgen import Driver

    conv = Conv(Driver().grammar())
    conv.convert()
    g = Grammar()
    g.loads(conv.pkl)
    g.loads(conv.pkl)


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:54:59.376741
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    This test ensures that Grammar.dump() does not modify the Grammar
    object by comparing the dumped grammar with the one that was dumped.

    This is an issue with mypyc, since it accidentally keeps
    references to the original object when dumping it, which may
    modify the object.

    This test is skipped if the Grammar class is the original one,
    since it's the one that contains the mypyc bug.
    """

    import sys
    from types import ModuleType

    if isinstance(sys.modules["lib2to3.pgen2.pgen2"], ModuleType):
        return

    g = Grammar()
    g.symbol2number = {"A": 3}
    g.number2symbol = {"4": "B"}

# Generated at 2022-06-13 17:55:08.606355
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = "test.pkl"
    data1 = {'states': ['data1']}
    data2 = {'states': ['data2']}
    def test_getstate(self):
        return data1
    def test_setstate(self, state):
        self.__class__._update(self, state)
    Grammar.__getstate__ = test_getstate
    Grammar.__setstate__ = test_setstate

    g = Grammar()
    g.dump(filename)
    g.loads(pickle.dumps(data2))
    g.load(filename)
    assert g.states == data1['states']
    os.remove(filename)

# Generated at 2022-06-13 17:55:17.858046
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

    # writing to a zero-size file will blow up
    filename = "0.pkl"
    with open(filename, "wb") as f:
        f.truncate(0)
    with open(filename, "rb") as f:
        d = pickle.load(f)
    for k, v in d.items():
        setattr(g, k, v)
    g.dump("1.pkl")
    del g
    with open("1.pkl", "rb") as f:
        d = pickle.load(f)
    os.unlink("1.pkl")
    os.unlink(filename)



# Generated at 2022-06-13 17:55:22.117900
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Test that the load() method will work on the grammar from the grammar
    # pickle file.  The file is very large, so we're just testing that it
    # can be imported, rather than that the data is correct.
    from . import grammar
    g = Grammar()
    g.load(grammar.__file__)

# Generated at 2022-06-13 17:55:30.924395
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.abspath(__file__).replace(".py", ".pickle"))

# Generated at 2022-06-13 17:55:35.679235
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pgen2
    from . import convert

    # Just load the tables once, since it's so slow.
    from . import pkgdir

    fname = os.path.join(pkgdir, "Grammar.txt")
    g = Grammar()
    g.load(fname)
    return


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:55:37.214751
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert Grammar().load("fake_file") is None

# Generated at 2022-06-13 17:55:44.114093
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    f = tempfile.NamedTemporaryFile()
    filename = f.name
    f.close()
    g.dump(filename)
    g2 = Grammar()
    g2.load(filename)
    os.unlink(filename)
    assert g.number2symbol == g2.number2symbol
    assert g.symbol2number == g2.symbol2number
    assert g.states == g2.states
    assert g.dfas == g2.dfas
    assert g.labels == g2.labels
    assert g.start == g2.start

# Generated at 2022-06-13 17:55:47.164912
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    stats = Grammar()
    try:
        stats.dump('/dev/null')
    except Exception as e:
        assert False, f'unexpected exception {e}'

# Generated at 2022-06-13 17:55:56.808067
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import grammar
    from . import conv
    from . import parse

    grammar_file = f"{os.path.dirname(__file__)}/Grammar.txt"
    try:
        with open(grammar_file, "rb") as fp:
            g = grammar.Grammar()
            g.loads(fp.read())
            g.async_keywords = False
        with open(f"{os.path.dirname(__file__)}/Grammar.dat", "rb") as fp:
            g1 = pickle.load(fp)
        assert g == g1
        assert g.start == g1.start
    except (IOError, pickle.UnpicklingError) as e:
        raise Exception("Grammar tests require Grammar.dat. Run pgen.")
    conv

# Generated at 2022-06-13 17:55:59.916045
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from pgen2.pgen import driver
    from pathlib import Path

    parser = driver.Driver()
    parser.load_grammar() # Compile grammar using pgen
    filename = str(Path(tempfile.gettempdir()) / "grammar.pickle")
    parser.grammar.dump(filename)
    parser2 = driver.Driver()
    parser2.load_grammar(filename)
    # Compare dump files of 2 parsers
    assert parser == parser2
    os.remove(filename)

# Generated at 2022-06-13 17:56:11.776530
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    import pgen2.parse

    class TestGrammarDump(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_Grammar_load(self):
            with self.assertRaises(AttributeError):
                grammar = pgen2.parse.Grammar()
                grammar.load("pgen2/pgen2_grammar.py")

        def test_Grammar_loads(self):
            grammar = pgen2.parse.Grammar()
            with self.assertRaises(AttributeError):
                grammar.loads(b'{x: "test"}')


if __name__ == "__main__":
    unittest.main()

# Generated at 2022-06-13 17:56:23.901799
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number.update({'None': 256, 'False': 257, 'True': 258})
    g.number2symbol.update({256: 'None', 257: 'False', 258: 'True'})
    g.states.append([(0, 258), (0, 257), (0, 256)])
    g.dfas.update({256: ([[(0, 256), (0, 257), (0, 258)]], {0: 0})})
    g.labels.append((0, None))
    g.labels.append((0, None))
    g.labels.append((0, None))
    g.labels.append((0, None))
    g.labels.append((0, None))
    g.labels.append((0, None))
    g

# Generated at 2022-06-13 17:56:34.803282
# Unit test for method load of class Grammar
def test_Grammar_load():
    import copy
    import sys
    import pytest
    from . import token

    # Okay, so why do we want to parse our own grammar?  It's because
    # Python's own grammar is modified at runtime to remove rules that
    # don't apply, so the data structures are somewhat misleading.
    # TODO: Remove this test when we're sure the unit tests work.
    filename = "Grammar.test_Grammar_load.pkl"

    import untokenize

    def generate_grammar_pickle(filename: Path) -> None:
        from . import symbol_re

        using_grammar = Grammar()
        using_grammar.async_keywords = sys.version_info[:2] >= (3, 7)
        using_grammar.start = "file_input"
        using_grammar.symbol

# Generated at 2022-06-13 17:56:39.781196
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number["a"] = 0
    g.number2symbol[1] = "b"
    g.states = [[[(0, 1), (1, 0)], [(0, 0)]]]
    g.dfas = {0: (0, {"c": 1})}
    g.labels = [(0, "")]
    g.keywords = {"d": 1}
    g.tokens = {2: 3}
    g.symbol2label = {"e": 4}
    g.start = 5

    f = tempfile.TemporaryFile()
    g.dump(f)
    f.seek(0)
    h = Grammar()
    h.load(f)

    assert g.symbol2number == h.symbol2number

# Generated at 2022-06-13 17:56:44.994652
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    g.dump(f.name)
    g.load(f.name)
    os.remove(f.name)

# Generated at 2022-06-13 17:56:55.139121
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.number2symbol = {1: 'one', 2: 'two'}
    g.symbol2number = {'one': 1, 'two': 2}
    g.states = [[(1, 2)], [(3, 4)]]
    g.dfas = {1: ([(5, 6), (7, 8)], {}), 2: ([(9, 10), (11, 12)], {})}
    g.labels = [(1, 'one'), (2, None)]
    g.keywords = {'one': 1, 'two': 2}
    g.tokens = {1: 3, 2: 4}
    g.symbol2label = {'one': 5, 'two': 6}
    g.start = 256

    filename = tempfile.mktemp()
    g

# Generated at 2022-06-13 17:57:02.828311
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2.pgen as pgen
    g = Grammar()
    g.symbol2number["if"] = 3
    g.symbol2number["foo"] = 5
    g.number2symbol[3] = "if"
    g.number2symbol[5] = "foo"
    g.states.append([(1, 2), (2, 3)])
    g.states.append([(0, 2)])
    g.states.append([(0, 2)])
    g.dfas[3] = (g.states[0], {4: 1})
    g.dfas[5] = (g.states[1], {3: 1, 4: 1})
    g.labels.append((4, None))
    g.labels.append((7, None))

# Generated at 2022-06-13 17:57:16.924058
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import conv
    from . import pygram

    g = conv.Converter("S", "S")
    g.grammar.dump("python.pgen.pkl")
    g.dump("python.pgen")
    g = pygram.PythonGrammar("2.7")
    g.dump("python27.pgen")
    g = pygram.PythonGrammar("3.3")
    g.dump("python33.pgen")
    g = pygram.PythonGrammar("3.4")
    g.dump("python34.pgen")
    g = pygram.PythonGrammar("3.5")
    g.dump("python35.pgen")
    g = pygram.PythonGrammar("3.6")
    g.dump("python36.pgen")

# Generated at 2022-06-13 17:57:25.264325
# Unit test for method dump of class Grammar

# Generated at 2022-06-13 17:57:39.486517
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    import sys
    import tempfile
    import unittest
    import warnings
    import six

    # The tables were originally pickled with protocol 0, while
    # pickle.dump() uses the highest protocol by default.  Silence the
    # warning produced by the unpickling of this data.
    warnings.filterwarnings("ignore", ".*invalid value encountered in.*", RuntimeWarning)

    # Generate a temporary filename for pickling.
    with tempfile.TemporaryFile() as f:
        pkl_file = f.name

    # Create a Grammar instance, dump it to a pickle file and load a new
    # instance which should be equivalent
    g1 = Grammar()
    g1.dump(pkl_file)
    g2 = Grammar()

# Generated at 2022-06-13 17:57:52.831363
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    This unit test ensures that 'load' method of class Grammar works as expected

    We first create the grammar instance, then we dump the grammar, load and compare
    we expect the result to be the same, if not an error is raised.
    """
    g = Grammar()
    g.symbol2number = {'a': 1, 'b': 0}
    g.number2symbol = {0: 'b', 1: 'a'}
    g.dfas = {1: ([1, 1], {1: 1}), 0: ([0, 1], {0: 1})}
    g.labels = [(1, 'aa'), (0, 'bb')]
    g.states = [[(1, 0), (1, 1)], [(1, 0)]]
    g.start = 1
    g.tokens

# Generated at 2022-06-13 17:57:55.776516
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert Grammar().load(None) is None

# Generated at 2022-06-13 17:57:58.239778
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    mg = Grammar()
    mg.tokens = {1: 1, 2: 2}
    mg.start = 2

    mg.dump("temp_test.pkl")

    mgg = Grammar()
    mgg.load("temp_test.pkl")

    assert mg.tokens == mgg.tokens
    assert mg.start == mgg.start



# Generated at 2022-06-13 17:58:08.247933
# Unit test for method load of class Grammar
def test_Grammar_load():
    pkl_file = './Grammar.pkl' # Pickle file
    with open(pkl_file, 'rb') as f:
        pkl_contents = f.read()

    d = pickle.loads(pkl_contents)

    def assert_dicts_equal(d1, d2):
        # First, check if d1 and d2 are dictionaries
        assert isinstance(d1, dict) and isinstance(d2, dict)
        # Then check if they have the same keys
        assert set(d1.keys()) == set(d2.keys())
        # Then check if the values of each key is the same
        for key in d1.keys():
            assert d1[key] == d2[key]


# Generated at 2022-06-13 17:58:08.729165
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    pass

# Generated at 2022-06-13 17:58:14.732038
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import py
    import pickle

    filename = str(py.path.local(__file__))[:-1] + '-Grammar.pickle'
    g = Grammar()
    g.dump(filename)
    assert os.path.exists(filename)
    g = Grammar()
    g.load(filename)
    assert True
    with open(filename, 'rb') as f:
        g = Grammar()
        g.loads(f.read())
        assert True

# Generated at 2022-06-13 17:58:21.743296
# Unit test for method load of class Grammar
def test_Grammar_load():
    fd, filename = tempfile.mkstemp(prefix="pytree_parser")
    try:
        os.close(fd)
        g = Grammar()
        g.number2symbol = {"number2symbol_value"}
        g.start = "start_value"
        g.dump(filename)
        g = Grammar()
        g.number2symbol = set()
        g.start = None
        g.load(filename)
        assert g.number2symbol == {"number2symbol_value"}
        assert g.start == "start_value"
    finally:
        os.remove(filename)


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:58:29.694851
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2.parse
    filename = "test_Grammar_dump.pickle"
    g = Grammar()
    pgen2.parse.generate_grammar(g, filename)
    g.dump(filename)
    h = Grammar()
    h.loads(open(filename, "rb").read())
    if h.symbol2number == g.symbol2number:
        print("method dump successful")
    else:
        print("method dump unsuccessful")


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:58:38.499514
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Test Grammar.load for a pickle file that has been created by
    Grammar.dump().
    """
    gr = Grammar()
    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as f:
        gr.dump(f.name)
    with open(f.name, "rb") as f:
        gr.load(f.name)


if __name__ == "__main__":
    import unittest

    suite = unittest.TestLoader().loadTestsFromTestCase(unittest.TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 17:58:46.438083
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'*': 1024}
    g.number2symbol = {1024: '*'}
    g.start = 1024
    g.states = [[[(0, 0)]]]
    g.dfas = {1024: ([[(0, 0)]], {0: 0})}
    g.labels = [(1024, None)]

    g.dump('/tmp/test-Grammar-dump.pickle')
    f = open('/tmp/test-Grammar-dump.pickle', 'rb')
    g2 = Grammar()
    g2.loads(f.read())
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.start == g

# Generated at 2022-06-13 17:58:52.343612
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # This is the actual Grammar.dump method, with a single assignment
    # to self.start
    def dump(self, filename):
        d = self.__dict__
        d["start"] = 16
        with tempfile.NamedTemporaryFile(
            dir=os.path.dirname(filename), delete=False
        ) as f:
            pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
        os.replace(f.name, filename)

    import pytest

    filename = "test_filename"
    g = Grammar()
    g.dump = dump
    patchable_dump = lambda self, filename: dump(self, filename)
    g.dump.__globals__["dump"] = patchable_dump
    g.dump(filename)
    assert g.start == 16

# Generated at 2022-06-13 17:58:56.331631
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # The filename parameter should not be checked for existence
    g = Grammar()
    g.dump("non-existent/file")

# Generated at 2022-06-13 17:58:59.447878
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test that there's no error when we try to dump a Grammar
    # instance.
    g = Grammar()
    fd, f = tempfile.mkstemp(prefix="Grammar_dump", suffix=".tmp")
    try:
        g.dump(f)
    finally:
        os.close(fd)
        os.remove(f)

# Generated at 2022-06-13 17:59:08.300443
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'foo': 1}
    g.number2symbol = {1: 'foo'}
    g.states = [[(0, 0)]]
    g.dfas = {1: (g.states[0], {1: 1})}
    g.labels = [(0, "EMPTY"), (1, 'foo')]
    g.start = 1
    g.dump('graminit.py')

if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:59:11.151400
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    G = Grammar()
    tmpname = os.path.join(tempfile.gettempdir(),
                           next(tempfile._get_candidate_names()))
    G.dump(tmpname)
    G.load(tmpname)
    os.remove(tmpname)


# Generated at 2022-06-13 17:59:21.887326
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tempdir:
        g = Grammar()
        temp_filename = Path(tempdir, "test.pkl")
        g.dump(temp_filename)
        assert pickle.loads(temp_filename.read_bytes()) == {
            "async_keywords": False,
            "dfas": {},
            "keywords": {},
            "labels": [(0, "EMPTY")],
            "number2symbol": {},
            "start": 256,
            "states": [],
            "symbol2label": {},
            "symbol2number": {},
            "tokens": {},
        }

# Generated at 2022-06-13 17:59:25.128539
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(__file__.replace(".py", ".pkl"))


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:59:29.575626
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import tokenize

    gr = Grammar()
    gr.start = 3
    gr.symbol2number = {'foo': 2}
    gr.number2symbol = {2: 'foo'}
    gr.keywords = {'else': 1}
    gr.tokens = {3: 1}
    gr.symbol2label = {'foo': 1}
    gr.labels = [(3, "bar")]
    gr.states = [[[(1, 2)]]]
    gr.dfas = {2: (gr.states[0], {1: 1})}
    gr.dump("Grammar.dump")

    # mypyc generates objects that don't have a __dict__, but they
    # do have __getstate__ methods that will return an equivalent
    # dictionary
   

# Generated at 2022-06-13 17:59:40.003454
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # mypyc generates objects that don't have a __dict__, but they
    # do have __getstate__ methods that will return an equivalent
    # dictionary
    class DummyGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.dummy = "dummy"

        def __getstate__(self):
            d = super().__getstate__()
            d["dummy"] = self.dummy
            return d

    tmpfile = tempfile.mkstemp()
    dummygrammar = DummyGrammar()
    dummygrammar.dump(tmpfile[1])
    with open(tmpfile[1], "rb") as f:
        contents = f.read()
    os.unlink(tmpfile[1])
