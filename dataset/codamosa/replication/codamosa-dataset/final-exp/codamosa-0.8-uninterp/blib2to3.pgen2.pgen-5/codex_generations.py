

# Generated at 2022-06-13 18:03:08.739262
# Unit test for method addfirstsets of class ParserGenerator
def test_ParserGenerator_addfirstsets():
    # XXX These unit tests should be moved out of this file and into test_parser.py
    pg = ParserGenerator()
    add_grammar_rules(pg)
    pg.make_dfas()

    # First set of 'and_expr' should include 'and' and 'not'
    # (since those are keywords, not names)
    first = pg.first['and_expr']
    assert first is not None
    assert 'and' in first
    assert 'not' in first

    # First set of 'argument' should include all the operators in 'comp_op'
    comp_ops = pg.first['comp_op']
    assert comp_ops is not None
    first = pg.first['argument']
    assert first is not None
    for op in comp_ops:
        assert op in first



# Generated at 2022-06-13 18:03:18.558821
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    import typing

    def check(text: str, expected: str) -> None:
        generator = ParserGenerator(text)
        startstate, finishstate = generator.parse_atom()
        assert isinstance(startstate, NFAState)
        assert isinstance(finishstate, NFAState)
        assert generator.line == expected
        generator.gettoken()
        assert generator.type == token.ENDMARKER

    check("a", "")
    check("a[", "")
    check("a]", "")
    check("(", "")
    check("a)", ")")
    check("a+", "+")
    check("a*", "*")
    check("", "")

# Generated at 2022-06-13 18:03:35.438765
# Unit test for method parse of class ParserGenerator

# Generated at 2022-06-13 18:03:41.112506
# Unit test for method dump_dfa of class ParserGenerator
def test_ParserGenerator_dump_dfa():
    import io
    import untokenize
    import tokenize

    def whattype(s: Text) -> Text:
        tokenizer = tokenize.generate_tokens(io.StringIO(s).readline)
        tok, val, _, _, _ = next(tokenizer)
        if tok == token.NUMBER:
            if "." in val or "e" in val:
                return "float"
            else:
                return "int"
        elif tok == token.STRING:
            return "string"
        elif tok == token.NAME:
            return "name"
        else:
            return repr(val)

    def parse(grammar: Text, start: Text = "single_input") -> "ParserGenerator":
        p = ParserGenerator()
        p.add_bnf

# Generated at 2022-06-13 18:03:46.074552
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    e, b = ParserGenerator().parse_rhs()
    ParserGenerator().dump_nfa("test", e, b)
    a = ParserGenerator().make_dfa(e, b)
    ParserGenerator().dump_dfa("test", a)


# Generated at 2022-06-13 18:03:52.351980
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator([], {})
    pg.dfas = {"a": [DFAState([NFAState()], False)], "b": [DFAState([NFAState()], False)]}
    pg.addfirstsets()



# Generated at 2022-06-13 18:04:02.320926
# Unit test for method calcfirst of class ParserGenerator
def test_ParserGenerator_calcfirst():
    pg = ParserGenerator()
    pg.dfas = {"foo": [NFAState(1), NFAState(1), NFAState(1)], "bar": [NFAState(1)]}
    pg.dfas["foo"][0].addarc(None, pg.dfas["bar"][0])
    pg.dfas["foo"][0].addarc("a", pg.dfas["foo"][1])
    pg.dfas["foo"][1].addarc("b", pg.dfas["foo"][2])

    pg.addfirstsets()
    assert pg.first["foo"] is not None
    assert pg.first["bar"] is not None
    assert "a" in pg.first["foo"]
    assert "b" in pg.first["foo"]
    assert pg.first["bar"] == {}

# Generated at 2022-06-13 18:04:11.688560
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    # Method simplify_dfa is tested in test_converter.py
    # This is just a quick check.
    pg = ParserGenerator()
    states = [parsedfa.DFAState({0: 1, 1: 1}, False),
              parsedfa.DFAState({2: 1}, False),
              parsedfa.DFAState({2: 1, 3: 1}, True)]
    states[0].addarc(states[1], "a")
    states[0].addarc(states[2], "b")
    states[1].addarc(states[1], "a")
    states[2].addarc(states[0], "a")
    states[2].addarc(states[0], "b")
    pg.simplify_dfa(states)
    assert len(states) == 2

