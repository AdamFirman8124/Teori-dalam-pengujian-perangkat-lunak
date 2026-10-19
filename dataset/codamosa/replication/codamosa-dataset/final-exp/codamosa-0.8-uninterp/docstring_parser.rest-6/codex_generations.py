

# Generated at 2022-06-13 19:52:05.606310
# Unit test for function parse
def test_parse():
    docstr = """My short description.

My long description.

:param type_name arg_name: description
:returns: description"""
    assert parse(docstr) == Docstring(
        short_description="My short description.",
        blank_after_short_description=False,
        long_description="My long description.",
        blank_after_long_description=False,
        meta=[
            DocstringMeta(
                args=["param", "type_name", "arg_name"],
                description="description",
            ),
            DocstringMeta(args=["returns"], description="description"),
        ],
    )

    docstr = """My short description.

My long description.

:param type_name arg_name: description
:returns: description
:raises Exception: description"""

# Generated at 2022-06-13 19:52:21.218189
# Unit test for function parse
def test_parse():
    text = """
    This function adds two variables.
    :param x: first argument
    :type x: integer
    :param y: second argument
    :type y: integer
    :return: addition of x and y
    """
    obj = parse(text)
    assert obj.short_description == 'This function adds two variables.'
    assert obj.long_description == None
    assert obj.blank_after_short_description == True
    assert obj.blank_after_long_description == True
    assert len(obj.meta) == 2
    assert obj.meta[0].arg_name == 'x'
    assert obj.meta[0].type_name == 'integer'
    assert obj.meta[0].is_optional == None
    assert obj.meta[0].default == None

# Generated at 2022-06-13 19:52:30.424512
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("Hello, world!") == Docstring(
        short_description="Hello, world!",
        blank_after_short_description=None,
    )
    assert parse("Hello, world!\n") == Docstring(
        short_description="Hello, world!",
        blank_after_short_description=True,
    )
    assert parse("Hello, world!\n\n") == Docstring(
        short_description="Hello, world!",
        blank_after_short_description=True,
        blank_after_long_description=True,
    )

# Generated at 2022-06-13 19:52:39.338767
# Unit test for function parse
def test_parse():
    text = '''This is the short description.

This is the long description.

Returns:
    int: An integer.

This is not part of the docstring.
'''
    expected = Docstring(
        short_description="This is the short description.",
        long_description="This is the long description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[DocstringReturns(args=['Returns', 'int'], description='An integer.', type_name='int', is_generator=False)],
    )

    expected.__repr__()
    actual = parse(text)
    assert actual == expected
    assert actual.__repr__() == expected.__repr__()
    assert actual.__repr__() == expected.__repr__()



# Generated at 2022-06-13 19:52:51.080142
# Unit test for function parse
def test_parse():
    """
    Unit test for function parse
    """
    docstring = """
    short description

    longer description
    """
    d = parse(docstring)
    assert(d.short_description == "short description")
    assert(d.long_description == "longer description")
    assert(not d.blank_after_short_description)
    assert(not d.blank_after_long_description)
    assert(not d.meta)

    docstring = """
    short description
    :param x:
    """
    d = parse(docstring)
    assert(d.short_description == "short description")
    assert(not d.long_description)
    assert(not d.blank_after_short_description)
    assert(not d.blank_after_long_description)

# Generated at 2022-06-13 19:52:57.914983
# Unit test for function parse
def test_parse():
    def f() -> T.List[int]:
        """Short.

        Long.

        :param a: first
        :type a: int
        :param b: second
        :type b: int
        :raises PermissionError:
        :returns:
        :rtype: int
        """
        ...

    doctest = parse(inspect.getdoc(f))
    assert doctest.short_description == "Short."
    assert doctest.long_description == "Long."
    assert doctest.blank_after_short_description == True
    assert doctest.blank_after_long_description == False
    assert len(doctest.meta) == 3


