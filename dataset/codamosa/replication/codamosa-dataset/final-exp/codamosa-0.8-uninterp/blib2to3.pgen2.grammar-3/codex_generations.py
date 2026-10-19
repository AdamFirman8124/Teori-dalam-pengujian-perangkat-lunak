

# Generated at 2022-06-13 17:49:57.948248
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Create a Grammar
    g1 = Grammar()
    g1.symbol2number = {"START": 256}
    g1.number2symbol = {256: "START"}
    g1.states = [[]]
    g1.dfas = {}
    g1.labels = [(0, "EMPTY")]
    g1.keywords = {}
    g1.tokens = {}
    g1.symbol2label = {}
    g1.start = 256
    g1.async_keywords = False

    # Dump it to a file
    g1.dump("./START.g")

    # Create a new one
    g2 = Grammar()
    # Load it from the file
    g2.load("./START.g")
    assert g2.symbol

# Generated at 2022-06-13 17:50:01.199681
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test Grammar.dump()."""
    g = Grammar()
    g.dump("/tmp/Grammar.dump")
    assert os.path.exists("/tmp/Grammar.dump")
    os.remove("/tmp/Grammar.dump")

# Generated at 2022-06-13 17:50:11.763390
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(os.path.join(os.path.dirname(__file__), "Grammar.pkl"))
    assert grammar.number2symbol[256] == "single_input"
    assert grammar.number2symbol[257] == "eval_input"
    assert grammar.number2symbol[258] == "file_input"
    assert grammar.number2symbol[259] == "decorator"
    assert grammar.number2symbol[260] == "decorators"
    assert grammar.number2symbol[261] == "decorated"
    assert grammar.number2symbol[262] == "async_funcdef"
    assert grammar.number2symbol[263] == "funcdef"
    assert grammar.number2symbol[264] == "parameters"

# Generated at 2022-06-13 17:50:21.304738
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 257
    g.tokens = {1: 2, 3: 4}
    g.symbol2number = {'a': 65, 'b': 66}
    g.number2symbol = {65: 'a', 66: 'b'}
    g.labels = [(1, "a"), (2, None)]
    g.dfas = {257: (
        [
            [(65, 1), (66, 2)],
            [(2, 1)],
            [],
        ],
        {2: 1, 4: 2},
    )}
    g.keywords = {"a": 1, "b": 2}
    g.symbol2label = {'a': 1, 'b': 2}
    import tempfile
    tmp_path = tempfile.Named

# Generated at 2022-06-13 17:50:29.904530
# Unit test for method load of class Grammar
def test_Grammar_load():
    import sys
    import pytest
    mypy = pytest.importorskip("mypy")

    def f(obj: Any) -> None:
        g = Grammar()
        g.load(obj)
        if not mypy:
            raise RuntimeError("need mypy to verify the correct types")
        assert isinstance(g.symbol2number, dict)
        assert isinstance(g.number2symbol, dict)
        assert isinstance(g.states, list)
        for state in g.states:
            assert isinstance(state, list)
            for arc in state:
                assert isinstance(arc, tuple)
                assert len(arc) == 2
                assert isinstance(arc[0], int)
                assert isinstance(arc[1], int)
        assert isinstance(g.dfas, dict)
       

# Generated at 2022-06-13 17:50:32.519244
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__.replace(".py", ".pickle"))
    assert g.symbol2number["and"] == 257
    assert g.tokens[token.NAME] == 0
    assert g.start == 257



# Generated at 2022-06-13 17:50:35.745590
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Grammar_dump.test"""
    import os
    import tempfile

    gram = Grammar()
    gram.dump(os.path.join(tempfile.gettempdir(), "grammar"))



# Generated at 2022-06-13 17:50:43.945935
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load('pgen-pickle/Grammar.pickle')

