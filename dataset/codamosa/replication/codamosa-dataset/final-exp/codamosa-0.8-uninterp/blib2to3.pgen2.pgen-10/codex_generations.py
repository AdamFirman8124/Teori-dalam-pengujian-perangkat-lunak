

# Generated at 2022-06-13 18:02:56.116540
# Unit test for method addfirstsets of class ParserGenerator

# Generated at 2022-06-13 18:02:58.535448
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    src="""["a","b"] | 'a'"""
    pg = ParserGenerator()
    a, z = pg.parse_alt()
    #print(a, z)
    assert False


# Generated at 2022-06-13 18:03:09.089176
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    # Unit test for make_dfa()

    class NFAState:
        __slots__ = "arcs",

        def __init__(self) -> None:
            self.arcs = []

        def addarc(self, nextstate: "NFAState" = None, label: Text = None) -> None:
            self.arcs.append((label, nextstate))

    def make_dfa(start: NFAState, finish: NFAState) -> List["DFAState"]:
        return ParserGenerator.make_dfa(None, start, finish)

    # Test case: simple grammar with no nullable rules.  Two states
    # for the DFA and one for the NFA.
    a = NFAState()
    z = NFAState()
    a.addarc(z, "a")
    d

# Generated at 2022-06-13 18:03:13.507525
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():

    from . import indentparser

    pg = ParserGenerator(indentparser.grammar)
    pg.generate_grammar()

    g = pg.make_grammar(indentparser.converter)

    g.check_consistency()



# Generated at 2022-06-13 18:03:23.662500
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    import os
    import sys
    import unittest

    class ParserGeneratorTestCase(unittest.TestCase):
        def test_ParserGenerator_raise_error(self):
            sys.argv[0] = 'raise_error'
            err = SyntaxError(msg="a", filename="b", lineno=1, offset=2, text="c")
            try:
                raise err
            except SyntaxError as e:
                self.assertEqual(str(e), "a")
                self.assertEqual(e.filename, "b")
                self.assertEqual(e.lineno, 1)
                self.assertEqual(e.offset, 2)
                self.assertEqual(e.text, "c")

    unittest.main()

# Generated at 2022-06-13 18:03:31.400367
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    pg = ParserGenerator()
    result = pg.parse_atom()

# Generated at 2022-06-13 18:03:33.173739
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    # No need to unit test
    pass



# Generated at 2022-06-13 18:03:41.612295
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    p = ParserGenerator()
    # Test case: a*
    a = NFAState(1)
    z = NFAState(2)
    a.addarc(a)
    a.addarc(z)
    dfa = p.make_dfa(a, z)
    assert len(dfa) == 2
    dfa = [state.nfaset for state in dfa]
    assert len(dfa[0]) == 2
    assert dfa[0] == dfa[1]
    assert 1 in dfa[0]
    assert 2 in dfa[0]
    assert not dfa[0][1].isfinal
    assert dfa[0][2].isfinal

    # Test case: (a|b)*
    a = NFAState(1)

# Generated at 2022-06-13 18:03:47.618585
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    print(pg.parse())

# Generate parser (parser module)
pg = ParserGenerator()
dfas, startsymbol = pg.parse()
del pg

# Memo dictionary
dfamemo = {}

# Module attributes
__all__ = ["dfas", "dfamemo", "startsymbol"]
# === END GRAMMAR ===


# Generated at 2022-06-13 18:03:52.586385
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    try:
        ParserGenerator("").expect(1, "")
    except SyntaxError:
        pass
    else:
        raise ValueError("should have raised SyntaxError")

# Generated at 2022-06-13 18:04:23.218074
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    # Test case for ParserGenerator.calcfirst()
    pg = ParserGenerator()
    pg.first = {
        "A": {"a": 1, "b": 1, "c": 1},
        "B": {"c": 1, "d": 1},
        "C": {"b": 1, "e": 1},
        "D": {"b": 1, "f": 1},
    }
    pg.calcfirst("E")
    assert pg.first["E"] == {
        "a": 1,
        "b": 1,
        "c": 1,
        "d": 1,
        "e": 1,
        "f": 1,
    }

    pg.calcfirst("F")
    assert pg.first["F"] == {"b": 1}

