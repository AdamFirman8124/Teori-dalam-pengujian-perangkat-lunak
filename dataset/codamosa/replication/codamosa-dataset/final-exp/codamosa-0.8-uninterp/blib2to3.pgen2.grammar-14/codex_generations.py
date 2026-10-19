

# Generated at 2022-06-13 17:49:55.514537
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("/tmp/grammar")
    g2 = Grammar()
    g2.load("/tmp/grammar")
    assert g2.number2symbol == g.number2symbol
    assert g2.symbol2number == g.symbol2number
    assert g2.states == g.states
    assert g2.dfas == g.dfas
    assert g2.labels == g.labels
    assert g2.keywords == g.keywords
    assert g2.tokens == g.tokens
    assert g2.symbol2label == g.symbol2label
    assert g2.start == g.start
    assert g2.async_keywords == g.async_keywords

# Generated at 2022-06-13 17:50:04.619071
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    from pgen2.parse import parse
    from pgen2.driver import Driver

    class _TestDriver(Driver):
        def __init__(self, *args, **kwds):
            super().__init__(*args, **kwds)
            self.tokens = []

        def log(self, tok, type, value, start, end, line):
            self.tokens.append(type)

    class _TestCase(unittest.TestCase):
        def test_load(self):
            grammar = Grammar()
            grammar.load(
                os.path.join(os.path.dirname(__file__), "..", "Python.pgen")
            )
            self.assertEqual(256, grammar.start)

            parser = parse(grammar)
            # Spec

# Generated at 2022-06-13 17:50:16.534802
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2
    from . import driver
    from .parse import PyCF_ONLY_AST
    import sys, os

    def lint(filename):
        # lint the file using the current grammar file
        argv = [sys.executable, '-m', 'pylint', filename]
        output = driver._run_pylint(argv)
        assert output
        print(output, file=sys.stdout)

    # generate a pickle file based on the current grammar
    pickle_file = os.path.join(os.path.dirname(__file__), 'Grammar.pickle')
    g = pgen2._generate_grammar(['Grammar.txt'])
    g.dump(pickle_file)

    # load the pickle file and test it

# Generated at 2022-06-13 17:50:22.993598
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number['ababa'] = 1
    g.symbol2number['baaba'] = 2
    g.number2symbol[1] = 'ababa'
    g.number2symbol[2] = 'baaba'
    g.states = [[(1, 'a'), (2, 'b')], [(3, 'c'), (4, 'd')]]
    g.dfas = {1: (g.states[0], {5: 1, 6: 1}), 2: (g.states[1], {7: 1, 8: 1})}
    g.labels = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    g.keywords = {'abc': 5, 'def': 3}

# Generated at 2022-06-13 17:50:31.156893
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pytest
    from pickle import load, dump
    import shutil

    g = Grammar()
    g.symbol2number["HELLO"] = 1
    g.number2symbol[1] = "HELLO"
    g.states = [[[(0, 0), (1, 1)], [(2, 2), (3, 3)]]]
    g.dfas = {1: ([[(0, 0), (1, 1)], [(2, 2), (3, 3)]], {})}
    g.labels = [(0, "EMPTY"), (1, "ONE"), (2, "TWO"), (3, "THREE")]
    g.keywords = {"HELLO": 1}
    g.tokens = {4: 1}

# Generated at 2022-06-13 17:50:36.776412
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.dfas = {0: ([[(0, 0)]], {0: 0})}
    fname = "test.pickle"
    g.dump(fname)
    g2 = Grammar()
    g2.load(fname)
    assert g.dfas == g2.dfas

# Generated at 2022-06-13 17:50:44.743340
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    tables = Grammar()
    tables.symbol2number["_NT"] = 256
    tables.number2symbol[256] = "_NT"
    tables.states.append([(260, 257)])
    tables.keywords["def"] = 261
    tables.tokens[token.LPAR] = 262
    tables.symbol2label["s"] = 263
    tables.labels.append((261, "def"))
    tables.labels.append((262, None))
    tables.labels.append((263, None))
    tables.start = 256

    with tempfile.TemporaryDirectory() as directory:
        filename = os.path.join(directory, "pgen_tables.pickle")
        tables.dump(filename)
        saved = Grammar()
        saved.load(filename)

        assert saved.sy

