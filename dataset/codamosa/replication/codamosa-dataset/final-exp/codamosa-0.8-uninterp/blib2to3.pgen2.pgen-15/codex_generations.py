

# Generated at 2022-06-13 18:03:08.850359
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    from io import StringIO

    def parse(text: str) -> List["DFAState"]:
        # Create a dummy parser generator object just for the test
        gen = ParserGenerator(StringIO(text))
        return gen.make_dfa(gen.parse_rhs()[0], gen.parse_rhs()[1])

    dfa = parse("a .")
    assert len(dfa) == 3

    dfa = parse("a .")
    assert len(dfa) == 3

    dfa = parse("a*")
    assert len(dfa) == 1

    dfa = parse("a|b")
    assert len(dfa) == 3

    dfa = parse("a (b|c)")
    assert len(dfa) == 4



# Generated at 2022-06-13 18:03:19.620236
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    import Grammar
    import token
    # Define a complete Grammar instance
    g = Grammar.Grammar(Grammar.start)
    # Define a ParserGenerator instance
    pg = ParserGenerator(g)
    # Define a token generator
    tokens = [
        (token.NAME, "whitespace1"),
        (token.OP, ":"),
        (token.NAME, "whitespace2"),
        (token.OP, "|"),
        (token.NAME, "whitespace3"),
        (token.OP, "|"),
        (token.NAME, "whitespace4")
    ]
    token_gen = iter(tokens)
    line = 1
    # Define the initial and ending states
    initial_state = NFAState()
    ending_state = N

# Generated at 2022-06-13 18:03:27.436479
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    from . import _parser_generated
    from . import pygram
    pg = ParserGenerator()
    pg.dump_dfa("a", _parser_generated.dfas["suite"])
    pg.dump_dfa("b", pygram.dfas["suite"])
    for i in range(1, 3):
        pg.dump_dfa("x", _parser_generated.dfas["eval_input"])
        pg.dump_dfa("y", pygram.dfas["eval_input"])
    pg.dump_dfa("c", _parser_generated.dfas["file_input"])
    pg.dump_dfa("d", pygram.dfas["file_input"])

# Generated at 2022-06-13 18:03:31.414508
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    if PgenGrammar().__class__.__name__ == "PgenGrammar":
        print("PgenGrammar constructor passed")
    else:
        print("FAILED: PgenGrammar constructor")


# Generated at 2022-06-13 18:03:39.938794
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    pg = ParserGenerator()
    pg.generator = iter([(token.NAME, '"literal"', (0, 12), (0, 22), "")])
    pg.gettoken()
    a, z = pg.parse_atom()
    assert a is not z
    assert z in next(iter(a.arcs.values()))
    assert len(a.arcs) == 1
    assert a.arcs[0][0] == '"literal"'
    assert a.arcs[0][1] is z

test_ParserGenerator_parse_atom()

# Unit tests for class ParserGenerator

# Generated at 2022-06-13 18:03:56.639772
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    parser = ParserGenerator()
    class MockTokenizer:
        def __iter__(self):
            yield tokenize.NAME, 'name', (1, 0), (1, 2), "line"
            yield tokenize.NAME, 'name', (1, 3), (1, 5), "line"
            yield tokenize.NEWLINE, '\n', (1, 6), (1, 7), "line"
            yield token.ENDMARKER, '', (2, 0), (2, 0), ''
    tokenizer = MockTokenizer()
    parser.generator = tokenizer
    parser.filename = 'mock file'
    result = parser.parse_alt()
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0].arcs == [(None, result[1])]
   

# Generated at 2022-06-13 18:04:06.515944
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    import sys
    import io
    import token

    if sys.version_info[:2] >= (3, 8):
        # importlib.metadata is available in Python 3.8+
        import importlib.metadata as importlib_metadata
    else:
        # importlib_metadata is a backport of importlib.metadata for older Python versions
        import importlib_metadata

    pgen_data = importlib_metadata.files("py3kparsing")
    assert pgen_data is not None

    dummy_filename = "test_ParserGenerator_parse_atom"
    dummy_text = (
        "[a b] | c [d e f] g | [h i j] | k 'lmn' | ['op' p] | q r [s t 'u' +] | v"
    )
    generator = tokenize.gener

