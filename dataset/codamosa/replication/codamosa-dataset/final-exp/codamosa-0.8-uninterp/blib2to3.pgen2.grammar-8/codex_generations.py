

# Generated at 2022-06-13 17:49:53.205086
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load("Grammar")


if __name__ == "__main__":
    import unittest

    unittest.main()

# Generated at 2022-06-13 17:50:02.732493
# Unit test for method load of class Grammar
def test_Grammar_load():
    def _test(g):
        # Python 3.7+ parses async as a keyword, not an identifier
        assert g.async_keywords

        assert g.symbol2number["single_input"] == 257
        assert g.symbol2number["file_input"] == 268
        assert g.symbol2number["stmt"] == 269
        assert g.symbol2number["compound_stmt"] == 278
        assert g.symbol2number["if_stmt"] == 279

        assert g.number2symbol[257] == "single_input"
        assert g.number2symbol[268] == "file_input"
        assert g.number2symbol[269] == "stmt"
        assert g.number2symbol[278] == "compound_stmt"
        assert g.number2symbol

# Generated at 2022-06-13 17:50:15.970754
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver
    # Test that a Grammar object can be created by parsing a py file, pickling
    # the object, reloading it and pickling the object again.
    g1 = driver.load_grammar("lib2to3/Grammar.txt")
    _, g2_file = tempfile.mkstemp()

# Generated at 2022-06-13 17:50:22.754047
# Unit test for method load of class Grammar
def test_Grammar_load():
    expected = Grammar()
    expected.load("Grammar.txt")
    actual = Grammar()
    actual.load("Grammar.txt")
    assert expected.symbol2number == actual.symbol2number
    assert expected.number2symbol == actual.number2symbol
    assert expected.states == actual.states
    assert expected.dfas == actual.dfas
    assert expected.labels == actual.labels
    assert expected.keywords == actual.keywords
    assert expected.tokens == actual.tokens
    assert expected.symbol2label == actual.symbol2label
    assert expected.start == actual.start
    assert expected.async_keywords == actual.async_keywords

# Generated at 2022-06-13 17:50:24.099395
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    assert g.dump(__file__) is None

# Generated at 2022-06-13 17:50:26.297799
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr: Grammar = Grammar()
    gr.load("Grammar.pkl")


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:50:34.198510
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Demonstrate ability of the Grammar class to load a pickle file that it
    # created itself.  Also, the pickle file provides a test case for this
    # function.
    import sys
    import types

    if sys.version_info >= (3, 8):
        stdlib_dir = "lib-38"
    elif sys.version_info[:2] > (3, 7):
        stdlib_dir = "lib-37"
    elif sys.version_info[:2] > (3, 6):
        stdlib_dir = "lib-36"
    elif sys.version_info[:2] > (3, 5):
        stdlib_dir = "lib-35"
    else:
        stdlib_dir = "lib"

    dirname = os.path.dirname(__file__)

# Generated at 2022-06-13 17:50:43.049486
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import get_grammar
    from .pgen2 import token

    a1 = Grammar()
    a1.symbol2number = {'a': 257, 'b': 258}
    a1.number2symbol = {257: 'a', 258: 'b'}
    a1.states = [[[(1, 2)], [(None, 257), (None, 258), (None, 0)], [(None, 257), (None, 258), (None, 0)]]]

# Generated at 2022-06-13 17:50:52.504703
# Unit test for method load of class Grammar
def test_Grammar_load():

    def mock_open(name, *args, **kwargs):
        return BytesIO(pkl)

    def mock_os_replace(src, dest):
        pass

    with ExitStack() as stack:
        stack.enter_context(patch("os.path.dirname", return_value=""))
        stack.enter_context(patch("tempfile.NamedTemporaryFile", side_effect=mock_open))
        stack.enter_context(patch("os.replace", new=mock_os_replace))

        g = Grammar()
        g.load("foo")

    assert g.symbol2number == {"foo": 42}

# Generated at 2022-06-13 17:51:01.592684
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"a": 1}
    g.number2symbol = {1: "a"}
    g.states = [1, 2]
    g.dfas = {1: (2, 3), 2: (3, 5)}
    g.labels = ["a", "b"]
    g.keywords = {"a": 1, "b": 2}
    g.tokens = {"c": 1, "d": 2}
    g.start = 1

    with tempfile.TemporaryDirectory() as td:
        fname = os.path.join(td, "test")
        g.dump(fname)

        n = Grammar()
        n.load(fname)

    assert n.symbol2number == g.symbol2number
    assert n.number

