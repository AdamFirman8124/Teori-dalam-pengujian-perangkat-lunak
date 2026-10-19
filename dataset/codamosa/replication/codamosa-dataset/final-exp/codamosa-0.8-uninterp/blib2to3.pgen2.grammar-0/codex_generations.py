

# Generated at 2022-06-13 17:49:52.336851
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Test the grammar dump method.
    """
    grammar = Grammar()
    grammar.dump(tempfile.mkstemp()[1])


# Generated at 2022-06-13 17:50:01.922882
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    This is the unit test for Grammar.dump()
    
    The test case is to create a Grammar instance, then dump it to a pickle file,
    then load it back from the pickle file, then use the test data to check whether
    the loaded instance is the same as the created instance.
    
    The test data is GrammarTestData.txt, which is a file containing 
    a pickle dumps of a created Grammar instance
    """
    import sys
    import pickle
    import os
    
    if 'test' in sys.argv:
        # generate test data if 'test' argument is in sys.argv
        g = Grammar()

# Generated at 2022-06-13 17:50:06.964595
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    test_grammar = Grammar()
    tmp = tempfile.NamedTemporaryFile()
    test_grammar.dump(tmp.name)
    tmp.file.close()

# Generated at 2022-06-13 17:50:16.213203
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gram = Grammar()
    gram_dump = Grammar.dump

    # Case 1: normal case
    # FIXME:  I don't know how to set up a fixture for the cases
    # below.  Perhaps we should reuse the test grammar pgen generates in
    # the test directory?
    gram_dump("t.pkl")

    # Case 2: filename = ""
    # FIXME:  How to cover this case?
    gram_dump("")

    # Case 3: filename = None
    # FIXME:  How to cover this case?
    # gram_dump(None)