# Generated at 2022-06-13 17:50:55.813231
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import sys
    import time

    class GrammarSubclass(Grammar):

        def __init__(self) -> None:
            super().__init__()
            self.a = "b"
            self.c = 1

    # In Python 3, NamedTemporaryFile will not unlink the file, since the file
    # is open.  If it is unlinked, the file descriptor is still open, and
    # os.replace will fail with [Errno 22] Invalid argument.  NamedTemporaryFile
    # restores the unlink flag after closing the file.  See
    # https://bugs.python.org/issue14243
    with tempfile.NamedTemporaryFile(delete=False) as f_name:
        f_name.close()
        pickle_file = f_name.name

# Generated at 2022-06-13 17:51:03.930548
# Unit test for method load of class Grammar
def test_Grammar_load():
    # pylint: disable=unused-variable,import-error
    import unittest

    from io import BytesIO
    from io import StringIO
    from unittest import TestCase

    # pylint: disable=invalid-name,missing-docstring,no-self-use
    class GrammarTest(TestCase):
        def test_load(self):
            class MyGrammar(Grammar):
                pass

            mg = MyGrammar()
            self.assertEqual(mg.symbol2number, {})

# Generated at 2022-06-13 17:51:13.550463
# Unit test for method load of class Grammar
def test_Grammar_load():
    class SGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__()
            self.symbol2number = {"a": 256, "b": 257}

    g = SGrammar()
    fd, fn = tempfile.mkstemp()
    os.close(fd)

    with tempfile.NamedTemporaryFile() as t:
        g.dump(t.name)
        os.replace(t.name, fn)
        g.load(fn)
    assert g.symbol2number == {"a": 256, "b": 257}

# Generated at 2022-06-13 17:51:18.460262
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump('/tmp/pgen_test')

# Generated at 2022-06-13 17:51:25.489961
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import convert

    g = Grammar()
    with tempfile.NamedTemporaryFile() as f:
        filename = f.name
        convert(g, filename)
        g.dump(filename)
        g2 = Grammar()
        g2.load(filename)
        assert g2.symbol2number == g.symbol2number
        assert g2.number2symbol == g.number2symbol
        assert g2.states == g.states
        assert g2.dfas == g.dfas
        assert g2.labels == g.labels
        assert g2.keywords == g.keywords
        assert g2.symbol2label == g.symbol2label
        assert g2.start == g.start

# Generated at 2022-06-13 17:51:35.177039
# Unit test for method load of class Grammar

# Generated at 2022-06-13 17:51:39.582840
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Check Grammar.load produces a usable grammar."""
    import io
    import tokenize

    g = Grammar()
    g.load(io.BytesIO(pickle.dumps(g)))

    dfa = g.dfas[g.symbol2number["file_input"]][0]
    for i in range(len(g.states)):
        state = g.states[i]
        for arc in state:
            label = g.labels[arc[0]]
            if label[0] is None:
                pass
            elif label[0] == token.OP:
                label = (opmap[label[1]], label[1])
            elif label[0] == token.NAME:
                pass
            elif label[0] == token.NEWLINE:
                pass

# Generated at 2022-06-13 17:51:49.479791
# Unit test for method load of class Grammar
def test_Grammar_load():
    from test import test_grammar

    class Gr(Grammar):
        def add_nonterminal(self, name, num, dfas):
            num = self.symbol2number.get(name, num)
            self.symbol2number[name] = num
            self.number2symbol[num] = name
            self.states.append(dfas)
            self.dfas[num] = dfas, {}

        def finish_nonterminal(self, name, num):
            pass

    g = Gr()
    g.add_nonterminal("a", 257, [[[(1, 1), (2, 2)], [(3, 1), (4, 2)]]])

# Generated at 2022-06-13 17:51:59.034304
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.start = 1
    g.labels = [1, 2]
    g.states = [1, 2]
    g.dfas = {1: [1, 2]}
    g.tokens = {1: 1, 2: 2}
    g.keywords = {1: 1, 2: 2}
    g.number2symbol = {1: 1, 2: 2}
    g.symbol2label = {1: 1, 2: 2}
    g.symbol2number = {1: 1, 2: 2}

    g.dump("test_Grammar_dump.pkl")

    g2 = Grammar()
    g2.load("test_Grammar_dump.pkl")
    os.remove("test_Grammar_dump.pkl")



# Generated at 2022-06-13 17:52:02.028263
# Unit test for method load of class Grammar
def test_Grammar_load():
    mg = Grammar()
    assert not mg.dfas
    # Test that the instance variables initialized by __init__
    # are overwritten by load()
    mg.load("Grammar/Grammar.tbl")
    assert mg.dfas

# Generated at 2022-06-13 17:52:11.799669
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

    # raise exception if file not exist
    filename = 'file_not_exist'
    try:
        g.load(filename)
    except (FileNotFoundError, IOError):
        pass
    else:
        assert False

    file = tempfile.NamedTemporaryFile()

    # test dump
    g.dump(file.name)
    d = pickle.load(file)
    assert d == {
        'symbol2number': {}, 'number2symbol': {}, 'states': [], 'dfas': {},
        'labels': [(0, 'EMPTY')], 'keywords': {}, 'tokens': {}, 'symbol2label': {},
        'start': 256, 'async_keywords': False
    }

    # test load

# Generated at 2022-06-13 17:52:14.004765
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    This is just testing class Grammar has this method
    """
    import StringIO

    g = Grammar()
    g.load(StringIO.StringIO())

