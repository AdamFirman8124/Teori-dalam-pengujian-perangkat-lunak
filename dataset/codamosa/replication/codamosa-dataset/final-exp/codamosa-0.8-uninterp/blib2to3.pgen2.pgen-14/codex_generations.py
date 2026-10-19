

# Generated at 2022-06-13 18:02:38.428436
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    import io
    import tokenize
    p = ParserGenerator()
    p.filename = "foo.py"
    p.line = 'a:"b"\n'
    p.type, p.value = tokenize.NAME, "a"
    p.begin = (1, 1)
    p.end = (1, 2)
    assert p.expect(tokenize.NAME, "a") == "a"
    assert p.value == ":"
    assert p.type == tokenize.OP
    assert p.expect(tokenize.OP, ":") == ":"
    p.type, p.value = tokenize.STRING, '"b"'
    p.begin = (1, 3)
    p.end = (1, 4)

# Generated at 2022-06-13 18:02:46.423744
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.initialize_dfas(spark_grammar.grammar, spark_grammar.syms, spark_grammar.keywords)
    pg.addfirstsets()
    assert pg.first["atom"] == set(
        ["[", "(", "NAME", '"True"', '"False"', '"None"', "'+'", "'-'", "'~'"]
    )
    assert pg.first["fpdef"] == set(["'('", "NAME"])
    assert pg.first["atom_expr"] == set(["[", "(", "NAME", '"True"', '"False"', '"None"', "'+'", "'-'", "'~'"])

# Generated at 2022-06-13 18:02:55.462194
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    PgenGrammar(b'a : "a"').parse_item()
    PgenGrammar(b'a : "a" ').parse_item()
    PgenGrammar(b'a : "a" +').parse_item()
    PgenGrammar(b'a : "a" [ "a" ]').parse_item()
    PgenGrammar(b'a : "a" [ "a" ] +').parse_item()
    PgenGrammar(b'a : "a" [ "a" ] *').parse_item()
    PgenGrammar(b'a : ( "a" )').parse_item()
    PgenGrammar(b'a : ( "a" ) +').parse_item()

# Generated at 2022-06-13 18:03:05.458729
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    generator = ParserGenerator()
    def test(s, expected):
        it = iter(s.split())
        gen = generator.parse_item()
        actual = tuple(next(gen) for _ in range(2))
        assert actual == expected, repr(actual)
    test("[a]", (NFAState(), NFAState()))
    test("a", (NFAState(), NFAState()))
    test("a +", (NFAState(), NFAState()))
    test("a *", (NFAState(), NFAState()))
    test("(a)", (NFAState(), NFAState()))
test_ParserGenerator_parse_item()

##    def dump_dfa(self, name, dfa):
##        print "Dump of DFA for", name
##        for i, state in

# Generated at 2022-06-13 18:03:18.075391
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    gen = ParserGenerator()
    gen.add_rhs(["a"], ["a"])
    gen.dfas["S"].append(DFAState({"a"}))
    gen.dfas["S"].append(DFAState({"a"}))
    gen.dfas["S"].append(DFAState({"a"}))
    gen.dfas["S"].append(DFAState({"a"}))
    gen.add_rhs(["a"], ["a"])
    gen.dfas["S"].append(DFAState({"a"}))
    gen.dfas["S"].append(DFAState({"a"}))
    gen.dfas["S"].append(DFAState({"a"}))

# Generated at 2022-06-13 18:03:20.839697
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.make_dfa = lambda *args: [DFAState({}, None)]
    pg.calcfirst("foo")
test_ParserGenerator_calcfirst()


# Generated at 2022-06-13 18:03:29.171354
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    from .parser_generator import ParserGenerator  # imported here to avoid circular import
    import io  # this module's types depend on parser_generator
    import sys

    pgen = ParserGenerator(sys.stdin)
    pgen.parse()
    dfas = pgen.dfas
    log_stream = io.StringIO()
    pgen.dump_dfa("start", dfas["start"], file=log_stream)

