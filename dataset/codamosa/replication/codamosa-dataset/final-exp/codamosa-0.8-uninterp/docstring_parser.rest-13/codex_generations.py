

# Generated at 2022-06-13 19:52:21.983878
# Unit test for function parse
def test_parse():
    text = """
    This is a function.

    This is a description.

    :param param: description
    :type param: str
    :return: description
    :rtype: int
    :returns: description
    :yields: description
    """

    doc = parse(text)

    print("short_desc: {0}".format(doc.short_description))
    print("long_desc: {0}".format(doc.long_description))
    print("meta[0]: {0}".format(doc.meta[0]))
    print("meta[1]: {0}".format(doc.meta[1]))
    print("meta[2]: {0}".format(doc.meta[2]))
    print("meta[3]: {0}".format(doc.meta[3]))

# Generated at 2022-06-13 19:52:24.493053
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc("""
    This function does some stuff.

    :param one: this is the first parameter
    :param two: and this is the second

    :returns: the result of the stuff
    """)
    ret = parse(text)
    assert str(ret) == text

# Generated at 2022-06-13 19:52:34.350216
# Unit test for function parse
def test_parse():
	docstring='''
	"""
	Here's a test function

	testing parse function
	:param int a: parameter a
	:param int b: parameter b
	:returns int: The sum of a and b
	"""
	'''
	a=parse(docstring)
	assert a.short_description == "Here's a test function"
	assert a.long_description == "testing parse function"
	assert a.blank_after_short_description == True
	assert a.blank_after_long_description == True
	tup1 = DocstringParam(None,None, None, None, None, None)
	tup2 = DocstringParam(None,None, None, None, None, None)
	tup1.args = ['param', 'int', 'a']

# Generated at 2022-06-13 19:52:46.117486
# Unit test for function parse
def test_parse():
    text = '''
    Some short description.

    This is the long description.

    :param str arg1: Argument 1.
    :param str arg2: Argument 2.
    :raises ValueError: In case of error.
    :yields: A boolean.
    :returns: Answer.
    '''

    str_meta = '''
    :param str arg1: Argument 1.
    :param str arg2: Argument 2.
    :raises ValueError: In case of error.
    :yields: A boolean.
    :returns: Answer.
    '''

# Generated at 2022-06-13 19:52:51.594716
# Unit test for function parse
def test_parse():
    def do_test(docstring, should_pass=True):
        try:
            r = parse(docstring)
            if not should_pass:
                raise RuntimeError('should_pass is False')
        except ParseError:
            if should_pass:
                raise

    do_test('', True)
    do_test(' ', True)

    do_test('single-line docstring', True)
    do_test('single-line docstring\n', True)
    do_test('single-line docstring\n\n', True)
    do_test('\nsingle-line docstring', True)
    do_test('\nsingle-line docstring\n', True)
    do_test('\nsingle-line docstring\n\n', True)


# Generated at 2022-06-13 19:52:59.312091
# Unit test for function parse
def test_parse():
    """Simple test function"""
    doc = parse(inspect.cleandoc(test_parse.__doc__))
    assert doc.short_description == "Simple test function"
    assert doc.long_description == "This is a test function.\n"


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Test the ReST parser.")
    parser.add_argument(
        "func",
        help="Function to test. For example: tests.test_rest.test_parse",
    )
    args = parser.parse_args(sys.argv[1:])

    module_name, func_name = args.func.rsplit(".", 1)
    mod = __import__(module_name, fromlist=["foo"])

# Generated at 2022-06-13 19:53:07.484069
# Unit test for function parse
def test_parse():
    s = """
        Parse the ReST-style docstring into its components.

        :returns: parsed docstring
        :rtype: cli.parsing.Docstring
        """
    parsed = parse(s)
    assert parsed.short_description == "Parse the ReST-style docstring into its components."
    assert len(parsed.meta) == 1
    assert parsed.meta[0].args == ['returns']
    assert parsed.meta[0].description == 'parsed docstring'
    assert isinstance(parsed.meta[0], DocstringReturns)


