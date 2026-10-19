

# Generated at 2022-06-13 19:31:14.574493
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:31:26.946245
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    code = inspect.cleandoc(
        """
        Short summary.

        Args:
            Optional:
                foo: foo is a required param.
            Optional (default=7):
                bar: bar is an optional param. Defaults to 7.
            Optional (default=None):
                baz: baz is an optional param. Defaults to None.
            Optional (default=False):
                biz: biz is an optional param. Defaults to False.
            Optional (default=True):
                buz: buz is an optional param. Defaults to True.

        Returns:
            Return type
    """
    )
    ret = GoogleParser().parse(code)
    assert ret.short_description == "Short summary."
    assert ret.meta[0].args == ["returns", "Return type"]

# Generated at 2022-06-13 19:31:38.584762
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # case 1
    doc = """
    This is a fake docstring.

    Parameters
    ----------
    a: int
        Hello.
    """
    result = parse(doc)
    assert result.short_description == "This is a fake docstring."
    assert result.long_description == None
    assert result.blank_after_short_description == False
    assert result.blank_after_long_description == False
    assert len(result.meta) == 1
    assert result.meta[0].args == ['param', 'a: int']
    assert result.meta[0].arg_name == 'a'
    assert result.meta[0].description == 'Hello.'
    assert result.meta[0].type_name == 'int'
    assert result.meta[0].default == None
    assert result.meta[0].is_

# Generated at 2022-06-13 19:31:50.770667
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    google_docstring
        Short description.
    
        Long description.
    
        Args:
            arg1 (str): The first argument.
            arg2 (str, optional): The second argument. Defaults to 'arg2'.
        Raises:
            SomeError: If some condition.
        Returns:
            str: The return value.
    """

# Generated at 2022-06-13 19:32:02.711146
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = """
    This function adds two numbers

    Args:
        a: first number
        b: second number

    Returns:
        Sum of the two numbers
    """
    assert parser.parse(docstring).short_description == "This function adds two numbers"
    assert parser.parse(docstring).blank_after_short_description == True
    assert parser.parse(docstring).blank_after_long_description == True
    assert parser.parse(docstring).long_description == "Args:\n\t a: first number\n\t b: second number\n\nReturns:\n\t Sum of the two numbers"


# Generated at 2022-06-13 19:32:04.797656
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse."""
    parser = GoogleParser()
    docstring = parser.parse("\nThe quick brown fox jumped over the lazy dog.\n")
    # print(docstring)
    

# Generated at 2022-06-13 19:32:15.789974
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Function XYZ
Params:
    a: This is the first parameter. Defaults to 0.
    b: This is the second parameter.
Returns:
    booleans: This is the return value.
"""
    parser = GoogleParser()
    docstring = parser.parse(text)
    assert docstring is not None
    assert docstring.short_description == "Function XYZ"
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 2
    assert docstring.meta[0].key in ['param']
    assert docstring.meta[0].args[0] == 'param'

# Generated at 2022-06-13 19:32:31.434530
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    out = parser.parse("""\
        Do stuff.

        Args:
            param1 (str): The first parameter.
            param2 (list): The second parameter.
            param3 (str, optional): The third parameter. Defaults to 'default'.

        Returns:
            str: The return value.
            int: Another return value.

        Raises:
            ValueError: If `param2` is equal to `param1`.

        Example:
            Examples can be given using either the ``Example`` or ``Examples``
            sections. Sections support any reStructuredText formatting, including
            literal blocks::

                $ python example_google.py

        Examples:
            Examples should be written in doctest format, and should illustrate how
            to use the function/class.
            >>>
        """)
    assert out == Docstring

# Generated at 2022-06-13 19:32:37.837427
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Documentation for the function.
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        A string
    Raises:
        KeyError: Raises an exception."""
    
    res = GoogleParser().parse(text)
    assert res.short_description == "Documentation for the function."
    assert res.long_description == None