# Generated at 2022-06-13 18:03:37.121487
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    pg = ParserGenerator()
    pg.filename = "test_filename"
    pg.end = (1, 2)
    pg.line = "test_line"
    try:
        pg.raise_error("test_msg")
    except SyntaxError as e:
        assert e.msg == "test_msg"
        assert e.filename == "test_filename"
        assert e.lineno == 1
        assert e.offset == 2
        assert e.text == "test_line"
    else:
        assert False, "expected SyntaxError"



# Generated at 2022-06-13 18:03:47.488236
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    tests = [
        ("[a b]", "(['a', 'b'], [])"),
        ("a b", "('a', 'b')"),
        ("a+", "('a', 'a')"),
        ("a*", "('a', 'a')"),
        ("a", "('a', 'a')"),
    ]
    pg = ParserGenerator()
    for s, expected in tests:
        a, z = pg.parse_item()
        print((a, z), expected)
        assert (a, z) == eval(expected)
    print('ParserGenerator.parse_item passes test')


# Generated at 2022-06-13 18:03:53.083541
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    pg = ParserGenerator()
    with pytest.raises(SyntaxError) as excinfo:
        pg.raise_error("Cannot be zero")
    assert str(excinfo.value) == "Cannot be zero"



# Generated at 2022-06-13 18:04:42.609256
# Unit test for method dump_dfa of class ParserGenerator

# Generated at 2022-06-13 18:04:51.657068
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    p = ParserGenerator()
    a = NFAState()
    z = NFAState()
    a.addarc(z, "a")
    a.addarc(z, "b")
    a.addarc(z, "c")
    dfa = p.make_dfa(a, z)
    assert len(dfa) == 2
    assert dfa[0].arcs == {"a": dfa[1], "b": dfa[1], "c": dfa[1]}
    assert dfa[0].nfaset == {a}
    assert dfa[1].nfaset == {z}


# Generated at 2022-06-13 18:05:03.264175
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    # The method gettoken() reads and returns a token from the given grammar string.
    # It calls the tokenize() method to get tokens.
    # It ignores tokens of type tokenize.NL and tokenize.COMMENT.
    # The code below is a mock tokenize() method that returns the given list of tokens.
    tokenize_output = iter([
        (tokenize.NL, "\n", (0, 0), (0, 1), ""),
        (tokenize.NAME, "token", (1, 0), (1, 5), "token"),
        (tokenize.OP, ":", (1, 6), (1, 7), ":"),
        (tokenize.STRING, "abc", (1, 8), (1, 11), "abc")
    ])
    parser = ParserGenerator("test")
    parser.generator = token

# Generated at 2022-06-13 18:05:10.297215
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    s = ParserGenerator()
    a = s.make_dfa(*s.parse_rhs())
    s.simplify_dfa(a)
    s.dump_dfa("foo", a)
    print("How many states", len(a))
    assert len(a) == 1


# End of unit test for method simplify_dfa of class ParserGenerator

# Generated at 2022-06-13 18:05:17.699707
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    dfa: List[DFAState] = []
    a = DFAState(1)
    b = DFAState(2)
    c = DFAState(3)
    d = DFAState(4)
    e = DFAState(5)
    dfa.append(a)
    dfa.append(b)
    dfa.append(c)
    dfa.append(d)
    dfa.append(e)
    a.addarc(b, 'a')
    a.addarc(c, 'b')
    b.addarc(c, 'b')
    c.addarc(d, 'c')
    d.addarc(b, 'b')
    d.addarc(e, 'd')
    e.addarc(d, 'd')
    pg = ParserGenerator

# Generated at 2022-06-13 18:05:22.960674
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    pg.generator = iter([(1, "foo", (1, 0), (1, 3), "foo"),
                         (2, ":", (1, 3), (1, 4), ":")])
    pg.gettoken()
    assert pg.parse_rhs() == ([], [])
    pg.generator = iter([(1, "foo", (1, 0), (1, 3), "foo"),
                         (2, ":", (1, 3), (1, 4), ":"),
                         (1, "bar", (1, 4), (1, 7), "bar"),
                         (4, "\n", (1, 7), (1, 8), "\n")])
    pg.gettoken()

