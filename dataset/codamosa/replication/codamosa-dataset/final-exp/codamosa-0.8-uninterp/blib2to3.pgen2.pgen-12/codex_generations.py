

# Generated at 2022-06-13 18:02:37.107702
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    from . import grammar_nt

    class Test:
        def __init__(self, value: Text, type: int, expected: Tuple["NFAState", "NFAState"]) -> None:
            self.value = value
            self.type = type
            self.expected = expected
            self.pg = ParserGenerator(grammar_nt)
            self.a, self.z = self.pg.parse_atom()

        def __repr__(self) -> Text:
            return "Test(%r, %r, %r)" % (self.value, self.type, self.expected)

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Test):
                return NotImplemented
            # pylint: disable=protected-access

# Generated at 2022-06-13 18:02:44.618760
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    def do(file):
        with tokenize.open(file) as f:
            code = f.read()
        print("\n=== Source code ===\n{}".format(code))
        gen = ParserGenerator()
        gen.check_grammar(code, file)
    
    this_dir = path.dirname(__file__)
    data_dir = path.join(this_dir, 'data')
    print("Data dir is {}".format(data_dir))
    do(path.join(data_dir, "demo1.py"))
    do(path.join(data_dir, "demo2.py"))

# Generated at 2022-06-13 18:02:54.714302
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    f = io.StringIO(
        """
    start: a
    a: b "|" d
    b: c
    c: "b"
    d: "d"
    """.strip()
    )
    pg = ParserGenerator()
    g = pg.make_grammar(f)
    assert g.keywords == {}

    assert g.start == g.symbol2number["start"]
    assert g.start == 0

    assert g.symbol2number == {"a": 0, "b": 1, "c": 2, "d": 3, "start": 4}
    assert g.number2symbol == {0: "a", 1: "b", 2: "c", 3: "d", 4: "start"}


# Generated at 2022-06-13 18:02:59.488688
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    pg.filename = "--test--"
    pg.generator = pg.tokenize_string(u"if|ifelse")
    pg.gettoken()
    a, z = pg.parse_rhs()
    pg.make_dfa(a, z)
    pg.make_dfa(a, z)  # second time should not change anything

test_ParserGenerator_parse_rhs()


# Generated at 2022-06-13 18:03:03.682349
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    pgen = ParserGenerator()
    pgen.make_fa('s', [('s', [('s', ['B', 'a']), ('s', ['A', 'b'])]), ('s', ['A', 'A'])])
    pgen.addfirstsets()
    assert pgen.first == {'s': {'A': 1, 'B': 1}}

# Generated at 2022-06-13 18:03:16.357314
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    import pytest
    import pgen2.parser
    from typing import Tuple, Dict
    from pgen2 import pgen
    from pgen2.pgen import PgenGrammar
    from pgen2.pgen_grammar import DFAState
    from pgen2.pgen2_parse import ParseResults
    
    
    
    # Test data for parse
    # Each list element is a tuple:
    #  First element is a list of lines constituting the input to
    #   the parse method
    #  Second element is a tuple of the expected grammar attributes
    #   after the parse method is called
    #  Third element is the expected return value of the parse method
    #   when called with the given input

# Generated at 2022-06-13 18:03:32.666609
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    import unittest

    class Test_ParserGenerator_simplify_dfa(unittest.TestCase):
        def test(self):
            p = ParserGenerator()
            s0 = DFAState({}, 0)
            p.simplify_dfa([s0])
            s1 = DFAState({}, 0)
            s1.addarc(s0, "a")
            p.simplify_dfa([s1, s0])
            s0.addarc(s1, "b")
            p.simplify_dfa([s1, s0])
            s2 = DFAState({}, 0)
            s3 = DFAState({}, 0)
            s3.addarc(s1, "a")
            s3.addarc(s2, "b")
            p

# Generated at 2022-06-13 18:03:41.484068
# Unit test for method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:03:46.928161
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    import io

    s = io.StringIO()
    PG = ParserGenerator()
    PG.dump_nfa("foo", PG.start, PG.start)
    output = s.getvalue()
    assert output == "Dump of NFA for foo\n  State 0\n    -> 1\n"



