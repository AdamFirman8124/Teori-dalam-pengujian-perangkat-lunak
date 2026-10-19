

# Generated at 2022-06-13 17:49:48.919333
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # setup test and call function
    g = Grammar()
    g.symbol2number['foo'] = 3
    g.number2symbol[3] = 'foo'
    g.states = [[]]
    g.dfas = {3: ([], {})}
    g.labels = [(0, "EMPTY")]
    g.keywords = {'foo': 2}
    g.dump('foo')

    with open('foo', 'rb') as f:
        d = pickle.load(f)
    assert d['symbol2number'] == {'foo': 3}
    assert d['number2symbol'] == {3: 'foo'}
    assert d['states'] == [[]]
    assert d['dfas'] == {3: ([], {})}

# Generated at 2022-06-13 17:49:52.601188
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest
    from io import BytesIO
    g = Grammar()
    g.tokens = {}
    with pytest.raises(TypeError):
        g.dump(BytesIO())

# Generated at 2022-06-13 17:50:00.830523
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pytest
    from . import conv, pgen

    g = Grammar()
    t = conv.parse_grammar()
    pgen.generate_parsing_tables(g, t)
    with tempfile.TemporaryFile() as f:
        g.dump(f)
        f.seek(0)
        h = Grammar()
        h.load(f)
    assert g == h

    s = g.symbol2number.copy()
    with pytest.raises(AttributeError):
        s.__delitem__('EMPTY')
    with pytest.raises(AttributeError):
        s.__setitem__('EMPTY', 999)

# Generated at 2022-06-13 17:50:11.336716
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    from . import parser

    class TestGrammar(unittest.TestCase):
        def test_load(self):
            # load grammar pickle file
            g = Grammar()
            g.load(parser.__file__.replace(".py", ".pkl"))
            self.assertTrue(
                hasattr(g, "symbol2number")
                and hasattr(g, "number2symbol")
                and hasattr(g, "dfas")
                and hasattr(g, "keywords")
                and hasattr(g, "tokens")
                and hasattr(g, "symbol2label")
                and hasattr(g, "labels")
                and hasattr(g, "states")
                and hasattr(g, "start")
            )


# Generated at 2022-06-13 17:50:21.035494
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os, pickle
    g = Grammar()
    g.symbol2number = {'and': 257, 'else': 258}
    g.number2symbol = {258: 'else', 257: 'and'}
    g.states = [[(0, 3), (0, 4)], [(0, 5), (257, 6)], [(258, 5), (0, 6)]]
    g.dfas = {257: ([[(257, 1), (0, 2)]], {1: 1}), 258: ([[(258, 1), (0, 2)]], {1: 1})}
    g.labels = [(0, 'EMPTY'), (258, None), (0, None), (257, None), (258, None), (0, None)]
    g.keywords = {'else': 258}
    g

# Generated at 2022-06-13 17:50:24.442236
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join(os.path.dirname(__file__),
                              "Python.asdl"))

