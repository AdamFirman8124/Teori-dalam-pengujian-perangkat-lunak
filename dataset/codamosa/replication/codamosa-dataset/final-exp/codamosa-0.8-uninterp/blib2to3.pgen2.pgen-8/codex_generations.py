

# Generated at 2022-06-13 18:02:19.243078
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    mg = ParserGenerator()
    assert mg.gettoken() not in (tokenize.COMMENT, tokenize.NL)
    mg.gettoken()
    mg.gettoken()
    mg.gettoken()
    mg.gettoken()
    assert mg.gettoken() not in (tokenize.COMMENT, tokenize.NL)
    mg.gettoken()
    mg.gettoken()
    assert mg.gettoken() not in (tokenize.COMMENT, tokenize.NL)
    mg.gettoken()
    assert mg.gettoken() not in (tokenize.COMMENT, tokenize.NL)
    mg.gettoken()
    assert mg.gettoken() not in (tokenize.COMMENT, tokenize.NL)
    mg.gettoken()
    mg.gettoken()
    mg.gettoken()

# Generated at 2022-06-13 18:02:28.291744
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pg = ParserGenerator()
    with open("_grammar.txt", "r") as f:
        pg.setup("_grammar.txt", f.read())
    pg.parse()
    pg.addfirstsets()
    #print("First sets added")
    c = pg.write_converter("_converter.txt")
    #print("Converter written")
    a = pg.dfas["atom"][1]
    b = pg.dfas["power"][1]
    c = pg.dfas["factor"][1]
    d = pg.dfas["term"][4]
    e = pg.dfas["arith_expr"][1]
    f = pg.dfas["test"[1]]
    g = pg.dfas["or_test"][1]

# Generated at 2022-06-13 18:02:39.549580
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    # These tests assume the default Python 3.x grammar;
    # in other words, that the method grammar.pgen() is called
    # with the argument start='file_input'.
    pgen = ParserGenerator(None, None)

# Generated at 2022-06-13 18:02:46.671585
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    p = ParserGenerator()
    def f():
        p.raise_error("Whoops")
    try:
        f()
    except SyntaxError as e:
        assert str(e) == "Whoops", str(e)
    else:
        assert False, "Expected exception"
    try:
        p.raise_error("foo")
    except SyntaxError as e:
        assert str(e) == "foo", str(e)
    else:
        assert False, "Expected exception"
    try:
        p.raise_error("%d-%d", 42, 88)
    except SyntaxError as e:
        assert str(e) == "42-88", str(e)
    else:
        assert False, "Expected exception"

# Generated at 2022-06-13 18:02:55.549011
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    pg.dfas = {"foo": [DFAState({pg.NFAState(): 1}, True)]}
    c = pg.make_grammar()
    assert c.make_first(c, "foo") == {0: 1}
    #
    pg = ParserGenerator()
    pg.dfas = {"foo": [DFAState({pg.NFAState(): 1}, True)]}
    pg.tokens = {token.NUMBER: 13}
    c = pg.make_grammar()
    assert c.make_first(c, "foo") == {13: 1}
    #
    pg = ParserGenerator()
    pg.dfas = {"foo": [DFAState({pg.NFAState(): 1}, True)]}

# Generated at 2022-06-13 18:02:58.988814
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    pg = ParserGenerator()
    s = """
    a: 'b'
"""
    pg.parse_string(s, "example")
    assert pg.parsed is not None


# Generated at 2022-06-13 18:03:06.559327
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    table = {
        "simple": "a*(a|b)a",
        "start string": '"print" rest_of_line',
        "star": 'expr "*" expr',
        "expr": "expr '+' term | term",
        "term": "term '*' factor | factor",
        "factor": "NAME | NUMBER | '(' expr ')'",
        "rest_of_line": "| NEWLINE DEDENT",
    }
    pg = ParserGenerator()
    for name, exp in table.items():
        print()
        print(name, "=", exp)
        pg.addrule(name, exp)
        a = pg.dfas[name][0]
        z = pg.dfas[name][-1]

