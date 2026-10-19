

# Generated at 2022-06-13 18:03:09.992041
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    pg.gettoken = lambda : None
    pg.value = "a"

    # Test: normal case
    pg.parse_atom = lambda : (None, None)
    result = pg.parse_alt()
    assert result == (None, None)

    # Test: case where parse_item is called more than once
    def parse_atom_side_effect(*args, **kwargs):
        # This function returns the second item in a tuple of length 2
        # when called the first time and the first item in a tuple of
        # length 2 when called the second time. It raises an
        # IndexError when called a third or subsequent time.
        parse_atom_side_effect.count += 1
        return (None, None)[parse_atom_side_effect.count - 1]

    parse_atom_side

# Generated at 2022-06-13 18:03:20.641975
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    def do_test(pg, expected):
        try:
            pg.raise_error("test %s %s", 1, 2)
        except SyntaxError as exc:
            exc_msg, exc_pos = exc.args
            assert exc_msg == expected
            assert exc_pos == (
                "foo",
                3,
                4,
                "if True:\n"
                "    raise NotImplementedError\n"
                "    while True:\n"
            )
        else:
            assert False, "did not raise SyntaxError"

    pg = ParserGenerator(
        None,
        """\
if True:
    raise NotImplementedError
    while True:
""",
        "foo",
    )
    for i in range(4):
        pg.gettoken()
    do_test

# Generated at 2022-06-13 18:03:28.994737
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    r"""Test case for method make_grammar of class ParserGenerator.

    This test is taken from Python's Grammar/Grammar and augmented with
    some further lines.
    
    """
    # Method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:03:33.808190
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    from blib2to3.pgen2.driver import save_grammar
    g = PgenGrammar()
    g.load_file(os.getenv("PYTHON_GRAMMAR"))
    save_grammar(g, "g_output.pickle")



# Generated at 2022-06-13 18:03:41.793735
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    import unittest
    from StringIO import StringIO

    class TestCase(unittest.TestCase):
        def test_empty(self):
            g = ParserGenerator(StringIO(""))
            g.gettoken()
            self.assertEqual(g.type, token.ENDMARKER)

        def test_comment(self):
            g = ParserGenerator(StringIO("# comment\n"))
            g.gettoken()
            self.assertEqual(g.type, token.ENDMARKER)

        def test_newline(self):
            g = ParserGenerator(StringIO("\n"))
            g.gettoken()
            self.assertEqual(g.type, token.ENDMARKER)


# Generated at 2022-06-13 18:03:52.033842
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    import pgen2.tokenize
    import io
    import token

    def make_tokenizer(input: str) -> Iterator[Token]:
        return pgen2.tokenize.generate_tokens(io.StringIO(input).readline)

    pg = ParserGenerator()
    a, z = pg.parse_rhs(make_tokenizer("foo"))
    assert a.arcs == [(None, z)]
    assert z.arcs == [("foo", z)]
    a, z = pg.parse_rhs(make_tokenizer(
        "foo | bar"
    ))
    assert a.arcs == [("foo", z), ("bar", z)]
    assert z.arcs == [(None, a)]

# Generated at 2022-06-13 18:04:01.929164
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from io import StringIO
    from tokenize import generate_tokens, COMMENT
    parser = ParserGenerator()

    s = StringIO("a: b c\n")
    parser.generator = (
        tup for tup in generate_tokens(s.readline) if tup[0] not in (COMMENT, tokenize.NL)
    )
    parser.gettoken()
    parser.expect(token.NAME)
    parser.expect(token.OP, ":")
    parser.expect(token.NAME, "b")
    parser.expect(token.NAME, "c")
    parser.expect(token.NEWLINE)

    s = StringIO("a: b c\n")

# Generated at 2022-06-13 18:04:11.481521
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pg = ParserGenerator()
    a = [DFAState({NFAState()}, False)]
    a[0].addarc(a[0], "a")
    pg.simplify_dfa(a)
    assert a[0].arcs == {"a": a[0]}

    a = [DFAState({NFAState()}, False)]
    a[0].addarc(a[0], "a")
    a[0].addarc(a[0], "b")
    b = [DFAState({NFAState()}, False)]
    b[0].addarc(b[0], "a")
    b[0].addarc(b[0], "b")
    a.append(b[0])
    b.append(a[0])
    pg.simplify_dfa(a)

# Generated at 2022-06-13 18:04:15.171284
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    """Unit test for constructor of class PgenGrammar"""
    test_grammar = PgenGrammar()
    assert test_grammar.start == None
    assert test_grammar.keywords == {}
    assert test_grammar.tokens == []
    assert test_grammar.dfas == {}
    assert test_grammar.parsing_table == None
    assert test_grammar.error_func == None