if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:50:26.461870
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    There are no unit tests for load yet.
    """
    assert True

# Generated at 2022-06-13 17:50:32.969844
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test for Grammar dump and load
    filename = tempfile.mktemp()
    gram = Grammar()
    gram.symbol2number = {"a": 1}
    gram.number2symbol = {1: "a"}
    gram.dfas = {1: ([], {})}
    gram.start = 1
    gram.dump(filename)
    gram2 = Grammar()
    gram2.load(filename)
    assert gram.symbol2number == gram2.symbol2number
    assert gram.number2symbol == gram2.number2symbol
    assert gram.dfas == gram2.dfas
    assert gram.start == gram2.start
    os.unlink(filename)



# Generated at 2022-06-13 17:50:38.801033
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    filename = tempfile.mkdtemp() + "dicts.pkl"
    # FIXME: This test fails on mypyc!
    # FIXME: Grammar.__init__ has been removed by mypyc
    grammar = Grammar()
    grammar.dump(filename)

    def clean_up():
        import os
        try:
            os.unlink(filename)
        except FileNotFoundError:
            pass

    clean_up()

# Generated at 2022-06-13 17:50:43.416458
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class TestGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.foo = "bar"

    gram = TestGrammar()
    f = tempfile.NamedTemporaryFile(dir='.')
    gram.dump(f.name)
    gram_copy = TestGrammar()
    gram_copy.load(f.name)
    assert gram_copy.foo == "bar"

# Generated at 2022-06-13 17:50:54.009627
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import pgen2.grammar

    class TestCase(unittest.TestCase):

        def runTest(self):
            gr = pgen2.grammar.Grammar()
            gr.load(pgen2.grammar.__file__.replace(".pyc", ".pkl"))

    return TestCase()



# Generated at 2022-06-13 17:51:02.768891
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import py.path
    import sys
    from . import token, pgen2

    try:
        pgen2.main(["-o", "tests/data/Grammar.dump"])
    except pgen2.Error:
        if sys.flags.optimize >= 2:
            # With -OO, the file tests/data/Grammar.dump is missing:
            # it's part of the __pycache__ directory, which gets
            # removed by test.support.CleanImport.
            #
            # The test is therefore skipped because the dump function
            # doesn't run on Python with -OO.
            py.test.skip("-OO: tests/data/Grammar.dump is missing")
        raise
    g = Grammar()
    g.load("tests/data/Grammar.dump")
    assert g.sy

# Generated at 2022-06-13 17:51:12.184492
# Unit test for method load of class Grammar
def test_Grammar_load():
    class MyGrammar(Grammar):
        def loads(self, pkl):
            Grammar._update(self, pickle.loads(pkl))
    # test regular grammar
    g = MyGrammar()
    g.loads(open(os.path.join(os.path.dirname(__file__), "Grammar.pkl"), "rb").read())
    assert g.start == 394
    # test async grammar
    g = MyGrammar()
    g.loads(open(os.path.join(os.path.dirname(__file__), "Grammar-async.pkl"), "rb").read())
    assert g.start == 396

# Generated at 2022-06-13 17:51:22.338206
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Unit test for method load of class Grammar"""
    import unittest
    import os
    import tokenize
    import io

    class TestGrammar_load(unittest.TestCase):

        def test_method(self):
            file = __file__
            dir = os.path.dirname(file)
            file = os.path.join(dir, "Grammar.pickle")
            assert os.path.isfile(file), file
            assert os.access(file, os.R_OK), file
            grammar = Grammar()
            grammar.load(file)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestGrammar_load)
    unittest.TextTestRunner(verbosity=2).run(suite)



# Generated at 2022-06-13 17:51:26.894714
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = os.path.join(os.path.dirname(__file__), "Grammar.pkl")
    g = Grammar()
    g.load(filename)
    assert g.async_keywords


test_Grammar_load()

# Generated at 2022-06-13 17:51:28.517504
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    pass

# Generated at 2022-06-13 17:51:29.536438
# Unit test for method load of class Grammar
def test_Grammar_load():  # type: ignore
    pass


# Generated at 2022-06-13 17:51:30.802460
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    assert grammar.dump(b'filename') == None

# Generated at 2022-06-13 17:51:38.333644
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import shutil
    from . import pgen2
    from . import test_support

    grammar = pgen2.driver.load_grammar(
        test_support.findfile("Grammar.txt"), "Grammar.txt"
    )
    filename = tempfile.mktemp()

# Generated at 2022-06-13 17:51:40.152212
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gr = Grammar()
    pkl = gr.dump("/dev/null")
    assert pkl is None

# Generated at 2022-06-13 17:51:52.366405
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import random
    import pickle
    import tempfile

    filename = os.path.join(tempfile.gettempdir(), "test_Grammar_dump.tmp")
    if os.path.exists(filename):
        os.unlink(filename)

    g = Grammar()

    # Fill collections
    # mypyc generates objects that don't have a __dict__, but they
    # do have __getstate__ methods that will return an equivalent
    # dictionary
    if hasattr(g, "__dict__"):
        d = g.__dict__
    else:
        d = g.__getstate__()  # type: ignore

    for i in range(10):
        d[str(i)] = [str(j) for j in range(10)]