# Generated at 2022-06-13 18:04:09.347209
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    pg.addtoken("[]")
    a, z = pg.parse_alt()

    assert a.arcs == [(None, z)]
    assert a.label == "ALT"
    assert a.num == 0

    assert z.arcs == []
    assert z.label == "ALT"
    assert z.num == 1



# Generated at 2022-06-13 18:04:15.898968
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    pg = ParserGenerator()
    pg.dfas.clear()
    pg.add_nonterminal("A", [("[", "a", "]")])
    pg.addfirstsets()
    a = pg.dfas["A"][0]
    print(pg.dump_dfa("A", [a]))
    pg.dfas.clear()
    pg.add_nonterminal("B", [("a", "|", "b")])
    pg.addfirstsets()
    b = pg.dfas["B"][0]
    print(pg.dump_dfa("B", [b]))
    pg.simplify_dfa([b])
    print(pg.dump_dfa("B", [b]))

# Generated at 2022-06-13 18:04:26.104469
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    import unittest
    from typing import Tuple
    from . import parser
    from . import pgen2_grammar as grammar
    from . import token
    generator = ParserGenerator(grammar)
    def parse_rhs(s: str) -> Tuple[parser.NFAState, parser.NFAState]:
        return generator.parse_rhs(s)
    def assertEqual(a: object, b: object) -> None:
        assert a == b
    def assertIn(a: object, b: object) -> None:
        assert a in b
    def assertNotIn(a: object, b: object) -> None:
        assert a not in b

# Generated at 2022-06-13 18:05:15.087276
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    pg.make_generator("x: 'x' | 'y'")
    a, z = pg.parse_alt()
    assert len(a.arcs) == 2
    assert len(a.arcs[0][1].arcs) == 1
    pg.make_generator("x: 'x' 'y'")
    a, z = pg.parse_alt()
    assert len(a.arcs) == 1
    assert len(a.arcs[0][1].arcs) == 1
    pg.make_generator("x: 'x'+ 'y'")
    a, z = pg.parse_alt()
    assert len(a.arcs) == 1
    assert len(a.arcs[0][1].arcs) == 2
    pg.make_

# Generated at 2022-06-13 18:05:25.316163
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    import parser
    import os

    # A ParserGenerator instance is needed to instantiate an LALR parser
    pg = parser.ParserGenerator()
    # I copied a generated parser here
    # open the file in python 3x
    f = open(os.path.join(os.path.dirname(__file__), "calc.py"), "r")
    # get all the contents of the file
    content = f.read()
    pg.build(content)
    # instantiate an LALR parser
    # pass the test_make_label_A

# Generated at 2022-06-13 18:05:35.766179
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    from . import parser_generator
    from .parser_generator import ParserGenerator
    import io
    import unittest


# Generated at 2022-06-13 18:05:42.557303
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    g = ParserGenerator()
    def test(input, output):
        if isinstance(input, str):
            input = list(g._tokenize(io.StringIO(input)))
        a, z = g.parse_atom()
        if a.arcs != output:
            print(a.arcs, "!=", output)
    test(
        [
            (token.NAME, 'NAME'),
        ],
        [('NAME', 1)],
    )
    test(
        [
            (token.STRING, '"S"'),
        ],
        [('S', 1)],
    )

# Generated at 2022-06-13 18:05:45.260869
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    s = 'token_cab = [ "c" | "d" ]'
    g = ParserGenerator(s)


