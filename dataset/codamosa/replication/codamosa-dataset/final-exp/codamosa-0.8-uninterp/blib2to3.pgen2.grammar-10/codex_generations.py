

# Generated at 2022-06-13 17:49:50.919750
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def test_pickle_dump(class_: Any) -> None:
        grammar = class_()
        with tempfile.TemporaryFile(mode="wb") as f:
            grammar.dump(f)

    test_pickle_dump(Grammar)

# Generated at 2022-06-13 17:49:55.933164
# Unit test for method load of class Grammar
def test_Grammar_load():
    # assert_raises(TypeError, Grammar().load, 1)
    g = Grammar()
    g.symbol2number = dict(a=1)
    g.dump(":memory:")
    g.symbol2number = dict(b=2)
    g.load(":memory:")
    assert g.symbol2number == dict(a=1)

# Generated at 2022-06-13 17:50:04.103156
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pickle
    from .conv import convert_grammar

    with open("Grammar/Grammar", "rb") as f:
        pgen = pickle.load(f)
    grammar = convert_grammar(pgen, True, False)
    grammar.start = 384
    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as f:
        grammar.dump(f.name)
    with open(f.name, "rb") as f:
        pickle.load(f)

    assert os.path.isfile(f.name)
    if os.path.isfile(f.name):
        os.remove(f.name)



# Generated at 2022-06-13 17:50:16.161311
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def gramcheck(gram: Grammar) -> None:
        assert gram.number2symbol == {256: "start", 257: "foo", 258: "bar"}
        assert gram.symbol2number == {"start": 256, "foo": 257, "bar": 258}
        assert gram.symbol2label == {"foo": 259, "bar": 260}
        assert gram.start == 256
        assert gram.state == [
            [(257, 257), (258, 258)]
        ]
        assert gram.keywords == {"foo": 259, "bar": 260}

    gram = Grammar()
    gram.number2symbol = {256: "start", 257: "foo", 258: "bar"}
    gram.symbol2number = {"start": 256, "foo": 257, "bar": 258}

# Generated at 2022-06-13 17:50:18.794362
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    grammar_path = os.path.join(os.path.dirname(__file__), "Grammar.txt")
    g.load(grammar_path)

# Generated at 2022-06-13 17:50:24.773572
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("../../Grammar/Grammar")
    assert isinstance(g.dfas, dict)
    assert isinstance(g.keywords, dict)
    assert isinstance(g.labels, list)
    assert isinstance(g.number2symbol, dict)
    assert isinstance(g.states, list)
    assert isinstance(g.symbol2label, dict)
    assert isinstance(g.symbol2number, dict)
    assert isinstance(g.tokens, dict)


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:50:27.504151
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    assert not hasattr(g, "symbol2number")
    g.load("test.pickle")


# Generated at 2022-06-13 17:50:31.315501
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    d = {'symbol2number': {'a': 256}, 'number2symbol': {256: 'a'}}
    g.load(d)
    assert (g.symbol2number == d['symbol2number'])
    assert (g.number2symbol == d['number2symbol'])

# Generated at 2022-06-13 17:50:41.674941
# Unit test for method load of class Grammar
def test_Grammar_load():
    def _check_load(pkl: bytes) -> None:
        g = Grammar()
        g.loads(pkl)
        assert g.symbol2number["foo"] == 1
        assert g.number2symbol[1] == "foo"
        assert g.labels[2][0] == 0


# Generated at 2022-06-13 17:50:46.899462
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Can't test loading of pickle file, but we can test that a file
    # gets written.  Note that this test is only capable of testing
    # one of the possible dumps, because the instance variables are
    # populated by subclasses, not here.  But the dump method doesn't
    # care about the contents.
    g = Grammar()
    g.dump("test_Grammar.dump")
    g.dump("test_Grammar_2.dump")


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:50:51.550520
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Set up
    filename = "grammar.txt"
    g = Grammar()
    g.dump(filename)
    # Test
    g.load(filename)
    # Clean up
    os.remove(filename)