# Generated at 2022-06-13 17:52:23.837253
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import target
    from .conv import conv
    from .pgen import pgen

    g = Grammar()
    assert not g.number2symbol
    assert not g.symbol2number
    assert not g.states
    assert not g.dfas
    assert g.labels == [(0, 'EMPTY')]
    assert not g.keywords
    assert not g.tokens
    assert not g.symbol2label
    assert g.start == 256
    assert not g.async_keywords

    t = target.Target("grammar")
    c = conv.Converter(t)
    c.setGrammar(pgen.Grammar())
    c.run()

    g = Grammar()
    g.load(t.getGrammarPickleFile())

    assert g.number

# Generated at 2022-06-13 17:52:28.574345
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    assert grammar.start == 256
    grammar.load("test/Parser/pgen2-sample.pickle")
    assert grammar.start == 256


# Generated at 2022-06-13 17:52:36.635784
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    d = g.symbol2number # type: Dict[str, int]
    def __getitem__(d: Dict[str, int], key: str) -> int:
        return d[key]
    def __setitem__(d: Dict[str, int], key: str, value: int) -> None:
        d[key] = value
    __getitem__(d, "error_leader")
    __setitem__(d, "error_leader", 1)
    f = tempfile.NamedTemporaryFile(dir="/tmp")
    g.dump(f.name)
    g.load(f.name)
    f.close()


# Generated at 2022-06-13 17:52:40.361570
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = os.path.join(os.path.dirname(__file__), "Grammar.pkl")
    t = Grammar.load(filename)

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:52:44.779783
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    fname = "test_Grammar_dump"
    grammar.dump(fname)
    with open(fname, "rb") as f:
        d = pickle.load(f)
    assert isinstance(d, dict)



# Generated at 2022-06-13 17:52:54.617612
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pygram
    from . import pgen2

    sys.argv = sys.argv[:1]  # reset sys.argv to [__main__]

    g = Grammar()
    g.load(pgen2.pgen)  # Pass
    assert g.start == 256
    assert g.tokens[41] == 2
    assert g.keywords["elif"] == 3

    # pgen2.pgen is the table for Python 2.7
    pygram.python_grammar.load(pgen2.pgen)
    assert pygram.python_grammar.start == 256
    assert pygram.python_grammar.tokens[41] == 2
    assert pygram.python_grammar.keywords["elif"] == 3


# Generated at 2022-06-13 17:53:02.800067
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.symbol2number = {'STMT': 256}
    g.number2symbol = {256: 'STMT'}
    fd, fname = tempfile.mkstemp()
    os.close(fd)
    try:
        g.dump(fname)
        g2 = Grammar()
        g2.load(fname)
        assert g.symbol2number == g2.symbol2number
        assert g.number2symbol == g2.number2symbol
    finally:
        os.remove(fname)

# Generated at 2022-06-13 17:53:11.702672
# Unit test for method load of class Grammar
def test_Grammar_load():
    # pickle file of class Grammar
    pkl_fname = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "Grammar27.pkl"
    )

    g = Grammar()
    g.load(pkl_fname)
    # load the grammar tables from the file Grammar27.pkl

