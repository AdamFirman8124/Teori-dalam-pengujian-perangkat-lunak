

# Generated at 2022-06-13 18:02:35.810184
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    s = """\
asdl_seq: "[]"
    | "[" asdl_expr_list "]"
asdl_expr_list: asdl_expr
    | asdl_expr_list "," asdl_expr
asdl_expr: asdl_term
    | asdl_expr "|" asdl_term
asdl_term: "{" asdl_field_list "}"
    | NAME
asdl_field_list: asdl_field
    | asdl_field_list "," asdl_field
asdl_field: NAME ["=" asdl_expr]
"""
    filename = "<string>"
    pg = ParserGenerator()
    pg.parse_grammar(filename, s)
    pg.addfirstsets()
    dfas = pg.dfas
    # XXX Using method dump_dfa
    pg

# Generated at 2022-06-13 18:02:40.075699
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    src = '''
    # comment
    x = 1
    '''
    p = ParserGenerator()
    d = {}
    p.add_start_rule(d, "x", '"=" NUMBER')
    d["NUMBER"] = p.make_dfa(p.parse_rhs(p.parse_atom("NUMBER")))
    p.make_tokenizer(src)
    p.dump()


# Generated at 2022-06-13 18:02:44.870172
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    import io
    import tokenize
    fname = "<parse_rhs>"
    s = "Foo: Bar Baz\n"
    f = io.StringIO(s)
    g = ParserGenerator()
    g.init_dfas()
    g.filename = fname
    g.generator = tokenize.generate_tokens(f.readline)
    a, z = g.parse_rhs()
    # g.dump_nfa("", a, z)



# Generated at 2022-06-13 18:02:54.807517
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    from .nfa import NFAState, DFAState

    def check(dfa: List[DFAState], expected: List[DFAState]) -> None:
        ParserGenerator.simplify_dfa(dfa)
        # "".join(str(x) for x in dfa) == "".join(str(x) for x in expected)
        assert "".join(str(x) for x in dfa) == "".join(str(x) for x in expected)
        check_always_visited(dfa, expected)


# Generated at 2022-06-13 18:03:04.842094
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    def mock_self():
        return parser.types.SimpleNamespace(
            type=token.NAME,
            value='value',
            generator=iter([]),
            filename='filename',
            end=(1,2),
            line='line',
        )
    self = mock_self()
    with pytest.raises(SyntaxError) as excinfo:
        ParserGenerator.expect(self, token.NEWLINE)
    assert str(excinfo.value) == 'expected NEWLINE/None, got NAME/value'
    self = mock_self()
    with pytest.raises(SyntaxError) as excinfo:
        ParserGenerator.expect(self, token.NAME, 'not value')
    assert str(excinfo.value) == "expected NAME/not value, got NAME/value"

# Generated at 2022-06-13 18:03:12.694231
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    pg = ParserGenerator()
    pg.type = token.STRING
    pg.value = "foo"
    pg.expect(token.STRING, "foo")
    pg.type = token.NAME
    pg.value = "foo"
    pg.expect(token.NAME, "foo")
    pg.expect(token.STRING, "foo")
    # Should raise SyntaxError


# Generated at 2022-06-13 18:03:17.056747
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    grammar = PgenGrammar("filename", "", True, False)
    assert grammar.filename == "filename"
    assert not grammar.parsing_succeeded
    assert not grammar.finished_parsing
    assert grammar.modified
    assert not grammar.partially_valid



# Generated at 2022-06-13 18:03:20.668206
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pgen = ParserGenerator()
    pgen.load_grammar(grammar)
    dfa = pgen.dfas["expr1"]
    pgen.dump_dfa("expr1", dfa)

test_ParserGenerator_dump_dfa()


# Generated at 2022-06-13 18:03:23.588487
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    parser = ParserGenerator()
    try:
        parser.raise_error("a %s %s b", "c", "d")
    except SyntaxError as e:
        assert str(e) == "a c d b"

# Generated at 2022-06-13 18:03:38.114133
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    def check(txt: Text, expect: Text) -> None:
        try:
            parser = ParserGenerator()
            nfa, znfa = parser.parse_atom(txt)
        except Exception as e:
            print("parse_atom(%r) raises %s" % (txt, type(e).__name__))
            raise
        else:
            got = "".join(sorted(arc[1] for arc in nfa.arcs))
            if got != expect:
                print("parse_atom(%r) = %r, expected %r" % (txt, got, expect))
            assert got == expect

    check("x", "x")

    try:
        parser = ParserGenerator()
        parser.parse_atom("+")
    except Exception as e:
        assert type(e).__name__