# Generated at 2022-06-13 19:32:47.658217
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test(text, expected):
        actual = GoogleParser().parse(text)
        assert actual == expected
    #
    # Normal examples

# Generated at 2022-06-13 19:33:05.089807
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # no docstring
    assert None == GoogleParser().parse(None)
    assert None == GoogleParser().parse("")
    assert None == GoogleParser().parse("  ")
    docstring = GoogleParser().parse("\n")
    assert None == docstring.short_description
    assert None == docstring.long_description
    assert [] == docstring.meta
    docstring = GoogleParser().parse("\n\n")
    assert None == docstring.short_description
    assert None == docstring.long_description
    assert [] == docstring.meta
    docstring = GoogleParser().parse("\n\n\n")
    assert None == docstring.short_description
    assert None == docstring.long_description
    assert [] == docstring.meta

    # single-line docstring

# Generated at 2022-06-13 19:33:09.811050
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    result =  GoogleParser().parse("""
    Args:
        a: An integer argument.

    Returns:
        A string describing the argument.
    """)
    #assert result == expected_result
    print(f"{repr(result)} is instance of {type(result)}")



# Generated at 2022-06-13 19:33:10.805449
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()

# Generated at 2022-06-13 19:33:11.546147
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass

# Generated at 2022-06-13 19:33:20.955384
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """This is a test docstring

    This is a test docstring.

    Arguments:
        arg1 (int): Description of arg1.
        arg2: Description of arg2.

    Raises:
        ValueError: if something is wrong.

    Returns:
        int: Description of return value.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> a = [1, 2, 3]
        >>> print [x + 3 for x in a]
        [4, 5, 6]
        >>> print "a\n\nb"
        a
        b
    """
    docstring = GoogleParser().parse(text)