# Generated at 2022-06-13 17:50:55.063944
# Unit test for method load of class Grammar
def test_Grammar_load():
    dfa_grammar_fname = os.path.join(os.path.dirname(__file__), "DfaGrammar.pickle")
    grammar_fname = os.path.join(os.path.dirname(__file__), "Grammar.pickle")
    if not os.path.exists(dfa_grammar_fname):
        from . import pgen2
        from . import conv

        g = conv.convert_grammar("Grammar.txt")
        g.report()
        g.dump(dfa_grammar_fname)
        g = Grammar()
        g.load(dfa_grammar_fname)
        g = pgen2.Grammar()
        g.load(dfa_grammar_fname)

# Generated at 2022-06-13 17:51:01.833851
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    G = Grammar()
    G.symbol2number = {"foo" : 256}
    G.dump("/tmp/test_Grammar_dump")
    with open('/tmp/test_Grammar_dump', 'rb') as f:
        s = f.read()
    os.remove('/tmp/test_Grammar_dump')
    assert s.startswith(b"\x80\x03cbuiltins\nGrammar\nq\x00)")

# Generated at 2022-06-13 17:51:17.363125
# Unit test for method load of class Grammar
def test_Grammar_load():
    import datetime
    import pickle
    import sys
    from io import BytesIO
    from typing import Dict, Tuple
    from . import tokenize

    from . import token

    # Grammar-pickling works only for the same Python version
    # If invoked from Python 3.8, for example, it should create
    # a Python 3.8-specific pickle.
    assert sys.version_info[0] == 3
    assert sys.version_info[1] in (6, 7, 8)
    pickle_version = tokenize.PICKLE_PROTOCOL

    # Create a token list.
    ut = tokenize.Untokenizer()
    ut.find_lines = lambda: [datetime.datetime.now()]
    ut.newline = lambda: b"\n"

# Generated at 2022-06-13 17:51:21.098538
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr = Grammar()
    assert gr.keywords == {}
    gr.keywords = {"abc": 1, "def": 2}
    assert gr.keywords != {}
    gr.load("/dev/null")
    assert gr.keywords == {}


# Generated at 2022-06-13 17:51:24.585327
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest

    g = Grammar()
    with pytest.raises(NotImplementedError):
        g.dump('foo')

# Generated at 2022-06-13 17:51:26.893876
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(__file__.replace(".py", ".grammar"))

# Generated at 2022-06-13 17:51:29.855569
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Check that no exception is raised when loading a grammar
    Grammar().load(__file__)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 17:51:37.437186
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number["+"] = 1
    g.number2symbol[1] = "+"
    g.states.append([])
    g.dfas[0] = g.states[0], {"a": 1}
    g.labels.append((1, None))
    g.keywords["a"] = 0
    g.tokens[1] = 0
    g.symbol2label["b"] = 0
    g.start = 1

    # mypyc generates objects that don't have a __dict__, but they
    # do have __getstate__ methods that will return an equivalent
    # dictionary
    if hasattr(g, "__dict__"):
        d = g.__dict__
    else:
        d = g.__getstate__()  # type:

# Generated at 2022-06-13 17:51:47.518386
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest
    from pprint import pprint

    g = Grammar()
    g.symbol2number = {'and': 278, 'not': 279, 'or': 280}
    g.number2symbol = {278: 'and', 279: 'not', 280: 'or'}
    g.states = [[[(1, 1), (2, 2)], [(2, 2), (3, 3), (4, 4)], [(1, 1), (2, 2)]]]

# Generated at 2022-06-13 17:51:57.780180
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def _test(x: int, y: int) -> int:
        return x + y

    g = Grammar()
    filepath = "./foo.pkl"
    g.dump(filepath)
    gg = Grammar()
    gg.load(filepath)
    assert gg.symbol2number == g.symbol2number
    assert gg.number2symbol == g.number2symbol
    assert gg.states == g.states
    assert gg.dfas == g.dfas
    assert gg.labels == g.labels
    assert gg.keywords == g.keywords
    assert gg.tokens == g.tokens
    assert gg.symbol2label == g.symbol2label
    assert gg.start == g.start
    # Test

