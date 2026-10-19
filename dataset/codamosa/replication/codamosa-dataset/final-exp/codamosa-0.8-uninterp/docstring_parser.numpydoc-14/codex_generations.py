

# Generated at 2022-06-13 19:42:05.197362
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    # Test multiple sections
    test_string = """\
Summary line.

    Extended description.

Parameters
----------
arg1 : int
    Description of `arg1`
arg2 : str
    Description of `arg2`

Other Parameters
----------------
arg3 : dict
    Description of `arg3`

Returns
-------
int
    Description of return value
"""

# Generated at 2022-06-13 19:42:13.180582
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring, DocstringParam, DocstringReturns, DocstringMeta
    from .numpydoc import parse
    doctest_string = """Returns
    -------
    numpy array
        A 2D numpy array
    """
    another_docstring = """yields numpy array
        A 2D numpy array
    """
    assert parse(doctest_string) == Docstring(
        short_description=None,
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[
            DocstringReturns(
                args=["returns"],
                description="A 2D numpy array",
                type_name="numpy array",
                is_generator=False,
                return_name=None)
        ]
    )

# Generated at 2022-06-13 19:42:25.757809
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_type = "NumpydocParser"

    parser = NumpydocParser()

    def test_description(description, short, long, short_blank, long_blank):
        d = parser.parse(description)
        assert d.short_description == short
        assert d.long_description == long
        assert d.blank_after_short_description == short_blank
        assert d.blank_after_long_description == long_blank

    test_description("""To be or not to be""",
        short = "To be or not to be",
        long = None,
        short_blank = False,
        long_blank = False)


# Generated at 2022-06-13 19:42:35.308546
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = []
    text.append(inspect.cleandoc("""\
        a simple doc string"""))
    text.append(inspect.cleandoc("""\
        a simple doc string
        with a more detailed description
        and some additional text which
        might span multiple lines."""))
    text.append(inspect.cleandoc("""\
        a simple doc string

        with a more detailed description
        and some additional text which
        might span multiple lines."""))
    text.append(inspect.cleandoc("""\
        a simple doc string

        with a more detailed description
        and some additional text which
        might span multiple lines.

        Additional text can be separated
        by a single blank line."""))

# Generated at 2022-06-13 19:42:42.618398
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:42:50.895850
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """A title.
    a short description
    :param param1: An input parameter
    :param param2: Another input parameter
    :returns: a return value
    
    A long description
    """
    docsting = NumpydocParser().parse(text)
    assert type(docsting) == Docstring
    assert docsting.short_description == "A title."
    assert docsting.long_description == 'a short description\n\nA long description'
    assert docsting.blank_after_short_description == True
    assert docsting.blank_after_long_description == True
    assert len(docsting.meta) == 2
    assert docsting.meta[0].description == "An input parameter"
    assert docsting.meta[1].description == "a return value"

# Generated at 2022-06-13 19:43:00.979966
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    s = " The short description.\n\nThe long description.\n\nParams\n------\narg_name\n    arg_description\narg2 : type, optional\n    descriptions can also span...\n    ... multiple lines\n\nRaises\n------\nValueError\n    A description of what might raise ValueError\n\nReturns\n-------\nreturn_name : type\n    A description of this returned value\nanother_type\n    Return names are optional, types are required"
    d = parse(s)
    assert d.short_description == "The short description."
    assert d.long_description == "The long description."
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == True