# Generated at 2022-06-13 19:33:31.370062
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''\
    Google style docstring

    This is the description of the function.
    It can have multiple lines.

    Args:
        param1 (str): The first parameter.
        param2 (str): The second parameter.

    Returns:
        str: Description of return value.
    '''
    result = GoogleParser().parse(text)


# Generated at 2022-06-13 19:33:45.216840
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test case 1
    gs = GoogleParser()
    text = "test text_1"
    ds = gs.parse(text)
    assert ds.__str__() == f"""short description: test text_1
long description: None
blank after short description: False
blank after long description: False
meta:
    examples: None""".strip()
    
    # test case 2
    gs = GoogleParser()
    text = "test text_2\n\n\nexamples:\n  test text_3"
    ds = gs.parse(text)
    assert ds.__str__() == f"""short description: test text_2
long description: None
blank after short description: False
blank after long description: False
meta:
    examples: test text_3""".strip()

    # test case 3


# Generated at 2022-06-13 19:33:57.205399
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Unit test for method parse of class GoogleParser
    """
    parser = GoogleParser(title_colon=True)
    docstring = """
    Some short summary.
    Some long summary.

    Arguments:
        arg_1 (str): Some description for arg_1.
        arg_2 (str): Some description for arg_2. Defaults to None.

    Args:
        arg_3 (int): Some description for arg_3.
        arg_4 (int): Some description for arg_4. Defaults to None.

    Raises:
        ValueError: Unable to parse docstring.

    """
    print(parser.parse(docstring))
    #<docstring.Docstring object at 0x10aa5c5f8>

# Generated at 2022-06-13 19:34:08.905027
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('') == Docstring()
    assert GoogleParser().parse(' ') == Docstring()
    assert GoogleParser().parse(None) == Docstring()

    # parse multiline docstrings
    docstring = '''
        This is a doc string.

        This is the long description.
        It should be indented with spaces.
    '''
    assert GoogleParser().parse(docstring) == Docstring(
        short_description='This is a doc string.',
        blank_after_short_description=True,
        long_description='This is the long description.\nIt should be indented with spaces.',
        blank_after_long_description=False,
        meta=[],
    )

    # parse multiline docstrings with blank line after short description

# Generated at 2022-06-13 19:34:19.599928
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:37.592476
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Example 1
    docstring = """
        First line is short description.

        This is where the long description goes. It can span multiple lines.
    
        Args:
            arg1 (str): Description for arg1
            arg2 (:obj:`int`, optional): Description for arg2
    
        Returns:
            bool: Description of return value
    
        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.
    """
    result = GoogleParser(title_colon=True).parse(docstring)
    assert result.short_description == "First line is short description."

# Generated at 2022-06-13 19:34:43.710903
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:53.494411
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    method_input = """Summary line.

Extended description.

Args:
    arg1 (str): Description of arg1
    arg2 (bool): Description of arg2. Defaults to False.
    arg3 (:obj:`int`): Description of arg3

Returns:
    bool: Description of return value.

"""
    method_output = GoogleParser().parse(method_input)
    # assert method_output.short_description == "Summary line."
    # assert method_output.long_description == "Extended description."
    # assert method_output.meta[1].args == ['param', "    arg2 (bool): Description of arg2. Defaults to False."]
    # assert method_output.meta[1].description == "Description of arg2."
    # assert method_output.meta[1].arg_name == "

# Generated at 2022-06-13 19:35:08.326697
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = "type: int\n\
                 description: This is a description"
    doc = GoogleParser().parse(docstring)
    assert doc.short_description == "type: int"
    assert doc.long_description == "description: This is a description"

    docstring = "type: int\n\
                 description: This is a description\n\
                 next_desc: Next description"
    doc = GoogleParser().parse(docstring)
    assert doc.short_description == "type: int"
    assert doc.long_description == "description: This is a description\nnext_desc: Next description"

    docstring = "type: int\n\n\
                 description: This is a description\n\
                 next_desc: Next description"
    doc = GoogleParser().parse(docstring)
    assert doc.short_

# Generated at 2022-06-13 19:35:17.061380
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringParam, DocstringRaises, DocstringReturns, DocstringMeta

# Generated at 2022-06-13 19:35:21.174731
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    Singular section.

    Multiple
    params:

        add(int, opt: int = 1): Add two numbers together. Defaults to 1.

        subtract(int, int): Subtract the second from the first.

    '''
    assert  isinstance(GoogleParser().parse(text), Docstring)

# Generated at 2022-06-13 19:35:31.209114
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser(title_colon=True)
    docstring = parser.parse('This is a function.\n\n'
                             'Args:\n'
                             '\tparam1: This is a param.\n'
                             '\tparam2: This is another param.\n\n'
                             'Returns:\n'
                             '\tbool: This is a return.')
    assert len(docstring.meta) == 4
    assert docstring.meta[0].args == ['short_description']
    assert docstring.meta[1].args == ['long_description']
    assert docstring.meta[2].args == ['param', 'param1']
    assert docstring.meta[3].args == ['returns', 'bool']


# Generated at 2022-06-13 19:35:48.084099
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def fun(a,*args,**kwargs):
        """Parse the Google-style docstring into its components.

        :returns: parsed docstring

        Arguments:
          a: parameter a
          *args: args
          **kwargs: kwargs

        Raises:
          ValueError: If a is not 1.

        Example:
          >>> fun(1)
          None
        """
        pass

    expected = parse(inspect.getdoc(fun))

    actual = GoogleParser().parse(inspect.getdoc(fun))
    assert expected.short_description == actual.short_description
    assert expected.long_description == actual.long_description
    assert expected.blank_after_short_description == actual.blank_after_short_description
    assert expected.blank_after_long_description == actual.blank_after_

# Generated at 2022-06-13 19:35:57.094106
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:36:03.942522
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:36:35.523529
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass

# Generated at 2022-06-13 19:36:37.133866
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert True == False