# Generated at 2022-06-13 18:03:13.341259
# Unit test for method parse of class ParserGenerator
def test_ParserGenerator_parse():
    r"""Test for method __parse__ of class ParserGenerator.
    """
    def test_case(
        value: Union[TextIO, str],
        expected_rules: Optional[Dict[Text, Text]],
        expected_dfas: Optional[Dict[Text, List["DFAState"]]],
        expected_startsymbol: Optional[Text],
        expected_first: Optional[Dict[Text, Dict[Text, int]]],
    ) -> None:
        print(value)
        rules = {}
        dfas = {}
        startsymbol = ""
        first = {}
        pg = ParserGenerator()
        if isinstance(value, str):
            value = io.StringIO(value)
        pg.parse_grammar(value, rules, dfas, startsymbol)
        print(rules)

# Generated at 2022-06-13 18:03:18.788287
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    def check(name: str, text: str, dump: str) -> None:
        pg = ParserGenerator()
        mydict = {}
        exec(text, mydict)
        pg.setup((name, mydict[name]))
        # pg.dump_nfa(name, *pg.parse_rhs())
        assert pg.buf == dump

# Generated at 2022-06-13 18:03:19.548876
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    x = PgenGrammar()


# Generated at 2022-06-13 18:03:50.649167
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    generator = [
        (tokenize.NAME, 'foo', (1, 0), (1, 3), 'foo'),
        (tokenize.OP, '=', (1, 4), (1, 5), '=')
    ]
    pg = ParserGenerator(generator, '<file path>')
    try:
        pg.raise_error('error message')
    except SyntaxError as e:
        assert e.args[0] == 'error message'
        assert e.args[1] == ('<file path>', 1, 5, '=')
    else:
        raise AssertionError

    try:
        pg.raise_error('%s %s', 'error', 'message')
    except SyntaxError as e:
        assert e.args[0] == 'error message'

# Generated at 2022-06-13 18:04:01.678989
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    import pgen2.pgen

    c = pgen2.pgen.ParserGenerator()
    g = Grammar()

    assert g.make_label(c, "NAME") == token.NAME, "Unexpected tok_name"
    assert g.make_label(c, '"async"') == token.async_, "Unexpected keyword"
    assert g.make_label(c, '"and"') == token.and_, "Unexpected keyword"
    assert g.make_label(c, '"or"') == token.or_, "Unexpected keyword"

# Generated at 2022-06-13 18:04:11.385280
# Unit test for method parse of class ParserGenerator

# Generated at 2022-06-13 18:04:18.072411
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator(None)

    token_values = [
        "token1", "token2", "token3"
    ]
    symbol_values = [
        "symbol1", "symbol2", "symbol3"
    ]

    token_labels = []
    for token_value in token_values:
        token_labels.append((token.NAME, token_value))

    symbol_labels = []
    for symbol_value in symbol_values:
        symbol_labels.append((0, symbol_value))

    labels = token_labels + symbol_labels

    symbol_labels_map = {}
    for symbol_value in symbol_values:
        symbol_labels_map[symbol_value] = len(symbol_labels_map)

    c = PgenGrammar

# Generated at 2022-06-13 18:04:23.904932
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    import StringIO, sys
    save = sys.stdout
    try:
        sys.stdout = StringIO.StringIO()
        ParserGenerator.test_ParserGenerator_dump_nfa()
    finally:
        out = sys.stdout.getvalue()
        sys.stdout = save
    print(out)


# Generated at 2022-06-13 18:04:29.822346
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    cases = [
        ("*", "abc", "abc"),
        ("\"abc\"|\"def\"", "abc", "abc"),
        ("\"abc\"|\"def\"", "def", "def"),
        ("\"a\"|\"ab\"", "ab", "ab"),
        ("\"a\"|\"ab\"", "a", "a"),
        ("NAME \"=\"", "x =", "x"),
        ("NAME [\"=\"]", "x =", "x ="),
        ("NAME [\"=\"]", "x", "x"),
        ("NAME | STRING", "abc", "abc"),
        ("NAME | STRING", "\"abc\"", "\"abc\""),
    ]
    for arg, input, expect in cases:
        pg = ParserGenerator()
        dfa, startsymbol = pg.parsestr

# Generated at 2022-06-13 18:04:35.765851
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    def test(input):
        input = input.strip()
        output = ParserGenerator(input).parse_item()
        print(repr(input), "->", output)

    test("")
    test("(())")
    test("[(())")
    test("(()[])")
    test("([])")
    test("['one' (two) 'three']")
    test("(a|b)c*")
    test("a")
    test("a*")
    test("a+")
    test("'a'")
    test("'a'*")
    test("'a'+")
    test("a?b!c+d{3}")

