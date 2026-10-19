

# Generated at 2022-06-13 18:02:25.919244
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    # test calcfirst using an example grammar
    pg = ParserGenerator()
    pg.add_rhs("a", ["NAME", "expr", "expr"])
    pg.add_rhs("a", ["expr", "expr", "expr"])
    pg.add_rhs("a", ["expr", "expr", "expr", "expr"])
    pg.add_rhs("a", ["expr", "expr", "expr", "expr", "expr"])
    pg.add_rhs("a", ["expr", "NAME", "expr", "expr", "expr", "expr"])
    pg.add_rhs("b", ["NAME", "NAME", "NAME"])
    pg.add_rhs("b", ["NAME", "NAME"])
    pg.add_rhs("b", ["NAME"])

# Generated at 2022-06-13 18:02:36.567742
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    # 1. Test above code for valid inputs

    # Arbitrary valid input
    p = ParserGenerator(
        [
            (token.NAME, "hello", (0, 0), (1, 1), "'hello'"),
            (token.NUMBER, "1", (1, 1), (1, 2), "'1'"),
            (token.OP, ";", (1, 2), (1, 3), "';'"),
        ],
        "graminit.txt",
    )
    p.gettoken()
    p.expect(token.NAME, "hello")
    p.expect(token.NUMBER, "1")
    p.expect(token.OP, ";")
    # End of unit test #1 for method raise_error of class ParserGenerator


# Generated at 2022-06-13 18:02:38.607788
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    """
    Test the constructor of the PgenGrammar class.
    """
    PG = PgenGrammar(token.tok_name)



# Generated at 2022-06-13 18:02:46.564524
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pg = ParserGenerator()
    dfa = [
        DFAState({"a"}, "a"),
        DFAState({"b"}, "b"),
        DFAState({"a"}, "a"),
        DFAState({"b"}, "b"),
        DFAState({"a"}, "a"),
        DFAState({"a"}, "a"),
    ]
    before = dfa[:]
    pg.simplify_dfa(dfa)
    assert dfa == [
        DFAState({"a"}, "a"),
        DFAState({"b"}, "b"),
        DFAState({"a"}, "a"),
    ]


# Generated at 2022-06-13 18:02:55.520515
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    def _test_prg(prg: ParserGenerator, cases: List[Tuple[str, Tuple[str, str]]]):
        for input, output in cases:
            prg.initfp(StringIO(input), "<testcase>")
            prg.gettoken()
            a, z = prg.parse_item()
            assert prg.type == token.ENDMARKER
            assert (str(a), str(z)) == output

    prg = ParserGenerator()

# Generated at 2022-06-13 18:03:05.527322
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
  from . import ParserGenerator
  from . import NFA
  from . import DFA
  pg = ParserGenerator()
  pg.startsymbol = "file_input"
  pg.dfas["file_input"] = [DFA.DFAState(NFA.closure_str({0: 1}), True)]
  pg.dfas["eval_input"] = [DFA.DFAState(NFA.closure_str({0: 1}), True)]
  pg2 = pg.converter()
  closure = NFA.closure_str({0: 1})
  assert pg2.make_first(pg2, "file_input") == {pg2.symbol2number["eval_input"]: 1}
  assert pg2.make_first(pg2, "eval_input") == closure

# Generated at 2022-06-13 18:03:18.255606
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    generator = ParserGenerator('')
    class Mock:
        labels = []
        symbol2label = {}
        symbol2number = {}
        tokens = {}
        keywords = {}
    c = Mock()
    c.symbol2number['x'] = 0
    assert generator.make_label(c, 'x') == 0
    assert c.labels == []
    assert c.symbol2label == {'x': 0}
    assert c.symbol2number == {'x': 0}
    assert c.tokens == {}
    assert c.keywords == {}
    assert generator.make_label(c, 'x') == 0
    assert c.labels == []
    assert c.symbol2label == {'x': 0}
    assert c.symbol2number == {'x': 0}

# Generated at 2022-06-13 18:03:19.366439
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pgen_grammar = PgenGrammar()


# Generated at 2022-06-13 18:03:27.815790
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    with open(__file__, "rb") as f:
        tokens = tokenize.generate_tokens(f.readline)
    pg = ParserGenerator()
    a, b = pg.parse_alt()
    # print(a)
    # print(b)
    # print((a, b))
    assert a is b
    pg.gettoken()
    pg.value = "|"
    a, b = pg.parse_alt()
    assert a.arcs[0][1] is b
    pg.gettoken()
    pg.value = "|"
    a, b = pg.parse_alt()
    assert a.arcs[0][1] is b
    # print(a)
    # print(b)
    # print((a, b))
    assert a is b
