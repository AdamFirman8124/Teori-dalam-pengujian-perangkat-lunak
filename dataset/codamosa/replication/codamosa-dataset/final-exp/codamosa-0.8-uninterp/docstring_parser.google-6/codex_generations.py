

# Generated at 2022-06-13 19:31:30.950118
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Summary line.
        
        Extended description.
        
        Parameters
        ----------
        arg1 : int
            Description of `arg1`
        arg2 : str
            Description of `arg2`
        Returns
        -------
        str
            Description of return value
        """

# Generated at 2022-06-13 19:31:42.504275
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #
    # Setup
    #
    parser = GoogleParser()
    
    test_string = """Arguments:
    arg1 (int): description of arg1.
    arg2 (float): description of arg2. Defaults to 0.5.
    arg3 (str): description of arg3. Defaults to 'foo'.
    
"""

    #
    # Test body
    #
    doc_string = parser.parse(test_string)
    #
    # Test result
    #
    assert doc_string.short_description is None
    assert doc_string.blank_after_short_description is False
    assert doc_string.long_description is None
    assert doc_string.blank_after_long_description is False
    assert doc_string.meta[0].args == ["param", "arg1 (int)"]

# Generated at 2022-06-13 19:31:48.728981
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    parser = GoogleParser()

    text = '''
    This function does something.

    Args:
        arg1: The first argument.
        arg2: The second argument.

    Returns
        int: The return value.
    '''

    docstring = parser.parse(text)
    assert len(docstring.meta) == 3
    assert docstring.meta[0].description == 'The first argument.'
    assert docstring.meta[0].arg_name == 'arg1'
    assert docstring.meta[1].description == 'The second argument.'
    assert docstring.meta[1].arg_name == 'arg2'
    assert docstring.meta[2].description == 'The return value.'
    assert docstring.meta[2].type_name == 'int'

# Generated at 2022-06-13 19:31:53.235391
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Quick sort algorithm.

    Parameters:
      arr: The list to sort.
      left: The left index. Defaults to 0.
      right: The right index. Defaults to the length of the list - 1.

    Returns:
      A sorted list.

    """
    expect = 'Quick sort algorithm.'
    results = GoogleParser().parse(text)
    assert(expect == results.short_description)

    # test long description
    expect = 'The list to sort. The left index. Defaults to 0. The right index. Defaults to the length of the list - 1.'
    results = GoogleParser().parse(text)
    assert(expect == results.long_description)

    # test meta
    expect = ['Returns:', 'A sorted list.']
    results = GoogleParser().parse(text)

# Generated at 2022-06-13 19:32:07.038828
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """A method that takes an argument.
    This method does some stuff.
    Args:
        arg1: the first argument. Defaults to 10.

    Returns:
        something
    """
    parser = GoogleParser()
    parsed_docstring = parser.parse(docstring)
    print(parsed_docstring)

    docstring = """A method that takes an argument.
    This method does some stuff.
    Args:
        arg1: The first argument. Defaults to 10.

    Returns:
        something
    """
    parser = GoogleParser()
    parsed_docstring = parser.parse(docstring)
    print(parsed_docstring)


# Generated at 2022-06-13 19:32:16.917398
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("asd") == Docstring(
        short_description="asd", long_description=None, meta=[]
    )
    # Single element sections
    assert GoogleParser().parse(".. example::\nasd\n") == Docstring(
        short_description="",
        long_description=None,
        meta=[DocstringMeta(args=["example"], description="asd")],
    )

# Generated at 2022-06-13 19:32:25.625661
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    goop = GoogleParser()
    docstring = """
    Computes the Levenshtein distance between sequences.
    This method has not been modified from the original.
    Source can be found at http://mwh.geek.nz/2009/04/26/python-damerau-levenshtein-distance/
    """
    docstring = inspect.cleandoc(docstring)
    assert goop.parse(docstring).__repr__() == """{
        'short_description': 'Computes the Levenshtein distance between sequences.',
        'long_description': 'This method has not been modified from the original.',
        'blank_after_short_description': False,
        'blank_after_long_description': False,
        'meta': []
    }"""