# Generated at 2022-06-13 17:52:07.510451
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Create a simple Grammar and dump it to a file
    g = Grammar()
    g.symbol2number["STMT"] = 40
    g.number2symbol[40] = "STMT"
    g.states = [[[(1, 2), (3, 4)], [(2, 3)], [(3, 4)]]]
    g.dfas = {41: (g.states[0], {1: 1, 3: 1}), 40: ([], {})}
    g.labels = [
        (1, None),
        (2, None),
        (3, None),
        (4, None),
    ]
    g.start = 40
    g.keywords = {
        "class": 3,
        "pass": 2,
        "def": 1,
    }
    g.tok

# Generated at 2022-06-13 17:52:09.464762
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(test_Grammar_load.__code__.co_filename.rstrip("c"))

# Generated at 2022-06-13 17:52:14.172401
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.dump(os.path.join(os.path.dirname(__file__), 'Grammar.pkl'))

# Generated at 2022-06-13 17:52:24.005068
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver
    from . import tokenize, token

    gr = driver.load_grammar("Grammar.txt")
    gr.dump("Grammar.pickle")
    gr2 = Grammar()
    gr2.load("Grammar.pickle")
    # can compare the two reports, but it's rather lengthy
    # gr.report()
    # gr2.report()
    assert gr == gr2, "test_Grammar_dump"

    # make sure it's really round-tripping properly
    assert gr2.symbol2number == gr.symbol2number, "test_Grammar_dump"
    assert gr2.number2symbol == gr.number2symbol, "test_Grammar_dump"

# Generated at 2022-06-13 17:52:33.626874
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def create_instance():
        from . import pgen2

        return pgen2.driver.load_grammar(b"python-grammar-34.txt")

    def create_pkl(instance, path):
        with tempfile.NamedTemporaryFile(dir=os.path.dirname(path), delete=False) as f:
            pickle.dump(instance, f, pickle.HIGHEST_PROTOCOL)
        os.replace(f.name, path)

    def create_pkl_from_dump(instance, path):
        with tempfile.NamedTemporaryFile(dir=os.path.dirname(path), delete=False) as f:
            instance.dump(f)
        os.replace(f.name, path)

    def check_instance(instance1, instance2):
        assert instance

# Generated at 2022-06-13 17:52:44.173244
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import test_pgen

    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, "temp_grammar")
        test_g = test_pgen.Grammar(filename)

        test_g.dump(filename)
        with open(filename, "rb") as f:
            result = f.read()

# Generated at 2022-06-13 17:52:50.045709
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver
    from . import conv
    d = driver.Driver(grammar_file="Grammar.txt", output_dir="/tmp")
    d.generate_grammar()

    c = conv.Converter("Grammar.txt", "Grammar.pickle")
    c.generate_grammar()


# Generated at 2022-06-13 17:53:02.234144
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pgen2.pgen
    import pgen2._tokenize

    grammar = pgen2.pgen.Grammar()
    grammar.start = 3

# Generated at 2022-06-13 17:53:11.224745
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 256
    g.dfas = {256: ([], {}), 256: ([], {})}
    g.tokens = {"if": 1, "else": 2}
    g.keywords = {"name": 10}
    g.symbol2number = {"int": 1, "float": 2}
    g.number2symbol = {1: "int", 2: "float"}
    g.states = [
        [
            (0, 1),
            (1, 1),
            (2, 1),
        ],
        [(2, 0)],
    ]

# Generated at 2022-06-13 17:53:17.799578
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gr = Grammar()
    assert os.path.exists("Grammar.dump") == False
    gr.dump("Grammar.dump")
    assert os.path.exists("Grammar.dump") == True
    os.remove("Grammar.dump")
    assert os.path.exists("Grammar.dump") == False


# Generated at 2022-06-13 17:53:26.409816
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()

# Generated at 2022-06-13 17:53:31.119352
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Check that pickling succeeds
    grammar = Grammar()
    try:
        with tempfile.TemporaryDirectory() as dirname:
            grammar.dump(os.path.join(dirname, "temp.pickle"))
            grammar2 = Grammar()
            grammar2.load(os.path.join(dirname, "temp.pickle"))
    except Exception:
        assert False