# Generated at 2022-06-13 18:04:20.950840
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    global __name__
    __name__ = "__main__"
    import sys
    import ast
    import io
    import traceback
    import inspect
    import os
    import astor
    import pprint
    import tokenize
    import token
    import keyword
    import grammar
    import symbol
    import pgen
    import re
    import parser
    import py_compile
    import runpy
    import pickle
    import pyclbr
    import filecmp
    import unittest
    import unittest.mock
    import contextlib
    import sqlite3
    import test

    pg = pgen.pgen()
    c = pg.converter

    # initialize c.labels

# Generated at 2022-06-13 18:04:54.549197
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator()
    dfa = [DFAState({}, None), DFAState({}, None)]
    pg.dump_dfa("test", dfa)


# Generated at 2022-06-13 18:05:01.140557
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    pg = ParserGenerator()
    pg.generator = iter([(tokenize.NAME, "rule", (1, 0), (1, 4), "rule\n")])
    pg.gettoken()
    assert pg.type == tokenize.NAME
    assert pg.value == "rule"
    assert pg.begin == (1, 0)
    assert pg.end == (1, 4)
    assert pg.line == "rule\n"



# Generated at 2022-06-13 18:05:08.392056
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    import io
    import tokenize
    import logging
    import sys
    import doctest
    import unittest
    import importlib.util
    import sysconfig
    import types
    import unittest.mock as mock
    import importlib.machinery as mach
    import tempfile

    from . import parser_driver

    logger = logging.getLogger(__name__)

    import_name = "tests.test_grammar"
    package_name = __name__
    module_name = "test_grammar"

    def parse(s):
        global _tokgen
        _tokgen = tokenize.generate_tokens(io.BytesIO(s.encode("utf-8")).readline)
        parser = ParserGenerator()
        return parser.parse()


# Generated at 2022-06-13 18:05:09.952086
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.calcfirst("test")
    assert pg.first["test"] is None, pg.first["test"]


# Generated at 2022-06-13 18:05:22.465659
# Unit test for method __eq__ of class DFAState
def test_DFAState___eq__():
    # "Python"(r'"[^"]*"' | r"'[^']*'" | '(' NAME ')' | NAME)
    n1 = NFAState()
    n2 = NFAState()
    n3 = NFAState()
    n4 = NFAState()
    n5 = NFAState()
    n6 = NFAState()
    n1.addarc(n2)
    n2.addarc(n3)
    n3.addarc(n4, "\"[^\"]*\"")
    n3.addarc(n5, "'[^']*'")
    n3.addarc(n6, "NAME")
    n4.addarc(n6)
    n5.addarc(n6)
    # Now, n1...n6 are wired together.  Create two equivalent states


# Generated at 2022-06-13 18:05:34.288859
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pg = PgenGrammar()
    # test for __init__
    assert pg
    # test for 'start' property
    assert not pg.start
    # test for 'dict' property
    assert pg.dict == {}

# Generated at 2022-06-13 18:05:45.315593
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    import re
    import sys
    def do_test(rule, result):
        print("Testing %r" % rule)
        pg = ParserGenerator()
        pg.add_rhs(rule)
        pg.gettoken()
        a, z = pg.parse_rhs()
        pg.dump_nfa('', a, z)

        # print("NFA:")
        # pg.dump_nfa('', a, z)
        # print("DFA:")
        # pg.dump_dfa('', pg.make_dfa(a, z))

        assert a.arcs == result

    do_test("a", [(1, 'a', 2)])
    do_test("a b", [(1, 'a', 2), (2, 'b', 3)])

# Generated at 2022-06-13 18:05:56.341951
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    from . import pytoken
    from .pytoken import generate_tokens

    def _test_dump(src: str, expected: str) -> None:
        parser = ParserGenerator()
        parser.setup(generate_tokens(pytoken.StringIO(src).readline), "test.py")
        parser.parse()
        parser.addfirstsets()
        dfa = parser.dfas["root"]
        state = dfa[0]
        print("Dump of NFA for root")
        todo = [state]
        for i, state in enumerate(todo):
            print("  State", i, state is state and "(final)" or "")
            for label, next in state.arcs.items():
                if next in todo:
                    j = todo.index(next)

# Generated at 2022-06-13 18:06:06.050981
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    import sys

    if sys.argv[1:]:
        sys.path.insert(0, sys.argv[1])
        del sys.argv[1]
    else:
        raise RuntimeError("First argument is the directory containing the grammars")

    def check(pg: ParserGenerator, s: str) -> Tuple["NFAState", "NFAState"]:
        pg.generator = tokenize.generate_tokens(io.StringIO(s).readline)
        pg.gettoken()
        return pg.parse_alt()

    pg = ParserGenerator()
    a, z = check(pg, "a")
    assert a.arcs == [(None, z)]
    a, z = check(pg, "a b")
    assert a.arcs == [(None, b)]
   