# Generated at 2022-06-13 19:53:18.244856
# Unit test for function parse

# Generated at 2022-06-13 19:53:31.764017
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    assert parse("\n") == Docstring()
    assert parse("\n\n\n") == Docstring()
    assert parse("this is short\n") == Docstring(
        short_description="this is short"
    )
    assert parse("this is short\n\n") == Docstring(
        short_description="this is short",
        blank_after_long_description=True,
    )
    assert parse("thi\n\n\n\n") == Docstring(
        short_description="thi",
        blank_after_short_description=True,
    )

# Generated at 2022-06-13 19:53:45.927947
# Unit test for function parse

# Generated at 2022-06-13 19:54:05.648043
# Unit test for function parse
def test_parse():
   # string to feed to parse()
   s = """\
   This is some sample docstring.

   :param str arg_name: arg description
   :param arg_name: arg description

   :returns: return description
   :rtype: str
   :return: return description
   :yield: yield description
   :yields: yield description
   :raises TypeError: raises description
   :raises: raises description
   :keyword: meta description
   :keyword arg_name: meta description

   Long description.
   """

   # expected elements
   expected_short_description = "This is some sample docstring."
   expected_blank_after_short_description = False
   expected_long_description = "Long description."
   expected_blank_after_long_description = True

# Generated at 2022-06-13 19:54:13.223268
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    docstring = """Shuffle items in a list in-place.

Get a new shuffled list using:
shuffled_list = random.sample(mylist, len(mylist))

This is a shallow copy.

"""
    doc = parse(docstring)
    assert doc.short_description == "Shuffle items in a list in-place."
    assert doc.blank_after_short_description is True
    assert doc.blank_after_long_description is False
    assert doc.long_description == """Get a new shuffled list using:
shuffled_list = random.sample(mylist, len(mylist))

This is a shallow copy."""
    assert doc.meta == []

# Generated at 2022-06-13 19:54:22.251375
# Unit test for function parse
def test_parse():
    doc1 = """\
    short_description__
    long_description__
    """
    parsed1 = parse(doc1)
    assert parsed1.short_description == "short_description"
    assert parsed1.long_description == "long_description"
    assert parsed1.blank_after_short_description is True
    assert parsed1.blank_after_long_description is True
    assert parsed1.meta == []

    doc2 = """\
    short_description
    :param a: 1
    :param b: 2
    :return: 3
    :rtype: 4
    """
    parsed2 = parse(doc2)
    assert parsed2.short_description == "short_description"
    assert parsed2.long_description == None
    assert parsed2.blank_after_short_description is True

# Generated at 2022-06-13 19:54:26.536848
# Unit test for function parse
def test_parse():
    d = parse('''
:param string prompt: The prompt displayed to the user.(defaults to "Selection: ")
:raises RuntimeError: If no valid choice was made
:returns: The choice made by the user
    ''')
    # print(d)
    for i in d.meta:
        print(i.arg_name)


# Generated at 2022-06-13 19:54:38.426612
# Unit test for function parse
def test_parse():
    docstring = \
    """Short desc.

    Long desc.

    :param type arg: arg desc with ``code``
    :param int arg2: arg2 desc
    :return: returns desc with ``code``
    :raises type error: raises desc

    Extended description.
    """
    print(docstring)
    docstring = parse(docstring)
    print(docstring)
    print(docstring.meta)
    for meta in docstring.meta:
        print(meta)
    print()


    docstring = "No desc."
    print(docstring)
    docstring = parse(docstring)
    print(docstring)
    print(docstring.meta)
    for meta in docstring.meta:
        print(meta)
    print()

    docstring = "No desc.\n\n"

# Generated at 2022-06-13 19:54:52.425759
# Unit test for function parse
def test_parse():
    text = """
    This is a short description.

    This is a long
    description.

    :param x: This is a parameter.
    :type x: str
    :param y: This is another parameter.
    :type y: bool

    :param (str, bool) z: This is a tuple parameter.
    :type z: (str, bool)

    :returns: This is what is returned.
    :rtype: str

    :return: This is also what is returned.
    :rtype: bool?
    """

    docstring = parse(text)
    assert docstring.short_description == "This is a short description."
    assert docstring.long_description == "This is a long\ndescription."
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long