# Generated at 2022-06-13 19:32:38.610125
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Call parse with a simple docstring
    assert(GoogleParser().parse("Method that does nothing.") == Docstring(
        short_description=None,
        long_description="Method that does nothing.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[]
    ))

    # Call parse with a docstring that has a blank line between the short description and the long description
    assert(GoogleParser().parse("Method that does nothing.\n\nThis is the long description.") == Docstring(
        short_description=None,
        long_description="This is the long description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[]
    ))

    # Call parse with a docstring that has a blank line after the long description


# Generated at 2022-06-13 19:32:48.295058
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("Test docstring") == Docstring(
        short_description="Test docstring",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description=None,
        meta=[],
    )
    assert parse("Test docstring\n") == Docstring(
        short_description="Test docstring",
        blank_after_short_description=False,
        blank_after_long_description=True,
        long_description=None,
        meta=[],
    )
    assert parse("Test docstring\n\n") == Docstring(
        short_description="Test docstring",
        blank_after_short_description=False,
        blank_after_long_description=True,
        long_description=None,
        meta=[],
    )

# Generated at 2022-06-13 19:32:55.938886
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:33:14.854191
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    # Short description
    docstring_text = "This is a short description."
    docstring = parser.parse(docstring_text)
    assert docstring.short_description == "This is a short description."
    # Short description, long description, blank after short description, blank after long description
    docstring_text = "This is a short description.\n\nThis is a longer description."
    docstring = parser.parse(docstring_text)
    assert docstring.short_description == "This is a short description."
    assert docstring.long_description == "This is a longer description."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    # Short description, long description, blank after short description, no blank after long description
    docstring

# Generated at 2022-06-13 19:33:24.475421
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # test_parse_returns_None
    parser = GoogleParser()
    text = None
    assert parser.parse(text) == Docstring()

    # test_parse_returns_empty_Docstring
    parser = GoogleParser()
    text = ''
    assert parser.parse(text) == Docstring()

    # test_parse_returns_Docstring_with_blank_short_description
    parser = GoogleParser()
    text = '''\
    '''
    assert parser.parse(text) == Docstring()

    # test_parse_returns_Docstring_with_blank_long_description
    parser = GoogleParser()
    text = '''\
    Description


    '''

# Generated at 2022-06-13 19:33:31.846536
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = GoogleParser().parse("""Hello world.
    This is a sentence.
    Attributes:
        foo: bar
        baz: blah
    Raises:
        OSError: An error occurred accessing the bigtable."""
)
# Tests if the method correctly generates a Docstring for an input string.
    assert doc.short_description == "Hello world."
    assert doc.long_description == "This is a sentence."
    assert [meta.args for meta in doc.meta] == [
        ['attribute', 'foo'],
        ['attribute', 'baz'],
        ['raises', 'OSError'],
    ]

# Generated at 2022-06-13 19:33:38.684503
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    googleParser = GoogleParser()
    sample_google_docstring1 = '''This module will do something.
        
    Args:
        arg1: get it 1
        arg2: get it 2
        
    Raises:
        a: exception1
        b: exception2
        
    Returns:
        x: anything
    '''
    element1 = googleParser.parse(sample_google_docstring1)
    
    sample_google_docstring2 = '''This module will do something.
        
    Args:
        arg1: get it 1
        arg2: get it 2
        
    Raises:
        a: exception1
        b: exception2
        
    Returns:
        x: anything
        y: anything
        z: anything
    '''

# Generated at 2022-06-13 19:33:39.967571
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert 1==1

# Generated at 2022-06-13 19:33:52.203178
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test case 1: no docstring
    text = ""
    ret = GoogleParser().parse(text)
    expected = Docstring()
    assert expected == ret, "GoogleParser.parse(\"\") returns %s, expected %s" % (
        ret,
        expected,
    )

    # Test case 2: no sections
    text = "No Section"
    ret = GoogleParser().parse(text)
    expected = Docstring(
        short_description="No Section",
        blank_after_short_description=False,
        long_description=None,
        blank_after_long_description=False,
        meta=[DocstringMeta(args=[], description="No Section", type_name=None)],
    )