# Generated at 2022-06-13 17:53:37.682954
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # from . import parser
    from . import pgen2

    def _generate_grammar(grammar_file: str) -> None:
        grammar = pgen2.driver.load_grammar(grammar_file)
        grammar.dump(grammar_file + ".dump")

    _generate_grammar(pgen2.pgen2.__file__)
    # _generate_grammar(parser.__file__)

# Generated at 2022-06-13 17:53:43.210812
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    test_file_name = "/tmp/test_Grammar_dump"
    grammar.dump(test_file_name)
    with open(test_file_name, "rb") as f:
        grammar_loaded = pickle.load(f)
    assert grammar.__dict__ == grammar_loaded
    os.remove(test_file_name)


# Generated at 2022-06-13 17:53:56.923156
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .tokens import NAME
    from .pgen2 import driver
    from .parse import Parser

    f = tempfile.NamedTemporaryFile(delete=False)
    g = driver.load_grammar()
    g.dump(f.name)
    h = g.copy()
    h.loads(open(f.name, "rb").read())
    os.remove(f.name)
    # compare grammars
    assert g.symbol2number == h.symbol2number
    assert g.number2symbol == h.number2symbol
    assert g.states == h.states
    assert g.dfas == h.dfas
    assert g.labels == h.labels
    assert g.keywords == h.keywords
    assert g.tokens == h.tokens
   

# Generated at 2022-06-13 17:54:02.330069
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .parse import Parser
    from .pgen2 import literals

    # This test could live in a different test file if it weren't
    # specific to the Grammar class's code.

    # In order to test dumping, we need to create a Grammar.  So
    # create a Parser and dump *that* grammar.
    p = Parser()
    fn = tempfile.mktemp()
    p.g.dump(fn)
    p2 = Parser()
    p2.g.load(fn)

    assert p.g == p2.g

    # Make sure the "literals" dict given to the parser is preserved.
    assert p2.g.number2symbol[257] == "and"
    assert 257 in p2.g.symbol2number
    assert 257 in p2.g.symbol2

# Generated at 2022-06-13 17:54:09.227481
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class FakeGrammar(Grammar):
        pass
    g = FakeGrammar()
    g.dump("/tmp/foo")
    with open("/tmp/foo", "rb") as f:
        fake_data = f.read()
    os.remove("/tmp/foo")
    g1 = FakeGrammar()
    g1.loads(fake_data)


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:54:16.531490
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import os
    import pickle
    import tempfile
    import unittest

    class GrammarDumpTests(unittest.TestCase):
        def setUp(self) -> None:
            self.grammar = Grammar()
            self.grammar.symbol2number = {"bob": 256, "fred": 257}
            self.grammar.number2symbol = {256: "bob", 257: "fred"}
            self.grammar.states = [[]]
            self.grammar.dfas = {256: (self.grammar.states[0], {})}
            self.grammar.labels = [("EMPTY", None)]
            self.grammar.keywords = {}
            self.grammar.tokens = {}
            self.grammar.symbol2label = {}
           

# Generated at 2022-06-13 17:54:23.621587
# Unit test for method load of class Grammar
def test_Grammar_load():
    import os
    import sys

    g = Grammar()
    g.symbol2number["sym"] = 256
    g.number2symbol[256] = "sym"

    # test load empty file
    g.load("empty.pkl")
    assert g.number2symbol == {"256": "sym"}
    os.remove("empty.pkl")

    # test load garbage string
    filename = "garbage.pkl"
    with open(filename, "w") as f:
        f.write("thisisnotapicklefile\n")
    try:
        g.load(filename)
    except Exception:
        pass
    else:
        raise AssertionError("load garbage string failed.")
    os.remove(filename)

    # test load non-existent file

# Generated at 2022-06-13 17:54:33.498771
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import pgen2
    from .pgen2 import pgen
    from .pgen2 import tokenize

    g = Grammar()
    g.load(pgen.find_module('python3') + '.pickle')

    # And some sanity checks...
    assert g.start == g.symbol2number['file_input']
    assert g.number2symbol[g.start] == 'file_input'
    assert g.number2symbol[g.symbol2number['xor_expr']] == 'xor_expr'

    firsts = set()
    for _, (first, _) in g.dfas[g.symbol2number['arglist']][1].items():
        firsts.update(first)
    assert firsts == set((token.NAME, token.STAR, token.POWER))