# Generated at 2022-06-13 19:55:02.056990
# Unit test for function parse
def test_parse():
    docstring = '''
    This is the short description.

    This is the long
    description. It is
    split into
    multiple
    lines.
    And it comes
    before the meta
    tags.

    :key arg description
    :key arg description
    :key arg description

    The long description continues
    here'''

    expected = '''This is the short description.

This is the long description. It is split into multiple lines. And it comes before
the meta tags.

:key arg description
:key arg description
:key arg description

The long description continues here'''

    final = inspect.cleandoc(docstring)
    assert final == expected

# Generated at 2022-06-13 19:55:10.300055
# Unit test for function parse
def test_parse():
    assert parse("""This is a
    test docstring.
    """).short_description == 'This is a test docstring.'

    assert parse("""This is a test docstring.

    And this is the continuation.
    """).short_description == 'This is a test docstring.'

    assert not parse("""This is a test docstring.

    And this is the continuation.
    """).blank_after_short_description

    assert parse("""This is a test docstring.

    And this is the continuation.
    """).long_description == 'And this is the continuation.'

    assert not parse("""This is a test docstring.

    And this is the continuation.
    """).blank_after_long_description


# Generated at 2022-06-13 19:55:19.752530
# Unit test for function parse

# Generated at 2022-06-13 19:55:32.063294
# Unit test for function parse
def test_parse():
    """
    Test docstring parsing.
    """
    from .common import Docstring
    assert parse(None) == Docstring()

    d = parse(
        """\
        This is a test docstring.
        The title will be above it.
        """
    )
    assert d.short_description == "This is a test docstring."
    assert (
        d.long_description
        == 'The title will be above it.\n\n'
        'The title will be above it.'
    )

    d = parse(
        """\
        This is a test docstring.

        The title will be above it.
        """
    )
    assert d.short_description == "This is a test docstring."

# Generated at 2022-06-13 19:55:36.590156
# Unit test for function parse
def test_parse():
    ret = parse('hello\nworld')
    print(ret)

# Generated at 2022-06-13 19:55:49.013001
# Unit test for function parse
def test_parse():
    """Test the validity of function parse.

    :returns: None
    """
    # Test empty string
    assert parse("") == Docstring()

    # Test short description only
    assert parse("Hello world").short_description == "Hello world"

    # Test short description + blank line + long description
    docstring = parse("Hello world\n\nfoobar")
    assert docstring.short_description == "Hello world"
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.long_description == "foobar"

    # Test short description + long description
    docstring = parse("Hello world\nfoobar")
    assert docstring.short_description == "Hello world"
    assert not docstring.blank_after_short_description
    assert docstring.blank_

# Generated at 2022-06-13 19:55:55.652510
# Unit test for function parse
def test_parse():
    from .common import Docstring
    from .common import DocstringMeta
    from .common import DocstringParam
    from .common import DocstringRaises
    from .common import DocstringReturns


# Generated at 2022-06-13 19:56:00.683017
# Unit test for function parse
def test_parse():
    """Test parse

    :returns: None
    """
    docstr = """Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    """
    doc = parse(docstr)
    assert len(doc.meta) == 1

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:56:12.277825
# Unit test for function parse
def test_parse():
    doc = parse("""\
    Foo func.

    :param x: X value
    :param y: Y value
    :return: the result
    :raises ValueError: when bad things happen
    """)

    assert doc.short_description == "Foo func."
    assert doc.long_description == "X value\nY value\nthe result\nwhen bad things happen"
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description
    assert doc.meta[0].arg_name == "x"
    assert doc.meta[0].args == ["param", "x"]
    assert doc.meta[0].description == "X value"
    assert doc.meta[0].is_optional is None
    assert doc.meta[0].type_name is None