if __name__ == "__main__":
    test_ParserGenerator_parse_item()

# Generated at 2022-06-13 18:04:44.173262
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    def check_raise(type, value, expect_type, expect_value):
        try:
            pg.expect(expect_type, expect_value)
            ok = False
        except SyntaxError:
            ok = True

        assert ok, (
            f"expected {expect_type}/{expect_value}, "
            f"got {type}/{value}"
        )

    pg = ParserGenerator([(token.NAME, "x"), (token.OP, ":")])
    pg.gettoken()
    check_raise(token.NAME, "x", token.NAME, "y")
    check_raise(token.NAME, "x", token.OP, ":")
    check_raise(token.NAME, "x", token.OP, "|")

# Generated at 2022-06-13 18:04:54.640027
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    msg = 'msg'
    args = ['arg1', 'arg2']
    filename = 'filename'
    end1 = 0
    end2 = 1
    line = 'line'
    p = ParserGenerator()
    p.filename = filename
    p.end = (end1, end2)
    p.line = line
    try:
        p.raise_error(msg, *args)
    except SyntaxError as e:
        assert e.filename == filename
        assert e.lineno == end1
        assert e.offset == end2
        assert e.text == line
        assert msg in e.msg
        for arg in args:
            assert arg in e.msg
        assert True
    except:
        assert False, 'wrong exception raised'



# Generated at 2022-06-13 18:04:58.549061
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    pg = ParserGenerator()
    c = pg.make_converter()
    assert c.make_label(c, "'NAME'") == 39
    assert c.make_label(c, "'('") == 40

# Generated at 2022-06-13 18:05:39.341621
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    """dump_nfa"""
    pg = ParserGenerator(StringIO.StringIO(''))
    pg.dump_nfa('expr', NFAState(), NFAState())



# Generated at 2022-06-13 18:05:43.743533
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    pgen_grammar_instance = PgenGrammar()
    assert isinstance(pgen_grammar_instance, grammar.Grammar)
    assert pgen_grammar_instance._locals
    assert pgen_grammar_instance.states
    assert pgen_grammar_instance._statemap


# Generated at 2022-06-13 18:05:54.984392
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    for source in (
        '"foo"',
        '"foo" "bar"',
        '"foo" | "bar"',
        '"foo" ( "bar" | "spam" ) "baz"',
        '"foo" ( [ "bar" | "spam" ] "baz" )',
        '"foo" ( [ "bar" | "spam" ] "baz" ) "eggs"',
    ):
        p = ParserGenerator()
        states_dict, startsymbol = p.generate(source)
        assert startsymbol is not None
        p.dump_nfa(startsymbol, states_dict[startsymbol][0], states_dict[startsymbol][-1])
    # NB: the last example will raise a ValueError because the two
    # alternatives "bar"

# Generated at 2022-06-13 18:06:05.030326
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    g = ParserGenerator()
    g.dfas["symbol"] = [DFAState(None, False), DFAState(None, True)]
    g.first["symbol"] = {"first": 1}
    c = g.make_grammar("symbol", [], {})
    assert c.symbol2number["symbol"] == 0
    assert c.first == {0: {"first": 1}}
    assert c.start == 0



# Generated at 2022-06-13 18:06:09.273901
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    s = """
a: 'a'
b: 'b'
c: 'c'
"""
    g = ParserGenerator()
    g.setup(s.splitlines())
    for name, dfa in g.dfas.items():
        g.dump_nfa(name, dfa[0], dfa[0])



# Generated at 2022-06-13 18:06:19.572701
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    # Tests that parse_alt creates the correct DFA for a little grammar
    pg = ParserGenerator()
    f = StringIO(
        """
a: 'a'+ 'b'*
b: 'b'+
"""
    )
    dfas, start = pg.parse_grammar(f, '<input>')
    a = dfas['a']
    b = dfas['b']
    if not (
        len(a) == len(b) == 3
        and a[0].arcs == {'a': a[0]}
        and b[0].arcs == {'b': b[0]}
    ):
        import sys
        from io import StringIO
        f = StringIO()
        pg.dump_dfa("a", a, file=f)

# Generated at 2022-06-13 18:06:29.981377
# Unit test for method make_first of class ParserGenerator

