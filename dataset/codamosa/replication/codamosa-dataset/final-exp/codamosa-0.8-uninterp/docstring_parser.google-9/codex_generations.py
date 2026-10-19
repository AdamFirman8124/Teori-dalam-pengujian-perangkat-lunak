

# Generated at 2022-06-13 19:31:19.944472
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Text to parse
    text = """Short description.

Long description.

Args:
    name (str): The name.

Raises:
    ValueError: An exception occurs.

Returns:
    str: A string.
    """
    # Set to False to print result
    result_equal_to_expected = True
    # Parse text
    google_parser = GoogleParser()
    result = google_parser.parse(text)
    # Expected result

# Generated at 2022-06-13 19:31:33.080351
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:31:48.162396
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = GoogleParser()
    text = (
        "This is a class.\n"
        "\n"
        "Args:\n"
        "  arg1 (str): bla bla\n"
        "  arg2 (str, optional): ble ble. Defaults to 'HELLO'.\n"
        "  arg3 (str): bli bli.\n"
        "  arg4 (str): bla bla.\n"
        "\n"
        "Example:\n"
        "  >>> instance = Klass(my_arg1, my_arg2)\n"
        "  >>> instance.method_a(my_arg3)"
    )
    docstring = doc.parse(text)
    assert docstring.short_description == "This is a class."

# Generated at 2022-06-13 19:31:59.578870
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """This function does something.
    Parameters
    ----------
    arg1 : int
        The first argument.
    arg2 : str
        The second argument.
    arg3 : list
        The third argument.
    arg4 : list of ints
        The fourth argument.
    Returns
    -------
    int
        The return value.
    """
    p = GoogleParser()
    s = p.parse(text)
    print(s)
    assert type(s) == Docstring
    print(s.long_description)

    s = Docstring()
    s.short_description = "This function does something."

# Generated at 2022-06-13 19:32:12.387719
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test case 1
    text = """A function that does something.

    Args:
        arg1: The first argument.
        arg2 (str): The second argument.
        arg3 (:obj:`int`, optional): The third argument.
        arg4 (:obj:`list` of :obj:`int`): The fourth argument.
        arg5 (:obj:`dict`): The fifth argument.

    Returns:
        str: The return value. True for success, False otherwise.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

    Raises:
        ValueError: If `n` is equal to `None`.
    """

    # Test case 2
    # text = """A function that does something.

    # Args:
    #     arg1: The first argument

# Generated at 2022-06-13 19:32:22.975346
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    This function does something.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    docstring=parse(docstring)
    assert docstring.short_description=='This function does something.'
    assert docstring.long_description==None
    assert docstring.blank_after_short_description==True
    assert docstring.blank_after_long_description==False
    assert len(docstring.meta)==4
    for i in range(len(docstring.meta)-1):
        assert docstring.meta[i].args[0]=='param'
    assert docstring.meta[-1].args[0]=='returns'
    assert docstring

# Generated at 2022-06-13 19:32:36.674919
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_string = """Summary line.

Description. Including a list:
- 1
- 2
- 3
- 4

Args:
    - arg1
    - arg2
    - arg3
    - arg4

Attributes:
    - att1
    - att2
    - att3
    - att4

Example:
    - example1

    - example2

    - example3

Examples:
    - example4

Raises:
    - raise1
    - raise2
    - raise3
    - raise4
"""

# Generated at 2022-06-13 19:32:46.898041
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    g = GoogleParser()

    # A simple docstring, no meta
    doc = g.parse(
        """
    Short description does not apply here.
    Short description does not apply here.
    Short description does not apply here.
    """
    )
    assert doc.short_description == "Short description does not apply here."
    assert (
        doc.long_description
        == "Short description does not apply here.\nShort description does not apply here.\nShort description does not apply here."
    )
    assert not doc.meta

    # A standard docstring

# Generated at 2022-06-13 19:32:53.100793
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test for empty docstring
    docstr_empty = DocstringParser.parse("")
    assert docstr_empty.short_description is None
    assert docstr_empty.long_description is None
    assert len(docstr_empty.meta) == 0

    # Test for simple docstring
    docstr_simple = DocstringParser.parse("abc")
    assert docstr_simple.short_description == "abc"
    assert docstr_simple.long_description is None
    assert len(docstr_simple.meta) == 0

    # Test for long docstring
    docstr_long = DocstringParser.parse("abc\ndef\nghi")
    assert docstr_long.short_description == "abc"
    assert docstr_long.long_description == "def\nghi"

