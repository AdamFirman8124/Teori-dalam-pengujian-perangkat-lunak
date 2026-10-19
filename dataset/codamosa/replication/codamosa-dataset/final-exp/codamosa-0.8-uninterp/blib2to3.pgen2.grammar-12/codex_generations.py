

# Generated at 2022-06-13 17:49:49.109769
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.dump("./tmp.pkl")


# Generated at 2022-06-13 17:49:59.749716
# Unit test for method load of class Grammar

# Generated at 2022-06-13 17:50:10.397886
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import tokenize

    import io
    import sys

    if sys.platform != "win32":  # noqa: B950
        from .pytree import Node

        g = Grammar()
        g.start = 1
        g.symbol2number = {"A": 1, "B": 2}
        g.states = [[[(0, 0), (-1, 1)], [(0, 0)]]]

# Generated at 2022-06-13 17:50:16.301724
# Unit test for method load of class Grammar
def test_Grammar_load():
    gram = Grammar()
    print("tokens")
    print(gram.tokens)
    gram.load("C:/Users/Gaurav/PycharmProjects/python-parser/pythonparser"
              "/Grammar/Grammar/Grammar.pkl")
    print("tokens")
    print(gram.tokens)

# Generated at 2022-06-13 17:50:17.252384
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert Grammar().load(None) is None

