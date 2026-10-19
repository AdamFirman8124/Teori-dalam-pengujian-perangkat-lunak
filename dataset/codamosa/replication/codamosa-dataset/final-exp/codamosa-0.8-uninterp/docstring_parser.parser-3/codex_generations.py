

# Generated at 2022-06-13 19:41:30.534191
# Unit test for function parse
def test_parse():
  text = '''This is the first line of the docstring.

This is the second line of the docstring.

Args:
  arg1: First argument.
  arg2: Second argument.

Returns:
  This is the return.

Raises:
  This is a raise.
'''
  print(parse(text))


if __name__ == '__main__':
  test_parse()

# Generated at 2022-06-13 19:41:34.106126
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = """Test stub of parse function.
    Args:
        text: docstring text to parse
        style: docstring style
    Returns:
        parsed docstring representation
    """
    doc = "Test stub of parse function."
    assert parse(text) == doc

# Generated at 2022-06-13 19:41:35.406605
# Unit test for function parse
def test_parse():
    docstring = parse(__doc__)
    print(docstring.meta)
    s = ','.join(docstring.meta)
    print(s)

# Generated at 2022-06-13 19:41:40.231544
# Unit test for function parse
def test_parse():
    """Check that the parser works for a docstring.
    """
    text = """
Parse the docstring into its components.

:param text: docstring text to parse
:param style: docstring style
:returns: parsed docstring representation
"""

# Generated at 2022-06-13 19:41:46.585186
# Unit test for function parse
def test_parse():
    """
    Test that parse() works for all docstring styles.
    """

    for style in Style:
        text = '''
        This is a valid docstring.
        '''
        docstring = parse(text, style)
        assert docstring.short_description == 'This is a valid docstring.'


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:41:54.043309
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    # test that the docstring is equal to itself after parsing
    text = '''
        Calculate the square of a number.

        :param x: The number to square.
    '''
    text2 = ''.join(parse(text).meta)
    assert text == text2
    # test that the docstring is equal to itself after parsing
    text = '''
        Calculate the square of a number.

        :param x: The number to square.
    '''
    text2 = ''.join(parse(text).meta)
    assert text == text2

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:02.828279
# Unit test for function parse
def test_parse():
	text = '''This is a docstring that is not a valid numpydoc docstring.
		"""
		Parameters
		----------

		Returns
		-------


		Notes
		-----


		Examples
		--------

		"""
		'''
		
	#st = Style.numpy
	st = Style.auto
	docs = parse(text, style=st)
	print(docs.metadata['Parameters'])
	print(docs.metadata['Returns'])
	print(docs.metadata['Notes'])
	print(docs.metadata['Examples'])

if __name__ == "__main__":
	test_parse()

# Generated at 2022-06-13 19:42:09.695876
# Unit test for function parse
def test_parse():
    docstring_text = """Module description.

Args:
    arg1 (int): Description of `arg1`
    arg2 (str): Description of `arg2`.

"""
    doc = parse(docstring_text)
    assert doc.short_description == 'Module description.'
    assert doc.long_description == ''
    assert doc.meta == {'arg1': 'int', 'arg2': 'str'}
    assert doc.content['arg1'] == 'Description of `arg1`'
    assert doc.content['arg2'] == 'Description of `arg2`.'

# Generated at 2022-06-13 19:42:23.989017
# Unit test for function parse
def test_parse():

    # Test case 1
    correct_result = True
    try:
        docstring = parse('Test case 1: No style specified')
    except ParseError as e:
        correct_result = False
    assert (correct_result)

    # Test case 2
    correct_result = False
    try:
        docstring = parse('Test case 2: Nonexistent style')
    except ParseError as e:
        correct_result = True
    assert (correct_result)

    # Test case 3
    correct_result = True
    try:
        docstring = parse('Test case 3: No style specified, but the string is valid', Style.numpy)
    except ParseError as e:
        correct_result = False
    assert (correct_result)

    # Test case 4
    correct_result = True

# Generated at 2022-06-13 19:42:28.192104
# Unit test for function parse
def test_parse():
    a = parse(text)
    print(a)
    assert a.summary == "Convert a block of text into a list of its paragraphs."

test_parse()



# ------------------------------------------------------------------------------

"""
    Unit test for function get_docstring
    """

# Generated at 2022-06-13 19:42:39.089654
# Unit test for function parse
def test_parse():
    assert parse.__doc__ == "Parse the docstring into its components.\n\n    :param text: docstring text to parse\n    :param style: docstring style\n    :returns: parsed docstring representation\n    "
    # Test: Base case
    try:
        return_val_1 = parse("Test")
        raise Exception("Test 1 Failed")
    except ParseError as pe:
        pass
    # Test: Test for all styles
    try:
        return_val_2 = parse("Test", style=Style.auto)
        raise Exception("Test 2 Failed")
    except ParseError as pe:
        pass