# Generated at 2022-06-13 19:43:12.931383
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    A function that takes in a number of names and returns the number of
    unusual last names they have.

    Parameters
    ----------
    num_names : number of names
        The number of names to process.

    Returns
    -------
    count : number of unusual names
        The number of unusual last names in the given list of names.
    """
    docstring = NumpydocParser().parse(text)
    assert docstring['description'] == "A function that takes in a number of names and returns the number of unusual last names they have."
    assert docstring['params'] == [{'type_name': 'number of names', 'description': 'The number of names to process.', 'is_optional': False, 'arg_name': 'num_names'}]

# Generated at 2022-06-13 19:43:24.093603
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test case 1: parse a null or empty string
    assert NumpydocParser().parse('') == Docstring()

    # Test case 2: parse a docstring with default sections
    text = '''
        Parameters
        ----------
        step_index : object
            The index of the step to be retrieved, 0-based.
        Returns
        -------
        list of steps
        '''
    assert (NumpydocParser().parse(text) ==
            Docstring(meta=[
                DocstringMeta([
                    'param', 'step_index'],
                    description='The index of the step to be retrieved, 0-based.',
                    arg_name='step_index', type_name='object'),
                DocstringMeta(['returns'], description='list of steps')
            ]))

    # Test case 3: parse a docstring with

# Generated at 2022-06-13 19:43:33.845533
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    One line description of the function.

    More detailed description.

    Parameters
    ----------
    arg1
        The first argument.
    arg2 : int
        The second argument.
    arg3 : (type, optional)
        The third argument.

    Returns
    -------
    Some return value.
    """

    parser = NumpydocParser()
    parsed_docstring = parser.parse(text)

    assert parsed_docstring.short_description == "One line description of the function."
    assert parsed_docstring.long_description == "More detailed description."
    assert parsed_docstring.blank_after_short_description == True
    assert parsed_docstring.blank_after_long_description == True

