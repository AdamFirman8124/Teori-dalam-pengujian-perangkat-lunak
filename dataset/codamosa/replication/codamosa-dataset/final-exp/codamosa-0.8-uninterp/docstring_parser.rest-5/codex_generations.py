

# Generated at 2022-06-13 19:52:22.240243
# Unit test for function parse
def test_parse():
    docstr = """Short description.

    Extended description.

    :param str arg_name: Extended description of arg_name
    :param str? arg_name_with_optional_type: Extended description of arg_name
    :param arg_name_without_type: Extended description of arg_name
    :param arg_name_without_type_or_description:
    :param arg_name_with_default: Extended description of arg_name. Defaults to 0.
    :raises ValueError: Extended description of error
    :raises: Extended description of error
    :returns: Extended description of return
    :returns str: Extended description of return
    :returns str?: Extended description of return
    :yields: Extended description of return
    :yields str: Extended description of return
    """
    doc = parse(docstr)
   

# Generated at 2022-06-13 19:52:25.491221
# Unit test for function parse
def test_parse():
    docstring = """
    This is a short description.

    This is the long description.

    :param str arg: argument description
    :param int arg2: another argument
    :param bool flag: a flag
    :raises: raised error
    :raises ValueError: another error
    :returns: return value
    :yields int: yields
    """

    parse(docstring)


# :type: (str) -> Docstring

# Generated at 2022-06-13 19:52:35.170021
# Unit test for function parse
def test_parse():
    docstring = """
    This function add two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    docstring = parse(docstring)
    assert docstring.short_description == "This function add two numbers."
    assert docstring.meta[0].args == ["Args"]
    assert docstring.meta[0].description == None
    assert docstring.meta[1].args == ["x", "The", "first", "number."]
    assert docstring.meta[1].description == None
    assert docstring.meta[2].args == ["y", "The", "second", "number."]
    assert docstring.meta[2].description == None
    assert docstring.meta[3].args == ["Returns"]

# Generated at 2022-06-13 19:52:46.073610
# Unit test for function parse
def test_parse():
    docstring = """Parses command line arguments

    This function parses command line arguments passed in an array and sets the
    relevant attributes in the class accordingly.

    :param args:
        the arguments to parse, defaults to ``sys.argv`` if not specified
        :type args: array of strings
    :param kwargs:
        any keyword parameters will be added as attributes to the class

    :raises argumentError:
        if an argument could not be successfully parsed

    :returns:
        ``None``

    :Example:

    >>> parser = ArgumentParser()
    >>> parser.addArgument("-n", "--number", help="number")
    >>> args = parser.parseArgs(["-n", "5"])
    >>> print(args.number)
    5
    """


# Generated at 2022-06-13 19:52:56.161775
# Unit test for function parse
def test_parse():
    """Test for function parse"""
    assert parse("Python!") == Docstring()
    assert parse("Python!\n") == Docstring()
    assert parse("Python!\n\n") == Docstring()
    assert parse("""\
          Python!

          And there it is.""") == Docstring(
        short_description="Python!",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="And there it is.",
    )
    assert parse("""
          Python!

          And there it is.

          """) == Docstring(
        short_description="Python!",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description="And there it is.",
    )

# Generated at 2022-06-13 19:53:02.393464
# Unit test for function parse
def test_parse():
    text = """
    func()
    :param int arg_name: Something.
    :returns: None
    :raises TypeError: something
    """
    ret = parse(text)
    assert ret.meta[0].arg_name == "arg_name"
    assert ret.meta[1].type_name == "None"
    assert ret.meta[2].type_name == "TypeError"

# Generated at 2022-06-13 19:53:11.292081
# Unit test for function parse

# Generated at 2022-06-13 19:53:20.546735
# Unit test for function parse
def test_parse():
    text = '''
Inserts element into the buffer at the given position.

:param int pos: The position to insert at.
:param int? length: The length of the insertion.
        defaults to 1.
:raises IndexError: If the position is invalid.

This method will raise an exception if you attempt to
insert at an invalid position.
    '''
    docstring = parse(text)
    assert len(docstring.meta) == 2
    assert isinstance(docstring.meta[0], DocstringParam)
    assert isinstance(docstring.meta[1], DocstringRaises)
    assert docstring.meta[0].arg_name == "pos"
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[1].description == "If the position is invalid."
    assert docstring

# Generated at 2022-06-13 19:53:21.306103
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:53:32.605056
# Unit test for function parse

# Generated at 2022-06-13 19:53:52.029170
# Unit test for function parse
def test_parse():
    text1 = """First line of description.