# Generated at 2022-06-13 19:42:47.658911
# Unit test for function parse
def test_parse():
    docstring = """
    This doc is written in Google style format
    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.
    """
    parsed_doc = parse(docstring, style='google')
    assert parsed_doc.args[0].name == 'arg1'
    assert parsed_doc.args[0].type_name == 'int'
    assert parsed_doc.args[0].description == 'The first argument.'
    assert parsed_doc.args[1].name == 'arg2'
    assert parsed_doc.args[1].type_name == 'str'
    assert parsed_doc.args[1].description == 'The second argument.'


# Generated at 2022-06-13 19:42:57.537604
# Unit test for function parse
def test_parse():
    text = r'''
    Title
    -------

    Summary line.

    Extended description.

    Parameters
    ----------
    arg1 : int
        Description of `arg1`
    arg2 : str
        Description of `arg2`

    Returns
    -------
    int
        Description of return value
    '''
    assert parse(text, Style.numpy).params == [
        {
            'name': 'arg1',
            'type': 'int',
            'description': 'Description of `arg1`'
        },
        {
            'name': 'arg2',
            'type': 'str',
            'description': 'Description of `arg2`'
        }
    ]


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:03.332555
# Unit test for function parse
def test_parse():
    import os
    from docstring_parser.common import Docstring
    from pathlib import Path
    SRC_DIR = os.path.dirname(__file__)
    # Test for Numpy style
    numpy_path = Path(SRC_DIR, 'tests/numpy_docstring.txt')
    assert isinstance(parse(numpy_path.read_text()), Docstring)
    # Test for Google style
    google_path = Path(SRC_DIR, 'tests/google_docstring.txt')
    assert isinstance(parse(google_path.read_text()), Docstring)

# Generated at 2022-06-13 19:43:06.870363
# Unit test for function parse
def test_parse():
    """Test for function parse"""
    text = "function to fill a line with bytes"
    assert parse(text, style=Style.google) is not None


# Generated at 2022-06-13 19:43:16.347241
# Unit test for function parse
def test_parse():
    text = '''"""Module summary line.

This is a multi-line description.
Which may contain:

    * inline markup
    * and code samples
    * like this one

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.
        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.
    module_level_variable2 (list): Descriptions should be in the form of
        sentences, and each sentence should end with a period.

.. _PEP 257:
    https://www.python.org/dev/peps/pep-0257/
"""'''

# Generated at 2022-06-13 19:43:20.087929
# Unit test for function parse
def test_parse():
    doc1='''This is a docstring.
    :parameter name: description
    '''
    assert parse(doc1).description=='This is a docstring.', "Error in parse function"


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:23.613713
# Unit test for function parse
def test_parse():
    """We test all of the unit tests that exist within the original docstring.
    
    This function is a unit test for the function parse.
    """
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 19:43:27.690700
# Unit test for function parse
def test_parse():
    """Test for function parse"""
    txt ="""
    Parameters
    ----------
    text : str
        Text to be parsed
    style : Style
        docstring style
    Returns
    -------
    Docstring, parsed docstring representation
    """
    assert parse(txt)


# Generated at 2022-06-13 19:43:33.622864
# Unit test for function parse
def test_parse():
    assert(parse("""This is a
    one sentence summary

    And this is the same sentence but with a little more words.

    Parameters
    ----------
    args1 : str
        argument 1
    args2 : str
        argument 2

    Returns
    -------
    str
        returned string
    """))

test_parse()

# Generated at 2022-06-13 19:43:38.873030
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleDocstring
    assert type(parse('the text')) is GoogleDocstring


# Generated at 2022-06-13 19:43:46.756290
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    text = '''"""
# Parameters
    X: array-like, shape (n_samples, n_features)
        Training data, where n_samples is the number of samples and n_features
        is the number of features.
    y: array-like, shape (n_samples,)
        Target values (class labels in classification, real numbers in
        regression)
        For classification, labels must correspond to classes.

# Returns
    H : array-like, shape = [n_features, n_features] or [n_features,
    n_features+1]
        H : array-like, shape = [n_features, n_features] or [n_features,
        n_features+1]
    """
    '''
    print(parse(text))


