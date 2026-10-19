

# Generated at 2022-06-13 19:31:42.418167
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    This unit test only covers the sections:

    - Returns
    - Yields
    - Param
    - Raises
    - type_name
    - arg_name
    - description
    """
    gp = GoogleParser()
    d = gp.parse("""
    docstring

    Args:
        arg1 (str): arg1 description.
        arg2 (str): arg2 description. Default: 'default'.
        arg3 (str, optional): arg3 description.

    Returns:
        str: something

    Yields:
        int: something

    Raises:
        ValueError: raises ValueError.
    """)

    assert d.short_description == "docstring"

    assert d.meta[0].args == ["param", "arg1 (str)"]
    assert d.meta[0].type_name

# Generated at 2022-06-13 19:31:48.683992
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse(
"""
A short description of the funciton

A longer description of the function.

This may span multiple lines
and include inline markup and other things.

Args:
    param1: The first parameter.
    param2: The second parameter.
        This may span multiple lines.

            This may include indented code.

Examples:
    This is an example of how to use this function.
        It may also include indented code.

    >>> print(x)
    42

Returns:
    Explanation of return value.
"""
    )
    assert docstring.short_description == "A short description of the funciton"

# Generated at 2022-06-13 19:31:53.198018
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class TestClass(object):
        def method_simple(self):
            """Method with a simple docstring.

            You will not find any section title.
            """
            pass

        def method_titles(self):
            """Method with some section titles.

            Arguments:
                param_a: Param a.
                param_b: Param b.
            Raises:
                TypeError: If something is wrong.
            """
            pass

        def method_titles_and_examples(self):
            """Method with some section titles and Example section.

            Arguments:
                param_a: Param a.
                param_b: Param b.
            Raises:
                TypeError: If something is wrong.
            Example:
                Example of this method.
            """
            pass


# Generated at 2022-06-13 19:32:07.292855
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test that GoogleParser can parse Google-style docstrings"""
    parser = GoogleParser()
    docstring = parser.parse("""\
        Sum two numbers.

        This function will return the sum of two numbers.

        Parameters
        ---------
        a : int
            First number.
        b : int
            Second number.

        Returns
        -------
        int
            Sum of a and b.
        """)
    assert len(docstring.meta) == 3
    assert docstring.short_description == "Sum two numbers."
    assert docstring.long_description == "This function will return the sum of two numbers."
    assert docstring.meta[0].description == "First number."
    assert docstring.meta[1].description == "Second number."
    assert docstring.meta[2].description == "Sum of a and b."