# Generated at 2022-06-13 17:51:00.984389
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import tempfile
    import unittest
    import pytest

    from ..conv import convert

    class GrammarDumpTests(unittest.TestCase):
        """Unit tests for method dump of class Grammar."""

        def setUp(self):
            self.pickle_file = os.path.join(tempfile.gettempdir(),
                                            "test_pgen_grammar_pickle_dump.pkl")
            g = convert(open("Grammar/Grammar"))
            g.dump(self.pickle_file)

        def tearDown(self):
            if os.path.exists(self.pickle_file):
                os.remove(self.pickle_file)


# Generated at 2022-06-13 17:51:03.431919
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.start = 42
    g.dump(os.devnull)
    h = Grammar()
    h.load(os.devnull)
    assert g.start == h.start

# Generated at 2022-06-13 17:51:06.590430
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Unit test for method load of class Grammar"""
    g = Grammar()
    g.load("Grammar.txt")  # this file is unused, but needed for mypy
    assert g.start == 256

# Generated at 2022-06-13 17:51:15.266399
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class MyGrammar(Grammar):
        def __init__(self):
            Grammar.__init__(self)
            self.foo = 1
            self.bar = "a"

    mg = MyGrammar()
    try:
        mg.dump("mysettings.pickle")
        mg2 = MyGrammar()
        mg2.load("mysettings.pickle")
    finally:
        os.remove("mysettings.pickle")
    assert mg.foo == mg2.foo
    assert mg.bar == mg2.bar

# Generated at 2022-06-13 17:51:24.375851
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {'Module': 256, 'stmt': 272}
    grammar.number2symbol = {256: 'Module', 272: 'stmt'}
    grammar.states = [[[(0, 0)]]]
    grammar.dfas = {
        272: ([[(0, 0)]], {256: 1}),
    }
    grammar.labels = [
        (0, ''),
        (0, 'stmt'),
        (1, 'Module'),
    ]
    grammar.keywords = {}
    grammar.tokens = {}
    grammar.start = 256
    grammar.symbol2label = {
        'Module': 1,
        'stmt': 2,
    }
    g = Grammar()

# Generated at 2022-06-13 17:51:31.641218
# Unit test for method load of class Grammar
def test_Grammar_load():
    """
    This tests the Grammar.load method.
    """
    from typing import cast

    g = Grammar()
    g.symbol2number = {"foo": 0}
    name = tempfile.mktemp()
    g.dump(name)
    h = Grammar()
    h.load(name)
    assert g.symbol2number == cast(Dict[str, int], h.symbol2number)
    os.remove(name)


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:51:36.427981
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class MyGrammar(Grammar):
        pass

    g = MyGrammar()
    g.dfas[1] = ([[()]], {0: 0})
    with tempfile.NamedTemporaryFile(mode="w+b", suffix=".pickle") as f:
        g.dump(f.name)
        f.seek(0)
        g2 = MyGrammar()
        g2.load(f.name)
        assert g2.dfas == g.dfas

# Generated at 2022-06-13 17:51:43.923740
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = "test_load.pkl"

    g = Grammar()
    g.symbol2number["symbol1"] = 1
    g.symbol2number["symbol2"] = 2
    g.number2symbol[1] = "symbol1"
    g.number2symbol[2] = "symbol2"
    g.states = [
        [
            [(256, 0), (257, 1)],
            [(257, 2)],
            [(0, 3)],
            [(258, 4)],
            [(0, 3)],
        ]
    ]
    g.dfas = {1: (g.states[0], {1: 1, 257: 1}), 2: (g.states[0], {2: 1})}

# Generated at 2022-06-13 17:51:49.065274
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.number2symbol = {"number" : 1}
    temp = tempfile.mktemp()
    g.dump(temp)
    with open(temp, "rb") as f:
        d = pickle.load(f)
    assert d == {"number2symbol" : {"number" : 1}}



# Generated at 2022-06-13 17:52:03.965342
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = os.path.join(os.path.dirname(__file__), "Grammar.pickle")
    try:
        with open(filename, "rb") as f:
            d = pickle.load(f)
    except OSError as e:
        print("Can't find or read file '{}': {}".format(filename, e))
        return
    for k, v in d.items():
        if k not in ("start", "async_keywords"):
            assert hasattr(Grammar, k), "Grammar is missing attribute {}".format(k)
    d["start"] = 256
    d["async_keywords"] = False
    g = Grammar()
    g.load(filename)

# Generated at 2022-06-13 17:52:10.889681
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import unittest
    # Make sure that dumping a grammar works.
    class DumpTester(unittest.TestCase):
        def test_dump(self):
            g = Grammar()
            g.labels.extend([(token.NUMBER, "NUMBER"), (token.NAME, "NAME")])
            g.states.append(
                [
                    [
                        (g.symbol2label["NAME"], 0),
                        (g.symbol2label["NUMBER"], 0),
                        (0, 0),
                    ]
                ]
            )
            g.symbol2number["foo"] = 1
            g.number2symbol[1] = "foo"
            g.tokens[token.PLUS] = 0

            out = io.BytesIO()
            g.dump(out)

# Generated at 2022-06-13 17:52:21.458803
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import shutil
    import tempfile

    def test_data(filename, data):
        g = Grammar()
        fd, path = tempfile.mkstemp()
        os.close(fd)
        try:
            g.loads(data)
            g.dump(path)
            with open(path, 'rb') as fp:
                assert fp.read() == data
        finally:
            try:
                os.unlink(path)
            except OSError:
                pass

    tempdir = tempfile.mkdtemp()
    filename = tempfile.mktemp(dir=tempdir)

# Generated at 2022-06-13 17:52:30.420384
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {"NEWLINE": 256}
    grammar.number2symbol = {256: "NEWLINE"}
    grammar.states = [None, []]
    grammar.dfas = {256: (None, {})}
    grammar.labels = [None, ("a", "b"), (256, None)]
    grammar.keywords = {"None": 1, "True": 2}
    grammar.tokens = {token.ENDMARKER: 1, token.NAME: 2}
    grammar.symbol2label = {"NEWLINE": 256}
    grammar.start = 256
    grammar.async_keywords = False

    grammar.dump(tempfile.mktemp())

# Generated at 2022-06-13 17:52:33.849975
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """Unit test for method dump of class Grammar"""
    import os
    import tempfile

    tempfile.tempdir = os.getcwd()
    f = open(tempfile.mktemp(".pickle"), "wb")
    g = Grammar()
    g.dump(f)
    g.dump(tempfile.mktemp(".pickle"))

# Generated at 2022-06-13 17:52:40.799050
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest
    from .pgen2 import driver

    gram = driver.load_grammar(pytest.PLY_GRAMMAR)
    gram.dump(pytest.PLY_GRAMMAR + ".dump")

    gram2 = Grammar()
    gram2.load(pytest.PLY_GRAMMAR + ".dump")

    def test_eq(a, b):
        if a != b:
            raise AssertionError('%r != %r' % (a, b))

    test_eq(gram.symbol2number, gram2.symbol2number)
    test_eq(gram.number2symbol, gram2.number2symbol)
    test_eq(gram.dfas, gram2.dfas)
    test_eq(gram.keywords, gram2.keywords)
    test_

# Generated at 2022-06-13 17:52:52.206783
# Unit test for method load of class Grammar
def test_Grammar_load():
    p = Grammar()
    p.loads(EMPTY_Grammar_pkl)



# Generated at 2022-06-13 17:53:03.563388
# Unit test for method load of class Grammar
def test_Grammar_load():
    import ast
    import contextlib
    import io
    import os
    import shutil
    import sys
    from .pgen2 import driver

    def _make_grammar(self):
        driver.make_grammar(self)

    args = ["", "-o", "/tmp/test_Grammar_load"]
    tmp_path = args[-1]

    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)
    with contextlib.ExitStack() as stack:
        grammar_path = os.path.join(tmp_path, "Grammar.txt")

# Generated at 2022-06-13 17:53:12.383495
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2
    from . import conv
    from .parse import ParseError
    gram = conv.convert(pgen2.main())
    gram.dump('test_Grammar_dump.pkl')
    gram = Grammar()
    gram.load('test_Grammar_dump.pkl')
    assert(gram.number2symbol[gram.start] == 'file_input')
    assert(gram.labels[0][1] == 'EMPTY')
    assert(gram.keywords['from'] == 1101)
    assert(gram.keywords['finally'] == 1105)
    assert(gram.labels[1105][1] == 'finally')
    assert(gram.tokens[token.NEWLINE] == 1021)

# Generated at 2022-06-13 17:53:23.959555
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import lark_configs
    # This test is written from an interactive session, without any
    # intention to be robust or to test corner cases.

    class TestGrammar(Grammar):
        pass

    test_grammar = TestGrammar()
    test_grammar.loads(lark_configs.config_ast.pgen_grammar)
    assert type(test_grammar) == TestGrammar
    assert len(test_grammar.states) > 0
    assert len(test_grammar.dfas) > 0
    assert len(test_grammar.labels) > 0
    assert test_grammar.dfas[300][1] == 'single_input'
    assert test_grammar.dfas[300][0][0][0] == 1
    assert test_grammar.labels

# Generated at 2022-06-13 17:53:44.124040
# Unit test for method load of class Grammar
def test_Grammar_load():
    def test_Grammar_load():
        grammar = Grammar()
        small_grammar_pickle_file = os.path.join(
            os.path.dirname(__file__), "../Lib/test/small_grammar.pickle"
        )
        with open(small_grammar_pickle_file, "rb") as f:
            grammar.loads(f.read())


# Generated at 2022-06-13 17:53:49.713603
# Unit test for method load of class Grammar
def test_Grammar_load():
    class A(object):
        pass
    a = A()
    a.x = 1
    g = Grammar()
    g._update({'a':a})
    assert g.a.x == 1
    assert not hasattr(g.a, 'y')

if __name__ == "__main__":
    g = Grammar()
    g.report()

# Generated at 2022-06-13 17:54:00.293932
# Unit test for method load of class Grammar
def test_Grammar_load():
    obj = Grammar()
    assert obj.symbol2number == {}
    assert obj.number2symbol == {}
    assert obj.states == []
    assert obj.dfas == {}
    assert obj.labels == [(0, "EMPTY")]
    assert obj.keywords == {}
    assert obj.tokens == {}
    assert obj.symbol2label == {}
    assert obj.start == 256
    assert obj.async_keywords == False
    try:
        obj.load(b'UNUSED_VALUE')
    except TypeError:
        pass
    else:
        assert False, 'TypeError not raised'
    try:
        obj.load(b'UNUSED_VALUE')
    except SyntaxError:
        pass
    else:
        assert False, 'SyntaxError not raised'
   

# Generated at 2022-06-13 17:54:10.288598
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr = Grammar()
    gr.load(os.path.join(os.path.dirname(__file__), 'Grammar.txt'))
    assert len(gr.symbol2number) == 258
    assert len(gr.number2symbol) == 258
    assert len(gr.states) == 1
    assert gr.states[0][0][0][0] in [256, 259]
    assert gr.start == 256
    assert type(gr.states) == list
    assert type(gr.keywords) == dict
    assert type(gr.tokens) == dict
    assert type(gr.symbol2label) == dict
    assert type(gr.labels[0]) == tuple

# Generated at 2022-06-13 17:54:13.043422
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    b = g.dumps()
    g = Grammar()
    g.loads(b)

# Generated at 2022-06-13 17:54:22.027699
# Unit test for method dump of class Grammar
def test_Grammar_dump():

    def t(filename, table):

        grammar = Grammar()
        for k, v in table.items():
            setattr(grammar, k, v)
        d = grammar.dump(filename)
        assert d == None
        g = Grammar()
        g.load(filename)
        os.unlink(filename)
        for k, v in table.items():
            if getattr(g, k) != v:
                print("t:", k, getattr(g, k))
        #assert g.symbol2number == table['symbol2number']
        #assert g.number2symbol == table['number2symbol']
        #assert g.keywords == table['keywords']
        #assert g.tokens == table['tokens']
        #assert g.symbol2label == table['symbol

# Generated at 2022-06-13 17:54:23.550462
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.pkl")

# Generated at 2022-06-13 17:54:33.422693
# Unit test for method load of class Grammar
def test_Grammar_load():
    def do_test(test_name, file_name):
        grammar_tables_2_7 = Grammar()
        grammar_tables_2_7.load(file_name)
        assert not grammar_tables_2_7.async_keywords
        copy_2_7 = grammar_tables_2_7.copy()
        assert not copy_2_7.async_keywords

        grammar_tables_3_8 = Grammar()
        grammar_tables_3_8.load(file_name)
        assert grammar_tables_3_8.async_keywords
        copy_3_8 = grammar_tables_3_8.copy()
        assert copy_3_8.async_keywords


# Generated at 2022-06-13 17:54:43.517777
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def get_tokens(t: Text) -> List[int]:
        from .tokenize import generate_tokens_non_async

        return [token for (tok, _, _, _, _, _) in generate_tokens_non_async(t)]

    def check(t: Text, p: List[int]) -> None:
        assert get_tokens(t) == p

    def check_errors(t: Text, p: List[int]) -> None:
        try:
            tokens = get_tokens(t)
        except Exception:
            pass
        else:
            assert tokens == p

    # The behavior of the tokenizer is tested in test_tokenize.

# Generated at 2022-06-13 17:54:45.320206
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = os.path.join(os.path.dirname(__file__), "Grammar.txt")
    assert os.path.isfile(filename)


# Generated at 2022-06-13 17:55:04.085106
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load("Python-2.7.3/Grammar/Grammar")

# Generated at 2022-06-13 17:55:18.218647
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gram = Grammar()
    gram.symbol2number = {"foo": 1, "bar": 2}
    gram.number2symbol = {1: "foo", 2: "bar"}
    gram.states = [[[(1, 1)], [(0, 2)]]]
    gram.dfas = {1: gram.states[0], 2: gram.states[0]}
    gram.labels = [(0, "EMPTY"), (1, None), (0, None)]
    gram.start = 256
    gram.keywords = {"foo": 1, "bar": 2}
    gram.tokens = {1: 3, 2: 4}
    gram.symbol2label = {"foo": 1, "bar": 2}

    gram.dump()

# Generated at 2022-06-13 17:55:27.113994
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class TestGrammar(Grammar):
        def __init__(self, filename: Path) -> None:
            super().__init__()
            self.filename = filename

        def dump(self, filename: Path) -> None:
            raise FileExistsError("Unable to write to " + filename)

    # Test dumping to a file that doesn't exist
    test_grammar = TestGrammar("test_grammar")
    test_grammar.dump("test_file")

    # Test dumping to a file that already exists
    test_grammar = TestGrammar("test_grammar")
    # noinspection PyTypeChecker
    try:
        test_grammar.dump("test_grammar")
    except FileExistsError:
        pass



# Generated at 2022-06-13 17:55:37.720200
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # function _make_grammar_dump_test_data
    grammar = Grammar()
    grammar.symbol2number = {'STRING%': 9, 'testrule': 0, 'testrule2': 1, 'expr': 2}
    grammar.number2symbol = {0: 'testrule', 1: 'testrule2', 2: 'expr'}

# Generated at 2022-06-13 17:55:47.815289
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickle
    from types import MethodType
    from .conv import Conv
    from .pgen import Pgen

    # Test basic structure
    g = Pgen()
    g.make_grammar()
    g.dump("test_grammar")
    g2 = Grammar()
    g2.load("test_grammar")
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.states == g2.states
    assert g.dfas == g2.dfas
    assert g.labels == g2.labels
    assert g.start == g2.start
    assert g.keywords == g2.keywords
    assert g.tokens == g2.tokens
    assert g.symbol2label

# Generated at 2022-06-13 17:55:57.417761
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2
    from . import tokenize

    def test_tokenize_pgen(s: str) -> Tuple[bool, str]:
        """Check that tokenize and pgen generate identical results."""
        tokens1 = list(tokenize.generate_tokens(s.__iter__().__next__))
        tokens2 = list(pgen2.tokenize(s.__iter__().__next__))
        if tokens1 != tokens2:
            print(tokens1)
            print(tokens2)
            return False, "tokenize and pgen tokenize differently"
        else:
            return True, ""

    def test_pgen_parse(s: str) -> Tuple[bool, str]:
        """Check that pgen and parse generate identical results."""
        tree1 = pgen2

# Generated at 2022-06-13 17:56:09.135079
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Test the Grammar load method"""

    grammar = Grammar()
    grammar.load("./parsing/Grammar.pickle")
    assert grammar.states == [[(258, 1)], [(0, 1)], [(260, 3), (259, 2), (0, 2)], [(0, 3)]]
    assert grammar.number2symbol[256] == "file_input"
    assert grammar.number2symbol[265] == "decorator"

