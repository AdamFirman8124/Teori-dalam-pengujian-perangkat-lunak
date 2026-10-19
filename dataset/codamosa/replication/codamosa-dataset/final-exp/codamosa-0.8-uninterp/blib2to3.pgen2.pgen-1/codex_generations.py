

# Generated at 2022-06-13 18:02:14.454205
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    from . import util
    from . import grammar

    def do_test(pg, input, expected):
        result = pg.parse_rhs()
        assert len(result) == 2, result
        first, last = result
        dfa = pg.make_dfa(first, last)
        assert len(dfa) <= len(expected) + 1, (dfa, expected)
        dfa = optimize_dfa(dfa)
        assert len(dfa) <= len(expected) + 1, (dfa, expected)
        skip = 0
        while len(dfa) > len(expected) and not dfa[-1].arcs:
            del dfa[-1]

# Generated at 2022-06-13 18:02:25.919914
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    import doctest
    try:
        import StringIO
    except ImportError:
        import io as StringIO
    import token
    import tokenize
    import unittest

    class TestMakeDfa(unittest.TestCase):
        def assert_states(self, dfa: List["DFAState"], answer: str) -> None:
            rc = []
            for i, state in enumerate(dfa):
                arcs = sorted(state.arcs.keys())
                if state.isfinal:
                    arcs.append("(final)")
                rc.append("%d: %s" % (i, " ".join(arcs)))
            self.assertEqual("\n".join(rc), answer)

        def test1(self) -> None:
            pg = ParserGenerator()
            pg.dfas = {}


# Generated at 2022-06-13 18:02:30.230755
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    p = ParserGenerator()
    p.type = token.NAME
    p.value = "foo"
    assert p.expect(token.NAME) == "foo"
    assert p.value == ""
    p.expect(token.OP, ":")
    p.value = "bar"
    p.expect(token.NAME)

# Generated at 2022-06-13 18:02:40.453934
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    import io
    import tokenize
    from typing import Generator, Tuple
    from lib2to3 import pygram, pytree
    def _readable(iterable: Iterable[Tuple[int, Text, Any, Any, Any]]
                  ) -> Generator[Tuple[int, Text, Any, Any, Any], None, None]:
        """
        Wraps an iterable that produces token tuples and returns the
        tuple's elements in the following order: type, string, start,
        end, line.
        """
        for t in iterable:
            yield (t[0], t[1], t[2], t[3], t[4])

# Generated at 2022-06-13 18:02:51.631678
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    gen = ParserGenerator()
    gen.raise_error = Mock()
    gen.gettoken = Mock()
    gen.gettoken.side_effect = [(4, "4", (1, 2), (1, 3), "4"), (0, "0", (2, 3), (2, 4), "0")]
    gen.value = "4"
    gen.type = 4
    gen.parse_atom()
    assert gen.raise_error.call_count == 0, "No errors should be raised"
    gen.value = "0"
    gen.type = 0
    gen.parse_atom()
    gen.raise_error.assert_called_once_with(
        "expected (...) or NAME or STRING, got 0/0",
    )



# Generated at 2022-06-13 18:02:59.394872
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    lr = ParserGenerator()
    c = lr.make_converter()
    c.labels = [
        (1, None),
        (2, None),
        (3, None),
        (4, None),
        (5, None),
        (6, None),
        (7, None),
        (8, None),
        (9, None),
        (10, None),
        (11, None),
    ]
    c.symbol2number = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# Generated at 2022-06-13 18:03:01.389868
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    import doctest
    from . import parser_generator
    return doctest.testmod(parser_generator)


# Generated at 2022-06-13 18:03:09.097389
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    """Test case for dump_nfa method of class ParserGenerator."""

    import io
    import unittest


# Generated at 2022-06-13 18:03:11.847872
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    from types import FunctionType

    # Test type (function)
    assert isinstance(pg.make_first, FunctionType), repr(pg.make_first)

    # Test results
    assert pg.make_first(None, "None") == {}

    # Test exception



# Generated at 2022-06-13 18:03:16.837017
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    p = ParserGenerator()
    p.first = {"expr": {"NAME": 1}, "term": {"NAME": 1}}
    p.dfas = {"expr": [], "term": []}
    p.addfirstsets()
    assert p.first == {"expr": {"NAME": 1}, "term": {"NAME": 1}}