# Generated at 2022-06-13 17:53:22.948742
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import grammar, parse, tokenize

    # Check that the methods dump, load, loads and report of class Grammar
    # work as expected.
    g = grammar.Grammar()
    g.parse(grammar.Grammar)
    gfile = tempfile.mktemp()
    g.dump(gfile)
    g2 = g.copy()
    g2.load(gfile)
    pf = parse.ParserFacade(g2)
    tok = tokenize.generate_tokens(pf.line_reader("1 + 1"))
    pf.parse(tok, "eval_input", "single")
    tfile = tempfile.mktemp()
    g2.dump(tfile)
    g3 = g2.copy()
    g3.load(tfile)

# Generated at 2022-06-13 17:53:28.344970
# Unit test for method load of class Grammar
def test_Grammar_load():
    gp = Grammar()
    gp.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    gp.report()

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:53:39.073205
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    filename = "test_Grammar_dump.pkl"
    g.dump(filename)
    with open(filename, "rb") as f:
        g2 = pickle.load(f)
    assert g2.keywords == {}
    assert g2.tokens == {}
    assert g2.symbol2label == {}
    assert g2.labels == [(0, "EMPTY")]
    assert g2.start == 256

# Generated at 2022-06-13 17:53:54.156993
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("test_grammar")
    with open("test_grammar", "rb") as f:
        d = pickle.load(f)
    assert d["symbol2number"] == g.symbol2number
    assert d["number2symbol"] == g.number2symbol
    assert d["states"] == g.states
    assert d["dfas"] == g.dfas
    assert d["labels"] == g.labels
    assert d["keywords"] == g.keywords
    assert d["tokens"] == g.tokens
    assert d["symbol2label"] == g.symbol2label
    assert d["start"] == g.start

# Generated at 2022-06-13 17:53:55.157820
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("filename")

# Generated at 2022-06-13 17:54:03.423782
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import tokenize

    # Create a pickle file
    filename = "Grammar.pickle"
    del tokenize.generate_tokens
    try:
        tokenize.tokenize
    except AttributeError:
        raise unittest.SkipTest("tokenize.tokenize not available")  # type: ignore

    g = tokenize.generate_tokens(iter(["2+2"]).__next__)
    g.next()

    with open(filename, "wb") as f:
        pickle.dump(g.grammar, f, pickle.HIGHEST_PROTOCOL)

    # Load the pickle file
    g = Grammar()
    g.load(filename)
    os.remove(filename)


# Generated at 2022-06-13 17:54:08.831318
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pgen2.pgen
    from pgen2.grammar import PgenParser
    pgenParser = PgenParser()

    # In the startup of this file, there is a line that assumes that
    # the grammar is present in the relative path 'Grammar.txt'; it
    # uses this grammar in building 'pgenGrammar'.  Use this
    # assumption to determine the 'Grammar.txt' file.
    pgenFile = pgenParser.pgenGrammar.pgenFile

    # Instantiate a Parser object with pgenGrammar
    parser = pgenParser.makeParser(pgenParser.pgenGrammar)
    assert parser

    # Save this Parser's grammar to pickle file 'Grammar.txt'
    parser.grammar.dump(pgenFile)

    # Instantiate another

# Generated at 2022-06-13 17:54:11.878973
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import builtins
    import io
    import pickle
    import sys

    g = builtins.__dict__["__builtins__"].__dict__["__grammar__"]
    f = io.BytesIO()
    g.dump(f)
    expected = f.getvalue()
    f = io.BytesIO()
    pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)
    actual = f.getvalue()
    assert expected == actual


# Generated at 2022-06-13 17:54:12.995942
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    pass


# Generated at 2022-06-13 17:54:21.975320
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class MyGrammar(Grammar):
        def __init__(self):
            Grammar.__init__(self)

# Generated at 2022-06-13 17:54:28.823615
# Unit test for method load of class Grammar
def test_Grammar_load():

    # save tables
    g = Grammar()
    d = {"abc": 123}
    with tempfile.NamedTemporaryFile(mode="wb") as f:
        pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
        name = f.name
    g.loads(pickle.dumps(d, pickle.HIGHEST_PROTOCOL))
    assert g.abc == 123  # pylint: disable=no-member
    g.abc = 456  # pylint: disable=assignment-from-no-return
    assert g.abc == 456  # pylint: disable=no-member
    g.dump(name)
    with open(name, "rb") as f:
        d2 = pickle.load(f)
    assert d == d2


