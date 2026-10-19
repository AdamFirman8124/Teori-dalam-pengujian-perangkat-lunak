

# Generated at 2022-06-13 19:31:17.953899
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
        Parameters
        ----------
        x: int
            Its a integer!
        y: float
            Its a floating point!
        """
    print(GoogleParser().parse(text))
    # Result:
    # Docstring(short_description='', blank_after_short_description=True, blank_after_long_description=False, long_description='', meta=[DocstringParam(args=['param', 'x: int'], description='Its a integer!', arg_name='x', type_name='int', is_optional=None, default=None), DocstringParam(args=['param', 'y: float'], description='Its a floating point!', arg_name='y', type_name='float', is_optional=None, default=None)])


# Generated at 2022-06-13 19:31:30.294021
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    if __name__ == "__main__":
        docstring = '''Sums two numbers.
        
        Args:
            a (int): first number to add
            b (int): second number to add
        Returns:
            int: the sum
        '''

        doc = parse(docstring)
        # print(doc)
        # Expected output:
        #
        # short_description          Sums two numbers.
        # long_description           None
        # blank_after_short_description True
        # blank_after_long_description  None
        # meta                       [DocstringParam(args=['Args', 'a (int): first number to add\nb (int): second number to add'], arg_name='a', arg_name_description='first number to add', description='first number to add', type_name='int', is

# Generated at 2022-06-13 19:31:42.144168
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''\
    Args:
        arg: The first argument.
        arg2 (int): The second argument
    Kwargs:
        kwarg: The first keyword argument.
            There can be multiple paragraphs in this one.
        kwarg2 (list): The second keyword argument.
    '''
    result = GoogleParser().parse(text)
    assert result.description == text
    assert str(result) == text
    assert result.short_description == ''
    assert result.long_description is None
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is False

    assert len(result.meta) == 4
    assert result.meta[0].args == ['param', 'arg']
    assert result.meta[0].description == 'The first argument.'

# Generated at 2022-06-13 19:31:48.537886
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text="Method Summary\nThis is method summary.\n\nArgs\n  int: number.\n  str: string.\n\nReturns\n  str: the string.\n\nAttribute\n  int: number.\n\nRaise\n  Exception: exception."
    assert(GoogleParser().parse(text).short_description=="Method Summary")
    assert(GoogleParser().parse(text).long_description=="This is method summary.")
    assert(GoogleParser().parse(text).blank_after_short_description==True)
    assert(GoogleParser().parse(text).blank_after_long_description==False)
    assert(GoogleParser().parse(text).meta[0].args==["param", "int"])
    assert(GoogleParser().parse(text).meta[0].description=="number.")

# Generated at 2022-06-13 19:31:53.533833
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = '''
    Hello

    :param int a: First parameter
    '''
    assert parser.parse(text) == Docstring(
        short_description="Hello",
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[
            DocstringParam(
                args=["param", "int a"],
                description="First parameter",
                arg_name="a",
                type_name="int",
                is_optional=None,
                default=None,
            )
        ],
    )



# Generated at 2022-06-13 19:32:07.672621
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import numpy as np
    import types

    def f(x: int, y: float = np.pi, z: float = None) -> int:
        """
        docstring

        :param x: first param
        :param y: second param
        :param z: third param
        :returns: z
        """

    f = types.FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)
    f.__doc__ = f.__doc__


# Generated at 2022-06-13 19:32:17.240939
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def func(arg):
        """This is a short description

        This is a long description.

        Args:
            arg: This is arg description.

        Returns:
            int. This is return description.
        """
        return arg

    docstring = parse(inspect.getdoc(func))
    assert docstring.short_description == 'This is a short description'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args[0] == 'param'
    assert docstring.meta[0].args[1] == 'arg'
    assert docstring.meta[0].description == 'This is arg description.'
    assert docstring.meta[1].args[0] == 'returns'

# Generated at 2022-06-13 19:32:26.177738
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == parse.__annotations__
    assert parse("summary\n") == parse.__annotations__
    assert parse("summary") == parse.__annotations__
    assert parse("summary\nlong description\n") == parse.__annotations__

    assert parse("summary\n\nlong description\n\nArgs:\n  arg1:\n  arg2:\n") == parse.__annotations__
    assert parse("summary\n\nlong description\n\nArgs:\n  arg1:   \n  arg2:   \n") == parse.__annotations__
    assert parse("summary\n\nlong description\n\nArgs:\n  arg1:  desc1\n  arg2:  desc2\n") == parse.__annotations__

# Generated at 2022-06-13 19:32:38.756904
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert_equal(GoogleParser().parse(test_text_1), res_test_text_1)
    assert_equal(GoogleParser().parse(test_text_2), res_test_text_2)
    assert_equal(GoogleParser().parse(test_text_3), res_test_text_3)
    assert_equal(GoogleParser().parse(test_text_4), res_test_text_4)
    assert_equal(GoogleParser().parse(test_text_5), res_test_text_5)
    assert_equal(GoogleParser().parse(test_text_6), res_test_text_6)
    assert_equal(GoogleParser().parse(test_text_7), res_test_text_7)
    assert_equal(GoogleParser().parse(test_text_8), res_test_text_8)

# Generated at 2022-06-13 19:32:48.416308
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:33:08.389115
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstr = '''
  This is a Google-style docstring that is intended to demonstrate
  Google-style docstrings.  The purpose of this docstring is to show
  what such a docstring might look like, to provide an example of the
  structure and content of such a docstring.  It is not intended to
  accurately represent what such a docstring for this function would
  look like.

  Args:
    arg1: The first value.
      This line is indented two spaces to show the hanging indent. This
      docstring is intended to demonstrate Google-style docstrings, not to
      accurately represent what the docstring for this function would look
      like.
    arg2: The second value.
    arg3 (int): The third value.

  Returns:
    bool: The return value. True for success, False otherwise.
'''

# Generated at 2022-06-13 19:33:09.900144
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Things to test:
    1. 
    """
    