# Generated at 2022-06-13 17:51:07.686958
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.dump(filename = "tests/unittest_Grammar_dump.pickle")

    with open("tests/unittest_Grammar_dump.pickle", "rb") as f:
        d = pickle.load(f)
    assert not d



# Generated at 2022-06-13 17:51:09.881436
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    assert g.states == []
    g.dump("tmp_grammar.py")
    assert os.path.exists("tmp_grammar.py")
    os.remove("tmp_grammar.py")


# Generated at 2022-06-13 17:51:19.130748
# Unit test for method load of class Grammar
def test_Grammar_load():
    name = "Grammar.load(self, filename: Path) -> None"
    p = Grammar()
    try:
        p.load(__file__)
        raise Exception("load() should not work on non-pickle files")
    except pickle.UnpicklingError:
        pass
    p.symbol2number = {"a": 1}
    p.dump(__file__ + ".pickle")
    q = Grammar()
    q.load(__file__ + ".pickle")
    assert q.symbol2number == p.symbol2number
    os.remove(__file__ + ".pickle")

# Generated at 2022-06-13 17:51:20.513632
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert Grammar().load("../pgen/Grammar.txt") == None

# Generated at 2022-06-13 17:51:23.680699
# Unit test for method load of class Grammar
def test_Grammar_load():
    sym = "sym"
    sym_num = 257
    gram = Grammar()
    gram.symbol2number = {sym: sym_num}
    pkl = pickle.dumps(gram)
    assert pickle.loads(pkl).symbol2number == gram.symbol2number

# Generated at 2022-06-13 17:51:29.810698
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest.mock

    f = unittest.mock.Mock()
    f.name = os.path.join(os.path.dirname(__file__), "tmp.pkl")
    try:
        g = Grammar()
        g.dump(f)
        g.load(f)
    finally:
        try:
            os.unlink(f.name)
        except OSError:
            pass

# Generated at 2022-06-13 17:51:38.889884
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Create a test grammar and pickle it.
    gram_in = Grammar()
    gram_in.symbol2number = {"foo": 256, "bar": 257}
    gram_in.number2symbol = {256: "foo", 257: "bar"}
    gram_in.states = [[[(0, 1)], [(1, 1), (2, 99)]]]
    gram_in.dfas = {257: (gram_in.states[0], {256: 1})}
    gram_in.labels = [(0, "EMPTY"), (1, None), (257, "bar")]
    gram_in.keywords = {"bar": 2}
    gram_in.tokens = {1: 1}
    gram_in.symbol2label = {"bar": 2}

# Generated at 2022-06-13 17:51:48.084020
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import parse_grammar

    g = Grammar()
    parse_grammar(g, "Grammar.txt", "Grammar.pickle")

    # Test unloading
    g2 = Grammar()
    g2.load(g.dump(tempfile.mktemp()))
    assert g.start == g2.start
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert len(g.states) == len(g2.states) == 5
    assert g.dfas == g2.dfas


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:51:58.181545
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .parse import Parser
    from .pgen2 import driver

    # Ensure consistent grammar tables
    import random

    random.seed(1)

    # This test is not robust against changes to the number of states
    # in the grammar.  For example, adding a statement to the grammar
    # can result in eg. a state 368 in the generated file, but only
    # state 367 during the test.

# Generated at 2022-06-13 17:52:07.559334
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle

    fname = "/path/to/python.grammar.pickle"
    with open(fname, "rb") as f:
        data = pickle.load(f)

    grammar = Grammar()
    grammar._update(data)

    grammar_data = grammar.__getstate__()
    assert data == grammar_data

    fname2 = os.path.join(tempfile.mkdtemp(), "python.grammar.pickle")
    grammar.dump(fname2)

    with open(fname2, "rb") as f:
        data2 = pickle.load(f)

    assert data == data2
    os.remove(fname2)
    os.rmdir(os.path.dirname(fname2))