# Unit

# Generated at 2022-06-13 18:03:29.775801
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    for name in ["lit", "seq", "alt", "atom"]:
        func = getattr(ParserGenerator, "dump_nfa_{}".format(name))
        func()

# Generated at 2022-06-13 18:04:12.245594
# Unit test for method addfirstsets of class ParserGenerator

# Generated at 2022-06-13 18:04:18.610616
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    p = ParserGenerator()
    p.dump_nfa("a",
      NFAState([(None, NFAState([('x', NFAState([])), ('y', NFAState([])),
                                 (None, NFAState([(None, NFAState([('z', NFAState([]))]))]))
                                ])),
                (None, NFAState([('y', NFAState([])), ('z', NFAState([]))])),
                ('a', NFAState([('b', NFAState([])), ('c', NFAState([]))])),
              ]),
      NFAState([]),
    )

# Generated at 2022-06-13 18:04:28.929383
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    """Test the method make_first of class ParserGenerator."""
    # The following code depends on the values of token constants
    # defined in module token, and should be changed if they change.

    # XXX The test should be moved to ParserGeneratorTest when we have
    # a package for the parser generator.

    import token
    import io
    import sys

    # Create a hackish ParserGenerator object just to get at the
    # make_first() method.
    pg = ParserGenerator(["code"], Tokenizer(io.StringIO(""), "<string>", sys.stdin), "code")

    pg.make_first(
        PgenGrammar(None, "code", None, None),
        '"else" / "elif" / "except" / "finally" / "try" / atom',
    )

# Generated at 2022-06-13 18:04:34.631293
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    from . import pgen2
    import os
    import tokenize
    test_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'data')
    tokenize.tokenize_file(os.path.join(test_data_path, 'data0', pgen2.GRAMMAR_PY + 'c'))



# Generated at 2022-06-13 18:04:40.236524
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    g = ParserGenerator()
    a, z = g.parse_alt()
    assert isinstance(a, NFAState)
    assert isinstance(z, NFAState)
    assert a is not z
    assert len(a.arcs) == 0
    assert len(z.arcs) == 0
    # assert str(a) == '<NFAState 0>'
    # assert str(z) == '<NFAState 1>'


# Generated at 2022-06-13 18:04:52.482332
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    pg.gettoken = Mock(return_value=None)
    pg.parse_item = Mock(side_effect=((1, 2), (3, 4)))
    pg.value = 'f'
    a, b = pg.parse_alt()
    pg.gettoken.assert_called_once_with()
    assert a == 1
    assert b == 4

    pg.value = 'g'
    a, b = pg.parse_alt()
    pg.gettoken.assert_called_with()
    assert a == 1
    assert b == 4

    pg.value = 'h'
    pg.parse_alt()
    pg.value = 'i'
    pg.parse_alt()
    pg.value = '|'
    pg.parse_alt()

# Generated at 2022-06-13 18:05:03.429849
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    pg = ParserGenerator(
        [("a", 123), ("b", 456)], [("c", r"^\d+$", re.compile(r"\d+"))]
    )
    assert pg.symbol2number == {"a": 257, "b": 258}
    assert pg.number2symbol == {257: "a", 258: "b"}
    assert pg.labels == [(token.STRING, "a"), (token.NUMBER, 456), (token.NAME, "c")]
    assert pg.keywords == {}
    assert pg.tokens == {token.STRING: 0, token.NUMBER: 1}
    assert pg.symbol2label == {"a": 0, "b": 1}
    assert pg.dfas == {}
    assert pg.first == {}



# Generated at 2022-06-13 18:05:14.559323
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    class MockConverter:
        tokens = {
            token.NAME: 200,
            token.NUMBER: 201,
            token.STRING: 202,
            token.NOT: 203,
            token.OR: 204,
            token.AND: 205,
            token.IS: 206,
            token.IN: 207,
            token.ISNOT: 208,
            token.NOTIN: 209,
            token.LT: 210,
            token.GT: 211,
            token.EQEQUAL: 212,
            token.LE: 213,
            token.GE: 214,
            token.NOTEQUAL: 215,
        }

# Generated at 2022-06-13 18:05:18.380705
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    g = ParserGenerator()
    g.parse_grammar("<foo> ::= 'foo' | 'bar'")
    g.make_dfa("foo", 0)
    g.dump_nfa("foo", 0)


# Generated at 2022-06-13 18:05:26.996448
# Unit test for method raise_error of class ParserGenerator

# Generated at 2022-06-13 18:06:32.468396
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    assert PgenGrammar()
    assert isinstance(PgenGrammar(), PgenGrammar)