# Generated at 2022-06-13 17:54:43.506516
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Create dummy Grammar object
    g = Grammar()
    g.symbol2number = dict(a=42, b=37)

# Generated at 2022-06-13 17:54:45.573878
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    p = tempfile.NamedTemporaryFile(delete=False)
    g.dump(p.name)
    p.close()
    os.unlink(p.name)

# Generated at 2022-06-13 17:54:56.501055
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 256
    g.keywords = {}
    g.symbol2number = {"root": 256, "foo": 257}
    g.number2symbol = {256: "root", 257: "foo"}

# Generated at 2022-06-13 17:55:07.356679
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.start = 2
    g.labels.append(3)
    g.labels.append((1, "abc"))
    g.states.append([(1, 1), (2, 2)])
    g.states.append([(3, 3), (4, 4)])
    g.dfas[2] = (0, {"a": 1, "b": 1, "c": 1})
    g.dfas[3] = (1, {"d": 1, "e": 1, "f": 1})
    g.symbol2number["abc"] = 4
    g.number2symbol[4] = "abc"
    g.keywords["abc"] = 5
    g.tokens[6] = 7
    g.symbol2label["def"] = 8
    g

# Generated at 2022-06-13 17:55:11.893714
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Make sure mypyc bytecode works, too.
    from .conv import parse_grammar, convert_grammar, compile_grammar

    fname = "Grammar.test"
    for compile in [False, True]:
        parse_grammar(
            os.path.join(os.path.dirname(__file__), "Python.asdl"),
            fname,
            compile,
        )
        g = Grammar()
        g.load(fname)

# Generated at 2022-06-13 17:55:12.958859
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("/dev/null")

# Generated at 2022-06-13 17:55:20.383760
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

    filename = "Grammar.dump.pickle"

    g.dump(filename)

    # Load that file back into a new grammar
    g2 = Grammar()
    g2.load(filename)

    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.states == g2.states
    assert g.dfas == g2.dfas
    assert g.labels == g2.labels
    assert g.keywords == g2.keywords
    assert g.tokens == g2.tokens
    assert g.symbol2label == g2.symbol2label
    assert g.start == g2.start

# Generated at 2022-06-13 17:55:23.721963
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class AGrammar(Grammar):
        def __init__(self) -> None:
            super(AGrammar, self).__init__()
            self.symbol = 0
    grammar = AGrammar()
    grammar.dump(tempfile.NamedTemporaryFile(delete=False).name)

# Generated at 2022-06-13 17:55:27.193176
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    path = Path(__file__)
    path = path.parent / "GrammarTables/Grammar.pickle"

    grammar = Grammar()
    grammar.dump(path)


# Generated at 2022-06-13 17:55:37.757655
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen2 import driver
    from . import token, python_grammar_no_print_statement

    import os
    import tempfile
    from shutil import copy
    from . import token

    # Copy the grammar to a temporary file and read it
    with tempfile.TemporaryDirectory() as tmp:
        fn = os.path.join(tmp, 'python-Grammar_dump.grammar')
        with open(fn, 'wb') as f:
            f.write(python_grammar_no_print_statement)
        grammar = driver.load_grammar(fn)
        assert grammar.keywords == {'False': 257, 'None': 259, 'True': 258}
        assert grammar.symbol2number == {'file_input': 256, 'eval_input': 275, 'decorator': 276}

        #

# Generated at 2022-06-13 17:55:47.904624
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # This is a gross hack to get 100% code coverage for the Grammar
    # class.  The dump method deliberately does not call dump on any
    # its instance variables, but instead references its __dict__
    # directly.  To get the dump method to call dump on its instance
    # variables, we create a subclass of Grammar that has a
    # __getstate__ method instead of a __dict__.  This class is never
    # used for anything else.
    class GrammarWithNoDict(Grammar):
        def __getstate__(self):
            return {}

    # Write the grammar tables to a file.
    # Note:  We must use a valid path name that is guaranteed to be on
    # the filesystem.  Using a NamedTemporaryFile will not work, since
    # it will be deleted before it can be reopened by the Grammar.