# Generated at 2022-06-13 18:04:31.154591
# Unit test for method gettoken of class ParserGenerator

# Generated at 2022-06-13 18:04:34.410866
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():

    g = PgenGrammar(token.tok_name)
    assert g.symbol2number == {}
    assert g.number2symbol == {}
    assert g.start == None
    assert g.dfas == {}



# Generated at 2022-06-13 18:04:43.193628
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    p = ParserGenerator()
    c = p.make_grammar()
    assert c

    # keyword, token.NAME
    assert c.make_label(c, '"with"') == c.tokens[token.NAME]

    # symbol
    assert c.make_label(c, 'expr') == c.symbol2label['expr']

    # operator, literal, token.STRING
    assert c.make_label(c, '"*"') == c.tokens[token.STAR]
    assert c.make_label(c, "'+'") == c.tokens[token.PLUS]
    assert c.make_label(c, "'='") == c.tokens[token.EQUAL]
    assert c.make_label(c, "'=='") == c.tokens

# Generated at 2022-06-13 18:04:45.871949
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    # Set up
    p = ParserGenerator()

    # Exercise
    tup = p.parse_alt()

    # Verify
    assert False, "Unimplemented"


# Generated at 2022-06-13 18:04:53.196283
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():

    # Set up a ParserGenerator
    pg = ParserGenerator()

    # Call method to test
    nfa_start, nfa_end = pg.parse_rhs()

    # Check results

    assert type(nfa_start) is NFAState, "type(nfa_start) should be NFAState"
    assert type(nfa_end) is NFAState, "type(nfa_end) should be NFAState"



# Generated at 2022-06-13 18:04:57.669187
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    pg = ParserGenerator()
    # A parser is a special case of a Scanner, distinguished by having
    # an associated .gettoken() method
    pg.gettoken() # fill in
    # End unit test for method gettoken of class ParserGenerator


# Generated at 2022-06-13 18:04:59.358595
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.addfirstsets()
    print(pg.first)



# Generated at 2022-06-13 18:05:07.065649
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    pg.filename = "<test case>"
    pg.generator = tokenize.generate_tokens(io.BytesIO(b'"" | "a"\n').readline)
    pg.gettoken()
    a, z = pg.parse_rhs()
    pg.expect(token.ENDMARKER)
    assert a is not z
    assert len(a.arcs) == 1
    assert len(z.arcs) == 1
    assert a.arcs[0][0] is None
    assert z.arcs[0][0] is None
    assert a.arcs[0][1] is not z
    assert z.arcs[0][1] is z
    assert len(a.arcs[0][1].arcs) == 2

# Generated at 2022-06-13 18:05:18.770714
# Unit test for constructor of class ParserGenerator
def test_ParserGenerator():
    pg = ParserGenerator()

# Generated at 2022-06-13 18:06:08.692593
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    f = open(os.path.join(os.path.split(__file__)[0], 'simple.txt'))
    pg = ParserGenerator()
    dfas = pg.parse(f.read())[0]
    f.close()
    c = pg.make_converter()
    for name in sorted(dfas.keys()):
        dfaset = dfas[name]
        firstset = pg.make_first(c, name)
        assert firstset == {c.labels[i][0]: 1 for i in range(len(c.labels))}
    print('ParserGenerator.make_first ok')

# Generated at 2022-06-13 18:06:16.466718
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    p = ParserGenerator()
    a = NFAState()
    b = NFAState()
    c = NFAState()
    d = NFAState()
    e = NFAState()
    a.addarc(b, "a")
    b.addarc(a, "a")
    c.addarc(a, "c")
    c.addarc(c, "c")
    c.addarc(d, "d")
    d.addarc(a, "d")
    e.addarc(c, "e")
    e.addarc(e, "e")
    dfa = p.make_dfa(e, a)
    assert len(dfa) == 4
    assert dfa[0].arcs["e"] == dfa[0]
    assert dfa[0].arcs