# Generated at 2022-06-13 19:32:17.051358
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
        One-line description.

        More description of the method.

        Args:
            p1 (str): Description of p1. Defaults to "".
            p2 (str): Description of p2. Defaults to "".

        Returns:
            bool: True if successful.
    '''
    # Parse a docstring according to the Google style
    docstring = GoogleParser().parse(text)
    # Check attribute short_description
    assert docstring.short_description == 'One-line description.', "Attribute short_description is not correct"
    # Check attribute long_description
    assert docstring.long_description == 'More description of the method.', "Attribute long_description is not correct"
    # Check attribute blank_after_short_description

# Generated at 2022-06-13 19:32:23.432560
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test that GoogleParser class can parse a basic docstring and returns the right type
    # This test is not important for the function itself
    assert GoogleParser().parse("This is a basic docstring.") == Docstring(
        short_description="This is a basic docstring.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[DocstringMeta(args=["summary"], description="This is a basic docstring.")],
    )


# Generated at 2022-06-13 19:32:26.808951
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from pydocstring.parsers import GoogleParser
    from pydocstring.tests import test_GoogleParser_parse as test_data
    parser = GoogleParser()
    for para in test_data:
        assert parser.parse(para) == test_data[para]
    print("Testing method parse of class GoogleParser finished")

test_GoogleParser_parse()

# Generated at 2022-06-13 19:32:39.057706
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('') == Docstring()

    assert GoogleParser().parse(
        '''
        Args:
            arg1: The first argument.
            arg2: The second argument.
        '''
    ) == Docstring(
        meta=[
            DocstringMeta(
                args=['param', 'arg1'],
                description='The first argument.'
            ),
            DocstringMeta(
                args=['param', 'arg2'],
                description='The second argument.'
            ),
        ]
    )


# Generated at 2022-06-13 19:32:48.631567
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_tp_str = r"""\
    Args:
        arg1 (str): The first argument.
        arg2 (int): The second argument.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        bool: The return value. True for success, False otherwise.
    """

# Generated at 2022-06-13 19:32:50.165840
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import doctest
    doctest.run_docstring_examples(GoogleParser.parse, globals())

# Generated at 2022-06-13 19:33:08.542650
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    ret = parser.parse("""\
        This is a description""")
    assert ret.short_description == "This is a description"
    assert ret.blank_after_long_description is True
    assert ret.blank_after_short_description is True
    assert ret.long_description is None
    assert ret.meta == []

# Generated at 2022-06-13 19:33:19.177256
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_test_1 = """Summary line.

This is a longer description of the function, which may include math and
use multiple paragraphs.

Args:
    arg1 (int): Description of arg1
    arg2 (str): Description of arg2
        This is a longer description of arg2
    arg3 (str):
        This is a longer description of arg3
        which may include math and use multiple paragraphs.
    arg4 (str): This follows the same format as arg3
    arg5 (str):
        This follows the same format as arg3:
        $$\sqrt {\frac {2} {n}}$$

Returns:
    int: Description of return value.

Raises:
    ValueError: If `arg2` is equal to `arg1`.
"""


# Generated at 2022-06-13 19:33:29.875238
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('') == Docstring()
    assert GoogleParser().parse('someText') == Docstring(short_description='someText')
    assert GoogleParser().parse('someText\n') == Docstring(short_description='someText')
    assert GoogleParser().parse('someText\n ') == Docstring(short_description='someText')
    assert GoogleParser().parse('\n someText\n') == Docstring(short_description='someText', blank_after_short_description=True)
    assert GoogleParser().parse('\n someText') == Docstring(short_description='someText', blank_after_short_description=True)
    assert GoogleParser().parse('\n someText\n ') == Docstring(short_description='someText', blank_after_short_description=True)

# Generated at 2022-06-13 19:33:32.079679
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """This function does something.
    
    Args:
        param1 (int): The first parameter.
        param2 (str, optional): The second parameter. Defaults to 'default'.
        
    Returns:
        bool: The return value. True for success, False otherwise.
    """
    print(GoogleParser().parse(text))

# Generated at 2022-06-13 19:33:38.437074
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("test") == Docstring(
        long_description=None,
        meta=[],
        short_description='test',
        blank_after_long_description=False,
        blank_after_short_description=False
    )



# Generated at 2022-06-13 19:33:44.795200
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ds = parse('Short desc\n\nLong desc\n\nArgs:\n  arg1\n  arg2\n      arg2 description.\n')
    assert(ds.meta[0] == DocstringMeta(args=['args', 'arg1'], description=None))
    assert(ds.meta[1] == DocstringMeta(args=['args', 'arg2'], description='arg2 description.'))

# Generated at 2022-06-13 19:33:49.729258
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Example of a docstring
    docstring = """Takes two numbers and adds them.

Args:
  first: First number
  second: Second number

Returns:
  Sum of two numbers
"""

    # Proper parsing by parse()
    parsed_docstring = GoogleParser().parse(docstring)

    # Expected parsing

# Generated at 2022-06-13 19:33:59.771329
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    s = 'SUMMARY\n\n    This is the summary\n\n    optional line\n\nDESCRIPTION\n\n    This is the description.\n\n    Second line\n    '
    docstring = GoogleParser().parse(s)
    assert docstring.short_description == 'SUMMARY'
    assert docstring.long_description == 'This is the description.\n\n    Second line'
    assert docstring.blank_after_long_description == True
    assert docstring.blank_after_short_description == True

    s = '\n    This is the summary\n\nDESCRIPTION\n\n    This is the description.\n    '
    docstring = GoogleParser().parse(s)
    assert docstring.short_description == 'This is the summary'

# Generated at 2022-06-13 19:34:03.694632
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Parse the Google-style docstring into its components.

    :returns: parsed docstring
    """
    print(GoogleParser().parse(text))

if __name__=='__main__':
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:34:09.204453
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:27.201423
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "This is a description.\n\nArgs:\n  arg1: description\n  arg2 (int): description\n"
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == "This is a description."
    assert docstring.long_description == "Args:\n  arg1: description\n  arg2 (int): description"
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert docstring.meta[0].description == "description"
    assert docstring.meta[0].args == ['param', 'arg1']
    assert docstring.meta[1].description == "description"
    assert docstring.meta[1].args == ['param', 'arg2 (int)']

# Generated at 2022-06-13 19:34:36.638460
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:51.767680
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class TestDocstring(Docstring):
        def __init__(self, short_desc='short description', long_desc='long description', params=None, returns=None, raises=None, attributes=None, examples=None):
            super().__init__()
            self.short_description=short_desc
            self.long_description=long_desc
            self.meta=[]
            if params:
                for p in params:
                    self.meta.append(p)
            if returns:
                self.meta.append(returns)
            if raises:
                self.meta.append(raises)
            if attributes:
                self.meta.append(attributes)
            if examples:
                self.meta.append(examples)


# Generated at 2022-06-13 19:35:02.114879
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    GoogleParser().parse("""\
        Example docstring.

        Anything after the first line is considerd the long description.

        Arguments:
            arg1: The first argument.
            arg2: The second argument.
        Returns:
            The return value. True for success, False otherwise.
        Raises:
            An exception.
        Attributes
            attr1 (str): The first attribute.
            attr2 (str): The second attribute.
        """)
    # TODO: Add more tests, to test all code paths
    assert True



# Generated at 2022-06-13 19:35:11.948638
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_text = '''
    The short description comes here.
    And then the long description.

    :param param1: The first parameter.
    :type param1: int
    :param param2: The second parameter.
    :type param2: str, optional
    :returns: The return value. True for success, False otherwise.
    :rtype: bool
    '''

    docstring = GoogleParser().parse(docstring_text)
    assert docstring.short_description == 'The short description comes here.'
    assert docstring.long_description == 'And then the long description.'
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 2

# Generated at 2022-06-13 19:35:14.022476
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert isinstance(GoogleParser().parse(""), Docstring)


# Generated at 2022-06-13 19:35:24.756160
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test for method parse of class GoogleParser
    print('executing test_GoogleParser_parse ...',end = '')
    # Test for class GoogleParser
    # Test for method parse of class GoogleParser
    target = GoogleParser()
    # command: parse(text: str) -> Docstring
    # case: input correct
    # expected returns: Docstring
    # expected output: 
    # short_description: asf
    # long_description: fas
    # blank_after_short_description: True
    # blank_after_long_description: False
    # meta: [DocstringParam(args=['params', 'dfdf: fds'], description='fadsf', arg_name='dfdf', type_name='fds', is_optional=True, default=None), DocstringReturns(args=['returns', 'fds:

# Generated at 2022-06-13 19:35:35.709294
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:35:37.920224
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .sample import sample_docstring
    from .__init__ import parse
    GoogleParser().parse(sample_docstring)
    parse(sample_docstring)
    parse("Hello, World!")

test_GoogleParser_parse()

# Generated at 2022-06-13 19:35:46.813796
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    assert parse("test") == Docstring(short_description='test')
    assert parse("test.") == Docstring(short_description='test.')

    desc = (
        "This function multiplies 2 numbers\n"
        "and writes the result to disk."
    )
    expected = Docstring(
        short_description='This function multiplies 2 numbers',
        long_description='and writes the result to disk.',
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert parse(desc) == expected
    assert parse("\n" + desc) == expected

    desc = (
        "This function multiplies 2 numbers\n\n"
        "and writes the result to disk."
    )

# Generated at 2022-06-13 19:36:03.329472
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .parser import parse

    docstring = """
    Parses a Google-style docstring into its components.

    Args:
        text (str): the docstring to parse

    Returns:
        Docstring: the parsed docstring

    Raises:
        ParseError: if the string is not a valid google docstring
    """
    d = parse(docstring)
    assert d.short_description == 'Parses a Google-style docstring into its components.'
    assert d.long_description == 'Args:\n    text (str): the docstring to parse\n\nReturns:\n    Docstring: the parsed docstring\n\nRaises:\n    ParseError: if the string is not a valid google docstring'
    assert d.meta[0].args == ['param', 'text']

# Generated at 2022-06-13 19:36:13.169905
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    assert parse("") == Docstring()
    docstring = """
    Short description.

    Long description here.
    """
    assert parse(docstring).short_description == "Short description."
    assert parse(docstring).long_description == "Long description here."

    docstring = """
    Short description.

    Long description here.


    :params:
        foo:
            Description
    """
    assert len(parse(docstring).meta) == 1
    assert parse(docstring).meta[0].args == ["params", "foo"]
    assert parse(docstring).meta[0].description == "Description"

    docstring = """
    Short description.

    Long description here.


    :returns:
        int: Description
    """
    assert len(parse(docstring).meta) == 1

# Generated at 2022-06-13 19:36:23.979161
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
Single line docstring.

Short description.

Long description.

Attributes:
    attr1 (blah): This is attr1.
    attr2 (blah): This is attr2.
    attr3 (blah): This is attr3.

Args:
    arg1 (int): This is arg1. Defaults to 42.
    arg2 (str): This is arg2. Defaults to 'hello'.
    arg3 (float): This is arg3.

Raises:
    ValueError: This is raised on bad value.
    RuntimeError: This is raised on runtime error.

Example:
    This is example.

Returns:
    int: This is return value.

"""
    ans = parse(text)
    assert ans.short_description == "Single line docstring."

# Generated at 2022-06-13 19:36:30.531163
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_function():
        """Short summary.

        Longer description.

        Args:
            a: First param
            b: Second param.
    
        Returns:
            A certain value.
    
        Raises:
            IOError: Raises an exception
        """
    docstring = inspect.getdoc(test_function)
    assert docstring == test_function.__doc__
    result = GoogleParser().parse(docstring)
    assert str(result) == docstring
    assert result.short_description=="Short summary."
    assert result.long_description=="Longer description."
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is True
    assert len(result.meta) == 3
    assert result.meta[0].description=="First param"
   

# Generated at 2022-06-13 19:36:39.484810
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:36:52.243521
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class TargetClass:
        """My Class Description

        Description of my class.

        Parameters:
            arg1 (str): Description of `arg1`. Default:-1
            arg2 (bool): Description of `arg2`.
        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
        """
        pass

    text = TargetClass.__doc__

    ret = parse(text)
    assert ret.short_description == "My Class Description"
    assert ret.blank_after_short_description
    assert ret.long_description == "Description of my class."
    assert ret.blank_after_long_description

    param_ret = ret.meta[0]
    assert param_ret.args == ["param", "arg1 (str):"]
    assert param_ret.description

# Generated at 2022-06-13 19:37:03.833209
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:14.560096
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Function that returns a string of a docstring
    def make_docstring(short_description, long_description, meta):
        s = short_description + "\n\n" if short_description else ""
        if long_description:
            s += long_description + "\n\n"
        for key, value in meta:
            s += key + ":\n"
            if value:
                s += "    " + value + "\n"
            s += "\n"
        return s

    # Actual test
    # Test default sections
    parse(make_docstring(None, None, [["Args", None]]))
    parse(make_docstring(None, None, [["Arguments", None]]))
    parse(make_docstring(None, None, [["Parameters", None]]))

# Generated at 2022-06-13 19:37:27.556135
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    assert parse("\n") == Docstring()

    assert parse("desc") == Docstring(short_description="desc")
    assert parse("desc\n") == Docstring(short_description="desc")
    assert parse("desc\n\n") == Docstring(
        short_description="desc", blank_after_short_description=True,
    )
    assert parse("desc\n\n\n") == Docstring(
        short_description="desc", blank_after_short_description=True,
    )

    assert parse("desc\nlong") == Docstring(
        short_description="desc", long_description="long"
    )
    assert parse("desc\nlong\n") == Docstring(
        short_description="desc", long_description="long",
    )
    assert parse

# Generated at 2022-06-13 19:37:35.418918
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    # Test 1
    text = "A short description.\n\n"
    "A long description."
    ret = parser.parse(text)
    assert(ret.short_description == "A short description.")
    assert(ret.long_description == "A long description.")
    assert(ret.blank_after_short_description == True)
    assert(ret.blank_after_long_description == False)
    assert(len(ret.meta) == 0)
    # Test 2
    text = "A short description.\n\n"
    "A long description.\n\n"
    "Arguments:\n"
    "  arg1: A test argument"
    ret = parser.parse(text)
    assert(ret.short_description == "A short description.")

# Generated at 2022-06-13 19:38:01.272539
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_docstring = """\
        A one-line summary that does not use variable names or the
        function name.

        Several sentences providing an extended description. Refer to
        variables like `var` and `the_function_name()` by name, since these
        are used in the examples, below.

        Args:
            arg1(int): Description of `arg1`
            arg2(str): Description of `arg2`
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            bool: The return value. True for success, False otherwise.

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `arg2` is equal to `arg1`.

        """
    test_doc_

# Generated at 2022-06-13 19:38:07.940985
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringReturns, DocstringRaises, DocstringParam, DocstringMeta

    doc = """
            Parse the Google-style docstring into its components.

            :param str text: Google-style docstring.
            :returns: parsed docstring.
            """
    google_parser_object = GoogleParser()
    ret = google_parser_object.parse(doc)

    assert ret.short_description == "Parse the Google-style docstring into its components."
    assert ret.long_description == None
    assert ret.blank_after_short_description == False
    assert ret.blank_after_long_description == True
    assert ret.meta[0] == DocstringParam("param", "text", "str", "Google-style docstring.", None, None)

# Generated at 2022-06-13 19:38:13.771172
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = """Test for method parse of class GoogleParser.

    This is a simple test for the docstring parsing.

    Args:
        a: It is a.
    """
    assert(GoogleParser().parse(doc).meta[0].args == ['a'])
    assert(GoogleParser().parse(doc).short_description == 'Test for method parse of class GoogleParser.')


# Generated at 2022-06-13 19:38:21.902497
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """Arguments:
      - arg1 (:obj:`arg1_type`, optional)
        arg1 desc. Defaults to arg1_default.
      - arg2 (:obj:`arg2_type`, optional)
        arg2 desc. Defaults to arg2_default."""
    assert parser.parse(text) == DocstringMeta(
        args=["arg1", "arg2"],
        description="arg1 desc. Defaults to arg1_default.",
        arg_name="arg1",
        type_name=":obj:`arg1_type`",
        is_optional=True,
        default="arg1_default",
    )

# Generated at 2022-06-13 19:38:35.340775
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert str(GoogleParser().parse("This is a docstring")) == """\
This is a docstring
"""
    assert str(GoogleParser().parse("This is a docstring\n")) == """\
This is a docstring
"""
    assert str(GoogleParser().parse("This is a docstring\n\n")) == """\
This is a docstring
"""
    assert str(GoogleParser().parse("This is a docstring\n\n\n")) == """\
This is a docstring
"""
    assert str(GoogleParser().parse("This is a docstring\n  \nMore...")) == """\
This is a docstring

More...
"""
    assert str(GoogleParser().parse("This is a docstring\n\nMore...")) == """\
This is a docstring

More...
"""

# Generated at 2022-06-13 19:38:43.818987
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('') == Docstring()
    assert GoogleParser().parse('   ') == Docstring()
    assert GoogleParser().parse('Hello, World!') == \
        Docstring(short_description='Hello, World!')
    assert GoogleParser().parse('Hello, World!\n') == \
        Docstring(short_description='Hello, World!')
    assert GoogleParser().parse('Hello, World!\n\n') == \
        Docstring(short_description='Hello, World!')
    assert GoogleParser().parse('Hello, World!\n\n  ') == \
        Docstring(short_description='Hello, World!')
    assert GoogleParser().parse('Hello, World!\n\nBaz') == \
        Docstring(short_description='Hello, World!', long_description='')
   

# Generated at 2022-06-13 19:38:56.090431
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:02.148453
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = """coucou
    Arguments:
        count (int): Number of things to coucou.
        braz_regex (str): Regular expression to match.
    Description of coucou method.
    """
    doc = GoogleParser().parse(doc)
    assert doc.short_description == 'coucou'
    assert doc.long_description == 'Description of coucou method.'
    assert doc.meta[0].type_name == 'int'
    assert doc.meta[0].arg_name == 'count'
    assert doc.meta[0].description == 'Number of things to coucou.'
    assert doc.meta[1].type_name == 'str'
    assert doc.meta[1].arg_name == 'braz_regex'

# Generated at 2022-06-13 19:39:11.557194
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_1 = GoogleParser().parse("")
    assert test_1.short_description == ""
    assert test_1.long_description == ""
    assert test_1.blank_after_short_description == False
    assert test_1.blank_after_long_description == False

    test_2 = GoogleParser().parse("Description")
    assert test_2.short_description == "Description"
    assert test_2.long_description == ""
    assert test_2.blank_after_short_description == False
    assert test_2.blank_after_long_description == False

    # testing with some newlines
    test_3 = GoogleParser().parse("\n")
    assert test_3.short_description == ""
    assert test_3.long_description == ""

# Generated at 2022-06-13 19:39:14.375617
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Tests for the method parse of class GoogleParser
    """
    import doctest
    doctest.testmod()

parse()

# Generated at 2022-06-13 19:39:43.371045
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def testFunction():
        """Short description.

        Long description.

        Arguments:
            arg1 (int): Short description of arg1.
            arg2 (str, optional): Short description of arg2. Defaults to 'default'.
            arg3 (str): Short description of arg3.

        Returns:
            dict: Short description of return value.

        Raises:
            ValueError: Short description of exception.
            TypeError: Short description of exception.
        """
        pass

    docstring = testFunction.__doc__
    assert "docstring" in dir()
    doc = GoogleParser().parse(docstring)
    assert isinstance(doc, Docstring)
    assert "short_description" in dir(doc)
    assert "long_description" in dir(doc)
    assert "meta" in dir(doc)

# Generated at 2022-06-13 19:39:49.757078
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_docstring = """
    Args:
        name: The file name.
        size: The maximum file size.
        offset: The starting position in the file.
        mode: The open mode.
    Returns:
        The file object(s)
    """
    parsed_docstring = GoogleParser().parse(test_docstring)

# Generated at 2022-06-13 19:40:00.204085
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    actual = GoogleParser().parse("""
    Args:
      name (str): Human readable name.
      age (int): Human age.

    Returns:
      str: A status message.
    """)

# Generated at 2022-06-13 19:40:09.153381
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser(sections=[Section("Return", "return", SectionType.SINGULAR)]).parse(
        '"""Get Blah from the blah blah.\n\nReturns the blah blah blah.\n\n"""') == Docstring(
        short_description="Get Blah from the blah blah.",
        long_description='Returns the blah blah blah.',
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[
            DocstringMeta(
                args=['return'],
                description='Returns the blah blah blah.'
            )
        ]
    )

# Generated at 2022-06-13 19:40:17.732368
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    parser = GoogleParser()
    docstring = """
    This is the first sentence. This is the description.

    Args:
        arg1 (str): The first argument.
        arg2 (str): The second argument.

    Returns:
        str: A string.
    
    """

# Generated at 2022-06-13 19:40:26.972776
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Summary line.

Keyword arguments:
    arg1 -- first argument
        more details about first argument
    arg2 -- second argument
        more details about second argument
    arg3 -- third argument
        more details about third argument

Returns:
    bool type

Raises:
    exceptions.AttributeError
    exceptions.IOError

    """
    parsed_docstring = parse(text)
    assert parsed_docstring.short_description == "Summary line."
    assert parsed_docstring.long_description == "Keyword arguments:\n    arg1 -- first argument\n        more details about first argument\n    arg2 -- second argument\n        more details about second argument\n    arg3 -- third argument\n        more details about third argument"
    assert parsed_docstring.blank_after_short_description == True
    assert parsed_docstring

# Generated at 2022-06-13 19:40:35.662729
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """A sample.
    :param int a: first param
    :type a: int
    :param int b: second param
    :type b: int
    :returns: parse docstring
    :rtype: Docstring
    """
    d = parse(text)
    text = """A sample.

    :param int a: first param
    :type a: int
    :param int b: second param
    :type b: int
    :returns: parse docstring
    :rtype: Docstring
    """
    d = parse(text)
    #assert 1 == 2

# Generated at 2022-06-13 19:40:40.783384
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test case 1
    text = """First line.
    Second line.
    Third line.

    Args:
        arg1: First argument.
        arg2: Second argument.

    Returns:
        None"""
    res = GoogleParser().parse(text)
    assert res.short_description == "First line."
    assert res.blank_after_short_description == False
    assert res.long_description == "Second line.\nThird line."
    assert res.blank_after_long_description == True
    assert len(res.meta) > 0
    assert res.meta[0].args == ["param", "arg1"]
    assert res.meta[0].arg_name == "arg1"
    assert res.meta[0].type_name == None
    assert res.meta[0].is_optional == None

# Generated at 2022-06-13 19:40:46.193132
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    title_colon = True
    if title_colon:
        colon = ":"
    else:
        colon = ""
    ret = Docstring()
    text = """
    Return a sorted list of the names available on the FTP server.
       
    Arguments:
        path (str):  Path to the directory to list (default is current dir).
       
    Returns:
        Sorted list of the names in the given directory.
       
    Raises:
        OSError: If the directory cannot be accessed.
    """
    text = inspect.cleandoc(text)
    match = re.compile("^(" + "|".join("(%s)" % t for t in DEFAULT_SECTIONS) + ")" + colon + "[ \t\r\f\v]*$").search(text)