# Generated at 2022-06-13 19:33:04.522378
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Testing parsing with a simple, good Docstring
    print("Testing good docstring parsing:")
    good_docstring = """
    This is the short description.

    This is the long description.  It can
    span multiple lines.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value
    """
    print("the expected result is:")
    print(repr(good_docstring))
    print("the result of the GoogleParser.parse method is:")
    print(repr(GoogleParser().parse(good_docstring)))

    # Testing parsing with a bad Docstring
    print("Testing bad docstring parsing:")

# Generated at 2022-06-13 19:33:20.382099
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from . import __doc__ as doc
    from .numpydoc import NumpyDocString
    from . import google
    from . import common
    from . import numpydoc
    from . import numpy_example
    from . import rst
    from . import sphinx
    from .common import Docstring, DocstringParam, DocstringRaises, DocstringReturns, DocstringMeta, ParseError
    from typing import List, Optional, Tuple
    from enum import Enum
    import re
    import inspect
    import sys
    import typing as T
    

    def test_GoogleParser_parse0():
        # Test code
        s = NumpyDocString("test doc")
        assert (s.short_description == "test doc")
        assert (s.long_description == None)

# Generated at 2022-06-13 19:33:30.889716
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "a"
    ret = parse(text)
    assert ret.short_description == "a"
    assert ret.blank_after_short_description is False
    assert ret.long_description is None
    assert ret.blank_after_long_description is False
    assert ret.meta == []

    text = "a\nb"
    ret = parse(text)
    assert ret.short_description == "a"
    assert ret.blank_after_short_description is False
    assert ret.long_description == "b"
    assert ret.blank_after_long_description is True
    assert ret.meta == []

    text = "a\n\nb"
    ret = parse(text)
    assert ret.short_description == "a"
    assert ret.blank_after_short_description is True

# Generated at 2022-06-13 19:33:44.848903
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:33:57.001361
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Short summary.

    Long description.

    Args:
        arg1: description of 'arg1'
        arg2 (int): description of 'arg2'
        arg3 (:class:`int`, optional): description of 'arg3'
        arg4 (int, optional, default=42): description of 'arg4'. Defaults to 3.
        arg5 (int, optional, default=42): description of 'arg5'. Defaults to 'foo'

    Returns:
        description of return value
    """

    docstring = parse(text)
    assert len(docstring.meta) == 5
    assert docstring.short_description == "Short summary."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description

# Generated at 2022-06-13 19:33:59.854380
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    for docstring in [
        """
        """
    ]:
        assert parse(docstring).short_description == ""



# Generated at 2022-06-13 19:34:10.458457
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	docstring = """\
Test method.

Args:
	a: Description of a.
	b: Description of b.
	c: Description of c.
	d: Description of d.

Returns:
	Description of return value.

Raises:
	TypeError
		Description of error 1
	ValueError
		Description of error 2
"""
	expected = '''\
Test method.

Args:
	a: Description of a.
	b: Description of b.
	c: Description of c.
	d: Description of d.

Returns:
	Description of return value.

Raises:
	TypeError
		Description of error 1
	ValueError
		Description of error 2
'''
	assert_equals(GoogleParser().parse(docstring).to_string(), expected) # Does the string

# Generated at 2022-06-13 19:34:17.144023
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class A():
        def f(self, a, b=2, e= None, d=1):
            """hello
            
            print hello

            :param a: a
            :param b: b
            :type b: int
            :param c: c
            :type c: string
            :param d: d
            :param e: e?
            :type e: int
            :returns: a
            :type a: int
            """


# Generated at 2022-06-13 19:34:20.011730
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import pytest
    from darglint.google.google import GoogleParser
    assert GoogleParser().parse('') is not None

# Generated at 2022-06-13 19:34:25.847383
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	class A:
		def test(self):
			"""test(test,test,test)\n	test"""
	GoogleParser().parse(A.test.__doc__)


__all__ = [
    "DocstringMeta",
    "SectionType",
    "Section",
    "GoogleParser",
    "PARAM_KEYWORDS",
    "RAISES_KEYWORDS",
    "RETURNS_KEYWORDS",
    "YIELDS_KEYWORDS",
    "DEFAULT_SECTIONS",
]

# Generated at 2022-06-13 19:34:28.047015
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #def test_parse(self):
    # Arrange
    # Act
    # Assert
    pass

# Generated at 2022-06-13 19:34:41.339065
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    d = "TEST: Test GoogleParser.parse function\n" \
        "This is the description.\n" \
        "    Args:\n" \
        "        p (int): This is p\n" \
        "        q (int): This is q\n" \
        "    Return:\n" \
        "        r (int): This is r"
    print(d)

    p = GoogleParser()
    ret = p.parse(d)
    print(ret.short_description)
    print(ret.long_description)
    print(ret.blank_after_short_description)
    print(ret.blank_after_long_description)

    for meta in ret.meta:
        print(meta.key)
        print(meta.args)
        print(meta.description)


# Generated at 2022-06-13 19:34:51.275062
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Single-line doc string
    assert parse("Hello") == Docstring(
        short_description='Hello',
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    ) 

    # Doublle-line doc string
    assert parse("Hello\nWorld") == Docstring(
        short_description='Hello',
        long_description='World',
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

    # Multi-line doc string

# Generated at 2022-06-13 19:35:06.118620
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:35:14.644302
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    This is a sample docstring.

    Use this to test the parser.

    Args:
        this_is_the_first_arg: This is the first arg.
        this_is_the_second_arg (int): This is the second arg.
            This is continued.

    Raises:
        ValueError: If `arg_error` is not 0 or 1.

    Returns:
        int: The return value.

    """
    parser = GoogleParser()