# Generated at 2022-06-13 18:05:34.576217
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    pg = ParserGenerator(grammar)
    dfa = pg.make_dfa(NFAState(), NFAState())
    assert len(dfa) == 1
    assert dfa[0].arcs == {}
    assert dfa[0].isfinal is True

    a = NFAState()
    b = NFAState()
    c = NFAState()
    d = NFAState()
    e = NFAState()
    f = NFAState()
    g = NFAState()
    h = NFAState()

    a.addarc(b, "a")
    a.addarc(c, "b")
    b.addarc(d, "a")
    b.addarc(e, "b")
    d.addarc(f, "a")

# Generated at 2022-06-13 18:05:45.316609
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    c = ParserGenerator()
    assert c.make_label(c, "expr") == 0
    assert c.make_label(c, "'id'") == 0
    assert c.make_label(c, '"if"') == 0
    assert c.make_label(c, '"def"') == 1
    assert c.make_label(c, '"elif"') == 2
    assert c.make_label(c, '"else"') == 3
    assert c.make_label(c, "NAME") == 0
    assert c.make_label(c, "NUMBER") == 1
    assert c.make_label(c, "STRING") == 2
    assert c.make_label(c, "'('") == 0
    assert c.make_label(c, "'+'") == 1
   

# Generated at 2022-06-13 18:05:56.341166
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    import unittest
    
    pg = ParserGenerator()

# Generated at 2022-06-13 18:06:06.051488
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    class ParserGenerator(ParserGenerator):
        def make_dfa(self, start: "NFAState", finish: "NFAState") -> List["DFAState"]:
            return start, finish
    from collections import OrderedDict
    import io
    lhs, rhs = 'foo', '{a: x=y}[("int"|"string")]'
    p = ParserGenerator(io.StringIO(lhs + ': ' + rhs))
    expected = (NFAState(arcs=((None, NFAState(arcs=((None, NFAState(arcs=(
        ('{a: x=y}', NFAState(final=True)),
    ))), ('[("int"|"string")]', NFAState(final=True))))),)), NFAState(final=True))


# Generated at 2022-06-13 18:06:59.402292
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    from . import parser
    from .pgen2 import grammar
    from .pgen2 import token

    def check_rules(grmr):
        for name in grmr.dfas:
            for state in grmr.dfas[name]:
                for label, next in state.arcs.items():
                    assert label is None or label in grmr.first[name]

    def check_grammar(rules):
        print("Testing grammars:")
        for name, contents in sorted(rules.items()):
            print("  %s" % name)
            grmr = ParserGenerator().parsestr(contents)
            grmr.addfirstsets()
            check_rules(grmr)
            c = grmr.converter()
            # XXX
            # grammar.check_grammar(c)
            # XXX

# Generated at 2022-06-13 18:07:03.257505
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    with open("Grammar.txt", "r", encoding="utf-8") as f:
        text = f.read()
    pg = ParserGenerator()
    pg.parse_grammar(text)
    assert pg.build_parser() is not None

if __name__ == "__main__":
    test_ParserGenerator()

# Generated at 2022-06-13 18:07:17.331994
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    import unittest

    class TestStringMethods(unittest.TestCase):

        class NFAState:
            def __init__(self):
                self.arcs = []
                self.isfinal = False

            def addarc(self, next, label=None):
                self.arcs.append((label, next))

        def test_make_dfa(self):
            start = self.NFAState()
            finish = self.NFAState()
            finish.isfinal = True
            start.addarc(start, "a")
            start.addarc(start, "b")
            start.addarc(finish)
            dfa = ParserGenerator.make_dfa(start, finish)
            self.assertEqual(len(dfa), 2)

# Generated at 2022-06-13 18:07:26.590142
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    print("test_ParserGenerator_dump_dfa ...", end="")
    pg = ParserGenerator()
    nfa = pg.parse_atom()
    dfa = pg.make_dfa(nfa[0], nfa[1])
    pg.simplify_dfa(dfa)
    pg.dump_dfa("foo", dfa)
    print("Done.")

# Helper for testing

# Generated at 2022-06-13 18:07:34.272190
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():

    class DFAState:

        def __init__(self, nfaset, finish):
            self.nfaset: Dict[NFAState, int] = nfaset
            self.finish = finish
            self.isfinal = finish in nfaset
            self.arcs: Dict[str, "DFAState"] = {}

        def __repr__(self):
            return "<DFAState %x>" % id(self)

        def __eq__(self, other):
            return self.arcs == other.arcs

        def addarc(self, state, label):
            self.arcs[label] = state

        def unifystate(self, state1, state2):
            for label, state in self.arcs.items():
                if state is state1:
                    self.arcs