# Generated at 2022-06-13 17:54:34.342805
# Unit test for method load of class Grammar
def test_Grammar_load():
    try:
        from .parse import ParseError
    except ImportError:
        return
    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    from . import tokenize

    try:
        g.parse(tokenize.generate_tokens(b"a"), "eval_input")
    except ParseError:
        pass
    else:
        raise AssertionError("parse() should raise ParseError")

# Generated at 2022-06-13 17:54:41.837879
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Test method load of class Grammar."""
    from . import test_grammar
    from .parse import Parser

    g = test_grammar.grammar()
    filename = "Lib/test/pgen/test_grammar.pkl"
    g.dump(filename)
    g2 = Grammar()
    g2.load(filename)
    os.remove(filename)
    p = Parser(g2)
    x = p.parse("if 1: pass")


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:54:51.803234
# Unit test for method load of class Grammar
def test_Grammar_load():
    try:
        import pickle_grammar
    except ImportError:
        return
    expected = Grammar()
    expected.loads(pickle_grammar.pickle_grammar)
    actual = Grammar()
    actual.load(pickle_grammar.__file__)
    assert len(expected.states) == len(actual.states)
    for i, state in enumerate(expected.states):
        assert state == actual.states[i]
    for key, value in expected.__dict__.items():
        if key == "states":
            continue
        assert getattr(expected, key) == getattr(actual, key)

# Generated at 2022-06-13 17:54:58.941577
# Unit test for method load of class Grammar
def test_Grammar_load():
    import difflib
    import sys

    # Generate a temporary .pickle file to load from
    from . import conv

    g = Grammar()
    c = conv.Converter()
    c.convert()
    g.__init__()
    g.dfas = c.dfas
    g.labels = c.labels
    g.start = c.start
    g.states = c.states
    g.keywords = c.keywords
    g.number2symbol = c.number2symbol
    g.symbol2label = c.symbol2label
    g.symbol2number = c.symbol2number
    g.tokens = c.tokens
    f = tempfile.NamedTemporaryFile(mode="w+b", delete=False)
    f.close()


# Generated at 2022-06-13 17:55:09.700549
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Test function load of class Grammar

    import unittest

    from . import pgen2
    from . import pgen2_grammar

    from .pgen2 import driver

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.g = Grammar()
            self.g.load(pgen2.grammar_pkl)

        def test_load(self):
            # Walk through the grammar using the parse driver and test that
            # the grammar is complete by parsing the program "None".
            # We could have used 'eval' but the driver is more general.
            driver.NullParser().parse(b"None", self.g)

        def test_main(self):
            driver.main([pgen2_grammar.__file__, pgen2.grammar_pkl])



# Generated at 2022-06-13 17:55:14.567181
# Unit test for method load of class Grammar
def test_Grammar_load():
    pickle_file = """\