# Generated at 2022-06-13 17:55:57.498341
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr = Grammar()
    gr.load("./test/data/parser/Grammar.pkl")
    assert gr.symbol2number == {'A': 256, 'B': 257, 'C': 258, 'D': 259, 'E': 260, 'F': 261, 'comma': 262, 'minus': 263}
    assert gr.number2symbol == {256: 'A', 257: 'B', 258: 'C', 259: 'D', 260: 'E', 261: 'F', 262: 'comma', 263: 'minus'}
    assert gr.states == [[(0, 1), (0, 2)], [(1, 2), (2, 3), (0, 3)]]

# Generated at 2022-06-13 17:56:05.118781
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    import os
    import sys
    if sys.version_info[0] == 2:
        import StringIO as io
    else:
        import io

    g = Grammar()
    g.symbol2number = {"key": "value"}
    g.number2symbol = {"key": "value"}
    g.states = [1, 2, 3]
    g.dfas = {4: 5}
    g.labels = [1, 2, 3]
    g.keywords = {"key": "value"}
    g.tokens = {4: 5}
    g.symbol2label = {"key": "value"}
    g.start = 256
    g.async_keywords = False

    f = io.BytesIO()
    g.dump(f)

# Generated at 2022-06-13 17:56:09.397805
# Unit test for method load of class Grammar
def test_Grammar_load():
    g: Grammar = Grammar()
    g.load('/Users/dave/work/python/cpython/3.7/Lib/idlelib/idle_test/grammar.pkl')
    print(g.dfas)


# Generated at 2022-06-13 17:56:17.878143
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import tokenize
    from typing import cast

    def helper(s: str) -> Tuple[int, str]:
        tok = next(tokenize.tokenize(s.encode()))
        return (cast(int, tok.type), tok.string)

    g = Grammar()
    assert g.tokens[helper("0")[0]] == g.keywords[helper("0")[1]]

    g.dump("Grammar.dump")
    g.load("Grammar.dump")
    assert g.tokens[helper("0")[0]] == g.keywords[helper("0")[1]]

    if os.path.exists("Grammar.dump"):
        os.remove("Grammar.dump")

# Generated at 2022-06-13 17:56:19.386792
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import doctest
    doctest.testmod()


# Generated at 2022-06-13 17:56:27.514377
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 1
    g.states = [[(1, 0)]]

# Generated at 2022-06-13 17:56:38.550874
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number["a"] = 1
    g.number2symbol[2] = "b"
    g.states = [[]]
    g.dfas[3] = ([], {})
    g.labels = [4]
    g.keywords["c"] = 5
    g.tokens[6] = 7
    g.symbol2label["d"] = 8
    g.start = 9
    filename = "test_Grammar_dump.pickle"

# Generated at 2022-06-13 17:56:43.131587
# Unit test for method load of class Grammar
def test_Grammar_load():
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "grammar.pkl")
        g = Grammar()
        g.dump(filename)
        g = Grammar()
        g.load(filename)
        g.dump(filename + "2")
        os.unlink(filename)
        os.unlink(filename + "2")

# Generated at 2022-06-13 17:56:52.480634
# Unit test for method load of class Grammar
def test_Grammar_load():
    # type: () -> None
    """Unit test for method load of class Grammar

    See also test_Grammar_loads.
    """
    import sys
    import tempfile
    from ._py_grammar import make_grammar

    # Write a temporary pickle file and load it.

    grammar = make_grammar()
    filename = tempfile.mktemp()
    grammar.dump(filename)
    new_grammar = Grammar()
    new_grammar.load(filename)

    # For each attribute determine if its values correspond.

    attrs = ["symbol2number", "number2symbol", "states", "dfas", "labels", "keywords", "tokens"]
    for attr in attrs:
        old_attr = getattr(grammar, attr)

# Generated at 2022-06-13 17:57:01.054397
# Unit test for method load of class Grammar
def test_Grammar_load():
    """

    """
    token = tokenize.tokenize(StringIO("def foo(): pass").readline)
    for toknum, tokval, _, _, _ in token:
        if toknum == token.NAME and tokval == 'def': break
        assert toknum != token.ENDMARKER, "Couldn't find 'def'"
    test_pkl = pickle.dumps((toknum, tokval))
    g = Grammar()
    assert g.tokens == {}
    g.loads(test_pkl)
    assert g.tokens == {toknum: 1}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 17:57:14.733602
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pygram import python_symbols as symbols

    g = Grammar()

    for sym, num in symbols.sym_name.items():
        name = sym.strip('"\'')
        g.symbol2number[name] = num
    for num, sym in symbols.sym_name.items():
        name = sym.strip('"\'')
        g.number2symbol[num] = name
    g.start = g.symbol2number["file_input"]

    fd, filename = tempfile.mkstemp()
    os.close(fd)
    try:
        g.dump(filename)
        g1 = Grammar()
        g1.load(filename)
        g1.report()
    finally:
        os.unlink(filename)

# Generated at 2022-06-13 17:57:34.131586
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def test_valid(g: Grammar):
        tmpfile = tempfile.NamedTemporaryFile()
        g.dump(tmpfile.name)
        g2 = Grammar()
        g2.loads(tmpfile.read())
        assert g.symbol2number == g2.symbol2number
        assert g.number2symbol == g2.number2symbol
        assert g.dfas == g2.dfas
        assert g.keywords == g2.keywords
        assert g.tokens == g2.tokens
        assert g.symbol2label == g2.symbol2label
        assert g.labels == g2.labels
        assert g.states == g2.states
        assert g.start == g2.start

# Generated at 2022-06-13 17:57:41.862942
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {'P': 256}
    grammar.number2symbol = {256: 'P'}
    grammar.states = []
    grammar.dfas = {}
    grammar.labels = [(1, 'p')]
    grammar.keywords = {}
    grammar.tokens = {}
    grammar.symbol2label = {}
    grammar.start = 256
    with tempfile.TemporaryFile(mode='w+b') as f:
        grammar.dump(f)
        f.seek(0)
        d = pickle.load(f)
    assert d['symbol2number'] == grammar.symbol2number
    assert d['number2symbol'] == grammar.number2symbol
    assert d['labels'] == grammar.labels

# Generated at 2022-06-13 17:57:43.511859
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.dump("")


# Generated at 2022-06-13 17:57:56.130693
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import re

# Generated at 2022-06-13 17:58:02.030983
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Unit test for method dump of class Grammar."""
    def test_dump(input: Any) -> None:
        """Test the dump method using pickle protocol 'input'."""
        g = Grammar()
        g.dump("/tmp/parserxxx")
        g.load("/tmp/parserxxx")

    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        test_dump(proto)

# Generated at 2022-06-13 17:58:03.634964
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    pass


# Generated at 2022-06-13 17:58:06.458372
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("/tmp/test.pkl")


# Generated at 2022-06-13 17:58:18.317649
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test Grammar.dump."""

    # Set up a Grammar instance for unit testing
    class GrammarSubclass(Grammar):
        def load_grammar(self):
            self.symbol2number = {"foo": 1, "bar": 2}
            self.number2symbol = {1: "foo", 2: "bar"}
            self.keywords = {"True": 1, "False": 2, "None": 3}
            self.states = [[(1, 2)], [(1, 3)]]
            self.start = 0
            self.dfas = {
                256: (
                    [(0, 1), (1, 2)],
                    {0: 1, 1: 2},
                )
            }
            self.labels = [(0, None), (1, None), (1, None)]