# Generated at 2022-06-13 17:50:24.162901
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    This tests that Grammar.load() works properly
    """
    from .conv import convert
    from .pgen import generate

    grammar = Grammar()

    filename = "./Grammar.pickle"
    convert(grammar, generate)
    grammar.dump(filename)

    new_grammar = Grammar()
    new_grammar.load(filename)

    assert grammar.symbol2number == new_grammar.symbol2number
    assert grammar.number2symbol == new_grammar.number2symbol
    assert grammar.states == new_grammar.states
    assert grammar.dfas == new_grammar.dfas
    assert grammar.labels == new_grammar.labels
    assert grammar.keywords == new_grammar.keywords
    assert grammar.tokens == new_grammar

# Generated at 2022-06-13 17:50:33.366478
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class M(Grammar):
        def __init__(self):
            super().__init__()
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

    # Test empty dicts
    m = M()
    m.dump('test')
    # Test populated dicts
    m = M()
    m.symbol2number = {'a': 1, 'b': 2}
    m.number2symbol = {1: 'a', 2: 'b'}

# Generated at 2022-06-13 17:50:42.546230
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test Grammar.dump() by reading the produced pickle back.
    g = Grammar()
    g.symbol2number["A"] = 1
    g.symbol2number["B"] = 2
    g.number2symbol[1] = "A"
    g.number2symbol[2] = "B"
    g.keywords["a"] = 1
    g.keywords["b"] = 2
    g.tokens[1] = token.NAME
    g.tokens[2] = token.NAME
    g.symbol2label["A"] = 2
    g.symbol2label["B"] = 3
    g.labels = [(1, "a"), (token.NAME, None), (2, "A"), (2, "B")]
    g.start = 1

# Generated at 2022-06-13 17:50:49.740663
# Unit test for method load of class Grammar
def test_Grammar_load():
    import os
    import tempfile
    import pickle
    from .pgen2 import driver
    import pykeyword.parser

    _grammar_pickle = os.path.join(os.path.dirname(__file__), "Grammar35.pickle")

    def fp(s: str) -> bytes:
        return s.encode("utf-8")

    # Build AST from code
    g1 = Grammar()
    g1.load(_grammar_pickle)
    g2 = Grammar()
    g2.loads(pickle.dumps(g1, pickle.HIGHEST_PROTOCOL))

    # Ensure equality of ASTs
    assert g1.states == g2.states
    assert g1.dfas == g2.dfas
    assert g1.labels == g2

# Generated at 2022-06-13 17:50:56.733479
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import pickle
    import unittest
    import unittest.mock

    # Testing dump
    grammar = Grammar()
    filename = "test_io.pkl"
    grammar.dump(filename)
    mock_open = unittest.mock.mock_open()
    with unittest.mock.patch("pgen2.grammar.open", mock_open, create=True):
        grammar.dump(filename)
    mock_open.assert_called_once_with(filename, "wb")

# Generated at 2022-06-13 17:51:08.309964
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

# Generated at 2022-06-13 17:51:20.426032
# Unit test for method load of class Grammar
def test_Grammar_load():
    import os
    import pgen2.pgen
    from io import BytesIO

    filename, gramfile = pgen2.pgen.parse_grammar(
        start="file_input", pgen_path=os.path.dirname(__file__)
    )
    gram = Grammar()
    gram.load(filename)
    gram2 = gram.copy()
    with open(filename, "rb") as f:
        gram.loads(f.read())
    assert gram.dfas == gram2.dfas
    assert gram.states == gram2.states
    assert gram.labels == gram2.labels
    assert gram.number2symbol == gram2.number2symbol
    assert gram.symbol2number == gram2.symbol2number
    with BytesIO() as f:
        gram.dump

# Generated at 2022-06-13 17:51:24.639693
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(filename='../tests/files/grammar.pickle')
    n = 257
    if n in grammar.symbol2number.values():
        pass
    elif n in grammar.number2symbol.keys():
        pass
    elif n in grammar.number2symbol.keys():
        pass
    elif n in grammar.number2symbol.keys():
        pass


# Generated at 2022-06-13 17:51:34.565421
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    t = Grammar()
    t.start = 10
    t.symbol2number = {"foobar": 5, "python": 6}
    t.number2symbol = {5: "foobar", 6: "python"}
    t.states = [[(0, 0)]]
    t.labels = [(0, "EMPTY"), (1, "foobar"), (2, "python")]
    t.dfas = {6: ([(0, 0)], {0: 1}), 5: ([(1, 0)], {1: 1})}
    t.keywords = {"foobar": 1, "python": 2}
    t.tokens = {1: 1, 2: 2}
    t.symbol2label = {"foobar": 1, "python": 2}
    temp = tempfile.mkstemp()

# Generated at 2022-06-13 17:51:44.100302
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import conv
    from . import token
    from .pgen2 import tokenize

    # Parse the grammar file itself
    g = conv.Converter()
    g.convert_grammar(tokenize.detect_encoding(__file__)[0])
    g.finish_grammar()

    # Write the grammar tables to a pickle file
    g.grammar.dump("Grammar.pickle")

    # Read the grammar tables from the pickle file
    h = Grammar()
    h.load("Grammar.pickle")
    assert g.grammar.start == h.start
    assert g.grammar.labels == h.labels
    assert g.grammar.dfas == h.dfas
    assert g.grammar.keywords == h.keywords
    assert g.gram

# Generated at 2022-06-13 17:51:47.092236
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert

    g = Grammar()
    convert(g, "Grammar.txt", "Grammar.pkl")
    g.load("Grammar.pkl")
    g.report()

# Generated at 2022-06-13 17:51:51.294142
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class MyGrammar(Grammar):
        pass
    g = MyGrammar()
    d = g.__getstate__()
    g2 = MyGrammar()
    g2.dump("test.pkl")
    g2.load("test.pkl")
    assert g.__getstate__() == g2.__getstate__()
    os.remove("test.pkl")

# Generated at 2022-06-13 17:51:59.901969
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import ast
    import unittest
    import typing

    class TestGrammar(Grammar):
        pass

    if hasattr(typing, "TYPE_CHECKING"):
        class _Grammar(Grammar):
            def __init__(self):
                super().__init__()
        typing.cast(_Grammar, Grammar)

    class TestCase(unittest.TestCase):
        def test_dump_pickle_ast_grammar(self):
            grammar = TestGrammar()
            with tempfile.TemporaryFile(suffix=".pickle") as f:
                ast.grammar.dump(grammar, f)
                f.flush()
                f.seek(0)
                g = TestGrammar()
                g.load(f)

# Generated at 2022-06-13 17:52:09.576190
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pytest

    from .pgen2 import driver

    def compare_grammars(a: Grammar, b: Grammar) -> None:
        for attr in (
            "symbol2number",
            "number2symbol",
            "dfas",
            "keywords",
            "tokens",
            "symbol2label",
        ):
            assert getattr(a, attr) == getattr(b, attr)
        assert a.labels == b.labels
        assert a.states == b.states
        assert a.start == b.start
        assert a.async_keywords == b.async_keywords

    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "Grammar.pickle")

# Generated at 2022-06-13 17:52:17.691630
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Make a dummy grammar pickle and show that Grammar().load()
    can read it.
    """
    from .pgen2 import driver as pgen2

    g = pgen2.make_grammar()

    # We have to do this dance because we're trying to test
    # Grammar.loads on a pickled 4.0 grammar pickle
    # (myschema.pickle_38).  In that case, Grammar.loads fails
    # because the Grammar class has changed since the pickle was
    # created.  We have to create a new pickle with a schema number
    # that matches the current grammar version.

    g.dump("tmp.pickle")
    g.loads(open("tmp.pickle", "rb").read())
    gr = Grammar()
    gr.load("tmp.pickle")