# Generated at 2022-06-13 19:53:08.403898
# Unit test for function parse
def test_parse():
    doc = parse("""\
    A function.
    :param message: an informative message
    :param attrs: a message attribute

    :returns: the message
    :raises NotImplementedError: if the message is invalid
    """)
    assert doc.short_description == "A function."
    meta = [e for e in doc.meta]
    assert len(meta) == 3
    assert meta[0].args == ["param", "message"]
    assert meta[0].description == "an informative message"
    assert meta[1].args == ["param", "attrs"]
    assert meta[1].description == "a message attribute"
    assert meta[2].args == ["returns"]
    assert meta[2].description == "the message"

# Generated at 2022-06-13 19:53:09.873805
# Unit test for function parse
def test_parse():
    assert parse(docstring_input) == docstring_parsed


# Generated at 2022-06-13 19:53:19.649604
# Unit test for function parse
def test_parse():
    text = """Test function
    :param int x: An integer
    :param y: A parameter with no type
    :param z: A parameter with no type nor name
    :param type b: A parameter with no name
    :yields: A generator
    :yields: A generator with no type
    :returns: A return object
    :returns: A return with no type
    :raises TypeError: This fails
    :raises TypeError: This fails with no args
    :raises: This fails with no type
    """

    docstring = parse(text)
    assert docstring.short_description == "Test function"
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is None

# Generated at 2022-06-13 19:53:21.629360
# Unit test for function parse
def test_parse():
    # TODO: Use pytest to test and build unit test
    pass

# Generated at 2022-06-13 19:53:35.376832
# Unit test for function parse
def test_parse():
    doc = """The function description.

    This is a very long description.
    It can span several lines.
    And has to be indented.
    """

    ret = Docstring(
        short_description="The function description.",
        blank_after_short_description=True,
        long_description="This is a very long description.\nIt can span several lines.\nAnd has to be indented.",
        blank_after_long_description=True,
        meta=[],
    )

    assert parse(doc) == ret



# Generated at 2022-06-13 19:53:49.007821
# Unit test for function parse
def test_parse():
    text = """
    A module providing the RestructuredText-style docstring parsing.

    :param int a: A number
    :param str b: A string
        It can be a multiline string.
    :param int c: A number with a default value
        Defaults to 1.
    """
    assert text == str(parse(text))
    text = """
    A module providing the RestructuredText-style docstring parsing.

    :param int a: A number
    :param str b: A string
        It can be a multiline string.
    """
    assert text == str(parse(text))

# Generated at 2022-06-13 19:54:02.212593
# Unit test for function parse
def test_parse():
    output = parse(text="""
        Short description.

        Long description.

        :param x: the first param
        :type x: int

        :param y: the second param, defaults to 42.
        :type y: str

        :returns: a new value
        :rtype: int
    """)

    assert output.short_description == "Short description."
    assert output.long_description == "Long description."

    assert type(output.meta[0]) == DocstringParam
    assert output.meta[0].arg_name == "x"
    assert output.meta[0].description == "the first param"
    assert output.meta[0].type_name == "int"
    assert output.meta[0].default is None

    assert type(output.meta[1]) == DocstringParam

# Generated at 2022-06-13 19:54:08.681236
# Unit test for function parse
def test_parse():
    string = """One line summary.

This is a more detailed description. It can be multi
line.
:param param_1: This is parameter 1.
:type param_1: str
:param param_2: This is parameter 2.
:type param_2: int, optional
:param param_3: This is parameter 3.
:type param_3: str, optional
:param param_4: This is parameter 4.
:type param_4: list, optional
:param param_5: This is parameter 5.
:type param_5: list, optional
:raises TypeError: if something bad happens.
:return: None
:rtype: NoneType
"""
    string = inspect.cleandoc(string)
    d = parse(string)
    assert d.short_description == "One line summary."
    assert d.blank_

# Generated at 2022-06-13 19:54:19.333484
# Unit test for function parse

