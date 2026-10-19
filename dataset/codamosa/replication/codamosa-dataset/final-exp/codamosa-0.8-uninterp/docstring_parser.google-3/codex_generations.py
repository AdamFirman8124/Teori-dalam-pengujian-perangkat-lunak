

# Generated at 2022-06-13 19:31:17.529419
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse('''
    a title
    A description

    title
    Args:
        param1: The first parameter.
        param2: The second parameter. Defaults to None.
    Raises:
        Exception: The first exception.
        Exception: The second exception.
    Yields:
        int: A number.
    Returns:
        int: The number 2.
    ''')

    assert docstring.short_description == "a title"
    assert docstring.long_description == "A description"
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False

    assert docstring.meta[0].__class__.__name__ == "DocstringParam"
    assert docstring.meta[0].description == "The first parameter."

# Generated at 2022-06-13 19:31:30.028838
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test(args):
        doc = GoogleParser().parse(args)

        assert doc.short_description is not None
        assert doc.short_description == 'Agent description'

        assert doc.long_description is not None
        assert doc.long_description == 'Agent description\n'

        assert doc.blank_after_short_description == True
        assert doc.blank_after_long_description == False

        assert doc.meta[0].key == 'param'
        assert doc.meta[0].args == ['param', 'speed (float):']
        assert doc.meta[0].description == 'Description of parameter speed'

        assert doc.meta[1].key == 'param'
        assert doc.meta[1].args == ['param', 'direction (int):']
        assert doc.meta[1].description == 'Description of parameter direction'

       

# Generated at 2022-06-13 19:31:41.843799
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_string = '''One line summary.

    Extended description.

    Two blank lines required at the end.

    Args:
        arg1: First argument.
        arg2: Second argument.

        A long description for the second argument.

    Kwargs:
        kwarg1: First keyword argument.
        kwarg2: Second keyword argument.

        A long description for the second keyword argument.

    Returns:
        One line summary.

        A long description of the return value.
    '''
    a = parse(doc_string)
    assert a.short_description == 'One line summary.'
    assert a.long_description == 'Extended description.'
    assert a.blank_after_short_description == True
    assert a.blank_after_long_description == True
    assert len(a.meta) == 3
    att

# Generated at 2022-06-13 19:31:50.864326
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring
    from .utils import compare_docstring
    from .parser import GoogleParser
    
    
    text = """\
        This is a short description.
    
        This is long description. Everything until the next empty line is part of the long description.
    
        This is another paragraph.
    
        Args:
            arg1 (str): The first argument.
            arg2 (int, optional): The second argument. Defaults to 42.
    
        Returns:
            None
        """
    
    expected = Docstring()
    expected.short_description = 'This is a short description.'
    expected.long_description = 'This is long description. Everything until the next empty line is part of the long description.\n        This is another paragraph.'
    expected.blank_after_short_description = True
    expected.blank