# Generated at 2022-06-13 19:43:57.383385
# Unit test for function parse
def test_parse():
    """Test for function parse."""
    doc = parse('abc')
    assert doc.full_docstring == 'abc'
    doc = parse('abc\n\nExtra text', style=Style.google)
    assert doc.full_docstring == 'abc\n\nExtra text'
    doc = parse('abc\n\nExtra text', style=Style.numpy)
    assert doc.full_docstring == 'abc\n\nExtra text'
    doc = parse('abc\n\nExtra text', style=Style.reStructuredText)
    assert doc.full_docstring == 'abc\n\nExtra text'
    doc = parse('abc\n\nExtra text', style=Style.sphinx)
    assert doc.full_docstring == 'abc\n\nExtra text'



# Generated at 2022-06-13 19:44:07.657749
# Unit test for function parse
def test_parse():
    assert parse('').summary == ''
    assert parse('Summary').summary == 'Summary'
    assert parse('Summary.\n').summary == 'Summary.'
    assert parse('Summary.\n\nExtended.').summary == 'Summary.'
    assert parse('Summary.\n\nExtended.').extended_summary == 'Extended.'

    # Google style


# Generated at 2022-06-13 19:44:11.792812
# Unit test for function parse
def test_parse():
    s = """
    """
    d = parse(s)
    assert d.short_description == ''
    assert d.long_description == ''
    assert d.extended_summary == ''
    assert d.params == {}
    assert d.return_annotation == ''
    assert d.examples == []
    assert d.exceptions == []
    assert d.yields == ''

# Generated at 2022-06-13 19:44:12.848545
# Unit test for function parse
def test_parse():
    assert 1 == 0

# Generated at 2022-06-13 19:44:22.440396
# Unit test for function parse
def test_parse():
    docstring = parse.__doc__
    doc = parse(docstring, Style.numpy)
    assert doc.short_description == "Parse the docstring into its components."
    assert doc.meta["param"]["text"] == "docstring text to parse"
    assert doc.meta["param"]["type"] == "str"
    assert doc.meta["param"]["name"] == "text"
    assert doc.meta["param"]["arg_name"] == "text"
    assert doc.meta["returns"]["text"] == "parsed docstring representation"

# Generated at 2022-06-13 19:44:32.965144
# Unit test for function parse
def test_parse():
    """Test function parse."""
    text = """\
        This is the description.
        And this is the second line of the description.

        :param param1: This is the first parameter.
        :param param2: This is the second parameter.
        :returns: This is what is returned.
        :raises keyError: This is a description of a raised exception.
        """

    d = parse(text)
    assert d.short_description == "This is the description."
    assert d.long_description == "And this is the second line of the description."
    assert len(d.params) == 2
    assert d.params["param1"] == "This is the first parameter."
    assert d.params["param2"] == "This is the second parameter."
    assert d.returns == "This is what is returned."
    assert len

# Generated at 2022-06-13 19:44:39.260813
# Unit test for function parse
def test_parse():
    docstring = '''
    This is documentation for the module

    Arguments:
        arg1: Argument number one
        arg2: Argument number two

    Returns:
        int: return value
    '''

    ds = parse(docstring)
    assert(len(ds.args) == 2)
    assert(ds.args[0].name == 'arg1')
    assert(ds.args[1].name == 'arg2')
    assert(len(ds.returns) == 1)

# Generated at 2022-06-13 19:44:46.945885
# Unit test for function parse
def test_parse():
    """Test the docstring parser."""
    expected = Docstring(
        summary=['Hello world'],
        description=['This is a test'],
        parameters=[
            ('x', 'The first variable.'),
            ('y', 'The second variable.')],
        return_=['This is a return value'],
        meta={'author': 'John Doe'})
    assert parse(
        """Hello world
    :param x: The first variable.
    :type x: int
    :param y: The second variable.
    :type y: int
    :return: This is a return value
    :rtype: str
    :author: John Doe
    :raises ImportError: when importing

    This is a test""", Style.pep257) == expected

# Generated at 2022-06-13 19:44:57.122968
# Unit test for function parse
def test_parse():

    text = '''
        Parse the docstring into its components.

        :param text: docstring text to parse
        :param style: docstring style
        :returns: parsed docstring representation
        :raises ParseError: if the docstring is malformed
        '''

    # >>> parse(text)  # doctest: +NORMALIZE_WHITESPACE
    # Docstring(summary='Parse the docstring into its components.',
    #           body='',
    #           params=[Parameter(name='text',
    #                             param_type='str',
    #                             description='docstring text to parse'),
    #                   Parameter(name='style',
    #                             param_type='Style',
    #                             description=None)],
    #           returns=Parameter(name=None,
    #                            