# Generated at 2022-06-13 19:33:58.233387
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
        Test with valid docstring

        Short description
        Long description
        More long description
        Arguments:
          param1: Param 1 description
          param2: Param 2 description
        Examples:
          >>> example1
            example1.__doc__
          >>> example2
            example2.__doc__
        Returns:
          return obj: Return description
        '''
    assert parse(text)
    

# Generated at 2022-06-13 19:34:08.006613
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # parse GoogleParser docstring
    doc = inspect.getdoc(GoogleParser)
    d = GoogleParser().parse(doc)
    assert "Google-style docstring parsing." == d.short_description
    assert len(d.meta) == 0

    # parse GoogleParser docstring
    d = parse(doc)
    assert "Google-style docstring parsing." == d.short_description
    assert len(d.meta) == 0

    # parse function docstring
    doc = inspect.getdoc(test_GoogleParser_parse)
    d = parse(doc)
    assert "Unit test for method parse" == d.short_description
    assert len(d.meta) == 0

# Generated at 2022-06-13 19:34:17.878252
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    d = p.parse("""
        Brief description.

        Extended description.
        More.

        Args:
            arg1: Int.
            arg2: str.
            arg3, optional (str): str. Defaults to '1'.
        Returns:
            optional: str. Defaults to '2'.

        Return type.
        Return description.
        Another line
        Another line

        """
        )
    assert d.short_description == "Brief description."
    assert d.blank_after_short_description
    assert d.long_description.startswith("Extended description.")
    assert d.blank_after_long_description
    assert len(d.meta) == 4
    assert d.meta[0].args == ["param", "arg1"]
    assert d.meta[0].description

# Generated at 2022-06-13 19:34:24.465041
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
This is a useful function.

Args:
    arg1 (str): The first argument.
    arg2 (int): The second argument. Defaults to 1.

Returns:
    float: Error rate.

Raises:
    ValueError: If `arg1` is greater than `arg2`.
    TypeError: If `a` is not an `int`.
"""
    print(GoogleParser().parse(text))

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:34:38.233633
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:41.862440
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Edit here to test different values for docstring
    docstring = '''Example:
        foo()
    '''

    parser = GoogleParser()
    ret = parser.parse(docstring)

    assert ret.short_description == 'Example'
    assert ret.long_description == 'foo()'
    assert ret.meta[0].args == ['example']
    assert ret.meta[0].description == 'foo()'


# Generated at 2022-06-13 19:34:51.806955
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    doc = '''Example function with types documented in the docstring.
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise.
    '''
    d = p.parse(doc)
    assert d.short_description == 'Example function with types documented in the docstring.'
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert len(d.meta) == 3
    assert d.meta[0].args == ['param1', 'int']
    assert d.meta[0].arg_name == 'param1'

# Generated at 2022-06-13 19:35:06.778636
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    GoogleParser = GoogleParser()
    docstring = inspect.cleandoc("""
        Parse the Google-style docstring into its components.

        :returns: parsed docstring
        :rtype: dict

        .. seealso::

            http://google.github.io/styleguide/pyguide.html#383-google-python-docstrings
        """)


# Generated at 2022-06-13 19:35:15.638664
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Normal case
    text = r"""
            The ``add_model`` method.

            Args:
                model: An instance of :class:`Model`.

            Raises:
                NotCorrectTypeError: If ``model`` is not correct type.
                ExistsModelError: If ``model`` is already in the database.

            Example:
                >>> model = Model(name="test")
                >>> parameter = Parameter(name="test_param")
                >>> database.add_model(model)
                >>> database.add_parameter(model, parameter)
                >>> database.add_model(model)
                ExistsModelError: Model 'test' already exists
            """
    parsed = parse(text)
    assert isinstance(parsed.short_description, str)
    assert parsed.short_description == "The ``add_model`` method."

# Generated at 2022-06-13 19:35:21.095856
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parse(
        """
        This is a short summary.

        This is the long description.

        Args:
            arg1 (int): Description of arg1.
            arg2 (str): Description of arg2.

        Returns:
            bool: Description of return value.
        """
    )
    parse(
        """
        This is a short summary.

        This is the long description.

        Args:
            arg1 (int): Description of arg1.
            arg2 (str): Description of arg2.

        Raises:
            ValueError: If something bad happens.

        Yields:
            bool: Description of yielded value.
        """
    )

# Generated at 2022-06-13 19:35:31.114205
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:35:47.854625
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '''
    This is an example of Google-style docstring.

    Args:
        a: the first parameter
        b: the second parameter. this parameter has "quoted string" inside.
        c: the third parameter
    Returns:
        This is a description of what is returned. 
        This can span multiple lines.
    Raises:
        AttributeError, KeyError
    '''

    assert GoogleParser().parse(docstring).short_description ==\
            "This is an example of Google-style docstring."


# Generated at 2022-06-13 19:35:56.893450
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    good_docstring = """Test

    :param foo: description
    :type foo: str
    :param bar: description
    :type bar: int, optional
    :return: description
    :rtype: str
    :raises ValueError: description

    """
    parsed = parser.parse(good_docstring)
    assert len(parsed.meta) == 4
    assert parsed.meta[0].arg_name == "foo"
    assert parsed.meta[0].type_name == "str"
    assert parsed.meta[1].arg_name == "bar"
    assert parsed.meta[1].type_name == "int"
    assert parsed.meta[1].is_optional is True
    assert isinstance(parsed.meta[2], DocstringReturns)

# Generated at 2022-06-13 19:36:03.775280
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("").short_description is None

    doc = parse("Summary sentence.")
    assert doc.short_description == "Summary sentence."
    assert doc.long_description is None

    doc = parse("Summary sentence.\n")
    assert doc.short_description == "Summary sentence."
    assert doc.long_description is None

    doc = parse("Summary sentence.\n\n")
    assert doc.short_description == "Summary sentence."
    assert doc.long_description is None

    doc = parse("Summary sentence.\n\nLonger description.")
    assert doc.short_description == "Summary sentence."
    assert doc.long_description == "Longer description."

    doc = parse("Summary sentence.\n\nLonger description.\n")
    assert doc.short_description == "Summary sentence."
    assert doc.long_description

# Generated at 2022-06-13 19:36:09.869258
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  parser = GoogleParser()
  print(parser.parse("Parses a Google-style docstring."))
  print(parser.parse("Parses a Google-style docstring.\n"))
  print(parser.parse("""
  Parses a Google-style docstring.

  Args:
    text (str): Text to parse.

  Returns:
    Docstring: Parsed docstring.
  """))


# Generated at 2022-06-13 19:36:11.275680
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert inspect.getsource(GoogleParser.parse)



# Generated at 2022-06-13 19:36:22.079599
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_input = '''Short description.

