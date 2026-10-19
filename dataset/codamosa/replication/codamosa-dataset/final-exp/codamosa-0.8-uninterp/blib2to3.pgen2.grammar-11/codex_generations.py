

# Generated at 2022-06-13 17:49:48.767149
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("/tmp/test_Grammar_dump")

test_Grammar_dump()

# Generated at 2022-06-13 17:49:59.306583
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'aa': 1, 'bb': 2}
    g.number2symbol = {1: 'aa', 2: 'bb'}
    g.states = [
        [(1, 0)],
        [(2, 1)]
    ]
    g.dfas = {
        1: ([], {1: 1}),
        2: ([], {1: 1})
    }
    g.labels = [(1, 'a'), (0, 'b')]
    g.start = 2
    g.keywords = {'b': 0}
    g.tokens = {1: 1}
    g.symbol2label = {'a': 0, 'b': 1}
    g.dump('/tmp/Grammar' + '.dump')

# Generated at 2022-06-13 17:50:02.050142
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load('/PATH/TO/Python/Grammar.txt')
    assert g.start == 256

# Generated at 2022-06-13 17:50:15.969055
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    import tempfile
    import os
    assert callable(Grammar.dump)

    def check_dump(grammar: Grammar) -> None:
        fd, filename = tempfile.mkstemp()
        os.close(fd)
        grammar.dump(filename)
        with open(filename, "rb") as f:
            new_grammar_d = pickle.load(f)
        os.remove(filename)
        assert new_grammar_d == grammar.__dict__
    check_dump(Grammar())

# Generated at 2022-06-13 17:50:18.213584
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import *
    from . import pgen2

    grammar = Grammar()
    CreateGrammar(pgen2, grammar)
    grammar.dump('test.pkl')

    grammar2 = Grammar()
    grammar2.load('test.pkl')
    grammar2.report()

# Generated at 2022-06-13 17:50:22.606823
# Unit test for method load of class Grammar
def test_Grammar_load():
    import py
    g = Grammar()
    before = g.tokens.copy()
    f = py.path.local.make_numbered_dir(prefix="grammar_", keep=3)
    g.dump(f.join("grammar.pyc"))
    g = Grammar()
    assert not g.tokens
    g.load(f.join("grammar.pyc"))
    assert g.tokens == before



# Generated at 2022-06-13 17:50:25.976630
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load("Grammar.pickle")
    for line in opmap_raw.splitlines():
        if line:
            op, name = line.split()
            assert getattr(token, name) == opmap[op]


del opmap_raw