# Generated at 2022-06-13 18:06:36.573752
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
  g = grammar.Grammar()

  assert isinstance(g.dfas, Dict[int, Optional['Dfa']])
  assert isinstance(g.states, Dict[int, Tuple['State', Any]])
  assert isinstance(g.symbol2label, Dict[int, int])
  assert isinstance(g.keywords, Dict[token.IS, Tuple[token.NAME, token.NAME]])
  assert isinstance(g.tokens, Sequence[int])



# Generated at 2022-06-13 18:06:39.743281
# Unit test for constructor of class PgenGrammar
def test_PgenGrammar():
    grammar_file = 'Grammar'
    start = 'file_input'
    pgen_grammar = PgenGrammar(grammar_file, start)



# Generated at 2022-06-13 18:06:49.936242
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    def make_token(ttype, value):
        return (ttype, value, (None, None), (None, None), None)

    def make_tokenizer(s):
        for t in s.split():
            if t[0].isalpha():
                yield make_token(token.NAME, t)
            elif t[0] in '0123456789':
                yield make_token(token.NUMBER, t)
            else:
                yield make_token(token.OP, t)
        yield (0, "", (None, None), (None, None), None)

    def make_pg(s):
        return ParserGenerator(make_tokenizer(s))

    def check(s, expected):
        pg = make_pg(s)
        a, z = pg.parse_rhs()
       

# Generated at 2022-06-13 18:07:36.794616
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from . import token
    pg = ParserGenerator()
    pg.gettoken = lambda: None
    pg.type = token.NAME
    pg.value = "foo"
    pg.begin = ("line 1", 1)
    pg.end = ("line 1", 4)
    pg.line = "foo\n"
    pg.filename = "<string>"
    pg.raise_error = lambda msg, *args: None
    assert pg.expect(token.NAME) == "foo"

# Generated at 2022-06-13 18:07:43.145466
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    import doctest
    import lib2to3.pgen2.parser

    globs = lib2to3.pgen2.parser.__dict__.copy()
    globs.update(locals())
    (failures, tests) = doctest.testmod(globs=globs, optionflags=doctest.ELLIPSIS)
    assert tests > 0 # "expected to run some tests in %s" % __file__
    assert failures == 0 # "expected no failures in %s" % __file__

if __name__ == "__main__":
    test_ParserGenerator_expect()

# Generated at 2022-06-13 18:07:56.460056
# Unit test for method make_grammar of class ParserGenerator

# Generated at 2022-06-13 18:08:03.823710
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    pg = ParserGenerator()
    pg.generator = iter([
        (token.NAME, "NAME", (0, 0), (0, 4), ""),
        (token.OP, "|", (0, 4), (0, 5), ""),
        (token.NAME, "NAME", (0, 5), (0, 9), ""),
        (token.ENDMARKER, "", (0, 9), (0, 9), ""),
    ])
    pg.gettoken()
    start, finish = pg.parse_rhs()
    assert start.arcs == {(None, finish), ("NAME", finish)}
    assert not finish.arcs


# Generated at 2022-06-13 18:08:11.677703
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    assert ParserGenerator("foo").parse_alt() == (
        NFAState({NFAState({NFAState({NFAState([(None, NFAState())])}): 1}): 1}),
        NFAState({NFAState([(None, NFAState())])}),
    )
test_ParserGenerator_parse_alt()


# ParserGenerator has a method parse_rhs, which takes no arguments,
# returns a 2-tuple of NFAState instances, and is called at
# grammar.py:16

# Generated at 2022-06-13 18:08:16.521645
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    r1 = "a : 'x' | 'y'\n"
    r2 = "b : 'i' a 'j' | 'k'\n"
    r3 = "c : 'p' | b\n"
    r4 = "d : c | 'q'\n"

    # check left recursion
    pg = ParserGenerator()
    pg.add_rhs(r1)
    pg.add_rhs(r2)
    pg.add_rhs(r3)
    pg.add_rhs(r4)
    pg.start_rule("d")
    pg.start_rule("b")
    with pytest.raises(ValueError):
        pg.addfirstsets()

    # check normal
    pg = ParserGenerator()

# Generated at 2022-06-13 18:08:26.939394
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    input = """\
def: 'def' NAME parameters ':' suite

parameters: '(' [varargslist] ')'

varargslist: (fpdef ['=' test] ',')* ('*' NAME [',' '**' NAME]
                                      | '**' NAME)
                            | fpdef ['=' test] (',' fpdef ['=' test])* [',']

fpdef: NAME | '(' fplist ')'
fplist: fpdef (',' fpdef)* [',']

"""
    input = io.StringIO(input)
    pg = ParserGenerator()
    pg._read_grammar(input)
    pg.parse()
    assert isinstance(pg.dfas['parameters'], list)