# Generated at 2022-06-13 19:31:58.375370
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    test_GoogleParser_parse()
    
    Desc
    """
    assert parse(text) == Docstring(
        short_description = 'test_GoogleParser_parse()',
        long_description = 'Desc',
        blank_after_short_description = True,
        blank_after_long_description = False,
        meta=[]
    )

# Generated at 2022-06-13 19:32:11.223010
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse('''
        This is a docstring for a method. It can span multiple lines.

        Args:
            param1 (T): Description of param1
            param2 (T, optional): Description of param2
            param3 (T): Description of param3
        ''').meta[0].args == ('param', 'param1 (T)')
    assert parse('''
        This is a docstring for a method. It can span multiple lines.

        Args:
        param1 (T): Description of param1
        param2 (T, optional): Description of param2
        param3 (T): Description of param3
        ''').meta[0].args == ('param', 'param1 (T)')

# Generated at 2022-06-13 19:32:22.314238
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	"""Unit test for method parse of class GoogleParser"""
	parser = GoogleParser()
	docstring = parser.parse("""
		This is a very simple function.

		Args:
			a: first parameter
			b: second parameter

		Returns:
			c: third parameter
		
	""")
	print(docstring.short_description)
	print(docstring.long_description)
	print(docstring.meta[0].description)
	print(docstring.meta[1].description)


# Generated at 2022-06-13 19:32:28.347970
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert True == True
    return
    text = """This function does something.

    This is a longer explanation of what it does.

    :param int x: param x
    :param int y: param y
    :returns: this is what's returned
    :raises ValueError: if x < 0
    """

    r = GoogleParser().parse(text)
    assert r.short_description == "This function does something."
    assert r.long_description == "This is a longer explanation of what it does."
    assert r.blank_after_short_description
    assert r.blank_after_long_description
    assert not r.meta
    assert r.params
    assert r.raises
    assert r.returns
    assert not r.yields

# Generated at 2022-06-13 19:32:39.978113
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstr = GoogleParser().parse("""
        This function does something.
        :param int param1: This is a first parameter.
        :param param2: This is a second parameter
        :param param3: This is a third, optional parameter. Defaults to True.
        :param float param4: This is a fourth, optional parameter. Defaults to 0.3.
        :returns int: This is a description of what is returned.
        :return: This is a description of what is returned.
        :raises ValueError: If something is wrong.
    """)
    assert docstr.short_description == "This function does something."
    assert docstr.long_description is None
    assert docstr.blank_after_short_description
    assert not docstr.blank_after_long_description

    # check parameters

# Generated at 2022-06-13 19:32:49.051327
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse('Single line\n\nLong description.\n\nArgs:\n    arg1: description.\n    arg2: description.\n\nRaises:\n    ValueError: description.\n\nReturns:\n    description.\n\nYields:\n    description.\n\n')

    # Short description
    print('|' + docstring.short_description + '|')
    assert docstring.short_description == 'Single line'

    # Long description
    print('|' + docstring.long_description + '|')
    assert docstring.long_description == 'Long description.'

    # Blank after short description
    print('|' + str(docstring.blank_after_short_description) + '|')
    assert docstring.blank_after_

# Generated at 2022-06-13 19:33:06.181659
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse(None) == Docstring()

    text = u"""Test google parser.

    Does this work?

    """
    result = Docstring(
        short_description="Test google parser.",
        long_description="Does this work?",
        blank_after_short_description=True,
        blank_after_long_description=True,
    )
    assert parse(text) == result

    text = u"""Test google parser.

    Does this work?
    """
    result = Docstring(
        short_description="Test google parser.",
        long_description="Does this work?",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert parse(text) == result

    text = u"""Test google parser.

    Does this work?"""

# Generated at 2022-06-13 19:33:17.546816
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring
    from .google import GoogleParser
    
    G_PARSER = GoogleParser()
    text = '''Parse the Google-style docstring into its components.
    
    :returns: parsed docstring
    '''
    exp_docstr = Docstring(
        short_description=None,
        long_description='Parse the Google-style docstring into its components.',
        meta=[DocstringReturns(
            args=['returns', 'parsed docstring'],
            description='parsed docstring',
            type_name='parsed docstring',
            is_generator=False,
        )],
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    res_docstr = G_PARSER.parse(text)

# Generated at 2022-06-13 19:33:23.835633
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Single line.
    And second.
    """
    expected = Docstring(
        short_description = "Single line.",
        blank_after_short_description = False,
        blank_after_long_description = False,
        long_description = "And second.",
        meta = [],
    )
    assert GoogleParser().parse(text) == expected


# Generated at 2022-06-13 19:33:33.166048
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    parser = p.parse("""\
        This is an example function.

        This is a longer description of the function.

        Args:
            arg1 (str): This is the first argument.
            arg2: This arg is not typed.

        Raises:
            ValueError: Raised when arg1 is not valid.
            ValueError: Raised when arg2 is not valid.

        Returns:
            str: a string.

        Examples:
            These are examples of the function

            >>> func(1, 2)
            3

            >>> func(2, 3)
            5
    """)
    assert parser.short_description == "This is an example function."
    assert parser.blank_after_short_description is True
    assert parser.long_description == ("This is a longer description of the function.")
   

# Generated at 2022-06-13 19:33:46.589862
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """
    This function does something.

    Args:
        param1: This is the first param.
        param2: This is a second param.
        param3: This is a third param.

    Returns:
        This is a description of what is returned.
        This can span multiple lines.

    Raises:
        KeyError: Raises an exception.
        OtherError: Raises a different exception.

    """
    parsed = parser.parse(text)
    assert parsed.short_description == "This function does something."
    assert parsed.long_description == "This can span multiple lines."
    assert parsed.blank_after_short_description
    assert parsed.blank_after_long_description
    assert len(parsed.meta) == 4