Long description.

Args:
    name: description of name
    other_name: description of other_name
    name_with_type (str): description of name_with_type
    complex_name (int, optional): description of complex_name. Defaults to 42.
    name_with_default (int): description of name_with_default. Defaults to 42.

Returns:
    complex_type (str, optional): description of complex_return
    other_return: description of other_return
    return: description of return

Raises:
    ValueError: description of exception
'''



# Generated at 2022-06-13 19:36:37.133937
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_text = '''
    """
    Some text for this docstring.
    
    Args:
        arg1 (int): Argument 1
        arg2 (float): Argument 2. Defaults to 10.
        arg3: Argument 3
        arg4 (str, optional): Argument 4
    """
    '''
    docstring_text_2 = '''
    """
    Some text for this docstring.
    
    Arguments:
        arg1 (int): Argument 1
        arg2 (float): Argument 2. Defaults to 10.
        arg3: Argument 3
        arg4 (str, optional): Argument 4
    """
    '''
    #without parameters
    docstring_text_3 = '''
    """
    Some text for this docstring.
    """
    '''
    #with parameters and no args


# Generated at 2022-06-13 19:36:43.216692
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # func_code is a deprecated attribute.
    # We have to use method_code in Python 3.4 or above
    if hasattr(inspect.signature, 'method_code'):
        method_code = inspect.signature
    else:
        method_code = inspect.func_code
    title_colon = False

# Generated at 2022-06-13 19:36:56.516863
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Case 1
    """
    try:
        GoogleParser.parse(GoogleParser(), "")
    except:
        assert False
    finally:
        assert True
    """
    Case 2
    """
    try:
        GoogleParser.parse(GoogleParser(), """Initialize a new object. Note that
        this will delete all previously existing content.

        :param name: The name of the object.
        :param alpha: The alpha value.
        :param beta: The beta value.
        """)
    except:
        assert False
    finally:
        assert True
    """
    Case 3
    """

# Generated at 2022-06-13 19:37:06.367924
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''
    This is a module docstring.
    
    This is the rest of the module docstring.
    
    Attributes:
        answer (int): The answer to life the universe and everything.
        pi (float): Pi (of course).
    
    Raises:
        TypeError: Only if i feel like it.
    
    Example:
        Just an example.
    
    Returns:
        str: Everything is a str.
    '''
    ret = parse(doc)
    assert ret.short_description == "This is a module docstring."
    assert ret.blank_after_short_description == True
    assert ret.long_description == "This is the rest of the module docstring."
    assert ret.blank_after_long_description == True