# Generated at 2022-06-13 17:52:27.188278
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Save the current value of sys.path
    d = Grammar()
    fd, fn = tempfile.mkstemp(prefix='pyregrtest_Grammar_dump.', suffix='.py')
    with os.fdopen(fd, "wb") as f:
        d.dump(f)
    os.remove(fn)

if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:52:36.264515
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os, pickle, tempfile, unittest
    from . import token

    class GrammarSubclass(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.symbol2number = {'a': '1', 'b': '2', 'c': '3'}
            self.number2symbol = {'1': 'a', '2': 'b', '3': 'c'}
            self.states = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
            self.dfas = {'1': ([(1, 2), (3, 4)], {}), '2': ([(5, 6), (7, 8)], {})}
            self.labels = [(0, 'EMPTY')]

# Generated at 2022-06-13 17:52:47.977535
# Unit test for method load of class Grammar
def test_Grammar_load():
    start = 256

# Generated at 2022-06-13 17:52:52.837584
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pathlib
    with open(pathlib.Path(__file__).parent / "Grammar.pickle", 'rb') as f:
        g = Grammar()
        g.loads(f.read())

if __name__ == "__main__":
    import sys

    g = Grammar()
    g.load(sys.argv[1])
    g.report()

# Generated at 2022-06-13 17:52:58.060735
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.symbol2number = {'root': 256}
    g.dump("/tmp/foo")
    x = Grammar()
    x.load("/tmp/foo")
    assert x.symbol2number == {'root': 256}

# Generated at 2022-06-13 17:53:04.941645
# Unit test for method load of class Grammar
def test_Grammar_load():
    fn = "test.pickle"
    try:
        g = Grammar()
        g.dfas = {"a": (1, 2), "b": (3, 4)}
        g.labels = [(1, 5), (3, 6)]
        g.dump(fn)
        g2 = Grammar()
        g2.load(fn)
        assert g.dfas == g2.dfas
        assert g.labels == g2.labels
    finally:
        os.remove(fn)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_Grammar_load()

# Generated at 2022-06-13 17:53:16.554723
# Unit test for method load of class Grammar
def test_Grammar_load():
    # open a pickle file
    with open('../../Grammar-3.8.2.1.pickle', 'rb') as f:
        g = Grammar()
        g._update(pickle.load(f))

    assert isinstance(g, Grammar)

if __name__ == "__main__":
    import sys
    import pickle
    g = Grammar()
    g.load(sys.argv[1])
    with open('Grammar-3.8.2.1.pickle', 'wb') as f:
        pickle.dump(g.__dict__, f)

# Generated at 2022-06-13 17:53:20.991191
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver

    grammar = driver.load_grammar("Grammar.txt")
    with tempfile.TemporaryDirectory() as tempdir:
        grammar.dump(os.path.join(tempdir, "test.pkl"))

# Generated at 2022-06-13 17:53:31.361379
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    try:
        g.load("test_grammar_mypyc.pkl")
    except (EOFError, IOError, ImportError):
        pass  # no pickle file
    else:
        # mypyc generates objects that don't have a __dict__, but they
        # do have __getstate__ methods that will return an equivalent
        # dictionary
        if hasattr(g, "__dict__"):
            d = g.__dict__
        else:
            d = g.__getstate__()  # type: ignore
        for k, v in d.items():
            if k != "__name__":
                getattr(g, k)

if __name__ == "__main__":
    import sys

    g = Grammar()

# Generated at 2022-06-13 17:53:39.352880
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle

    g = Grammar()
    g.symbol2number = {'foo': 106}
    g.number2symbol = {106: 'foo'}
    g.states = [[[(0, 0)]]]
    g.dfas = {106: ([[(0, 0), (0, 0)]], {0: 1}), 107: ([[(0, 0), (0, 0)]], {0: 1})}
    g.labels = [(0, None), (1, None)]
    g.keywords = {'bar': 1}
    g.tokens = {105: 1}
    g.symbol2label = {'bar': 1}
    g.start = 256


# Generated at 2022-06-13 17:53:53.662021
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Test that the load() method of Grammar actually loads the
    attributes of the instance it is called upon.
    """
    from .conv import grammar_to_pgen

    pgen = grammar_to_pgen(token.grammar)
    pgen.save()
    path = pgen.path
    for name in ("symbol2number", "number2symbol", "states", "dfas", "labels", "keywords",
            "tokens", "symbol2label", "start"):
        attr_path = path + "." + name
        with open(attr_path, "rb") as f:
            attr = pickle.load(f)
        g = Grammar()
        g.load(path)
        assert getattr(g, name) == attr

# Generated at 2022-06-13 17:53:57.730232
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.number2symbol = {1: "a"}
    g.symbol2number = {"a": 1}
    try:
        g.dump(__file__ + ".pickle")
    finally:
        os.remove(__file__ + ".pickle")

# Generated at 2022-06-13 17:54:05.053977
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io
    import pickle
    from .parse import Grammar

    class FakeGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__()
            self.symbol2number = {b"foo": 1}  # type: Dict[bytes, int]
            self.number2symbol = {1: b"foo"}  # type: Dict[int, bytes]
            self.states = [[(1, 2), (3, 4)]]  # type: List[DFA]
            self.dfas = {1: ([2, 3], {2: 2})}  # type: Dict[int, DFAS]
            self.labels = [(1, b"foo")]  # type: List[Label]
            self.keywords = {b"foo": 1}

# Generated at 2022-06-13 17:54:06.113374
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(1)

# Generated at 2022-06-13 17:54:11.020928
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gram = Grammar()
    import io

    class fake_file:
        def __init__(self):
            self.io = io.BytesIO()

        def __enter__(self):
            return self.io

        def __exit__(self, type, value, traceback):
            self.io.close()

    gram.dump(fake_file())

test_Grammar_dump()

# Generated at 2022-06-13 17:54:17.899467
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class A(Grammar):
        def __init__(self, val: str) -> None:
            self.val = val
            Grammar.__init__(self)

    a = A("some string")
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    a.dump(f.name)
    b = A("some other string")
    b.load(f.name)
    os.remove(f.name)

# Generated at 2022-06-13 17:54:24.033604
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test dumping a grammar.

    This is done by loading the grammar for Python 2.7, saving it to
    a file, and loading it again.

    """
    from .pgen2 import driver

    g = driver.load_grammar(2.7)
    g.dump("Grammar.27.pickle")
    gg = driver.load_grammar("Grammar.27.pickle")
    assert g == gg

# Generated at 2022-06-13 17:54:33.498942
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'foo': 1, 'bar': 2}
    g.number2symbol = {1: 'foo', 2: 'bar'}
    g.labels = [(1, 'foo'), (2, 'bar')]
    g.dfas = {1: (1, 2), 2: (1, 2)}
    g.states = 2
    g.start = 1

    (fd, temp_fname) = tempfile.mkstemp()
    os.close(fd)

    try:
        g.dump(temp_fname)
        g.load(temp_fname)
        assert g.states == 2
    finally:
        os.remove(temp_fname)


# Generated at 2022-06-13 17:54:43.506511
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gram = Grammar()
    gram.symbol2number = "symbol2number"
    gram.number2symbol = "number2symbol"
    gram.states = "states"
    gram.dfas = "dfas"
    gram.labels = "labels"
    gram.keywords = "keywords"
    gram.tokens = "tokens"
    gram.symbol2label = "symbol2label"
    gram.start = "start"
    gram.async_keywords = "async_keywords"
    with tempfile.NamedTemporaryFile() as f:
        gram.dump(f.name)
        with open(f.name, "rb") as f2:
            assert pickle.load(f2) == gram.__dict__



# Generated at 2022-06-13 17:54:53.387979
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import tempfile
    from .parse import Parser

    class GrammarSubclass(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.symbol2number["symbol1"] = 257
            self.number2symbol[257] = "symbol1"
            self.states = [[[(0, 0), (1, 0)], []]]
            self.dfas[257] = [[[(0, 0), (1, 0)], []], {"token1": 1}]
            self.labels = [(0, "EMPTY"), (1, "token1")]
            self.start = 257
            self.keywords["keyword1"] = 3

    tmpdir = tempfile.TemporaryDirectory()