# Generated at 2022-06-13 17:51:57.240147
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    source_path = os.path.join(os.path.dirname(__file__), "Grammar.txt")
    g.load(source_path)
    assert len(g.dfas) == 0

# Generated at 2022-06-13 17:52:07.031148
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    # mypyc doesn't currently handle cyclic types well
    g = Grammar()
    g.symbol2number = {'foo': 1, 'bar': 2}
    g.number2symbol = {1: 'foo', 2: 'bar'}
    g.labels = [
        (1, None),
        (65535, 'foo'),
        (0, 'EMPTY')]

# Generated at 2022-06-13 17:52:11.878828
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    tempdir = tempfile.mkdtemp()
    try:
        filename = os.path.join(tempdir, "Grammar_dump_test")
        grammar.dump(filename)
        with open(filename, "rb") as f:
            assert f.read()
    finally:
        os.remove(filename)
        os.rmdir(tempdir)

# Generated at 2022-06-13 17:52:19.142406
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2
    from .pygram import pygram
    from .pgen2.parse import Token, PythonParser

    # Make a parser
    parser = PythonParser()

    # Create a grammar
    grammar = pgen2.driver._create_grammar(pygram, opmap)

    # Dump it
    with tempfile.NamedTemporaryFile() as f:
        grammar.dump(f.name)
        grammar.load(f.name)

    # Some sanity checks
    assert parser.grammar == grammar

    # Parse an assignment statement

# Generated at 2022-06-13 17:52:28.126097
# Unit test for method load of class Grammar
def test_Grammar_load():
    import StringIO
    g = Grammar()
    g.load("Python/Grammar.pkl")
    f = StringIO.StringIO()
    g.dump(f)
    f.seek(0)
    g2 = Grammar()
    g2.loads(f.read())
    assert g.keywords == g2.keywords
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.dfas == g2.dfas
    assert g.states == g2.states
    assert g.labels == g2.labels
    assert g.start == g2.start
    assert g.async_keywords == g2.async_keywords