# Generated at 2022-06-13 19:33:20.054616
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Example 1:
    text = """

    Returns an iterator over the elements of a container.

    Returns:
        container: The container to iterate over.
        reverse: If True, iterate backwards.
    """

    res = GoogleParser().parse(text)
    assert res.short_description == "Returns an iterator over the elements of a container."
    assert res.blank_after_short_description == False
    assert res.long_description == None
    assert res.blank_after_long_description == False
    assert len(res.meta) == 2
    assert res.meta[0].key == "returns"
    assert res.meta[0].type == SectionType.SINGULAR_OR_MULTIPLE
    assert res.meta[0].title == "Returns"

# Generated at 2022-06-13 19:33:30.640122
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
    This is the docstring for GoogleParser.parse().
    It is used to parse a Google-style docstring into its components.

    Sphinx is one tool that can be used to format
    Google-style docstrings for display.

    Args:
        text: the docstring to parse
    Returns:
        A Docstring object
    """

    docstring = GoogleParser().parse(text)

    assert docstring.short_description == "This is the docstring for GoogleParser.parse()"
    assert 'blank_after_short_description' not in docstring
    assert docstring.long_description == "It is used to parse a Google-style docstring into its components.\n\nSphinx is one tool that can be used to format\nGoogle-style docstrings for display."
    assert docstring.blank_after_long

# Generated at 2022-06-13 19:33:44.793997
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = "Example of a Google-style Python docstring.\n\nArgs:\n    arg1 (int, optional): The first argument.\n    arg2 (str, optional): The second argument. Only one\n        sentence allowed.\n    *args: Variable length argument list.\n    **kwargs: Arbitrary keyword arguments.\n\nRaises:\n    AttributeError: The ``Raises`` section is a list of all exceptions\n        that are relevant to the interface.\n    ValueError: If `param2` is equal to `param1`.\n\nReturns:\n    bool: The return value. True for success, False otherwise.\n    \n    \n    \n        """
    doc = ""
    g = GoogleParser()
    result = g.parse(doc)
    assert result == Docstring()