# Generated at 2022-06-13 18:05:56.260783
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    mygrammar = PgenGrammar("<bad-file>", "<bad-data>")
    mygrammar.add_production("1", [("1", None)], "", "", "", "")
    mygrammar.add_production("1", [("1", None)], "", "", "", "")
    mygrammar.add_production("1", [("1", None)], "", "", "", "")
    assert mygrammar.states is None
    assert mygrammar.error_func is None
    assert mygrammar.sr_conflicts is None
    assert mygrammar.rr_conflicts is None
    assert mygrammar.resolve_conflict is None
    assert mygrammar.symbol2number == {"1":0}

# Generated at 2022-06-13 18:06:03.415152
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    generator = ParserGenerator()
    source = '''
S: "if"
S: "if" "not"
S: "if" "not" "a"
S: "if" "not" "a" "b"
S: "if" "not" "a" "b" "c"
S: "if" "not" "a" "b" "c" "d"
S: "while"
S: "while" "not"
S: "while" "not" "a"
S: "while" "not" "a" "b"
S: "while" "not" "a" "b" "c"
S: "while" "not" "a" "b" "c" "d"
'''
    generator.parse_grammar(source)
    generator.addfirstsets()


# Generated at 2022-06-13 18:06:11.336914
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    pg.dfas = {'start': [DFAState({DFAState(set(), DFAState({}))}, DFAState({}))], 'expr': [DFAState({DFAState(set(), DFAState({}))}, DFAState({}))], 'term': [DFAState({DFAState(set(), DFAState({}))}, DFAState({}))], 'factor': [DFAState({DFAState(set(), DFAState({})), DFAState({DFAState(set(), DFAState({}))}, DFAState({}))}, DFAState({}))]}
    startsymbol = 'start'
    pg.startsymbol = startsymbol

# Generated at 2022-06-13 18:06:20.855999
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    from . import grammar
    from .parser import Parser

    def make_parser(grammar_str: str) -> Parser:
        class PyParser(Parser):
            def p_error(self, p: Grammar) -> int:
                raise RuntimeError("syntax error")
        return PyParser(grammar_str)

    def check_rhs(grammar_str: str, exp_rhs: List[List[Tuple[Optional[Text], ...]]]) -> None:
        parser = make_parser(grammar_str)
        parser.make_pgen_grammar(0)
        g = parser.pgen_grammar
        rule = g.grammar[g.symbol2number[g.startsymbol]]
        rhs = rule[1]

# Generated at 2022-06-13 18:06:27.982234
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    c = pg.make_grammar_converter()
    pg.dfas = {'a': [DFAState({}), DFAState({})],
               'b': [DFAState({}), DFAState({})],
               }
    pg.make_first(c, 'a')
    pg.make_first(c, 'b')
    assert c.first == {'a': {}, 'b': {}}


# Generated at 2022-06-13 18:07:11.041341
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    s = r"""
foo:
    'foo'
    | 'bar'
    | 'baz'
    | 'quux'
    | 'spam'
    | 'badger'
"""
    assert ParserGenerator(s).parse_rhs()


# Generated at 2022-06-13 18:07:19.530695
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    rhs = Grammar(
        """
    r : r1 | (r1 r2) | (r1 r2) | (r1 r3) | r4
    r1 : a | b
    r2 : c
    r3 : d
    r4 : e
    """
    )
    pg = ParserGenerator(rhs.rules, rhs.symbol2number)
    pg.addfirstsets()
    first = pg.first

    assert first["r"] == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1}
    assert first["r1"] == {"a": 1, "b": 1}
    assert first["r2"] == {"c": 1}
    assert first["r3"] == {"d": 1}

# Generated at 2022-06-13 18:07:25.919479
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    from test.support import cpython_only
    from test.test_pgen import generate_grammar

    cpython_only("requires C implementation of pgen")

    filename = generate_grammar()
    try:
        with open(filename, "rb") as f:
            pg = ParserGenerator()
            pg.parse_file(f)
    finally:
        os.remove(filename)