# Generated at 2022-06-13 18:03:49.856687
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pgen = ParserGenerator()
    pgen.parse_rhs()

# Generated at 2022-06-13 18:04:32.520661
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    cases = (
        ("hoge | foo | bar", "hoge foo bar"),
        ("hoge", "hoge"),
        ("hoge | foo", "hoge foo"),
        ("[hoge]", "hoge"),
        ("[hoge | foo]", "hoge foo"),
        ("[ [hoge] | foo]", "hoge foo"),
        ("hoge [foo | bar] | baz", "hoge foo bar baz"),
        ("hoge foo + | baz", "hoge(foo)+ baz"),
        ("hoge foo * | baz", "hoge(foo)* baz"),
    )
    for s, t in cases:
        pg = ParserGenerator()

# Generated at 2022-06-13 18:04:33.914811
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pgen = PgenGrammar()  # check that it works



# Generated at 2022-06-13 18:04:42.802564
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    # Test method make_label of class ParserGenerator
    c = PgenGrammar(None, 10, 10)
    p = ParserGenerator()
    p.symbol2number = {'file_input': 0}
    p.labels = [(0, None)]
    p.tokens = {
        1: 1, 2: 2, 4: 3, 58: 4, 257: 5, 258: 6, 259: 7, 260: 8, 261: 9
    }

# Generated at 2022-06-13 18:04:44.211415
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    g = grammar.Grammar()
    pg.prepare(g)
    pg.parse_rhs()



# Generated at 2022-06-13 18:04:48.793698
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    def test(s, result, sep=" ", *, start=0):
        s = s.replace(" ", "")
        gen = pg.parse_rhs(s, start=start)
        got = next(gen)
        try:
            assert_equal(got, result)
        except:
            print("Want:", repr(result))
            print("Got: ", repr(got))
            raise

    test('', ('', 0))
    test('a', ('a', 1))
    test('a|b', ('|', 0), result=('', 1))
    test('(a)', ('(a)', 3))
    test('a|(b)', ('a', 1), result=('|', 0))

# Generated at 2022-06-13 18:04:59.344380
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    p = ParserGenerator()
    p.type = token.NAME
    p.value = "NAME"
    assert p.expect(token.NAME) == "NAME"
    assert p.type == token.NAME
    assert p.value == "NAME"
    p.gettoken = lambda : None  # raw string
    p.type = token.NAME
    p.value = "NAME"
    assert p.expect(token.NAME) == "NAME"
    assert p.type == token.NAME
    assert p.value == "NAME"
    p.gettoken = lambda : None  # raw string
    p.type = token.NAME
    p.value = "NAME"
    assert p.expect(token.NAME, "NAME") == "NAME"
    assert p.type == token.NAME

# Generated at 2022-06-13 18:05:07.065274
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    parser = ParserGenerator([])
    parser.value = "("
    parser.gettoken = lambda: None
    parser.parse_rhs = lambda: parser.parse_item()
    parser.parse_item = lambda: (1, 2)
    assert parser.parse_item() == (1, 2)
    parser.value = "("
    parser.parse_atom = lambda: (2, 3)
    assert parser.parse_item() == (2, 3)
    parser.value = "("
    parser.parse_atom = lambda: (3, 4)
    assert parser.parse_item() == (3, 4)
    parser.value = "("
    parser.parse_atom = lambda: (4, 5)
    parser.value = "+"
    assert parser.parse_item() == (4, 5)
    parser

# Generated at 2022-06-13 18:05:10.247907
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    import doctest
    import pgen
    doctest.run_docstring_examples(pgen.ParserGenerator.make_dfa, globals())

# Generated at 2022-06-13 18:05:17.681409
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    from . import pgen
    import re
    import io
    import types
    import unittest

    class PGrammarTest(unittest.TestCase):
        def test_make_dfa(self):
            pgen = pgen.ParserGenerator()

# Generated at 2022-06-13 18:05:23.319389
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    p = ParserGenerator()
    try:
        p.raise_error('error message')
    except SyntaxError as exc:
        assert str(exc) == "error message"
        assert exc.filename == None
        assert exc.lineno == 0
        assert exc.offset == 0
        # assert exc.text == None
    else:
        assert False, "invalid exception"