Value of ``a`` defaults to 1.
    """
    text2 = """
First line of description.

Value of ``a`` defaults to 1.
    """
    text3 = """
First line of description.

:param int a: Value of a.
    """
    text4 = """
First line of description.

:param int a: Value of a.
:param str b: Value of b.
    """

    parsed = parse(text1)
    assert parsed.short_description == "First line of description."
    assert parsed.blank_after_short_description == False
    assert parsed.long_description == None
    assert parsed.blank_after_long_description == False
    assert len(parsed.meta) == 0

    parsed = parse(text2)

# Generated at 2022-06-13 19:54:04.929676
# Unit test for function parse
def test_parse():
    def func():
        """
        Short.

        Long.

        :param foo: with some description.
        :type foo: str
        :return: with some
                 description.
        :rtype: int
        :raises Exception: with some
                           description.
        :raises Exception: with some
                           description.
        """


    # test parse()
    docstring = parse(func.__doc__)
    assert docstring.short_description == "Short."
    assert docstring.long_description == "Long."
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 3
    assert docstring.meta[0].description == "with some description."
    assert docstring.meta[0].type_name

# Generated at 2022-06-13 19:54:13.015793
# Unit test for function parse
def test_parse():
    doc_obj = parse(__doc__)

# Generated at 2022-06-13 19:54:22.179211
# Unit test for function parse
def test_parse():
    doc = """Bla bla bla bla.

    :param a: This is first param
    :type a: int
    :param b: Second param
    :type b: str
    :param c: Third, with default.
        And second line for fun.
    :type c: bool
    :returns: Nothing, expected to return nothing
    :raises Nostradamus: If a great prophet appears, then this error is raised

    And a paragraph ...
    """
    res = parse(doc)
    assert res.short_description == "Bla bla bla bla."
    assert res.meta[-4].arg_name == "a"
    assert res.meta[-4].type_name == "int"
    assert res.meta[-3].arg_name == "b"

# Generated at 2022-06-13 19:54:29.802389
# Unit test for function parse

# Generated at 2022-06-13 19:54:39.952199
# Unit test for function parse
def test_parse():
    docstring = parse("""
        Short description.

        Long description.

        :param arg1: this is a first argument
        :param arg2: this is a second argument
        :param arg3: this is a third argument with a default
            defaults to end of the line.

        :type arg1: int
        :type arg2: str, optional
        :type arg3: str

        :returns: None
        :rtype: None
    """)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description

    assert len(docstring.meta) == 4
    assert docstring.meta[0].key == "param"

# Generated at 2022-06-13 19:54:52.424494
# Unit test for function parse
def test_parse():
    assert(parse("This is a test") ==
           Docstring(
               short_description="This is a test",
               blank_after_short_description=False,
               long_description=None,
               blank_after_long_description=False,
               meta=[]))

    assert(parse("This is a test\n") ==
           Docstring(
               short_description="This is a test",
               blank_after_short_description=True,
               long_description=None,
               blank_after_long_description=False,
               meta=[]))


# Generated at 2022-06-13 19:54:56.775935
# Unit test for function parse
def test_parse():
    text = """
    This is a short description.

    This is a
    long description.

    It spans multiple lines.

    :param x: This is the first parameter.
    :type x: int
    :kwarg y: This is a keyword argument.
    :type y: str
    :kwarg z: This is another keyword argument
        that does span multiple lines.
    :type z: bool
    :returns: This is what is returned.
        It spans multiple lines.
    :rtype: str
    :raises Exception: If something bad happens.
    """
    print(parse(text))
    print(type(parse(text)))

# Generated at 2022-06-13 19:55:07.067158
# Unit test for function parse
def test_parse():
    docstring = parse("""\
    My short description

    First line of long description.

    Second line of long description.
    """)
    print(docstring)

    docstring = parse("""\
    My short description.

    :param int var1: Description of var1.
    :param int var2: Description of var2.
             Description of var2 continued.

    First line of long description.

    :return: Description of return value.
    """)
    print(docstring)


# Generated at 2022-06-13 19:55:16.941217
# Unit test for function parse
def test_parse():
    assert parse("""
    Short description.

    Long description.
    """) == Docstring(
        short_description="Short description.",
        blank_after_short_description=False,
        long_description="Long description.",
        blank_after_long_description=False,
    )

    assert parse("""
    Short description.


    Long description.

    """) == Docstring(
        short_description="Short description.",
        blank_after_short_description=True,
        long_description="Long description.",
        blank_after_long_description=True,
    )


# Generated at 2022-06-13 19:55:38.502488
# Unit test for function parse
def test_parse():
    # Normal test examples
    def test_function():
        """
        Brief description of this function.

        More details.
        """
        pass

    docstring = parse(test_function.__doc__)

    assert docstring.short_description == "Brief description of this function."
    assert docstring.long_description == "More details."
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is True
    assert len(docstring.meta) == 0

    def test_function():
        """
        Brief description of this function.

        :param a: description of a
        :param b: description of b
        :type a: int
        :type b: str
        :returns: description of return value
        """
        pass


# Generated at 2022-06-13 19:55:51.119817
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("Docstring with no meta.") == Docstring(
        short_description="Docstring with no meta."
    )
    assert parse("Docstring with\n\nlong\n\ndescription.") == Docstring(
        short_description="Docstring with",
        long_description="long\n\ndescription.",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 19:55:56.307556
# Unit test for function parse
def test_parse():
    text = """
    hello

    world

    :yields: str: the text
    :param best: str: the text
    :returns: str: the text
    """
    res = parse(text)
    assert res.blank_after_long_description
    assert res.blank_after_short_description
    assert res.short_description == "hello"
    assert res.long_description == "world"

# Generated at 2022-06-13 19:56:11.950567
# Unit test for function parse
def test_parse():
    d = parse('''
    Example::

    >>> caplog.record_tuples == [
    ...     ('root', logging.CRITICAL, 'foo'),
    ...     ('root', logging.ERROR, 'bar'),
    ... ]

    :params x: Some param
    :params y: Some param
    :raises RuntimeError: if self.foo is set to true
    :returns: The result of the function
    :anywhere: something
    ''')
    assert len(d.meta) == 4
    assert d.meta[0].args == ['params', 'x']
    assert d.meta[0].description == 'Some param'
    assert d.meta[1].args == ['params', 'y']
    assert d.meta[1].description == 'Some param'

# Generated at 2022-06-13 19:56:19.343135
# Unit test for function parse
def test_parse():
    # Parse empty text
    text = ""
    ret = parse(text)
    assert ret.short_description == None
    assert ret.long_description == None
    assert ret.blank_after_short_description == False
    assert ret.blank_after_long_description == False
    assert len(ret.meta) == 0

    # Parse text with only short description
    text = "Short description."
    ret = parse(text)
    assert ret.short_description == "Short description."
    assert ret.long_description == None
    assert ret.blank_after_short_description == False
    assert ret.blank_after_long_description == False
    assert len(ret.meta) == 0

    # Parse text with short description, newline and long description
    text = "Short description.\n\nLong description."
    ret

# Generated at 2022-06-13 19:56:27.229721
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc(
    """
    This is the short description.

    This is the long description.

    :param arg_name: This is the argument description.
    :returns: This is the return description.
    :raises Exception: This is an exception description.
    """
    )
    docstring = parse(text)
    assert docstring.short_description == "This is the short description."
    assert docstring.long_description == """
    This is the long description.
    """.strip()
    assert len(docstring.meta) == 3
    assert docstring.meta[0].args == ["param", "arg_name"]
    assert docstring.meta[0].description == "This is the argument description."
    assert docstring.meta[0].arg_name == "arg_name"
    assert docstring

# Generated at 2022-06-13 19:56:35.550393
# Unit test for function parse
def test_parse():
    from . import docstring

    d = docstring.parse(
        """This is the short description.

        This is the long description.

        :param int a: This is a a
        :param str b: This is b b
        :param list[int] c: This is c c
        :param list[str] d: This is d d
        """
    )
    print(d)
    assert d.short_description == "This is the short description."
    assert d.long_description == "This is the long description."
    assert d.blank_after_short_description
    assert d.blank_after_long_description
    print("META:", d.meta)

    assert len(d.meta) == 4
    assert d.meta[0].args == ["param", "int", "a"]
    assert d.meta

# Generated at 2022-06-13 19:56:47.398100
# Unit test for function parse
def test_parse():
    text = """Parses REST-style docstring into its components.

    :param text: text of docstring
    :type text: str
    :returns: parsed docstring
    :rtype: Docstring
    :raises ParseError: when parsing fails
    """
    ds = parse(text)
    assert ds.short_description == "Parses REST-style docstring into its components."

# Generated at 2022-06-13 19:57:01.589395
# Unit test for function parse
def test_parse():
    text = """\
        Short description.

        Longer description.

        :param a: First parameter.
            This should be in the second line.
        :type a: int
        :param b: Second parameter.
        :type b: str
        :raises TypeError: if ``b`` is not a string.
        :returns: The string.
        :rtype: str
        :returns: The integer.
        :rtype: int
        :yields: The string.
        :ytype: str

        Other comments.
    """
    docstring = parse(text)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == """\