# Generated at 2022-06-13 17:56:16.506308
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import conv, pgen
    pth = pgen.import_module("parser", "graminit.c")

    g = Grammar()
    g.load(pth)
    assert len(g.symbol2number) >= 52
    assert len(g.number2symbol) >= 52
    assert len(g.states) >= 572

    g = Grammar()
    conv.make_pgen_grammar(g, pth)
    assert len(g.symbol2number) >= 52
    assert len(g.number2symbol) >= 52
    assert len(g.states) >= 572

# Generated at 2022-06-13 17:56:25.331964
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import sys
    import re
    import unittest

    class TestGrammarDump(unittest.TestCase):
        def test_Grammar_dump(self):
            g = Grammar()
            g.dump(sys.modules[__name__].__file__ + "c")
            with open(sys.modules[__name__].__file__ + "c", "r", encoding="utf_8") as f:
                nf = re.sub(r"\b(dump|load)[(][^)]*[)]", "", f.read())
            with open(sys.modules[__name__].__file__, "r", encoding="utf_8") as f:
                of = re.sub(r"\b(dump|load)[(][^)]*[)]", "", f.read())

# Generated at 2022-06-13 17:56:27.112190
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pytest

    d_org = Grammar()
    d_new = Grammar()

    with pytest.raises(TypeError):
        # Grammar.dump() takes 1 positional argument but 2 were given
        d_org.dump(d_new)