# Generated at 2022-06-13 19:45:02.435471
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.numpy import NumpyParser
    from docstring_parser.docstring import FunctionDocstring
    text = """    This is the docstring of a function

    Parameters
    ----------
    param1 : str
        Parameter 1.
    param2 : int
        Parameter 2.

    Returns
    -------
    str
        Return value.
    """
    result = parse(text, style=Style.numpy)

    assert isinstance(result, FunctionDocstring)
    assert len(result.summary) == 2
    assert len(result.parameters) == 2


# Generated at 2022-06-13 19:45:11.696996
# Unit test for function parse
def test_parse():
    print("Unit test for function parse")
    text = """\
    This is the docstring of this function.
    It can span multiple lines.

    :param parameter: A parameter
    :returns: What the function returns
    """
    print("text:", text)
    p = parse(text, Style.numpy)
    print("p:", p)
    print("Parse succeeds:", p is not None)
    print("p.short_description:", p.short_description)
    print("p.long_description:", p.long_description)
    print("p.meta:", p.meta)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:45:19.517041
# Unit test for function parse
def test_parse():
    docstring = """Summarize the Docstring.
    Extracted from the section under the first heading.

    This is a multiline summary, it can contain newlines and all kinds of punctuation.

    Args:
        param1(int): The first parameter.
        param2(str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    result = parse(docstring, style=Style.google)
    assert result.short_description == "Summarize the Docstring."
    assert result.long_description == """Extracted from the section under the first heading.
    This is a multiline summary, it can contain newlines and all kinds of punctuation."""
    assert result.meta["param1"][0].arg_type == "int"

# Generated at 2022-06-13 19:45:27.205314
# Unit test for function parse
def test_parse():
    print(parse("""
    :param blk: The block that this code snippet belongs to.
    :param code: The code snippet content as a list of lines.
    :param lineno: The line number where this code snippet starts.
    :param indent: The indentation of this code snippet.
    :param filename: The filename of this code snippet.
    :param options: An option dictionary to render this code snippet.
    :param encoding: The encoding of this code snippet.
    :param analysis: A list of tuples, containing the text of the line and the analysis
        results for syntax highlighting.
    """))


# Generated at 2022-06-13 19:45:31.569870
# Unit test for function parse
def test_parse():
    """ Test for function parse """
    docstring = parse('''The function is used to parse a docstring into its components.

    :param text: docsting text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    ''')
    print(docstring)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:37.673146
# Unit test for function parse
def test_parse():
    text = '''
        This function adds two numbers
        :param x: first number
        :type x: int
        :param y: second number
        :type y: int
        :return: sum of two numbers
    '''
    doc = parse(text, style=Style.numpy)
    assert doc.format() == text, "test_parse error"

# Test for function parse
test_parse()

# Generated at 2022-06-13 19:45:46.440588
# Unit test for function parse
def test_parse():

    def f():
        """The function.

        :param a: parameter

        :Example:

        >>> f()
        <function f at 0x00000000023B27B8>

        :returns: None
        """
        pass
    res = parse(f.__doc__)
    assert res.short_description == 'The function.'
    assert len(res.params) == 1
    assert res.params['a'].description == 'parameter'
    # assert res.params['a'].type == 'str'
    assert res.example == '>>> f()\n<function f at 0x00000000023B27B8>'
    assert res.returns.description == 'None'
    # assert res.returns.type == 'NoneType'
    assert res.yields is None
    assert res.raises is None

# Generated at 2022-06-13 19:45:49.896032
# Unit test for function parse
def test_parse():
    text='@author: A random guy'
    parsed_docstring = parse(text)
    assert parsed_docstring.meta['author']=='A random guy'

# Generated at 2022-06-13 19:45:54.069190
# Unit test for function parse
def test_parse():
    docstring = parse(text)
    print(docstring)
    print(docstring.short_description)
    print(docstring.long_description)
    print(docstring.meta)
    print('\n'.join(docstring.meta.get('parameters', [])))



# Generated at 2022-06-13 19:45:58.546599
# Unit test for function parse
def test_parse():
    doc_string = ('This is a docstring\n'
                  '\n'
                  'Args:\n'
                  '    param1: First parameter\n'
                  '    param2: Second parameter\n'
                  '\n'
                  'Returns:\n'
                  '    Return param1 and param2 in a list')
    style = Style.google
    doc = parse(doc_string, style)
    print(doc.params[0].description)
    print(doc.params[1].description)


# Generated at 2022-06-13 19:46:04.025492
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    style = GoogleStyle()
    docstring = """This is a test function.
    :param str x: x parameter
    :param int y: y parameter
    :returns: 2*x
    """
    parsed = parse(docstring)
    assert parsed == style.parse(docstring)

# Generated at 2022-06-13 19:46:04.576105
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:46:15.279524
# Unit test for function parse
def test_parse():
    text = """\
    This function does something.

    This is a really long sentence that describes this function in an extensive
    manner.

    :param int arg1: the first argument
    :param arg2: the second argument
    :type arg2: str
    :returns: description of return value
    :rtype: int
    """


# Generated at 2022-06-13 19:46:25.554785
# Unit test for function parse
def test_parse():
    doct = """This is a test docstring.
    :param test_param1: param1
    :param test_param2: param2
    :returns: return value
    :raises: raise an exception"""
    try:
        d = parse(doct)
        assert d == Docstring(description='This is a test docstring.',
                            meta={'param': ['test_param1: param1', 'test_param2: param2'],
                            'return': ['return value'],
                            'raise': 'raise an exception'})
        return True
    except:
        return False


# Generated at 2022-06-13 19:46:36.925216
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.google import Google as S
    from docstring_parser.common import Docstring

    text = """
    This is a description.

    :param str arg1: Argument 1.
    :param arg2: Argument 2.
    :returns: Something.
    :rtype: str
    """
    style = Style.google

    import doctest
    assert doctest.testmod().failed == 0
    assert parse(text) == S(text)
    assert parse(text, style) == S(text)
    assert parse(Docstring(text), style) == S(text)


# Generated at 2022-06-13 19:46:38.529961
# Unit test for function parse
def test_parse():
    d = parse('****')
    assert d == parse('****')


# Generated at 2022-06-13 19:46:47.007874
# Unit test for function parse
def test_parse():
    """Test for parse function"""
    from docstring_parser.common import Docstring
    text = '''
    Parse the docstring into its components.

    Params
    ------
    text: str
        docstring text to parse
    style: Style
        docstring style
    Returns
    -------
    Docstring
        parsed docstring representation
    '''
    docstring = parse(text=text, style=Style.google)
    assert(docstring.summary=="Parse the docstring into its components.")
    assert(docstring.description=="")
    assert(len(docstring.params)==2)
    assert(docstring.returns.name=="Docstring")
    assert(docstring.returns.description=="parsed docstring representation")
    assert(len(docstring.meta)==4)

# Generated at 2022-06-13 19:46:48.672801
# Unit test for function parse
def test_parse():
    assert parse("Test docstring") == Docstring(summary="Test docstring")

# Generated at 2022-06-13 19:46:56.455531
# Unit test for function parse
def test_parse():
    text = "Title\n\n:param x: some description\n:returns: nothing"
    docstring = parse(text)
    assert len(docstring.sections) == 2
    assert docstring.sections[0].name == 'Parameters'
    assert len(docstring.sections[0].content) == 1
    assert docstring.sections[0].content[0].argname == 'x'
    assert docstring.sections[1].name == 'Returns'

# Generated at 2022-06-13 19:47:09.850894
# Unit test for function parse
def test_parse():
    def func():
        """Brief summary for function.

        Extended description for function.

        Parameters
        ----------
        arg1 : int
            Description of `arg1`
        arg2 : str
            Description of `arg2`

        Examples
        --------
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> a = [1, 2, 3]

        """
        pass
    ds = parse(func.__doc__)
    assert ds.summary == 'Brief summary for function.'
    assert ds.extended_summary == 'Extended description for function.'
    assert len(ds.parameters) == 2
    assert ds.parameters[0].name == 'arg1'
    

# Generated at 2022-06-13 19:47:20.028749
# Unit test for function parse
def test_parse():
    assert parse("", style=Style.google) == Docstring("", "", [])
    assert parse("", style=Style.numpy) == Docstring("", "", [])
    assert parse("", style=Style.sphinx) == Docstring("", "", [])
    assert (parse("a\n", style=Style.google) ==
            Docstring("a", "", []))
    assert (parse("a\n", style=Style.numpy) ==
            Docstring("a", "", []))
    assert (parse("a\n", style=Style.sphinx) ==
            Docstring("a", "", []))
    assert (parse("a\n", style=Style.auto) ==
            Docstring("a", "", []))

# Generated at 2022-06-13 19:47:20.729630
# Unit test for function parse
def test_parse():
    print(parse("""string"""))

# Generated at 2022-06-13 19:47:26.294254
# Unit test for function parse
def test_parse():
    assert parse('one two three') == parse('one two three', Style.pep257)
    assert parse('one two three') == parse('one two three', Style.dunno)
    assert parse('one two three') != parse('one two three', Style.google)
    assert parse('one two three') != parse('one two three', Style.numpy)

# Generated at 2022-06-13 19:47:30.287747
# Unit test for function parse
def test_parse():
    text = """This is a sample docstring that demonstrates how to
    use the Docstring parser.

    Some more
    text.

    :param arg1: first argument
    :param arg2: second argument
    :returns: nothing
    """

    print(parse(text))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:35.885655
# Unit test for function parse
def test_parse():
    # docstring text to parse
    text = '''
    This is a test docstring to parse
    :param hello: test1
    :param world: test2
    '''
    # docstring style
    style = Style.google
    d = parse(text, style)
    print(d.meta)
    print(d.short_description)
    print(d.description)
    print(d.long_description)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:47:44.911584
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    raw_docstring = '''Single line summary.
    Extended description.

    Args:
        arg1: The first argument.
        arg2: The second argument.

    Raises:
        KeyError: The `key` is not found.

    Returns:
        The return value. True for success, False otherwise.
    '''
    docstring = parse(raw_docstring)
    assert docstring == GoogleStyle(raw_docstring)
    return


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:47:47.456912
# Unit test for function parse
def test_parse():
    print(parse('''
    parsed
    '''))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:58.555861
# Unit test for function parse
def test_parse():
    """
    This function tests the function parse.
    """
    from collections import Counter
    from docstring_parser.common import Argument, Parameter, Return, Variable, Value
    from docstring_parser.styles import Numpy

    docstring = """Example function with types documented in the docstring.