# Generated at 2022-06-13 17:50:31.039931
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Test dump() method of Grammar class.
    """
    from . import pgen
    from .conv import parseGrammar
    from .parse import Parser

    file = 'pickle_grammar_temp.pkl'
    g = parseGrammar(pgen.grammar, 'file_input')
    g.dump(file)
    h = Grammar()
    h.load(file)
    p = Parser(h)
    p.parse()
    os.remove(file)



# Generated at 2022-06-13 17:50:35.224222
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    assert isinstance(grammar, Grammar)

# Generated at 2022-06-13 17:50:43.615827
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import Convertor
    from .pgen import generate_grammar
    from tempfile import NamedTemporaryFile
    from .compile import compile_grammar
    import sys

    def _test_compile_grammar(source, tmpfile):
        grammar = generate_grammar(source, outputdir=os.path.dirname(tmpfile.name))
        grammar.dump(tmpfile)
        tmpfile.seek(0)
        cgrammar = Grammar()
        cgrammar.load(tmpfile)
        assert grammar == cgrammar

    # Basic tests
    with NamedTemporaryFile(delete=False) as tmpfile:
        _test_compile_grammar('parser/Grammar.py', tmpfile)
        _test_compile_grammar('grammar.pickle', tmpfile)

    # Test

# Generated at 2022-06-13 17:50:56.951707
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    f = Grammar()
    f.dump("/tmp/astroid_test_file")
    f.load("/tmp/astroid_test_file")

# Generated at 2022-06-13 17:51:02.649046
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load("Python3.6.2/Grammar/Grammar")
    assert grammar.async_keywords
    grammar.load("Python3.7/Grammar/Grammar")
    assert grammar.async_keywords
    grammar.load("Python3.8/Grammar/Grammar")
    assert grammar.async_keywords

# Generated at 2022-06-13 17:51:04.822856
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Tests of method load of class Grammar.
    grammar = Grammar()
    assert not hasattr(grammar, "symbol2number")
    grammar.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    assert hasattr(grammar, "symbol2number")

# Generated at 2022-06-13 17:51:15.010932
# Unit test for method load of class Grammar
def test_Grammar_load():
    import os
    import tempfile
    import pickle

    # Create test file
    tmp_file = os.path.join(tempfile.gettempdir(), "test_Grammar_load.pkl")
    with open(tmp_file, "wb") as f:
        d = dict(x=1, y=2)
        pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)

    # Test load() method
    g = Grammar()
    g.load(tmp_file)
    assert g.x == 1
    assert g.y == 2

    # Remove test file
    os.remove(tmp_file)

# Generated at 2022-06-13 17:51:24.217662
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys

    try:
        import importlib.resources as ir
    except ImportError:
        # Try backported to PY<37 `importlib_resources`.
        import importlib_resources as ir

    with ir.path(tokenize_grammar, "Grammar.pkl") as pkl:
        g = Grammar()
        g.loads(pkl.read_bytes())
        f = tempfile.NamedTemporaryFile(prefix="Grammar", suffix=".pkl", delete=False)


# Generated at 2022-06-13 17:51:28.092026
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    G = Grammar()
    try:
        with tempfile.TemporaryDirectory() as path:
            G.dump(os.path.join(path, "grammar.pickle"))
    except OSError:
        pass  # Likely the file already exists

# Generated at 2022-06-13 17:51:29.853990
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load('Grammar.txt')
    grammar.report()


# Generated at 2022-06-13 17:51:34.903181
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g1 = Grammar()
    Grammar._dump(g1, 'tmp.pickle')
    # check file created and can be loaded
    g2 = Grammar()
    g2.load('tmp.pickle')
    assert g1 is not g2
    if hasattr(g1, '__dict__'):
        assert g1.__dict__ == g2.__dict__
    else:
        assert g1.__getstate__() == g2.__getstate__()
    os.remove('tmp.pickle')

# Generated at 2022-06-13 17:51:36.793213
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    dummy_filename = '/tmp/pgen_Grammar_dump_test'

    g = Grammar()
    g.dump(dummy_filename)

    g.load(dummy_filename)

    os.remove(dummy_filename)

# Generated at 2022-06-13 17:51:46.840896
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Test the method load of class Grammar
    g = Grammar()
    sym_msg = "abc"
    sym_msg2 = "Hello world"
    gs = Grammar()
    gs.symbol2number = {sym_msg: "1", sym_msg2: "2"}
    sym_sym = "world"
    sym_sym2 = "Hello"
    gs.number2symbol = {sym_sym: "2", sym_sym2: "1"}
    dfa1 = [1, 2]
    dfa2 = [2, 3]
    gs.states = [dfa1, dfa2]
    sym_dfa1 = 123
    sym_dfa2 = 0

# Generated at 2022-06-13 17:52:00.067259
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.number2symbol = {300: 'STMT'}
    g.symbol2number = {'STMT': 300}
    g.start = 300
    g.states = [[[(0, None), (5, 2)], [(5, 3)], [], [(5, 4)], [], [(5, 1)]],
                [[(0, None)], [], [], [], [], [(5, 2)]]]

# Generated at 2022-06-13 17:52:09.765547
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import parse_grammar, write_grammar
    from .pgen import generate_grammar
    from .tokenizer import generate_tokens, untokenize

    g = Grammar()
    parse_grammar(g, "Grammar.txt")
    write_grammar(g, "Grammar.txt")
    parse_grammar(g, "Grammar.txt")
    generate_grammar(g, "Grammar.txt")
    parse_grammar(g, "Grammar.txt")

    # Grammar.txt contains a code fragment that needs to be tokenized
    source = open("Grammar.txt").read()
    tokens = list(generate_tokens(source))[:-1]
    tokens2 = generate_tokens(source + "\n")

# Generated at 2022-06-13 17:52:17.813429
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    foo = Grammar()
    # initialize tables
    foo.symbol2number = {'x': "3"}
    foo.number2symbol = {3: 'x'}
    foo.states = [
        [
            [(1, 1), (2, 2), (0, 3)],
            [(4, 4)],
            [(5, 5), (6, 6)],
            [],
            [(7, 7)],
            [(8, 8)],
            []
        ]
    ]

# Generated at 2022-06-13 17:52:22.712933
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = os.path.join(tempfile.gettempdir(), "tmp-grammar.pickle")
    try:
        os.remove(filename)
    except OSError:
        pass

    g = Grammar()
    g.dump(filename)
    g2 = Grammar()
    g2.load(filename)

# Generated at 2022-06-13 17:52:33.041957
# Unit test for method load of class Grammar
def test_Grammar_load():
    from ..pgen2 import driver
    import os
    import tempfile
    import time

    def test(name: Text, version: str) -> None:
        fname = os.path.join(os.path.dirname(__file__), "Python" + version + ".grammar")
        with open(fname, "rb") as f:
            g = driver.load_grammar(f)

        t1 = time.perf_counter()
        for i in range(100):
            g_copy = g.copy()
        print(name, "copy", time.perf_counter() - t1)

        t1 = time.perf_counter()
        for i in range(100):
            g_copy = pickle.loads(pickle.dumps(g))

# Generated at 2022-06-13 17:52:35.183820
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Test load().
    """
    g = Grammar()
    s = pickle.dumps(g)
    g.loads(s)
    del g