# Generated at 2022-06-13 19:56:19.422857
# Unit test for function parse
def test_parse():
    # Testing if we can import parse
    # Successful if there is no error
    print("Test #1: Testing if we can import parse")
    try:
        import doct
        doct.core.parse
        print("OK")
    except:
        print("Failed")
    # Testing if the parse function works
    # Successful if there is no error
    print("Test #2: Testing if the parse function works")

# Generated at 2022-06-13 19:56:29.848331
# Unit test for function parse
def test_parse():
    docstring = """
    Test Docstring
    :param int code: Code of response
    :param str message:
    :rtype: str
    :returns: test string
    """
    doc_parsed = parse(docstring)
    assert doc_parsed.short_description == "Test Docstring"
    assert doc_parsed.long_description == None
    assert doc_parsed.blank_after_short_description == False
    assert doc_parsed.blank_after_long_description == None
    assert len(doc_parsed.meta) == 2
    assert doc_parsed.meta[0].args == ["param", "int", "code"]
    assert doc_parsed.meta[0].description == "Code of response"

# Generated at 2022-06-13 19:56:42.051211
# Unit test for function parse
def test_parse():
  assert parse("") == Docstring()
  assert parse("foobar") == Docstring(
      short_description="foobar", long_description=None, meta=[]
  )
  assert parse("foo\nbar") == Docstring(
      short_description="foo",
      long_description="bar",
      blank_after_short_description=False,
      blank_after_long_description=True,
      meta=[],
  )
  # This is an unusual ReST-style docstring.

# Generated at 2022-06-13 19:56:53.495588
# Unit test for function parse
def test_parse():
    assert parse("Hello World") == (
        "Hello World",
        None,
        False,
        False,
        []
    )

    assert parse("Hello World\n") == (
        "Hello World",
        None,
        False,
        False,
        []
    )

    assert parse("Hello World\n\n") == (
        "Hello World",
        None,
        True,
        False,
        []
    )

    assert parse("Hello World\n\nHello World\n") == (
        "Hello World",
        "Hello World",
        False,
        False,
        []
    )

    assert parse("Hello World\n\nHello World\n\n") == (
        "Hello World",
        "Hello World",
        False,
        True,
        []
    )

   

# Generated at 2022-06-13 19:57:04.377589
# Unit test for function parse
def test_parse():
    docstring = '''
Sample module docstring

:param first_param: This is the first parameter.
:param second_param: This is the second parameter.
:returns: None
:raises SomeException: When an exception is raised.
:raises OtherException: When another exception is raised.
This line should be ignored, when calculating the long description.
'''

    doc = parse(docstring)
    assert doc.short_description == "Sample module docstring"
    assert doc.long_description == "This line should be ignored, when calculating the long description."
    assert len(doc.meta) == 4
    assert doc.meta[0].arg_name == "first_param"
    assert doc.meta[1].arg_name == "second_param"
    assert doc.meta[2].type_name == "None"
    assert doc

# Generated at 2022-06-13 19:57:11.236345
# Unit test for function parse