# Generated at 2022-06-13 17:50:21.205656
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Unit test for method load of class Grammar"""

    import parser
    import conv
    import sys

    if sys.version_info < (3, 8):
        p = conv.PyGrammar()
    else:
        p = conv.Py3Grammar()
    p.dump("Grammar.cache")
    p1 = Grammar()
    p1.load("Grammar.cache")
    parser.suite(p1)



# Generated at 2022-06-13 17:50:26.757623
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    a = Grammar()
    a.dump("a.pkl")
    b = Grammar()
    b.load("a.pkl")
    assert a.symbol2number == b.symbol2number
    assert a.number2symbol == b.number2symbol
    assert a.states == b.states
    assert a.dfas == b.dfas
    assert a.labels == b.labels
    assert a.start == b.start

# Generated at 2022-06-13 17:50:32.209310
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    if __name__ != "__main__":
        import pytest
        pytest.skip("not a test")

    tmpfile = tempfile.mktemp(prefix='parser_grammar_',
                              suffix='.pickle', dir='.')
    try:
        g = Grammar()
        g.dump(tmpfile)
        print("tmpfile =", tmpfile)
    finally:
        try:
            os.unlink(tmpfile)
        except OSError:
            pass

if __name__ == "__main__":
    test_Grammar_dump()

# Generated at 2022-06-13 17:50:36.237408
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

    f = "bad_name_does_not_exist/foobar"

    try:
        g.dump(f)
    except (OSError, IOError):
        pass
    else:
        raise AssertionError("dump() did not fail on invalid filename")

# Generated at 2022-06-13 17:50:41.761435
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import conv
    from .pgen2 import driver

    f = driver.find_grammar("python3.7")
    g = driver.load_grammar(f)
    c = conv.Converter(g)
    c.convert()
    c.grammar.dump("test_Grammar.dump")


__all__ = ["Grammar", "opmap", "test_Grammar_dump"]

# Generated at 2022-06-13 17:50:46.194382
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # This can't be a unit test, because the name of the temporary
    # file is hard-coded.  It's not clear how to make a temporary
    # file, write to it, and close it in such a way that the name can
    # be passed back to the function being tested.
    from .pgen2 import driver

    driver.compile(["compiler/parse.txt"])
    driver.main(["compiler/parse.txt"])

# Generated at 2022-06-13 17:50:58.717539
# Unit test for method load of class Grammar
def test_Grammar_load():
    # test_Grammar_load_is_symmetric
    g1 = Grammar()
    g1.symbol2number = {
        "foo": 1,
        "bar": 2,
    }
    g1.number2symbol = {
        1: "foo",
        2: "bar",
    }
    g1.dfas = {
        1: ([[(1, 2)]], {1: 0}),
    }
    g1.states = [[[(1, 2)]]]
    g1.labels = [(1, None)]
    with tempfile.NamedTemporaryFile() as file:
        g1.dump(file.name)
        g2 = Grammar()
        g2.load(file.name)
        assert g2.symbol2number == g1.symbol

# Generated at 2022-06-13 17:51:07.892710
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

# Generated at 2022-06-13 17:51:12.061279
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver
    from .pgen2 import tokenize

    g = Grammar()
    g.load(driver.find_grammar("python3.6"))
    with open("Grammar.py", "rb") as f:
        g2 = Grammar()
        g2.loads(f.read())
    print(g2.symbol2number)
    print(g2.number2symbol)
    print(g2.states)
    print(g2.dfas)
    print(g2.labels)
    print(g2.start)

# Generated at 2022-06-13 17:51:22.228134
# Unit test for method load of class Grammar
def test_Grammar_load():
    import sys
    import types
    import unittest
    import os
    import test.support

    class TestGrammarLoader(unittest.TestCase):
        def setUp(self):
            self.tmpdir = test.support.TESTFN
            os.mkdir(self.tmpdir)
            self.cwd = os.path.realpath(os.curdir)
            os.chdir(self.tmpdir)
            self.loader = Grammar()
            self.globs = {"Grammar": Grammar}

        def tearDown(self):
            os.chdir(self.cwd)
            test.support.rmtree(self.tmpdir)

        def test_load(self):
            path = 'test'
            expected = Grammar()

# Generated at 2022-06-13 17:51:32.995000
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Test for method load of class Grammar."""
    # Read pickle file
    from . import pgen2
    from . import tokenizer
    from . import parsetok

    gr = Grammar()
    gr.dump("Grammar.pickle")
    gr.load("Grammar.pickle")

    # Test parsing
    pt = parsetok.Parser()
    pt.set_grammar(gr)
    t = tokenizer.Tokenizer()

    py_string = b"1 + 2"
    node = pt.parse(t.generate_tokens(py_string), True)
    assert node is not None

    py_string = b"1 ;"
    node = pt.parse(t.generate_tokens(py_string), True)
    assert node is not None

    py_string

# Generated at 2022-06-13 17:51:35.849104
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    tf = tempfile.NamedTemporaryFile(prefix='tmp_grammar_')
    g.dump(tf.name)
    tf.close()
    os.remove(tf.name)

# Generated at 2022-06-13 17:51:43.628205
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

    try:
        g.loads(b'0\n.')
    except pickle.UnpicklingError as e:
        assert str(e) == "the STRING opcode argument must be quoted"
    else:
        assert False, "expected exception"

    try:
        g.loads(b'''cos\nsystem\n(S'echo HACKED'\ntR.''')
    except pickle.UnpicklingError as e:
        assert str(e) == "could not find MARK"
    else:
        assert False, "expected exception"


# Generated at 2022-06-13 17:51:54.563609
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.symbol2number = {'foo': 1, 'bar': 2}
    g.number2symbol = {1: 'foo', 2: 'bar'}
    g.states = [ [[(1,0)], [(0,2), (2,3)]] ]
    g.dfas = {1: ([[(1,0)], [(0,2), (2,3)]], {42: 1})}
    g.labels = [(0, 'EMPTY'), (1, None), (2, None)]
    g.keywords = {'foo': 2, 'bar': 3}
    g.tokens = {42: 4}
    g.symbol2label = {'baz': 3}
    g.start = 4
    g.async_keywords = False

   

# Generated at 2022-06-13 17:51:58.747082
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import parse

    filename = os.path.join(os.path.dirname(__file__), "Grammar.pkl")
    parse.Grammar().load(filename)



# Generated at 2022-06-13 17:51:59.656768
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gr = Grammar()
    gr.dump("test")