# Generated at 2022-06-13 17:52:36.296112
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    assert Grammar().dump(None) == None

# Generated at 2022-06-13 17:52:42.259582
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle

    # mypyc can't handle this, since it depends on unittest.TestCase
    # class GrammarTestCase(unittest.TestCase):
    #     def setUp(self):
    #         self.grammar = Grammar()
    #     def test_dump(self):
    #         self.grammar.dump('/tmp/GrammarTest.pickle')
    #         with open('/tmp/GrammarTest.pickle', 'rb') as f:
    #             d = pickle.load(f)
    #         self.assertTrue(d)

    # mypyc can't handle this, since it depends on unittest.TestCase
    # class GrammarTestCase(unittest.TestCase):
    #     def setUp(self):
    #         self.grammar

# Generated at 2022-06-13 17:52:49.721696
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.loads(b'\x80\x04\x95\xc7\x00\x00\x00\x00\x00\x00\x00\x8c#token\x94\x8c\x04NAME\x94K\x00K\x01K\x02\x86\x94\x8c\ntype_ignore\x94K\x00\x86\x94.')



# Generated at 2022-06-13 17:53:01.940874
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__)  # Test that loading from a file works

    s = pickle.dumps(g)
    g2 = Grammar()
    g2.loads(s)  # Test that loading from a bytes object works

    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.states == g2.states
    assert g.dfas == g2.dfas
    assert g.labels == g2.labels
    assert g.keywords == g2.keywords
    assert g.tokens == g2.tokens
    assert g.symbol2label == g2.symbol2label
    assert g.start == g2.start

    # Check that copying works


# Generated at 2022-06-13 17:53:26.010468
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .parse import Parser
    from .conv import parse_grammar_file, generate_grammar, convert_grammar
    from .pgen import read_grammar

    grammar_file = os.path.join(os.path.dirname(__file__), "Grammar.txt")
    tmp_prefix = os.path.join(
        os.path.dirname(__file__), "tmp_grammar_%s" % __name__
    )

    # Test the parsing
    grammar = parse_grammar_file(grammar_file)
    generate_grammar(grammar, tmp_prefix)
    py_grammar = read_grammar(tmp_prefix + ".py", None)
    pkl_grammar = read_grammar(tmp_prefix + ".pickle", None)

# Generated at 2022-06-13 17:53:33.052872
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest
    from tempfile import NamedTemporaryFile
    from pickle import load, HIGHEST_PROTOCOL
    # no coverage for this test case, as it should be covered by mypyc
    if False:
        from . import conv

    if False:
        from .pgen2 import driver # no coverage

    grammar = Grammar()
    with NamedTemporaryFile() as file:
        grammar.dump(file.name)
        with open(file.name, "rb") as pkl_file:
            load(pkl_file)