# Generated at 2022-06-13 17:52:34.667865
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test that Grammar pickle files load."""
    from .pgen2 import driver

    grammar_file = os.path.join(os.path.dirname(__file__), "Grammar.txt")
    pkl_file = os.path.join(os.path.dirname(__file__), "Grammar.pkl")
    driver.generate_grammar(grammar_file, pkl_file)
    g = Grammar()
    g.load(pkl_file)
    # g.report()

# Generated at 2022-06-13 17:52:41.320352
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    import tempfile
    import unittest
    import stat

    class GrammarInit(Grammar):
        def __init__(self) -> None:
            super().__init__()
            self.symbol2number = {"foo": 257}
            self.number2symbol = {257: "foo"}
            self.states = [
                [
                    (1, 257),
                    (1, 258),
                    (1, 259),
                    (1, 260),
                    (1, 261),
                ]
            ]
            self.dfas = {257: (self.states[0], {1: 1})}
            self.labels = [(0, "EMPTY"), (1, None), (1, "foo")]
            self.keywords = {"foo": 2}

# Generated at 2022-06-13 17:52:52.650195
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Construct a simple grammar to test the dump method
    gram = Grammar()
    gram.symbol2number = {'a': 256, 'b': 257}
    gram.number2symbol = {256: 'a', 257: 'b'}
    gram.dfas = {256: ([], {3: 1, 1: 1}), 257: ([], {2: 1, 1: 1})}
    gram.symbol2label = {'NT_OFFSET': 256, 'NT_OFFSET+1': 257}
    gram.labels = [
        (1, None),
        (2, None),
        (3, None),
        (4, 'a'),
        (5, 'b'),
        (256, None),
        (257, None)
    ]

# Generated at 2022-06-13 17:53:03.770767
# Unit test for method load of class Grammar
def test_Grammar_load():
    def test_grammar(grammar: Grammar) -> None:
        assert grammar.symbol2number
        assert grammar.number2symbol
        assert grammar.states
        assert grammar.dfas
        assert grammar.labels
        assert grammar.keywords
        assert grammar.tokens
        assert grammar.symbol2label
        assert grammar.start

    pkl_file = os.path.join(os.path.dirname(__file__), "Grammar.pkl")
    test_grammar(Grammar())
    test_grammar(Grammar())
    test_grammar(Grammar())
    g = Grammar()
    g.load(pkl_file)
    test_grammar(g)
    g = Grammar()

# Generated at 2022-06-13 17:53:23.814315
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'foo': 2, 'bar': 4}
    g.number2symbol = {2: 'foo', 4: 'bar'}
    g.states = [[[(1, 2), (3, 4)], [(5, 6), (7, 8)]]]
    g.dfas = {2: ([[(1, 2), (3, 4)], [(5, 6), (7, 8)]], {1: 1, 3: 1, 5: 1, 7: 1,
                                                        8: 1}),
               4: ([[(9, 10), (6, 8)], [(11, 12), (13, 14)]], {9: 1, 11: 1, 13: 1,
                                                             14: 1})}

# Generated at 2022-06-13 17:53:31.784023
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    # The following attributes will be defined when
    # _Grammar__getstate__ is called.
    assert g.symbol2number is None
    assert g.number2symbol is None
    assert g.states is None
    assert g.dfas is None
    assert g.labels is None
    assert g.keywords is None
    assert g.tokens is None
    assert g.symbol2label is None
    assert g.start is None
    assert g.async_keywords is None
    # The following attributes will be defined when
    # Grammar.__init__ is called.
    assert g.start == 256

    # Note that once create_grammar_pickle.py has been run, we can
    # just use g.load('Grammar.pkl') here. But since

# Generated at 2022-06-13 17:53:39.519110
# Unit test for method load of class Grammar
def test_Grammar_load():
    import sys, string, random

    from .pgen2 import tokenize as tokenize_module

    # Test the loading of a concrete grammar
    grammar_file = sys.modules['__main__'].__file__
    g = Grammar()
    g.load(grammar_file)

    text = open(grammar_file).read()

    for s in string.ascii_letters + string.digits + ' \n\t':
        text = text.replace(s, ' ')

    tokens = []
    tokenize = tokenize_module.generate_tokens(iter(text).__next__)

    for t in tokenize:
        tokens.append(t)
        type = t[0]
        token = t[1]
        start = t[2]
        end = t[3]


# Generated at 2022-06-13 17:53:44.081983
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest

    class TestGrammar(unittest.TestCase):
        def test_dump(self):
            # type: () -> None
            grammar = Grammar()
            gram = tempfile.mkstemp()
            grammar.dump(gram[1])
            assert os.path.isfile(gram[1]) == True
            os.remove(gram[1])

    unittest.main()


# Generated at 2022-06-13 17:53:55.035059
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import py
    import os
    import pickle
    import shutil
    import tempfile
    dir = tempfile.mkdtemp(prefix="py3-")
    filename = os.path.join(dir, "Grammar")
    try:
        grammar = Grammar()
        grammar.start = 257
        grammar.dump(filename)
        assert os.path.exists(filename)
        with open(filename, "rb") as f:
            d = pickle.load(f)
    finally:
        shutil.rmtree(dir)
    assert d == {"start": 257, "async_keywords": False}


# Generated at 2022-06-13 17:54:07.410120
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import types
    filename = "_tmp_"

# Generated at 2022-06-13 17:54:15.381283
# Unit test for method load of class Grammar
def test_Grammar_load():

    import unittest
    import unittest.mock
    import io

    data_in: bytes = b"\x80\x03}q\x00)"

    class MockPickle:
        def loads(self, data_in: bytes) -> Dict[str, Any]:
            return {"a": 1, "b": 2, "c": 3}

    class TestGrammar(unittest.TestCase):
        def setUp(self) -> None:
            self.mock_pickle = MockPickle()
            grammar = Grammar()
            grammar.load(io.BytesIO(data_in))
            assert grammar.a == 1
            assert grammar.b == 2
            assert grammar.c == 3

    unittest.main()


if __name__ == "__main__":
    test_Grammar

# Generated at 2022-06-13 17:54:25.540839
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"symbol": 2}
    g.number2symbol = {2: "number"}
    g.states = []
    g.dfas = {}
    g.labels = [(0, "EMPTY")]
    g.keywords = {}
    g.tokens = {}
    g.symbol2label = {}
    g.start = 256
    g.async_keywords = False

    # with tempfile.NamedTemporaryFile() as f:
    #     g.dump(f.name)
    g.dump("test_Grammar_dump.pickle")

    g2 = Grammar()
    g2.load("test_Grammar_dump.pickle")

    assert g is not g2
    assert repr(g) == repr

# Generated at 2022-06-13 17:54:29.588160
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = "./python3.4-ast.pkl"
    py34 = Grammar()
    py34.load(filename)
    py35 = py34.copy()
    assert py34.start == 256
    assert py34.start == py35.start

# Generated at 2022-06-13 17:54:35.603871
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.symbol2number = {'a':1}
    grammar.number2symbol = {1: 'a'}
    grammar.states = ['a', 'b']
    grammar.dfas = {1:'1', 2:'2'}
    grammar.labels = ['a', 'b']
    grammar.keywords = {'a':1}
    grammar.tokens = {1:'a'}
    grammar.symbol2label = {'a':1}
    grammar.start = 1
    grammar.async_keywords = False
    with tempfile.NamedTemporaryFile(suffix=".pkl") as f:
        grammar.dump(f.name)
        new_grammar = Grammar()
        new_grammar.load(f.name)

# Generated at 2022-06-13 17:55:03.870726
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def check(x):
        pass
    filename = ""
    g = Grammar()
    g.dump(filename)


# Generated at 2022-06-13 17:55:13.221848
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    from io import BytesIO
    with tempfile.TemporaryFile() as f:
        g = Grammar()
        g.dump(f)
        f.seek(0)
        d = pickle.load(f)
    f2 = BytesIO()
    pickle.dump(d, f2, pickle.HIGHEST_PROTOCOL)
    g.loads(f2.getvalue())
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert g.keywords == {}
    assert g.tokens == {}
    assert g.symbol2label == {}
    assert g.states == []
    assert g.dfas == {}
    assert g.labels == [(0, "EMPTY")]
    assert g.start == 256
   

# Generated at 2022-06-13 17:55:22.301697
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = dict(a=1, b=2, c=3)
    g.number2symbol = dict(zip(g.symbol2number.values(), g.symbol2number.keys()))
    g.states = [[["a", "b"], ["a", "c"]], [["b", "b"], ["a", "c"]]]
    g.dfas = dict(z=("a", "b"))
    g.labels = [("a", "b"), ("a", "b")]
    g.keywords = dict(a="b")
    g.tokens = dict(a="b")
    g.symbol2label = dict(a="b")
    g.start = 256
    g.async_keywords = False

# Generated at 2022-06-13 17:55:27.467954
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    from unittest.mock import Mock, patch

    mock_open = Mock()
    with patch("pickle.dump", mock_open):
        g = Grammar()
        g.dump("test")
        assert mock_open.called_with(g, mock_open.return_value, pickle.HIGHEST_PROTOCOL)


# Generated at 2022-06-13 17:55:37.160712
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import logging

    # Log and handle exceptions
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())
    try:
        fname = sys._getframe().f_code.co_name
        filename = os.path.join(os.path.join(os.path.dirname(__file__), fname + ".pyg"))
        if os.path.isfile(filename):
            os.unlink(filename)
            logger.debug("Removing %s", filename)
        gram = Grammar()
        gram.dump(filename)
        logger.debug("Dumping %s", gram)
    except:
        logger.exception("Cannot dump grammar")


# Generated at 2022-06-13 17:55:38.237408
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    path = "/tmp/python3-grammar.dump"
    gram = Grammar()
    gram.dump(path)

# Generated at 2022-06-13 17:55:48.545433
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    import tempfile
    import shutil

    class TestGrammar(unittest.TestCase):
        def setUp(self):
            self.dir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.dir)


# Generated at 2022-06-13 17:55:58.032956
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import unittest
    import pickle as _pickle
    from pyflakes.checker import Checker


# Generated at 2022-06-13 17:56:02.485379
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def _test(load_grammar_from_file: bool, load_grammar_from_generator: bool):
        grammar = Grammar()
        if load_grammar_from_file:
            py_grammar = Grammar()
            py_grammar_file = os.path.join(
                os.path.dirname(__file__), "Grammar.txt"
            )
            py_grammar.load(py_grammar_file)
            grammar.copy_from(py_grammar)
        elif load_grammar_from_generator:
            from .pgen2 import driver

            grammar = driver.pgen()
        assert grammar
        with tempfile.NamedTemporaryFile() as f:
            grammar.dump(f.name)
            f.file.seek(0)

# Generated at 2022-06-13 17:56:04.556378
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("test1.pickle")


# Generated at 2022-06-13 17:56:28.380965
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'foo': 42}
    g.number2symbol = {42: 'foo'}
    g.states = [[(1, 2), (3, 4)], [(5, 6)], [(7, 8)]]
    g.dfas = {42: ([[(1, 2), (3, 4)], [(5, 6)], [(7, 8)]], {42: 1})}
    g.labels = [(0, 'EMPTY'), (1, None), (2, None), (3, 'keyword')]
    g.keywords = {'keyword': 3}
    g.tokens = {1: 2, 3: 3}
    g.symbol2label = {'bar': 4}
    g.start = 256

# Generated at 2022-06-13 17:56:32.517865
# Unit test for method load of class Grammar
def test_Grammar_load():
    gram = Grammar()

    with open("Grammar.pkl", "rb") as f:
        gram.loads(f.read())
    assert gram.symbol2number['atom'] == 257
    assert gram.number2symbol[257] == 'atom'
    assert gram.states == []
    assert gram.dfas == {}
    assert gram.labels == [(0, 'EMPTY')]
    assert gram.keywords == {}
    assert gram.tokens == {}
    assert gram.symbol2label == {}
    assert gram.start == 256

# Generated at 2022-06-13 17:56:41.928277
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import conv
    from . import tokenize
    from .parse import Parser

    parser = Parser()
    g_pkl = conv.generate_pkl()
    parser.grammar.load(g_pkl)

    # Create a list of all the symbols in the grammar
    symbols = set(parser.grammar.symbol2number.keys())

    # Create a list of all the tokens in the grammar's token list
    token_numbers = set(parser.grammar.tokens.keys())
    tokens = {tok_name for tok_name, _, _, _ in tokenize.tok_name}

    # Verify all the tokens are in the grammar
    assert token_numbers <= tokens

    # Create a list of all the keywords in the grammar's keyword list

# Generated at 2022-06-13 17:56:45.309374
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    test_Grammar_dump
    """
    grammar = Grammar()
    grammar.dump("name")