# Generated at 2022-06-13 18:06:38.527890
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    pg = ParserGenerator()
    # Make an NFA with two states and an epsilon transition between them.
    a = NFAState()
    z = NFAState()
    a.addarc(z)
    # Convert it to a DFA.  It should have two states, and no epsilon
    # transition.
    dfa = pg.make_dfa(a, z)
    assert len(dfa) == 2
    assert dfa[0].arcs == {None: dfa[1]}
    # Make a bigger NFA
    a = NFAState()
    z = NFAState()
    a.addarc(z, "a")
    a.addarc(z, "b")
    dfa = pg.make_dfa(a, z)
    assert len(dfa) == 2


# Generated at 2022-06-13 18:06:49.200033
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    p = ParserGenerator()
    p.debug = 1

# Generated at 2022-06-13 18:06:55.104371
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from tatsu.test.test_util import test_expect

    import token
    import tokenize
    import io

    def generator():
        for i in range(6):
            yield (i, i, (i, i), (i, i), i)
        raise StopIteration

    def fail(object):
        raise SyntaxError('', (1, 1, '', 1))
    parser_generator = ParserGenerator(generator=generator(), fail=fail)
    parser_generator.filename = ''

    test_expect(parser_generator, 5, 5, None, (1, 1, '', 1))
    test_expect(parser_generator, 4, 4, '', (1, 1, '', 1))

# Generated at 2022-06-13 18:07:01.338835
# Unit test for method __eq__ of class DFAState
def test_DFAState___eq__():
    a = DFAState({}, None)
    b = DFAState({}, a)
    assert a == b
    assert not (a != b)
    c = DFAState({}, a)
    a.addarc(b, "1")
    assert a != b
    b.addarc(b, "1")
    assert a != b
    a.addarc(c, "2")
    assert a != b
    b.addarc(c, "3")
    assert a != b
    a.addarc(c, "3")
    assert a != b
    b.addarc(a, "2")
    assert a == b

# Generated at 2022-06-13 18:07:17.702478
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    from ._grammar import ParserGenerator
    from . import token
    from .grammar import SType

    g = ParserGenerator()
    g.add_production("start", ("start", "test", "1", "test", "2"), SType.RHS, True, "RHS")
    g.add_production("start", ("start", "~test", "3", "~test", "4"), SType.RHS, True, "RHS")
    g.add_production("start", ("start", "test", "5", "~test", "6"), SType.RHS, True, "RHS")
    g.add_production("start", ("start", "~test", "7", "test", "8"), SType.RHS, True, "RHS")

# Generated at 2022-06-13 18:07:34.232092
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    pg = ParserGenerator()

    # Tokens
    a = NFAState()
    z = NFAState()
    a.addarc(z, "a")

    # Rule parsing
    aa = NFAState()
    zz = NFAState()
    aa.addarc(a)
    aa.addarc(a)
    aa.addarc(a)
    aa.addarc(a)
    z.addarc(zz)
    z.addarc(zz)
    z.addarc(zz)
    z.addarc(zz)

    # Empty rule
    aaa = NFAState()
    zzz = NFAState()
    aaa.addarc(zzz)
    zzz.addarc(aaa)

    # Make DFA
    dfa = pg.make_df

# Generated at 2022-06-13 18:07:42.359138
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    from io import StringIO
    from . import pgen
    from .tokenize import tokenize, untokenize
    from . import grammar
    from . import pytoken
    from .symbol import sym_name

    def dump_pgen_grammar(fp: TextIO, g: pgen.PgenGrammar) -> None:
        print("# Automatically generated by _testcapi.test_ParserGenerator_parse().", file=fp)
        print(file=fp)
        symbols = sorted(g.number2symbol.items())
        print("symbol2number = {", file=fp)
        for number, symbol in symbols:
            print('    "%s": %d,' % (symbol, number), file=fp)
        print("}", file=fp)
        print(file=fp)

# Generated at 2022-06-13 18:07:55.625820
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    def _test(text, result, errors=0):
        pg = ParserGenerator()
        pg.setup(text)
        func = pg.parse_atom
        
        def _print_error(function, *expected):
            print('Error in', function)
            print('Expected:', *expected)
            print('Got:', *sys.exc_info()[1:])

        try:
            ans = func()
        except errors:
            _print_error('_test', result, errors)
        except:
            e = sys.exc_info()[0]
            _print_error('_test', result, errors, e)
        else:
            assert ans == result, "%s != %s" % (ans, result)

    _test('name', (1, 2))

# Generated at 2022-06-13 18:08:04.299948
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import io
    from . import tokenize
    from . import token