# Generated at 2022-06-13 19:33:58.053885
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class Foo:
        """This is a class

        Args:
            this (int): a
            that (:obj:`int`, optional): b
            these (List[int]): c
            those (List[:obj:`int`, :obj:`float`]): d

        Example:
            >>> x = y
            >>> x = [w, z]

        Raises:
            ValueError: something

        Returns:
            str: something

        """

    doc = GoogleParser().parse(Foo.__doc__)

# Generated at 2022-06-13 19:34:09.282155
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_target = """
    Google-style docstrings.

    Short summary of this class.

    Long description of this class.

    Args:
        param1 (bool): The first parameter.
        param2 (int): The second parameter.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    

# Generated at 2022-06-13 19:34:20.331806
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text1 = """\
    This function does something.

    Args:
        arg1: The first argument.
        arg2: The second argument.

    Returns:
        This is a description of what is returned.
    """
    docstring1 = GoogleParser().parse(text1)
    if (
        docstring1.short_description
        == "This function does something."
        and docstring1.long_description is None
        and docstring1.blank_after_short_description == False
        and docstring1.blank_after_long_description == False
        and len(docstring1.meta) == 2
    ):
        pass
    else:
        print("test1 failed, got:")
        print("short_description:", docstring1.short_description)

# Generated at 2022-06-13 19:34:27.830827
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "Test\nArgs:\n    param1 (int): this is an int\n"
    text += "    param2 (str): this is a string\n\nReturns:\n    int"

    # GoogleParser object with default sections
    gp = GoogleParser()
    doc = gp.parse(text=text)
    
    assert(len(doc.meta) == 3)

    assert(doc.meta[0].description == "Test")
    assert(doc.meta[0].args == ["description"])

    assert(doc.meta[1].description == "this is an int")
    assert(doc.meta[1].arg_name == "param1")
    assert(doc.meta[1].args == ["param", "param1 (int)"])

    assert(doc.meta[2].description == None)

# Generated at 2022-06-13 19:34:37.094151
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    G = GoogleParser()
    s = G.parse("""
        This is a function to demo the GoogleParser parser
        :param a: the first parameter
        :param b: the second parameter, can has more than one lines
        :param c: the third parameter
        :return: something
        :rtype: str
        :Example:
        >>> example1 = 1
        >>> example2 = 2
        >>> example3 = 3
        """)
    assert s.short_description == "This is a function to demo the GoogleParser parser"
    assert s.meta[0].args == ("param", "a")
    assert s.meta[0].description == "the first parameter"
    assert s.meta[1].args == ("param", "b")
    assert s.meta[1].description == "the second parameter, can has more than one lines"


# Generated at 2022-06-13 19:34:51.274206
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    This is a method.
    This is a description of the method.

    Args:
        arg1 (int): the first arg. Defaults to 0.
        arg2 (int): the second arg.
    """
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == "This is a method."
    assert docstring.long_description == "This is a description of the method."
    assert len(docstring.meta) == 2
    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[0].description == "the first arg."
    assert docstring.meta[0].is_optional
    assert docstring.meta[0].default == "0"
    assert doc

# Generated at 2022-06-13 19:35:06.118961
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("Testing method parse of class GoogleParser")
    parser = GoogleParser()
    docstringParser = GoogleParser()

    # Test 1. description 
    docstringText = """The number a is a parameter.
    The number b is also a parameter.
    """
    docstring = docstringParser.parse(docstringText)
    docstring_test = Docstring(
        short_description = "The number a is a parameter.",
        blank_after_short_description = False,
        long_description = "The number b is also a parameter.",
        blank_after_long_description = True,
        meta = [DocstringMeta(args = [], description = "The number a is a parameter."),
                DocstringMeta(args = [], description = "The number b is also a parameter.")],
    )
    print("Should be:")
   