# Generated at 2022-06-13 18:06:37.775431
# Unit test for method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:06:48.873334
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    parser = ParserGenerator()
    dfa = []
    state_a = DFAState({}, None)
    dfa.append(state_a)
    state_b = DFAState({}, None)
    dfa.append(state_b)
    state_c = DFAState({0: 1}, None)
    dfa.append(state_c)
    state_d = DFAState({1: 1}, None)
    dfa.append(state_d)
    state_e = DFAState({}, None)
    dfa.append(state_e)
    state_f = DFAState({}, None)
    dfa.append(state_f)
    state_g = DFAState({2: 1}, None)
    dfa.append(state_g)
    state_h = DFA

# Generated at 2022-06-13 18:07:00.333093
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():

    # Test that the make_first method in the ParserGenerator class is
    # implemented correctly.  Note that this routine does not actually
    # test the make_first method.  Instead, it tests the calcfirst
    # and addfirstsets methods because make_first depends on the order
    # of the arguments and that order is not known at the time
    # make_first was implemented.
    pg = ParserGenerator()
    pg.dfas = {
        # List of DFAState instances
        "start": [DFAState({pg.make_nfastate(0, 0): 1}, None)],
        "expr": [DFAState({pg.make_nfastate(1, 0): 1}, None)],
        "factor": [DFAState({pg.make_nfastate(2, 0): 1}, None)],
    }

# Generated at 2022-06-13 18:07:17.039117
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    # Parsing
    def do(input):
        print("do(%r)" % (input,))
        pg = ParserGenerator()
        dfa, startsymbol = pg.parse(input)
        pg.addfirstsets()
        c = pg.make_converter()
        print(c.tokens)
        print(c.keywords)
        print(c.start)
        print(c.labels)
        for i, states in enumerate(c.states):
            if i in c.dfas:
                print("DFA for", c.number2symbol[i])
            for j, arcs in enumerate(states):
                print("  State", j)
                for label, next in arcs:
                    print("    %s -> %d" % (label, next))


# Generated at 2022-06-13 18:07:22.763604
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    from . import token as token_mod

    def make_pgen(grammar: Text) -> ParserGenerator:
        c = ParserGenerator(grammar)
        c.addfirstsets()
        c.make_pgen_grammar()
        return c

    c = make_pgen("""
        start: NUMBER
        NUMBER: '0' | '1'
        """)
    assert c.labels == [(token_mod.NUMBER, None), (self.symbol2number["NUMBER"], None)]
    assert c.dfas[self.symbol2number["start"]][1] == {
        c.labels[1][0]: 1
    }

    c = make_pgen("""
        start: foo 'b'
        foo: 'a'
        """)
    assert c.lab

# Generated at 2022-06-13 18:07:24.132153
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    pg = ParserGenerator()
    pg.gettoken()

# Generated at 2022-06-13 18:07:27.559824
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator(StringIO("foo: 'foo' | bar"))
    pg.make_dfas()
    pg.addfirstsets()
    assert pg.first['foo'] == {'foo': 1}



# Generated at 2022-06-13 18:07:31.469145
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    pg = ParserGenerator(tokenize.generate_tokens('"test"'))
    pg.gettoken()
    assert pg.type == token.STRING
    assert pg.value == "test"
    pg.gettoken()
    assert pg.type == token.ENDMARKER
    assert pg.value == ""
    pg.gettoken()
    assert False


# Generated at 2022-06-13 18:07:36.004049
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    pgen = ParserGenerator()
    stream = io.StringIO('A: "foo"\n')
    stream = tokenize.generate_tokens(lambda: stream.readline())
    pgen.generator = stream
    pgen.gettoken()
    pgen.expect(token.NAME)
    pgen.expect(token.OP, ":")
    pgen.expect(token.STRING)
    pgen.expect(token.NEWLINE)


# Generated at 2022-06-13 18:07:41.453445
# Unit test for function generate_grammar
def test_generate_grammar():
    p = ParserGenerator(Path(__file__).with_name("Grammar.txt"))
    g, default_rule = p.make_grammar()
    assert default_rule == "single_input", default_rule
    assert g[default_rule].keys() == {0}, g[default_rule].keys()

if __name__ == "__main__":
    test_generate_grammar()