# Generated at 2022-06-13 19:43:43.840783
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    Parameters
    ----------
    x: int
        x description.
    v : float, optional
        The velocity at which the rocket is launched. Default is 100.

    Returns
    -------
    a : float
        The acceleration.
    '''
    NumpydocParser_parse(text)



# Generated at 2022-06-13 19:43:49.817070
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert str(parse("")) == '''<Docstring>
'''
    assert str(parse("foo")) == '''<Docstring>{
    short_description: 'foo'
}'''
    assert str(parse("""
foo

bar


baz

""")) == '''<Docstring>{
    short_description: 'foo'
    blank_after_short_description: True
    blank_after_long_description: True
    long_description: 'bar


baz
'
}'''

# Generated at 2022-06-13 19:43:59.843049
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    t = """First line
Second line, possibly over multiple lines

.. deprecated:: 1.0
    Second line of deprecation warning,
    possibly over multiple lines

Parameters
----------
param1 : type, optional
    Description of `param1`, which has type `type` and defaults to
    `None`.

Example
-------
Example following the "Example" section.

    >>> print('this is an example')
    this is an example

See Also
--------
The "See Also" section can contain arbitrary references,
e.g. :py:class:`~python:dict`, :py:func:`~python:sorted`, or
:py:class:`~builtins.list`.
"""
    a = NumpydocParser().parse(t)
    print("===short description===")
    print(a.short_description)


# Generated at 2022-06-13 19:44:09.077846
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def _test(text_input):
        return NumpydocParser().parse(text_input)

    # Single paragraph docstring
    assert _test("A docstring.") == Docstring(
        short_description="A docstring.", long_description=None, meta=[]
    )

    # docstring with a newline after short description
    assert _test("A docstring.\n") == Docstring(
        short_description="A docstring.",
        long_description=None,
        blank_after_short_description=True,
        meta=[],
    )

    # docstring with a newline after short description and newlines before and after long description

# Generated at 2022-06-13 19:44:16.434676
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:31.020548
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser=NumpydocParser()
    a = """
    This is a test function for NumpydocParser.parse method.
    This function should keep the description for the function and
    the data for the parameters.

    Parameters
        ----------
            a : int
                first parameter
            b : str
                second parameter
            c : float
                third parameter
    """
    parser.parse(a)
    # assert the result of parse from the input
    assert parser.parse(a).short_description =="This is a test function for NumpydocParser.parse method. This function should keep the description for the function and the data for the parameters."
    assert parser.parse(a).meta[0].description =="first parameter"
    assert parser.parse(a).meta[1].description =="second parameter"

# Generated at 2022-06-13 19:44:40.750513
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    class TestDeprecationSection(Section):
        def parse(self, text: str) -> T.Iterable[DocstringDeprecated]:
            for line in text.split("\n"):
                yield DocstringDeprecated(
                    args=[self.key], description=_clean_str(line)
                )

    # test docstring

# Generated at 2022-06-13 19:44:49.506564
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Testing NumpydocParser.parse()"""
    numpydoc_parser = NumpydocParser()

# Generated at 2022-06-13 19:44:57.367921
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:08.727045
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:22.457138
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    
    docstring = '''
    A function that computes the mean and standard deviation
    
    Parameters
    ----------
    data : array_like
        An array like object containing the sample data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which the means are computed. The default is to
        compute the mean of the flattened array.
    
    Returns
    -------
    m : float
        The median of the array elements along the given axis.
    v : float
        The median of squares of the array elements along the given axis.

    '''

    parsed_docstring = parse(docstring)

    print(parsed_docstring.meta)



# Generated at 2022-06-13 19:45:31.615313
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # Parse only short description
    docstring = parser.parse('short description')
    assert docstring.short_description == 'short description'
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 0

    # Parse only long description, with empty line in the middle
    text = 'short description\n\nlong\ndescription'
    docstring = parser.parse(text)
    assert docstring.short_description == 'short description'
    assert docstring.long_description == 'long\ndescription'
    assert docstring.blank_after_short_description
    assert not docstring.blank_after_long_description
    assert len

# Generated at 2022-06-13 19:45:40.623976
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Summary line

    Extended description

    Parameters
    ----------
    arg_name: type, optional
        arg_description.
    arg_2: int, optional defaults to 3
        arg_2 description
    arg_3: {'yes', 'no'}, optional
        arg_3 description

    Attributes
    ----------
    attr1
        description of attr1

    Returns
    -------
    str
        description of return value
    str, optional
        description of optional return value
    """
    doc = NumpydocParser().parse(text)
    return doc



# Generated at 2022-06-13 19:45:51.552569
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:02.952145
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:14.013186
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:26.634956
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = ''' My function
    =================

        Parameters
        ----------
        a : int
            The first parameter.
        b : float
            The second parameter.
        c : array, optional
            The third parameter, defaults to c.

        Returns
        -------
        x : float
            The first returned value.
        y : int
            The second returned value.
        z : bool
            If x > y.

    My function does something similar to...
    '''
    ret = NumpydocParser().parse(text)
    assert ret.short_description == 'My function'
    assert ret.blank_after_short_description == True
    assert ret.blank_after_long_description == True

# Generated at 2022-06-13 19:46:37.255114
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:46.330501
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    input_text = """A short summary

Longer multi-line description of what this thing does.

This can also have references and other stuff after the long description

This is an example.

    >>> i = 123
    >>> print(i)
    123

.. deprecated:: 1.2
    This function has been moved to the module ``numpy.testing.nosetester``.

Parameters
----------
inp : type
    description

Raises
------
TypeError
    Because the input is not a string

References
----------
    Reference [1]_, [2]_, [3]_

.. [1] http://example.com
.. [2] http://example.com
.. [3] http://example.com

See Also
--------
    - other_func
    - other_func : description


"""

    expected

# Generated at 2022-06-13 19:46:58.255823
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
First line of the docstring

This is the first paragraph of the description.

This is the second paragraph of the description.


Parameters
----------
param1 : {'a', 'b'}, optional
    This is the first parameter.

param2 : bool
    This is the second parameter.

    It can have multiple paragraphs.

Returns
-------
return1
    The first return value.

return2 : int
    The second return value.
"""
    doc = parse(docstring)

    assert isinstance(doc, Docstring)
    assert doc.short_description == "First line of the docstring"
    assert doc.blank_after_short_description is True
    assert doc.long_description == "This is the first paragraph of the description.\n\nThis is the second paragraph of the description."
    assert doc

# Generated at 2022-06-13 19:47:09.788553
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """
    An example of using numpydoc's parse function.

    Parameters
    ----------
    a : type
        First parameter
    b : type, optional
        Second parameter
    """
    parsed = parser.parse(text)
    assert len(parsed.meta) == 2
    assert parsed.short_description == "An example of using numpydoc's parse function."
    assert parsed.long_description == "First parameter\n\nSecond parameter"

# Generated at 2022-06-13 19:47:19.994809
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:30.030189
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    myNDP = NumpydocParser()

# Generated at 2022-06-13 19:47:34.483934
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    s = NumpydocParser()
    assert s.parse("") == Docstring()
    assert s.parse("Hello, world") == Docstring(
    short_description="Hello, world",
    long_description=None,
    blank_after_short_description=False,
    blank_after_long_description=False,
    meta=[],
)


# Generated at 2022-06-13 19:47:46.337172
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:57.715978
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    """A docstring.

    Short description.

    Long description, which may go to multiple lines.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str, optional
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    Examples
    --------
    A code example:

    >>> print("Hello world")
    Hello world
    """
    '''
    docstring = NumpydocParser().parse(text)
    print(docstring.short_description)
    print(docstring.long_description)
    assert len(docstring.meta.keys()) == 1
    assert len(docstring.meta['param']) == 2
    assert len(docstring.meta['returns']) == 1