# Generated at 2022-06-13 18:04:20.754889
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pg = ParserGenerator()
    pg.symbol2number = {'S': 1}
    pg.make_label = lambda self, label: int(label)
    class DFAState:
        def __init__(self, nfaset, finish):
            self.nfaset = nfaset
            self.isfinal = (finish in nfaset)
            self.arcs = {}
        def addarc(self, next, label):
            self.arcs[label] = next
        def unifystate(self, old, new):
            self.arcs[label] = new
        def __eq__(self, other):
            if self.isfinal != other.isfinal:
                return False
            if len(self.arcs) != len(other.arcs):
                return False
           

# Generated at 2022-06-13 18:04:29.846351
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator()
    # Parse a simplified, hand-coded version of a part of the grammar.
    pg.dfas = {"foo": [  # type: ignore
        DFAState({NFAState(0): 1}, "bar") ,
        DFAState({NFAState(1): 1, NFAState(3): 1}, "bar") ,
        DFAState({NFAState(2): 1, NFAState(4): 1}, "bar") ,
        DFAState({NFAState(2): 1}, "foo") ,
        DFAState({NFAState(1): 1}, "bar") ,
        DFAState({NFAState(4): 1}, "bar") ,
    ]}

# Generated at 2022-06-13 18:04:39.729009
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    # Collect a set of assertions
    L = []
    def check(s: Text, r: Text) -> None:
        L.append((s, r))
    # Last but not least, assert that we parsed an identical grammar
    pg = ParserGenerator()
    x = pg.parse(StringIO(r"""

empty_file :

name_or_num : NAME
            | NUMBER

func_calls : func_call
           | func_call func_calls

func_call : name_or_num '(' func_args ')'

func_args :
          | func_arg
          | func_arg ',' func_args

func_arg : name_or_num
         | STRING

"""))
    assert x is not None

    # Method dump_dfa

# Generated at 2022-06-13 18:04:44.274019
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    try:
        #try:
            a = PgenGrammar()
        #except TypeError:
        #    print("TypeError")
        #else:
        #    print("noError")
    except Exception:
        print("Error")



# Generated at 2022-06-13 18:04:55.031433
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    from . import grammar, token
    from .tokenizer import generate_tokens, untokenize
    from .pytoken import generate_tokens as pytokenize

    def check(g: PgenGrammar) -> None:
        assert g.states is not None
        for i, state in enumerate(g.states):
            assert i == len(state), (i, state)
            for j, (label, next) in enumerate(state):
                assert j == len(label), (j, label)
                assert j == len(next), (j, next)
                assert g.states[next][0][0] == g.states[next][0][0], (i, next)


# Generated at 2022-06-13 18:04:57.879496
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    grammar = ParserGenerator().make_grammar()
    assert isinstance(grammar, PgenGrammar)


# Generated at 2022-06-13 18:05:06.360868
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.dfas = {
        "a": [DFAState({NFAState(): 1}, NFAState())],
        "b": [DFAState({NFAState(): 1}, NFAState())],
    }
    pg.first = {}
    pg.calcfirst("a")
    assert pg.first["a"] == {"a": 1}
    pg.calcfirst("b")
    assert pg.first["b"] == {"b": 1}
    pg = ParserGenerator()
    a, az, b, bz = [NFAState() for i in range(4)]
    pg.dfas = {"a": [DFAState({a: 1}, az), DFAState({b: 1}, bz)]}
    pg.first = {}

# Generated at 2022-06-13 18:05:10.896435
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    parser: ParserGenerator
    input: str
    parser = ParserGenerator(tokenize.generate_tokens(io.StringIO(input).readline))
    parser.gettoken()
    parser.gettoken()
    parser.gettoken()

# Generated at 2022-06-13 18:05:23.647411
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    c = PgenGrammar()
    class Spec1:
        first = {
            "A": {"a": 1},
            "B": {"a": 1, "b": 1},
            "C": {"b": 1},
            "D": {"b": 1},
        }
        symbol2number = {
            "A": 101,
            "B": 102,
            "C": 103,
            "D": 104,
        }
        symbol2label = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
        }
        tokens = {"a": 5, "b": 6}
    assert c.make_first(Spec1, "A") == {5: 1}