# Generated at 2022-06-13 18:07:37.063026
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pgen = ParserGenerator()

    class DFAState:
        def __init__(self, nfaset: Dict[NFAState, int], finish: NFAState) -> None:
            self.nfaset = nfaset
            self.isfinal = finish in nfaset
            self.arcs: Dict[str, DFAState] = {}

        def addarc(self, to: "DFAState", label: str) -> None:
            assert label not in self.arcs
            self.arcs[label] = to

        def unifystate(self, state1: "DFAState", state2: "DFAState") -> None:
            for label, dest1 in list(self.arcs.items()):
                if dest1 is state1:
                    self.arcs[label]

# Generated at 2022-06-13 18:07:41.809557
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    grammar_str = """
    number: /[0-9]+/
    operator: '+'
    """
    pg = ParserGenerator()
    d = eval(pg.pgen(grammar_str))
    c = pg.convert(d)
    assert c.make_label(c, "number") == 1
    assert c.make_label(c, "+") == 2

# Generated at 2022-06-13 18:07:55.376687
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    # The following example is taken from the Dragon Book, Figure 3.34
    p = ParserGenerator()
    a, b, c, d, e, f, g, h, i, z = (
        NFAState() for j in range(10)
    )  # type: NFAState # noqa
    a.addarc(z, "a"); a.addarc(b, "b")
    b.addarc(c, "b"); b.addarc(f, "a")
    c.addarc(d, "b"); c.addarc(e, "a")
    d.addarc(c, "a"); d.addarc(z, "b")
    e.addarc(d, "a"); e.addarc(z, "b")
    f.addarc(g, "a"); f.add

# Generated at 2022-06-13 18:08:04.156919
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pgen = ParserGenerator([])
    class BogusTokenizer:
        def __call__(self, readline):
            while True:
                value = readline()
                if not value:
                    yield 0, "", (1, 1), (1, 1), ""
                for line in value.splitlines():
                    for i, c in enumerate(line):
                        if c.isalpha():
                            yield token.NAME, c, (i + 1, i + 2), (i + 1, i + 2), line
                        else:
                            yield ord(c), c, (i + 1, i + 2), (i + 1, i + 2), line
    pgen.generator = BogusTokenizer()()
    pgen.gettoken()
    assert pgen.type == token.NAME

# Generated at 2022-06-13 18:08:10.643103
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    """Unit test for method expect of class ParserGenerator"""
    pg = ParserGenerator()
    pg.begin = ("beginfile", 1)
    pg.end = ("endfile", 2)
    pg.filename = "filename"
    pg.line = "line"
    try:
        pg.expect(1, 2)
    except SyntaxError:
        pass
    else:
        print("Expected syntax error")



# Generated at 2022-06-13 18:08:19.156139
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    import unittest
    import pgen
    import pgen2
    import io
    import re


# Generated at 2022-06-13 18:08:26.904527
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    from pgen2 import token
    from pgen2.pgen import ParserGenerator
    from pprint import pprint

    pg = ParserGenerator()

    # Create some dummy states with arcs.
    state1 = pg.DFAState({}, None)
    state2 = pg.DFAState({}, None)
    state3 = pg.DFAState({}, None)
    state4 = pg.DFAState({}, None)
    state1.addarc(state2, "1")
    state1.addarc(state3, "2")
    state2.addarc(state1, "1")
    state2.addarc(state3, "3")
    state3.addarc(state1, "2")
    state3.addarc(state2, "3")

# Generated at 2022-06-13 18:10:02.323252
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    def check(source, expected):
        actual = ParserGenerator(source.splitlines()).parse_item()
        assert actual == expected, (actual, expected)
    check("foo", (NFAState(), NFAState(arcs=[(None, NFAState(arcs=[("foo", NFAState())], final=True))], final=False)))
    check("foo*", (NFAState(), NFAState(arcs=[(None, NFAState(arcs=[("foo", NFAState())], final=True))], final=True)))
    check("foo+", (NFAState(), NFAState(arcs=[(None, NFAState(arcs=[("foo", NFAState())], final=True))], final=False)))