# Generated at 2022-06-13 17:57:02.053892
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class G(Grammar):
        def __init__(self, *args, **kwds):
            super().__init__(*args, **kwds)
    g = G()
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    g.dump(f.name)
    g.load(f.name)
    os.remove(f.name)

# Generated at 2022-06-13 17:57:16.160838
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import parse_grammar
    from .pgen import driver
    from .reindent import reindent

    # This is a test for method load of class Grammar

    # The following grammar is a slightly modified version of the one
    # for Python 2.4


# Generated at 2022-06-13 17:57:18.921162
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io, os

    g = Grammar()
    g.dump(io.BytesIO())
    g.dump(os.devnull)



# Generated at 2022-06-13 17:57:26.481075
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {"key1": 1, "key2": 2}
    g.number2symbol = {1: "key1", 2: "key2"}
    g.states = [[(1, 0)]]
    g.dfas = {1: ([[(1, 0), (2, 0)]], {}), 2: ([[(1, 0), (2, 0)]], {})}
    g.labels = [(3, "label3"), (4, "label4"), (5, "label5")]
    g.keywords = {"label3": 3, "label4": 4}
    g.tokens = {3: 3, 4: 4, 5: 5}
    g.symbol2label = {"symbol1": 3, "symbol2": 4}
    g