# Generated at 2022-06-13 18:05:25.216961
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    pg.make_first(None, None)



# Generated at 2022-06-13 18:06:15.213959
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator(
        [
            "  foo: 'foo'\n"
            "  bar: 'bar'\n"
            "  baz: 'zap' | 'zip'\n"
            "  bif: 'zot' | 'zap'\n"
            "  bof: 'zop' | 'zup'\n"
            "  big: 'zep' | 'zop'\n"
            "  bap: 'zip'\n"
        ]
    )
    dfas, startsymbol = pg.parse()

# Generated at 2022-06-13 18:06:21.177195
# Unit test for method parse_rhs of class ParserGenerator

# Generated at 2022-06-13 18:06:30.867186
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    # XXX: Is this a good test case?
    tokens = [
        (token.NAME, "A"),
        (token.OP, ":"),
        (token.NAME, "x"),
        (token.NEWLINE, "\n"),
        (token.NAME, "B"),
        (token.OP, ":"),
        (token.NAME, "x"),
        (token.NEWLINE, "\n"),
        (token.ENDMARKER, ""),
    ]
    gen = ParserGenerator(tokens)
    assert gen.expect(token.NAME) == "A"
    assert gen.value == ":"
    gen.expect(token.OP, ":")
    assert gen.value == "x"
    gen.expect(token.NAME)
    assert gen.value == "\n"
    gen

# Generated at 2022-06-13 18:06:39.650407
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    import tokenize
    from tokenize import tokenize
    from io import StringIO
    from tokenize import StringIO as StringIO
    from io import BytesIO
    from tokenize import BytesIO as BytesIO
    from tokenize import tokenize
    from tokenize import untokenize
    from pgen2.parse import untokenize as untokenize
    from tokenize import generate_tokens
    from pgen2.parse import generate_tokens as generate_tokens
    from tokenize import NL
    from pgen2.parse import NL as NL
    from tokenize import TokenError
    from pgen2.parse import TokenError as TokenError
    from tokenize import COMMENT
    from pgen2.parse import COMMENT as COMMENT
    from tokenize import INDENT
    from pgen2.parse import INDENT as IND

# Generated at 2022-06-13 18:06:47.595771
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import tokenize
    import io

    #  Python source code, syntax-highlighted by Pygments
    #
    #  tokenize.detect_encoding(readline)
    #
    #  for t in generate_tokens(readline):
    #      print("%d,%d:%d:%s:%s" % (t[2][0], t[2][1], t[0], t[1], repr(t[4])))
    #


# Generated at 2022-06-13 18:06:54.846476
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    import doctest

    if sys.flags.optimize >= 2:
        # Under -OO, dump_nfa will not be included in the generated .pyo,
        # so this will fail.
        pytest.skip("cannot test with -OO")
    doctest.run_docstring_examples(ParserGenerator.dump_nfa, _gen, globals(), True, False)



# Generated at 2022-06-13 18:07:02.242511
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    pg = ParserGenerator()
    # "true"
    tup = ("NAME", "true", (0, 0), (3, 0), b"true")
    actual = pg._ParserGenerator__gettoken(tup)
    assert actual == tup
    # "true" ENDMARKER
    tup = ("ENDMARKER", "", (3, 0), (3, 0), b"")
    actual = pg._ParserGenerator__gettoken(tup)
    assert actual == tup
    # "true" comment
    tup = ("COMMENT", "", (3, 0), (3, 0), b"")
    actual = pg._ParserGenerator__gettoken(tup)
    assert actual == tup
    # "true" newline

# Generated at 2022-06-13 18:07:18.111161
# Unit test for constructor of class ParserGenerator

# Generated at 2022-06-13 18:07:34.730602
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    def check(s: Text, expected: Dict[Text, Text]) -> None:
        nfa, finish = ParserGenerator(s).parse_item()
        assert finish.arcs == []
        arcs = [(label, state.arcs[0][1]) for label, state in nfa.arcs]
        assert arcs == [(expected, "")]

    check('"x"', '"x"')
    check("'x'", "'x'")
    check("xyz", "xyz")
    check("(xyz)", "xyz")
    check("[xyz]", "xyz")
    check("xyz+", "xyz")
    check("xyz*", "xyz")
    check("[xyz]*", "xyz")
    check("[xyz]+", "xyz")