# Unit

# Generated at 2022-06-13 19:33:56.923380
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unittest of GoogleParser.parse"""

    assert str(GoogleParser().parse('')) == \
        'Docstring(short_description=None, long_description=None, blank_after_short_description=None, blank_after_long_description=None, meta=[])'

    assert str(GoogleParser().parse('"""Simple example."""')) == \
        'Docstring(short_description=\'Simple example.\', long_description=None, blank_after_short_description=None, blank_after_long_description=None, meta=[])'


# Generated at 2022-06-13 19:34:02.800382
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    with open('./test_GoogleParser_parse.txt', 'r') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]
        text = '\n'.join(lines)
    ret = parser.parse(text)
    print(ret.meta)


# Generated at 2022-06-13 19:34:05.082628
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # TODO write
    raise NotImplementedError


# Generated at 2022-06-13 19:34:13.046531
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('') == Docstring()
    assert GoogleParser().parse('Simple String') == Docstring(
        long_description='Simple String',
        short_description='Simple String',
        blank_after_long_description=True,
        blank_after_short_description=False)
    assert GoogleParser().parse('Simple String\nAnother string') == Docstring(
        long_description='Simple String\nAnother string',
        short_description='Simple String',
        blank_after_long_description=True,
        blank_after_short_description=False)

# Generated at 2022-06-13 19:34:23.723884
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring
    assert GoogleParser().parse(None) == Docstring()
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("\n") == Docstring()
    assert GoogleParser().parse("\n\n") == Docstring()
    assert GoogleParser().parse("\n\n\n") == Docstring()
    assert GoogleParser().parse("\n\n\n\n") == Docstring()
    assert GoogleParser().parse("\n\n\n\n\n") == Docstring()
    assert GoogleParser().parse("\n\n\n\n\n\n") == Docstring()
    assert GoogleParser().parse("\n\n\n\n\n\n\n") == Docstring()
    assert GoogleParser

# Generated at 2022-06-13 19:34:37.935930
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Setup
    docstring = "Short summary.\n\nLong description.\n\nArgs:\n  arg1: \
    First argument.\n  arg2: Second argument. Defaults to None.\nReturns: \
    Some value.\n"
    # Expected outcome
    expected_object = Docstring()
    expected_object.short_description = "Short summary."
    expected_object.blank_after_short_description = True
    expected_object.blank_after_long_description = True
    expected_object.long_description = "Long description."

# Generated at 2022-06-13 19:34:43.933252
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert(GoogleParser().parse('') == Docstring())
    assert(GoogleParser().parse('no title') == Docstring())
    assert(GoogleParser().parse('no title\n') == Docstring())
    assert(GoogleParser().parse('\n') == Docstring())
    assert(GoogleParser().parse('\n\n') == Docstring())
    assert(GoogleParser().parse('title:\n') == Docstring())
    assert(GoogleParser().parse('title:\n\n') == Docstring())
    assert(GoogleParser().parse('\nshort description\n') == \
        Docstring(short_description='short description'))
    assert(GoogleParser().parse('no title\nshort description\n') == \
        Docstring(short_description='short description'))

# Generated at 2022-06-13 19:34:53.159840
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("------test_GoogleParser_parse------")
    parser = GoogleParser()
    text = '''
    pytest
    
    Tests for `pytest` module.
    
    :copyright: (c) 2020 by Qix.
    :license: MIT, see LICENSE for more details.
    
    Attributes
    ----------
    NAME: str
        The name of pytest.
    version: str
        The version of pytest.
    AUTHOR: str
        The name of author.
    '''
    res = parser.parse(text)
    print("short_description:", res.short_description)
    print("long_description:", res.long_description)
    print("meta:", res.meta)



# Generated at 2022-06-13 19:35:07.943658
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Test HTML creation of GoogleParser.parse,
    the read method of class GoogleParser
    """
    googleParser = GoogleParser()