# Generated at 2022-06-13 17:57:36.171067
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pickle
    from _pickle import UnpicklingError
    from io import BytesIO

    for proto in range(pickle.DEFAULT_PROTOCOL, pickle.HIGHEST_PROTOCOL + 1):
        gram = Grammar()
        pickled_gram = pickle.dumps(gram, proto)

        gram.load(BytesIO(pickled_gram))
        gram.loads(pickled_gram)

        # test for unpickling errors
        for error in UnpicklingError, AttributeError, ImportError:
            try:
                pickle.loads(pickled_gram, encoding="bytes", errors=error)
            except Exception as exc:
                assert isinstance(exc, error)


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:57:37.613052
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import grammar

    g = Grammar()
    g.load(grammar)

# Generated at 2022-06-13 17:57:44.208572
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest
    from io import BytesIO
    from pprint import pprint

    class TestCase(unittest.TestCase):
        def test(self):
            with open("Grammar.pickle", "rb") as f:
                pkl = f.read()
            # Avoid writing files by pickling into a StringIO object
            f = BytesIO(pkl)
            g = Grammar()
            g.loads(pkl)
            # mypyc generates objects that don't have a __dict__, but
            # they do have __getstate__ methods that will return an
            # equivalent dictionary
            if hasattr(g, "__dict__"):
                d = g.__dict__
            else:
                d = g.__getstate__()  # type: ignore