# Generated at 2022-06-13 19:48:00.850813
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """Parse the numpy-style docstring into its components.
    :returns: parsed docstring
    """
    NumpydocParser().parse(text)

# Generated at 2022-06-13 19:48:13.497799
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:16.802774
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import numpydoc
    docstring = """
        This is a test for the NumpydocParser class.
        This test will be used to check the autotests.py file.

        Parameters
        ----------
        arg1 : int
            Lowest value in the range.

        arg2 : int
            Highest value in the range.

        Returns
        -------
        int
            A random integer between arg1 and arg2.
        """
    result = numpydoc.NumpydocParser().parse(docstring)
    assert result

# Generated at 2022-06-13 19:48:33.276714
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def f():
        """
            Parameters
            ----------
            key1: type, optional
                value can extend over multiple lines,
                and will be cleaned and dedented
            key 2: type, optional
                value2
                <fuzzy>

            Returns
            -------
            type
                value
        """
    parsed = parse(inspect.getdoc(f) or "")
    print(parsed.meta)
    assert parsed.meta[0].args == ['param', 'key1']
    assert parsed.meta[1].args == ['param', 'key 2']
    assert parsed.meta[2].args == ['returns']
    assert parsed.short_description is None
    assert parsed.long_description is None
    assert parsed.blank_after_short_description is False

# Generated at 2022-06-13 19:48:47.791790
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:58.142535
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
        A short summary

        A longer, more verbose summary

        Parameters
        ----------
        arg1: type
            first argument

        arg2 : type, optional
            second argument

        Returns
        -------
        return_name : type
            a return value
        """

    # TODO: Verify this test
    doc = NumpydocParser().parse(text)
    assert doc.short_description == "A short summary"
    assert doc.long_description == "A longer, more verbose summary"
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True


# Generated at 2022-06-13 19:49:08.005120
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Examines statistics of a dataset
        1. Calculates mean of a dataset
        2. Calculates variance of a dataset
    Parameters
    ----------
    dataset : sequence of numbers
        An arbitrary dataset of numbers
    Returns
    -------
    mean : float
        Sample mean
    variance : float
        Sample variance
    """
    parser = NumpydocParser()
    docstring = parser.parse(text)
    assert docstring.short_description == "Examines statistics of a dataset"
    assert docstring.long_description == "1. Calculates mean of a dataset\n2. Calculates variance of a dataset"
    assert len(docstring.meta) == 2
    assert docstring.meta[0] == DocstringMeta(['param', 'dataset'], description='An arbitrary dataset of numbers')

# Generated at 2022-06-13 19:49:13.608062
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
        Foo

        Returns
        -------
        str:
            The test string.
    """
    r = NumpydocParser().parse(text)
    assert r.short_description == 'Foo\n'
    assert r.meta[0].type_name == 'str'



# Generated at 2022-06-13 19:49:22.193506
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:29.708338
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert NumpydocParser().parse(
        """
    This is a short summary.

    This is the long description.
    It has two paragraphs.

    This is the second paragraph.
    """.strip()
    ) == Docstring(
        short_description="This is a short summary.",
        long_description="This is the long description. It has two paragraphs.\n\nThis is the second paragraph.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )



# Generated at 2022-06-13 19:49:40.597213
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    def test(text, expected_ret):
        ret = parser.parse(text)
        assert ret == expected_ret

    test(
        """
        Simple title.
        """,
        Docstring(
            short_description="Simple title.",
            long_description=None,
            blank_after_short_description=True,
            blank_after_long_description=False,
            meta=[],
        ),
    )

# Generated at 2022-06-13 19:49:53.101431
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:01.871845
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Summary line.

    Extended description. Extended description line two.

    Parameters
    ----------
    arg1 : int
        Description of `arg1`
    arg2 : str
        Description of `arg2`
    arg3 (optional) : bool
        Description of `arg3`.

    Raises
    ------
    KeyError
        When a key error
        is encountered.
    OtherError
        When an other error
        is encountered.

    Warns
    -----
    Warning
        When a warning
        is triggered.
    """
    text = inspect.cleandoc(text)
    nd_parser = NumpydocParser()

    # test parsing without adding a section
    docstring = nd_parser.parse(text)
    assert docstring.short_description == "Summary line."

# Generated at 2022-06-13 19:50:10.847865
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # parses empty docstring
    assert parse("") == Docstring()

    # parses description only
    doc = parse("The first line.")
    assert doc.short_description == "The first line."
    assert doc.long_description == None
    assert len(doc.meta) == 0

    # parses one-liner
    doc = parse("A function.\n")
    assert doc.short_description == "A function."
    assert doc.long_description == None
    assert len(doc.meta) == 0

    # parses long description
    doc = parse("A function.\n\nLong description.\n")
    assert doc.short_description == "A function."
    assert doc.long_description == "Long description."
    assert len(doc.meta) == 0

    # parses long description with empty first line
   

# Generated at 2022-06-13 19:50:29.143628
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
  # Testing the part that creates new Docstring()
  # Testing with no comment
  s = NumpydocParser()
  d = s.parse("")
  assert d.short_description == None
  assert d.long_description == None
  assert d.blank_after_long_description == False
  assert d.blank_after_short_description == False
  # Testing when the string is blank
  d = s.parse("     ")
  assert d.short_description == None
  assert d.long_description == None
  assert d.blank_after_long_description == False
  assert d.blank_after_short_description == False

  # Testing the part that splits into short and long descriptions
  # Testing with no \n
  d = s.parse("This is my docstring - it is only a string, but I like it")

# Generated at 2022-06-13 19:50:40.050608
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    simple test for NumpydocParser.parse()
    """
    test_docstring = '''
    Parameters
    ----------
    x : array_like
        The x-coordinates of the M sample points (x[i], y[i]).

    y : array_like
        The y-coordinates of the sample points (x[i], y[i]).
    '''

    nd_parser = NumpydocParser(None)
    nd_parser.parse(test_docstring)

    nd_parser.sections['Parameters'].title = "Parameters"
    nd_parser.sections['Parameters'].key = 'param'
    nd_parser.sections['Parameters'].parse(test_docstring)


# Generated at 2022-06-13 19:50:48.482351
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    #This is an example of docstring with title Examples
    text = """This is an example of docstring with title Examples.
             .. Examples::
             >>> print ("examples")
             examples
             """
    doc = parser.parse(text)
    assert doc.short_description == "This is an example of docstring with title Examples."
    assert doc.long_description == ">>> print (\"examples\")\nexamples"
    assert doc.meta[0].key == "examples"
    assert doc.meta[0].args == ["examples"]


# Generated at 2022-06-13 19:50:53.430432
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''Single line description

            Long description.

            Parameters
            ----------
            arg1 : int
                Description of arg1.
            arg2 : List[int]
                Description of arg2.

            Returns
            -------
            List[str]
                Description of return value.
    '''

    NumpydocParser().parse(docstring)

# Generated at 2022-06-13 19:51:01.245538
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
     Load the data.

     Parameters
     ----------
     str
        The name of the file to load.
     Returns
     -------
     bool
        True.
    """
    assert isinstance(NumpydocParser().parse(text), Docstring)
    text = """
    Load the data.

    Parameters (long).

    Returns
    -------
    bool
        True.
    """
    assert isinstance(NumpydocParser().parse(text), Docstring)

# Generated at 2022-06-13 19:51:13.453503
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = """
    simple string
    """
    result = parser.parse(docstring)
    assert (not result.short_description) and (result.long_description == '')

    docstring = """
    simple string
    """
    result = parser.parse(docstring)
    assert (result.short_description == 'simple string') and (not result.long_description)

    docstring = """
    Simple string
    Long description
    """
    result = parser.parse(docstring)
    assert (result.short_description == 'simple string') and (result.long_description == 'Long description')

    docstring = """
    Simple string
    Long description
    Long description

    """
    result = parser.parse(docstring)

# Generated at 2022-06-13 19:51:23.591307
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    expected_description = "This is a docstring for a function."
    expected_short_description = "This is a docstring for a function."
    expected_long_description = "This is a multiline docstring."
    expected_blank_after_short_description = True
    expected_blank_after_long_description = True