# Generated at 2022-06-13 17:58:28.273790
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle

    class DummyGrammar(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.s = "foo"
            self.l = [1, 2, 3]

    g = DummyGrammar()
    f = tempfile.NamedTemporaryFile(mode='wb', delete=False)
    g.dump(f.name)
    f.close()
    with open(f.name, 'rb') as f:
        d = pickle.load(f)
    os.unlink(f.name)
    assert d == {'l': [1, 2, 3], 's': 'foo'}



# Generated at 2022-06-13 17:58:32.157330
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import conv
    from .pgen import pgen

    gr = Grammar()
    c = conv()
    c.convert("Python.gram", gr)
    fn = "Python.pkl"
    gr.dump(fn)
    gr2 = pgen()
    if not os.path.exists(fn):
        raise ValueError("{} not found".format(fn))
    gr2.load(fn)
    os.unlink(fn)


# Generated at 2022-06-13 17:58:40.844451
# Unit test for method load of class Grammar
def test_Grammar_load():
    pickle_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Grammar.pickle")
    assert os.path.exists(pickle_path)
    g = Grammar()
    g.load(pickle_path)

# Generated at 2022-06-13 17:58:44.684177
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.dump(os.path.join(tempfile.gettempdir(), "test_grammar.pkl"))
    grammar = Grammar()
    grammar.load(os.path.join(tempfile.gettempdir(), "test_grammar.pkl"))
if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:58:46.042948
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .test.test_grammar import dump_as_pgen

    dump_as_pgen()

# Generated at 2022-06-13 17:58:48.891359
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .pgen import driver

    g = driver.load_grammar("Grammar.txt")
    filename = "Grammar.pkl"
    g.dump(filename)
    driver.dump_grammar(filename)
    if os.path.exists(filename):
        os.remove(filename)



# Generated at 2022-06-13 17:58:54.333482
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Given a grammar
    from .conv import Converter

    conv = Converter("Grammar.test")
    conv.convert()
    grammar = conv.grammar

    # When a file is dumped and re-loaded
    with tempfile.NamedTemporaryFile(delete=False) as f:
        grammar.dump(f.name)
    grammar2 = Grammar()
    grammar2.load(f.name)

    # Then the two grammars are identical

# Generated at 2022-06-13 17:58:58.398028
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    # 1. Dump pickle file before load test, since load accesses member variables
    with tempfile.NamedTemporaryFile() as f:
        g.dump(f)

    # 2. Restore g from pickle file
    g.load(f)


del opmap_raw

# Generated at 2022-06-13 17:59:03.610429
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    import io

    def test_one(pkl: bytes, cls: Any) -> None:
        d = pickle.loads(pkl)
        f = io.BytesIO()
        g = cls()
        g._update(d)
        g.dump(f)
        f.seek(0)
        g2 = cls()
        g2.load(f)
        assert g.symbol2number == g2.symbol2number
        assert g.number2symbol == g2.number2symbol
        assert g.states == g2.states
        assert g.dfas == g2.dfas
        assert g.labels == g2.labels
        assert g.keywords == g2.keywords
        assert g.tokens == g2.tokens

# Generated at 2022-06-13 17:59:14.582276
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = './Grammar.pickle'
    # - check if the file exists. If so, then we need to process it...
    if os.path.isfile(filename):
        f = open(filename, 'rb')
        # - load the Grammar from the pickle file
        g = Grammar()
        g.load(filename)
        # - print out the attributes for debugging...
        print('\n=== Grammar attributes ===')
        print('g.symbol2number:', g.symbol2number)
        print('g.number2symbol:', g.number2symbol)
        print('g.states:', g.states)
        print('g.dfas:', g.dfas)
        print('g.labels:', g.labels)

# Generated at 2022-06-13 17:59:26.289092
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Test dump() method of class Grammar

    The method Grammar.dump() dumps the grammar tables to a pickle file,
    so the loading of dump() is tested in test_Grammar_load().
    """
    g = Grammar()

    g.symbol2number = {'a': 1, 'b': 2}
    g.number2symbol = {1: 'a', 2: 'b'}
    g.states = [[(0, 0), (1, 1)], [(2, 2), (3, 3)]]
    g.dfas = {1: (g.states[0], {1: 1}), 2: (g.states[1], {2: 2})}
    g.labels = [(0, None), (1, None), (2, None), (3, None)]
    g.keywords

# Generated at 2022-06-13 17:59:31.172455
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    data = dict(symbol2number = {'foo': 100}, number2symbol = {100: 'foo'})
    data = pickle.dumps(data)
    g.loads(data)
    assert g.symbol2number['foo'] == 100
    assert g.number2symbol[100] == 'foo'