cos\nsystem\n(S'echo foobar'\ntR.\
"""
    Grammar().loads(pickle_file)


if __name__ == "__main__":
    import doctest
    from . import conv, pgen

    doctest.testmod()
    g = Grammar()
    g.load(conv.pickle_file)
    g.report()
    g = pgen.generate_grammar("Grammar.txt")
    g.report()

# Generated at 2022-06-13 17:55:23.186225
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {"foo": 256, "bar": 257}
    grammar.number2symbol = {256: "foo", 257: "bar"}
    grammar.states = [[[(0, 0)], [(1, 2)], []]]
    grammar.dfas = {256: (grammar.states[0], {1: 1})}
    grammar.labels = [(1, None), (0, "EMPTY")]
    grammar.keywords = {}
    grammar.tokens = {}
    grammar.symbol2label = {}
    grammar.start = 256
    # Python 3.7+ parses async as a keyword, not an identifier
    grammar.async_keywords = False
    grammar.dump("test_Grammar_dump.pkl")


# Generated at 2022-06-13 17:55:31.709990
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()

# Generated at 2022-06-13 17:55:39.762915
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    This method tests Grammar.load.

    Note that if Grammar.load is changed, Grammar.loads must also
    change correspondingly.

    """

    class DerivedGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__()
            self.example = "example"

    g1 = DerivedGrammar()
    g1.symbol2number = {"None": 0, "a": 1, "b": 2}
    g1.number2symbol = {0: "None", 1: "a", 2: "b"}
    g1.states = [[[(0, 0), (1, 1), (2, 2)], [(0, 3), (2, 0)]], [[(1, 0)]]]

# Generated at 2022-06-13 17:55:49.766368
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen import driver
    import unittest
    import pickle
    import os
    import tempfile
    import sys
    import py_compile

    class Grammar_Methods(unittest.TestCase):
        def setUp(self):
            if not hasattr(self, "assertIsInstance"):
                self.assertIsInstance = unittest.TestCase.assertTrue
            if not hasattr(self, "assertIsNotNone"):
                self.assertIsNotNone = unittest.TestCase.assertTrue


# Generated at 2022-06-13 17:55:53.803490
# Unit test for method load of class Grammar
def test_Grammar_load():
    import ast, tempfile
    grammar = Grammar()
    f = tempfile.NamedTemporaryFile(delete=False)
    pkl = pickle.dumps(grammar.__dict__)
    f.write(pkl)
    f.close()
    grammar.load(f.name)
    with open(f.name, "rb") as f:
        assert pickle.load(f) == grammar.__dict__
    os.remove(f.name)


# Generated at 2022-06-13 17:55:58.607858
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import pickle
    from .token import NAME
    from .tokenize import tokenize

    if sys.version_info[:2] >= (3, 8):
        # Python 3.8+ version uses new grammar.
        for suffix in ("", "_async"):
            def gen_grammar(suffix=""):
                g = Grammar()  # type: ignore
                g.start = 1 + 256
                g.number2symbol = {"1": "file_input"}
                g.tokens = {NAME: 5 + 256}
                g.symbol2number = {"file_input": 1 + 256}
                g.keywords = {"foo": 5 + 256}
                g.symbol2label = {"file_input": 1 + 256}

# Generated at 2022-06-13 17:56:12.675001
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import token
    from .parse import Grammar

    g = Grammar()
    g.load("./Grammar.pickle")


# Generated at 2022-06-13 17:56:14.577834
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.loads(test_Grammar_dump())

# Store test data for method dump of class Grammar

# Generated at 2022-06-13 17:56:17.327452
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    f = tempfile.NamedTemporaryFile()
    g.dump(f.name)
    f.close()


# Generated at 2022-06-13 17:56:25.933607
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Test case for method load of class Grammar
    # See issue 13352
    import types
    import sys
    import unittest
    import pkgutil

    GSTest = unittest.TestCase("__init__")

    # When getting the grammar from test_grammar in 2.7 and all
    # versions of Python 3 (including PyPy3) the grammar is in a
    # pyc_bundle_archive. In 3.4 it is not, but thankfully it is
    # always in a module.
    p = 'test.support.parser_data' if sys.version_info[:2] == (3, 4) else 'test.support.test_grammar'
    g = pkgutil.get_data(p, 'Grammar.txt')
    gram = Grammar()
    # Make sure an exception is thrown if

# Generated at 2022-06-13 17:56:26.536366
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load()

# Generated at 2022-06-13 17:56:31.362822
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {'STMT': 258, 'expr': 259, 'testlist': 260, 'test': 261}
    grammar.number2symbol = {258: 'STMT', 259: 'expr', 260: 'testlist', 261: 'test'}
    grammar.states = [[],
                      [(258, 1), (0, 2)],
                      [(258, 2)],
                      [(260, 4), (261, 6), (260, 7), (0, 5)],
                      [(260, 5)],
                      [(259, 5)],
                      [(258, 5)],
                      [(261, 5)],
                      [(258, 5)]]

# Generated at 2022-06-13 17:56:40.836130
# Unit test for method dump of class Grammar

# Generated at 2022-06-13 17:56:49.365662
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pgen2

    g = pgen2.driver.load_grammar("Grammar.txt")
    assert g.start == 257
    assert len(g.symbol2number) == 274
    assert len(g.number2symbol) == 274
    assert len(g.states) == 326
    assert len(g.dfas) == 274
    assert len(g.labels) == 588
    assert len(g.keywords) == 0
    assert len(g.tokens) == 0
    assert len(g.symbol2label) == 274
    assert not g.async_keywords

# Generated at 2022-06-13 17:56:58.942474
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import ast
    import io
    import os

    class MyGrammar(Grammar):
        def __init__(self) -> None:
            Grammar.__init__(self)
            self.symbol2number = {"s": 0}
            self.number2symbol = {0: "s"}
            self.states = [[[(1, 0), (2, 0)]]]
            self.dfas = {0: (self.states[0], {1: 1, 2: 1})}
            self.labels = [(1, None), (2, None)]
            self.keywords = {}
            self.tokens = {}
            self.symbol2label = {}
            self.start = 256

    g = MyGrammar()

    output = io.BytesIO()
    g.dump(output)

# Generated at 2022-06-13 17:57:03.606102
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    filename = os.path.abspath(__file__) + '_dump_grammar_test'
    grammar.dump(filename)
    grammar_copy = Grammar()
    grammar_copy.load(filename)
    for attr in ('symbol2number', 'number2symbol', 'states', 'dfas', 'labels', 'keywords', 'tokens', 'start'):
        assert getattr(grammar, attr) == getattr(grammar_copy, attr)
    os.remove(filename)


if __name__ == "__main__":
    test_Grammar_dump()
    print("Everything passed")

# Generated at 2022-06-13 17:57:18.864446
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle

# Generated at 2022-06-13 17:57:33.914503
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert  # type: ignore
    from .pgen import generate  # type: ignore

    # Create the following grammar and save it to a temporary file:
    #
    # expr = expr + term | expr - term | term
    # term = term * factor | term / factor | factor
    # factor = digit
    # digit = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    #
    # The grammar is encoded with the following non-terminals,
    # literals, and productions:
    #
    # non-terminals: (expr, term, factor, digit)
    # literals: ('+', '-', '*', '/', '0', 1', '2', '3', '4', '5',
    #            '6', '7', '8', '9')
   

# Generated at 2022-06-13 17:57:37.227717
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    assert not os.path.isfile('Grammar.pickle')
    g.dump('Grammar.pickle')
    assert os.path.isfile('Grammar.pickle')
    os.remove('Grammar.pickle')

# Generated at 2022-06-13 17:57:41.646790
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("./Parser/Grammar.py.pkl")
    assert g.symbol2number['stmt'] == 258


if __name__ == "__main__":
    import sys

    g = Grammar()
    name = sys.argv[1]
    if name == "-":
        g.loads(sys.stdin.buffer.read())
    else:
        g.load(name)
    g.report()

# Generated at 2022-06-13 17:57:52.795370
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test the method dump() of the class Grammar."""
    grammar_object = Grammar()
    assert not isinstance(grammar_object, Grammar)  # before calling dump()
    # use dump() to convert the object to a dump format
    grammar_object.dump('grammar_object_dump')
    # load a new Grammar object from the dump file
    reloaded_grammar_object = Grammar()
    reloaded_grammar_object.load('grammar_object_dump')
    assert isinstance(reloaded_grammar_object, Grammar)  # after calling load()

# Generated at 2022-06-13 17:57:57.922518
# Unit test for method load of class Grammar

# Generated at 2022-06-13 17:58:03.035940
# Unit test for method load of class Grammar
def test_Grammar_load():
    fil = "../../Grammar/Grammar3.6.9"
    import pickle
    with open(fil, "rb") as f:
        d = pickle.load(f)
    g = Grammar()
    g.load(fil)
    assert g.symbol2number == d['symbol2number']
    assert g.number2symbol == d['number2symbol']

# Generated at 2022-06-13 17:58:05.901255
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver

    p = driver.load_grammar()
    p.dump("Grammar.dump")


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:58:15.643988
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import gzip

    gram = Grammar()
    gram.number2symbol = {"x": "1", "y": "2", "z": "3"}
    gram.symbol2number = {"1": "x", "2": "y", "3": "z"}
    gram.states = [
        [(1, 2), (4, 5), (7, 8)],
        [(9, 10), (11, None), (11, 5)],
        [(12, 5), (11, 13)],
        [],
    ]
    gram.dfas = {0: ([[(6, 2), (6, 4), (6, 5), (0, 3)]], {11: 1}), 3: ([[(0, 4)]], {})}

# Generated at 2022-06-13 17:58:23.011437
# Unit test for method load of class Grammar
def test_Grammar_load():
    class DummySubclass(Grammar):
        pass
    d = Grammar()
    d.a = 123
    d.b = {1, 2, 3}
    d.c = {1: 1, 2: 2}
    d.d = {1: {1, 2, 3}}
    d.e = [1, 2, 3]
    dumpfile = tempfile.NamedTemporaryFile()
    d.dump(dumpfile.name)
    d2 = DummySubclass()
    d2.load(dumpfile.name)
    assert d2.a == d.a
    assert d2.b == d.b
    assert d2.c == d.c
    assert d2.d == d.d
    assert d2.e == d.e

# Generated at 2022-06-13 17:58:31.763739
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class FakeGrammar(Grammar):
        def __getstate__(self) -> Dict[str, Any]:
            return {}

    start_options = os.name in ["nt", "posix"]
    g = FakeGrammar()
    g.dump("graminit.py")
    assert os.path.exists("graminit.py") == start_options
    if start_options:
        os.remove("graminit.py")

    try:
        g.loads(b"")
    except pickle.PicklingError:
        pass
    else:
        raise RuntimeError("expected a pickling error")

    g.number2symbol = {}
    g.copy()

# Generated at 2022-06-13 17:58:41.079666
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # This function must be self contained, to ensure that it can run
    # standalone, as well as being importable.
    import sys

    # Strategy:
    # 1. Make a grammar and dump it.
    # 2. Use importlib to load the dump.
    # 3. Read sys.stdout to see if everything worked okay.

    # Make a Grammar instance, with a dummy value
    g = Grammar()
    g.dfas[1] = ([(3, 4)], {1: 1})
    g.number2symbol[1] = "POP_TOP"
    g.labels[3] = (1, None)
    g.labels[4] = (1, None)
    g.symbol2number["POP_TOP"] = 1

    # Save the grammar to a string

# Generated at 2022-06-13 17:58:42.540823
# Unit test for method load of class Grammar
def test_Grammar_load():
    l = [0, 1, 2]
    assert l == load_Grammar(l)



# Generated at 2022-06-13 17:58:49.599638
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import shutil
    import tokenize
    from io import StringIO
    from unittest import TestCase

    from .pgen2 import driver

    class MyTestCase(TestCase):

        def get_driver(self, version: str) -> driver.Driver:
            grammar = driver.load_grammar(version)
            return driver.Driver(grammar, convert=True)

        def test_dump(self) -> None:
            driver = self.get_driver(3)
            with tempfile.TemporaryDirectory() as tmpdir:
                filename = os.path.join(tmpdir, "Grammar.pickle")
                driver.grammar.dump(filename)
                with open(filename, "rb") as f:
                    data = f.read()
                self.assertTrue(data)
                driver2 = self

# Generated at 2022-06-13 17:58:59.595989
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

# Generated at 2022-06-13 17:59:09.053594
# Unit test for method load of class Grammar
def test_Grammar_load():
    # No unit test on correct behavior of Grammar, because the class
    # is too big and complicated.  Here we test that loading a
    # complete pickle file doesn't crash.  The file is dumped by
    # ../Tools/pgen/pgen.py.

    # This is the PEP 279 parser.
    filename = "Grammar.pkl"
    try:
        with open(filename, "rb") as f:
            g = Grammar()
            g.loads(f.read())
    except FileNotFoundError:
        # Skip test if the pickle file isn't available
        pass

# Generated at 2022-06-13 17:59:12.364154
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver
    def get_pickle_name():
        from tempfile import NamedTemporaryFile
        f = NamedTemporaryFile(delete=False)
        f.close()
        return f.name
    fn = get_pickle_name()
    driver.make_pgen_grammar_pickle(fn, "graminit.txt")
    g = Grammar()
    g.load(fn)
    os.remove(fn)
    return g


# Generated at 2022-06-13 17:59:15.066021
# Unit test for method load of class Grammar
def test_Grammar_load():
    gram = Grammar()
    gram.load(b'{i}')

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:59:26.580329
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io
    g = Grammar()

# Generated at 2022-06-13 17:59:37.395134
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    import types

    fn: str = "Grammar.dump.test"
    c = Grammar()
    c.symbol2number = {}
    c.number2symbol = {}
    c.states = "states"
    c.dfas = ''
    c.labels = "labels"
    c.keywords = ''
    c.tokens = ''
    c.start = ''
    c.async_keywords = ''
    try:
        c.dump(fn)
        with open(fn, 'rb') as f:
            f_contents = f.read()
    finally:
        try:
            os.remove(fn)
        except:
            pass
    # Generated data is loaded while looking for a module called
    # Grammar.dump.test