# Generated at 2022-06-13 18:07:41.422845
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator(io.StringIO("abc\ndef\n"), "f")
    a, z = pg.parse_rhs()
    assert a.getarcs() == {None: {z}}
    assert z.getarcs() == {"abc": {}}
    assert z.getarcs(symbols={"def"}) == {"def": {}}

    pg = ParserGenerator(io.StringIO("'a'\n'b'\n"), "f")
    a, z = pg.parse_rhs()
    assert a.getarcs() == {None: {z}}
    assert z.getarcs() == {"'a'": {}}
    assert z.getarcs(symbols={"'b'"}) == {"'b'": {}}

    # Test bug #15149

# Generated at 2022-06-13 18:07:45.394757
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():

    # body of test_ParserGenerator_calcfirst

    pg = ParserGenerator()
    dfa = {}
    pg.dfas = dfa
    pg.addfirstsets()



# Generated at 2022-06-13 18:07:57.969770
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    text = """
# match a simple arithmetic expression
expr: term ('+' term)*
term: factor ('*' factor)*
factor: NAME | NUMBER | '(' expr ')'
"""
    pg = ParserGenerator()
    dfa = pg.make_generator(io.StringIO(text))
    # pg.dump_nfa("expr", dfa[0])
    # pg.dump_nfa("term", dfa[1])
    # pg.dump_nfa("factor", dfa[2])

    text = """
# match a simple arithmetic expression
expr: term ('+' term)*
term: factor ('*' factor)*
factor: NAME | NUMBER | '(' expr ')'
"""
    pg = ParserGenerator()
    dfa = pg.make_generator(io.StringIO(text))
    #

# Generated at 2022-06-13 18:08:02.969203
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    pgen = ParserGenerator()
    dfa = [
        DFAState({NFAState(): 1, NFAState(): 1}, NFAState()),
        DFAState({NFAState(): 1, NFAState(): 1}, NFAState()),
        DFAState({NFAState(): 1, NFAState(): 1}, NFAState()),
    ]
    dfa[0].addarc(dfa[1], "a")
    dfa[1].addarc(dfa[2], "b")
    dfa[2].addarc(dfa[0], "c")
    pgen.simplify_dfa(dfa)
    assert len(dfa) == 1
    assert dfa[0].nfaset == {NFAState(): 1, NFAState(): 1}

# Generated at 2022-06-13 18:08:14.498600
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    import io

    from . import tokenize

    filename = "some_file.py"
    file = io.StringIO(
        dedent(
            """\
        def some_method(self):
            # some comment
        """
        )
    )
    generator = tokenize.generate_tokens(file.readline)
    parser = ParserGenerator(filename, generator)
    parser.gettoken()
    parser.gettoken()
    try:
        parser.raise_error("expected %s/%s, got %s/%s", "foo", "bar", "baz", "buz")
    except SyntaxError as e:
        msg = str(e)
        assert msg == "expected foo/bar, got baz/buz"
        assert e.filename == filename

# Generated at 2022-06-13 18:09:08.167856
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    assert isinstance(PgenGrammar("pgen_grammar"), grammar.Grammar)


# Generated at 2022-06-13 18:09:22.733732
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    s = r"""
expr:
    | expr '+' term
    | expr '-' term
    | expr '*' term
    | expr '/' term
    | expr '^' term
    | '-' expr
    | term
term:
    | term ID
    | term '(' expr ')'
    | '(' expr ')'
    | NUMBER
    | ID
        """

    # XXX remove any pyc or pycache file
    # XXX replace the generator with a mock
    generator = pg.tokenize(s)
    # next(generator) # skip first token (NEWLINE)
    pg.type, pg.value = next(generator) #  expr
    pg.gettoken = lambda : None
    pg.generator = generator
    # print("accept", pg.value)