# Generated at 2022-06-13 18:04:13.528430
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    try:
        raise ParserGenerator('', '', '', '', '', '', '', '').raise_error('msg')
    except:
        pass

# Generated at 2022-06-13 18:04:22.396805
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    # pylint: disable=protected-access
    c = ParserGenerator()
    c.labels = []
    c.tokens = {}
    c.keywords = {}
    c.symbol2label = {}
    c.symbol2number = {}
    c.symbol2number["a"] = 1
    c.symbol2number["b"] = 2
    assert c.make_label(c, "a") == 1
    assert c.make_label(c, "b") == 2
    assert c.make_label(c, "c") == 3
    assert c.make_label(c, "+") == 4
    assert c.make_label(c, "-") == 5
    assert c.make_label(c, "NUMBER") == 6

# Generated at 2022-06-13 18:04:55.701251
# Unit test for method gettoken of class ParserGenerator
def test_ParserGenerator_gettoken():
    import io
    from typing import List
    from typing import Union
    from lib2to3.pgen2.parse import ParseError
    from lib2to3.pgen2.parse import ParserGenerator
    from lib2to3.pgen2.parse import Token
    from lib2to3.pgen2.parse import handle_token

    def testcase(b: bytes, expected: List[Token]) -> None:
        print("Testing", repr(b))
        parser = ParserGenerator()
        tokens = []
        def callback(type_: int, token: Union[Text, bytes]) -> None:
            tokens.append((type_, token))
        parser.gettoken = handle_token(callback)
        f = io.StringIO(b.decode("utf-8"))
        parser.generator = tokenize.gener

# Generated at 2022-06-13 18:05:05.297807
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():

    class DFAState:
        def __init__(self, nfaset: Dict[NFAState, int]) -> None:
            self.nfaset = nfaset
            self.arcs = {}
            self.isfinal = False

        def __eq__(self, other: Any) -> bool:
            assert isinstance(other, DFAState)
            return self.arcs == other.arcs

        def addarc(self, next: "DFAState", label: Text) -> None:
            self.arcs[label] = next

        def unifystate(self, old: "DFAState", new: "DFAState") -> None:
            arcs = {}
            for label, next in self.arcs.items():
                arcs[label] = next is old and new or next
            self.arcs

# Generated at 2022-06-13 18:05:11.277888
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    p = ParserGenerator()
    p.type = token.NAME
    p.value = 'x'
    print(p.expect(token.NAME))
    print(p.value)
    print(p.expect(token.NAME,'x'))
    print(p.value)
    print(p.expect(token.OP,'y'))

test_ParserGenerator_expect()


# Generated at 2022-06-13 18:05:24.001658
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    """Unit test for method parse_atom of class ParserGenerator"""
    from pgen2 import tokenize, token
    from pgen2.parser import ParserGenerator

    for t in (
        (token.NAME, "NAME"),
        (token.STRING, "STRING"),
        (token.OP, "("),
        (token.OP, ")"),
        (token.OP, "["),
        (token.OP, "]"),
        (token.OP, "|"),
        (token.OP, "+"),
        (token.OP, "*"),
        (tokenize.OP, ":"),
        (tokenize.NL, "\n"),
    ):
        tok = tokenize.generate_tokens(io.StringIO(t[1]).readline)

# Generated at 2022-06-13 18:05:34.699082
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    """
    def test_ParserGenerator_make_grammar():
        from . import pytree
        from . import grammar
        from .pgen2 import token
        # Use the nonterminal names found in pytree.
        pygram = pytree.make_grammar(grammar.sym2str, pytree.nonterminals)

        def test_sym(name: Text) -> int:
            sym = pygram.sym2number.get(name)
            if sym is None:
                raise ValueError("unknown symbol %r" % name)
            return sym

        pgen = ParserGenerator(pygram, "grammar")
        pgen.generate_consts()
        pgen.generate_grammar_data()
        ast = pgen.make_grammar()
        check_grammar(ast)
    """