# Generated at 2022-06-13 17:52:18.042565
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import re

    g = Grammar()
    g.symbol2number = {"a": 1, "b": 2, "c": 3}
    g.states = [[((1, "a"), 1), ((2, None), 2), ((0, 3), 3)], []]
    g.labels = [(0, "EMPTY"), (1, "a"), (2, None)]
    td = tempfile.TemporaryDirectory()
    g.dump(os.path.join(td.name, "file"))
    with open(os.path.join(td.name, "file"), "rb") as f:
        pkl = f.read()

# Generated at 2022-06-13 17:52:24.256976
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickle
    from io import BytesIO

    def pickle_grammar(g):
        output = BytesIO()
        pickle.dump(g, output)
        return output.getvalue()

    g1 = Grammar()
    g1.symbol2number["test"] = 1
    g2 = Grammar()
    g2.loads(pickle_grammar(g1))
    assert g2.symbol2number["test"] == 1

# Generated at 2022-06-13 17:52:27.229481
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(__file__.replace(".py", ".pkl"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 17:52:32.678192
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Create a temporary empty file
    import tempfile
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.close()
    # Create an empty Grammar object and pickle it to the temporary file
    g = Grammar()
    g.dump(tmp_file.name)
    # Load the pickled Grammar object from the temporary file
    g = Grammar()
    g.load(tmp_file.name)
    # Delete the temporary file
    os.remove(tmp_file.name)


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:52:38.006599
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest.mock
    g = Grammar()
    g.dump("test_Grammar_dump.pkl")
    assert os.path.exists("test_Grammar_dump.pkl")
    os.remove("test_Grammar_dump.pkl")
    with unittest.mock.patch('pickle.dump') as mock_dump:
        g.dump("")
        assert mock_dump.call_count == 1


# Generated at 2022-06-13 17:52:40.896104
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io
    from .parse import test_Grammar_load
    g = Grammar()
    g.loads(io.BytesIO(test_Grammar_load).read())

# Generated at 2022-06-13 17:52:52.289676
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test for Grammar.dump
    # 1. create a grammar object
    grammar = Grammar()
    grammar.number2symbol = {256: "file_input"}
    grammar.symbol2number = {"file_input": 256}
    grammar.dfas = {256: ([[(513, 1), (256, 0)], [(1, 2), (0, 1)]], {0: 1})}
    grammar.start = 256
    grammar.keywords = {"from": 258}
    grammar.tokens = {257: 257, 258: 258}
    grammar.symbol2label = {"file_input": 256, "NAME": 1, "from": 258}
    grammar.labels = [(0, "EMPTY"), (256, None), (258, "from")]

# Generated at 2022-06-13 17:52:55.118820
# Unit test for method load of class Grammar
def test_Grammar_load():
    top_grammar = Grammar()
    top_grammar.load(os.environ.get("GRAMMAR_PICKLE"))



# Generated at 2022-06-13 17:53:02.482274
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import StringIO

    # StringIO can be a context manager in Python 2 and 3
    if hasattr(StringIO.StringIO, "__enter__"):
        output = StringIO.StringIO()
    else:
        output = io.BytesIO()
    assert isinstance(output, io.IOBase)

    d = Grammar()
    d.dump(output)
    data = output.getvalue()
    del d
    d = Grammar()
    d.loads(data)

# Generated at 2022-06-13 17:53:04.458054
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar_obj = Grammar()
    grammar_obj.load('Parser/Grammar.txt')
    assert grammar_obj is not None

# Generated at 2022-06-13 17:53:10.786036
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load('Grammar.pickle')


# Generated at 2022-06-13 17:53:17.087588
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Check that loading a grammar file and writing it immediately to another
    file yields an identical copy.
    """
    gfilename = os.path.join(os.path.dirname(__file__), "Grammar.txt")
    with open(gfilename, "rb") as f:
        g = pickle.load(f)

    with tempfile.NamedTemporaryFile() as f:
        g.dump(f.name)
        f.flush()
        with open(f.name, "rb") as gf:
            h = pickle.load(gf)

        assert g.symbol2number == h.symbol2number
        assert g.number2symbol == h.number2symbol
        assert g.states == h.states
        assert g.dfas == h.dfas

# Generated at 2022-06-13 17:53:25.854368
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.number2symbol = {}
    g.symbol2number = {}
    g.states = []
    g.dfas = {}
    g.labels = []
    g.keywords = {}
    g.tokens = {}
    with tempfile.TemporaryFile(mode="wb") as f:
        g.dump(f)
        f.seek(0)
        g2 = Grammar()
        g2.loads(f.read())
    assert g == g2

if __name__ == "__main__":
    import sys

    g = Grammar()
    g.load(sys.argv[1])
    g.report()

# Generated at 2022-06-13 17:53:32.848011
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import tokenize

    g = Grammar()
    g.load("Grammar.pickle")
    g.start = g.symbol2number["file_input"]
    tok = tokenize.generate_tokens(iter(["pass"]).__next__)
    try:
        next(tok)  # remove the encoding token
    except AttributeError:
        pass  # Python 3.7 doesn't have an encoding token
    r = parse.parse(g, tok)
    assert r is None, "Grammar.load() failed"

# For convenience and backwards compatibility.
from . import parse  # type: ignore


__all__ = ["Grammar", "Label", "parse"]

# Generated at 2022-06-13 17:53:33.389458
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    assert Grammar().dump

# Generated at 2022-06-13 17:53:40.142077
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pytest
    import sys
    class _Grammar(Grammar):
        def __init__(self, d: Dict[str,Any]) -> None:

            # Call super class __init__()
            super().__init__()

            # Load the attributes from the string representation
            self._update(d)

    with pytest.raises(FileNotFoundError):
        g = _Grammar({})
        g.load("/this/file/name/definitely/does/not/exist")

    g = _Grammar({})
    filename = __file__
    g.load(filename)
    assert g.symbol2number == {'string': 258, 'STRING': 257}

# Generated at 2022-06-13 17:53:41.018934
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.txt")

# Generated at 2022-06-13 17:53:41.852519
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    assert True

# Generated at 2022-06-13 17:53:53.183718
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickletools
    import sys
    import unittest
    import tempfile

    simple_grammar = '''
    symbol2number = {'a': 0, 'b': 1}
    number2symbol = {0: 'a', 1: 'b'}
    states = [[[(0, 1)]]]
    dfas = {2: ([[[(0, 1)]]], {0: 1}), 3: ([[[(0, 1)]]], {0: 1})}
    labels = [(0, None)]
    start = 2
    '''
    attrs = {}
    for line in simple_grammar.split('\n'):
        line = line.strip()
        if line:
            key, val = line.split('=')
            key = key.strip()
            val = eval(val)

# Generated at 2022-06-13 17:53:55.921173
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest
    grammar = Grammar()
    with pytest.raises(AttributeError):
        grammar.dump("")


# Generated at 2022-06-13 17:54:11.302666
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import conv
    from .pgen import driver
    from .parse import Parser

    filename = "Grammar.pickle"
    p = Parser()
    p.load_grammar()
    g = p.grammar

    g.dump(filename)

    g2 = Grammar()
    g2.load(filename)
    assert g2.symbol2number == g.symbol2number
    assert g2.number2symbol == g.number2symbol
    assert g2.dfas == g.dfas
    assert g2.keywords == g.keywords
    assert g2.tokens == g.tokens
    assert g2.labels == g.labels
    assert g2.states == g.states
    assert g2.start == g.start

    # Regression test

# Generated at 2022-06-13 17:54:21.140813
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    import parse

    class TestGrammarDump(unittest.TestCase):
        def test_dump(self):
            filename = (
                "Python-3.7.5/Lib/test/badsyntax_3177.py"
            )
            with self.assertRaises(tokenize.TokenError) as context:
                parse.suite(open(filename).readline)
            self.assertEqual(
                context.exception.args[0],
                "EOF in multi-line statement",
            )
            grammar = parse.Parser(parse.gr).grammar
            grammar.dump("pickle_grammar")
            file = open("pickle_grammar", "rb")
            pickle_grammar = pickle.load(file)

# Generated at 2022-06-13 17:54:30.512297
# Unit test for method load of class Grammar
def test_Grammar_load():
    import inspect
    import pkgutil
    import unittest

    class GrammarTest(unittest.TestCase):
        """Test load() method of Grammar."""

        def test_load(self):
            for _, module_name, _ in pkgutil.walk_packages(
                os.path.dirname(os.path.abspath(inspect.getfile(Grammar)))
            ):
                if not module_name.startswith("_"):
                    module = __import__(module_name)
                    if hasattr(module, "load_grammar"):
                        module.load_grammar(self.assertTrue)

    unittest.main()

# Generated at 2022-06-13 17:54:31.597080
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.dump("")

# Generated at 2022-06-13 17:54:33.141318
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr = Grammar()
    gr.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))

# Generated at 2022-06-13 17:54:43.432809
# Unit test for method load of class Grammar
def test_Grammar_load():
    import shutil
    import tempfile
    import sys

    gr = Grammar()
    gr.symbol2number = {'UNKNOWN': 256, 'ENDMARKER': 257}
    gr.number2symbol = {256: 'UNKNOWN', 257: 'ENDMARKER'}
    gr.states = [[(257, 1)]]
    gr.dfas = {256: ([[(0, 0)]], {257: 0})}
    gr.labels = [(0, None), (257, None)]
    gr.keywords = {}
    gr.tokens = {257: 1}
    gr.symbol2label = {}

    # save the grammar

# Generated at 2022-06-13 17:54:49.738977
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class myGrammar(Grammar): pass

    ng = myGrammar()
    ng.dump("/does/not/exist")
    ng.load("/does/not/exist")
    ng.loads(b'\x80\x03c__main__\nmyGrammar\nq\x00)\x81q\x01.')
    ng.report()
    ni = ng.copy()
test_Grammar_dump()

# Generated at 2022-06-13 17:54:55.074366
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os.path
    import tempfile
    import shutil

    root_tmp_dir = tempfile.mkdtemp()
    try:
        grammar_dump_filename = os.path.join(root_tmp_dir, "grammar_dump.pkl")

        grammar = Grammar()
        grammar.dump(grammar_dump_filename)
        grammar.load(grammar_dump_filename)

        assert grammar
    finally:
        shutil.rmtree(root_tmp_dir)

# Generated at 2022-06-13 17:54:56.604511
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    print(f"grammar={grammar}")
    assert False  # TODO: implement your test here


# Generated at 2022-06-13 17:54:58.948234
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Ensure Grammar.load() is valid.
    """
    gram = Grammar()
    gram.load("Grammar.pkl")



# Generated at 2022-06-13 17:55:12.416578
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Create a grammar instance; initialized with None
    g = Grammar()
    g.number2symbol = {1: "foo", 2: "bar"}
    g.symbol2number = {"foo": 1, "bar": 2}
    g.states = [[(1, 2), (3, 4), (5, 6)]]
    g.dfas = {1: (1, {1: 1}), 2: (2, {2: 2})}
    g.labels = [(1, None), (2, "foo")]
    g.keywords = {"foo": 2}
    g.tokens = {3: 1, 4: 2}
    g.symbol2label = {"bar": 3}
    g.start = 256

    # Dump the grammar to a file

# Generated at 2022-06-13 17:55:21.653504
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    a = Grammar()
    a.load(__file__.replace(".py", ".pkl"))
    a.dump(__file__.replace(".py", ".pickle"))
    with open(__file__.replace(".py", ".pickle"), "rb") as f:
        d = pickle.load(f)
        assert d["symbol2number"] == {"single_input": 257, "file_input": 258}
        assert d["number2symbol"] == {257: "single_input", 258: "file_input"}

# Generated at 2022-06-13 17:55:30.557643
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Verify that when Grammar.load is called that it has the correct attributes
    grammar = Grammar()
    grammar.load('./mypy/mypy/pgen2/grammar.pkl')

# Generated at 2022-06-13 17:55:39.181496
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()

# Generated at 2022-06-13 17:55:40.515517
# Unit test for method load of class Grammar
def test_Grammar_load():
    _Grammar_load()


# Generated at 2022-06-13 17:55:50.209835
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:55:53.685565
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load('Python/Grammar.pkl')
    assert g.start == 257
    assert g.number2symbol[257] == 'file_input'

# Generated at 2022-06-13 17:55:55.592222
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.pickle")
    g.report()


del opmap_raw

# Generated at 2022-06-13 17:56:00.199953
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import tokenize

    fol = tokenize.generate_grammar()
    grammar = Grammar()
    grammar.load(fol)

    # Test attributes
    assert len(grammar.symbol2number) > 0
    assert len(grammar.number2symbol) > 0
    assert len(grammar.states) > 0
    assert len(grammar.dfas) > 0
    assert len(grammar.labels) > 0
    assert isinstance(grammar.start, int)
    assert isinstance(grammar.keywords, dict)
    assert isinstance(grammar.tokens, dict)

    # expect exception
    with tempfile.TemporaryFile() as f:
        grammar.load(f.__enter__().name)



# Generated at 2022-06-13 17:56:12.321773
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    try:
        import StringIO
    except ImportError:  # pragma: no cover
        import io as StringIO

    def _test_attributes(self, d):
        self._update(d)
        self.dump(stream)

    Grammar._test_attributes = _test_attributes

    stream = StringIO.StringIO()
    g = Grammar()

    g.symbol2number = {"a": 256, "b": 257}
    g.number2symbol = {256: "a", 257: "b"}
    g.dfas = {
        256: ([[(257, 1), (257, 0)]], {0: 1}),
        257: ([[(257, 2), (257, 0)]], {0: 1}),
    }
    g.keywords = {"a": 257}
   

# Generated at 2022-06-13 17:56:28.119818
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import os
    import pickle
    from typing import Dict
    from . import pgen2

    class TestGrammar(unittest.TestCase):
        def setUp(self) -> None:
            self.grammar = pgen2.driver.load_grammar("Grammar/Grammar")

        def assert_grammar(self, grammar: Grammar) -> None:
            def get_state(state: DFA, label: int) -> int:
                for lbl, state in state:
                    if lbl == label:
                        return state
                return -1

            # n2s
            self.assertEqual(
                grammar.number2symbol[grammar.start], "file_input"
            )

            # s2n

# Generated at 2022-06-13 17:56:31.922358
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("_test_Grammar_dump.pkl")


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:56:36.644075
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2
    import parse

    f = tempfile.NamedTemporaryFile(suffix='.pickle')
    fname = f.name

    # NOTE: how do we make sure that f is actually closed?
    g = pgen2.pgen(fname, False)
    g.parse_grammar()
    f = parse.CompilingParser(g, False)

# Generated at 2022-06-13 17:56:44.706584
# Unit test for method load of class Grammar
def test_Grammar_load():
    import sys
    import unittest

    try:
        import pytest
    except ImportError:
        pytest = None

    from . import pgen2

    class LoaderTestCase(unittest.TestCase):
        """Test loading grammar pickle files."""

        def setUp(self):
            self.loader = pgen2.pgen.Loader(pgen2.grammar)

        def test_load(self):
            """Test load method of the grammar pickle file."""
            if pytest:
                with pytest.raises(ImportError):
                    self.loader.load_grammar()
            else:
                self.assertRaises(ImportError, self.loader.load_grammar)

    unittest.main(exit=False)



# Generated at 2022-06-13 17:56:52.538562
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver

    p = driver.Pgen()

    # This will fail if the grammar is not installed
    g = p.load_grammar()

    # This will fail if the original grammar object is changed
    assert isinstance(g, Grammar)

if __name__ == "__main__":
    p = driver.Pgen()
    p.main()
    # args = sys.argv[1:]
    # if not args:
    #     args = [tokenize.detect_encoding(sys.stdin.buffer)[0]]
    # for filename in args:
    #     print(filename)
    #     p.load_grammar(filename)

# Generated at 2022-06-13 17:56:55.055970
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__.rpartition('.')[0]+'.pyl')

# Generated at 2022-06-13 17:57:02.799019
# Unit test for method dump of class Grammar

# Generated at 2022-06-13 17:57:16.924607
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver
    from .tokenize import tokenize
    from . import parse

    g = driver.load_grammar("Python.asdl")
    p = parse.Parser(g)

    code = """if True:
    print('foo')
"""
    for t in tokenize(code):
        p.addtoken(t)

    # p.parsetokens()  # This also works, but isn't as effective a test

    # Demonstrate the bug fixed in Issue #21594
    try:
        p.addtoken((token.NEWLINE, '\n'))
    except parse.ParseError as pe:
        pass
    else:
        assert False, "addtoken() should have raised ParseError"


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:57:25.265090
# Unit test for method load of class Grammar
def test_Grammar_load():
    import struct
    import io
    import pickle

    pickle_version = pickle.__version__
    
    # int vs. long
    if pickle_version[0] == '1':
        high_version = ord('a')
    elif pickle_version[0] == '2':
        high_version = ord('c')
    elif pickle_version in ('3', '4'):  # pragma: no cover
        high_version = ord('\x80')
    else:  # pragma: no cover
        raise AssertionError(pickle_version)

    # 2.x, 3.x compatibility
    if pickle_version[0] in ('1', '2'):
        long1 = lambda x: x
        long4 = lambda x: x
        proto = ord('c')
   

# Generated at 2022-06-13 17:57:27.956168
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Test loading of pickle files
    g = Grammar()
    g.load("Grammar.txt")

# Generated at 2022-06-13 17:57:38.532233
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.loads(pickle.dumps(g))
    g.load(__file__)

# Generated at 2022-06-13 17:57:51.884108
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    def check(filename: str) -> None:
        g.load(filename)
        assert g.start == 300
        assert g.tokens[1234] == 3
        assert g.keywords["if"] == 5
        assert g.symbol2label["foo"] == 8
        assert g.symbol2number["fusebox"] == 17
        assert g.number2symbol[17] == "fusebox"
        assert g.states[10][20][30] == (40, 50)
        assert g.dfas[1][1][20] == (30, 40)
        assert g.labels[12] == (34, 56)
    with tempfile.TemporaryDirectory() as d:
        filename = os.path.join(d, "test_pickle")
        g.start

# Generated at 2022-06-13 17:57:54.961634
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    assert Grammar().dump  # For pyflakes


if __name__ == "__main__":
    g = Grammar()
    g.report()

# Generated at 2022-06-13 17:58:03.231143
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import ast
    import io
    import pickle
    from pprint import pprint

    class DummyGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.symbol2number["a"] = 1
            self.symbol2number["b"] = 2
            self.symbol2number["c"] = 3
            self.number2symbol[1] = "a"
            self.number2symbol[2] = "b"
            self.number2symbol[3] = "c"
            self.states.append([(1, 2), (3, 4)])
            self.states.append([(5, 6), (7, 8)])

# Generated at 2022-06-13 17:58:12.877824
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import tempfile
    filename = tempfile.mktemp()
    # Test reading the pickle fails
    try:
        with open(filename, 'rb') as f:
            d = pickle.load(f)
    except Exception as e:
        assert(str(e) == f"No such file or directory: '{filename}'")
    # Create a new Grammar object and test method dump
    grammar = Grammar()
    assert(grammar.dump(filename) is None)
    # Test reading the pickle succeeds
    with open(filename, 'rb') as f:
        d = pickle.load(f)
    assert(d == grammar.__dict__)
    # Test reading the pickle fails
    os.remove(filename)

# Generated at 2022-06-13 17:58:15.988699
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest

    g = Grammar()
    g.start = 2
    with pytest.raises(NotImplementedError):
        g.dump("pgen_grammar.pickle")

# Generated at 2022-06-13 17:58:21.391979
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert_grammar
    from .pgen import generate_grammar
    from .parse import Parser

    # Generate a grammar from a Python grammar file
    pgen_grammar_filename = generate_grammar(convert_grammar())

    # Create a new Grammar instance filling its members with data from pickle file
    gr = Grammar()
    gr.load(pgen_grammar_filename)

    # Create a Parser instance
    p = Parser(gr)
    assert len(p.gr.states) > 0

# Generated at 2022-06-13 17:58:31.118460
# Unit test for method load of class Grammar
def test_Grammar_load():
    # copied from Lib/test/test_grammar.py
    from io import BytesIO
    from pickletools import dis
    grammar = Grammar()
    grammar.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    assert grammar.symbol2number["atom"] == 288
    assert grammar.symbol2number["async_stmt"] == 324
    if not grammar.async_keywords:
        assert grammar.symbol2number["async"] == 290

    # test that there's no pickling madness
    f = BytesIO()
    pickle.dump(grammar, f, pickle.HIGHEST_PROTOCOL)
    f.seek(0)
    data = f.read()
    dis(data)
    grammar2 = pickle

# Generated at 2022-06-13 17:58:36.921387
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest

    class GrammarTestCase(unittest.TestCase):
        def test_dumping(self):
            grammar = Grammar()
            grammar.dump("pgen_test.txt")
            try:
                grammar.load("pgen_test.txt")
            finally:
                os.unlink("pgen_test.txt")

    test_case = GrammarTestCase()
    test_case.test_dumping()

# Generated at 2022-06-13 17:58:38.418886
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.pickle")



# Generated at 2022-06-13 17:58:51.532295
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Test pickle protocol 0
    x = Grammar()
    x.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    d = x.__getstate__()
    assert d == x.__dict__
    # Test pickle protocol 2
    x = Grammar()
    x.load(os.path.join(os.path.dirname(__file__), "Grammar.pk2"))
    d = x.__getstate__()
    assert d == x.__dict__

# Generated at 2022-06-13 17:58:54.124968
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load("Python/graminit.pickle")

    # For Python.asdl, we check that the number of
    # definitions is the same as the number of symbols.
    # The numbers are hardcoded here.
    assert len(grammar.symbol2number) == 113
    assert len(grammar.number2symbol) == 113

# Generated at 2022-06-13 17:59:02.887127
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number['foo'] = 42
    g.number2symbol[42] = 'foo'
    g.dfas[43] = (['bar'], {}) # type: ignore
    g.states = ['foo'] # type: ignore
    g.keywords = {'bar': 23, 'baz': 24}
    g.tokens = {25: 26}
    g.symbol2label['a'] = 42
    g.labels = [('b', 'c')] # type: ignore
    g.start = 'b' # type: ignore

    temp_dir = tempfile.mkdtemp(prefix='pytype-test_Grammar_dump-')

# Generated at 2022-06-13 17:59:08.809209
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join("Grammar/Grammar", "Grammar.pkl"))
    grammar.dump("Grammar.pkl")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 17:59:11.175682