# Generated at 2022-06-13 19:35:21.344340
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    Parses the Google-style docstring into its components.
    
    :returns: parsed docstring
    '''
    expected = Docstring(short_description="Parses the Google-style docstring into its components.", long_description='returns: parsed docstring', blank_after_short_description=True, blank_after_long_description=False, meta=[DocstringMeta(args=['returns'], description='parsed docstring')])
    assert GoogleParser().parse(text) == expected

# Generated at 2022-06-13 19:35:31.296236
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse(docstring_google) == expect_docstring_google

#========================================================
# Testing
#========================================================

docstring_google = """\
Sum values of the given name in a dictionary.

If no name is passed, the function will return None.

Args:
    dic (dict): The dictionary to be summed.

Returns:
    The sum of all occurrences of the given key.
"""


# Generated at 2022-06-13 19:35:38.501022
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    example = """
    A class for testing.

    This is the long description. It can have multiple lines.

    Example:
        >>> print('Hello World')
        'Hello World'

    Attributes:
        var (int): A variable for testing.
    """
    example2 = """
    A class for testing.

    This is the long description. It can have multiple lines.

    Examples:
        >>> print('Hello World')
        'Hello World'

    Attributes:
        var (int): A variable for testing.
    """
    missing_title = """
    This is a missing title.

    This is the long description. It can have multiple lines.

    Example:
        >>> print('Hello World')
        'Hello World'

    Attributes:
        var (int): A variable for testing.
    """

# Generated at 2022-06-13 19:35:46.024794
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_string = '''Example function with types documented in the docstring.
    
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    '''
    docstring_1 = GoogleParser().parse(doc_string)
    print(docstring_1.meta)
    print(docstring_1.short_description)
    print(docstring_1.long_description)
    print(docstring_1.blank_after_short_description)
    print(docstring_1.blank_after_long_description)

test_GoogleParser_parse()

# Generated at 2022-06-13 19:35:50.925913
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('') == Docstring()
    assert GoogleParser().parse('Test.') == Docstring(short_description='Test.', long_description=None, blank_after_short_description=False, blank_after_long_description=False)


if __name__ == "__main__":
    text = """
    :param email_address: Indicates the email address for which to query on.
        :type email_address: str
        :param entry_id: Indicates the entry_id for which to query on.
    """
    docstring = GoogleParser().parse(text)

# Generated at 2022-06-13 19:35:56.251574
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    assert parse("\n") == Docstring()
    assert parse("short\n") == Docstring(short_description="short")
    assert parse("short\nlong\n") == Docstring(
        short_description="short", long_description="long"
    )
    assert parse("short\nlong 1\nlong 2\n") == Docstring(
        short_description="short", long_description="long 1\nlong 2"
    )
    assert parse("short\n\nlong\n") == Docstring(
        short_description="short",
        blank_after_short_description=True,
        long_description="long",
        blank_after_long_description=True,
    )

# Generated at 2022-06-13 19:36:28.427575
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = 'This is a short description.\n\n'
    text += 'This is a long description.\n'
    text += 'And it is still long.\n'
    text += 'It keeps on being long.\n\n'
    text += 'Args:\n'
    text += '    arg1 (str): this is the first argument.\n'
    text += '    arg2 (int): this is the second argument\n'
    text += '        and it has multiple lines.\n'
    text += '    arg3: this is the third argument\n'
    text += '        and it also has multiple lines.\n'
    text += '        with no type specified.\n'
    text += '        This is a long description.\n'
    text += '        And it is still long.\n'

# Generated at 2022-06-13 19:36:38.275287
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	'''
	Test method parse of class GoogleParser
	'''
	parser = GoogleParser()
	
	docstring = '''Single-line short description.