Longer description.

Other comments.
"""

# Generated at 2022-06-13 19:57:07.954636
# Unit test for function parse
def test_parse():
    text = """
Convert the source sequence of <tt>Bhamlab</tt> into a new sequence.

    :param int width: the width of the new sequence
    :param int height: the height of the new sequence
    :param bool horizontal: when ``True`` scans horizonally
    :param int rotation: the amount of rotation (in degrees)
    :raises ValueError: if the amount of rotation is not a multiple of 90
    :returns: a new sequence
"""
    ret = parse(text)


# Generated at 2022-06-13 19:57:29.366190
# Unit test for function parse
def test_parse():
    docstring = """
    blah blah blah
    bloo bloo bloo

    :param string foobar: foo bar
    :type foobar: string
    :param foobar: an integer
    :type foobar: int
    :param int max_number: your favorite number
    :param max_number: your favorite number
    :returns: None
    :return: None
    :rtype: NoneType
    :raises TypeError: if foobar is not string
    :raises: if foobar is not string
    :yields int: the next number in the sequence
    :yield int: the next number in the sequence
    :yield: the next number in the sequence
    """
    ds = parse(docstring)
    assert ds.short_description == "blah blah blah"
    assert ds.long_

# Generated at 2022-06-13 19:57:38.292150
# Unit test for function parse

# Generated at 2022-06-13 19:57:52.218953
# Unit test for function parse
def test_parse():
    if __name__ == "__main__":
        class TestDocstring(Docstring):
            def __init__(
                self,
                short_description: str,
                long_description: str,
                params: T.List[T.Tuple[str, str]] = (),
                returns: T.Optional[str] = None,
            ):
                super().__init__()
                self.short_description = short_description
                self.long_description = long_description
                returns = returns or None

# Generated at 2022-06-13 19:58:03.701189
# Unit test for function parse
def test_parse():
    assert parse('The quick brown fox jumps over the lazy dog\n') == \
           Docstring(short_description='The quick brown fox jumps over the lazy dog',
                     blank_after_short_description=True, blank_after_long_description=False,
                     long_description=None)
    assert parse('This is the one-line summary.\n\nAnd now for something completely different.\n') == \
           Docstring(short_description='This is the one-line summary.',
                     blank_after_short_description=False, blank_after_long_description=True,
                     long_description='And now for something completely different.')

# Generated at 2022-06-13 19:58:15.486122
# Unit test for function parse

# Generated at 2022-06-13 19:58:26.260623
# Unit test for function parse
def test_parse():
    assert parse("")
    # Test for when the meta chunk is missing
    assert parse("Hello World").short_description == "Hello World"
    # Test for when the meta chunk is present
    assert (
        parse("Hello World\n:returns: foo\n:raises: bar\n:tries hard: : it works")
        .long_description
        == "it works"
    )
    # Test for when the meta chunk is present

# Generated at 2022-06-13 19:58:35.612549
# Unit test for function parse
def test_parse():
    docstring = """
    Short description.
    Possibly very long description.

    :argument foo: description for foo
    :argument bar: description for bar
    :raises ValueError: if something goes wrong
    :returns: something
    """

    p = parse(docstring)

    assert p.short_description == "Short description."
    assert p.long_description == "Possibly very long description."
    assert p.blank_after_short_description == True
    assert p.blank_after_long_description == False

    assert len(p.meta) == 4

    assert isinstance(p.meta[0], DocstringParameter)
    assert p.meta[0].parameter_name == "foo"
    assert p.meta[0].description == "description for foo"

    assert isinstance(p.meta[1], DocstringParameter)

# Generated at 2022-06-13 19:58:41.582481
# Unit test for function parse
def test_parse():
    docstring = parse("Test parse function\n\n\n:param str name: Test docstring")
    assert docstring.short_description == "Test parse function"
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 1



# Generated at 2022-06-13 19:58:57.439728
# Unit test for function parse
def test_parse():
    test_case = """
    This is the very short description
    This is the long description
    This is part of the long description
    :param x: the first argument
    :param y: the second argument
    :returns: x + y
    """

    docstring = parse(test_case)
    assert(docstring.short_description == "This is the very short description")
    assert(docstring.long_description == "This is the long description\nThis is part of the long description")
    assert(docstring.blank_after_short_description == True)
    assert(docstring.blank_after_long_description == False)
    assert(docstring.meta[0].args == ['param', 'x', 'the', 'first', 'argument'])
    assert(docstring.meta[0].description == 'the first argument')


# Generated at 2022-06-13 19:59:07.769456
# Unit test for function parse
def test_parse():
    docstring = """\
        Parse the ReST-style docstring into its components.

        :param str foo: some parameter
        :param int bar?: optional parameter
        :returns: parsed docstring
        :returns: another return value
        :raises ValueError: if something goes wrong.
        :raises: another exception
        :yields: some generator stuff

        Some long description.
        """
    parsed = parse(docstring)
    assert parsed.short_description == """\
        Parse the ReST-style docstring into its components.
        """
    assert parsed.blank_after_short_description
    assert parsed.long_description == """\
        Some long description.
        """
    assert parsed.blank_after_long_description
    assert isinstance(parsed.meta[0], DocstringParam)
   

# Generated at 2022-06-13 19:59:22.863275
# Unit test for function parse
def test_parse():
    doc = inspect.getdoc(parse)
    ds = parse(doc)
    assert ds.short_description == 'Parse the ReST-style docstring into its components.'
    assert len(ds.meta) == 4
    assert ds.meta[0].arg_name == 'text'
    assert ds.meta[0].type_name == 'str'
    assert ds.meta[0].description == 'docstring to parse'
    assert ds.meta[1].arg_name == 'returns'
    assert ds.meta[1].type_name is None
    assert ds.meta[1].description == 'parsed docstring'
    assert ds.meta[2].type_name == 'ValueError'
    assert ds.meta[2].description == 'Error parsing meta information.'
    assert ds

# Generated at 2022-06-13 19:59:28.642842
# Unit test for function parse
def test_parse():
    print(parse('''
    Short description.
    
    :param int age: The person's age.
    :param str name: The person's name.
        :param float weight: The person's weight.
    :return: Death date.
    '''))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:59:35.334233
# Unit test for function parse
def test_parse():
    assert parse("""
        Single line.
        """).short_description == "Single line."
    assert parse("""
        Single line.
        """).long_description is None
    assert parse("""
        Single line.

        Multi line.
        """).long_description == "Multi line."
    assert parse("""
        Single line.

        Multi line.

        """).long_description == "Multi line."
    assert parse("""
        Single line.

        Multi line.
        """).blank_after_short_description is True
    assert parse("""
        Single line.

        Multi line.

        """).blank_after_short_description is True
    assert parse("""
        Single line.

            Multi line, with leading whitespace.
        """).long_description == "Multi line, with leading whitespace."

# Generated at 2022-06-13 19:59:42.023638
# Unit test for function parse
def test_parse():
    # """Check parse function
    #
    # Test that parse function can parse the docstring
    # without error
    # """
    test_docstring = """
    test

    :param str arg1: description
    :param arg2: description
    :return: description
    :rtype: str
    """
    docstring = parse(test_docstring)
    assert len(docstring.meta) == 3
    