# Generated at 2022-06-13 17:57:57.694742
# Unit test for method load of class Grammar
def test_Grammar_load():
    import ast
    import traceback
    import io
    import unittest

    def get_structure(g: Grammar) -> str:
        structure = " ".join(
            list(
                map(
                    lambda arg: arg + ": " + str(getattr(g, arg)),
                    [
                        "symbol2number",
                        "number2symbol",
                        "states",
                        "dfas",
                        "labels",
                        "keywords",
                        "tokens",
                        "symbol2label",
                        "start",
                        "async_keywords",
                    ],
                )
            )
        )
        return structure


# Generated at 2022-06-13 17:57:59.975937
# Unit test for method load of class Grammar
def test_Grammar_load():
    class DummyGrammar(Grammar):
        pass
    DummyGrammar().load(__file__)

# Generated at 2022-06-13 17:58:16.223845
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Check that we can load an AST grammar.
    # We don't need the result of the load, just a check that it doesn't crash.
    basepath = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
    ast_grammar_path = (
        os.path.join(basepath, "Lib", "ast.pkl")
        if os.path.exists(os.path.join(basepath, "Lib", "ast.pkl"))
        else os.path.join(basepath, "Grammar", "Grammar")
    )
    g = Grammar()
    g.load(ast_grammar_path)