Single-line long description.

Args:
  arg1: An argument.
  arg2: Another argument.

Raises:
  Exception: An exception.

Returns:
  A value.
'''
	
	docstring = parser.parse(docstring)
	print (docstring.short_description)
	print (docstring.long_description)
	print (docstring.meta[0].description)
	print (docstring.meta[0].arg_name)
	print (docstring.meta[0].args[0])
	print (docstring.meta[1].description)
	print (docstring.meta[1].type_name)
	

# Generated at 2022-06-13 19:36:46.209259
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '''
    Args:
        key: key for args1
        value: value for args2
    Params:
        key: key for params1
        value: value for params2
    Returns:
        key: key for returns1
        value: value for returns2
    '''

    parser = GoogleParser()
    docstring = parser.parse(docstring)

    assert len(docstring.meta) == 3

    assert docstring.meta[0].description == 'key for args1'
    assert docstring.meta[1].description == 'key for params1'
    assert docstring.meta[2].description == 'key for returns1'

    assert docstring.meta[0].key == 'Args'
    assert docstring.meta[1].key == 'Params'
    assert docstring.meta[2].key

# Generated at 2022-06-13 19:36:56.082953
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "test method" + '\n'+'\n'
    text += "Args:" + '\n'
    text += "    arg1: type of arg1" + '\n'
    text += "    arg2: type of arg2" + '\n'+'\n'
    text += "Returns:" + '\n'
    text += "    type of return"

    docstring = GoogleParser().parse(text)



if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:37:06.101365
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
This is the first line.

This is the second line.

Args:
    x: An integer.
    y: An optional string.

Returns:
    None
    """
    ds = GoogleParser().parse(text)
    assert ds.short_description == "This is the first line."
    assert ds.long_description == "This is the second line."
    assert ds.blank_after_short_description
    assert not ds.blank_after_long_description
    assert set(m.arg_name for m in ds.meta if isinstance(m, DocstringParam)) == {"x", "y"}
    assert set(m.type_name for m in ds.meta if isinstance(m, DocstringParam)) == {"int", "str"}

# Generated at 2022-06-13 19:37:15.774762
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Simple test case
    text = """
    A very simple function.

    A very simple function with a very long
    and long and long and long and long
    multi-line docstring.

    Attributes:
        param1 (str): The first parameter.
        param2 (str): The second parameter.
    """
    result = GoogleParser().parse(text)

    assert(result.short_description == "A very simple function.")
    assert(result.long_description == "A very simple function with a very long and long and long and long and long multi-line docstring.")
    assert(result.blank_after_short_description == False)
    assert(result.blank_after_long_description == True)
    assert(len(result.meta) == 2)

# Generated at 2022-06-13 19:37:19.019927
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse.__doc__ is not None
    # Method parse returns an instance of class Docstring
    assert isinstance(GoogleParser().parse('A simple docstring.'), Docstring)

# Generated at 2022-06-13 19:37:30.089593
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:45.635773
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Test 1
    # Description: The docstring text is empty, the parser should return a Docstring Object with all attributes set to None
    # Input: 
    # Expected output:
    #      empty_docstring = Docstring(None, None, None, None, None)
    # Actual output:
    assert GoogleParser().parse("") == Docstring(None, None, None, None, None)

    # Test 2
    # Description: The docstring text is contains only a short description text with a blank line after the short description
    # Input: 
    # Expected output:
    #      short_docstring = Docstring("docstring short description", None, None, True, False)
    # Actual output:

# Generated at 2022-06-13 19:37:53.418998
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    func_name = "test_parse_method"
    text = """\
    This is a short description.

    This is a long description.

    Attributes:
        arg1 (str): Description of `arg1`. Default is `42`.
        arg2 (int): Description of `arg2`.
    """
    actual = parser.parse(text)

    expected = Docstring()
    expected.short_description = "This is a short description."
    expected.blank_after_short_description = True
    expected.long_description = "This is a long description."
    expected.blank_after_long_description = True

# Generated at 2022-06-13 19:38:23.132117
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    Google style::

        Parses a Google-style docstring into its components.
    '''