# Generated at 2022-06-13 17:53:37.460735
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import os
    import tempfile
    from . import pgen2
    g = pgen2.parse_grammar(io.StringIO(pgen2.grammar), "Grammar", "grammar")
    fd, name = tempfile.mkstemp()
    os.close(fd)
    try:
        g.dump(name)
        g.load(name)
    finally:
        os.remove(name)

# Generated at 2022-06-13 17:53:46.229148
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class TestGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__()
            # test attributes
            self.symbol2number = {"a": 1, "b": 2, "c": 3, "d": 4}
            self.number2symbol = {"1": "a", "2": "b", "3": "c", "4": "d"}
            self.states = [[(0, 1)], [(1, 1), (2, 4)], [(1, 2)], [(2, 3)], []]
            self.dfas = {"1": (self.states[0], {1: 1}), "2": (self.states[1], {1: 1})}

# Generated at 2022-06-13 17:53:57.019468
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"None": 0, "True": 1, "False": 2, "Ellipsis": 3}
    g.number2symbol = {0: "None", 1: "True", 2: "False", 3: "Ellipsis"}
    g.states = [
        [
            [(1, 2), (1, 3), (1, 4), (3, 7)],
            [(9, 7), (1, 6)],
            [],
            [(1, 5)],
            [],
            [(4, 2)],
            [(4, 3)],
            [],
        ]
    ]

# Generated at 2022-06-13 17:54:00.969478
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .grammar import Grammar
    g = Grammar()
    with open(os.path.join(os.path.dirname(__file__), 'Grammar.pkl'), 'rb') as f:
        g.loads(f.read())
    assert g.tokens[token.STRING] == g.labels[1]

# Generated at 2022-06-13 17:54:11.671317
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {'symbol': 0}
    grammar.number2symbol = {0: 'symbol'}
    grammar.states = [[]]
    grammar.dfas = {0: ([[],[]], dict())}
    grammar.labels = [(0, None)]
    grammar.keywords = {'keyword': 0}
    grammar.tokens = {0: 0}
    grammar.symbol2label = {'symbol': 0}
    grammar.start = 256
    grammar.async_keywords = False

    f = os.path.join(os.path.dirname(__file__), "../test/test.pkl")
    grammar.dump(f)

    grammar2 = Grammar()
    grammar2.load(f)

    assert grammar.sy