# Generated at 2022-06-13 19:54:27.708559
# Unit test for function parse
def test_parse():
    docstring = """
       Add the integers a and b together.
       :param int a: the first integer
       :param int b: the second integer
       :returns: the sum of a and b
       :rtype: int
       :raises ValueError: if a and b are negative
       :raises MemoryError: if the addition cannot be performed
       """
    parsed = parse(docstring)
    assert parsed.short_description == "Add the integers a and b together."
    assert parsed.long_description == "the sum of a and b\nif a and b are negative\nif the addition cannot be performed"
    assert parsed.blank_after_short_description == False
    assert parsed.blank_after_long_description == True
    assert parsed.meta[0].arg_name == 'a'
    assert parsed.meta[0].type

# Generated at 2022-06-13 19:54:33.840791
# Unit test for function parse
def test_parse():
    # Basic test
    text = """\
    A simple function
    :param x: an argument
    :returns: nothing"""
    assert parse(text) == Docstring(
        short_description="A simple function",
        meta=[
            DocstringParam(
                args=["param", "x", "an argument"],
                description="an argument",
                arg_name="x",
                type_name=None,
                is_optional=None,
                default=None,
            ),
            DocstringReturns(args=["returns", "nothing"], description="nothing"),
        ],
    )

    # Test with type annotations

# Generated at 2022-06-13 19:54:41.384908
# Unit test for function parse
def test_parse():
    doc = """Short summary.

Long description.

    :param x: The x value.
    :param y: The y value.
    :type y: int, optional
    :param z: The z value.
    :type z: int, optional
      defaults to 42.
    :returns str: Response.
    :returns: Response.
    :rtype: str
    :raises: IndexError
    """
    doc = inspect.cleandoc(doc)
    doc = parse(doc)
    assert doc.short_description == "Short summary."
    assert doc.long_description == "Long description."
    assert len(doc.meta) == 7
    assert doc.meta[0].description == "The x value."
    assert doc.meta[1].description == "The y value."

# Generated at 2022-06-13 19:54:49.039588
# Unit test for function parse
def test_parse():
    """Test parse function"""
    text = """
    Short docstring

    Long docstring.

    :param abc: Argument name
    """
    assert parse(text) == Docstring(
        short_description="Short docstring",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="Long docstring.",
        meta=[DocstringParam(args=["param", "abc"], description="Argument name")],
    )

# Generated at 2022-06-13 19:54:54.154986
# Unit test for function parse
def test_parse():
    doc = """\
    test function
    
    :param x: 
    :param y: 
    :param z: 
    """
    d = parse(doc)
    assert d.short_description == "test function"
    assert len(d.meta) == 3


# Generated at 2022-06-13 19:55:17.806925
# Unit test for function parse
def test_parse():
    # Test setup
    docstring = parse(
        """
        Short summary.

        Longer description.
        """
    )
    # Test 1 -
    assert docstring.short_description == "Short summary."
    # Test 2 -
    assert docstring.long_description == "Longer description."
    # Test 3 -
    assert docstring.blank_after_short_description
    # Test 4 -
    assert docstring.blank_after_long_description
    # Test 5 -
    assert not docstring.meta

    # Test setup

# Generated at 2022-06-13 19:55:20.355450
# Unit test for function parse
def test_parse():
    assert parse("hello") == Docstring("hello")

    text = """hello
        :param a: a
    """
    assert parse(text) == Docstring("hello", [DocstringMeta(["param", "a"], "a")])

# Generated at 2022-06-13 19:55:32.593769
# Unit test for function parse
def test_parse():

    """
    This is a test docstring.

    :param str filename: The file to open.
    :returns: The opened file.
    :raises FileNotFoundError: When the file does not exist.
    """


# Generated at 2022-06-13 19:55:40.664643
# Unit test for function parse
def test_parse():
    from os import path
    import sys
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from pdoc import __pdoc__
    fobj = __pdoc__["pdoc"]["__init__"]["parse"]
    if not fobj:
        raise AssertionError("could not find function object")
    docstring = parse(fobj.__doc__)
    print(docstring)
    print(docstring.meta)
    print(docstring.meta[0].description_lines)
    print(docstring.meta[0].description_lines[1])


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:55:46.691912
# Unit test for function parse
def test_parse():
    docstring = """Short description.

Long description.  Long description continued.

    :param foo: description of foo.
    :type foo: str
    :param baz: description of baz with a rather long type name int32, default
        defaults to 33.
    :returns: f
    :rtype: float
    :raises RuntimeError: when it is the wrong type
    :raises TypeError: when it is the wrong type
    """
    doc = parse(docstring)
    assert doc.short_description == "Short description."
    assert doc.long_description == "Long description.  Long description continued."
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == False

    assert doc.meta[0].args == ["param", "foo", "str"]
    assert doc