# Generated at 2022-06-13 18:08:59.258810
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pgen = ParserGenerator()

    def test(s: str, value: str, type: int, next: str) -> None:
        tok = pgen.tokenize(s)
        pgen.setup_parser(tok)
        a, z = pgen.parse_item()
        assert pgen.value == value and pgen.type == type and pgen.getlist() == next

    test("abc", "abc", token.NAME, "")
    test("abc*", "*", token.OP, "")
    test("abc+", "+", token.OP, "")
    test("abc(", "(", token.OP, "")
    test('abc"', '"', token.OP, "")
    test("abc[", "[", token.OP, "")

# Generated at 2022-06-13 18:09:03.410710
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    from . import nfa

    # a*
    dfa = nfa.ParserGenerator().make_dfa(*nfa.ParserGenerator().parse_atom())
    nfa.ParserGenerator().dump_dfa("a*", dfa)



# Generated at 2022-06-13 18:09:11.232991
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator(["x", "y"], ["x : NAME", "y : NAME"], start="x")
    c = pg.convert()
    assert c.dfas[c.symbol2number["x"]][1] == {
        c.symbol2label["NAME"]: 1
    }, "simple first set"
    pg = ParserGenerator(["x"], ["x : NAME | NUMBER"], start="x")
    c = pg.convert()
    assert c.dfas[c.symbol2number["x"]][1] == {
        c.symbol2label["NAME"]: 1,
        c.symbol2label["NUMBER"]: 1,
    }, "alternatives in first set"

# Generated at 2022-06-13 18:09:23.308168
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    for _i in range(10):
        pgen = ParserGenerator({"abcdefghijklmnopqrstuvwxyz": "abc"})
        a = NFAClosure()
        z = NFAClosure()
        a.addstate(NFAState())
        z.addstate(NFAState())
        NFAState.connect(a.getstate(), z.getstate(), "abc")
        a, z = pgen.make_dfa(a.getstate(), z.getstate())
        assert a.arcs.get("abc") == z
        pgen.simplify_dfa([a, z])
        assert a.arcs.get("abc") == z

# Generated at 2022-06-13 18:09:37.585230
# Unit test for method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:09:44.769436
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    a = DFAState({}, False)
    aa = DFAState({}, False)
    b = DFAState({}, False)
    c = DFAState({}, False)
    d = DFAState({}, False)
    e = DFAState({}, False)
    p = ParserGenerator([], [], [], {})
    a.addarc(aa, "a")
    a.addarc(b, "b")
    aa.addarc(c, "c")
    aa.addarc(d, "d")
    b.addarc(c, "c")
    b.addarc(d, "d")
    c.addarc(e, "e")
    d.addarc(e, "e")
    states = [a, aa, b, c, d, e]


# Generated at 2022-06-13 18:09:52.407070
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    g = ParserGenerator(
        """
foo: 'x'*
bar: 'y'*
""",
        {},
        "foo",
    )
    g.make_grammar()
    assert g.make_first(None, "foo") == {34: 1, 35: 1}
    assert g.make_first(None, "bar") == {0: 1, 34: 1, 35: 1}



# Generated at 2022-06-13 18:10:01.471019
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    import io
    import tokenize

    pg = ParserGenerator()

    for token in tokenize.tokenize(io.BytesIO(b"a+").readline):
        pg.process_token(token)

    dfas = pg.dfas
    assert "expr" in dfas
    assert "a_expr" not in dfas

    dfa = dfas["expr"][0]
    assert len(dfa.arcs) == 1

    # The data we're interested in is in these keys.
    dfa.arcs = tuple(dfa.arcs.keys())
    assert dfa.arcs == (u"a",)

#     TODO: This test is currently failing.
#     # Note: It is important that the NFA for "a" be reduced.
#     # The whole point of make_dfa

# Generated at 2022-06-13 18:10:12.443185
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    print(ParserGenerator._test_ParserGenerator_make_first.__doc__)
    #
    # Setup a ParserGenerator
    pg = ParserGenerator()
    pg.dfas['expr'] = []
    pg.symbol2number['expr'] = 0
    pg.first['expr'] = {'x': 1, '(' : 1 }
    #
    # Call the method.
    c = pg.make_first(pg, 'expr')
    #
    # Check the results.
    assert type(c) is dict, c
    assert '(' in c.keys(), c.keys()
    assert 'x' in c.keys(), c.keys()
    #
    # Return success.
    return 0

# Generated at 2022-06-13 18:10:15.611630
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    parser = ParserGenerator()
    parser.parse()
    parser.dump_nfa('x', parser.dfas['x'][0], parser.dfas['x'][0])