# Generated at 2022-06-13 18:07:42.526881
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    pg = ParserGenerator()
    c = PgenGrammar(pg)
    c.symbol2number['test'] = 1
    c.tokens[token.STRING] = 2
    c.keywords['test2'] = 3
    c.labels = [
        (1, None),  # symbol
        (token.STRING, None),  # token
        (token.NAME, "test2")  # keyword
    ]
    assert pg.make_label(c, 'test') == 0, "symbol should return 0"
    assert pg.make_label(c, 'STRING') == 1, "token should return 1"
    assert pg.make_label(c, '"test2"') == 2, "keyword should return 2"

# Generated at 2022-06-13 18:09:14.281737
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    p = ParserGenerator()
    p.make_nfas()
    p.addfirstsets()


# Generated at 2022-06-13 18:09:25.075484
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    pg = ParserGenerator()
    pg.make_scanner()

    from grammar_parser import grammar_parser

    # parse the grammar file and get a list of tuples
    # (rule name, list of rule_item and '|' with the first
    # rule_item in the first position of the list).
    list_of_rules = grammar_parser.parse_grammar()
    # parse the list of tuples and get a list of tuples
    # (rule name, NFAState and NFAState)
    list_of_nfastates = pg.parse_list_of_rules(list_of_rules)
    # set the name of the start rule
    name_start_rule = 'file_input'
    # get the NFAState and NFAState of the start rule

# Generated at 2022-06-13 18:09:28.270616
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    # Test that 'newline_re' compiles
    p = ParserGenerator()
    p.newline_re.match("\n")


# Generated at 2022-06-13 18:09:41.226509
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    import io
    import unittest

    class ParserGenerator_dump_nfaTest(unittest.TestCase):

        def test_dump_nfa(self):
            import pickle
            import types

# Generated at 2022-06-13 18:09:41.793812
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pass



# Generated at 2022-06-13 18:09:51.325822
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    import io
    import unittest
    import token
    from typing import List

    testcase = unittest.TestCase()

    class Dummy(object):
        def gettoken(self):
            self.type = token.NAME
            self.value = "foo"

    d = Dummy()
    d.gettoken()

    d.expect(token.NAME)
    testcase.assertEqual(d.type, token.NAME)
    testcase.assertEqual(d.value, "foo")

    d.expect(token.NAME, "foo")
    testcase.assertEqual(d.type, token.NAME)
    testcase.assertEqual(d.value, "foo")

    # Test raising SyntaxError

# Generated at 2022-06-13 18:09:54.883570
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    try:
        ParserGenerator(None).expect(token.NAME, "foo")
        assert False
    except SyntaxError as e:
        assert e.msg == "expected NAME/foo, got ENDMARKER/None"


# Generated at 2022-06-13 18:09:56.837431
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    p = ParserGenerator()
    start = NFAState()
    finish = NFAState()
    start.addarc(NFAState(), 'a')
    states = p.make_dfa(start, finish)
    assert len(states) == 3



# Generated at 2022-06-13 18:10:04.540021
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():

    class _FakeGrammarSpec(GrammarSpec):

        symbols = [
            # Some ready-made elements.
            NT("string", ("[^ \t\n]*",)),
            NT("name", ("[a-zA-Z_][a-zA-Z_0-9]*",)),
            NT("number", ("[0-9]+",)),
            # A pre-defined element (not really needed here).
            NT("encoding_decl", ("NAME", "STRING")),
        ]

        # The 'file_input' rule.

# Generated at 2022-06-13 18:10:09.437876
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    import unittest
    from unittest import mock
    from . import pgen
    import io
    import textwrap

    class ParserGenerator_simplify_dfa(unittest.TestCase):
        def _call(self, source_text: str, *, debug: bool = False) -> None:
            input_file = io.StringIO()
            input_file.write(textwrap.dedent(source_text))
            input_file.seek(0)
            dfa = pgen.ParserGenerator(input_file, debug=debug).dfas["file_input"]
            pgen.ParserGenerator.simplify_dfa(dfa)

        def test_empty(self) -> None:
            self._call(
                """
            file_input:
                |
            """
            )

       