# Generated at 2022-06-13 18:05:39.458362
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    pgen = ParserGenerator()
    pgen.parse_rhs = lambda: (NFAState(), NFAState())
    pgen.gettoken = lambda: None
    pgen.expect = lambda *args, **kwargs: None
    pgen.raise_error = lambda *args, **kwargs: None

    pgen.value = "("
    pgen.type = 77  # assume this is OP
    pgen.parse_atom()
    pgen.parse_rhs.assert_called_with()
    pgen.expect.assert_called_with(77, ")")

    pgen.value = "SPAM"
    pgen.type = token.NAME
    a = NFAState()
    z = NFAState()
    pgen.parse_atom()

# Generated at 2022-06-13 18:05:47.172755
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pg = ParserGenerator()

# Generated at 2022-06-13 18:05:56.897382
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    parser = ParserGenerator("foo", b"")
    parser.token = "NAME"
    parser.value = "bar"
    parser.type = token.NAME
    parser.begin = (1, 1)
    parser.end = (1, 2)
    parser.line = b""
    parser.gettoken = lambda: None
    parser.raise_error = lambda msg,a=None,b=None: print("Error: ",msg,a,b)
    parser.parse_item = lambda: (parser.value, parser.value)
    a, z = parser.parse_alt()
    #print("'%s' '%s'" % (a, z))
    assert a == "bar", a
    assert z == "bar", z

# Generated at 2022-06-13 18:06:06.341898
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    def make_label(c, label):
        # XXX Maybe this should be a method on a subclass of converter?
        ilabel = len(c.labels)
        if label[0].isalpha():
            # Either a symbol name or a named token
            if label in c.symbol2number:
                # A symbol name (a non-terminal)
                if label in c.symbol2label:
                    return c.symbol2label[label]
                else:
                    c.labels.append((c.symbol2number[label], None))
                    c.symbol2label[label] = ilabel
                    return ilabel
            else:
                # A named token (NAME, NUMBER, STRING)
                itoken = getattr(token, label, None)
                assert isinstance(itoken, int), label

# Generated at 2022-06-13 18:06:14.447701
# Unit test for method raise_error of class ParserGenerator
def test_ParserGenerator_raise_error():
    from types import TracebackType
    from pickle import PicklingError
    generator = ParserGenerator("", "")
    generator._test = "test"
    with raises((AssertionError, SyntaxError)):
        generator.raise_error("hello", "world")
    exc: SyntaxError = generator.raise_error("hello")
    assert isinstance(exc, SyntaxError)
    assert exc.filename == "", exc.filename
    assert exc.lineno is not None
    assert exc.msg == "hello", exc.msg
    exc = generator.raise_error("hello", generator)
    assert isinstance(exc, SyntaxError)
    assert exc.filename == "", exc.filename
    assert exc.lineno is not None
    assert exc.msg == "hello", exc.msg

# Generated at 2022-06-13 18:07:13.543731
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pg = ParserGenerator()
    # function calls are ugly in Python 2, but we do not
    # care about Python 2.

    def tk(type, value):
        pg.type, pg.value = type, value
        return pg.parse_item()

    def simple(type, value):
        a, z = tk(type, value)
        assert len(a.arcs) == 1
        assert len(z.arcs) == 0
        assert len(a.arcs[0]) == 2
        label, next = a.arcs[0]
        assert label == value
        assert next is z
        return a, z

    def check_rhs(type, value):
        a, z = tk(type, value)
        assert a.arcs[0][0] is None
        assert a.arc

# Generated at 2022-06-13 18:07:21.314169
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator()
    pg.dfas = {
        "a": [DFAState(None, None)],
        "b": [DFAState(None, None)],
        "c": [DFAState(None, None)]
    }
    pg.first = {
        "a": {"'a'": 1},
        "b": {"'b'": 1},
        "c": {None: 1}
    }
    pg.symbol2number = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    c = PgenGrammar()
    c.tokens = {
        token.OP: 1,
        token.NAME: 2
    }
    assert pg.make_first(c, "a") == {2: 1}
   

# Generated at 2022-06-13 18:07:27.935153
# Unit test for method dump_nfa of class ParserGenerator
def test_ParserGenerator_dump_nfa():
    from test.test_parser import findfile
    import os

    for dirpath, dirnames, filenames in os.walk(findfile("grammar")):
        for fn in filenames:
            p = ParserGenerator()
            filename = os.path.join(dirpath, fn)
            with tokenize.open(filename) as f:
                contents = f.read()
            print("\n** Testing %s:" % filename)
            g = p.parse_string(contents)
            g.dump_nfa()