# Generated at 2022-06-13 18:04:03.238091
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    pg = ParserGenerator(grammar)
    pg.addfirstsets()
    assert pg.first["single_input"] == {"(": 1, "[": 1, "$end": 1, "name": 1, "str": 1}
    assert pg.first["file_input"] == {"(": 1, "[": 1, "name": 1, "str": 1}
    assert pg.first["eval_input"] == {"(": 1, "[": 1, "name": 1, "str": 1}

# Generated at 2022-06-13 18:04:06.906319
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    from grammar import _converter
    from grammar import _pgen
    from grammar import _tokenizer
    pgen = _pgen.ParserGenerator([])
    pgen.dump_nfa("test", ("start"), ("final"))


# Generated at 2022-06-13 18:04:14.562893
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    import pytest
    from typing import Dict

    class DummyConverter:
        # Hack for unit testing method make_first
        def __init__(self):
            self.labels = []
            self.symbol2label = {}
            self.symbol2number = {}
            self.keywords = {}
            self.tokens = {}

        def make_label(self, c: ParserGenerator, label: Text) -> int:
            ilabel = len(self.labels)
            self.labels.append(label)
            return ilabel

    pg = ParserGenerator()

# Generated at 2022-06-13 18:04:19.252591
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pg = ParserGenerator()
    dfa = []
    d = {1: 1}
    dfa.append(DFAState(d, None))
    d = {2: 1, 3: 1}
    dfa.append(DFAState(d, None))
    d = {3: 1}
    dfa.append(DFAState(d, None))
    d = {1: 1, 2: 1}
    dfa.append(DFAState(d, None))
    d = {1: 1, 2: 1}
    dfa.append(DFAState(d, None))
    pg.simplify_dfa(dfa)
    assert len(dfa) == 3



# Generated at 2022-06-13 18:04:26.239175
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    import io
    import sys

    saved_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    try:
        a = ParserGenerator()
        a.dump_dfa('a', [(5,)])
        assert mystdout.getvalue() == "Dump of DFA for a\n  State 0 (final)\n"
    finally:
        sys.stdout = saved_stdout


# Generated at 2022-06-13 18:04:37.062569
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    from lib2to3.main import main
    from lib2to3.pgen2.pgen import tokenize
    from lib2to3.pgen2.parse import ParserGenerator
    from lib2to3.tests import support

    generator = ParserGenerator()
    # Make sure file name in token (filename, lineno, start, end) is properly
    # set.
    input = """\
import sys
import os.path
"""
    # Call gettoken() with a fake input, line number.
    filename = "f.py"
    lineno = 1
    generator.filename = filename
    generator.generator = tokenize.generate_tokens(support.StringIOWrapper(input))

# Generated at 2022-06-13 18:04:45.084752
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    from .parser import pickle
    from . import parser
    import unittest
    from test.support import captured_stdout

    # Make sure pickle actually works.
    value = pickle.dumps(parser.suite("a = 1"))
    assert isinstance(value, bytes)
    ast = pickle.loads(value)
    assert isinstance(ast, parser.st2tuple(parser.suite("a = 1")))

    # Print the grammar module
    pg_module = ParserGenerator().pgen()
    with captured_stdout() as stdout:
        exec(pg_module, {}, {})
    pg_module_code = stdout.getvalue()
    assert pg_module_code
    assert "parse" in pg_module_code
    assert "error" in pg_module_code

# Generated at 2022-06-13 18:04:55.700964
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    parser = ParserGenerator()

# Generated at 2022-06-13 18:05:05.004631
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    # These tests are complicated, because token.tok_name and token.NAME
    # have been changed to use the mapping in Lib/token.py.
    import tokenize

# Generated at 2022-06-13 18:05:13.566040
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    parser = ParserGenerator()
    dfa = [
        DFAState({NFAState(): 1}, NFAState()),
        DFAState({NFAState(): 1}, NFAState()),
        DFAState({NFAState(): 1}, NFAState()),
    ]
    dfa[0].addarc(dfa[1], "a")
    dfa[0].addarc(dfa[2], "b")
    dfa[1].addarc(dfa[2], "c")
    dfa[2].addarc(dfa[1], "d")
    parser.dump_dfa("name", dfa)



# Generated at 2022-06-13 18:06:29.196293
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.dfas = {
        "a": [DFAState({}, False), DFAState({}, True)],
        "b": [DFAState({}, False), DFAState({}, True)],
        "c": [DFAState({}, False), DFAState({}, True)],
        "d": [DFAState({}, False), DFAState({}, True)],
        "e": [DFAState({}, False), DFAState({}, True)],
        "f": [DFAState({}, False), DFAState({}, True)],
    }
    pg.dfas["a"][0].addarc(pg.dfas["b"][0], "b")