# Generated at 2022-06-13 17:59:00.751429
# Unit test for method load of class Grammar
def test_Grammar_load():
  """Test for method load.
     
         This function creates a subclass TempGrammar, creates an
         object of TempGrammar, runs dump on the instance of the
         subclass and then loads that file and checks to make sure
         the same grammar is loaded.
         
         Args:
             None
         Returns:
             None
         Raises:
             None
         """
  gram = Grammar()
  TempClass = type("TempGrammar", Grammar.__bases__, dict(Grammar.__dict__))
  tempGram = TempClass()
  tempGram.dump("test.pickle")
  gram.load("test.pickle")
  assert gram.symbol2number == tempGram.symbol2number
  assert gram.number2symbol == tempGram.number2symbol

# Generated at 2022-06-13 17:59:03.551563
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    import pickle
    g.loads(pickle.dumps({"symbol2number": {}, "number2symbol": {}, "states": [], "dfas": {}, "labels": [(0, "EMPTY")], "keywords": {}, "tokens": {}, "symbol2label": {}, "start": 256, "async_keywords": False}))

# Generated at 2022-06-13 17:59:07.453935
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load("Grammar.txt")


if __name__ == "__main__":
    test_Grammar_load()

# Generated at 2022-06-13 17:59:17.112022
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert g.states == []
    assert g.dfas == {}
    assert g.labels == [(0, "EMPTY")]
    assert g.keywords == {}
    assert g.tokens == {}
    assert g.symbol2label == {}
    assert g.start == 256

    g.dump("./test_grammar.pickle")
    g = Grammar()
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert g.states == []
    assert g.dfas == {}
    assert g.labels == [(0, "EMPTY")]
    assert g.keywords == {}
    assert g.tokens == {}

# Generated at 2022-06-13 17:59:28.581724
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:59:31.906502
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("test_Grammar_dump")


if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:59:37.357790
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import mypy.parse
    import tempfile

    with tempfile.TemporaryFile() as f:
        mypy.parse.Grammar().dump(f)
        f.seek(0)
        try:
            mypy.parse.Grammar().load(f)
        except AttributeError as e:
            assert False, "loading dumped grammar failed: %s" % e