# Generated at 2022-06-13 19:35:14.648114
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    doc = """Test parser
    :param int arg1: argument 1
    """
    docstring = parser.parse(doc)
    print(docstring.short_description)
    print(docstring.long_description)
    print(docstring.meta)
    doc = """Test parser
    :param int arg1: argument 1
    :param int arg2: argument 2
    """
    docstring = parser.parse(doc)
    print(docstring.short_description)
    print(docstring.long_description)
    print(docstring.meta)
    doc = """Test parser

    :param int arg1: argument 1
    :param int arg2: argument 2
    """
    docstring = parser.parse(doc)
    print(docstring.short_description)

# Generated at 2022-06-13 19:35:25.456038
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert Docstring() == GoogleParser().parse("")
    assert Docstring() == GoogleParser().parse(" ")
    assert Docstring(short_description="foo") == GoogleParser().parse("foo")
    assert (
        Docstring(
            short_description="foo",
            long_description="bar\nbaz",
            blank_after_short_description=True,
            blank_after_long_description=False,
        )
        == GoogleParser().parse("foo\n\nbar\nbaz")
    )

# Generated at 2022-06-13 19:35:36.011662
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # 1
    googleParser = GoogleParser()
    text = "Implements the identity function"
    result = googleParser.parse(text)
    assert result.short_description == "Implements the identity function"
    assert result.blank_after_short_description == False
    assert result.blank_after_long_description == False
    assert result.long_description == None
    assert len(result.meta) == 0

    # 2
    googleParser = GoogleParser()
    text = """\
    Parses the Google-style docstring into its components.
    
    :returns: parsed docstring
    """
    result = googleParser.parse(text)
    assert result.short_description == "Parses the Google-style docstring into its components."
    assert result.blank_after_short_description == True

# Generated at 2022-06-13 19:35:51.740450
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:35:59.518515
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse(" ") == Docstring()
    assert GoogleParser().parse("a") == Docstring(
        short_description="a", long_description=None
    )
    assert GoogleParser().parse("a b") == Docstring(
        short_description="a b", long_description=None
    )
    assert GoogleParser().parse("a\nb") == Docstring(
        short_description="a", long_description="b"
    )
    assert GoogleParser().parse("a\n b") == Docstring(
        short_description="a",
        long_description="b",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 19:36:06.420576
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # 1. Method parse can handle given doc string without titles.
    text_without_titles = """
    google style doc string by python
    """
    ret = GoogleParser().parse(text_without_titles)
    expected_ret = Docstring(
        short_description="google style doc string by python",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )
    assert ret == expected_ret

    # 2. Method parse can handle given doc string with titles.

# Generated at 2022-06-13 19:36:11.513160
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import sys
    import os
    import doctest
    current_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    module_path = os.path.join(current_path, '..')
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS,
                    path=module_path)

# Generated at 2022-06-13 19:36:17.484470
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse(None) == Docstring()
    docstring = "This is a description.\n\n"
    assert GoogleParser().parse(docstring).short_description == "This is a description."
    assert GoogleParser().parse(docstring).long_description == None
    docstring = "This is a description.\n    It is multi-line.\n"
    assert GoogleParser().parse(docstring).short_description == "This is a description."
    assert GoogleParser().parse(docstring).long_description == "It is multi-line."
    docstring = "This is a description.\n\n    It is multi-line.\n"
    assert GoogleParser().parse(docstring).short_description == "This is a description."

# Generated at 2022-06-13 19:36:37.053004
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #tests for method parse of class GoogleParser
    assert(GoogleParser(
        sections=[Section("SectionTitle", "SectionKey", 2)]
    ).parse('') == Docstring())
    assert(
        GoogleParser(
            sections=[Section("SectionTitle", "SectionKey", 2)]
        ).parse(
            'This is the short description.\n' +
            '\n' +
            'And this is the long description.'
        ) == Docstring(
            short_description="This is the short description.",
            blank_after_short_description=True,
            long_description="And this is the long description.",
            blank_after_long_description=False,
            meta=[]
        )
    )