# Generated at 2022-06-13 18:07:35.345597
# Unit test for method make_first of class ParserGenerator
def test_ParserGenerator_make_first():
    pg = ParserGenerator(grammar)
    c = pg.make_converter()
    assert c.make_first(c, "<node>") == {8: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
    assert c.make_first(c, "<classdef>") == {8: 1, 1: 1}
    assert c.make_first(c, "<decorated>") == {1: 1}
    assert c.make_first(c, "<decorators>") == {1: 1}
    assert c.make_first(c, "<funcdef>") == {8: 1, 1: 1}
    assert c.make_first(c, "<fpdef>") == {1: 1}
    assert c.make_

# Generated at 2022-06-13 18:07:44.370234
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    import os
    import sys
    import unittest

    basepath = os.path.dirname(__file__)
    basepath = os.path.join(basepath, "..", "Parser")
    if basepath not in sys.path:
        sys.path.insert(0, basepath)
    from pgen2 import driver

    UNINITIALIZED = -1
    INFINITY = -2

    class DFAState:
        __slots__ = "arcs", "isfinal", "seen"

        def __init__(self) -> None:
            self.arcs: Dict[int, "DFAState"] = {}  # Map label to DFAState
            self.isfinal = False
            self.seen = UNINITIALIZED


# Generated at 2022-06-13 18:07:54.555468
# Unit test for method make_dfa of class ParserGenerator
def test_ParserGenerator_make_dfa():
    """Make sure that make_dfa produces the right result for a simple input"""
    pg = ParserGenerator()
    a = NFAState()
    z = NFAState()
    a.addarc(z, 'a')
    z.addarc(a, 'b')
    dfa = pg.make_dfa(a, z)
    assert len(dfa) == 2
    assert dfa[0].arcs == {'a': dfa[1]}
    assert dfa[1].arcs == {'b': dfa[0]}

# Generated at 2022-06-13 18:08:03.549730
# Unit test for method simplify_dfa of class ParserGenerator
def test_ParserGenerator_simplify_dfa():
    parser = ParserGenerator()

# Generated at 2022-06-13 18:08:04.860653
# Unit test for method parse_alt of class ParserGenerator
def test_ParserGenerator_parse_alt():
    pass # testcase.test_parse_alt(ParserGenerator)



# Generated at 2022-06-13 18:08:09.793100
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    """Test the method Grammar.make_label()
    """
    from . import grammar
    from .pgen import ParserGenerator, PgenGrammar, DFAState, NFAState
    from .token import token

    class Token(token):
        STRING = len(token.tok_name)
        NAME = STRING + 1
        NUMBER = STRING + 2
        NEWLINE = STRING + 3

    token.tok_name[Token.STRING] = "STRING"
    token.tok_name[Token.NAME] = "NAME"
    token.tok_name[Token.NUMBER] = "NUMBER"
    token.tok_name[Token.NEWLINE] = "NEWLINE"
    pgen = ParserGenerator()

# Generated at 2022-06-13 18:08:18.716300
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    from . import num_terminals
    p = ParserGenerator()
    c = p.make_converter()
    assert c.tokens == {}
    assert c.keywords == {}
    assert c.labels == []
    assert c.symbol2label == {}
    assert c.symbol2number == {}
    assert c.dfas == {}
    assert c.start == -1
    assert p.make_label(c, "NAME") == 1
    assert c.tokens == {}
    assert c.labels == [(1, None)]
    assert c.keywords == {}
    assert p.make_label(c, "NUMBER") == 2
    assert c.tokens == {2: 1}
    assert c.labels == [(1, None), (2, None)]

# Generated at 2022-06-13 18:10:37.804829
# Unit test for method parse_atom of class ParserGenerator
def test_ParserGenerator_parse_atom():
    # Set up error reporting
    class DummyFilename:
        pass

    filename = DummyFilename()
    filename.name = "tokenizer.py"

    def parse_atom(self, value: Text) -> Tuple[int, int]:
        self.type = token.STRING
        self.value = value
        self.begin = (0, 0)
        self.end = (0, 0)
        self.line = ""
        self.filename = filename
        try:
            a, z = self.parse_atom()
        except SyntaxError as e:
            e.__traceback__ = None
            raise e

    import tokenize

    dummy = ParserGenerator()
    # '[' should produce one character of output
    a, z = parse_atom(dummy, "[")

# Generated at 2022-06-13 18:10:44.252370
# Unit test for method expect of class ParserGenerator
def test_ParserGenerator_expect():
    from .parser import ParserGenerator
    from .pgen import PgenGrammar

    def test_function(parser: ParserGenerator, type: int, value: Any) -> None:
        expected = parser.expect(type, value)
        assert expected == value
        assert parser.type == type
        assert parser.value == value

    def test_function_err(parser: ParserGenerator, type: int, value: Any) -> None:
        try:
            parser.expect(type, value)
        except SyntaxError:
            pass
        else:
            assert False

    g = PgenGrammar()

    p = ParserGenerator(g)
    p.filename = "testfile"
    p.type = token.NAME
    p.value = "a"
    p.line = "code"

# Generated at 2022-06-13 18:10:53.827118
# Unit test for method parse_rhs of class ParserGenerator
def test_ParserGenerator_parse_rhs():
    import sys
    import tokenize
    import io

    def _parse(text):
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
        generator = iter(tokens)
        return ParserGenerator("<string>", generator).parse_rhs()

    a, z = _parse("a")
    assert str(a.arcs) == "({'a': <NFAState 1>},)"
    assert a.arcs[0][1] is z
    assert a.arcs[0][0] == "a"
    assert str(z.arcs) == "()"

    a, z = _parse("a|b")

# Generated at 2022-06-13 18:11:03.516490
# Unit test for method parse_item of class ParserGenerator
def test_ParserGenerator_parse_item():
    pg = ParserGenerator()
    for text, (type, value) in [
        # Text, (tok_type, result)
        ("a", (token.NAME, "a")),
        ("'a'", (token.STRING, "'a'")),
        ("[a]", (token.OP, "[")),
        ("(a)", (token.OP, "(")),
        ("a+", (token.OP, "+")),
        ("a*", (token.OP, "*")),
    ]:
        f = io.StringIO('%s \n' % text)
        tokens = tokenize.generate_tokens(f.readline)
        pg.initialize(tokens)
        pg.gettoken()
        assert pg.type == type, (text, pg.type)
       

# Generated at 2022-06-13 18:11:10.212395
# Unit test for method make_grammar of class ParserGenerator
def test_ParserGenerator_make_grammar():
    pg = ParserGenerator(
        """
      S: 'a'
      """
    )
    c = pg.make_grammar()

    assert c.start == c.symbol2number["S"]
    assert c.start == c.symbol2number["S"]
    assert c.labels == [(97, None)]
    ##assert c.keywords == {}
    assert c.tokens == {}
    assert c.dfas == {0: ([[[(97, 0)], True, {}]], {})}
    assert c.states == [[[[(97, 0)], True, {}]]]
    assert c.symbol2label == {}
    assert c.symbol2number == {"S": 0}


# Generated at 2022-06-13 18:11:15.212549
# Unit test for function generate_grammar
def test_generate_grammar():
    def check_grammar(filename: Path = "Grammar.txt") -> None:
        # Check the structure of the grammar.
        p = ParserGenerator(filename)
        g = p.make_grammar()
        # Make sure there is a "file_input" rule.
        assert g.start not in ("file_input", "eval_input", "single_input")
        assert "file_input" in g.dfas
        # Make sure it has a (optionally empty) sequence of stmts.
        a, z = g.dfas["file_input"][0].arcs["stmt"]

# Generated at 2022-06-13 18:11:25.789929
# Unit test for method make_label of class ParserGenerator
def test_ParserGenerator_make_label():
    c = ParserGenerator("<test>")
    labels = c.labels
    symbols = c.symbol2number
    tokens = c.tokens
    keywords = c.keywords
    assert len(labels) == 0
    assert len(c.symbol2label) == 0
    # First an identifier followed by a number
    for name in "a a1".split():
        assert name not in tokens
        assert name not in symbols
        assert name not in keywords
        i = c.symbol2number[name] = c.make_label(c, name)
        assert len(c.symbol2label) == 1
        assert name in symbols
        assert symbols[name] == i
        assert len(c.labels) == i + 1
        assert c.labels[i] == (token.NAME, name)