# Generated at 2022-06-13 18:06:37.162473
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    class FakeTokenizer:
        def __init__(self, tok_name: int, token: str) -> None:
            self.tok_name = tok_name
            self.token = token

    tokenizer = FakeTokenizer(token.NAME, "foo")
    p = ParserGenerator(tokenizer, "foo")
    try:
        p.raise_error("%s", "hello")
    except SyntaxError as err:
        assert str(err) == "hello"
        assert err.filename == "foo"
        assert err.lineno == 0
        assert err.offset == 0
        assert err.text == "<string>"


# Generated at 2022-06-13 18:06:48.416974
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    # Tests taken from class unittest.case.TestCase.
    class DummyTestCase(object):

        def assertEqual(self, first, second, msg=None):
            """Fail if the two objects are unequal as determined by the '=='
               operator.
            """

        def assertFalse(self, expr, msg=None):
            """Fail the test if the expression is true."""

        def assertTrue(self, expr, msg=None):
            """Fail the test unless the expression is true."""
            if not expr:
                raise AssertionError(msg)

    testcase = DummyTestCase()
    testcase.assertEqual(PgenGrammar.__name__, 'PgenGrammar')
    testcase.assertFalse(PgenGrammar.__bases__ == ())
    testcase.assertTrue

# Generated at 2022-06-13 18:06:50.480530
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    assert isinstance(PgenGrammar, type)


# Generated at 2022-06-13 18:07:00.916595
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    import pytest

    pg = ParserGenerator()
    a = pg.makeNFAState()
    z = pg.makeNFAState()
    a.addarc(pg.makeNFAState(), 'a')
    a.addarc(z, 'b')
    dfa = pg.make_dfa(a, z)
    assert len(dfa) == 2
    state0, state1 = dfa
    assert len(state0.arcs) == 2
    state0_arcs = dict(state0.arcs)
    assert state0_arcs['a'] == state0_arcs['b'] == state1
    assert len(state1.arcs) == 0
    assert not state0.isfinal
    assert state1.isfinal



# Generated at 2022-06-13 18:07:10.354245
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    test_msg = "test message"
    test_tuple = (1,2,3,4)
    try:
        raise ParserGenerator([]).raise_error(test_msg, test_tuple)
    except SyntaxError as e:
        assert e[0] == test_msg
        assert e.offset == test_tuple
    else:
        assert False, 'Expected a SyntaxError'


# Generated at 2022-06-13 18:07:11.579835
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    x = PgenGrammar(x=[str])


# Generated at 2022-06-13 18:07:19.646262
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    pg = ParserGenerator()
    a = NFAState()
    b = NFAState()
    c = NFAState()
    d = NFAState()
    e = NFAState()
    f = NFAState()
    a.addarc(b, "a")
    a.addarc(f)
    b.addarc(None, "b")
    b.addarc(c)
    b.addarc(e)
    c.addarc(d)
    c.addarc(e)
    d.addarc(None, "c")
    e.addarc(None, "d")
    f.addarc(None, "e")
    f.addarc(a)
    pg.dump_nfa("test", a, f)

# Generated at 2022-06-13 18:07:36.269508
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    pg = ParserGenerator()
    c = pg._converter()
    def check(label, expected):
        print(label, expected)
        if isinstance(expected, int):
            assert_equal(pg.make_label(c, label), expected)
        else:
            assert_raises(expected, pg.make_label, c, label)
    # XXX should check that the label actually is converted to expected
    # XXX should check that the symbol2number and label tables are correctly updated

    # Test TRANSLATOR comments
    check("translator_comments", token.COMMENT)
    check("_translator_comments_", token.NAME)

    # Test keywords and operators
    check("and", token.NAME)
    check("and", token.NAME)  # check that table is updated
    check("is", token.NAME)


# Generated at 2022-06-13 18:07:44.538165
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    import token
    from .gen_grammar_token import gen_grammar_token
    from .gen_grammar import gen_grammar
    from .python_grammar import python_grammar
    from .python_grammar_token import python_grammar_token
    from .grammar import Grammar
    # Generate token module
    gen_grammar_token(python_grammar_token)
    # Generate grammar module
    gen_grammar(python_grammar)
    g = Grammar('single_input')
    pg = ParserGenerator(g)
    pg.addfirstsets()
    result = set(pg.first['file_input'].keys())

# Generated at 2022-06-13 18:10:04.997214
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pgen = ParserGenerator()
    pgen.parse_alt()