# Generated at 2022-06-13 19:36:45.645814
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
        The docstring to parse.

        :param int a: First parameter.

        :param b: Second parameter.

        :returns:
            some text

            more text

        :raises ZeroDivisionError:
            If b is 0.
    """

# Generated at 2022-06-13 19:36:58.527150
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    meta: DocstringMeta
    params: T.List[DocstringParam]
    parser = GoogleParser()

# Generated at 2022-06-13 19:37:03.345209
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse(
    """Compute the sigmoid of x element-wise.

    Parameters
    ----------
    x : array_like
        Input values.

    Returns
    -------
    ndarray, float
        The sigmoid of `x`, element-wise.
    """
    )
    assert docstring.short_description == "Compute the sigmoid of x element-wise."
    assert docstring.long_description == "Input values."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].args[0] == 'param'
    assert docstring.meta[0].args[1] == 'x'

# Generated at 2022-06-13 19:37:10.448207
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    def func_with_docstring():
        """
        Short summary.

        Long summary.
        """

    docstring = parse(inspect.getdoc(func_with_docstring))

    expected_docstring = Docstring(
        short_description="Short summary.",
        long_description="Long summary.",
        blank_after_short_description=True,
        blank_after_long_description=False,

    )

    assert docstring == expected_docstring

# Generated at 2022-06-13 19:37:17.757188
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    assert parse("No description.") == Docstring(
        short_description="No description."
    )
    assert parse("No description.\n") == Docstring(
        short_description="No description."
    )
    assert parse("No description.\n\n") == Docstring(
        short_description="No description.",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
    )
    assert parse("One line.") == Docstring(
        short_description="One line."
    )

# Generated at 2022-06-13 19:37:30.565409
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert (
        GoogleParser().parse("Short description\n\nLong description")
        == Docstring(
            short_description="Short description",
            blank_after_short_description=True,
            long_description="Long description",
            blank_after_long_description=False,
            meta=[],
        )
    )
    assert (
        GoogleParser().parse("Short description\n\nLong description\n")
        == Docstring(
            short_description="Short description",
            blank_after_short_description=True,
            long_description="Long description",
            blank_after_long_description=True,
            meta=[],
        )
    )

# Generated at 2022-06-13 19:37:46.178782
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:52.546151
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
Hello world.

Args:
    arg1: A description of arg1.
    arg2: A description of arg2. Defaults to False.
    arg3: A description of arg3.
        It can be broken up into multiple lines,
        or even empty lines.
Returns:
    result1: A description of result1.
        It can be broken up into multiple lines,
        or even empty lines.

Raises:
    ValueError: If anything is wrong.
    TypeError: If anything is wrong.
"""
    #result = parse(docstring)
    #print result
    #assert result == 


# Generated at 2022-06-13 19:37:56.843230
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = '''
    """
    Description:
    Description continuation.
    I. Description part I.
    I. Description part II.
    II. Description part III.
    """
    '''
    d = parser.parse(text)
    assert d.short_description == "Description:"
    assert d.long_description == "Description continuation.\nI. Description part I.\nI. Description part II.\nII. Description part III."
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == False


# Generated at 2022-06-13 19:38:23.764488
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	parser = GoogleParser()
	docstring = parser.parse("""
    This is a google-style module docstring.

    This is a long description. It can be several paragraphs long,
    and go on and on and on and on and on and on and on and on and on.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """)
	assert docstring.short_description == "This is a google-style module docstring."
	assert docstring.long_description == """This is a long description. It can be several paragraphs long,
and go on and on and on and on and on and on and on and on and on."""
	assert docstring.blank_after_short_description == True
	

# Generated at 2022-06-13 19:38:27.092987
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test = '\n'.join(['test', '', 'hello'])
    assert parse(test).short_description == 'test'
    assert parse(test).long_description == 'hello'
    assert parse(test).blank_after_short_description == True 
    assert parse(test).blank_after_long_description == False
    assert parse(test).meta ==[]
    #print(parse(test))


# Generated at 2022-06-13 19:38:39.676058
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = inspect.cleandoc('''
        This is a short summary of my method.

        This is a longer description of the method.
        It can have multiple lines of text.

        Args:
            arg1 (int): description of argument 1
            arg2 (str): description of argument 2
            arg3: description of argument 3

        Returns:
            str: description of returned value

        Raises:
            ValueError
            TypeError
            NameError
    ''')
    parser = GoogleParser()
    my_doc = parser.parse(docstring)
    assert my_doc
    assert my_doc.short_description == "This is a short summary of my method."
    assert my_doc.long_description == '''This is a longer description of the method.
It can have multiple lines of text.'''
    assert my_doc