# Generated at 2022-06-13 19:37:15.969442
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''\
    Some short description.
    
    Some longer description for this function.
    
    Args:
        a: First thing to pass.
        b: Second argument, defaults to "Foo".
            Also supports multi-line descriptions.
            And even more.
        c: Third thing.
            Yes, it can happen.
    
    Returns:
        This will be something.
    
    Raises:
        ValueError: Something bad happened.
        
        ValueError: Actually, something worse.
    '''
    doc = GoogleParser().parse(text)
    assert doc.short_description == "Some short description."
    assert doc.long_description == "Some longer description for this function."
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True
   

# Generated at 2022-06-13 19:37:28.427116
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ds = """
    Inserts a value into the collection.
    If the collection already contains an element with the specified value, the
    addition is ignored.

    Arguments:
        value: The object to add to the collection.
    """
    ret = GoogleParser().parse(ds)
    assert ret.short_description == "Inserts a value into the collection."
    assert ret.blank_after_short_description == False
    assert ret.long_description == "If the collection already contains an element with the specified value, the\naddition is ignored."
    assert ret.blank_after_long_description == True

    assert ret.meta[0].description == "The object to add to the collection."
    assert ret.meta[0].arg_name == "value"
    assert ret.meta[0].type_name is None
    assert ret.meta

# Generated at 2022-06-13 19:37:30.849131
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    googleParser = GoogleParser()
    docstring = inspect.cleandoc("""
        """
    )


    assert parse(docstring) == googleParser.parse(docstring)



# Generated at 2022-06-13 19:37:40.385491
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    d = '''\
        Args:
            a (int): Value of a.
            b (int): Value of b.
        '''

    doc = GoogleParser().parse(d)
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.meta == [
        DocstringParam(args=["param", "a (int)"], description="Value of a.", arg_name="a", type_name="int", is_optional="int", default="int"),
        DocstringParam(args=["param", "b (int)"], description="Value of b.", arg_name="b", type_name="int", is_optional="int", default="int"),
    ]



# Generated at 2022-06-13 19:37:42.965291
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring
    from .parser import GoogleParser
    p = GoogleParser()
    assert p.parse(None) == Docstring()
    assert p.parse("") == Docstring()



# Generated at 2022-06-13 19:37:52.191740
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    sample_docstring = """
        My docstring

        Args:
            name (string): My name
            best_friend (str): My best friend's name

        Raises:
            RuntimeError: The error message.

        Returns:
            The best friend's name
    """
    from .models import Docstring
    from typing import Dict, Optional

    test_docstring: Optional[Docstring] = GoogleParser().parse(sample_docstring)

    assert len(test_docstring.meta) == 3

    assert test_docstring.meta[0].args == ['param', 'name (string)']
    assert test_docstring.meta[0].arg_name == 'name'
    assert test_docstring.meta[0].type_name == 'string'


# Generated at 2022-06-13 19:38:02.117480
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Parses string arguments into datetime.

    The string should be in a format understood by datetime.datetime.strptime
    (except that fractional seconds are allowed).

    Args:
      dt_str: A string representation of the date and time in a format from the
        datetime.datetime.strptime documentation.

    Raises:
      ValueError: If dt_str is not a string or is not in a known format.
    """

    docstring_parsed = parse(docstring)

    assert docstring_parsed.short_description == 'Parses string arguments into datetime.'
    assert docstring_parsed.long_description == """The string should be in a format understood by datetime.datetime.strptime
    (except that fractional seconds are allowed)."""

# Generated at 2022-06-13 19:38:08.554953
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    f = lambda x: google_parser.parse(x).__dict__
    assert f('') == {
        'short_description': None,
        'long_description': None,
        'blank_after_short_description': False,
        'blank_after_long_description': False,
        'meta': [],
    }
    assert f('\n') == {
        'short_description': None,
        'long_description': None,
        'blank_after_short_description': True,
        'blank_after_long_description': False,
        'meta': [],
    }

# Generated at 2022-06-13 19:38:12.620547
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    d = gp.parse("""Exapmle of a docstring.

    Args:
        a (str): A
        b (str): B
        c (int): C

    Returns:
        None
        """)

# Generated at 2022-06-13 19:38:21.280022
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def my_function_with_docstring(arg1, arg2):
        """This is an example of a function's docstring.
        Function may have arguments, return, raises and yield value(s).

        :param arg1: The first parameter.
        :param arg2: The second parameter.
        :returns: None
        :raises Exception: if something bad happens.
        :yields: None
        """

    docstring = GoogleParser().parse(
        my_function_with_docstring.__doc__
    )
    assert docstring.short_description == 'This is an example of a function\'s docstring.'
    assert docstring.long_description == 'Function may have arguments, return, raises and yield value(s).'
    assert len(docstring.meta) == 10

# Generated at 2022-06-13 19:38:34.530537
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_text = """
    This is a docstring.
    This is the long description.

    Args:
        arg1 (str): The first argument.
        arg2 (Optional[int]): The second argument.

    Returns:
        str: A string return value.
    """
    docstring = GoogleParser().parse(docstring_text)

    assert docstring.short_description == "This is a docstring."
    assert docstring.long_description == "This is the long description."
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False

    params = [docstring.meta[0], docstring.meta[1]]
    param1, param2 = params
    assert param1.arg_name == "arg1"
    assert param1.type_name

# Generated at 2022-06-13 19:38:41.452211
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    obj = GoogleParser()
    assert inspect.getdoc(GoogleParser.parse) == 'Parse the Google-style docstring into its components.\n\n:returns: parsed docstring\n'

    text = inspect.cleandoc(inspect.getdoc(GoogleParser))
    assert obj.parse(text) == inspect.cleandoc(inspect.getdoc(GoogleParser))

    assert inspect.getdoc(GoogleParser.__init__) == 'Setup sections.\n\n:param sections: Recognized sections or None to defaults.\n:param title_colon: require colon after section title.\n'

    text = inspect.cleandoc(inspect.getdoc(GoogleParser.__init__))
    assert obj.parse(text) == inspect.cleandoc(inspect.getdoc(GoogleParser.__init__))

   

# Generated at 2022-06-13 19:38:55.695468
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse('Takes two numbers and adds them.\n\n    >>> add(2, 3)\n    5\n\n    >>> add(100,200)\n    300\n    ')
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == 'Takes two numbers and adds them.'
    assert not docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.long_description == '    >>> add(2, 3)\n    5\n\n    >>> add(100,200)\n    300\n'
    assert len(docstring.meta) == 0
    parser.add_section(Section('Example','examples', SectionType.SINGULAR))

# Generated at 2022-06-13 19:39:11.245949
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = """
        Short summary

        :param arg1: First argument
        :param arg2: Second argument
        :param arg3: Third arg
        :type arg1: int, optional
        :type arg2: str, optional
        :returns:
            test_returns
        :raises:
            ValueError, KeyError
        """

    parsed = parser.parse(docstring)
    assert len(parsed.meta) == 5
    assert parsed.short_description == "Short summary"
    assert parsed.long_description == ""
    assert parsed.blank_after_short_description
    assert not parsed.blank_after_long_description

    section = parsed.meta[0]
    assert section.args == ["param", "arg1"]

# Generated at 2022-06-13 19:39:21.558953
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """This is the short description.

This is the first line of the long description.
This is the second line of the long description.

Args:
    param1 (str): This is the first parameter. Defaults to None.
        This is the second line of description for the first parameter.
    param2 (int, optional): This is the second parameter.
        Defaults to 10.

Returns:
    str: This is the return value.
"""
    result = GoogleParser().parse(docstring)

    assert result.short_description == "This is the short description."
    assert result.long_description == "This is the first line of the long description.\nThis is the second line of the long description."
    assert result.blank_after_short_description
    assert result.blank_after_long_description

# Generated at 2022-06-13 19:39:30.840902
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "test_method(test_arg_a, test_arg_b) \n" \
           "\n" \
           "Args:\n" \
           "    test_arg_a(string): test_arg_a_description\n" \
           "    test_arg_b(string): test_arg_b_description\n" \
           "\n" \
           "Returns:\n" \
           "    test_return_description"
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == "test_method(test_arg_a, test_arg_b)"
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].args

# Generated at 2022-06-13 19:39:41.756152
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstr = """A class docstring.

    Attributes:
        my_attr (int): My attribute.
        my_other_attr [str]: My other attribute.
        my_third_attr[int]: My third attribute.
        my_fourth_attr (int, optional): My fourth attribute.
        my_fifth_attr: My fifth attribute.
    """

# Generated at 2022-06-13 19:39:48.738606
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    expected_short_description = "Calculates the binomial coefficient."
    expected_long_description = "This is useful for calculating the number of possible combinations for n items, taken k at a time.\n\n    >>> binomial(10,3)\n    120\n\n    >>> binomial(7,3)\n    35"
    expected_returns_description = "The binomial coefficient."
    expected_param_arg_name = "n"
    expected_param_description = "The total number of items."
    expected_raises_description = "If n < 0 or k < 0 or k > n."
    expected_examples_description = ">>> binomial(10,3)\n120\n\n>>> binomial(7,3)\n35"
    expected_blank_after_short_description = False
    expected_blank_after

# Generated at 2022-06-13 19:39:59.665833
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def f1():
        """
        Short description.

        Long description.

        Arguments:
            arg1:
                description.
            arg2:
                description.

        Returns:
            description.

        Example:
            Examples can be given using either the ``Example`` or ``Examples`` sections.
            Sections support any reStructuredText formatting, including literal
            blocks::

                $ python example_google.py
        """
        pass

    def f2():
        """
        Short description.

        Arguments:
            arg1:
                description.
            arg2:
                description.

        Returns:
            description.

        Example:
            Examples can be given using either the ``Example`` or ``Examples`` sections.
            Sections support any reStructuredText formatting, including literal
            blocks::

                $ python example_google.py
        """

# Generated at 2022-06-13 19:40:08.971461
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:40:17.650895
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
        Google style docstring.

        Formatting with Markdown.

        Args:
            arg1: The first argument.
            arg2: The second argument.
        Args:
            arg3: The third argument.
            arg4: The fourth argument.
        Raises:
            ValueError: if something bad happens.
        Returns:
            Some return value.
        Yields:
            Some yield value.
        """
    assert parse(text).short_description == "Google style docstring."
    assert parse(text).meta[0].description == (
        "The first argument."
    )
    assert parse(text).meta[1].description == (
        "The second argument."
    )
    assert parse(text).meta[2].description == (
        "The third argument."
    )

# Generated at 2022-06-13 19:40:26.920096
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import pytest
    from .common import ParseError, RETURNS_KEYWORDS, DocstringReturns, DocstringParam, PARAM_KEYWORDS, DocstringRaises, Docstring, RAISES_KEYWORDS
    from .google import GoogleParser

    def test_GoogleParser_parse_01():
        docstring = "Compute some value\n\n:param x: The x parameter.\n:type x: int\n:param y: The y parameter.\n:type y: int\n:returns: Result of computation.\n:rtype: int\n"

# Generated at 2022-06-13 19:40:27.935768
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass
