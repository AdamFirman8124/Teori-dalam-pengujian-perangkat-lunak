

# Generated at 2022-06-13 19:41:45.549991
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    f = open("numpydoc_section.txt","r")
    text = f.read()
    f.close()
    text = inspect.cleandoc(text)
    
    expected_result = [
        ('c', 'This is c'),
        ('a', 'This is a'),
        ('b', 'This is b')
    ]
    
    actual_result = []
    
    for match, next_match in _pairwise(KV_REGEX.finditer(text)):
        start = match.end()
        end = next_match.start() if next_match is not None else None
        value = text[start:end]
        actual_result.append((match.group(), inspect.cleandoc(value)))
    
    assert(expected_result == actual_result)


# Generated at 2022-06-13 19:41:52.643437
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    from .common import DocstringMeta

    parse_string = "key\n    value\nkey2 : type\n    values can also span...\n    ... multiple lines"

    section = _KVSection('Params', 'param')
    result = list(section.parse(parse_string))

    assert isinstance(result[0], DocstringMeta)
    assert result[0].description == 'value'

    assert isinstance(result[1], DocstringMeta)
    assert result[1].description == 'values can also span...\n... multiple lines'



# Generated at 2022-06-13 19:41:57.862296
# Unit test for method parse of class Section
def test_Section_parse():
    text = '''
    Parameters
        ----------
        a : type
            Parameter description
    '''
    c = ParamSection("Parameters","param")
    param_list = c.parse(text)
    for element in param_list:
        assert element.description == 'Parameter description'
        assert element.args == ['param', 'a']

# Test for method parse of class RaisesSection

# Generated at 2022-06-13 19:42:01.629660
# Unit test for method parse of class Section
def test_Section_parse():
    s = Section("title", "key")
    text = "\n\nThis is a sample\n\n"
    assert s.parse(text) == [DocstringMeta(['key'], description = "This is a sample")]


# Generated at 2022-06-13 19:42:10.151171
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    from . import common
    from .common import DocstringMeta

    text = """
    ax
        The axis along which the product is performed.

    initial
        Initial value, to avoid spurious NumPy warnings if `a` is
        empty.
        """
    actual_output = common.Docstring()
    actual_output.meta.append(DocstringMeta(["param", "ax"],
                                            description="The axis along which the product is performed."))
    actual_output.meta.append(DocstringMeta(["param", "initial"],
                                            description="Initial value, to avoid spurious NumPy warnings if `a` is\n        empty."))
    expected_output = actual_output
    assert actual_output == expected_output
    

# Generated at 2022-06-13 19:42:19.634951
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    section = _KVSection("KeyValue", "kv")
    text = """
    key1
        value1
    key2 : type
        values can also span multiple lines
    key3 : type
    """

    parsed_text = section.parse(text)

    assert next(parsed_text).description == 'value1'
    assert next(parsed_text).description == 'values can also span multiple lines'
    assert next(parsed_text).description == ''



# Generated at 2022-06-13 19:42:26.239680
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    '''
    We only test this method of the class _KVSection, because the other methods
    are tested by test_parser_numpydoc.py
    '''
    text = '''
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
    '''
    parser = NumpydocParser()
    for _ in parser._KVSection("Parameters", "param").parse(text):
        assert True


# Generated at 2022-06-13 19:42:31.310040
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    parser = ParamSection("Parameters", "param")
    text="""
        arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines
     """
    text = inspect.cleandoc(text)
    metas = parser.parse(text)
    expected = [DocstringParam(args=['param', 'arg_name'],
        description='arg_description', is_optional=False, type_name=None,
        default=None),
    DocstringParam(args=['param', 'arg_2'],
        description='descriptions can also span...\n... multiple lines',
        is_optional=True, type_name='type', default=None)]
    assert metas == expected

# Generated at 2022-06-13 19:42:36.144378
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    text = """
        first
            first value
        second : type, optional
            second value
        third
            third value
    """
    parser = _KVSection("", "")
    assert parser.parse(text) == [
        DocstringMeta(["", "first"], description="first value"),
        DocstringMeta(["", "second"], description="second value"),
        DocstringMeta(["", "third"], description="third value"),
    ]



# Generated at 2022-06-13 19:42:41.979023
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    text = """
        key
            value
        key2 : type
            values can also span...
            ... multiple lines
    """
    assert list(_KVSection("title", "key").parse(text)) == [
        {
            "args": ['key'],
            "description": "value",
        },
        {
            "args": ['key2'],
            "description": "values can also span...\n... multiple lines"
        },
    ]


# Generated at 2022-06-13 19:43:02.483421
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring

    text = '''\
    Calculate the sum of two numbers.

    Parameters
    ----------
    a : int
        The first operand.
    b : int
        The second operand.

    Returns
    -------
    int
        The sum of the two operands.
    '''

    res = parse(text)

    d = Docstring()
    d.short_description = "Calculate the sum of two numbers."
    d.long_description = "The sum of the two operands."
    d.blank_after_short_description = True
    d.blank_after_long_description = True


# Generated at 2022-06-13 19:43:08.433233
# Unit test for method parse of class Section
def test_Section_parse():
    """Test the method parse of class Section."""
    section = Section(title="title", key="key")

    text = """
    text
    text
    text
    """

    ret = section.parse(text)
    ret1 = DocstringMeta([section.key], description="text\ntext\ntext")

    assert ret == [ret1]

# Generated at 2022-06-13 19:43:13.192982
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # taken from https://numpydoc.readthedocs.io/en/latest/format.html
    text = """
        Attributes
        ----------
        foo : int
            Foo parameter.
    """
    assert NumpydocParser().parse(text).meta[0].get_arg_names() == ["param", "foo"]

# Generated at 2022-06-13 19:43:24.352972
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    def test_parse(test_text,test_short_description_text,test_long_description_text,test_meta):
        text = test_text
        docstring = parser.parse(text)
        assert docstring.short_description == test_short_description_text
        assert docstring.long_description == test_long_description_text
        assert len(docstring.meta) == len(test_meta)
        for i in range(len(test_meta)):
            assert docstring.meta[i].description == test_meta[i]

    # Test with no meta block
    test_parse('Function docstring.','Function docstring.','',[])

    # Test with one meta block

# Generated at 2022-06-13 19:43:28.677141
# Unit test for method parse of class Section
def test_Section_parse():
    s=Section("test","test")
    print(s.title)
    print(s.key)

    print(s.title_pattern)

    s.parse("test\n----\ntest1")

if __name__ == '__main__':
    test_Section_parse()
    pass

# Generated at 2022-06-13 19:43:42.051463
# Unit test for method parse of class Section
def test_Section_parse():
    docstring = """
    Parameters
    ----------
    a : int, optional
        first parameter
        optional parameter
    b : list of ints
        a list of ints
        obvi

    Returns
    -------
    a : int
        first returned value
        single return
    b : int, optional
        second returned value
        optional return
    """
    tempDoc = Docstring()
    tempDoc.short_description = "testing docstrings"

# Generated at 2022-06-13 19:43:43.428710
# Unit test for method parse of class Section
def test_Section_parse():
    with open('test_Section/test_Section_parse.txt', 'r') as file:
        text = file.read()
    ret = parse(text)
    return ret

# Generated at 2022-06-13 19:43:48.316666
# Unit test for method parse of class Section
def test_Section_parse():
    text = """Function that generate an automatic documentation of a module.

    Parameters
    ----------
    module : module
        module to document.
    functions : list or tuple
        functions to document, or None to document all functions.
    classes : list or tuple
        classes to document, or None to document all classes.
    module_doc : string
        documentation of the module, if None it will be retrieved from the
        docstring of the module.
    packagename : string
        name of the package which contains the module, if None it will be
        retrieved from the module.

    Returns
    -------
    doc : Doc
        instance with the documentation.
    """
    parser = NumpydocParser()
    ret = parser.parse(text)

# Generated at 2022-06-13 19:43:52.903325
# Unit test for method parse of class Section
def test_Section_parse():
    dic = {'desc': 'This is a description', 'key': 'key'}
    assert Section(dic["desc"], dic["key"]).parse(dic["desc"]) == [DocstringMeta([dic["key"]], 'This is a description')]



# Generated at 2022-06-13 19:43:58.224901
# Unit test for method parse of class Section
def test_Section_parse():
    text = 'input\n    param1\n    param2\n    '
    res = ParamSection("Input", "input").parse(text)
    res = list(res)
    assert(res[0] == DocstringParam(["input", "param1"], description=None))
    assert(res[1] == DocstringParam(["input", "param2"], description=None))


# Generated at 2022-06-13 19:44:08.465717
# Unit test for method parse of class Section
def test_Section_parse():
    text = "Parameters\n----------\nb : int\n    The parameter b"

    expected_result = DocstringMeta(["param", "b"], description="The parameter b",arg_name="b",type_name="int")

    section = Section("Parameters", "param")
    gen = section.parse(text)

    result = next(gen)

    assert result == expected_result

# Generated at 2022-06-13 19:44:11.327899
# Unit test for method parse of class Section
def test_Section_parse():
    section = Section("test", "test")
    text = """test
    description"""
    for match in section.parse(text):
        assert match._args == ['test']
        assert match._description == 'description'



# Generated at 2022-06-13 19:44:19.206845
# Unit test for method parse of class Section
def test_Section_parse():
    """Unit test for method parse of class Section
    """

    # Tests for method Section.parse
    def test_a():
        """Tests for method Section.parse
        """

        title_pattern = "^Test\s*?\n{}\s*$".format("-" * 4)

# Generated at 2022-06-13 19:44:28.609902
# Unit test for method parse of class Section
def test_Section_parse():
    str1 = '''
    Raises
    ------
    typ : type
        a type
    '''
    obj = NumpydocParser()
    sec = Section("Raises", "raises")
    obj.add_section(sec)
    res = obj.parse(str1)
    assert res.meta[0].type_name == "type"
    assert res.meta[0].args == ["raises", "typ"]
    assert res.meta[0].description == "a type"



# Generated at 2022-06-13 19:44:32.613280
# Unit test for method parse of class Section
def test_Section_parse():
    section = Section("Parameters", "param")
    text = "arg_name\n    arg_description\n"
    res = section.parse(inspect.cleandoc(text))
    res1 = next(res)
    assert res1.args == ['param', 'arg_name']
    assert res1.description == 'arg_description'


# Generated at 2022-06-13 19:44:43.209314
# Unit test for method parse of class Section
def test_Section_parse():
    from .common import DocstringMeta
    from .numpydoc import Section

# Generated at 2022-06-13 19:44:47.734037
# Unit test for method parse of class Section
def test_Section_parse():
    text = '''blah:
        a: A
        b: B'''
    assert Section('blah', 'blah').parse(text) == \
        [DocstringMeta(['blah'], description='blah:\n        a: A\n        b: B')]

if __name__ == "__main__":
    import pytest
    pytest.main('-v')

# Generated at 2022-06-13 19:44:49.694609
# Unit test for method parse of class Section
def test_Section_parse():
    section = Section("Parameters", "param")
    list(section.parse("arg_name\n   arg_description"))


# Generated at 2022-06-13 19:44:51.957734
# Unit test for method parse of class Section
def test_Section_parse():
    doctring = Section('Parameters','param')
    text = "arg_name\n arg_description"
    assert type(doctring.parse(text)) == itertools.zip_longest

# Generated at 2022-06-13 19:44:56.367396
# Unit test for method parse of class Section
def test_Section_parse():
    s = Section("Title", "Key")
    assert hasattr(s, "title")
    assert s.title == "Title"
    assert hasattr(s, "key")
    assert s.key == "Key"
    assert hasattr(s, "title_pattern")
    assert s.title_pattern == "^(Title)\s*?\n------\s*$"
    assert hasattr(s, "parse")


# Generated at 2022-06-13 19:45:10.866125
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_string = '''
    A function to display a message.

    Parameters
    ----------
    msg : str
        The message to be displayed.

    Returns
    -------
    length : int
        The length of the message.

    Raises
    ------
    ValueError
        If the message is an empty string.

    See Also
    --------
    display_message2 : A more advanced function that adds a star to the front
        of the message.

    Examples
    --------
    >>> message='Hello'
    >>> length = display_message(message)
    >>> print(length)
    5
    '''

    parser = NumpydocParser()
    doc_string = parser.parse(doc_string)

    assert doc_string.short_description == 'A function to display a message.'
    assert doc_string.blank_after_

# Generated at 2022-06-13 19:45:22.907420
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test the method parse of class NumpydocParser

    """
    text = """
        Short description.
        
        Long description.
        
        Parameters
        ----------
        arg1 : int
            description...
        arg2
            description...
        arg3 : str
            description...
        arg4 : {'small', 'medium'}
            description...
        arg5 : int or float, optional
            description...
        arg6 : bool, optional
            description...
        
            continued
        
        arg7 :
            description...
            multiline
        
        Returns
        -------
        ret_var : type
            description...
        """
    text = inspect.cleandoc(text)
    factory = NumpydocParser()
    doc = factory.parse(text)

# Generated at 2022-06-13 19:45:27.559866
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    text = """
        do_something(a, b)
        do something

        Parameters
        ----------
        a : str
            a is a string
        b : int
            b is an integer

        Raises
        ------
        ValueError
            when a is greater than b

        Returns
        -------
        two : int
            a plus b
        """
    docstring = parser.parse(text)

    assert docstring.short_description == "do something"
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 3
    docstring_meta = docstring.meta

# Generated at 2022-06-13 19:45:37.813323
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring_parser = NumpydocParser()
    docstring = """
        This is a very short description.

        This is a rather long description which spans
        multiple lines.

        Parameters
        ----------
        arg1 : int
            A short description of arg1
        arg2: str
            A short description of arg2, which can span
            over multiple lines

        Returns
        -------
        retval: :class:`~empty.empty`
            A short description of retval
        """

# Generated at 2022-06-13 19:45:46.550168
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import doctest
    #build parser for test
    parser = NumpydocParser()
    # parse docstring
    ref = parser.parse('''Parse numpy docstring.

    Parameters
    ----------
    text : str
        Text to parse

    Returns
    -------
    value : int
        Parsed value

    Examples
    --------
    >>> parser = NumpydocParser()
    >>> parser.parse('text')
    'text'
    ''')
    #build reference

# Generated at 2022-06-13 19:45:57.891581
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:03.753120
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    res = parser.parse("""
        This is the short description.
        
        This is the long description.
        
        Parameters
        ----------
        a : int
            A parameter for the function.
        b : str
            Another parameter for the function.
        
        Returns
        -------
        dict
            A dictionary with something.
        
        Raises
        ------
        TypeError
            If something is wrong, this is raised.
        ValueError
            If something is wrong, this is raised.
        
        """ )
    assert res.short_description == "This is the short description."
    assert res.long_description == "This is the long description."
    assert res.meta[0].description == "A parameter for the function."

# Generated at 2022-06-13 19:46:09.103176
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = """\
    Returns a list of the given size filled with a given value.
    
    Parameters
    ----------
    func : callable
        The function to be executed on each item of the iterable.
        Optional, defaults to None.
    true_values : bool
        The bool value to fill the list with. Optional, defaults to True.
    *args:
        The *args to pass to the function.
    default : int
        The default value used if the iterable is empty. Optional.
    test: List[str], optional
        A list of strs.
    **kwargs:
        The **kwargs to pass to the function.
    """
    parser = NumpydocParser()
    parsed = parser.parse(doc)
    print(parsed.meta[3].arg_name)

# Generated at 2022-06-13 19:46:12.790483
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    for i in range(2):
        nd = NumpydocParser()
        docstring = nd.parse.__doc__
        assert type(docstring) == str
        assert len(docstring) != 0



# Generated at 2022-06-13 19:46:16.687771
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    numpy_docstring = parser.parse.__doc__
    assert numpy_docstring == "Parse the numpy-style docstring into its components.\n\n:returns: parsed docstring"
    # Testing the return type of the method
    assert type(numpy_docstring) is str


# Generated at 2022-06-13 19:46:30.140185
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:34.071766
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = """
        A short description.

        A long description.
        """
    result = parser.parse(docstring)
    assert result.short_description == "A short description."
    assert result.long_description == "A long description."
    assert result.blank_after_short_description == False
    assert result.blank_after_long_description == True


# Generated at 2022-06-13 19:46:48.046474
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:59.466073
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Short description.

    This is a long description (it can span multiple lines).

    Parameters
    ----------
    arg 1
        arg 1 description

    arg 2 : int
        arg 2 description

    Raises
    ------
    ValueError
        If something goes wrong.

    Notes
    -----
    order of sections does not matter


    Returns
    -------
    return_name : str
        the return description

    """
    docstring = parse(text)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "This is a long description (it can span multiple lines)."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description

    assert len(docstring.meta) is 5

    # Check the order of sections

# Generated at 2022-06-13 19:47:12.647850
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """Collect the function parameters, except for the argument list.

    Parameters
    ----------
    something : str
        An argument that should be a string.
    something_else : int, optional
        An optional argument whose default value can be None.

    Returns
    -------
    type1 : int
        A return value.

    Other Parameters
    ----------------
    other : :obj:`str`, optional
        Something optional.

    Notes
    -----
    These might be a footnote or something like that.

    This can span lines.

    See Also
    --------
    :func:`decorator2`, :func:`decorator3`
    """

    actual = NumpydocParser().parse(docstring)

# Generated at 2022-06-13 19:47:18.272469
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = '''
    Short description:
    Long description.
    Parameters
    ----------
    a : int
        Description of argument a
    '''
    docstring = parser.parse(text)
    assert docstring.short_description == 'Short description:'
    assert docstring.long_description == 'Long description.'
    assert docstring.meta[0].description == 'Description of argument a'


# Generated at 2022-06-13 19:47:28.238580
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test case 1: docstring is empty
    text = ''
    expected = Docstring()
    assert NumpydocParser().parse(text) == expected

    # Test case 2: docstring is None
    text = None
    expected = Docstring()
    assert NumpydocParser().parse(text) == expected

    # Test case 3: docstring exists and the syntax of docstring is not standard
    text = '''
    example docstring
    '''
    expected = Docstring()
    expected.short_description = 'example docstring'
    expected.blank_after_short_description = False
    assert NumpydocParser().parse(text) == expected

    # Test case 4: docstring exists and does not have a long description

# Generated at 2022-06-13 19:47:36.812106
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser=NumpydocParser()
    assert parser.parse(
    """This is a numpydoc parser.

Parameters
----------
arg1 : int
    Description of arg1
arg2 : list
    Description of arg2.
    We can write multi-line description.
    Yes we can!

    You can also give default values for aruments.
    Note that default value is deduced from the first line.
"""
).meta==(
    DocstringMeta(['param', 'arg1'], description='Description of arg1'),
    DocstringMeta(['param', 'arg2'], description='Description of arg2.\nWe can write multi-line description.\nYes we can!\n\nYou can also give default values for aruments.\nNote that default value is deduced from the first line.')
)

# Generated at 2022-06-13 19:47:47.325332
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    parser = NumpydocParser()

    text = """
        This is a short description.

        This is a long
        description.

        Arguments
        ---------
        arg1 : int
            description of arg1
        arg2 : str
            description of arg2

        Returns
        -------
        arg1
            description of arg1
        arg2 : str
            description of arg2

        Raises
        ------
        ValueError
            Error raised if something occurred.
        """

    docstring = parser.parse(text)
    # print(docstring.short_description)
    # print(docstring.long_description)
    # print(docstring.blank_after_short_description)
    # print(docstring.blank_after_long_description)
    # print(docstring.meta)


# Generated at 2022-06-13 19:47:55.000509
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # TypeError case
    assert NumpydocParser().parse("") == Docstring()
    # default case
    assert NumpydocParser().parse("a\n----\n1\n")
    # with arg case
    assert NumpydocParser().parse("a\n----\n1\n", "") == Docstring()
    # TypeError case
    assert NumpydocParser().parse("a\n----\n1\n", 1) == Docstring()


# Generated at 2022-06-13 19:48:12.963243
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:21.456879
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Function to calculate the square of a number.

    Examples
    --------
    >>> square(2)
    4
    >>> square(5)
    25

    Parameters
    ----------
    x : number
        The number to be squared.

    Returns
    -------
    number
        The square of the input number.
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "Function to calculate the square of a number."
    assert docstring.blank_after_short_description
    assert docstring.long_description == "Examples\n--------\n>>> square(2)\n4\n>>> square(5)\n25"
    assert docstring.blank_after_long_description
    assert len(docstring.meta) == 2

# Generated at 2022-06-13 19:48:26.619755
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:48:37.737778
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:48:47.410455
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test the method parse of class NumpydocParser
    """
    import textwrap

    # Default parser
    parser = NumpydocParser()
    assert parser.parse("").meta == []
    assert parser.parse("short\n").meta == []
    assert parser.parse("\nshort").meta == []
    assert parser.parse("short\n\n").meta == []
    assert parser.parse("\nshort\n").meta == []
    assert parser.parse("\nshort\n\n").meta == []

    # Section titles
    assert parser.parse("short\n\nParameters\n---------\na").meta == [
        DocstringMeta(["param"], description="a")
    ]

# Generated at 2022-06-13 19:48:59.707622
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = '''
    Short description
    Long description
    Parameters
    ----------
    a : type
        parameter a

    b : type, optional
        parameter b

    *args
        variable length argument list.
    **kwargs
        arbitrary keyword arguments.

    Returns
    -------
    type
    '''
    ret = parser.parse(text)
    assert ret.short_description == 'Short description', 'Short description is wrong'
    assert ret.long_description == 'Long description', 'Long description is wrong'
    assert ret.blank_after_short_description, 'missing blank line after Short description'
    assert ret.blank_after_long_description, 'missing blank line after Long description'
    assert len(ret.meta) == 5, 'Incorrect number of meta'

# Generated at 2022-06-13 19:49:08.228946
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
    """
    ret = Docstring()
    if not text:
        return ret
    text = inspect.cleandoc(text)
    match = True
    if match:
        desc_chunk = text[: match.start()]
        meta_chunk = text[match.start() :]
    else:
        desc_chunk = text
        meta_chunk = ""
    parts = desc_chunk.split("\n", 1)
    ret.short_description = parts[0] or None
    if len(parts) > 1:
        long_desc_chunk = parts[1] or ""
        ret.blank_after_short_description = long_desc_chunk.startswith("\n")
        ret.blank_after_long_description = long_desc_chunk.endsw

# Generated at 2022-06-13 19:49:14.901986
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    np = NumpydocParser()
    docstring = np.parse("""
        Short description.

        Long description.

        Parameters
        ----------
        arg_name : type
            arg description
        ## todo: is there a difference between an arg and a parameter?

        Raises
        ------
        ValueError
            A description of what might raise ValueError

        Returns
        -------
        return_name : type
            A description of this returned value
        another_type
            Return names are optional, types are required

        Examples
        --------
        Examples should be written in doctest format, and should illustrate how
        to use the function/class.
        >>>

        See Also
        --------
        other_function : Related function
        third_function, fourth_function, fifth_function
        """
    )


# Generated at 2022-06-13 19:49:22.810863
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:32.535313
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    doc = parser.parse('This is a doc\n')
    assert doc.short_description == 'This is a doc'
    assert doc.long_description == None
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert len(doc.meta) == 0

    doc = parser.parse('This is a doc\n\nThis is the long description')
    assert doc.short_description == 'This is a doc'
    assert doc.long_description == 'This is the long description'
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == False
    assert len(doc.meta) == 0


# Generated at 2022-06-13 19:49:56.548111
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    This test is designed to manually test the NumpydocParser.parse() method.
    Here we write the unit test for the method on the docstring of the method itself.
    The test is a construction of the manual test of the method on the docstring.
    The code is constructed by me which means it will most likely break somewhere
    as a result of an indentation or procedural error.
    If this occurs you will notice that the output has not changed.
    To fix this you must look at the manual test and look for the error.
    You can find the test in the docstrings of the NumpydocParser.parse() method.
    """

# Generated at 2022-06-13 19:50:05.048708
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    input_str = """
    Parameters
    ----------
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
    """

    output_str = """
    Parameters
    ----------
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
    """

    # Create parser object
    p = NumpydocParser()

    # Create test object
    ret = p.parse(input_str)

    # Compare result
    assert str(ret) == output_str

# Generated at 2022-06-13 19:50:13.136566
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    doc = '''This is a short description.
    This is a long description.

    This is an extra line of long description.

    Parameters
    ----------
    num1 : int
        First number to multiply

    num2 : int
        Second number to multiply

    Returns
    -------
    int
        The product of arguments num1 and num2.
    '''
    assert parse(doc).short_description == 'This is a short description.'
    assert parse(doc).long_description == 'This is a long description.\n\nThis is an extra line of long description.' # noqa
    assert parse(doc).blank_after_short_description == True
    assert parse(doc).blank_after_long_description == True
    assert parse(doc).meta[0].description == 'First number to multiply'

# Generated at 2022-06-13 19:50:25.896455
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test docstring
    text = "Test docstring.\n\n" \
           "Parameters\n" \
           "----------\n" \
           "parameter_1\n" \
           "    Description of parameter\n" \
           "parameter_2 : str, optional\n" \
           "    Another description\n" \
           "\n" \
           "Raises\n" \
           "------\n" \
           "ValueError\n" \
           "    Something raises ValueError\n" \
           "TypeError\n" \
           "    Something raises TypeError"

    parser = NumpydocParser()
    parsed_docstring = parser.parse(text)

    # Test short_description
    assert parsed_docstring.short_description == "Test docstring."

    # Test blank_after

# Generated at 2022-06-13 19:50:27.405177
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = NumpydocParser()
    docstring_txt = """Returns a string."""
    assert docstring.parse(docstring_txt) == Docstring()



# Generated at 2022-06-13 19:50:35.594226
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    p = NumpydocParser()
    text = """Sample numpydoc docstring.
      
            Parameters
            ----------
            type_name
                description
            arg_2 : type, optional
                description2
            arg_3
                description3
            Returns
            -------
            type_name
                description7
            returns
                description8
            Warnings
            --------
            Warning
                description11
            Notes
            -----
            Note
                description13
            See Also
            --------
            also see
            """
    p.parse(text)
    print(p)


if __name__ == '__main__':
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:50:44.779964
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse("""\
        Return the cumulative density function of the standard normal distribution.
        If `log` is True, the natural logarithm of the probability density
        is returned.
        """
    )
    assert docstring.short_description == "Return the cumulative density function of the standard normal distribution."
    assert docstring.long_description == "If `log` is True, the natural logarithm of the probability density\n" + \
        "is returned."


# Generated at 2022-06-13 19:50:54.974055
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This class represents an abstract base class (ABC) for
    probability distributions.

    Notes
    -----
    The ``A`` class defines the interface of interest and all methods
    of this class raise ``NotImplementedError``.

    The ``B`` class is a fully functional implementation that can
    be used as a mixin and/or base class.

    The ``C`` defines the ``A`` interface completely abstract.
    It should be used as the base class for all distribution ABCs.

    Methods and properties defined in ``B`` but not in ``A`` can be
    overridden by subclasses of ``C``.

    Attributes
    ----------
    *something*: list
        This contains something
    chances : int
        The number of chances
    """

    parser = NumpydocParser()
    parsed = parser.parse(text)



# Generated at 2022-06-13 19:51:07.616292
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    description = """
This is a description.

    Nested code block.

    More nested code block.

Last line of description."""
    meta_text = """
Params
    arg1
        arg1 description
    arg2
        arg2 description

Attributes
    attr1
        attribute 1
    attr2
        attribute 2

Raises
    ValueError
        Raised when something
        raises a ValueError
    Exception
        Generic exception
"""

    docstring = description + meta_text

    doc = NumpydocParser().parse(docstring)

    assert doc.short_description == "This is a description."
    assert doc.long_description == """
    Nested code block.

    More nested code block.

Last line of description."""

    assert doc.blank_after_short_description == True

# Generated at 2022-06-13 19:51:18.714927
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    npd = NumpydocParser()