# Generated at 2022-06-13 19:59:53.931020
# Unit test for function parse
def test_parse():
    test = parse(
        """
        Short description.

        Long description.
        More Long description.

        Parameters
        ----------
        a: int
            Parameter a. This is the first parameter.

        Returns
        -------
        str
            description

        """
    )
    assert test.short_description == "Short description."

    assert test.long_description == "Long description.\nMore Long description."

    assert test.blank_after_short_description == True

    assert test.blank_after_long_description == False

    assert test.meta[0].args == ["Parameters"]

    assert test.meta[0].description == "---------"

    assert test.meta[1].key == "a"

    assert test.meta[1].description == "Parameter a. This is the first parameter."

    assert test.meta[1].arg

# Generated at 2022-06-13 20:00:01.432430
# Unit test for function parse
def test_parse():
    text = """\
Return x^2.

:param str x:
:param str y:
:raises IndexError:
:returns:
:yields:
"""
    doc = parse(text)
    assert doc.short_description == "Return x^2."
    assert doc.long_description == ""
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == True
    assert len(doc.meta) == 4
    assert (
        doc.meta[0]
        == DocstringParam(
            args=["param", "str", "x"], description="", arg_name="x", type_name="str", is_optional=None, default=None
        )
    )



# Generated at 2022-06-13 20:00:11.329601
# Unit test for function parse
def test_parse():
    test = parse('''Test script

:param str name:
:returns str:
:raises ValueError:
:yields float:
''')
    assert test.short_description == 'Test script'
    assert test.long_description == None
    assert test.blank_after_short_description == True
    assert test.blank_after_long_description == False