# Generated at 2022-06-13 19:36:45.681638
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test of parsing a docstring
    # GoogleParser.parse(text: str)
    def my_function():
        """
        This is a summary
        section

        Args:
            arg_1: This is a description. Defaults to True
            arg_2 (int): This is a description

        Returns:
            Something

        Raises:
            Something
        """

    parser = GoogleParser()
    result = parser.parse(my_function.__doc__)

# Generated at 2022-06-13 19:36:58.570140
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring=r"""        Compute the a priori phases and amplitudes of the
        interaction matrix.

        Arguments:
            G (numpy.ndarray): the interaction matrix

        Returns:
            tuple: the a priori phases and amplitudes in the format
                (phases, amplitudes)

        Raises:
            ValueError: if G is not a square matrix
        """
    gp=GoogleParser()
    docstring=gp.parse(docstring)
    assert docstring.short_description=='Compute the a priori phases and amplitudes of the'
    assert docstring.meta[0].args[1]=='G (numpy.ndarray)'
    assert docstring.meta[0].description=='the interaction matrix'
    assert docstring.meta[1].args[1]=='tuple'

# Generated at 2022-06-13 19:37:07.031916
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Summary line.

    Extended description.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Return description
    """

    parsed_docstring = GoogleParser().parse(docstring)
    assert(parsed_docstring.short_description == "Summary line.")
    assert(parsed_docstring.long_description == "Extended description.")
    assert(parsed_docstring.meta[0].description == "Description of arg1")
    assert(parsed_docstring.meta[1].description == "Description of arg2")
    assert(parsed_docstring.meta[2].description == "Return description")

# Generated at 2022-06-13 19:37:16.153625
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Make sure the method returned the expected values
    assert GoogleParser().parse("Hello world!") == Docstring(short_description="Hello world!", blank_after_short_description=False, blank_after_long_description=True, long_description=None, meta=[])
    assert GoogleParser().parse("Hello world!\n\nLorem ipsum dolor sit amet.") == Docstring(short_description="Hello world!", blank_after_short_description=True, blank_after_long_description=True, long_description="Lorem ipsum dolor sit amet.", meta=[])

# Generated at 2022-06-13 19:37:22.693113
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    '''test docstring-parser'''
    string='''
    This is a test string.

    :param s: the setting
    :type s: int
    :return: the setting
    '''

    assert string == GoogleParser().parse(string).__str__()


# Generated at 2022-06-13 19:37:31.859521
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = "Test GoogleParser.parse() short description."
    doc += "\n"

    doc += "Test GoogleParser.parse() long description."
    doc += "\n"

    doc += "Attributes:\n"
    doc += "    a (int): First attribute. Defaults to 1.\n"
    doc += "    b (str): Second attribute. Defaults to \"2\".\n\n"

    doc += "Raises:\n"
    doc += "    ArithmeticError: The exception type.\n"
    doc += "    ZeroDivisionError: Another exception type.\n\n"

    parser = GoogleParser()
    docstring = parser.parse(doc)
    assert len(docstring.meta) == 3
    assert docstring.short_description == "Test GoogleParser.parse() short description."


# Generated at 2022-06-13 19:37:47.636275
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:54.393283
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .Google import GoogleParser
    from .Numpy import NumpyParser
    import os
    import sys
    import unittest

    class TestGoogleParserParse(unittest.TestCase):

        def test_parse_function(self):
            """Test `parse` method with different types of parameters."""


# Generated at 2022-06-13 19:38:40.613539
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:55.525814
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test None as param
    text = None
    docstring = GoogleParser().parse(text)
    assert docstring.short_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.long_description is None
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 0

    # test empty string as param
    text = ""
    docstring = GoogleParser().parse(text)
    assert docstring.short_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.long_description is None
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 0

    # test no new line
    text = "Short description"

# Generated at 2022-06-13 19:38:58.300610
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse("""
    name -> str
        Try to return name.

    Parameters
    ----------
    name : str
        Name of the test.
    """)

    assert docstring.short_description == 'name -> str'


# Generated at 2022-06-13 19:39:04.044701
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
        Get info on this node.

        Info can contain anything.
    
        Parameters
        ----------
        item : str
            Id of the item.
        name : str, optional
            Name of the item.
        val : int
            Value of the item. Defaults to 2.
        lat : float, optional
            Lattitude.
        lon : float, optional
            Longitude.
        '''
    assert parse(text).short_description == 'Get info on this node.'
    assert parse(text).long_description == 'Info can contain anything.'
    assert parse(text).meta[0].description == 'Id of the item.'
    assert parse(text).meta[0].arg_name == 'item'
    assert parse(text).meta[0].type_name == 'str'

# Generated at 2022-06-13 19:39:12.572446
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser."""
    parser = GoogleParser()
    assert parser.parse("") == Docstring()
    assert parser.parse("Example:") == Docstring(
        short_description="Example", long_description=None, meta=[]
    )
    assert parser.parse("Example:\n\n") == Docstring(
        short_description="Example",
        long_description=None,
        meta=[DocstringMeta(args=["Example", ""], description=None)],
    )
    assert parser.parse("Example:\n    This is example foo") == Docstring(
        short_description="Example",
        long_description=None,
        meta=[DocstringMeta(args=["Example", "This is example foo"], description=None)],
    )