# Generated at 2022-06-13 18:06:28.425765
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    def check(exc, filename, lineno, offset, text):
        assert exc.args[0] == filename, exc.args
        assert exc.args[1] == lineno, exc.args
        assert exc.args[2] == offset, exc.args
        assert exc.args[3] == text, exc.args

    pg = ParserGenerator()

    try:
        pg.raise_error("foo")
    except SyntaxError as err:
        check(
            err, "<string>", 1, 0, ""
        )  # NB the text cannot be part of the error message
    else:
        assert False, "did not get expected exception"


# Generated at 2022-06-13 18:06:34.037477
# Unit test for method __eq__ of class DFAState
def test_DFAState___eq__():
    from copy import copy
    # Set up a DFA
    def make_states():
        a = DFAState(dict(), None)
        b = DFAState(dict(), None)
        return a, b

    a, b = make_states()
    # Test the two states for equality
    print(a == b)
    # Add an arc to one state
    a.addarc(b, 'x')
    # Test the two states for inequality
    print(a == b)
    # Add the same arc to the other state
    b.addarc(b, 'x')
    # Test the two states for equality
    print(a == b)
    # Make a copy of one of the states
    c = copy(a)
    # Test the state against the original, and against its copy
    print(a == b)
    print

# Generated at 2022-06-13 18:06:46.894706
# Unit test for constructor of class ParserGenerator

# Generated at 2022-06-13 18:06:59.044068
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    if __name__ != "__main__":
        return
    class CollectComments(Generator):
        def __init__(self, s: str) -> None:
            self.s = s
            self.tokens = []

        def __next__(self) -> Tuple[int, Text, Text, Text, Text]:
            while self.s:
                if self.s[0] == "#":
                    while self.s[0] != "\n":
                        self.s = self.s[1:]
                elif self.s[0].isspace():
                    self.s = self.s[1:]
                elif self.s[0] == "\\":
                    self.s = self.s[1:]
                    if self.s[0] == "\n":
                        self.s = self.s[1:]


# Generated at 2022-06-13 18:07:07.284854
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    import textwrap
    import os
    import tempfile
    import subprocess
    import shutil

    # ParserGenerator.simplify_dfa
    fd, filename = tempfile.mkstemp(suffix=".py", text=True)

# Generated at 2022-06-13 18:07:18.845701
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    import pprint
    pg = ParserGenerator()
    pg.dfas = {
        'A': [DFAState({'B': 1, 'C': 1}, True),
              DFAState({'B': 1}, False),
              DFAState({}, False)],
        'B': [DFAState({}, False)],
        'C': [DFAState({'B': 1}, True)]}
    pg.startsymbol = 'A'
    c = pg.convert()
    assert c.first == {'A': {'B': 1, 'C': 1}, 'B': {}, 'C': {'B': 1}}, c.first

# Generated at 2022-06-13 18:07:20.525759
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    assert True  # XXX

# Generated at 2022-06-13 18:07:31.277458
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    pg = ParserGenerator()
    pg.builddfas("", "a = b ; b = '+' | b c | c ; c = '3' | '4'")
    a = pg.dfas["a"][0]  # final state
    assert a.arcs[("+",)] == a
    assert a.arcs[("3",)] == a
    assert a.arcs[("4",)] == a
    assert a.arcs[("",)] == a

# Generated at 2022-06-13 18:09:22.330339
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    fname = inspect.stack()[0][3]
    pgen = ParserGenerator("(", "<fname>", 0, len("("), "(" + EOF)
    exc = None
    try:
        pgen.raise_error("oops")
    except SyntaxError as exc:
        pass
    assert isinstance(exc, SyntaxError)
    assert exc.msg == "oops"
    assert exc.filename == "<fname>"
    assert exc.lineno == 0
    assert exc.offset == 1
    assert exc.text == "(" + EOF

    pgen = ParserGenerator("(", "<fname>", 0, len("("), "(" + EOF)
    exc = None