# Generated at 2022-06-13 19:38:52.028937
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Short summary.

    Longer summary

    Args:
        x: Parameter x.
        y: Parameter y.

    Example:
        examples.
    """

# Generated at 2022-06-13 19:38:57.258620
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test for empty docstring
    txt = ""
    docstring = GoogleParser().parse(txt)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []

    # Test for docstring without titles
    txt = """This string is used in the repr of objects.\n\n\"\"\""""
    docstring = GoogleParser().parse(txt)
    assert docstring.short_description == "This string is used in the repr of objects."
    assert docstring.long_description == "\"\"\""
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
   

# Generated at 2022-06-13 19:39:08.085519
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:14.375118
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''Single line short description. Blah blah blah.

    :param int param1: The first parameter.
    :param int param2: The second parameter.
    :param int param3: The third parameter.
    :returns: this is what is returned
    :rtype: int
    :raises keyError: depends b
    '''

    docstring = GoogleParser().parse(doc)
    print(docstring)

if __name__ == "__main__":
  test_GoogleParser_parse()

# Generated at 2022-06-13 19:39:21.449289
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    # A simple google style docstring, this is a summary of the given method

    The extended description give a more detailed explanation, it can spread on
    many paragraphs

    Args:
        param1(str): Description of param1
        param2(bool): Description of param2
        param3(Optional[str]): Description of param3
        param4(str, optional): Description of param4

    Returns:
        int: The return value.
    """
    parser = GoogleParser()
    parsed_docstring = parser.parse(docstring)
    parsed_meta = [
        ("param", "param1"),
        ("param", "param2"),
        ("param", "param3"),
        ("param", "param4"),
        ("returns", "int"),
    ]

# Generated at 2022-06-13 19:39:30.733572
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringParam, DocstringReturns, DocstringRaises, DocstringMeta
    class C:
        def foo(self, x, y=None):
            """ A short description of foo.

            A long description of foo.

            Arguments:
                x: A positional argument.
                y: An optional argument. Defaults to None.

            Returns:
                Returned value.
            """

    doc = C.foo.__doc__
    g = GoogleParser()
    parsed = g.parse(doc)

    assert parsed.short_description == 'A short description of foo.'
    assert parsed.long_description == 'A long description of foo.'
    assert parsed.blank_after_short_description == True
    assert parsed.blank_after_long_description == False
    assert len(parsed.meta) == 4


# Generated at 2022-06-13 19:39:36.976497
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    This is a description.
    First line.
    More detailed description

    Arguments:
        hi: value
        bye: value
    '''

    parsed = GoogleParser().parse(text)

    assert parsed.short_description == "This is a description."
    assert parsed.long_description == "First line.\nMore detailed description\n"
    assert parsed.meta[0].description == "value"

# Generated at 2022-06-13 19:40:25.325063
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    s = """
    This is a short description
    
    This is a long description that spans multiple lines
    
    Args:
      param1 (str): The first parameter.
      param2 (int): The second parameter. Defaults to 2.
      
    Returns:
      bool: The return value. True for success, False otherwise.
      
    Raises:
      AttributeError: The ``Raises`` section is a list
          of all exceptions
          that are relevant to the interface.
      ValueError: If `param2` is equal to `param1`.
    """

# Generated at 2022-06-13 19:40:36.618135
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = GoogleParser()

    text = "test"
    result = doc.parse(text)
    assert result.short_description == text
    assert result.long_description == None

    text = "test\n\nlong\n\n"
    result = doc.parse(text)
    assert result.short_description == text[:4]
    assert result.long_description == text[5:].strip()

    text = "test\n\nlong1\nlong2"
    result = doc.parse(text)
    assert result.short_description == text[:4]
    assert result.long_description == text[5:].strip()

    text = "test\n\nlong1\n\nlong2"
    result = doc.parse(text)
    assert result.short_description == text[:4]

# Generated at 2022-06-13 19:40:44.413393
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # initialization
    GoogleParser_instance = GoogleParser()
    text = '''
        :param text: docstring element text
        :param title: title of section containing element
        :key section.title: section title
        :key section.key: section key
        :key section.type: section type
        :return:
        '''
    test_result = GoogleParser_instance.parse(text)
    print(test_result)
    return test_result
# if __name__ == '__main__':
#     test_GoogleParser_parse()