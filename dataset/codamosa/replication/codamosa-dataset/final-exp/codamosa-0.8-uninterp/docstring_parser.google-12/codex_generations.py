

# Generated at 2022-06-13 19:31:18.837586
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Case 1: first line only
    docstring = 'This is a test, i.e., a test test'
    docstring_object = GoogleParser().parse(docstring)
    assert docstring_object.short_description == 'This is a test, i.e., a test test'
    assert docstring_object.long_description is None
    assert docstring_object.blank_after_short_description is None
    assert docstring_object.blank_after_long_description is None
    assert not docstring_object.meta

    # Case 2: first line + one line description
    docstring = 'This is a test, i.e., a test test\nThis is a description of the method.'
    docstring_object = GoogleParser().parse(docstring)

# Generated at 2022-06-13 19:31:28.724991
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  text = '''Arguments
  ----------
  a : int
      A. Defaults to 3.
  b : str
      B.
  c : str, optional
      C.
  d : str?, optional
      D.
  e : str
      E.
      E.
  f
    F.

Raises
------
  ValueError
      On no data.
  IndexError
      On broken data.

Returns
-------
  int
  str'''
  print('Test GoogleParser_parse function:')
  google_parser = GoogleParser()
  print(google_parser.parse(text))


# Generated at 2022-06-13 19:31:34.579392
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_docstr = """
        This is the first line of the docstring.
        Followed by the second line,
        which is wrapped after the first line.
    """
    import re
    text = inspect.cleandoc(google_docstr)
    # clean docstring
    ret = Docstring()
    ret.short_description = inspect.getdoc(GoogleParser).split('\n')[0]
    # first and second line of docstring
    ret.long_description = inspect.cleandoc(google_docstr)
    # Google-style docstring
    # ret.blank_after_short_description = True
    assert re.match(ret.short_description, google_docstr)


# Generated at 2022-06-13 19:31:37.739031
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    assert p.parse("") == Docstring()


# Generated at 2022-06-13 19:31:50.372519
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #test case 1
    doc_string_obj = GoogleParser()
    text = """Computes the loss of a convolution operation.
    Args:
      conv_output: tensor, output of the convolution.
      target: tensor, the target output values.
      num_classes: the number of classes.
      head_index: index of the head.
      class_weights: tensor, containing the weights for each class.
    Returns:
      loss: scalar, the computed loss entry.
    """
    obj = doc_string_obj.parse(text)
    assert obj.short_description == "Computes the loss of a convolution operation."
    assert obj.blank_after_short_description == True
    assert obj.blank_after_long_description == True

# Generated at 2022-06-13 19:32:05.213538
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Create test data
    text = """Brief summary.

           Extended summary.

           Returns:
               Returns nothing.

           Yields:
               Yields something.

           Raises:
               KeyError: An exception.
               ValueError: Another exception.

           Examples:
               Example usage.
               >>> f(1)
               1
               >>> f(2)
               5
    """
    result = parse(text)

    # Test
    assert result.short_description == "Brief summary."
    assert result.long_description == "Extended summary."
    assert result.blank_after_short_description
    assert result.blank_after_long_description
    assert isinstance(result.meta[0], DocstringReturns)
    assert result.meta[0].description == "Returns nothing."

# Generated at 2022-06-13 19:32:09.430377
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    import string
    from random import choice
    for _ in range(1000):
        s = [choice(string.ascii_letters + " \n") for _ in range(100)]
        text = "".join(s)
        assert str(GoogleParser().parse(text)) == str(parse(text))

# Generated at 2022-06-13 19:32:18.698501
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    foo_docstring = """
        Foo function.

        Parameters
        ----------
        a: int, optional
            An integer.
        b: float, optional
            A float.

        Returns
        -------
        None
    """
    d = GoogleParser().parse(foo_docstring)
    assert d.short_description == "Foo function."
    assert d.long_description == ""
    assert d.meta[0].description == "None"
    assert d.meta[1].description == "An integer."
    assert d.meta[1].arg_name == "a"
    assert d.meta[1].is_optional == True
    assert d.meta[1].type_name == "int"
    assert d.meta[2].description == "A float."
    assert d.meta[2].arg_name == "b"

# Generated at 2022-06-13 19:32:33.439407
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse(
        """
    This function does something.

    Args:
        arg1: The first argument.
        arg2: The second argument.
    Returns:
        The return value. True for success, False otherwise.
    Raises:
        AttributeError, KeyError
    """
    )
    assert docstring.short_description == "This function does something."
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 6
    assert docstring.meta[0].args == ["returns", "The return value. True for success, False otherwise."]
    assert docstring.meta[0].is_generator is False


# Generated at 2022-06-13 19:32:44.681637
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    example = """
    This is a test.
    Blah blah blah.
    blah blah blah

    Args:
        haha: a test 

    Returns:
        Return a test.
    
    Raises:
        Error.
    """

    # run method parse
    parsed = GoogleParser().parse(example)

    # expected result
    expected_short_description = 'This is a test.'
    expected_long_description = 'Blah blah blah.\nblah blah blah'
    expected_blank_after_short_description = True
    expected_blank_after_long_description = False

# Generated at 2022-06-13 19:33:04.931674
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    assert parse("""
    Short description.
    """) == Docstring(
        short_description="Short description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description=None,
        meta=[
            DocstringMeta(
                args=[],
                description=None
            )
        ]
    )
    assert parse("""
    Short description.

    Long description.
    """) == Docstring(
        short_description="Short description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="Long description.",
        meta=[
            DocstringMeta(
                args=[],
                description=None
            )
        ]
    )

# Generated at 2022-06-13 19:33:16.464126
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:33:23.511296
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """GoogleParser's parse method should return Docstring for doc strings in Google Style."""
    assert isinstance(
        parse(
            """
    Short summary.

    Long description.

    Args:
        text: Test string to parse.

    Returns:
        Parsed docstring.
        """
        ),
        Docstring,
    )

    # Test group of DocstringParam
    assert isinstance(
        parse(
            """
    Short summary.

    Long description.

    Args:
        text: Test string to parse.
        """
        ),
        Docstring,
    )

    # Test optional param

# Generated at 2022-06-13 19:33:30.465426
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:33:37.594345
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ds = '''Calculate sum of numbers
    :param a: File name
    :param b: Current line number (start from 1)
    :type a: Integer
    :type b: Integer, optional
    :returns: sum of a and b
    :rtype: Integer
    :raises ValueError: if a or b is invalid
    '''
    parser = GoogleParser()
    parsed = parser.parse(ds)
    assert parsed.short_description == 'Calculate sum of numbers'
    assert parsed.long_description is None
    assert parsed.meta[0].args == ['param', 'a: File name']
    assert parsed.meta[1].args == ['param', 'b: Current line number (start from 1)']
    assert parsed.meta[2].args == ['type', 'a']
    assert parsed.meta

# Generated at 2022-06-13 19:33:49.567825
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    '''
        Test the GoogleParser() parse() method
    '''
    f = GoogleParser()
    # (expected, input)

# Generated at 2022-06-13 19:33:58.477481
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    dummy_text = """
    Short description.

    Long description.
    Even longer description.

    Args:
        arg1 (str): Description for argument 1.
        arg2 (str, optional): Description for argument 2.
    """
    docstring = GoogleParser().parse(dummy_text)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description.\nEven longer description."
    assert docstring.meta[0].description == "Description for argument 1."
    assert docstring.meta[1].description == "Description for argument 2."
    assert docstring.meta[1].is_optional == True

# Generated at 2022-06-13 19:34:09.594700
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse('') == Docstring()
    assert parse('A') == Docstring(
        short_description='A',
        blank_after_short_description=True,
    )
    assert parse('A\n\nB') == Docstring(
        short_description='A',
        blank_after_short_description=True,
        long_description='B',
        blank_after_long_description=True,
    )
    assert parse('A\n\nB\n\n') == Docstring(
        short_description='A',
        blank_after_short_description=True,
        long_description='B',
        blank_after_long_description=True,
    )

# Generated at 2022-06-13 19:34:20.790003
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    GoogleParser().parse(text=None)
    GoogleParser().parse(text="")

    p = GoogleParser()
    p.add_section(Section(title="Test", key="test", type=SectionType.SINGULAR))
    p.parse("This is a test.")
    p.parse("Test: This is a test.")
    p.parse("Test: This is a test. With more stuff.")
    with pytest.raises(ParseError):
        p.parse("Test:")
    with pytest.raises(ParseError):
        p.parse("Test")

    p = GoogleParser()
    p.add_section(Section(title="Test", key="test", type=SectionType.MULTIPLE))
    p.parse("This is a test.")
    p.parse("Test: This is a test.")
   

# Generated at 2022-06-13 19:34:28.075671
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:40.901935
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = inspect.cleandoc(
        """
        Short description
        Some more description.

        Args:
            arg1 (str): This is the first argument.
            arg2 (str): This is the second argument.
            arg3 (str): This is the third argument.
        """
    )
    instance = GoogleParser()
    result = instance.parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 3
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args == ['param', 'arg1']
    assert result.meta[0].arg_name == 'arg1'
    assert result.meta[0].description == 'This is the first argument.'
    assert result.meta[0].type_name == 'str'

# Generated at 2022-06-13 19:34:43.976137
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    a = parser.parse("""
    Test whether the network is connected.
    Returns \\*True\\* if the network is connected
    """)
    if a.long_description != None:
        print("pass")


test_GoogleParser_parse()

# Generated at 2022-06-13 19:34:53.674508
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    t = """
    Class for creating pykitti.

        :param base_path: The path where raw data is located
        :param date: The date as string YYYY-MM-DD
        :param drive: The drive as string, e.g. '0027'
        :param frames: List of frames to load
        :param loaded_calib: Loaded calibration data
        :param cached_calib: Cache calibration data?
        :param imformat: The file format to read images
    """
    t2 = """
    Module for reading velodyne [1]_ binary files.
    """
    t3 = """
    This is an example class.

        :param param1: this is a first param
        :param param2: a second param
        :raises keyError: raises an exception
    """

# Generated at 2022-06-13 19:35:08.449530
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Test all return types
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("one line") == Docstring('one line')
    assert \
        GoogleParser().parse("one line\nnext line") \
        == Docstring('one line', False, 'next line', False, None)
    assert \
        GoogleParser().parse("one line\n\nnext line") \
        == Docstring('one line', True, 'next line', False, None)
    assert \
        GoogleParser().parse("one line\nnext line\n") \
        == Docstring('one line', False, 'next line', False, None)
    assert \
        GoogleParser().parse("one line\n\nnext line\n") \
        == Docstring('one line', True, 'next line', False, None)
   

# Generated at 2022-06-13 19:35:17.182136
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    assert parse('') == Docstring()

    text = '''
    1. short description
    2. short description with 'quote'

    Long description.
    Long description.
    '''
    assert parse(text) == Docstring(
        short_description='1. short description',
        blank_after_short_description=False,
        long_description='Long description.\nLong description.',
        blank_after_long_description=False,
        meta=[DocstringMeta(
            args=[''],
            description='2. short description with \'quote\'')]
    )


# Generated at 2022-06-13 19:35:27.338216
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '''
    Test parsing Google-style docstrings.

    This is the long description.
    
    Args:
        arg1 (int): The first number.
        arg2 (int): The second number.

    Returns:
        int: The return value.
    '''

    parsed_docstring = GoogleParser().parse(docstring)

    assert parsed_docstring.short_description == 'Test parsing Google-style docstrings.'
    assert parsed_docstring.long_description == 'This is the long description.'
    assert parsed_docstring.meta[0].args == ['returns', 'int']
    assert parsed_docstring.meta[0].description == 'The return value.'
    assert parsed_docstring.meta[1].args == ['param', 'arg1 (int)']

# Generated at 2022-06-13 19:35:32.424427
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''Args:
    output_directory (str): Output folder
    '''


# Generated at 2022-06-13 19:35:39.217306
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test for parsing simple case
    input_text = "Example of parse(text) method used for unit testing"
    docstring_object = GoogleParser().parse(input_text)
    assert docstring_object.short_description == "Example of parse(text) method used for unit testing"
    assert docstring_object.long_description == None
    assert docstring_object.blank_after_short_description == None
    assert docstring_object.blank_after_long_description == None
    assert len(docstring_object.meta) == 0

    # Test for parsing docstring with short description
    input_text = "Parse Google-style docstring into its components.\n\nThis is a long description."
    docstring_object = GoogleParser().parse(input_text)

# Generated at 2022-06-13 19:35:44.094256
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:35:55.154704
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("hello") == Docstring(
        short_description="hello",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )
    assert GoogleParser().parse("hello\n") == Docstring(
        short_description="hello",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description=None,
        meta=[],
    )
    assert GoogleParser().parse("hello\n\n") == Docstring(
        short_description="hello",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=True,
        meta=[],
    )

# Generated at 2022-06-13 19:36:02.989287
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("""
        Short description.

        Long description.

        :param arg:
        :type arg: str
        :returns: some type
        :rtype: int
    """).short_description == "Short description."


# Generated at 2022-06-13 19:36:12.939754
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Obtain docstring from __doc__ attribute
    ds = parse.__doc__

    # Instantiate GoogleParser
    parser = GoogleParser()

    # Parse and obtain Docstring object
    Docstring = parser.parse(ds)

    # Expected arguments of parse
    exp_args = ['text']

    # Expected arg_name of parse
    exp_arg_name = 'text'

    # Expected description of parse
    exp_description = (
        'Parse the Google-style docstring into its components.\n\n'
        ':returns: parsed docstring'
    )

    # Expected key of parse
    exp_key = 'returns'

    # Expected short_description of parse
    exp_short_description = 'Parse the Google-style docstring into its components.'

    # Expected blank_

# Generated at 2022-06-13 19:36:16.119961
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    source = '''
    This function does something.

    Args:
        param1
    '''
    parsed = parse(source)
    print(parsed)


# Generated at 2022-06-13 19:36:26.012843
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print('Testing method parse of class GoogleParser')
    p = GoogleParser()

# Generated at 2022-06-13 19:36:37.440495
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse('docstring') == Docstring(short_description='docstring')
    assert parse('') == Docstring()

    assert parse('docstring\n\n') == Docstring(short_description='docstring')
    assert parse('docstring\n') == Docstring(short_description='docstring')
    assert parse('docstring\n\n ') == Docstring(short_description='docstring')
    assert parse('docstring\n   extra') == Docstring(
        short_description='docstring',
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description='extra'
    )

# Generated at 2022-06-13 19:36:45.860545
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # I have to test these because GoogleParser() is the main object used
    # in `yapf`.
    google_parser = GoogleParser()
    # Test with a docstring that doesn't contain a title before the
    # description
    docstring_without_title = "This is a docstring."
    docstring = google_parser.parse(docstring_without_title)
    assert(docstring.short_description == docstring_without_title)
    assert(docstring.long_description == None)
    assert(docstring.blank_after_short_description == False)
    assert(docstring.blank_after_long_description == False)

    # Test with a docstring that contains a title before the description
    docstring_with_title = "Args:\n  arg_name: something\n"

# Generated at 2022-06-13 19:36:58.743669
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_docstring_sample = """
    Tests if a given number is prime or not.

    We are testing if the given number is prime or not. 

    Params
    ----------
    n : int
        A positive integer number.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
        Note that 'True' and 'False' capitalization is important.
    """
    parsed_docstring = GoogleParser().parse(google_docstring_sample)
    assert parsed_docstring.short_description == "Tests if a given number is prime or not."
    assert parsed_docstring.meta[0].description == "A positive integer number."
    assert parsed_docstring.meta[0].arg_name == "n"
    assert parsed_docstring.meta[0].type_name == "int"
   

# Generated at 2022-06-13 19:37:03.389372
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_method():
        """Test method that has parameters.

        Example:
            >>> test_method(1)

        Example:
            >>> test_method("arg")

        Args:
            arg1: argument 1
            arg2: argument 2 (int, optional)

        Returns:
            description of return
            value.

        Raises:
            ValueError: if something wrong.
            TypeError: if something else wrong.
        """

    text = test_method.__doc__
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == "Test method that has parameters."
    assert docstring.long_description == "Example:\n    >>> test_method(1)\n\nExample:\n    >>> test_method(\"arg\")"

# Generated at 2022-06-13 19:37:09.378245
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''
    Summarize the Router class here.

    This is a long description.

    Attributes:
        attr1: The first attribute.
        attr2: The second attribute.
    '''
    print(GoogleParser().parse(doc))


if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:37:10.316727
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass


# Generated at 2022-06-13 19:37:28.092373
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """\
    This is a summary.

    This is a long description.

    Args:
        param1 (str): Description of `param1`

    Returns:
        bool: Description of return value

    Raises:
        AttributeError: The error raised when `param2` is not found.
        ValueError: The error raised when `param2` is of the wrong type.
    """
    long_description = """\
    This is a long description.
    """

# Generated at 2022-06-13 19:37:35.646873
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_function(a, b=None):
        """Test function.

        :param a: argument
        :param b: another argument
        :type b: bool
        :returns: returns
        :rtype: str
        :raises IndexError: raises
        """
        pass


# Generated at 2022-06-13 19:37:40.881416
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test case 1
    test_1_input_text = """\
    This is the Google-style docstring for a function.

    This is the first line of the first paragraph.

    This is the second line of the first paragraph.

    This is the first line of the second paragraph.

    This is the second line of the second paragraph.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        str: The return value. True for success, False otherwise.
    """

# Generated at 2022-06-13 19:37:50.565288
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''Classe de test
        :param nome: Nome de teste
        :type nome: string
        :param idade: Idade de teste
        :type idade: int
    '''

    ret = GoogleParser().parse(doc)
    #print(ret)

    #assert ret.short_description == 'Classe de test'
    assert(ret.short_description == 'Classe de test')
    #assert ret.long_description == ''
    assert(ret.long_description is None)
    #assert ret.blank_after_short_description == True
    assert(ret.blank_after_short_description)
    #assert ret.blank_after_long_description == True
    assert(ret.blank_after_long_description)

    #assert len(ret.meta) == 5

# Generated at 2022-06-13 19:37:57.767387
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import pytest
    text_1 = '''
    first line - short description
    second line - short description.

    first line - long description
    second line - long description
    '''
    # pytest.set_trace()
    parse(text_1)
    text_2 = '''
    first line - short description

    first line - long description
    second line - long description
    '''
    parse(text_2)



# Generated at 2022-06-13 19:38:04.683410
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    good_doc_inputs = [
        """
        Method summary

        Parameters
        ----------
        arg1 : str
            Description of `arg1` (with type).
        arg2 : int, optional
            Description of `arg2` (with type and explicitly optional).
        arg3 : int, optional
            Description of `arg3` (with type and explicitly optional).

        Returns
        -------
        str
            Description of return value.
        """
    ]
    # TODO(alvargz, 2020-06-06): Test all the other use cases.

# Generated at 2022-06-13 19:38:10.640574
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Unit test for method parse of class GoogleParser
    """
    test_string = """
    The adder.

    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
        c (int): The third number to be added.

    Returns:
        int: The result of adding the first and second numbers.
    """

    result = GoogleParser().parse(test_string)
    print("result:", result)
    assert (
        result.short_description
        == "The adder."
        == result.long_description
        != result.meta[0].description
        != result.meta[1].description
        != result.meta[2].description
        != result.meta[3].description
    )

# Generated at 2022-06-13 19:38:15.244688
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Xyz
    Xyz is something.
    Args:
    x [int] - Description for x
    y [str] - Description for y. Defaults to 'default'.
    z [int] - Description for z
    Raises:
    TypeError - Description
    ZeroDivisionError - Description
    Example:
    Exmaple explanation
    """
    doc = GoogleParser().parse(docstring)
    print(doc.short_description)
    print(doc.long_description)
    print(doc.blank_after_short_description)
    print(doc.blank_after_long_description)
    for item in doc.meta:
        if type(item) is DocstringParam:
            print(item.arg_name)
            print(item.description)
            print(item.type_name)
           

# Generated at 2022-06-13 19:38:25.795085
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    This is a test of the emergency broadcast system.

    Arguments:
      param1 (str): This is the first parameter.
      param2 (str): This is the second parameter.

    Returns:
      str: This is a string that is returned.



    Raises:
      ValueError: If `param2` is equal to `param1`.
      TypeError: If `param1` is not a string.

    """
    result = GoogleParser().parse(text)
    assert result.short_description == "This is a test of the emergency broadcast system."
    assert result.long_description is None
    assert result.blank_after_short_description
    assert result.blank_after_long_description
    assert result.meta[0].args[0] == "param1"

# Generated at 2022-06-13 19:38:38.849453
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser."""

# Generated at 2022-06-13 19:38:48.350063
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = """Single-line summary.

    Extended description.

    Args:
        arg1: The first argument.
        arg2: The second argument.
    """

    parser = GoogleParser()
    ret = parser.parse(doc)
    assert ret.short_description == "Single-line summary."
    assert ret.long_description == "Extended description."
    assert len(ret.meta) == 2
    assert ret.meta[0].args[0] == 'param'
    assert ret.meta[0].args[1] == 'arg1'
    assert ret.meta[0].description == 'The first argument.'
    assert ret.meta[0].arg_name == 'arg1'
    assert ret.meta[1].args[0] == 'param'

# Generated at 2022-06-13 19:38:58.152431
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:08.953013
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Title

    Short description

    Long description

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert len(docstring.meta) == 2
    assert type(docstring.meta[0]) == DocstringParam
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[0].is_optional == False
    assert docstring.meta[0].description == "The first argument."

# Generated at 2022-06-13 19:39:15.521921
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Summary line.
    
    Extended description.
    
    Parameters
    ----------
    arg1 : str
        Description of arg1
    arg2 : List[int]
        Description of arg2
    
    Returns
    -------
    str
        Description of return value.
    
    """
    parsed = parse(docstring)

    assert parsed.short_description == "Summary line."
    assert parsed.long_description == "Extended description."
    assert parsed.blank_after_short_description
    assert parsed.blank_after_long_description

    assert isinstance(parsed.meta[0],DocstringParam)
    assert isinstance(parsed.meta[1],DocstringParam)
    assert isinstance(parsed.meta[2],DocstringReturns)


# Generated at 2022-06-13 19:39:24.029507
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    gp = GoogleParser()

    # Test case 1: Title: Parameters
    text = '''Single line description.
    Parameters:
        param1 (str): The first parameter.
        param2 (str): The second parameter.Defaults to None.
    Example:
        Usage of param1 and param2.
    '''
    ds = gp.parse(text)
    assert len(ds.meta) == 3
    assert ds.meta[0].args == ['param', 'param1 (str)']
    assert ds.meta[0].description == 'The first parameter.'
    assert ds.meta[0].arg_name == 'param1'
    assert ds.meta[0].type_name == 'str'
    assert ds.meta[0].is_optional == False
    assert ds.meta[0].default == None

# Generated at 2022-06-13 19:39:32.367145
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("GoogleParser_parse: Running unit test for method parse")
    doc = "/**\n"
    doc += "Arithmetic functions.\n"
    doc += "\n"
    doc += "This module provides functions for multiplication and addition.\n"
    doc += "\n"
    doc += "Args:\n"
    doc += "    x(int): The first value.\n"
    doc += "    y(int): The second value.\n"
    doc += "    z(int): The third value.\n"
    doc += "\n"
    doc += "Returns:\n"
    doc += "    float: The result of the operation.\n"
    doc += "\n"
    doc += "Raises:\n"

# Generated at 2022-06-13 19:39:42.673022
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
        """
    rt = GoogleParser().parse(text)
    assert rt.short_description is None
    assert rt.long_description is None

    text = """\
        This is a good example::

            print(hello.world)
        """
    rt = GoogleParser().parse(text)
    assert rt.short_description == "This is a good example"
    assert rt.long_description == "print(hello.world)"

    text = """\
        This is a good example::

            print(hello.world)

        """
    rt = GoogleParser().parse(text)
    assert rt.short_description == "This is a good example"
    assert rt.long_description == "print(hello.world)"


# Generated at 2022-06-13 19:39:47.848988
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_text = "    Args:\n        param1:  The first parameter.\n        param2:  The second parameter.\n    \n    Returns:\n        The return value. True for success, False otherwise.\n    "
    docstring = GoogleParser().parse(docstring_text)
    print(docstring.short_description)
    print(docstring.long_description)
    print(docstring.blank_after_short_description)
    print(docstring.blank_after_long_description)

    # Test if docstring meta info can be retrieved successfully
    for meta in docstring.meta:
        print(meta.args)
        print(meta.description)
        print(meta.arg_name)
        print(meta.type_name)
        print(type(meta.is_optional))

# Generated at 2022-06-13 19:39:58.812716
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_short_description = """
    Some google-style docstring.

    It contains a long description which is the second line.
    """
    doc_short_description += '\n' * 3

    doc_long_description = """
    Some google-style docstring.
    """
    doc_long_description += '\n' * 3
    doc_long_description += """
    It contains a long description which is the second line.
    """
    doc_long_description += '\n\n'

    doc_short_description_no_newline = (
        """Some google-style docstring.

    It contains a long description which is the second line.
    """
    )
    doc_short_description_no_newline += '\n' * 3


# Generated at 2022-06-13 19:40:02.694109
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ds = '''
    Method for getting some data.

    Long description.

    Arguments:
        arg1 (int): first argument.
        arg2 (int, optional): second argument. Defaults to 10.

    Returns:
        str: Some string.

    Raises:
        ValueError: If something goes wrong.

    '''
    s = GoogleParser()
    res = s.parse(ds)
    print(res)
    pass

# Generated at 2022-06-13 19:40:10.972211
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    parser = GoogleParser()

    # test case 1
    text = '"""\nParse the Google-style docstring into its components.\n\n:returns: parsed docstring\n"""\n'
    res = parser.parse(text)
    print("Docstring.parse:", res)

    # test case 2
    text = '"""\nParse the Google-style docstring into its components.\n\nArgs:\n    text: docstring to parse\n\nReturns:\n    parsed docstring\n"""\n'
    res = parser.parse(text)
    print("Docstring.parse:", res)


# Generated at 2022-06-13 19:40:18.710249
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = r'''
        This is an example.

        Parameters
        ----------
        arg1 : int
            Description of `arg1`.
        arg2 : str
            Description of `arg2` with a continuation line.
        arg3 : float
            Description of `arg3`.
            Defaults to 2.5.
        arg4 : list[float]
            Description of `arg4`.

        Raises
        ------
        RuntimeError
            If things go wrong.

        Returns
        -------
        int
            The return value.

        Yields
        -------
        int
            The yielded value.

        Examples
        --------
        >>> print('Hello world!')
        Hello world!
    '''
    parsed = GoogleParser().parse(text)
    assert parsed.short_description == "This is an example."
    assert parsed.long

# Generated at 2022-06-13 19:40:27.379552
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	GoogleParser_parse = GoogleParser().parse

# Generated at 2022-06-13 19:40:37.849655
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
        Google-style docstring parsing.

        :param sections: Recognized sections or None to defaults.
        :param title_colon: require colon after section title.

        Args:
            sections (list): Recognized sections or None to defaults.
            title_colon (bool): require colon after section title.

        Parameters:
            sections (list): Recognized sections or None to defaults.
            title_colon (bool): require colon after section title.

        Returns:
            Docstring: parsed docstring
    """
    ds = GoogleParser().parse(text)

    print(ds.short_description)
    print(ds.long_description)
    print(ds.blank_after_short_description)
    print(ds.blank_after_long_description)

# Generated at 2022-06-13 19:40:43.552896
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # a sample docstring
    text = '''
    This is a sample docstring.

    This is the long description. It can have multiple lines.

    Args:
        arg1: The first argument.
        arg2: The second argument. Defaults to None.

    Returns:
        The return description. 
    '''
    parser = GoogleParser()
    doc = parser.parse(text)
    assert doc.short_description == 'This is a sample docstring.'
    assert doc.long_description == 'This is the long description. It can have multiple lines.'
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True
    assert len(doc.meta) == 2
    assert doc.meta[0].args == ['param', 'arg1: The first argument.']

# Generated at 2022-06-13 19:40:50.217505
# Unit test for method parse of class GoogleParser