# Generated at 2022-06-13 18:08:40.581093
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    # args is a tuple containing positional arguments
    args = ("Derp", 1, 2, 3)
    # SyntaxError is a class. We create a subclass for testing
    # and use that in the unit test.
    class DummySyntaxError(SyntaxError):
        def __init__(self, msg: str, args: Tuple[str, int, int, str], *, foo: int) -> None:
            pass
    # Pass the 
    g = ParserGenerator(None, 'filename', None, ())
    class dummy_self:
        def __init__(self):
            self.filename = 'filename'
            self.begin = (1, 2)
            self.end = (3, 4)
            self.line = 'line'

# Generated at 2022-06-13 18:08:42.538498
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    # No tests yet
    pass

# Generated at 2022-06-13 18:08:49.564278
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    pg = ParserGenerator()
    pg.end = (3, 10)
    pg.line = "line number three"
    pg.filename = "somefilename"

    try:
        pg.raise_error("ERROR: Expected %s/%s, got %d/%s", "token.STRING", "'EOF'",
                       token.NUMBER, "'3'")
    except SyntaxError as e:
        msg, filename, lineno, offset, line = e.args
        assert msg == "ERROR: Expected token.STRING/'EOF', got NUMBER/'3'"
        assert filename == pg.filename
        assert lineno == pg.end[0]
        assert offset == pg.end[1]
        assert line == pg.line
    else:
        raise AssertionError("Expected exception")

   

# Generated at 2022-06-13 18:10:49.409508
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    input = r"""
        start: a b
        a: 'x'
        b: 'y'
        """
    pg = ParserGenerator()
    dfas, startsymbol = pg.parse_grammar(input)
    # print dfas, startsymbol
    assert dfas is not None
    assert startsymbol is not None

# Generated at 2022-06-13 18:10:52.045308
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    fname = "<test data>"
    p = test_support.import_module("_parser")
    p.ParserGenerator("", 0, 0, "", "", fname)

# Generated at 2022-06-13 18:11:02.436332
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    p = ParserGenerator()
    p.add_rhs("foo", "(bar | baz)")
    p.add_rhs("bar", "[a b]")
    p.add_rhs("baz", "['a' 'b']")
    p.dfas["foo"] = [DFAState({}, False), DFAState({}, True)]
    p.dfas["bar"] = [
        DFAState({}, False),
        DFAState({DFAState({}, True): 1}, True),
        DFAState({DFAState({}, True): 1}, True),
    ]

# Generated at 2022-06-13 18:11:09.959686
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    def make_converter(s: str) -> PgenGrammar:
        pg = ParserGenerator()
        pg.parse_string(s)
        pg.addfirstsets()
        return pg.convert()

    def parse_alt(s: str) -> Tuple[NFAState, NFAState]:
        pg = ParserGenerator()
        pg.parse_string(s)
        return pg.parse_alt()

    def check(s: str, c: PgenGrammar) -> None:
        # Complexity: O(len(s)**3)
        start, z = parse_alt(s)
        c_start, c_z = c.states[0][0], c.states[-1][0]
        assert start.arcs == c_start
        assert z.arcs == c

# Generated at 2022-06-13 18:11:15.016292
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    import TokenSupport
    from TokenSupport import token
    from TokenSupport import tokenize

    def iterable(toks: List[Token]) -> Iterator[Token]:
        for tok in toks:
            yield tok

    def nfa(n1: int, n2: int, s: int, e: int, line: Text) -> Token:
        return Token(n1, n2, s, e, line)

    def token(*args: Any) -> Token:
        return nfa(tokenize.NAME, *args)

    def op(*args: Any) -> Token:
        return nfa(tokenize.OP, *args)


# Generated at 2022-06-13 18:11:25.727885
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    f = io.StringIO()
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        pgen = ParserGenerator("./Lib/pgen2/pgen.txt")
        pgen.dump_nfa("foo", pgen.dfas["dottedname"][0], pgen.dfas["dottedname"][-1])
    finally:
        sys.stdout = oldstdout
    got = "".join(f.getvalue().split())