Args:
    param1 (int): The first parameter.
    param2 (:obj:`str`, optional): The second parameter. Defaults to 'test'.
        The third line of description should be longer so we can see what
        happens when it wraps to the next line.
    param3 (list of :obj:`str`): The fourth parameter.

    param_x, param_y, param_z (int, str): Multiple parameters
        on a single line.

Returns:
    bool: The return value. True for success, False otherwise.
"""


# Generated at 2022-06-13 19:48:04.151895
# Unit test for function parse
def test_parse():
    """Test the parse function"""


# Generated at 2022-06-13 19:48:16.461191
# Unit test for function parse
def test_parse():
    test_docstring1 = '''
    :param fname: file name
    :type fname: str
    :param lmode: file mode
    '''
    test_docstring2 = '''
    :param fname: file name
    :type fname: str
    '''
    p1 = parse(test_docstring1, style = 'google')
    p2 = parse(test_docstring2, style = 'google')
    assert (p1.params['fname'].type_name == 'str')
    assert (p1.params['fname'].description == 'file name')
    assert (p1.params['lmode'].type_name == 'None')
    assert (p1.params['lmode'].description == 'file mode')
    assert (p1.returns is None)

# Generated at 2022-06-13 19:48:32.889075
# Unit test for function parse
def test_parse():
    docstring = """\