if __name__ == "__main__":
    header = "Testing Grammar class method dump"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    test_Grammar_dump()

# Generated at 2022-06-13 17:56:55.475667
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.loads(b'\x80\x04\x95\x9d\x00\x00\x00\x00\x00\x00\x00(\x8c\x14symbol2number\x94}\x8c\x18number2symbol\x94}\x8c\x06states\x94\x8c\x0bconcatenate\x94\x93\x94.]\x94\x8c\x0cdfas\x94\x8c\x07labels\x94]\x94\x8c\x05start\x94K\x00ub.')
    assert g.symbol2number == {'concatenate': 256}
    assert g.number2symbol == {256: 'concatenate'}


# Generated at 2022-06-13 17:57:03.058513
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'A': 257}
    g.number2symbol = {257: 'A'}
    g.states = [[(0, 257)]]
    g.dfas = {257: ([[(0, 257)]], {257: 1})}
    g.labels = [(0, "EMPTY"), (257, 'A')]
    g.keywords = {}
    g.tokens = {}
    g.symbol2label = {'A': 257}
    g.start = 257
    g.async_keywords = False
    temp_file = tempfile.NamedTemporaryFile()
    g.dump(temp_file.name)
    g.load(temp_file.name)
    assert g.start == 257
    # delete temporary file