# Generated at 2022-06-13 17:54:21.338630
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Test load() method of Grammar"""
    # Python 3.7+ parses async as a keyword, not an identifier
    grammar = Grammar()

# Generated at 2022-06-13 17:54:27.997606
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import io
    from pickle import dumps

    class Test_Grammar_load(unittest.TestCase):
        @staticmethod
        def test_Grammar_load_empty(self):
            g = Grammar()
            f = io.BytesIO()
            g.dump(f)
            f.seek(0)
            g.load(f)

    unittest.main(Test_Grammar_load)

# Generated at 2022-06-13 17:54:30.427042
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    filename = "foo.pkl"
    grammar = Grammar()
    grammar.dump(filename)
    with open(filename, 'rb') as f:
        pickle.load(f)

# Generated at 2022-06-13 17:54:44.051174
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import tokenize
    from .pgen2 import tokenize as tokenize2
    from . import pytree
    from . import pygram
    from .pgen2 import driver

    def compare(pkl, old_start, new_symbol2number, new_states):
        old_g = pickle.loads(pkl)
        old_g.report()
        old_g.start == old_start
        old_g.symbol2number == new_symbol2number
        old_g.states == new_states

    pygram_grammar = pygram.python_grammar
    pygram_grammar_no_print_statement = pygram.python_grammar_no_print_statement
    driver.load_grammar(pygram_grammar)

    fname = tempfile.NamedTemporaryFile().name
   

# Generated at 2022-06-13 17:54:48.799478
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    assert g.start == 256
    g.load('/tmp/test_Grammar_load')
    assert g.start == -1


if __name__ == "__main__":
    import sys

    g = Grammar()
    g.load(sys.argv[1])
    g.report()

# Generated at 2022-06-13 17:54:57.053995
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import io

    # Construct a grammar object
    grammar = Grammar()
    grammar.symbol2number = {'term': 256, 'dotted_name': 257}
    grammar.number2symbol = {256: 'term', 257: 'dotted_name'}
    grammar.states = [[[(257, 1)],
                       [(1, 0), (0, -1)],
                       [(1, 2), (0, -2)],
                      ]]
    grammar.dfas = {256: (grammar.states[0], {257: 1}),
                    257: (grammar.states[0], {257: 1})}
    grammar.labels = [(0, 'EMPTY'), (257, 'dotted_name')]
    grammar.keywords = {'dotted_name': 257}
    grammar

# Generated at 2022-06-13 17:55:08.017548
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:55:12.198839
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver
    from . import pytree

    # This should exercise a few edges cases in the dump/loads
    # process.  Basically, we want to get something that looks
    # like a normal compilation run, but then we want to short-
    # circuit the parser and instead just use the dumped grammar.


# Generated at 2022-06-13 17:55:19.239097
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import conv
    from . import pgen

    # Create a grammar object
    f = conv.ForestGrammar()
    g = pgen.pgen(f)

    # Dump the grammar object
    t = tempfile.mktemp()
    g.dump(t)

    # Load the dumped object
    h = Grammar()
    h.load(t)

    assert g.states == h.states
    assert g.keywords == h.keywords
    assert g.tokens == h.tokens
    assert g.symbol2label == h.symbol2label
    assert g.start == h.start

# Generated at 2022-06-13 17:55:21.947769
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver, parser

    gr = driver.load_grammar("Grammar/Grammar")
    assert gr
    assert gr.start == 257
    assert gr.symbol2number == parser.symbol2label



# Generated at 2022-06-13 17:55:30.773915
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os.path

    def _test_Grammar_dump_1(tmpdir_autodel: str) -> str:
        filename = os.path.join(tmpdir_autodel, "pgen_test")
        grammar = Grammar()

        # Generate an empty grammar
        grammar.dump(filename)
        grammar.load(filename)

        # Generate a simple grammar
        grammar.keywords = dict(a=257)
        grammar.tokens = dict(b=258)
        grammar.symbol2number = dict(c=259)
        grammar.start = 259

# Generated at 2022-06-13 17:55:32.169978
# Unit test for method load of class Grammar
def test_Grammar_load():
    pass


if __name__ == "__main__":
    # Test the method load of class Grammar
    test_Grammar_load()

# Generated at 2022-06-13 17:55:40.018170
# Unit test for method load of class Grammar
def test_Grammar_load():
    import re
    import sys
    import pickle
    from . import pgen2

    filename = sys.argv[0]
    if re.search(r"\.py$", filename):
        filename = re.sub(r"\.py$", ".pkl", filename)

    g = Grammar()
    g.load(filename)

    g2 = pgen2.make_grammar(pickle.loads)
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.states == g2.states
    assert g.dfas == g2.dfas
    assert g.labels == g2.labels
    assert g.keywords == g2.keywords
    assert g.tokens == g2.tokens

# Generated at 2022-06-13 17:55:50.285557
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    Verify that loading a dumped grammar does not raise an exception.
    """
    filename = os.path.join(os.path.dirname(__file__), "Grammar.txt")
    with open(filename, "rb") as f:
        pickle_data: bytes = f.read()
    test_grammar = Grammar()
    test_grammar.loads(pickle_data)
    # the pickle data is specific to Python 3.6, so we don't
    # actually check any of the fields

# Generated at 2022-06-13 17:55:53.809693
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        g.dump(f.name)
    os.remove(f.name)

# Generated at 2022-06-13 17:55:55.717868
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert Grammar().load(os.path.join(os.path.split(__file__)[0], "Grammar.pkl")) is None