# Generated at 2022-06-13 18:06:12.083865
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    import io
    import tokenize
    text = '"ab"'
    f = io.StringIO(text)
    g = tokenize.generate_tokens(f.readline)
    gen = ParserGenerator(g, "test_ParserGenerator_parse_item")
    gen.gettoken()
    a, z = gen.parse_item()
    assertTokenEqual(a, NFAState([], [("ab", z)]))
    assertTokenEqual(z, NFAState())
    gen.gettoken()
    assert gen.value is None


# Generated at 2022-06-13 18:07:30.221660
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    assert ParserGenerator.parse_item("abcd") == ("abcd", "")
    assert ParserGenerator.parse_item("'abcd'") == (None, "abcd")


if __name__ == "__main__":
    import sys

    try:
        filename = sys.argv[1]
    except IndexError:
        print("no file name argument given")
        sys.exit(2)
    f = open(filename)
    pg = ParserGenerator()
    pg.setup(f.readline)
    dfas, startsymbol = pg.parse()
    pg.addfirstsets()
    c = pg.make_converter()
    print(c.make_grammar())

# Generated at 2022-06-13 18:07:40.473590
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    def t(source: Text, expected: Dict[int, int]) -> None:
        f = io.StringIO(source)
        g = ParserGenerator()
        g.parse_grammar(f)
        c = g.make_converter()
        c.states.append([]) # dummy
        first = g.make_first(c, "A")
        assert first == expected
        assert c.labels == [
            (1, None), (2, None), (3, None), (4, None), (5, None), (6, None), (7, None)
        ]
        assert c.tokens == {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}

# Generated at 2022-06-13 18:07:54.209444
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    p = ParserGenerator(None)
    p.source = iter([
        (token.NAME, 'alt', (0, 0), (0, 0), 'alt'),
        (token.OP, '|', (0, 0), (0, 0), '|'),
        (token.NAME, 'alt', (0, 0), (0, 0), 'alt'),
        (token.NEWLINE, '', (0, 0), (0, 0), ''),
    ])
    p.gettoken()
    assert p.value == 'alt'
    a, z = p.parse_rhs()
    assert a.arcs == [(None, z)]
    assert z.arcs == [(None, a), ('alt', z)]
    assert repr(a) == repr(z)


# Generated at 2022-06-13 18:08:03.349802
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    def _test(input, expected):
        global pgen
        pgen = ParserGenerator()
        actual = pgen.parse_item()
        assert actual == expected, "unexpected result for input %r" % input
    pgen = None
    global pgen
    _test("[abc]", (NFAState(arcs=[(Arc("abc"), 1)]), NFAState(arcs=[])))
    _test("abc", (NFAState(arcs=[(Arc("abc"), 1)]), NFAState(arcs=[])))
    _test("abc+", (NFAState(arcs=[(Arc("abc"), 1)]), NFAState(arcs=[(Arc(None), 0)])))

# Generated at 2022-06-13 18:08:14.727805
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    pg = ParserGenerator("", "")

# Generated at 2022-06-13 18:08:26.105725
# Unit test for method raise_error of class ParserGenerator

# Generated at 2022-06-13 18:08:39.748168
# Unit test for method simplify_dfa of class ParserGenerator

# Generated at 2022-06-13 18:08:47.635333
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    c = pg.converter()
    pg.make_label(c, "'*'")
    pg.make_label(c, "'+'")
    pg.make_label(c, "'-'")
    pg.make_label(c, "'/'")
    pg.make_label(c, "NAME")
    pg.make_label(c, 'NUMBER')
    pg.make_label(c, 'STRING')
    pg.make_label(c, 'atom')
    pg.make_label(c, 'testlist')
    pg.make_label(c, 'testlist_comp')

# Generated at 2022-06-13 18:09:04.333445
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    pg.setup()
    #    0   02   34   56   7  85
    #    012345678901234567890123
    pg.line = "alpha | beta | gamma"
    pg.pos = 0
    a, z = pg.parse_rhs()
    # pg.dump_nfa("rhs", a, z)
    assert a.arcs == [([None], a.next[0])]
    assert a.next[0].arcs == [
        (["alpha"], a.next[0].next[0]),
        (["beta"], a.next[0].next[1]),
        (["gamma"], a.next[0].next[2]),
    ]
    assert a.next[0].next[0].arcs == []

# Generated at 2022-06-13 18:09:11.681421
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import io
    import tokenize
    from .gen import ParserGenerator

    source = """
    start: 'a'
    """
    g = ParserGenerator()
    fp = io.StringIO(source)
    g.parse(fp.name, tokenize.tokenize(fp.readline))



# Generated at 2022-06-13 18:11:24.690881
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    # __init__():
    g = PgenGrammar("S", [], [], [], [], [])
    assert g.start == "S"
    assert isinstance(g.lr_action, dict)
    assert g.lr_goto == {}
    assert g.lr_productions == {}
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert not g.keywords
    assert not g.tokens