# Generated at 2022-06-13 19:55:57.252910
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("Hello, World!") == Docstring(
        short_description="Hello, World!",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("Hello, World!\n\nThis is a docstring.") == Docstring(
        short_description="Hello, World!",
        long_description="This is a docstring.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

    # with meta

# Generated at 2022-06-13 19:56:05.292062
# Unit test for function parse

# Generated at 2022-06-13 19:56:15.652026
# Unit test for function parse
def test_parse():
    from docstr_coverage.common import DocstringReturns
    text = """
    Sum numbers.
    
    :param int a: First number.
    :param int b: Second number.
    :rtype: int
    """

# Generated at 2022-06-13 19:56:25.225177
# Unit test for function parse

# Generated at 2022-06-13 19:56:34.908097
# Unit test for function parse

# Generated at 2022-06-13 19:56:52.163269
# Unit test for function parse
def test_parse():
    docstring = """
    Short description.

    Long description.

    :param arg1: The first argument.
    :type arg1: str
    :param arg2: The second argument.
        Defaults to 'hello'.
    :type arg2: str
    :returns: None
    :rtype: None

    .. warning::

        This is a warning.

    .. todo::

        This is a todo.

    >>> example code
    >>> more example code

    """
    doc = parse(docstring)
    print(doc.short_description)
    print(doc.long_description)
    print(doc.blank_after_short_description)
    print(doc.blank_after_long_description)
    print(doc.meta)

# Generated at 2022-06-13 19:56:57.898649
# Unit test for function parse
def test_parse():
    docstring = '''\
    This is a docstring.

    This is long description.  It is wrapped to 80 characters.
    In-line markup and references are ignored.  So are code blocks::

        print("Hello world!")

        # Hello world!!!!!!!

        print("Hello world again!")

        # Hello world again!!

    :param arg_name: argument name goes here
    :type arg_name: str
    :returns: Return value description goes here.  If multiple
       return values are present, both this and the previous
       paragraph should be used to describe each return value.
    :rtype: int
    '''
    ret = parse(docstring)
    assert ret.short_description == "This is a docstring."

# Generated at 2022-06-13 19:57:06.573713
# Unit test for function parse

# Generated at 2022-06-13 19:57:16.901597
# Unit test for function parse

# Generated at 2022-06-13 19:57:28.611039
# Unit test for function parse
def test_parse():
    assert parse("Simple short line") == Docstring(
        short_description="Simple short line",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("Simple short\nline") == Docstring(
        short_description="Simple short",
        long_description="line",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("Simple short line\n") == Docstring(
        short_description="Simple short line",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=True,
        meta=[],
    )

# Generated at 2022-06-13 19:57:38.078301
# Unit test for function parse
def test_parse():
    text = """\
    Short description.

    Long description.

    :param str arg1: First argument.
    :type arg2: int
    :param arg3:
        Third argument.
    :param bool is_true:
        True iff...
        :defaults to True.
    :param arg5: Fifth argument.
    :returns: a value.
    :return:
        Return value.
    :rtype: int
    :raises TypeError: if bad type.
    :raises: if bad.
    :raises Exception:
        If bad.
        Should use ValueError.
    :yield: a value.
    :yields: a value.
    :returns:
        Return value.
        :type: int
    :metavar: foo
    :foo: bar
    """


# Generated at 2022-06-13 19:57:52.182525
# Unit test for function parse
def test_parse():
    docstr= '''This is for executing the whole code
    :param a: int
    :param b: int
    :returns: Returns a-b
    :raises TypeError: result is not an integer
    '''

    obj=parse(docstr)
    print(obj.short_description)
    print(obj.blank_after_short_description)
    print(obj.blank_after_long_description)
    print(obj.long_description)
    print(obj.meta[0].args[0])
    print(obj.meta[0].arg_name)
    print(obj.meta[0].is_optional)
    print(obj.meta[0].type_name)
    print(obj.meta[0].default)
    print(obj.meta[0].description)

# Generated at 2022-06-13 19:58:03.701737
# Unit test for function parse
def test_parse():
    assert parse("""Return the sum of a and b.""") == Docstring(short_description='Return the sum of a and b.', blank_after_short_description=True, blank_after_long_description=False, long_description=None, meta=[])
    assert parse("""Return the sum of a and b.

    Take two numbers and return their sum.
    """) == Docstring(short_description='Return the sum of a and b.', blank_after_short_description=True, blank_after_long_description=False, long_description='Take two numbers and return their sum.', meta=[])

# Generated at 2022-06-13 19:58:15.486271
# Unit test for function parse
def test_parse():

    def parse_and_check(before: str, after: T.Dict[str, T.Any]) -> None:
        doc = parse(before)
        assert doc.short_description == after["short_description"]
        assert doc.blank_after_short_description == after["blank_after_short_description"]
        assert doc.long_description == after["long_description"]
        assert doc.blank_after_long_description == after["blank_after_long_description"]
        assert doc.meta == after["meta"]


# Generated at 2022-06-13 19:58:26.261389
# Unit test for function parse
def test_parse():
    source = '''
        :foo:
        :param arg: The function argument.
        :param arg2: The second argument.
        :returns: The return value.
        :raises Exception: If something bad happens.
        :other: Other meta.

        This is a long description.
        It is indented.

        It can include multiple paragraphs separated by blank lines.
        '''

    expected_docstring = '''
        :foo:
        :param arg: The function argument.
        :param arg2: The second argument.
        :returns: The return value.
        :raises Exception: If something bad happens.
        :other: Other meta.

        This is a long description. It is indented. It can include multiple paragraphs separated by blank lines.
        '''


# Generated at 2022-06-13 19:58:44.044389
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc("""\
    The first line is brief description.

    The second line is the long description.""")

    d = parse(text)
    assert d.short_description == "The first line is brief description."
    assert d.long_description == "The second line is the long description."
    assert d.blank_after_short_description is True
    assert d.blank_after_long_description is True

    d = parse(text + "\n")
    assert d.short_description == "The first line is brief description."
    assert d.long_description == "The second line is the long description."
    assert d.blank_after_short_description is True
    assert d.blank_after_long_description is False


# Generated at 2022-06-13 19:58:58.188461
# Unit test for function parse
def test_parse():
    test1 = """
    This is a summary.

    This is a summary.
    """
    result1 = parse(test1)
    expected1 = Docstring(
        'This is a summary.',
        'This is a summary.',
        [],
        True,
        False,
        'This is a summary.\n\nThis is a summary.',
    )
    assert result1 == expected1

    test2 = """
    This is a summary.

    :param a: Description of a.
    :type a: int
    """
    result2 = parse(test2)

# Generated at 2022-06-13 19:59:01.493539
# Unit test for function parse
def test_parse():
    doc_str = """Test function.
    :param int a: First param.
    :param int b: Second param.
    :returns: Description of return.
    """
    parse(doc_str)

# Generated at 2022-06-13 19:59:10.075227
# Unit test for function parse

# Generated at 2022-06-13 19:59:21.301343
# Unit test for function parse
def test_parse():
    text = """
    Random bits of text.
    
    :param bar: Blah blah blah.
    :param foo: Multiple
                 lines.
    :returns: Blah blah.
    """
    assert parse(text).short_description.strip() == "Random bits of text."
    assert parse(text).long_description.strip() == ""
    assert parse(text).meta[0].key == "param"
    assert parse(text).meta[0].arg_name == "bar"
    assert parse(text).meta[0].description == "Blah blah blah."
    assert parse(text).meta[1].description.strip() == "Multiple lines."
    assert parse(text).meta[2].key == "returns"
    assert parse(text).meta[2].description == "Blah blah."



# Generated at 2022-06-13 19:59:31.838562
# Unit test for function parse
def test_parse():
    docstring = parse(
        '''
    Foo short description

    Foo long description.

    :type v1: int
    :param v1: xxx
    :type v2: int
    :param v2: xxx
    :returns:
        Returns the foo of args.
        The foo of args is 1 if args[0] == args[1] else -1.
    :rtype: int
    '''
    )
    # print(docstring)
    # print(docstring.long_description)
    # print(docstring.short_description)
    # print(docstring.blank_after_short_description)
    # print(docstring.blank_after_long_description)
    # print(docstring.meta)
    assert docstring.long_description == "Foo long description."
    assert doc

# Generated at 2022-06-13 19:59:42.244850
# Unit test for function parse

# Generated at 2022-06-13 19:59:54.208007
# Unit test for function parse
def test_parse():
    docstring = r"""
    Parse the ReST-style docstring into its components.

    :param aaaaaaaaa: comment a
    :param bbbbbbbbb: comment b
    :param ccccccccc: comment c
    :returns: comment d

    this is a very long paragraph
    that spans multiple lines
    whatever...

    :yields: comment e
    :raises xxxxxxxx: comment f
    :raises yyyyyyyy: comment g
    :param hhhhhhhhh: comment h

    :returns: comment i
    """

# Generated at 2022-06-13 20:00:06.540843
# Unit test for function parse
def test_parse():
    docstring1 = """
    A short description for a function.

    A longer description for a function.

    :param arg1: This is the first argument of the function.
    :type arg1: int
    :param arg2: This is the second argument of the function. This argument
        has a description that extends to more than one line.
    :param arg3: This is the third argument of the function.
    :param arg4: This is the fourth argument of the function.
    :returns: This is the return value

    :Example:

    >>> test_parse()

    """

# Generated at 2022-06-13 20:00:19.214548
# Unit test for function parse

# Generated at 2022-06-13 20:00:35.057576
# Unit test for function parse
def test_parse():
    """Test that parse() can successfully parse a docstring."""
    docstring = """
    This is a test :param this_is_a_parameter: Description.
    :param optional_parameter: Description. defaults to None.
    :raises ValueError: Description
    :returns: Description
    """
    d = parse(docstring)
    assert d.short_description == "This is a test"
    assert d.long_description is None
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False

    assert len(d.meta) == 3
    assert d.meta[0].description == "Description."
    assert d.meta[0].arg_name == "this_is_a_parameter"
    assert d.meta[0].type_name is None
   

# Generated at 2022-06-13 20:00:45.805057
# Unit test for function parse
def test_parse():
    text = """
    This is the short description.

    This is the long description.

    :param int arg1: An integer argument
    :param arg2: A regular argument
    :keyword kw1: A keyword argument, defaults to True.
    :keyword kw2: A keyword argument, defaults to None.
    :type kw1: bool
    :returns: An integer
    :rtype: int
    :raises ValueError: Raised when something bad happens
    """
    ds = parse(text)
    assert ds.short_description == "This is the short description."
    assert ds.long_description == "This is the long description."
    assert ds.blank_after_short_description
    assert ds.blank_after_long_description
    assert len(ds.meta) == 6

# Generated at 2022-06-13 20:00:56.161735
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring()
    assert parse('short') == Docstring(short_description='short')
    assert parse('short\nlong') == Docstring(
        short_description='short',
        long_description='long',
        blank_after_short_description=False,
        blank_after_long_description=False,
    )
    assert parse('short\n\n    long') == Docstring(
        short_description='short',
        long_description='long',
        blank_after_short_description=True,
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 20:01:04.429832
# Unit test for function parse
def test_parse():
    doc_string = "hello"
    assert parse(doc_string).short_description == "hello"

    doc_string = """hello
    hello2"""
    assert parse(doc_string).short_description == "hello"
    assert parse(doc_string).long_description == "hello2"

    doc_string = """hello

    hello2"""
    assert parse(doc_string).short_description == "hello"
    assert parse(doc_string).long_description == "hello2"

    doc_string = """hello
        hello2"""
    assert parse(doc_string).short_description == "hello"
    assert parse(doc_string).long_description == "hello2"

    doc_string = "hello\n        hello2"
    assert parse(doc_string).short_description == "hello"

# Generated at 2022-06-13 20:01:14.352209
# Unit test for function parse
def test_parse():
    docstring_example = '''
    Test function for docstring parsing.

    Because Docstrings are awesome!
    
    :param s: something cool
    :param n: how cool it is
    :param b: weather or not we like it
    :rtype: dumbo
    :returns: something amazing
    :raises: ValueError if something goes wrong
    '''
    docstring = parse(docstring_example)
    assert docstring.short_description == 'Test function for docstring parsing.'

    assert docstring.meta[0].args == ['param', 's', 'something cool']
    assert docstring.meta[1].args == ['param', 'n', 'how cool it is']
    assert docstring.meta[2].args == ['param', 'b', 'weather or not we like it']


# Generated at 2022-06-13 20:01:20.041809
# Unit test for function parse
def test_parse():
    docstring = """
    Calculate the sum of two integers.

    :param int x: The first number.
    :param int y: The second number.
    :param int z: The third number.
    :returns: The sum of the given numbers.
    :raises TypeError: If any of the given numbers are not integers.
    """

    parsed_docstring = parse(docstring)

    assert parsed_docstring.short_description == "Calculate the sum of two integers."
    assert parsed_docstring.long_description == """
    The first number.
    The second number.
    The third number.
    The sum of the given numbers.
    If any of the given numbers are not integers.
    """


# Generated at 2022-06-13 20:01:25.243542
# Unit test for function parse
def test_parse():
    from .test_fixtures import DOCSTRING_TO_PARSE

    parsed_docstring = parse(DOCSTRING_TO_PARSE)
    print(parsed_docstring)
    assert parsed_docstring.long_description == "This is a long description"
    assert parsed_docstring.short_description == "This is a docstring"

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 20:01:37.170729
# Unit test for function parse
def test_parse():
    def f(a, b="foo"):
        """Short description.
        :param a: first parameter.
        :type a: str
        :param b: second parameter. Defaults to "foo"
        :type b: str
        :raises: ValueError
        :raises: TypeError
        :raises: IndexError
        :raises: ValueError
        :returns: the result
        :rtype: str
        :yields: something
        :yields: something else
        :yield: another thing
        :yield: yet another thing
        :return a list of str
        """
        # do nothing
        pass

    docstring = parse(inspect.getdoc(f))
    assert docstring.short_description == "Short description."
    assert docstring.blank_after_short_description is False

# Generated at 2022-06-13 20:01:41.577922
# Unit test for function parse
def test_parse():
    doc = """
    Get and Set the object onto the stack.
    :param obj: Object to place on the stack
    :type obj: obj
    :raises RuntimeError: If the object is not a valid type
    :returns: True on success
    """
    parsed = parse(doc)
    assert parsed.short_description == "Get and Set the object onto the stack."
    assert parsed.long_description == ":param obj: Object to place on the stack\n:type obj: obj\n:raises RuntimeError: If the object is not a valid type\n:returns: True on success"
    assert parsed.meta[0].key == "param"
    assert parsed.meta[0].arg_name == "obj"
    assert parsed.meta[0].type_name == "obj"

# Generated at 2022-06-13 20:01:51.433052
# Unit test for function parse
def test_parse():
    docstring = parse(
        '''First line.
        Second line.

        :param name: The name.
        :type name: string
        :param address: The address.
        :type address: string
        :returns: Return.
        :rtype: string
        '''
    )
    assert docstring.short_description == 'First line.'
    assert docstring.long_description == 'Second line.'
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 3
    assert str(docstring.meta[0]) == ":param name: The name."
    assert str(docstring.meta[1]) == ":param address: The address."