# Generated at 2022-06-13 18:09:28.886417
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    pg = ParserGenerator(())
    pg.type, pg.value = 42, 'foo'
    assert pg.expect(42) == 'foo'
    try:
        pg.expect(43)
    except SyntaxError as exc:
        assert str(exc) == "expected 43/None, got 42/foo"
    else:
        assert False, "expected SyntaxError"
    try:
        pg.expect(42, 'bar')
    except SyntaxError as exc:
        assert str(exc) == "expected 42/bar, got 42/foo"
    else:
        assert False, "expected SyntaxError"

# Generated at 2022-06-13 18:09:37.830735
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    r = pg.parse('''
    stmt: simple_stmt | compound_stmt
    simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
    small_stmt: (expr_stmt | print_stmt  | del_stmt)
    # etc.
    ''')

# Generated at 2022-06-13 18:09:42.213229
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    grammar = r'''
        calc: add_expr
        add_expr: mul_expr ('+' mul_expr)*

        mul_expr: factor ('*' factor)*
        factor: '(' add_expr ')' | NUMBER
        '''

    pg = ParserGenerator()
    pg.parse_grammar(grammar)
    pg.dump_dfa("add_expr", pg.dfas["add_expr"])



# Generated at 2022-06-13 18:09:51.356513
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    def test(input: str, type: int, value: Any, exc: Any) -> None:
        g = ParserGenerator()
        try:
            g.filename = "<test case>"
            g.generator = tokenize.generate_tokens(io.StringIO(input).readline)
            g.gettoken()
            g.expect(type, value)
        except exc as e:
            assert str(e) == str(SyntaxError(*e.args))
        else:
            assert not exc
    test("\n", token.NEWLINE, None, None)
    test("\n", token.NAME, None, SyntaxError("expected NAME/None, got 1/None", ("<test case>", 2, 0, "\n")))
    test("abc\n", token.NAME, "abc", None)

# Generated at 2022-06-13 18:09:54.693102
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    generator = ParserGenerator()
    test_cases = get_testcases_ParserGenerator_calcfirst()
    for arglist, expected in test_cases:
        with pytest.raises(expected) as excinfo:
            generator.calcfirst(*arglist)
        exception = excinfo.value
        check_exception(exception, *expected)

# Generated at 2022-06-13 18:10:03.132233
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    test_cases = [
        ("", ("",)),
        (".", ("",)),
        ("a", ("a",)),
        ("a?", ("a",)),
        ("a+", ("a",)),
        ("a*", ("a",)),
        ("ab", ("ab",)),
        ("a(b)", ("a",)),
        ("a|b", ("a",)),
        ("a|", ("a",)),
        ("a*a*", ("aaa",)),
        ("a*b+", ("ab", "ab", "abb",)),
        ("a*b?", ("a",)),
        ("a*b*", ("b", "ab", "abb", "aab")),
    ]
    p = ParserGenerator()
    for text, expected in test_cases:
        nfa1, nfa2 = p.parse_

# Generated at 2022-06-13 18:10:09.600340
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    msg = "msg"
    args = ()
    _msg = " ".join([msg] + list(map(str, args)))
    filename = "filename"
    end_0 = 0
    end_1 = 0
    line = "line"

    assert _msg == "msg"
    assert filename == "filename"
    assert end_0 == 0
    assert end_1 == 0
    assert line == "line"



# Generated at 2022-06-13 18:10:13.651959
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.dfas = {"A": [DFAState({NFAState(): 1}, False), DFAState({NFAState(): 1}, True)]}
    pg.calcfirst("A")
    assert pg.first["A"] is not None
test_ParserGenerator_calcfirst()


# Generated at 2022-06-13 18:10:25.514120
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    def helper(grammar: Text, expected_result):
        gen = ParserGenerator()
        actual_result = gen.parse_rhs(tokenize.generate_tokens(io.StringIO(grammar).readline))
        assert expected_result == actual_result, "Expected: %s, got: %s" % (expected_result, actual_result)
    # _:
    helper('', None)
    helper('a', None)
    helper('(', None)
    helper('(a', None)
    helper('(a)', None)
    helper('(ab)', None)
    helper('(a|b)', None)
    helper('(a|b c)', None)
    helper('(a|b)|c', None)
    helper('(a|b)|c', None)
   