# Generated at 2022-06-13 18:09:37.206702
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    from _geninterp import PgenGrammar, PgenParser
    pgen = ParserGenerator()
    c: PgenGrammar = pgen.make_pgen_grammar()
    p: PgenParser = PgenParser(c)
    assert p.handle_token(token.NAME, "foo") == c.symbol2number["foo"]
    assert p.handle_token(token.NUMBER, "1") == c.symbol2number["NUMBER"]
    assert p.handle_token(token.STRING, "1") == c.symbol2number["STRING"]
    assert p.handle_token(token.DEDENT, "1") == c.symbol2number["DEDENT"]

# Generated at 2022-06-13 18:09:44.559733
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    # ParserGenerator.__init__(source: str, filename: str) -> None
    # ParserGenerator.expect(type: int, value: Optional[Any]) -> Text
    pg = ParserGenerator("")
    try:
        pg.expect(token.NAME, "abc")
    except SyntaxError:
        pass
    try:
        pg.expect(token.NAME, "abc")
    except SyntaxError as e:
        assert e.msg == "expected NAME/abc, got ENDMARKER/None"
        assert e.lineno == 1
    try:
        pg.expect(token.NAME, "abc")
    except SyntaxError:
        pass
    try:
        pg.expect(token.NAME)
    except SyntaxError:
        pass

# Generated at 2022-06-13 18:09:46.603056
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    p = ParserGenerator()
    p.dump_dfa("root", [DFAState({}, {})])

# Generated at 2022-06-13 18:09:54.123624
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    from . import pgen

    gram = pgen.ParserGenerator()

    # Check that recursive definitions report a SyntaxError
    gram.addproduction("A : 'a' A")

    with pytest.raises(SyntaxError):
        gram.calcfirst("A")

    # Check that recursive definitions that are not actually used
    # do not report a SyntaxError
    gram = pgen.ParserGenerator()
    gram.addproduction("A : 'a'")
    gram.addproduction("A : 'b' A")
    gram.addproduction("B : 'b' A")
    gram.calcfirst("B")

    # Check that rules that require a token that can be empty
    # cause a SyntaxError to be raised.
    gram = pgen.ParserGenerator()

# Generated at 2022-06-13 18:10:02.717135
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():  # pylint: disable=uncontrollable-flow
    # pylint: disable=line-too-long
    # The method parse_atom is called in a loop, and the tests have to
    # reproduce that.  Each test needs to end with a token that's not
    # NAME or STRING so that the loop will exit.

    class MockTokenizer:
        def __init__(self, tokens):
            self.tokens = tokens
            self.i = -1

        def __next__(self):
            self.i += 1
            return self.tokens[self.i]


# Generated at 2022-06-13 18:10:07.305789
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    data = """
# A comment
expr: x '+' y    # Another comment
    | x
"""
    dfa, startsymbol = pg.parse(data)
    assert dfa
    assert startsymbol == "expr"

# Generated at 2022-06-13 18:10:16.796319
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    pg.add_nonterminal(b"NEWLINE", b"\n")
    pg.add_nonterminal(b"NUMBER", b"[0-9]+")
    pg.add_nonterminal(b"ADD", b"[+-]")
    pg.add_nonterminal(b"MULT", b"[*/%]")
    pg.add_nonterminal(b"POINT", b"[.]")
    pg.add_nonterminal(b"LPAREN", b"[(]")
    pg.add_nonterminal(b"RPAREN", b"[)]")
    pg.add_nonterminal(b"POWER", b"[**]")
    pg.add_nonterminal(b"WS", b"[ \t]")
    pg.add_nonterminal

# Generated at 2022-06-13 18:10:26.355880
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    ## # This is too simplistic for the real grammar parser...
    ## p = ParserGenerator({}, {})
    ## a = DFAState({}, 'a')
    ## b = DFAState({}, 'b')
    ## a.addarc(b, 'a')
    ## b.addarc(a, 'b')
    ## p.dump_dfa('foo', [a, b])
    pass


import token
import tokenize
import grammar
import os
import re
import sys

START = 256
tokens = []  # List of (name, value) pairs used to represent the current file being compiled.
dfas = {}  # Dictionary of {name: [List of DFAState instances]}
symbol2number = {}  # dictionary of {name: number}; used to assign numbers to symbols
symbol2label = {} 