# Generated at 2022-06-13 17:57:17.191497
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Unit test for method Grammar.dump"""
    import unittest

    import pickle

    class GrammarTestCase(unittest.TestCase):
        def setUp(self):
            # only the attributes we are interested in
            self.test = Grammar()
            self.test.symbol2number = {"TEST_SYMBOL2NUMBER": 1}
            self.test.number2symbol = {1: "TEST_NUMBER2SYMBOL"}
            self.test.states = ["TEST_STATES"]
            self.test.dfas = {"TEST_DFAS": (["TEST_DFAS_DFA"], {"TEST_DFAS_FIRST": 1})}

# Generated at 2022-06-13 17:57:25.485684
# Unit test for method load of class Grammar
def test_Grammar_load():
    class TestGrammar(Grammar):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)

    grammar = TestGrammar()
    grammar.load(__file__.replace(".py", ".pkl"))
    assert grammar.symbol2number == {
        "CLASSDEF": 258,
        "ERROR_DEDENT": 261,
        "NAME": 257,
        "NEWLINE": 259,
        "STMT": 260,
    }
    assert grammar.number2symbol == {
        258: "CLASSDEF",
        259: "NEWLINE",
        257: "NAME",
        260: "STMT",
        261: "ERROR_DEDENT",
    }

# Generated at 2022-06-13 17:57:35.901046
# Unit test for method load of class Grammar
def test_Grammar_load():
    test_grammar = Grammar()
    test_grammar.load("Lib/test/pgen_test/test_grammar")

# Generated at 2022-06-13 17:57:38.108186
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("test.pkl")


# Generated at 2022-06-13 17:57:54.571849
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    assert os.path.isfile(get_pkl_path())


# Generated at 2022-06-13 17:57:59.558558
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2.pgen
    from pgen2.conv import convert

    if not hasattr(pgen2.pgen, "generate_grammar"):
        return  # Python 3.8+

    for ver in ("2.7", "3.8"):
        grammar = convert(pgen2.pgen.generate_grammar(ver))
        grammar.dump(ver + ".pickle")
        grammar2 = Grammar()
        grammar2.load(ver + ".pickle")
        assert grammar.labels == grammar2.labels
        assert grammar.states == grammar2.states
        assert grammar.keywords == grammar2.keywords
        assert grammar.symbol2label == grammar2.symbol2label
        assert grammar.symbol2number == grammar2.symbol2number
        assert grammar.number2sy

# Generated at 2022-06-13 17:58:08.984336
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import grammar
    from . import symbols
    from . import token

    # Define x for using it in the assertion
    x = token.NAME

    # Test all exceptions raised by the method
    try:
        # Test with invalid file path
        grammar.dump('abc.pkl')
    except OSError:
        pass

    try:
        # Test with invalid file path (dir does not exist)
        grammar.dump('/dir1/dir2/grammar.pkl')
    except OSError:
        pass

    try:
        # Test with invalid file path (dir is not writable)
        grammar.dump('/usr/bin/grammar.pkl')
    except OSError:
        pass

    # Test with valid file
    grammar.dump('/tmp/grammar.pkl')

   

# Generated at 2022-06-13 17:58:18.289286
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

    g.symbol2number = {
        "foo": 1,
        "bar": 2,
    }

    g.number2symbol = {
        1: "foo",
        2: "bar",
    }

    g.states = [
        [
            [(0, "EMPTY"), (1, 1)],
            [(2, 2)],
            [(3, 3)],
        ]
    ]

    g.dfas = {
        3: (
            [
                [(4, 5)],
                [(6, 7)],
                [(8, 9)],
            ],
            {
                3: 42,
                5: 123,
            },
        )
    }


# Generated at 2022-06-13 17:58:21.501606
# Unit test for method load of class Grammar
def test_Grammar_load():
    import os
    import pickle

    path = os.path.join("python", "Grammar.pickle")
    if os.path.exists(path):
        with open(path, "rb") as f:
            d = pickle.load(f)
        Grammar()._update(d)

# Generated at 2022-06-13 17:58:23.541449
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump(__file__[:-3] + '_dump_test.pickle')

if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:58:27.464779
# Unit test for method load of class Grammar
def test_Grammar_load():
    class FakeClass(object):
        def __getstate__(self) -> Any:
            return ("a", "b")
    class_ = FakeClass()
    grammar = Grammar()
    class_.__setstate__ = grammar.loads
    unpickler = pickle.Unpickler(BytesIO(b"\x80\x02C\x01\x831\x02\x832\x03."))
    unpickler.load()


del opmap_raw

# Generated at 2022-06-13 17:58:33.661126
# Unit test for method dump of class Grammar

# Generated at 2022-06-13 17:58:35.366263
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump(tempfile.mktemp())


# Generated at 2022-06-13 17:58:39.470764
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    assert g.start == 257
    assert g.symbol2number["comp_op"] == 268
    assert g.number2symbol[268] == "comp_op"
    assert g.labels[3][1] == "comp_op"
    assert g.keywords["True"] == 11
    assert g.tokens[51] == 11


del opmap_raw, token

# Generated at 2022-06-13 17:59:04.765064
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import conv
    import pickle
    import tempfile
    import unittest
    from pprint import pprint
    from . import token

    class TestGrammar(unittest.TestCase):
        def setUp(self):
            self.gr = conv.Grammar()
            self.gr.dump("Grammar.dump")

        def tearDown(self):
            os.remove("Grammar.dump")

        def test_Grammar_load(self):
            gr2 = conv.Grammar()
            gr2.load("Grammar.dump")
            self.assertEqual(self.gr.symbol2number, gr2.symbol2number)
            self.assertEqual(self.gr.number2symbol, gr2.number2symbol)

# Generated at 2022-06-13 17:59:12.591196
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import pickle

    class TestCase(unittest.TestCase):
        def test_load(self):
            from . import driver
            from . import parser

            with open(driver.find_grammar("Python.asdl"), "rb") as f:
                pkl = pickle.load(f)

            g = parser.Grammar()
            g.loads(pkl)
            self.assertEqual(g.start, 256)

    unittest.main(module="parserlib_test", defaultTest="TestCase.test_load")

# Generated at 2022-06-13 17:59:14.389603
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("/tmp/parsetab.pickle")


# Generated at 2022-06-13 17:59:26.117100
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Method load of class Grammar should set attributes:
    #     symbol2number, number2symbol, states, dfas, labels, start, keywords, tokens
    # There is no method in class Grammar to check this.

    class TestGrammar(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.symbol2number = {'a': 256}
            self.number2symbol = {256: 'a'}
            self.states = [
                [[(0, 2)], [(48, 1), (0, 2)], [(48, 0), (0, 2)]]
            ]

# Generated at 2022-06-13 17:59:36.956719
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import ast
    import os

    def copy_grammar(grammar: Grammar, target_async_keywords: bool) -> Grammar:
        new_grammar = grammar.copy()
        new_grammar.async_keywords = target_async_keywords
        return new_grammar

    def compare_grammars(g1: Grammar, g2: Grammar) -> None:
        for dict_attr in (
            "symbol2number",
            "number2symbol",
            "dfas",
            "keywords",
            "tokens",
            "symbol2label",
        ):
            dict1 = getattr(g1, dict_attr).copy()
            dict2 = getattr(g2, dict_attr).copy()
            dict1.pop("")
            dict2.pop