# Generated at 2022-06-13 17:56:02.925597
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {"fake_symbol2number_a": 0, "fake_symbol2number_b": 1}
    grammar.number2symbol = {"fake_number2symbol_a": 0, "fake_number2symbol_b": 1}
    grammar.states = ["fake_states_a", "fake_states_b"]
    grammar.dfas = {"fake_dfas_a": (0, 1), "fake_dfas_b": (0, 2)}
    grammar.labels = [("fake_labels_a", None)]
    grammar.keywords = {"fake_keywords_a": "fake_keywords_a"}
    grammar.tokens = {"fake_tokens_a": "fake_tokens_a"}
    grammar.symbol2

# Generated at 2022-06-13 17:56:08.615001
# Unit test for method load of class Grammar
def test_Grammar_load():
    print("--- Testing Grammar load ---")
    with open("Grammar.pickle", "rb") as f:
        d = pickle.load(f)
    gr = Grammar()
    gr.loads(pickle.dumps(d))
    if gr.load:
        print("Success")
    else:
        print("Fail")


# Generated at 2022-06-13 17:56:17.627459
# Unit test for method load of class Grammar
def test_Grammar_load():
    import sys
    import os
    import pickle
    import unittest

    class _TestGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__()
            self.symbol2number = {"'foo'": 257, "'bar'": 258, "'baz'": 259}
            self.number2symbol = {v: k for k, v in self.symbol2number.items()}
            self.states = [[(0, 0)]]
            self.dfas = {
                258: (self.states[0], {}),
                257: (self.states[0], {"'bar'": 1, "'baz'": 1}),
            }
            self.labels = [(1, None)]
            self.keywords = {"'bar'": 1}
           

# Generated at 2022-06-13 17:56:26.206469
# Unit test for method load of class Grammar
def test_Grammar_load():
    import sys
    import pickle
    import unittest

    class TestGrammarLoad(unittest.TestCase):
        grammar_file = sys.modules[__name__].__file__.replace(".py", ".pgen_grammar")
        with open(grammar_file, "rb") as f:
            grammar_data = pickle.load(f)

        def check_dict(self, dict_name: str, dict_attr: str):
            # getattr(self.g, attr) is a view (python >= 3.7) or a
            # dictproxy (python < 3.7).
            # This should work in both cases
            assertion = getattr(self.g, dict_name) == self.grammar_data[dict_attr]
            self.assertTrue(assertion)


# Generated at 2022-06-13 17:56:30.933689
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gr = Grammar()
    gr.dump("/tmp/testpickle.pickle.23.125")

if __name__ == "__main__":
    test_Grammar_dump()
    print("All tests passed")

# Generated at 2022-06-13 17:56:40.424600
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    import gzip
    import io
    from . import grammar
    from .tokenize import detect_encoding
    from .pgen2 import tokenize

    class TestCase(unittest.TestCase):
        def run_test(self):
            with tokenize.open(grammar.__file__) as f:
                encoding, _ = detect_encoding(f.readline)
            with open(grammar.__file__, encoding=encoding) as f:
                encoding, _ = detect_encoding(f.readline)
            with tokenize.open(grammar.__file__, encoding=encoding) as f:
                lines = []
                for line in f:
                    lines.append(line)
                data = "".join(lines)

            # We want to test round-tripping to and

# Generated at 2022-06-13 17:56:50.027272
# Unit test for method load of class Grammar
def test_Grammar_load():

    from . import grammar, parser

    import sys

    f = open(grammar.__file__)
    g = f.read()
    f.close()

    f, path = tempfile.mkstemp()
    os.close(f)
    try:
        p = pickle.dumps(g, pickle.HIGHEST_PROTOCOL)
        f = open(path, "wb")
        f.write(p)
        f.close()
        g2 = Grammar()
        g2.load(path)
        sys.stdout.write("Grammar loaded OK\n")  # noqa
    finally:
        os.remove(path)

# Generated at 2022-06-13 17:57:02.531136
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"a": 0, "b": 1, "c": 2}
    g.number2symbol = {0: "a", 1: "b", 2: "c"}
    g.states = [[(0, 0), (1, 1), (0, 1)], [(None, 0), (2, 1), (3, 2)]]
    g.dfas = {0: (g.states[0], {0: 1, 1: 1}), 1: (g.states[1], {0: 1, 1: 1, 2: 1})}
    g.labels = [(0, "EMPTY"), None, (1, "b"), (2, "c")]
    g.keywords = {"b": 2, "c": 3}

