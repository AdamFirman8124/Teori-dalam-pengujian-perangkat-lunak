

# Generated at 2022-06-13 19:31:14.693626
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def method_parse():
        input_string = """This is a description of the method.
        This is the first line of the long description.
        This is the second line of the long description.
        Args:
            n: This is an integer.
            m: This is a float.
            xyz: This is a string.
        Returns:
            The sum of the arguments.
        Raises:
            ValueError: If n or m are negative.
            TypeError: If n or m are not integers.
        """
        docstring_out = parse(input_string)
        return docstring_out
    docstring_out = method_parse()
    docstring_keywords_out = docstring_out.keywords

# Generated at 2022-06-13 19:31:27.064440
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    assert parse("hello") == Docstring(short_description="hello", long_description=None)
    assert parse("hello\n") == Docstring(short_description="hello", long_description=None)
    assert parse("hello\nworld") == Docstring(short_description="hello", long_description="world")
    assert parse("hello\nworld\n") == Docstring(short_description="hello", long_description="world")
    assert parse("hello\n\nworld") == Docstring(short_description="hello", long_description=None)
    assert parse("hello\n\nworld\n") == Docstring(short_description="hello", long_description="world")

# Generated at 2022-06-13 19:31:38.652289
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = """Example.
    Args:
        arg (int): Description of arg.
        *args: Description of *args.
        arg_kw (str): Description of arg_kw.
        **kwargs: Description of **kwargs.
        arg_kw_def (int, optional): Arg kw def. Defaults to '0'.
    """
    parsed_docstring = GoogleParser().parse(doc)
    assert isinstance(parsed_docstring, Docstring)
    assert len(parsed_docstring.meta) == 5

    meta1 = parsed_docstring.meta[0]
    assert isinstance(meta1, DocstringMeta)
    assert meta1.description == "Example."

    meta2 = parsed_docstring.meta[1]
    assert isinstance(meta2, DocstringParam)
    assert meta2

# Generated at 2022-06-13 19:31:50.800726
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Generate a DCGAN network based on a configuration json file.

    :param config_path: path to configuration file
    :param params: optional parameters
    :returns: the resulting network as a DeepGTAVModel instance
    :raises: AssertionError if input size is different from training size
    """
    doc = GoogleParser().parse(text)
    assert doc.short_description == "Generate a DCGAN network based on a configuration json file."
    assert doc.long_description == ""
    assert doc.blank_after_long_description
    assert doc.blank_after_short_description
    assert len(doc.meta) == 2
    assert doc.meta[0].args == ["returns"]
    assert doc.meta[0].description == "the resulting network as a DeepGTAVModel instance"
    assert doc

# Generated at 2022-06-13 19:32:01.450009
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("BEGIN test_GoogleParser_parse")
    doc = """mylib.mymod.myfunc
==============================================================
This function does something really cool. It takes arguments
``alpha`` and ``beta``.

    Args:
        alpha (str): The first argument.
        beta (str, optional): The second argument. Defaults to 'beta'.
    Raises:
        OSError: An error occurred.
    Examples:
        Some examples here.
    Returns:
        The return value. True for success, False otherwise.
"""
    docstring = GoogleParser().parse(doc)
    assert docstring is not None
    assert docstring.short_description == "This function does something really cool. It takes arguments ``alpha`` and ``beta``."
    assert docstring.blank_after_short_description
    assert docstring.long_description

# Generated at 2022-06-13 19:32:11.544384
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:32:19.951238
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:32:24.876043
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Empty input
    assert GoogleParser().parse(None) == Docstring()
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("   ") == Docstring()

    # No section titles
    doc = "This is the short description.\n" + \
          "This is the long description."
    expected = Docstring(
        short_description="This is the short description.",
        blank_after_short_description=False,
        long_description="This is the long description.",
        blank_after_long_description=False,
        meta=[],
    )
    assert GoogleParser().parse(doc) == expected

    # Multiple singular sections

# Generated at 2022-06-13 19:32:38.140657
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Arrange
    doc = inspect.cleandoc("""
    This is the short description
    Long description.

    This is a section of the long description.

    Args:
      arg_1: The first argument.
      arg_2: The second argument.
      arg_3: The third argument.

    Returns:
      Nothing.
    """)
    expected = Docstring()
    expected.short_description = "This is the short description"
    expected.long_description = "Long description.\n\nThis is a section of the long description."
    expected.blank_after_short_description = True
    expected.blank_after_long_description = True

# Generated at 2022-06-13 19:32:47.902797
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = r"""
    Parse the Google-style docstring into its components.

    :returns: parsed docstring
    """
    ret = GoogleParser().parse(docstring)

    assert ret.short_description == "Parse the Google-style docstring into its components."
    assert ret.long_description == ":returns: parsed docstring"
    assert ret.blank_after_short_description == True
    assert ret.blank_after_long_description == True

    _ret = Docstring()
    _ret.short_description = ret.short_description
    _ret.long_description = ret.long_description
    _ret.blank_after_short_description = ret.blank_after_short_description
    _ret.blank_after_long_description = ret.blank_after_long_description
    assert ret == _ret

# Generated at 2022-06-13 19:33:03.398227
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    sections = [
        Section("Arguments", "param", SectionType.MULTIPLE),
        Section("Returns", "returns", SectionType.SINGULAR_OR_MULTIPLE),
    ]
    parser = GoogleParser(sections=sections)
    parser.add_section(Section("Args", "param", SectionType.MULTIPLE))

    docstr = """
    This is a short description.

    This is a long description. It is separated
    from the short description by a blank line.

    Arguments:
        arg1: The first argument.
        arg2: The second argument, which has inline markup
            in it.
            Like this.
            And more.

    Returns:
        The return value.
    """

    parsed = parser.parse(docstr)


# Generated at 2022-06-13 19:33:09.803169
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # setup
    text = "hello world"
    # target
    ret = GoogleParser().parse(text)
    # assert
    assert ret.short_description == "hello world"
    assert not ret.blank_after_short_description
    assert ret.long_description is None
    assert not ret.blank_after_long_description
    assert ret.meta == []

# Generated at 2022-06-13 19:33:20.023012
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = """Calculates factorial of a number.

    :param x: Number to calculate factorial
    :type x: int
    :param y: Ignored
    :returns: factorial of x
    :raises ValueError: if the input value is negative or not an integer
    """
    parse_result = parser.parse(docstring)
    assert(parse_result.short_description == "Calculates factorial of a number.")
    assert (parse_result.blank_after_short_description == True)
    assert(parse_result.blank_after_long_description == False)
    assert (parse_result.long_description == "")
    assert (len(parse_result.meta) == 4)
    assert (len(parse_result.meta[0].args) == 2)
   

# Generated at 2022-06-13 19:33:30.598064
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("\n") == Docstring()
    assert GoogleParser().parse("foo\n") == Docstring(
        short_description="foo", blank_after_short_description=True
    )
    assert GoogleParser().parse("foo\n\n") == Docstring(
        short_description="foo", blank_after_short_description=True
    )
    assert GoogleParser().parse("foo\nbar") == Docstring(
        short_description="foo", long_description="bar"
    )
    assert GoogleParser().parse("foo\nbar\n") == Docstring(
        short_description="foo", long_description="bar"
    )

# Generated at 2022-06-13 19:33:38.660765
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
        Sum the values in an iterable.

        :param iterable: iterable of numbers to sum.
        :param int start: optional initial value for the sum
        :returns: the sum of the values.
        :raises: TypeError if any argument is not numeric.
        """
    parser = GoogleParser()
    print(parser.parse(text))

# Generated at 2022-06-13 19:33:48.844145
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    f = "This is a description of the function :param x: parameter x :returns: stuff"
    assert GoogleParser().parse(f).short_description == "This is a description of the function"
    assert GoogleParser().parse(f).meta[0].args[0] == "param"
    assert GoogleParser().parse(f).meta[0].arg_name == "x"
    assert GoogleParser().parse(f).meta[1].args[0] == "returns"
    assert GoogleParser().parse(f).meta[1].arg_name == None
    assert GoogleParser().parse(f).meta[1].type_name == "stuff"
    return True



# Generated at 2022-06-13 19:33:55.269250
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Return a list of the test names used in a module.
    
    :param module: Module
    :param verbose: 0 or 1
    :param warn: Ignored.
    :returns: List of strings
    """    
    ret = Docstring.from_str(text)
    import pprint
    pprint.pprint(ret)


# Generated at 2022-06-13 19:34:07.549618
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #input
    text = '''
    This function does something.

    :param a: The first parameter.
    :type a: str
    :param b: The second parameter.
    :type b: int
    '''

    #expected_output
    short_description = 'This function does something.'
    blank_after_short_description = True
    long_description = None
    blank_after_long_description = None
    params = [
        DocstringParam(args=['param', 'a'], description='The first parameter.', arg_name='a', type_name='str', is_optional=False, default=None),
        DocstringParam(args=['param', 'b'], description='The second parameter.', arg_name='b', type_name='int', is_optional=False, default=None)
    ]
   

# Generated at 2022-06-13 19:34:14.367044
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    doc1 = f"""Summarize the Fluent Python book.

    :param long_desc: long description of the book
    :type long_desc: str
    :param short_desc: short description of the book
    :type short_desc: str
    :returns: full and short descriptions
    :rtype: tuple[str]

    """
    ret1 = parser.parse(doc1)
    assert( ret1.short_description == "Summarize the Fluent Python book." )
    assert( ret1.long_description == "long description of the book" )
    assert( ret1.blank_after_short_description == False )
    assert( ret1.blank_after_long_description == True )
    assert( len(ret1.meta) == 3 )

# Generated at 2022-06-13 19:34:24.765782
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # arguments
    text = """Description of the function.

    Arguments:
      arg1(int): description for arg1.
      arg2(str): description for arg2.

    Returns:
      An integer.
    """

# Generated at 2022-06-13 19:34:47.373237
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    expected = Docstring(
        short_description="Method goo",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description=None,
        meta=[
            DocstringParam(
                args=["param", "x"],
                description="The x value.",
                arg_name="x",
                type_name="int",
                is_optional=None,
                default=None,
            ),
            DocstringParam(
                args=["param", "y: int"],
                description="The y value.",
                arg_name="y",
                type_name="int",
                is_optional=False,
                default=None,
            ),
        ],
    )


# Generated at 2022-06-13 19:34:53.395627
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test 1
    string = """
    Gets the whole sentence.
    
    Arguments:
        start_time: the beginning time to get sentence.
        end_time: the ending time to get sentence.
    """
    ret = parse(string)
    print(ret)
    assert isinstance(ret, Docstring)
    assert isinstance(ret.meta[0], DocstringParam)
    print("Test parse(): PASSED.")

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:35:08.265869
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import docstring_parser as docparser
    google_parser = docparser.GoogleParser()

# Generated at 2022-06-13 19:35:11.906421
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    Some short description.

    Some long description.
    """
    assert GoogleParser().parse(docstring).short_description == 'Some short description.'

# Unit tests for method _setup of class GoogleParser

# Generated at 2022-06-13 19:35:18.825108
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    doc_1 = """Simple example with short description only.

    """
    x = parser.parse(doc_1)
    assert x.short_description == "Simple example with short description only." and x.long_description == None and x.meta == []
    doc_2 = """Simple example with long description.

    We should have blank line after short description.
    """
    x = parser.parse(doc_2)
    assert x.short_description == "Simple example with long description." and x.long_description == "We should have blank line after short description." and x.meta == []
    doc_3 = """Simple example with both short and long description with multiple paragraphs.

    We should have blank line after short description.
    First paragraph of long description.

    Second paragraph of long description.
    """

# Generated at 2022-06-13 19:35:20.257642
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse(): 
    pass 


# Generated at 2022-06-13 19:35:30.728079
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    """
    # testing general docstring structure
    doc = """

# Generated at 2022-06-13 19:35:44.700356
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """\
    Returns the item at a given position.

    Raises:
        IndexError: when position is out of range.

    Returns:
        int: the item.
    """
    docstring = parser.parse(text)
    assert docstring.short_description == "Returns the item at a given position."
    assert docstring.long_description == "Raises:\n    IndexError: when position is out of range.\n\nReturns:\n    int: the item."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 2

# Generated at 2022-06-13 19:35:45.537443
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass


# Generated at 2022-06-13 19:35:55.767769
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('\"\"\"\n        A docstring of the class.\n        \"\"\"') == Docstring(short_description='A docstring of the class.', long_description=None, meta=[], blank_after_short_description=True, blank_after_long_description=False)
    assert GoogleParser().parse('\"\"\"\n        A docstring of the class.\n        \"\"\"') == Docstring(short_description='A docstring of the class.', long_description=None, meta=[], blank_after_short_description=True, blank_after_long_description=False)

# Generated at 2022-06-13 19:36:12.788040
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
        The short description ends at this line.
        
        The long description continues for more lines.
        The long description is indented as much as this line.
        
        Args:
            arg1(str): The first argument. The type is specified in parentheses.
            arg2 (str, optional) : The second argument.
                It has the same indentation as the first argument.
                It also spans multiple lines,
                and supports empty lines.
        
        Returns:
            bool: The return value. True for success, False otherwise.
    '''
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == "The short description ends at this line."
    assert docstring.long_description == "The long description continues for more lines.\nThe long description is indented as much as this line."
   

# Generated at 2022-06-13 19:36:23.698347
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from yapf.yapflib import py3compat
    from yapf.yapflib import consistency_checker

    def parse_and_assert(text, expected_docstring):
        docstring = GoogleParser().parse(text)
        assert docstring.short_description == expected_docstring.short_description
        assert docstring.long_description == expected_docstring.long_description
        assert docstring.blank_after_short_description == expected_docstring.blank_after_short_description
        assert docstring.blank_after_long_description == expected_docstring.blank_after_long_description
        assert len(docstring.meta) == len(expected_docstring.meta)

    def iter_args(docstring_meta):
        for meta in docstring_meta.meta:
            yield meta.args
       

# Generated at 2022-06-13 19:36:27.964041
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    o = GoogleParser().parse('''
    List of lists of numbers, where each constituent list corresponds to a
    node with whose value is a list of neighbor node indicies.

    Arguments:
        adjlist: List of lists of numbers, where each constituent list
            corresponds to a node with whose value is a list of neighbor
            node indicies.

    Returns:
        NetworkX graph.
    ''')
    print(o)


# Generated at 2022-06-13 19:36:38.168930
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    text = """\
        A short description of the module.

        A longer description of the module.

        Args:
            arg1: The first description.
                The second line of description.
            arg2 (optional): The third description.

        Returns:
            The return description.
    """


# Generated at 2022-06-13 19:36:46.154180
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # when sections is None
    parser = GoogleParser()
    text = '''
    This is a test Docstring.
    '''
    print(parser.parse(text))
    text = '''
    This is a test Docstring.

    :param name: Name
    :type name: str
    :returns: Name
    '''
    print(parser.parse(text))
    text = '''
    This is a test Docstring.

    :param name: Name.
    :type name: str
    :returns: Name.
    '''
    print(parser.parse(text))
    text = '''
    This is a test Docstring.

    :param name: Name
    :type name: str
    :returns: Name
    :raises TypeError: This is a test for raises.
    '''

# Generated at 2022-06-13 19:36:59.070765
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    docstr = ''' \
    Short description about the function.

    Long description about the function.

    Args:
        arg_1 (str): The first argument.
        arg_2 (:obj:`int`, optional): The second argument. Defaults to 2.

    Returns:
        str: Return value of the function.

    Examples:
        Examples can be given using either the ``Example`` or ``Examples``
        sections. Sections support any reStructuredText formatting, including
        literal blocks::

            $ python example_google.py
    '''


# Generated at 2022-06-13 19:37:08.145781
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("\n") == Docstring()
    assert GoogleParser().parse("    \n") == Docstring()
    assert GoogleParser().parse("1\n") == Docstring()
    assert GoogleParser().parse("1\n2") == Docstring()
    assert GoogleParser().parse("1\n2\n") == Docstring()
    assert GoogleParser().parse("1\n2\n3") == Docstring()
    assert GoogleParser().parse("1\n2\n3\n") == Docstring()
    assert GoogleParser().parse("1\n2\n3\n4") == Docstring()
    assert GoogleParser().parse("1\n2\n3\n4\n") == Docstring()
    assert GoogleParser().parse("\n1") == Doc

# Generated at 2022-06-13 19:37:16.639918
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    Summary line.

    Extended description.

    Args:
        arg1 (int): Description of `arg1`
        arg2 (str): Description of `arg2`. Defaults to 'foo'.
            Extended description of `arg2`.
        arg3 (bool): Description of `arg3`

    Returns:
        bool: Description of return value.
        Defaults to False.
            Extended description of return value.

    Raises:
        NameError: Description of `NameError`
    """


# Generated at 2022-06-13 19:37:20.385299
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .examples import google_docstring_examples
    for example in google_docstring_examples.parse_test_cases:
        doc = parse(example["doc"])
        assert doc == example["result"]

# Generated at 2022-06-13 19:37:30.872065
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text_1 = "test_GoogleParser_parse\n\n    This is a multiline description.\n    And this is another line.\n\n    Attributes:\n        attr1 (int): Description of attr1\n        attr2 (str): Description of attr2\n\n    Returns:\n        None\n        "
    text_2 = "test_GoogleParser_parse\n\n    This is a multiline description.\n    And this is another line.\n\n    Attributes:\n        attr1 (int): Description of attr1\n        attr2 (str): Description of attr2\n\n    Returns:\n        None"
    text_3 = "test_GoogleParser_parse\n    This is a multiline description.\n    And this is another line."
    text_

# Generated at 2022-06-13 19:37:48.729475
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test method parse of class GoogleParser.

    Tests if parse returns the correct Docstring object. 
    """
    query_text = """
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    """
    docstring = parse(query_text)
    assert docstring.short_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.long_description == None
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []
    

# Generated at 2022-06-13 19:37:57.942257
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    def test_function():
        """Short description.

        Long description.
        """
        pass
    docstring = inspect.getdoc(test_function)
    parsed_docstring = parser.parse(docstring)
    assert parsed_docstring.short_description == 'Short description.'
    assert parsed_docstring.long_description == 'Long description.'
    assert parsed_docstring.blank_after_short_description is True
    assert parsed_docstring.blank_after_long_description is True



# Generated at 2022-06-13 19:38:05.621257
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:15.593017
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # set up environment to test parsing
    class Dummy(object):
        def __init__(self, *args: str, **kwargs: str) -> None:
            return None

        def __call__(self, *args: str, **kwargs: str) -> None:
            return None

        def __bool__(self) -> bool:
            return False

        def __repr__(self) -> str:
            return "Dummy"

    f = Dummy()

    # generate test data
    f.f = Dummy()
    f.f.f = Dummy()
    f.f.f.f = Dummy()
    f.f.f.f.f = Dummy()
    f.f.f.f.f.f = Dummy()


# Generated at 2022-06-13 19:38:23.288611
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:28.847615
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Parse the Google-style docstring into its components.

    :returns: parsed docstring
    """

    expected_info = {'short_description': 'Parse the Google-style docstring into its components.', 'long_description': ':returns: parsed docstring\n', 'blank_after_short_description': False, 'blank_after_long_description': False, 'meta': [DocstringMeta(args=['Returns'], description='parsed docstring', arg_name='Returns', type_name=None, is_optional=None)]}
    
    doc_str = GoogleParser().parse(text)
    info = doc_str.info()
    assert info == expected_info

# Generated at 2022-06-13 19:38:38.474051
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """Summary line.
    Extended description of method.
    Args:
        arg1 (str): Description of arg1
        arg2 (list): Description of arg2
    Returns:
        bool: Description of return value
    """
    docstring = parser.parse(text)
    assert docstring.short_description == 'Summary line.'
    assert docstring.long_description == (
        'Extended description of method.')
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 2


# Generated at 2022-06-13 19:38:51.184642
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse("""\
        Example Google docstring

        Parameters
        ----------
        a : int
            The 'a' parameter.
        b : float
            The 'b' parameter.

        Returns
        -------
        int
            The 'return value' parameter.

        Examples
        --------
        This is an example of this function, with the input of ``test``.

            >>> test
            4

        And the output, ``4``.
        """)
    assert docstring.short_description == "Example Google docstring"
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True

# Generated at 2022-06-13 19:38:55.905306
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    test_docstring = """
 Parameters
    ----------
    Y: array-like, shape (n_samples, n_features)
        Target values.
    X: array-like, shape (n_samples, n_features)
        Training input samples.

    Returns
    -------
    coef : ndarray, shape (n_features,)
        Fitted parameters.
    """
    res = parser.parse(test_docstring)
    assert res.meta[0].keyword == 'param'
    assert res.meta[1].keyword == 'param'
    assert res.meta[2].keyword == 'returns'

# Generated at 2022-06-13 19:39:01.991910
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def parse_test(docstring, expected_result):
        assert GoogleParser().parse(docstring) == expected_result


# Generated at 2022-06-13 19:39:36.221286
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    assert parser.parse("example") == Docstring(
        short_description="example",
        long_description=None,
        meta=[],
        blank_after_short_description=False,
        blank_after_long_description=False,
    )

    assert parser.parse("""
    example

    Description:
      Long description.

    """
    ) == Docstring(
        short_description="example",
        long_description="Long description.",
        meta=[],
        blank_after_short_description=True,
        blank_after_long_description=False,
    )


# Generated at 2022-06-13 19:39:45.133338
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = '''
    short description 

    long description
    '''
    assert len(parser.parse(text).meta) == 0
    assert parser.parse(text).short_description == ("short description")
    assert parser.parse(text).long_description == ("long description")

    text = '''
    short description

    long description
    
    
    '''
    assert parser.parse(text).blank_after_short_description == True
    assert parser.parse(text).blank_after_long_description == True

    text = '''
    short description
    
    
    
    
    long description
    '''
    assert parser.parse(text).blank_after_short_description == False
    assert parser.parse(text).blank_after_long_description == True


# Generated at 2022-06-13 19:39:56.274128
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = ""
    description = parse(docstring)
    assert description.short_description == None
    assert description.long_description == None
    assert description.blank_after_short_description == False
    assert description.blank_after_long_description == False
    assert description.meta == []

    docstring = "Short description.\n"
    description = parse(docstring)
    assert description.short_description == "Short description."
    assert description.long_description == None
    assert description.blank_after_short_description == False
    assert description.blank_after_long_description == False
    assert description.meta == []

    docstring = "Short description.\n\nLong description.\n"
    description = parse(docstring)
    assert description.short_description == "Short description."
    assert description.long_description

# Generated at 2022-06-13 19:40:11.466397
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    
    parser = GoogleParser()

    # Parse with no docstring
    res = parser.parse("")
    assert res.short_description == None
    assert res.long_description == None
    assert res.blank_after_short_description == False
    assert res.blank_after_long_description == False
    assert len(res.meta) == 0

    # Parse with only short description
    res = parser.parse("This is a short description\n")
    assert res.short_description == "This is a short description"
    assert res.long_description == None
    assert res.blank_after_short_description == False
    assert res.blank_after_long_description == False
    assert len(res.meta) == 0

    # Parse with only short description and indent

# Generated at 2022-06-13 19:40:25.225906
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    input = '''
    This is a short description.

    This is a long description.

    Args:
        param1(int): This is a param
        param2 (int): This is a param
        param3: This is a param
        param4 (int, optional): This is an optional param. Defaults to True.
        param5 [int]: This is a param with a default value. Defauls to 0.

    Returns:
        None

    Raises:
        ValueError: If `param2` is equal to `param1`.
    '''

# Generated at 2022-06-13 19:40:36.546465
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Case 1
    text = """Parse the Google-style docstring into its components.
    :returns: parsed docstring"""
    assert GoogleParser().parse(text) == Docstring(
        short_description="Parse the Google-style docstring into its components.",
        blank_after_short_description=False,
        long_description="returns: parsed docstring",
        blank_after_long_description=False,
        meta=[
            DocstringMeta(args=["returns"], description="parsed docstring"),
        ],
    )

    # Case 2
    text = """Parse the Google-style docstring into its components.
    :returns: parsed docstring
    
    New line after short description
    """

# Generated at 2022-06-13 19:40:47.215164
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    docstring_one_title = """Reference class for basic commands.
    """
    docstring_multi_title = """Reference class for basic commands.

    Args:
        arg_1 (str): first argument
        arg_2 (str): second argument

    Raises:
        NameError: If a name is not defined.
    """
    # Test 1:
    # This tests if the docstring 'docstring_one_title' gets parsed correctly
    # Test will return True if the description of the parsed docstring matches the description of passed 'docstring_one_title'.
    assert p.parse(docstring_one_title).short_description == "Reference class for basic commands."
    # Test 2:
    # This tests if the docstring 'docstring_multi_title' gets parsed correctly
    # Test will return True if