# Generated at 2022-06-13 20:00:22.509936
# Unit test for function parse
def test_parse():
    text = """
    Args:
      arg1 (str): The first argument.
      arg2 (str, optional): The second argument. Defaults to None.
      x (int):
        The x coordinate of the point.
    Returns:
      Point: The point.
    Raises:
      ValueError: if x or y are too large or too small.
    """

    ds = parse(text)
    assert ds.short_description == 'Args: arg1 (str): The first argument. arg2 (str, optional): The second argument. Defaults to None. x (int): The x coordinate of the point. Returns: Point: The point. Raises: ValueError: if x or y are too large or too small.'
    assert ds.blank_after_short_description == True

# Generated at 2022-06-13 20:00:30.299557
# Unit test for function parse
def test_parse():
    from .examples import docstrings
    # parse docstrings with tags
    for docstring in (
        docstrings.WITH_ALL,
        docstrings.WITH_PARAM_AND_RAISES_AND_RETURNS,
        docstrings.WITH_NONE,
        docstrings.WITH_PARAM_AND_RETURNS_AND_RAISES,
    ):
        assert parse(docstring)

    # parse docstrings without tags
    for docstring in docstrings.WITHOUT_TAGS:
        assert parse(docstring)

    # parse docstrings with tags
    for docstring in docstrings.WITH_TAGS:
        assert parse(docstring)

    # parse docstrings with tags and extra spaces

# Generated at 2022-06-13 20:00:36.438082
# Unit test for function parse

# Generated at 2022-06-13 20:00:57.524524
# Unit test for function parse

# Generated at 2022-06-13 20:01:03.888112
# Unit test for function parse
def test_parse():
    import os
    import fullrst.parse

    directory = os.path.dirname(os.path.realpath(__file__))
    docstring_file = os.path.join(directory, "examples", "example.rst")
    with open(docstring_file) as fd:
        print(fullrst.parse.parse(fd.read()))


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 20:01:09.429140
# Unit test for function parse
def test_parse():
    test = """
    :param x: The first argument.
              Multiline description.
    :type x: int

    :param y: The second argument.
    :type y: int
    :returns: The answer.
    :rtype: int

    :raises ValueError: if x is negative.
    """
    expected = """
    :param x: The first argument.
              Multiline description.
    :type x: int

    :param y: The second argument.
    :type y: int
    :returns: The answer.
    :rtype: int

    :raises ValueError: if x is negative.
    """
    expected = expected.replace('\n    ', '\n')
    parsed = parse(test)
    generated = str(parsed)
    assert expected == generated
    assert parsed

# Generated at 2022-06-13 20:01:16.986995
# Unit test for function parse

# Generated at 2022-06-13 20:01:26.647955
# Unit test for function parse
def test_parse():
    example = """A short summary

    A more detailed description with multiple lines, if required.

    :param arg1: description of arg1
    :param arg2: description of arg2 which is a type.

    :returns: description of what is
    returned"""

    result = parse(example)
    assert result.short_description == "A short summary"
    assert result.blank_after_short_description == False
    assert result.long_description == "A more detailed description with multiple lines, if required."
    assert result.blank_after_long_description == False
    assert len(result.meta) == 2
    assert result.meta[0].args[0] == "param"
    assert result.meta[0].arg_name == "arg1"
    assert result.meta[0].type_name is None

# Generated at 2022-06-13 20:01:38.763468
# Unit test for function parse
def test_parse():

    def test_func():
        """Test function

        This function is used for unit testing the parse function.

        :param arg1: The first argument
        :type arg1: str
        :param arg2: The second argument
        :type arg2: int
        :raises KeyError: Raises an exception
        :rtype: str
        """
        pass

    assert str(parse(inspect.getdoc(test_func))) == "Test function\n\nThis function is used for unit testing the parse function.\n\n\nArgs:\n    arg1 (str):The first argument\n\n    arg2 (int):The second argument\n\n\nRaises:\n    KeyError: Raises an exception\n\n\nReturns:\n    str: \n"

# Generated at 2022-06-13 20:01:47.998803
# Unit test for function parse
def test_parse():
    from .common import Docstring

    s = """Main description.

This is the long description. It can go on for
a while.

:param arg1: parameter 1
:param arg2: parameter 2, defaults to a value
:param arg3: parameter 3, no defaults.
:raises Exception: it's an exception.
:raises Exception: it's another exception.
:returns: it returns nothing.
:returns: it returns something.
:yields: it yields something.

:param arg4: another parameter, defaults to a value.
:yields: it yields something else.
"""
    docstring = parse(s)