# Generated at 2022-06-13 17:57:14.040819
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 0
    g.symbol2number = {'root': 0}
    g.number2symbol = {0: 'root'}
    g.labels = [(0, "EMPTY")]
    filename = 'grammar.pkl'
    g.dump(filename)
    g1 = Grammar()
    g1.load(filename)
    assert g.start == g1.start
    assert g.symbol2number == g1.symbol2number
    assert g.number2symbol == g1.number2symbol
    assert g.labels == g1.labels



# Generated at 2022-06-13 17:57:23.535057
# Unit test for method load of class Grammar
def test_Grammar_load():
    Grammar().load("Grammar.pickle")

# Generated at 2022-06-13 17:57:38.830370
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    from pickle import NONE
    from io import BytesIO
    import unittest
    import textwrap
    from collections import defaultdict

    pickle_proto: int = pickle.HIGHEST_PROTOCOL

    class GrammarTests(unittest.TestCase):

        def test_dump_load(self):
            for proto in range(pickle_proto + 1):
                g1 = Grammar()
                g1.symbol2number = defaultdict(lambda: 0, symbol2number={'a': 1})
                g1.number2symbol = defaultdict(lambda: 0, number2symbol={1: 'a'})
                g1.states = [1, 2]

# Generated at 2022-06-13 17:57:52.193100
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import types
    def load(byte_stream: io.BytesIO) -> Dict[str, Any]:
        return types.MappingProxyType(pickle.load(byte_stream))
    g = Grammar()
    with tempfile.NamedTemporaryFile(
        dir=os.path.dirname(__file__), delete=False
    ) as f:
        g.dump(f.name)

# Generated at 2022-06-13 17:57:59.517895
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import conv

    gf = conv.GrammarFile()
    gf.load_grammar()
    g = gf.grammar

    with tempfile.TemporaryDirectory() as dirname:
        filename = os.path.join(dirname, "test.pgen")
        g.dump(filename)
        g2 = Grammar()
        g2.load(filename)
        assert g.symbol2number == g2.symbol2number
        # The above assertion may fail, if the grammar file has been updated.
        assert g.keywords == g2.keywords


# Generated at 2022-06-13 17:58:07.342220
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from pathlib import Path
    from subprocess import getstatusoutput

    g = Grammar()
    g.dump('_test_grammar_dump.pkl')
    g.load('_test_grammar_dump.pkl')
    g.report()
    getstatusoutput('rm -f _test_grammar_dump.pkl')

# Generated at 2022-06-13 17:58:17.087947
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # To make mypy happy, we need to assign a value to the locals
    # that we are going to use, so create the bare objects we're going
    # to assign to.
    g = Grammar()
    filename = None
    try:
        f = tempfile.NamedTemporaryFile(delete=False)
        filename = f.name
        f.close()

        g.dump(filename)

    finally:
        if filename:
            try:
                os.unlink(filename)
            except OSError:
                pass

# Generated at 2022-06-13 17:58:27.809739
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test dumping to a file, and loading from it
    g = Grammar()
    g.symbol2number = {"key1": 1, "key2": 2}
    g.number2symbol = {2: "key2", 1: "key1"}
    g.states = [[[(1,1)]]]
    g.dfas = {1:([[(1,1)]], {})}
    g.labels = [(1,None)]
    g_file = "my_file"
    g.dump(g_file)
    g2 = Grammar()
    g2.load(g_file)
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.states == g2.states

# Generated at 2022-06-13 17:58:33.869995
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 5
    g.symbol2number = {"s1": 1, "s2": 2}
    g.number2symbol = {1: "s1", 2: "s2"}
    g.dfas = {
        1: ([[(2, 2), (0, 1)], [(3, 3)], [(0, 1), (3, 3)]], {1: 2, 3: 2}),
        2: ([[(0, 1)]], {1: 1}),
        3: ([[(0, 1)]], {1: 1}),
    }
    g.states = [[[(2, 2), (0, 1)], [(3, 3)], [(0, 1), (3, 3)]]]