# Generated at 2022-06-13 19:57:18.777083
# Unit test for function parse
def test_parse():
    from .common import Docstring

    # test empty docstring
    assert parse("") == Docstring()

    # test short docstring
    assert parse("short desc") == Docstring(
        short_description="short desc",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    # test long docstring
    assert parse("short desc\n\nlong desc") == Docstring(
        short_description="short desc",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="long desc",
        meta=[],
    )

    # test long docstring with extra blank line
    assert parse("short desc\n\nlong desc\n\n") == Docstring

# Generated at 2022-06-13 19:57:30.016941
# Unit test for function parse
def test_parse():
    text = """
        Short description

        Long description.

        :param x: parameter x
        :type x: int
        :param y: parameter y
        :type y: int
        :returns: returns something.
        :rtype: str
        :raises ZeroDivisionError: if something goes wrong.
    """
    doc = parse(text)
    assert doc.short_description == "Short description"
    assert doc.blank_after_short_description == False
    assert doc.long_description == "Long description."
    assert doc.blank_after_long_description == False
    assert len(doc.meta) == 4
    # First one is a parameter
    meta_param = doc.meta[0]
    assert isinstance(meta_param, DocstringParam)
    assert meta_param.arg_name == "x"


# Generated at 2022-06-13 19:57:34.219874
# Unit test for function parse
def test_parse():
    docstring = """
    This is a first line
    This is second line

    :param arg1: This is some arg1
    :param arg2: This is another arg2
    :returns: The return
    """

    parsed = parse(docstring)
    print(parsed.meta[0])
    assert parsed.meta[0].arg_name == "arg1"


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:57:48.476533
# Unit test for function parse
def test_parse():
    docstring = """
        Short description.

        Long description.

        :param type_name arg_name:
        :param type_name? arg_name:
        :param type_name? arg_name: Defaults to value.
        :param type_name? arg_name:
        Defaults to value.

        :returns:
        :returns type_name:
        :returns type_name: long description
        """

    doc = parse(docstring)
    test_docstring = Docstring()
    test_docstring.short_description = "Short description."
    test_docstring.long_description = "Long description."

# Generated at 2022-06-13 19:57:52.754941
# Unit test for function parse
def test_parse():
    doc_string = """
    Converts a Python value to Json.
    :param data: the Python value to convert to Json.
    :returns: the corresponding Json value.
    :raises
    """
    r = parse(doc_string)
    # print(r.meta)


# Generated at 2022-06-13 19:58:04.689834
# Unit test for function parse
def test_parse():
    text = """
    Short description.

    Long description.

    :param type_name arg_name: argument description.
    :param type_name arg_name: argument description.
    :raises type_name: exception description.
    :returns: return description.
    :yields: yield description.
    """
    docstring = parse(text)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert len(docstring.meta) == 4
    assert docstring.meta[0].arg_name == "type_name"
    assert docstring.meta[0].type_name == "arg_name"

# Generated at 2022-06-13 19:58:15.966128
# Unit test for function parse
def test_parse():
    doc = r"""
    Test function.

    :param x:
        x value.
    :param y:
        y value. defaults to (1 + x).
    :type y: int
    :param z: (optional)
        z value. defaults to 7.
    :type z: int
    :returns:
        x + y
    """
    result = parse(doc)

    assert result.short_description == "Test function."
    assert result.long_description == "x value.\ny value. defaults to (1 + x)."
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == True
    assert len(result.meta) == 4


# Generated at 2022-06-13 19:58:20.050873
# Unit test for function parse

# Generated at 2022-06-13 19:58:27.463326
# Unit test for function parse
def test_parse():
    docstring = """This is the short description of the function.
    This is the second line of the short description.
    
    
    
    
    
    
    
    
    
    
    
    
    
    And this is the first line of the long description.


    """
    assert(parse(docstring).short_description=='This is the short description of the function.')
    assert(parse(docstring).long_description=='And this is the first line of the long description.')
    assert(len(parse(docstring).meta)==0)


# Generated at 2022-06-13 19:58:41.838100
# Unit test for function parse
def test_parse():
    assert parse(
        """\
    This is a test.
    """
    ) == Docstring()

    assert parse(
        """\
    This is a test.

    And this is the second
    line.
    """
    ) == Docstring(
        short_description="This is a test.",
        blank_after_short_description=True,
        long_description="And this is the second\nline.",
        blank_after_long_description=False,
        meta=[],
    )


# Generated at 2022-06-13 19:58:57.528975
# Unit test for function parse
def test_parse():
    text = """\
This is a test function.

    :param user_id: A unique user id.
    :type user_id: int
    :param lastname: A user last name.
    :returns: A user full name.
"""

# Generated at 2022-06-13 19:59:07.769363
# Unit test for function parse

# Generated at 2022-06-13 19:59:20.125003
# Unit test for function parse
def test_parse():
    test_input = """
    Docstring for function.

    :param id: The ID of the user.
    :type id: str
    :param is_admin: Whether the user is an admin.
    :type is_admin: bool
    :param children: The user's children.
    :type children: List[User]
    :param email: The user's email.
    :type email: str
    :param meta: Dict[str, Any]
    :returns: User
    :rtype: User
    :raises ValueError: If the user cannot be found.
    :yields User: The users that match the params.
    :returns: The user that matches the params.
    """

# Generated at 2022-06-13 19:59:31.000252
# Unit test for function parse
def test_parse():
    import io
    
    text_fun_1 = """
    Array construction from slices.

    :param ???: xfbuffers for which to create a vector view.
    :type ???: List[int], int, or None
    """

    text_fun_2 = """
    Check if the kernel is using a GPU or not.

    :rtype: bool
    """

    text_fun_3 = """
    Returns default values for all the arguments to the program

    :param xf.graph.Program program: program generated by the API
    :returns: default values for the given program
    :rtype: List[Tensor]
    """


# Generated at 2022-06-13 19:59:41.372730
# Unit test for function parse
def test_parse():
    docstring_text = """
    Args:
        arg1: arg1 arg1 arg1
        arg2 (int): arg2 arg2 arg2"""
    docstring = parse(docstring_text)
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == ['arg1']
    assert docstring.meta[0].description == 'arg1 arg1 arg1'
    assert docstring.meta[0].is_optional is None
    assert docstring.meta[0].type_name is None
    assert docstring.meta[0].default is None
    assert docstring.meta[0].is_generator is False
    assert docstring.meta[1].args == ['arg2', 'int']
    assert docstring.meta[1].description == 'arg2 arg2 arg2'
    assert doc

# Generated at 2022-06-13 19:59:53.048751
# Unit test for function parse
def test_parse():
    text = """
        Sums two numbers together and returns the result.

        :param arg1: The first number.
        :type arg1: float

        :param arg2: The second number.
        :type arg2: float

        :param arg3: The second number.
        :type arg3: float

        :returns: The sum of the two numbers.
        :rtype: float
    """
    res = parse(text)

    print(res.short_description)
    print(res.meta)
    print(res.meta[0].__dict__)
    print(res.meta[1].__dict__)
    print(res.meta[2].__dict__)
    print(res.meta[3].__dict__)

    assert res.short_description == "Sums two numbers together and returns the result."


# Generated at 2022-06-13 19:59:58.043299
# Unit test for function parse
def test_parse():
    doc = parse.__doc__
    assert doc
    print(doc)

doc = parse.__doc__
print(doc)
assert doc

if __name__ == "__main__":
    print(sys.argv[0], "will create no output, but assert a failure")
    print("Use last lines of output above to verify this.")
    print("Run with -v to see bootstrap output as well.")

# Generated at 2022-06-13 20:00:08.793508
# Unit test for function parse
def test_parse():
    text = """
    This is the short description

    This is the longer
    description

    :param arg1: This is the first argument
    :param arg2: This is the second
    :type arg2: str
    :param arg3: This is the third argument.
    :type arg3: list
    :type arg4: numpy.ndarray


    """

# Generated at 2022-06-13 20:00:20.582132
# Unit test for function parse
def test_parse():
    """
    >>> docstring = parse("""

# Generated at 2022-06-13 20:00:31.229152
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
    A short description.

    A long description.

    :param arg1: The first argument.
    :type arg1: int
    :param arg2: The second argument.
    :param arg3: The third argument. This argument has no type.
    :type arg3:
    :returns: The return value.
    :rtype: Object
    """
    )

    assert docstring.short_description == "A short description."
    assert docstring.blank_after_short_description is True
    assert docstring.long_description == "A long description."
    assert docstring.blank_after_long_description is False

    params = docstring.params
    assert len(params) == 3
    assert params[0].arg_name == "arg1"
    assert params[0].type_

# Generated at 2022-06-13 20:00:37.063078
# Unit test for function parse
def test_parse():
    text = \
"""Python 2.

This is a long description which provides additional information
unavailable in the short description.

:param str name: long description of the parameter name
:param bool is_env: defaults to False.

:param bool is_true: True or False
:returns: None or something else
:raises ValueError: when something is wrong.
"""
    ds = parse(text)
    assert ds.short_description == "Python 2."
    assert ds.blank_after_short_description == True
    assert ds.long_description == "This is a long description which provides additional information unavailable in the short description."
    assert ds.blank_after_long_description == False


# Generated at 2022-06-13 20:00:46.915932
# Unit test for function parse
def test_parse():
    docstring = """Summarize a number
    This is the "long" description.

    :param x: the number to be summarized
    :type x: int | str
    :param y: the other number to be summarized
    :type y: int | str
    :param operator: the operator to apply
    :type operator: str
    :return: the answer
    :rtype: int | float
    :raises: a custom exception if x is invalid
    :raises: a custom exception if y is invalid
    :raises: a custom exception if operator is invalid
    """
    parsed_docstring = parse(docstring)
    assert parsed_docstring.short_description == 'Summarize a number'
    assert parsed_docstring.long_description == 'This is the "long" description.'

# Generated at 2022-06-13 20:00:57.801552
# Unit test for function parse
def test_parse():
    # this was a bug in the original code, now fixed
    text = parse(r'''
    This docstring has no meta-data.
    ''')
    assert text.short_description == 'This docstring has no meta-data.'
    assert text.long_description == None
    assert text.blank_after_short_description == False
    assert text.blank_after_long_description == True
    assert text.meta == []

    # minimal docstring
    text = parse(r'''
    This docstring has a :returns:`return` meta-data.
    ''')
    assert text.short_description == 'This docstring has a :returns:`return` meta-data.'
    assert text.long_description == None
    assert text.blank_after_short_description == True
    assert text.blank_after

# Generated at 2022-06-13 20:01:05.930285
# Unit test for function parse
def test_parse():
    # example docstring
    d = """\
    short description line

    more detailed description
    :param v: initial velocity
    :type v: float
    :param t: time
    :type t: float
    :return: distance travelled
    :rtype: float
    """
    print(parse(d))
    print(parse(d).short_description)
    print(parse(d).long_description)
    print(parse(d).blank_after_short_description)
    print(parse(d).blank_after_long_description)
    print(parse(d).meta)


# Generated at 2022-06-13 20:01:11.733006
# Unit test for function parse
def test_parse():
    ds = """
    Function to bla bla.

    :param arg1: The first argument.
    :type arg1: int
    :param arg2: The second argument.
    :type arg2: str, optional
    :raises KeyError: raises an exception
    :returns:
    :rtype: int
    """
    print(parse(ds))



# Generated at 2022-06-13 20:01:18.457434
# Unit test for function parse
def test_parse():
    rst_docstring = """\
    The short description of the function.
    
    The long description of the function.
    
    :param foo: Description of foo.
    :param bar: Description of bar.
    :returns: Description of the return value.
    :raises ValueError: Description of the exception.
    """
    docstring = parse(rst_docstring)
    assert docstring.short_description == "The short description of the function."
    assert docstring.long_description == "The long description of the function."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.meta[0].args == ["param", "foo"]

# Generated at 2022-06-13 20:01:27.619512
# Unit test for function parse

# Generated at 2022-06-13 20:01:39.854490
# Unit test for function parse
def test_parse():
    docstring = """Test function for docstring parsing

    This function is used for testing the parsing of docstrings.
    """

    parsed_docstring = parse(docstring)

    assert parsed_docstring.short_description == "Test function for docstring parsing"
    assert parsed_docstring.long_description == "This function is used for testing the parsing of docstrings."
    assert parsed_docstring.blank_after_short_description is False
    assert parsed_docstring.blank_after_long_description is False


# Generated at 2022-06-13 20:01:50.198411
# Unit test for function parse
def test_parse():
    doc = parse(
        """
        The FooBar class.

        This is the long description.

        :param x: parameter x
        :type x: int
        :param y: parameter y
        :type y: int
        :returns: x + y
        :rtype: int
        :raises ValueError: if x is negative
        """
    )

    assert doc.short_description == "The FooBar class."
    assert (
        doc.long_description
        == "This is the long description.\n\n:param x: parameter x\n:type x: int\n:param y: parameter y\n:type y: int\n:returns: x + y\n:rtype: int\n:raises ValueError: if x is negative"
    )
    assert doc.blank_after_short_description