# Generated at 2022-06-13 19:35:09.457797
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """No unit test for method parse of class GoogleParser"""


# Generated at 2022-06-13 19:35:13.980136
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    if __name__ == '__main__':
        print('Testing GoogleParser.parse()')
        docstrings = [
            '''Summarize arguments.
            Args:
                x: First value.
                y: Second value.
            Returns:
                Sum of x and y.'''
        ]
        for docstring in docstrings:
            print(GoogleParser().parse(docstring))

# Generated at 2022-06-13 19:35:30.090580
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse("This is return value")
    assert docstring.short_description == "This is return value"
    assert docstring.long_description is None
    assert len(docstring.meta) == 0

    docstring = GoogleParser().parse("This is return value\n\nLong description")
    assert docstring.short_description == "This is return value"
    assert docstring.long_description == "Long description"

    docstring = GoogleParser().parse("This is return value\nLong description")
    assert docstring.short_description == "This is return value"
    assert docstring.long_description == "Long description"

    docstring = GoogleParser().parse(
        "This is return value\n\nLong description\n\n"
    )

# Generated at 2022-06-13 19:35:34.712880
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()

# Generated at 2022-06-13 19:35:44.391657
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_GoogleParser_parse.__doc__ = GoogleParser.parse.__doc__
    test_googleParser = GoogleParser()
    docstring = test_googleParser.parse.__doc__
    result = test_googleParser.parse(docstring)
    
    #Testing the values stored in the parsed-docstring meta
    for meta in result.meta:
        if(meta.__class__ == DocstringReturns):
            #Test if the return type is correct
            if(meta.args[1].split(" ")[0] != 'str'):
                raise AssertionError("Parse() stored the wrong return-type in DocstringReturns")
    
    #Test if the values stored in the parsed-docstring are correct
    if(result.long_description != "Parse the Google-style docstring into its components."):
        raise Assertion