# Generated at 2022-06-13 19:38:29.378356
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test GoogleParser.parse."""
    text = """
    Test function.

    Attributes
        attr1: test attribute 1
        attr2: test attribute 2
    
    Raises
        TestError: Test error
    """
    parser = GoogleParser()
    test_GoogleParser_parse.__name__ = "test_GoogleParser_parse"
    doc = parser.parse(text)
    assert doc.short_description == "Test function."
    assert doc.long_description == None
    assert doc.blank_after_long_description == None
    assert doc.blank_after_short_description == False
    assert len(doc.meta) == 3
    assert doc.meta[0].description == "test attribute 1"
    assert doc.meta[1].description == "test attribute 2"

# Generated at 2022-06-13 19:38:39.766684
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:55.079345
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class TestCase:
        """This is a test class.
        """

        def foo(self):
            """This is a test method.
            """

            def bar():
                """This is a test function.
                """

    class Parameter(IntEnum):
        """Recognized parameter names.

        * PARAMETERS:
        foo : str, optional
            Foo description. Defaults to None.
        bar : int
            Bar description.

        EXCEPTIONS:
        ValueError
            If invalid.
        OpenFailed
            If open failed.

        """

    class Broken(IntEnum):
        """This is a broken docstring.

        * PARAMETERS:
        foo : str, optional
            Foo description. Defaults to None.

        """

    doc_none = parse("")

# Generated at 2022-06-13 19:38:57.200970
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class Test:
        test=""
        
    Docstring = GoogleParser().parse(Test.__doc__)
    assert len(Docstring.meta) == 12
    return Docstring

# print(Docstring.meta)

# Generated at 2022-06-13 19:39:08.083032
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_str = GoogleParser().parse("""
    Short description.

    Long description.

    Args:
        arg: Argument description.
        arg2: Argument 2 description.
            Arg2 description continued.
        arg3 (int): Argument 3 description.
    Raises: ExampleException1
        If example exception is thrown.

    Example:
        Examples
        >>> foo()
        bar
    Returns:
        foo
    """)


# Generated at 2022-06-13 19:39:17.751936
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    source = '''
    This is a test docstring.

    Args:
      arg1 (str): The first argument. Defaults to "".
      arg2 (str, optional): The second argument. Defaults to "".

    Returns:
      str: The concatenated arguments.
    '''
    google = GoogleParser()
    docstring = google.parse(source)
    assert(docstring.short_description == 'This is a test docstring.')
    assert(docstring.long_description == None)
    assert(docstring.blank_after_short_description == False)
    assert(docstring.blank_after_long_description == True)
    assert(len(docstring.meta) == 3)
    assert(docstring.meta[0].description == 'The first argument. Defaults to "".')

# Generated at 2022-06-13 19:39:25.207573
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = inspect.cleandoc(
'''
        This is a sample docstring

        This is the long description.

        Args:
            arg1: This is the first argument
            arg2: This is a second argument

            This is a description that spans multiple lines

        Returns:
            This is a description of what is returned

            This is a description that spans multiple lines
        '''
    )
    print(GoogleParser().parse(text).meta[1].arg_name)
    print(GoogleParser().parse(text).meta[1].description)
    print(GoogleParser().parse(text).meta[2].arg_name)
    print(GoogleParser().parse(text).meta[2].description)
    print(GoogleParser().parse(text).meta[3].arg_name)

# Generated at 2022-06-13 19:39:32.800049
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:42.987901
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    assert google_parser.parse("") == Docstring()



# Generated at 2022-06-13 19:40:36.792945
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert_msg = "Test method parse of class GoogleParser failed"
    # Empty docstring
    empty_expected = Docstring()
    assert GoogleParser().parse(None) == empty_expected, assert_msg
    assert GoogleParser().parse("") == empty_expected, assert_msg

    # Clear docstring
    clear_expected = Docstring(
        short_description="Hello",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="",
        meta=[],
    )
    assert GoogleParser().parse("Hello") == clear_expected, assert_msg

    # Examples

# Generated at 2022-06-13 19:40:38.297538
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    GoogleParser().parse("")


# Generated at 2022-06-13 19:40:43.361170
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # {
    #     "param1": "value1"
    # },
    # {
    #     "param2": "value2"
    # },

    # {
    #     "param1": "value1",
    #     "param2": "value2"
    # }
    pass


# Generated at 2022-06-13 19:40:46.996607
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp_content = inspect.getsource(GoogleParser.parse)  # getsource lines
    num_assert = 0
    num_throws = 0
    for i in range(len(gp_content)):
        if "assert" in gp_content[i]:
            num_assert += 1
        if "throw" in gp_content[i]:
            num_throws += 1
    print("Line coverage for method parse of class GoogleParser is:")
    print(num_assert / (num_assert + num_throws))

test_GoogleParser_parse()