one line summary

longer
multiline
description

:param arg1_name: description of arg1
:type arg1_name: ``str``
:param arg2_name: description of arg2
:type arg2_name: ``int``
:returns: description of return value
:rtype: ``bool``"""

    parsed = parse(docstring, style=Style.numpy)

    assert parsed.short_description == "one line summary"
    assert parsed.long_description == "longer\nmultiline\ndescription"
    assert parsed.returns.description == "description of return value"
    assert parsed.returns.type_name == "bool"
    assert parsed.returns.annotation == "bool"
    assert len(parsed.params) == 2

# Generated at 2022-06-13 19:48:42.038129
# Unit test for function parse
def test_parse():
    assert parse("""
    A sample docstring.

    Args:
        alpha: some number
        beta: another number
    Returns:
        gamma: a third number
    """)==Docstring(
            content_blocks=[],
            meta={
                'Args': [
                    ('alpha', 'some number'),
                    ('beta', 'another number'),
                    ],
                'Returns': [
                    ('gamma', 'a third number'),
                    ]
                },
            summary='A sample docstring.',
            )


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)

# Generated at 2022-06-13 19:48:49.954512
# Unit test for function parse

# Generated at 2022-06-13 19:48:53.486210
# Unit test for function parse
def test_parse():
    d = parse("""Summary line.

    Extended description.
    """, style=Style.pep257)
    assert d.summary == 'Summary line.'
    assert d.description == 'Extended description.\n'
    

# Generated at 2022-06-13 19:48:58.835507
# Unit test for function parse
def test_parse():
    text = '''
        line 1
        line 2
    '''
    docstring = parse(text)
    assert type(docstring.summary) is str
    assert type(docstring.extended_summary) is str
    assert type(docstring.parameters) is Docstring._Parameters
    assert type(docstring.returns) is str
    assert type(docstring.meta) is Docstring._Meta


# Generated at 2022-06-13 19:49:01.316671
# Unit test for function parse
def test_parse():
    text = """one-line short description

    extended description
    """
    parsed = parse(text)
    assert "one-line short description" == parsed.short_description



# Generated at 2022-06-13 19:49:02.952226
# Unit test for function parse
def test_parse():
    test_text = """
    Unit test for function parse
    """
    assert parse(test_text)

# Generated at 2022-06-13 19:49:11.436503
# Unit test for function parse
def test_parse():
    """Test parse() in docstring_parser.parse"""
    test_example_text = '''
        Description:
            Description line 1
            Description line 2
        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2
        Returns:
            int: Description of return value
    '''
    # make sure parse returns a docstring object
    assert type(parse(test_example_text)) == Docstring
    # test for the length of the parsed docstring
    assert len(parse(test_example_text).meta) == 3
    # test for the length of the parsed docstring:args
    assert len(parse(test_example_text).meta['Args']) == 2


# Generated at 2022-06-13 19:49:21.257383
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import google, numpy
    c = '''\
    Returns the name of the Numerical Python module.

    Parameters
    ----------
    numbers : a sequence of integers
        Return the first value in the sequence.

    Returns
    -------
    value : int
        The first value in the sequence.

    Other Parameters
    ----------------
    value : int
        A value to return.

    Raises
    ------
    Error
        If an error occurred.
    '''

    parser = parse(c, Style.google)
    assert parser.doc == "Returns the name of the Numerical Python module."
    assert parser.args == [{'arg': 'numbers', 'type': None, 'desc': 'a sequence of integers\n        Return the first value in the sequence.'}]

# Generated at 2022-06-13 19:49:32.334672
# Unit test for function parse
def test_parse():
    text = """ """
    style = Style.google
    docstring = parse(text, style)
    assert docstring.summary == ""
    assert docstring.description == ""
    assert docstring.extended_summary == ""
    assert docstring.params == []
    assert docstring.returns == None
    assert docstring.yields == None
    assert docstring.raises == []
    assert docstring.warns == []
    assert docstring.attention == []
    assert docstring.version_added == None
    assert docstring.version_changed == None
    assert docstring.deprecated == None
    assert docstring.meta == {}
    assert docstring.examples == []
    assert docstring.see_also == []
    assert docstring.references == []
    assert docstring.notes == []
    assert docstring

# Generated at 2022-06-13 19:49:38.998432
# Unit test for function parse
def test_parse():
    """ Unit test for function parse """
    text = '''
    :param int i: Blah blah
    :returns: Blah blah
    '''
    docstring = parse(text)
    assert docstring.meta["parameters"][0]['name'] == 'i'
    assert docstring.meta["returns"]['name'] == ''
    print(docstring)

# Generated at 2022-06-13 19:49:40.207260
# Unit test for function parse
def test_parse():
    assert parse("").meta == []

# Generated at 2022-06-13 19:49:53.852536
# Unit test for function parse
def test_parse():
    # Test case for parsing docstring in sphinx style
    doc_string = "This is a sample code for testing docstring parsing in Sphinx style"
    doc_string_keyword = "sample code"
    doc_string_short_summary = "This is a sample code for testing docstring parsing in Sphinx style"
    doc_string_summary = "This is a sample code for testing docstring parsing in Sphinx style"
    parsed_doc_string = parse(doc_string, style=Style.sphinx)
    assert (parsed_doc_string.keywords[0].key == "sample code")
    assert (parsed_doc_string.short_summary == doc_string_short_summary)
    assert (parsed_doc_string.summary == doc_string_summary)

    # Test case for parsing docstring in google style

# Generated at 2022-06-13 19:49:56.936265
# Unit test for function parse
def test_parse():
    docstring = """Parameters