# Generated at 2022-06-13 19:35:51.291517
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Single line summary

    Single line description.

    Long
    multiline
    description.

    Args:
        arg1: The first argument.
        arg2 (str): The second argument. (default: None)

    Returns:
        str: The return value. (default: "return")

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    """
    docstring = GoogleParser().parse(text)
    print(docstring)

# Generated at 2022-06-13 19:36:02.627734
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test case 1
    text0 = """Short description.

    Long description.

    Args:
        arg1: arg 1 description
        arg2: arg 2 description
    
    Returns:
        something
    """
    docstring0 = parse(text0)
    assert docstring0.short_description == "Short description."
    assert docstring0.long_description == "Long description."
    assert docstring0.blank_after_short_description == True
    assert docstring0.blank_after_long_description == False
    assert len(docstring0.meta) == 2
    
    assert docstring0.meta[0].args[0] == "param"
    assert docstring0.meta[0].args[1] == "arg1"
    assert docstring0.meta[0].description == "arg 1 description"
   

# Generated at 2022-06-13 19:36:12.893928
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_string = """\
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string
    This is a test string

    Args:
        arg_1: The first argument
        arg_2: The second argument
        arg_3: The third argument
        arg_4: The forth argument
    """
    obj = GoogleParser()
    function = obj.parse


# Generated at 2022-06-13 19:36:23.732792
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '''Returns a list of tuples, where each tuple is a pair of elements from the two\nlists. The returned list is truncated in length to the length of the shorter of\nthe two input lists.\n\nThe list returned is not guaranteed to be in any specific order, even if the\ninput lists are sorted.'''

# Generated at 2022-06-13 19:36:26.976496
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
        This is a test for the Google style docstring
        :param int x: The x vector.
        :param int y: The y vector.
        :returns: The x + y vector.
        '''
    result = GoogleParser().parse(text)
    print(result)


# Generated at 2022-06-13 19:36:41.659296
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises

    def assert_parsed_equal(glob, except_text):
        def check(text, expected):
            actual = parse(text)
            assert actual == expected

        if isinstance(glob, list):
            for (text, expected) in glob:
                check(text, expected)
        elif isinstance(glob, tuple):
            text = glob[0]
            expected = glob[1]
            check(text, expected)
        elif isinstance(glob, str):
            text = glob
            expected = except_text
            check(text, expected)

    # Simple examples

# Generated at 2022-06-13 19:36:48.362934
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:00.313204
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringReturns
    from .common import DocstringRaises
    from .common import DocstringParam
    from .common import DocstringMeta

    text = """
    This is a method.

    Args:
        param1: This is a first param.
        param2: This is a second param.

    Returns:
        This is a description of what is returned.
        This can span multiple lines.
    """

# Generated at 2022-06-13 19:37:09.018125
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''
    Mean squared error regression loss
    Parameters
    ----------
    y_true : tensor_like
        Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred : tensor_like
        The predicted values. shape = `[batch_size, d0, .. dN]`.
    sample_weight : tensor_like
        Sample weights. shape = `[batch_size, d0, .. dN]`. Defaults to 1.
    Returns
    -------
    Tensor with one scalar loss entry per sample.
    '''
    # print(GoogleParser().parse(doc))
    # print(GoogleParser().parse('Test'))
    # print(GoogleParser().parse('Test\n'))
    # print(GoogleParser().parse('Test\n\n'))

# Generated at 2022-06-13 19:37:12.576813
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    doc = "A Google style docstring."
    docstring = GoogleParser().parse(doc)

    assert docstring.short_description == "A Google style docstring."
    assert docstring.blank_after_short_description == False
    assert docstring.long_description == None
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 0


# Generated at 2022-06-13 19:37:25.458897
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = "This is a docstring.\n\nyes\n\n"
    expected = Docstring(
        short_description="This is a docstring.",
        long_description="yes",
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[],
    )
    result = GoogleParser().parse(docstring)
    assert expected == result

    docstring = """

    Returns:
        str: yes hello

    """

# Generated at 2022-06-13 19:37:49.103697
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    docstring = inspect.cleandoc('''
    Parse the Google-style docstring into its components.

    Returns:
        Docstring: parsed docstring
    ''')
    assert GoogleParser().parse(docstring).short_description == "Parse the Google-style docstring into its components."
    assert GoogleParser().parse(docstring).long_description == "Returns:\tDocstring: parsed docstring"

    docstring = inspect.cleandoc('''
    First sentence.

    Second sentence.
    ''')
    assert GoogleParser().parse(docstring).short_description == "First sentence."
    assert GoogleParser().parse(docstring).long_description == "Second sentence."


# Generated at 2022-06-13 19:37:50.972386
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass
    # TODO


# Generated at 2022-06-13 19:37:57.943373
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''Parses Google-style docstrings.

    :return: parsed docstring
    '''
    assert GoogleParser().parse(text) == Docstring(short_description='Parses Google-style docstrings.', long_description=':return: parsed docstring', blank_after_short_description=False, blank_after_long_description=True, meta=[DocstringMeta(args=['return'], description='parsed docstring')])

# Generated at 2022-06-13 19:38:00.819056
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text='''
    This module is an implementation of a synchronization barrier, which can
    be used for many different purposes.
    '''

    # Before the deprecated
    assert GoogleParser().parse(text)
    print("test_GoogleParser_parse() passed")


# Generated at 2022-06-13 19:38:07.672416
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    assert parser.parse(
        """Summary line.

    Extended description.

    Args:
        arg1 (int): Description of arg1
    """
    ) == Docstring(
        short_description="Summary line.",
        long_description="Extended description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[
            DocstringParam(
                args=["param", "arg1 (int)"],
                description="Description of arg1",
                arg_name="arg1",
                type_name="int",
                is_optional=None,
                default=None,
            )
        ],
    )


if __name__ == "__main__":
    import sys

    # Run unit tests

# Generated at 2022-06-13 19:38:18.225156
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    doc = '''This is a short description.
    This is a long description.

    This is the 2nd line of long description.

    :param str name: Name of the person.
    :param int age: Age of the person. Default to 23.
    :raises ValueError: If the name is empty.
    :raises ValueError: If the age is not positive.
    :returns: (name, age)
    '''
    parsed_doc = parser.parse(doc)
    assert parsed_doc.short_description == 'This is a short description.'
    assert parsed_doc.long_description == 'This is a long description.\n    This is the 2nd line of long description.'
    assert parsed_doc.blank_after_short_description == True
    assert parsed_doc.blank_after_long

# Generated at 2022-06-13 19:38:31.382431
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import inspect
    import pydocstring

    def fun(a: int, b, *args, c, d: "Foo", e: "Bar" = 1, f: "Kek", **kwargs):
        """This is a documentation string.

        Arguments:
        a -- An integer.
        b -- A string.
        *args -- Variable length argument list.
        c -- A required keyword-only argument.
        d -- An optional keyword-only argument (default: Foo).
        e -- An optional keyword-only argument (default: 1).
        f -- An optional keyword-only argument (default: None).
        **kwargs -- Arbitrary keyword arguments.

        Returns:
        We can return nothing.
        """

    ds = GoogleParser().parse(inspect.getdoc(fun))
    print(ds)



# Generated at 2022-06-13 19:38:40.407679
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def foo():
        """Print a string.

        :arg str s: string to be printed
        :returns: string length
        :raises ValueError: if s is None
        :Example:

        >>> foo('Hello World')
        11
        """
        pass

    parser = GoogleParser()
    docstring = parser.parse(foo.__doc__)
    assert docstring.short_description == "Print a string."
    assert docstring.long_description is None
    assert len(docstring.meta) == 3
    assert docstring.meta[0].args == ['param', 's (str)']
    assert docstring.meta[0].description == 'string to be printed'
    assert docstring.meta[1].args == ['returns']
    assert docstring.meta[1].description == 'string length'
    assert doc

# Generated at 2022-06-13 19:38:55.495921
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert (GoogleParser().parse('')) == Docstring()

# Generated at 2022-06-13 19:39:01.936745
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    print('Inside function test_GoogleParser_parse')
    GoogleParser().parse(text)

if __name__ == "__main__":
    text = """Description of function:

    This is a long description.

    Args:
      param1: The first parameter.
      param2: The second parameter.

    Returns:
      A dict with two outputs listed below.
      output1: The first output.
      output2: The second output.

    Raises:
      ValueError: if `param2` is equal to `param1`.
      TypeError: if param2 is not a string.

    """

    doc = GoogleParser().parse(text)

    assert doc.short_description == "Description of function"

    assert doc.long_description is not None
    assert doc.long_

# Generated at 2022-06-13 19:39:20.200243
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """

    :return:
    """
    import doctest
    doctest.run_docstring_examples(GoogleParser.parse, globals())

# Generated at 2022-06-13 19:39:23.701954
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .test_common import assertDocstringEquals, test_data
    text = """Sample Google style docstring.

