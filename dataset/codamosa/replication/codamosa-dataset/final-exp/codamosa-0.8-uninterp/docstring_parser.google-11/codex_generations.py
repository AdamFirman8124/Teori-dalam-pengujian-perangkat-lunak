

# Generated at 2022-06-13 19:31:20.820650
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("\n") == Docstring()
    assert GoogleParser().parse("Tests Google-style docstrings.\n") == Docstring(
        short_description="Tests Google-style docstrings.",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert GoogleParser().parse("\n    Tests Google-style docstrings.\n") == Docstring(
        short_description="Tests Google-style docstrings.",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 19:31:33.886425
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    parser = GoogleParser()
    for docstring, expected_docstring in parse_testcases:
        assert(parser.parse(docstring) == expected_docstring)

# Note:
# - The following docstring examples are taken and adapted from the
# Google docstring guide.
# - The line numbers inside docstrings refer to the official Google guide.


# Generated at 2022-06-13 19:31:48.281236
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    def function1():
        """Short description.
        Long description.

        Args:
            param1 (int): Parameter 1.
            param2 (str): Parameter 2.
        Raises:
            ValueError: When something bad happens.

        Returns:
            int: Return value.
        """

    def function2():
        """Short description.
        Long description.

        Args:
            param1 (int): Parameter 1.
            param2 (str): Parameter 2.
        Raises:
            ValueError: When something bad happens.

        Returns:
            int: Return value.
        """

    d: Docstring = GoogleParser().parse(function1.__doc__)
    assert d.short_description == 'Short description.', print(d)

# Generated at 2022-06-13 19:31:55.461320
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:32:04.790482
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import textwrap

    def check_parse(gtext, expected):
        text = textwrap.dedent(gtext).strip()
        print("\n", "-"*40, "\n", "Input:\n", text, "\n")
        if isinstance(expected, Exception):
            with pytest.raises(expected):
                GoogleParser().parse(text)
        else:
            result = GoogleParser().parse(text)
            print("Result:\n", result)
            assert result == expected

    check_parse(
"""
"""
,
        Docstring(
            short_description=None,
            long_description=None,
            blank_after_short_description=False,
            blank_after_long_description=False,
            meta=[]
        ),
    )


# Generated at 2022-06-13 19:32:07.921204
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Given a google style docstring with no new lines,
    When parse() is called
    Then return a DocString"""

    #GIVEN
    text = "This is a test string"
    Google = GoogleParser()
    
    #WHEN
    parsed = Google.parse(text)

    #THEN
    assert parsed.short_description == text



# Generated at 2022-06-13 19:32:17.330944
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse(None) == Docstring()
    assert parse("") == Docstring()
    text = """\
    Short description.

    Long description.

    Args:
        foo: description
        bar (int): description
        baz: description. Defaults to 'bar'.
    """
    docstring = Docstring(
        short_description='Short description.',
        long_description='Long description.\n\n',
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    docstring.meta.append(
        DocstringMeta(
            args=['param'],
            description='description',
        )
    )

# Generated at 2022-06-13 19:32:26.243671
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:32:38.805727
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
    A python decorator and decorator-generator to check docstrings.

    If check_returns, check_raises and check_params are true, check the
    function arguments using the function annotations and docstring.
    Otherwise, only check the docstring.

    Returns:
        A decorator or decorator-generator.
    """

    try:
        docstring = GoogleParser().parse(text)
    except Exception as e:
        raise e
    assert docstring.short_description == "A python decorator and decorator-generator to check docstrings."
    assert docstring.long_description == """\
If check_returns, check_raises and check_params are true, check the
function arguments using the function annotations and docstring.
Otherwise, only check the docstring."""
    assert docstring.blank_after

# Generated at 2022-06-13 19:32:48.447598
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser_ = GoogleParser()
    expected_text = '''Solve a linear equation system a x = b.

This is a full description of this function.

Args:
    a: coefficients matrix.
    b: independent terms vector.

Returns:
    x: solution of the linear system.
    status: status of the calculation.

Raises:
    np.linalg.LinAlgError: when matrix is singular or not square.

Examples:
    >>> a = np.array([[1,1],[1,-1]])
    >>> b = np.array([0,0])
    >>> x, status = solve(a,b)
    >>> x
    array([0, 0])
    >>> status
    'Singular matrix'
'''

# Generated at 2022-06-13 19:33:02.356981
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    g = GoogleParser()
    print("{}".format(g.parse("test docstring")))


if __name__ == "__main__":

    test_GoogleParser_parse()

# Generated at 2022-06-13 19:33:14.993924
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert(str(parse("Find the max of two nums.")) == "Docstring(short_description='Find the max of two nums.', blank_after_short_description=False, long_description=None, blank_after_long_description=True, meta=[])")
    assert(str(parse("Find the max of two nums.\nLong description.")) == "Docstring(short_description='Find the max of two nums.', blank_after_short_description=True, long_description='Long description.', blank_after_long_description=True, meta=[])")

# Generated at 2022-06-13 19:33:24.785068
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:33:33.863169
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = """\
        A one-line summary that does not use variable names or the
        function name.

        Several sentences providing an extended description.
        Refer to variables like `var1` and `var2`,
        and to functions like `func1` and `func2`.

        Args:
            arg1 (int): Description of `arg1`
            arg2 (str): Description of `arg2`
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            bool: Description of return value

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `arg2` is equal to `arg1`.

        """
    d = parser.parse(docstring)

# Generated at 2022-06-13 19:33:46.905151
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test for missing title
    test_text = """
    Short description.

    Long description.
    """
    result = GoogleParser().parse(test_text)
    assert result == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    # Test for all sections

# Generated at 2022-06-13 19:33:58.233345
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringReturns
    from .common import DocstringParam
    from .common import DocstringRaises
    from .common import DocstringMeta
    class Fn:
        """Summary.
        Args:
            a (str, optional): Description. Defaults to None.
            b (int): Description.
        Returns: Description.
        Raises: Description.
        """
        pass
    parser = GoogleParser()
    doc = parser.parse(inspect.getdoc(Fn))
    assert len(doc.meta) == 3
    assert doc.meta[0] == DocstringParam(args=['param', 'a (str, optional)'], description='Description. Defaults to None.', arg_name='a', type_name='str', is_optional=True, default='None')
    assert doc.meta[1] == Docstring

# Generated at 2022-06-13 19:34:09.403410
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:20.493115
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """test_GoogleParser_parse
    """

# Generated at 2022-06-13 19:34:27.944319
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    texto = inspect.cleandoc('''
    Construtor da classe

    Args:
        p1(str): descricao do parametro p1.
                 É um parametro longo que ocupa mais de uma linha.
        p2(int): descricao do parametro p2.
                 Defaults to 8.
    ''')
    parser = GoogleParser()
    d = parser.parse(texto)
    assert d is not None
    assert len(d.meta) == 2
    assert d.meta[0].arg_name == "p1"
    assert d.meta[0].description == "descricao do parametro p1. É um parametro longo que ocupa mais de uma linha."

# Generated at 2022-06-13 19:34:37.205896
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:53.023047
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''Summary line.

This is an extended description.

Args:
    arg1 (str): Description of `arg1`.
    arg2 (int): Description of `arg2`.

Returns:
    int. The return value.

Raises:
    KeyError: Raises an exception.
'''
    gParser = GoogleParser()

# Generated at 2022-06-13 19:35:07.814858
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from collections import OrderedDict

    test_cases = OrderedDict()
    # Test case: 1
    # A function docstring

# Generated at 2022-06-13 19:35:16.523719
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = """
    Sum two numbers.

    Multiplies two numbers and returns the result.

    Parameters
    ----------
    arg : str
        The argument to be evaluated

    Returns
    -------
    bool
        The result of the evaluation.
    """

# Generated at 2022-06-13 19:35:26.947392
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:35:30.872420
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Execute the game according to the game settings.
    """
    parser = GoogleParser()
    docstring = parser.parse(docstring)
    docstring = parser.parse("")


# Generated at 2022-06-13 19:35:36.989546
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    return

# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

# @Author: Michele Brescia <michelebrescia>
# @Date:   2019-09-30T14:00:25+02:00
# @Email:  michelebrescia93@gmail.com
# @Filename: GoogleParser.py
# @Last modified by:   michelebrescia
# @Last modified time: 2019-09-30T14:01:31+02:00
"""
Class GoogleParser
"""



# Generated at 2022-06-13 19:35:44.276267
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
            This is the short description.

            This is the long description.

            Args:
                arg1 (int): The first argument.
                arg2 (Union[int, str]): The second argument.
                arg3 (int, optional): The third argument. Defaults to 3.
                arg4 (int, optional): The fourth argument. Defaults to 4.

            Raises:
                ValueError: When any argument is negative.
                TypeError: When any argument is not an int.

            Returns:
                int: The return value.
            """

    assert parse(docstring) is not None

# Generated at 2022-06-13 19:35:47.535551
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
        This is summary
        This is description
        Args:
            arg1 (type): Description of arg1
            arg2 (type): Description of arg2
            arg3 (type): Description of arg3
        """
    print(GoogleParser().parse(text))



# Generated at 2022-06-13 19:35:56.617627
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Testing the exception raised
    try:
        text = '''\
        This is a test docstring.

        Parameters
        ----------
        value : float
            The value to be converted.
        '''
        GoogleParser().parse(text)
        assert False
    except ParseError as e:
        assert "Expected paramenter name." in str(e)

    text = '''\
This is a test docstring.

Parameters
----------
value : float
    The value to be converted.
'''

# Generated at 2022-06-13 19:35:57.107673
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass



# Generated at 2022-06-13 19:36:05.926620
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import doctest
    doctest.testmod(verbose=True)
    print('Tests Passed!')

if __name__ == '__main__':
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:36:14.731362
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text_1 = '''\
    Calculate something.

    Long description

    This will help you calculate something.

    Parameters
    ----------
    arg1 : int
        Description.
    arg2 : int
        Description.

    Returns
    -------
    int
        Description.
    '''

# Generated at 2022-06-13 19:36:25.103459
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class Example(object):
        """Short description.

        Long description.

        :param arg1: first arg description
        :param arg2: second arg description
        :param arg3: third arg description
        :param arg4: fourth arg description
        :param arg5: fifth arg description
        :type arg1: int
        :type arg5: str
        :returns: return description
        :rtype: int
        :raises Exception1: exception description
        :raises Exception2: exception description
        """
        pass

    # Test
    docstring = GoogleParser().parse(Example.__doc__)

    # Asserts
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description is True

# Generated at 2022-06-13 19:36:31.500537
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ds = """One line summary.

Extended description.

Args:
    arg1: The first argument.
    arg2: The second argument.

Returns:
    None.
"""
    print(ds)
    doc = GoogleParser().parse(ds)
    if doc:
        print(doc.meta)
    else:
        print("cannot parse doc")


# Generated at 2022-06-13 19:36:40.423786
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    args = """Arguments:
    arg1 (str): Description of arg1.
    arg2 (str): Description of arg2.
"""
    args_float = """Args:
    arg1 (str): Description of arg1.
    arg2 (str): Description of arg2.
    arg3 (float, optional): Description of arg3. Defaults to "str".
"""
    args_param = """Parameters:
    arg1 (str): Description of arg1.
    arg2 (str): Description of arg2.
"""
    args_bad = """Params:
    arg1 (str): Description of arg1.
    arg2 (str): Description of arg2.
"""

# Generated at 2022-06-13 19:36:47.651406
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    my_docstring = p.parse(
        """My description.

        Args:
            parameter_1 (float): description1
            parameter_2 (int): description2
                Continued description2
            parameter_3 (list): description3
                Continued description3
        Returns:
            bool: description4
                Continued description4
            str: description5
                Continued description5
            int: description6
                Continued description6
            float: description7
                Continued description7
            list: description8
                Continued description8
                Continued description8
        """
    )
    assert my_docstring.short_description == "My description."
    assert (
        my_docstring.meta[0].description
        == "description1\n                Continued description2"
    )

# Generated at 2022-06-13 19:36:55.695592
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Empty str
    assert(isinstance(GoogleParser().parse(""), Docstring))
    # Simple description
    assert(isinstance(GoogleParser().parse("hello"), Docstring))
    # Correct section
    assert(isinstance(GoogleParser().parse("Args:\n    arg1 (int):description"), Docstring))
    # Correct section
    assert(isinstance(GoogleParser().parse("Raises:\n    arg1 (int):description"), Docstring))


# Generated at 2022-06-13 19:37:05.821709
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    This is a google style docstring.
    This is a google style docstring.This is a google style docstring.
    This is a google style docstring.This is a google style docstring.
    This is a google style docstring.This is a google style docstring.
    This is a google style docstring.This is a google style docstring.
    This is a google style docstring.This is a google style docstring.
    This is a google style docstring.This is a google style docstring.
    This is a google style docstring.

    Args:
        x: a dummy number
        y: a dummy number
        z: a dummy number

    Returns:
        This is a google style docstring.
    """

# Generated at 2022-06-13 19:37:15.534070
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert(GoogleParser().parse(None) == Docstring())
    assert(GoogleParser().parse('') == Docstring())
    assert(GoogleParser().parse('docstring') == Docstring(short_description='docstring'))
    assert(GoogleParser().parse('docstring\nlong description') == Docstring(short_description='docstring', blank_after_short_description=True, long_description='long description', blank_after_long_description=False))
    assert(GoogleParser().parse('docstring\nlong description\n') == Docstring(short_description='docstring', blank_after_short_description=True, long_description='long description', blank_after_long_description=True))

# Generated at 2022-06-13 19:37:28.164703
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:42.702212
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "param x: x description\nparam y: y description"
    p = GoogleParser()
    d = p.parse(text)
    assert len(d.meta) == 2
    assert d.meta[0].arg_name == "x"
    assert d.meta[0].description == "x description"
    assert d.meta[1].arg_name == "y"
    assert d.meta[1].description == "y description"

# Generated at 2022-06-13 19:37:46.732379
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .numpy import NUMPY_PARSED_DOCSTRING
    print(GoogleParser().parse.__doc__)
    print(GoogleParser().parse(NUMPY_PARSED_DOCSTRING))


# Generated at 2022-06-13 19:37:53.997042
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:02.608082
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("===================")
    print("Testing GoogleParser")
    print("===================")
    text = """
    Some documentation

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.
        kwarg1 (str): A keyword argument.
    """
    # Test docstring with no description
    assert GoogleParser().parse("").short_description == None
    # Test docstring with a description
    assert GoogleParser().parse(text).short_description == 'Some documentation'
    # Test docstring with no long description
    assert GoogleParser().parse("").long_description == None
    

if __name__=="__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:38:08.802817
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

# Generated at 2022-06-13 19:38:18.931168
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    param1 = DocstringParam(
        args=["param", "c"],
        description="c should be in [0, 1].",
        arg_name="c",
        type_name="float",
        is_optional=False,
        default=None,
    )
    param2 = DocstringParam(
        args=["param", "d"],
        description="d is optional.",
        arg_name="d",
        type_name=None,
        is_optional=True,
        default=None,
    )
    param3 = DocstringParam(
        args=["param", "e"],
        description="e is optional.",
        arg_name="e",
        type_name=None,
        is_optional=True,
        default="<insert default>",
    )

# Generated at 2022-06-13 19:38:22.883499
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test():
        """A sample function.

        :param test: test param
        :param test2: test param 2
        :param test3: test param 3
        :param test4: test param 4
        :param test5: test param 5
        :returns: test returns
        :yields: test yields
        """
        pass
    parser = GoogleParser()
    return parser.parse(test.__doc__)


# Generated at 2022-06-13 19:38:29.221745
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class Foo:
        """Summary line.

        Extended description of function.

        Args:
            param1: The first parameter.
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines
              - should be formatted in long lines

            param2 (int): The second parameter.

        Returns:
            Description of return value.

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.

        """
        return



# Generated at 2022-06-13 19:38:39.712503
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """\
        Short description.

        Long description. Multiple paragraphs are allowed.

        Arguments:
        arg1 (str): Description of arg1. Defaults to None.
        arg2 (int): Description of arg2.

        Returns:
        str: Description of return value.
        """

    ds = GoogleParser().parse(docstring)

    assert ds.short_description == "Short description."
    assert ds.long_description == "Long description. Multiple paragraphs are allowed."
    assert ds.blank_after_short_description
    assert ds.blank_after_long_description

    assert len(ds.meta) == 3

    assert ds.meta[0].args == ["param", "arg1 (str)"]
    assert ds.meta[0].arg_name == "arg1"
    assert ds

# Generated at 2022-06-13 19:38:55.078960
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    description = "This is a description"
    attrs = "Attributes:\n    attr1 (int): attribute 1\n    attr2 (str): attribute 2\n"
    params = "Parameters:\n    param1 (int): param 1\n    param2 (str): param 2\n"
    returns = "Returns:\n    int: return 1\n"
    raises = "Raises:\n    ZeroDivisionError: 0\n"
    doc = description + "\n\n" + attrs + "\n" + params + "\n" + returns + "\n" + raises

    result = GoogleParser().parse(doc)

    assert result.short_description == description
    assert result.long_description == None
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == None

# Generated at 2022-06-13 19:39:22.182650
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_str0 = ""
    test_str1 = "    This is a test sting, which is not a docstring."
    test_str2 = """
    This is a one line docstring.
    
    This is a one line log description.
    """
    test_str3 = """
    This is a one line docstring.
    
    This is a one line log description.
    
    Args:
        arg1(str): This is argument one.
    """
    test_str4 = """
    This is a one line docstring.
    
    This is a one line log description.
    
    Args:
        arg1(str): This is argument one.
        
    Returns:
        out(int): This is return.
    """

# Generated at 2022-06-13 19:39:31.184852
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()

    assert GoogleParser().parse("hello world") == Docstring(
        short_description="hello world",
        blank_after_short_description=False,
        blank_after_long_description=False,
    )

    assert GoogleParser().parse("hello world\n") == Docstring(
        short_description="hello world",
        blank_after_short_description=True,
        blank_after_long_description=True,
    )

    assert GoogleParser().parse("hello world\n\nHello again") == Docstring(
        short_description="hello world",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="Hello again",
    )


# Generated at 2022-06-13 19:39:42.016756
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # 1) Test case for parsing a docstring
    docstring = """
    This is the short description.

    This is the long description.  It can even have multiple paragraphs.
    Though this gets harder to read as the docstring evolves.

    Parameters:
        arg1(str): the first argument
        arg2(str): the second argument
        arg3(str): the third argument

    Returns:
        bool: True if successful, False otherwise
        """
    obj = GoogleParser()
    docstring = obj.parse(docstring)
    assert(docstring.short_description == "This is the short description.")
    assert(
        docstring.long_description ==
        "This is the long description.  It can even have multiple paragraphs.\nThough this gets harder to read as the docstring evolves."
        )

# Generated at 2022-06-13 19:39:46.633177
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Function to add two integers.
    Args:
      a (int): First integer.
      b (int): Second integer.
    Returns:
      int: Sum of a and b.
    """
    assert parse(docstring).short_description.strip() == 'Function to add two integers.'
    assert parse(docstring).blank_after_short_description is True
    assert parse(docstring).long_description is None
    assert parse(docstring).blank_after_long_description is False
    assert parse(docstring).meta[0].description == 'First integer.'
    assert parse(docstring).meta[1].description == 'Second integer.'
    assert parse(docstring).meta[2].description == 'Sum of a and b.'

# Generated at 2022-06-13 19:39:58.089888
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    gp.add_section(Section("Arg", "arg", SectionType.MULTIPLE))
    gp.add_section(Section("Arg2", "arg2", SectionType.SINGULAR))
    gp.add_section(Section("Arg3", "arg3", SectionType.SINGULAR_OR_MULTIPLE))

# Generated at 2022-06-13 19:40:08.023281
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    text_1 = """Compute the mandelbrot sequence for a given complex
number, z.  The mandelbrot set is the set of numbers where the
mandelbrot sequence does not diverge.

Args:
    z (complex): Input complex number.

Returns:
    int: Number of iterations before the mandelbrot sequence
        diverges.

Raises:
    OverflowError: If the number of iterations before divergence
        exceeds the maximum allowed value.

"""


# Generated at 2022-06-13 19:40:17.237570
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google = GoogleParser()
    docstring = "test_GoogleParser_parse()"
    ret = google.parse(docstring)
    assert ret.short_description == "test_GoogleParser_parse()"
    assert ret.long_description == None
    assert ret.blank_after_short_description == True
    assert ret.blank_after_long_description == None
    assert len(ret.meta) == 0

    docstring = """This is a test for GoogleParser.parse().
    :param x: the x value.
    :type x: int
    :param y: the y value.
    :type y: int
    """
    ret = google.parse(docstring)
    assert ret.short_description == "This is a test for GoogleParser.parse()."
    assert ret.long_description == None
    assert ret.blank

# Generated at 2022-06-13 19:40:22.715500
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # The test is not set up properly, because we never call the parse
    # method indirectly. Therefor, we are not able to test without
    # errors and the code coverage is not measured correctly.
    parser = GoogleParser()
    docstring = parser.parse(text)
    assert docstring is not None

# Generated at 2022-06-13 19:40:28.959805
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	text = "Raises:\n    error1:\n        description of error 1\n    error2:\n        description of error 2"
	parsed_txt = Docstring(short_description=None, long_description=None, meta=[DocstringRaises(args=['raises', 'error1'], description='description of error 1', type_name='error1'), DocstringRaises(args=['raises', 'error2'], description='description of error 2', type_name='error2')])
	result = GoogleParser().parse(text)
	assert result==parsed_txt

# Generated at 2022-06-13 19:40:38.611566
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text_0 = """
    Test.
    """
    text_1 = """
    Test.

    Args:
      a: 1st param.
      b: 2nd param.
      c: 3rd param.

    Returns:
      A tuple containing:
        - x: first element
        - y: second element
    """
    docstring_1 = parser.parse(text_1)
    assert str(docstring_1) == "Test."
    assert docstring_1.short_description == "Test."
    assert docstring_1.long_description is None
    assert len(docstring_1.meta) == 4
    meta_1_a, meta_1_b, meta_1_c, meta_1_r = docstring_1.meta