# Generated at 2022-06-13 18:10:13.337713
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()

# Generated at 2022-06-13 18:10:19.968769
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    lines = [
        "[a] | [b]",
        "[a]* | [b]*",
        "foo : bar",
        "foo : bar | baz",
        "foo : 'a'",
        "foo : 'a' | 'b'",
    ]
    pg = ParserGenerator()
    grammar = pg.make_grammar(lines, "test_ParserGenerator_make_grammar")
    assert isinstance(grammar, PgenGrammar)
    print(grammar)

# Generated at 2022-06-13 18:10:29.183256
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    # Test
    pgen = ParserGenerator()
    with io.StringIO("# a comment\n\n x: 'a'\n") as fp:
        pgen.generator = tokenize.generate_tokens(fp.readline)
        pgen.gettoken()
        assert (pgen.type, pgen.value) == (token.NAME, "x")
        pgen.gettoken()
        assert (pgen.type, pgen.value) == (token.OP, ":")
        pgen.gettoken()
        assert (pgen.type, pgen.value) == (token.STRING, "a")

# Generated at 2022-06-13 18:10:38.231501
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    from . import parser_interface

    py = parser_interface.PyCF_ONLY_AST

    # The test string is a logically empty grammar with a bytestring
    # comment and a bytestring string. As a result, tokenize will feed
    # in NAME tokens for 'b', 'r', and 'u' and the complete bytestring
    # will be returned by gettoken() as a single STRING token.
    string = b"#abc\nb'''xxx'''"

    gen = ParserGenerator()

    pdict, pstr, pseq, pmap, pset = parser_interface.prepare_grammar_data(
        gen._grammar_string, py
    )
    gen.set_grammar(pdict, pstr, pseq, pmap, pset)

    gen.check_grammar()
    gen

# Generated at 2022-06-13 18:10:39.441414
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    pg.parse_rhs()


# Generated at 2022-06-13 18:10:44.846084
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    g = PgenGrammar({},{})
    try:
        g.get_reserved({})
    except:
        raise TypeError(
        "Error in constructor for class PgenGrammar()")


# Check if grammar files are correct

# Generated at 2022-06-13 18:10:53.862294
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    """Tests ParserGenerator.dump_dfa()."""
    g = ParserGenerator()
    dfa = [
        DFAState(
            {NFAState([((None, NFAState()),), ((None, NFAState()),)]): 1},
            NFAState([((None, NFAState()),)]),
        ),
        DFAState(
            {NFAState([((None, NFAState()),), ((None, NFAState()),)]): 1},
            NFAState([((None, NFAState()),)]),
        ),
        DFAState(
            {NFAState([((None, NFAState()),), ((None, NFAState()),)]): 1},
            NFAState([((None, NFAState()),)]),
        ),
    ]

# Generated at 2022-06-13 18:10:58.406969
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    txt = """
    start: a c
         | b d e
    a: "a"
    b: "b"
    c: "c"
    d: "d"
    e: "e"
    """
    g = ParserGenerator()
    g.parse_grammar(txt)
    g.check_all()
    g.make_parsetab()
    # g.dump_grammar()


# Generated at 2022-06-13 18:11:07.900748
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    from cpython.pgen2.tokenize import generate_tokens, COMMENT, NL, NAME, STRING, OP
    from cpython.pgen2.grammar import parse_grammar
    from io import StringIO
    dfa_file = 'cpython/Lib/tokenize.py'
    with open(dfa_file, "r") as f:
        dfa_source = f.read()

    def make_dfa(dfa_source):
        contents = StringIO(dfa_source)
        generator = generate_tokens(contents.readline)
        parsed = parse_grammar(generator, dfa_file)
        return parsed[0]

    dfas = make_dfa(dfa_source)