# Generated at 2022-06-13 17:58:46.722038
# Unit test for method dump of class Grammar

# Generated at 2022-06-13 17:58:52.744468
# Unit test for method load of class Grammar
def test_Grammar_load():

    def helper(filename, module, message):
        if os.path.exists(filename) and os.stat(filename).st_size > 0:
            g = Grammar()
            g.load(filename)
            s = module.check_grammar(g)
            print(s, end=' ')
            assert not s, message
        else:
            print("no grammar file: " + filename)

    # mypyc doesn't produce a __curdir__ attribute on the module object
    # so just build the filename relative to this test function
    filename = os.path.join(os.path.dirname(__file__), "Grammar.pkl")
    helper(filename, token, "token module")
    import brainfuck


# Generated at 2022-06-13 17:58:55.127005
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    with tempfile.TemporaryDirectory() as td:
        filename = os.path.join(td, "grammar.pickle")

        g = Grammar()
        g.dump(filename)
        with open(filename, 'rb') as f:
            assert len(f.read()) > 0


# Generated at 2022-06-13 17:59:00.976079
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"test": 1}
    with tempfile.NamedTemporaryFile(delete=False) as f:
        pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        g.loads(open(f.name, "rb").read())
        assert g.symbol2number == {"test": 1}, "dump and loads in Grammar class failed"
        os.remove(f.name)


# Generated at 2022-06-13 17:59:01.994300
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load
    g.loads
    g.copy
    g.report

# Generated at 2022-06-13 17:59:14.221357
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    from unittest import mock

    grammar = Grammar()

    grammar.symbol2number = {"foo": 257}
    grammar.number2symbol = {257: "foo"}
    grammar.states = [
        [
            [(0, 0), (0, 0)],
            [(0, 0), (1, 0)],
            [(1, 1), (0, 2)],
            [(2, 2), (0, 3)],
        ]
    ]
    grammar.dfas = {
        257: (grammar.states[0], {257: 1}),
    }
    grammar.labels = [(0, "EMPTY"), (257, None), (258, None), (0, "EMPTY")]
    grammar.keywords = {"a": 258}

# Generated at 2022-06-13 17:59:25.945438
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.test_attr = "test"
    grammar.symbol2number = {"TEST": 1}
    grammar.number2symbol = {1: "TEST"}
    grammar.states = [[]]
    grammar.dfas = {1: ([], {})}
    grammar.labels = [(1, "TEST")]
    grammar.keywords = {"TEST": 1}
    grammar.tokens = {1: 1}
    grammar.symbol2label = {1: 1}
    grammar.start = 256
    grammar.async_keywords = False
    with tempfile.NamedTemporaryFile(delete=False) as f:
        grammar.dump(f.name)
        new_grammar = Grammar()
        new_grammar.load(f.name)
        assert new

# Generated at 2022-06-13 17:59:33.424842
# Unit test for method load of class Grammar
def test_Grammar_load():
    import io
    import pickle
    from typing import Dict
    from . import token

    def unpickle(g: Grammar):
        # type: (Grammar) -> Dict[str, Any]

        # mypyc generates objects that don't have a __dict__, but they
        # do have __getstate__ methods that will return an equivalent
        # dictionary
        if hasattr(g, "__dict__"):
            d = g.__dict__
        else:
            d = g.__getstate__()  # type: ignore

        return d

    grammar = Grammar()
    grammar.keywords = {'else': 257, 'print': 258}
    grammar.tokens = {token.PLUS: 1, token.MINUS: 2}

# Generated at 2022-06-13 17:59:39.651511
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from os import unlink

    def remove(filename):
        # unlink succeeds if filename exists,
        # otherwise silently fails.
        try:
            unlink(filename)
        except OSError:
            pass

    i = Grammar()
    i.symbol2number = {}
    i.number2symbol = {}
    i.states = []
    i.dfas = {}
    i.labels = []
    i.keywords = {}
    i.tokens = {}
    i.symbol2label = {}
    i.start = 256
    i.async_keywords = False
    filename = "testdata/test_Grammar_dump.pkl"
    remove(filename)
    i.dump(filename)
    assert os.path.exists(filename)
    i2 = Grammar