# Unit test for method load of class Grammar
def test_Grammar_load():
    # the test environment does not provide a pgen-generated
    # grammar, so we just make sure that the method runs.
    class G(Grammar):
        def __init__(self):
            super().__init__()
            self.load("test.pickle")
    G()

# Generated at 2022-06-13 17:59:17.231695
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle

    class MockGrammar(Grammar):
        def __init__(self):
            self.a = 1
            self.b = 2
            Grammar.__init__(self)

    grammar = MockGrammar()
    grammar.dump("MockGrammar.cache")

    with open("MockGrammar.cache", "rb") as f:
        assert pickle.loads(f.read()) == MockGrammar().__dict__


# Generated at 2022-06-13 17:59:20.487921
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Lib/pgen2/pgen2/Grammar.txt")
    print("done")

# Generated at 2022-06-13 17:59:25.725468
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver
    gram = driver.load_grammar("Grammar/Grammar.txt")
    assert gram.dfas[256][1][token.NAME] == 1
    gram.loads(gram.dumps())
    assert gram.dfas[256][1][token.NAME] == 1


# Generated at 2022-06-13 17:59:33.321065
# Unit test for method load of class Grammar
def test_Grammar_load():
    '''Unit test for method load of class Grammar.'''
    g = Grammar()
    # Test that the tables are empty
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert g.states == []
    assert g.dfas == {}
    assert g.labels == [(0, "EMPTY")]
    assert g.keywords == {}
    assert g.tokens == {}
    # Load the tables from a pickle file.
    g.load('<data>')
    # Test that the tables have been loaded.
    assert g.symbol2number == {'word' : 256, 'expr' : 257, 'term' : 258}
    assert g.number2symbol == {256 : 'word', 257 : 'expr', 258 : 'term'}
    assert g.states

# Generated at 2022-06-13 17:59:35.686717
# Unit test for method load of class Grammar
def test_Grammar_load():
    s = Grammar()
    s.load("Grammar.txt")
    s.report()

# Generated at 2022-06-13 17:59:49.623330
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Verify that Grammar.load can load a pickle file.
    g = Grammar()
    g.symbol2number["foo"] = 42
    g.number2symbol[42] = "foo"
    g.states.append([])
    g.states[0].append((42, 0))
    g.dfas[42] = (g.states[0], {token.NAME:1})
    g.labels.append((token.NAME, None))
    g.keywords[token.NAME] = 42
    g.tokens[token.NAME] = 42
    g.symbol2label["foo"] = 42
    g.start = 42
    with tempfile.TemporaryFile(mode="wb+") as f:
        g.dump(f)
        f.seek(0)
        h = Grammar