# Generated at 2022-06-13 18:10:15.365243
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    p = ParserGenerator()

# Generated at 2022-06-13 18:10:30.371149
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    from . import pytoken
    import tokenize
    from .pgen2 import driver
    from .pgen2 import parse
    import io
    import sys
    import unittest

    # Replace sys.stdout and sys.stderr with non-sys.__stdout__ streams,
    # so we can test what is written to them by trying to run a nonexistent
    # file.
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    stdout = io.StringIO()
    stderr = io.StringIO()
    parser = driver.ParserGenerator()

# Generated at 2022-06-13 18:10:39.114241
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator(tokenize.StringIO(""), "<test>")
    pg.first = {"one": {"token1": 1, "token2": 1}, "two": {"token3": 1}, "three": None}
    pg.dfas = {"one": [], "two": [], "three": []}
    c = pg.make_converter()
    # c.labels needs to be sorted on string values to make sure values
    # are added in the proper order.
    c.labels.sort(key=lambda x: x[1] or "")
    assert c.labels == [(tokenizer.NAME, "token1"), (tokenizer.NAME, "token2"), (tokenizer.NAME, "token3")]

# Generated at 2022-06-13 18:10:51.567943
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    # Test a tiny grammar
    def check(rulelist: List[grammar.Grammar], expected: GrammarInfo) -> None:
        pg = ParserGenerator()
        for name, rhs in rulelist:
            pg.add_rule(name, rhs)
        dfas, startsymbol = pg.dfas, pg.startsymbol
        assert startsymbol == "S"
        assert len(dfas) == 2
        assert len(dfas["S"]) == 5
        assert len(dfas["X"]) == 3
        first = pg.first
        assert first == {"S": {"foo": 1, "bar": 1}, "X": {"baz": 1, None: 1}}

# Generated at 2022-06-13 18:11:02.128365
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    from io import StringIO
    pg = ParserGenerator("<string>", StringIO("# Comment\n"
                                              "foo: 'foo'\n"
                                              "bar: 'bar'\n"))
    tok = pg.gettoken()
    assert (pg.type, pg.value) == (tokenize.NAME, "foo"), (pg.type, pg.value)
    tok = pg.gettoken()
    assert (pg.type, pg.value) == (token.OP, ":"), (pg.type, pg.value)
    tok = pg.gettoken()
    assert (pg.type, pg.value) == (token.STRING, "'foo'"), (pg.type, pg.value)
    tok = pg.gettoken()

# Generated at 2022-06-13 18:11:09.792064
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from . import grammar_nts
    from . import token
    # 1. Test two matching tokens
    lines = [
        "1:    NAME STRING+",
        "2:    NAME STRING*",
    ]
    parser = ParserGenerator(lines)
    parser.gettoken()
    parser.expect(token.NAME)
    parser.expect(token.OP, ":")
    parser.expect(token.NAME)
    parser.expect(token.STRING)
    parser.expect(token.OP, "+")
    parser.expect(token.NEWLINE)
    parser.expect(token.NAME)
    parser.expect(token.OP, ":")
    parser.expect(token.NAME)
    parser.expect(token.STRING)

# Generated at 2022-06-13 18:11:17.671599
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator()
    pg.make_scanner()
    dfa = [
        DFAState({"start": 1}, "finish"),
        DFAState({"a": 1, "b": 2}, "finish"),
        DFAState({"c": 3}, "finish"),
        DFAState({"d": 4}, "finish"),
        DFAState({"e": 5}, "finish"),
        DFAState({}, "finish")
        ]
    dfa[0].addarc(dfa[1], "a")
    dfa[0].addarc(dfa[1], "b")
    dfa[1].addarc(dfa[2], "c")
    dfa[1].addarc(dfa[0], "a")

# Generated at 2022-06-13 18:11:26.905562
# Unit test for function generate_grammar
def test_generate_grammar():
    p = ParserGenerator("Grammar.txt")
    grammar = p.make_grammar()
    assert isinstance(grammar, PgenGrammar)
    assert isinstance(grammar.check_version, PgenGrammar.check_version)
    assert grammar.start == "file_input"
    assert isinstance(grammar.keywords, dict)
    assert isinstance(grammar.tokens, dict)
    assert isinstance(grammar.dfas, dict)
    assert isinstance(grammar.labels, list)
    assert isinstance(grammar.states, list)
    assert grammar.states[0] == "file_input"
    assert isinstance(grammar.first, dict)