----------
p : float
    The value of the pressure.
"""
    d = parse(docstring)
    assert d.short_description == "Parameters"
    assert len(d.params) == 1

# Generated at 2022-06-13 19:50:07.342246
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.google import GoogleStyle
    actual = parse("""\
Overview
Definitions
  - $f: A function.
  - $a: An argument.
Syntax
  $f($a)
Side Effect
  None
Raises
  - ValueError: If $a is invalid.
Returns
  True if $a is valid, False otherwise.
""")
    expected = Docstring(
        overview='Overview',
        definitions=[
            ('$f', 'A function.'),
            ('$a', 'An argument.'),
        ],
        syntax='$f($a)',
        side_effect='None',
        raises=[
            ('ValueError', 'If $a is invalid.'),
        ],
        returns='True if $a is valid, False otherwise.',
    )
    assert actual == expected



# Generated at 2022-06-13 19:50:16.235774
# Unit test for function parse
def test_parse():
    """Test Parse"""
    text = '''
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    """
    '''

    o = parse(text)
    assert o.meta['summary'] == 'Summary line.'

    params = o.meta['params']
    assert len(params) == 2
    assert params['arg1'].arg_type == 'int'
    assert params['arg1'].description == 'Description of arg1'
    assert params['arg2'].arg_type == 'str'
    assert params['arg2'].description == 'Description of arg2'

    returns = o.meta['returns']

# Generated at 2022-06-13 19:50:17.032125
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:50:28.760311
# Unit test for function parse
def test_parse():
    text = '''
    One line summary.

    Extended description.

    Parameters
    ----------
    filename : str
        Path to the input file.
    format : {'abs', 'log'}, optional
        Format to return the data in.
    '''

    parsed = parse(text)
    assert len(parsed.sections) == 2
    assert parsed.args == ['filename', 'format']
    assert parsed.kwargs == {'filename': 'str', 'format': "{'abs', 'log'}"}

    text = '''
    Scikit-learn tools for decision trees.

    These tools support the decision tree algorithms.
    '''

    parsed = parse(text)
    assert len(parsed.sections) == 0
    assert parsed.args == []
    assert parsed.kwargs == {}


# Generated at 2022-06-13 19:50:40.319874
# Unit test for function parse
def test_parse():
    assert repr(parse("Hello docstring")) == repr(
        Docstring(
            content="Hello docstring", meta={}, description="Hello docstring",
            extras=[]
        )
    )
    assert repr(parse("Hello docstring\n\nHello meta")) == repr(
        Docstring(
            content="Hello docstring",
            meta={'Hello': 'meta'},
            description="Hello docstring",
            extras=[]
        )
    )
    assert repr(parse("Hello docstring\n\nHello meta\n\nHello extras")) == repr(
        Docstring(
            content="Hello docstring",
            meta={'Hello': 'meta'},
            description="Hello docstring",
            extras=['Hello extras']
        )
    )

# Generated at 2022-06-13 19:50:44.296718
# Unit test for function parse
def test_parse():
    try:
        parse_ = parse(text="", style=Style.auto)
    except ParseError as e:
        print(e)

# Generated at 2022-06-13 19:50:45.808622
# Unit test for function parse
def test_parse():
    text = 'The main parsing routine.'
    parse(text)


# Generated at 2022-06-13 19:50:50.267993
# Unit test for function parse
def test_parse():
    """Test parse method"""
    text = '''\
    """
    The function is for doctest
    :param test: not used
    """
    '''
    result = parse(text)
    assert result.description == 'The function is for doctest'
    assert result.params['test'].description == 'not used'
    assert result.params['test'].type_name is None
    assert result.params['test'].name == 'test'

# Generated at 2022-06-13 19:50:56.690774
# Unit test for function parse
def test_parse():
    # sample function docstring used for testing
    sample_docstring = r'''
        summary
        ---------
        sample function
        Parameters
        ----------
        var_a : int
            the first parameter of type int
        var_b : string
            the second parameter of type string
        var_c : np.array
            the third parameter of type numpy array
        Returns
        -------
        int
            the return value of this function
    '''
    parsed_data = parse(sample_docstring)
    print(parsed_data)


# Generated at 2022-06-13 19:51:01.551803
# Unit test for function parse
def test_parse():
    text = """
    :param a: A parameter
    :param b: Another parameter
    :returns: Returns
    """
    doc = parse(text)
    assert doc.params == {'a': 'A parameter', 'b': 'Another parameter'}


# Generated at 2022-06-13 19:51:04.642441
# Unit test for function parse
def test_parse():
    try:
        d = parse("This is a test")
        assert d.short_description == "This is a test\n"
    except:
        assert False

# Generated at 2022-06-13 19:51:14.852500
# Unit test for function parse
def test_parse():
    text = """A one-liner summary ending in a dot.

    A multi-line description.  This may
    span multiple lines.

    Note that this is parsed properly.

    Parameters
    ----------
    arg1 : int, float
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    str
        Description of return value

    Raises
    ------
    ImportError
        If the module is not installed

    Other Parameters
    ----------------
    optional : str
        Description of optional parameter
    """
    doc = parse(text, style=Style.numpy)
    print(doc.short_description)
    print(doc.long_description)
    print(doc.sections)
    print(doc.style)
    print(doc.meta)
    
    


# test_parse()