Args:
    name: name.
    age: age.

Returns:
    return value.

Raises:
    ValueError: raises.
"""
    assertDocstringEquals(GoogleParser().parse(text), test_data["google"])



# Generated at 2022-06-13 19:39:29.387073
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''    Args:
        a (int): A integer.
        b (int): A integer.
        
        '''
    docstrings = GoogleParser().parse(text)
    assert docstrings.meta[0].arg_name == 'a'
    assert docstrings.meta[0].type_name == 'int'
    assert docstrings.meta[1].arg_name == 'b'
    assert docstrings.meta[1].type_name == 'int'

# Generated at 2022-06-13 19:39:34.893331
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = GoogleParser.parse(text='This is the short description.\n\nThis is line 1 of the long description.\nThis is line 2 of the long description.')
    assert_equal(text, 'This is the short description.')
    assert_equal(text, '\nThis is line 1 of the long description.\nThis is line 2 of the long description.')

    text = GoogleParser.parse(text='This is the short description.\n\nThis is the long description.')
    assert_equal(text, 'This is the short description.')
    assert_equal(text, '\nThis is the long description.')

    text = GoogleParser.parse(text='This is the short description.\nThis is the long description.')
    assert_equal(text, 'This is the short description.This is the long description.')

# Generated at 2022-06-13 19:39:44.329920
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class Test:
        def f():
            """ A test.

            :type arg: int
            :param arg: doc
            :returns: a number
            :raises ValueError: if the value is invalid

            """
            pass

# Generated at 2022-06-13 19:39:49.336617
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    method_name = "parse"
    description = "Google-style docstring parsing."

# Generated at 2022-06-13 19:39:59.935909
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    my_parser = GoogleParser()
    assert my_parser.parse("") == Docstring()
    assert my_parser.parse("Hello there.") == Docstring(
        short_description="Hello there."
    )
    assert my_parser.parse("Hello there.\nBlah.") == Docstring(
        short_description="Hello there.",
        long_description="Blah.",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert my_parser.parse("Hello there.\nBlah.\n\n") == Docstring(
        short_description="Hello there.",
        long_description="Blah.",
        blank_after_short_description=True,
        blank_after_long_description=True,
    )

# Generated at 2022-06-13 19:40:09.093859
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  g_parser = GoogleParser()
  print('test_GoogleParser_parse')
  docstring1 = '''
  Test function 1.

  This function just tests if the parsing is working.
  A longer description of the function

  Args:
    arg1 (int): The first parameter.
    arg2 (str): The seconds parameter. Defaults to 'value'.

  Returns:
    The return value. True for success, False otherwise.

  Raises:
    ValueError: if arg2 is None.
  '''
  parsed_docstring1 = g_parser.parse(docstring1)
  print(parsed_docstring1)

# Generated at 2022-06-13 19:40:17.732821
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    data = """
    """
    #positive tests
    assert GoogleParser().parse(data).short_description == None
    assert GoogleParser().parse(data).long_description == None
    assert GoogleParser().parse(data).blank_after_long_description == False
    assert GoogleParser().parse(data).blank_after_short_description == False
    data = """Short summary.
    Longer descripition.

    """
    assert GoogleParser().parse(data).short_description == "Short summary."
    assert GoogleParser().parse(data).long_description == "Longer descripition."
    assert GoogleParser().parse(data).blank_after_long_description == True
    assert GoogleParser().parse(data).blank_after_short_description == False

# Generated at 2022-06-13 19:40:22.932534
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """This is the short description.
    
    This is the long description.
    
    Args:
        single_arg (str): This is a single argument with type specification.
        
    Args:
        single_arg2 (int): This is a single argument with type specification.
    
    Raises:
        ValueError: when args not provided.
        
    Returns:
        str: The return description.
        
    """
    

# Generated at 2022-06-13 19:40:41.052964
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse("Returns the square roots of `x`.")
    assert docstring.short_description == "Returns the square roots of `x`."


# Generated at 2022-06-13 19:40:43.680916
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Arrange
    text = """Raises:
    ValueError: If `x` is negative.
"""
    # Act
    docstring = GoogleParser().parse(text)
    # Assert
    assert(isinstance(docstring.meta[0], DocstringRaises))
    assert(len(docstring.meta) == 1)


# Generated at 2022-06-13 19:40:49.132291
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
Blah blah blah

Args:
    first (str): first thing
    second (int, optional): second thing. Defaults to 1.

Example:

   some code
   some other code

Returns:
    (:class:`.ReturnType`): a return
"""

    result = GoogleParser().parse(text)
    assert result.meta[1].arg_name == "first"
    assert result.meta[1].type_name == "str"
    assert result.meta[2].arg_name == "second"
    assert result.meta[2].type_name == "int"