# Generated at 2022-06-13 18:10:01.032855
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    from pgen2.pgen import ParserGenerator
    pg = ParserGenerator()
    pg.build_grammar('{"a": "b"}')
    pg.make_pgen()
    pg.pgen.write('pgen_test.py')


# Generated at 2022-06-13 18:10:05.257524
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    # See issue #16453
    pg = ParserGenerator()
    pg.make_grammar(grammar, tokens)


# Generated at 2022-06-13 18:10:07.305900
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    p = ParserGenerator(StringIO("(x)"))
    assert p.parse_atom() == p.parse_atom()


# Generated at 2022-06-13 18:10:17.181894
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    print("test_ParserGenerator_dump_nfa ...")
    # Create a class that prints everything to stdout
    class MyParserGenerator(ParserGenerator):
        def __init__(self):  # type: ignore
            ParserGenerator.__init__(self)

        def dump_nfa(self, name, start, finish):
            print("Dump of NFA for", name)
            todo = [start]
            for i, state in enumerate(todo):
                print("  State", i, state is finish and "(final)" or "")
                for label, next in state.arcs:
                    if next in todo:
                        j = todo.index(next)
                    else:
                        j = len(todo)
                        todo.append(next)

# Generated at 2022-06-13 18:10:22.626054
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    pg.gettoken = lambda: None
    pg.value = "a"
    while 1:
        try:
            a, z = pg.parse_alt()
        except SyntaxError:
            break
        assert a is z, "unexpected non-empty ALT"
        assert a.arcs == []
        pg.value = pg.value + "a"

# Generated at 2022-06-13 18:10:33.141376
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    # From #15155
    pg = ParserGenerator(["expr"], """
    expr: cmp_expr ('or' cmp_expr)*
    cmp_expr: arith_expr ('<'|'>'|'=='|'>='|'<='|'<>'|'!=') arith_expr
    arith_expr : term ('+'|'-') term
    term: factor ('*'|'/') factor
    factor: INTEGER | '(' expr ')'
    """)

# Generated at 2022-06-13 18:10:40.977189
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    pg = ParserGenerator()
    pg.symbol2number['NAME'] = 1
    pg.symbol2number['NUMBER'] = 2
    pg.symbol2number['STRING'] = 3
    pg.symbol2number['some_name'] = 4
    pg.symbol2number['some_other_name'] = 5
    pg.symbol2number['foo'] = 6
    pg.tokens[token.OP] = 10
    pg.tokens[token.NAME] = 11
    pg.tokens[token.NUMBER] = 12

    pg.labels.append((101, None))
    pg.labels.append((102, None))
    pg.labels.append((103, None))
    pg.labels.append((104, None))

# Generated at 2022-06-13 18:10:43.387963
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    grammar = ParserGenerator()
    s = grammar.parse("a = b c\nc = 'c'\nb = 'b'")
    aa = s.dfas["a"][0]
    grammar.dump_nfa("a", aa, aa)


# Generated at 2022-06-13 18:10:47.862588
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    pg = ParserGenerator()
    with pytest.raises(SyntaxError) as pytest_wrapped_e:
        pg.raise_error("%s should be %s", 1, 2)
    assert pytest_wrapped_e.type == SyntaxError
    assert pytest_wrapped_e.value.msg == "1 should be 2"
    assert pytest_wrapped_e.value.filename == "None"
    assert pytest_wrapped_e.value.lineno == 0
    assert pytest_wrapped_e.value.offset == 0
    assert pytest_wrapped_e.value.text == ""



# Generated at 2022-06-13 18:10:56.770992
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    pg = ParserGenerator()

    def _p(g, *args, **kwds) -> None:
        pg.add_production(*args, **kwds)

    _p("expr", ["term"], ["expr", "+", "term"])
    _p("term", ["factor"], ["term", "*", "factor"])
    _p("term", ["factor"], ["term", "/", "factor"])
    _p("factor", ["'('", "expr", "')'"], ["NAME"])
    _p("factor", ["NUMBER"])

    # dfas, startsymbol = pg.parse_grammar(text)
    dfas, startsymbol = pg.parse_grammar(EXPR_GRAMMAR)
    assert startsymbol == "expr", startsymbol