# Generated at 2022-06-13 19:39:22.017731
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "    test text\n    test text\n    test text \n    test text"

    text = inspect.cleandoc(text)

    # print(text)
    if not text:
        return None

    # Find first title and split on its position
    # ret.titles_re = re.compile(
    #     "^("
    #     + "|".join("(%s)" % t for t in ret.sections) + ")"
    #     + colon
    #     + "[ \t\r\f\v]*$",
    #     flags=re.M,
    # )
    titles_re = re.compile('^(Parameters|Args|Raises):[ \t\r\f\v]*$', flags=re.M)

# Generated at 2022-06-13 19:39:30.838782
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_fun():
        """Short desc.
        Long desc.

        Args:
            arg1 (str): The first argument.

        Raises:
            ValueError: When something bad happens.
        """
        pass

    docstring = GoogleParser().parse(test_fun.__doc__)
    assert docstring.short_description == "Short desc."
    assert docstring.long_description == "Long desc."
    assert docstring.meta[0].args == [
        "param",
        "arg1 (str)",
    ]
    assert docstring.meta[0].description == "The first argument."
    assert docstring.meta[1].args == ["raises", "ValueError"]
    assert docstring.meta[1].description == "When something bad happens."

# Generated at 2022-06-13 19:39:41.364173
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():                                                                    
    from pathlib import Path
    from docpie import Docpie
    from pprint import pprint
    
    # get the docstring for test
    for __file__ in [Path(__file__).parent / "test_google_docstring.py"]:
        for name, value in vars(Docpie).items():
            if name.startswith("_"): continue
            if not inspect.isclass(value): continue
            print(f"{__file__}: {name}")
            parser = Docpie(google=True, __file__=__file__, cls=value)
            pprint(parser.train())
            print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:39:47.381680
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''
        Test Function
        
        This is a test function
        
        Params:
            name: A string
            age: An int
            
            score: (int) a score.

        Raises:
            ValueError: if the input is not correct.
            
            TypeError: if the input is not correct.
            
        Example:
            >>> test_function(1, '3')
            
    '''
    docstring = parse(doc)
    assert len(docstring.meta) == 3
    assert docstring.meta[1].description == "A string"
    docstring.pprint()

# Generated at 2022-06-13 19:39:53.035800
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gs = GoogleParser()
    print(gs.parse("""
        Some function.
        :param arg1: some arg
        :params arg2: some arg
        :return: some return
        :yield: some yield
        :raises: some raise
        :raises ValueError: some raise
        :returns SomeClass: some retur
    """))
