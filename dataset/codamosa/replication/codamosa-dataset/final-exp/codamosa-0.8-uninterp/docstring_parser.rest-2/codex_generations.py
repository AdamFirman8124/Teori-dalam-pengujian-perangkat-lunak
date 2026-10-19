

# Generated at 2022-06-13 19:52:15.997889
# Unit test for function parse
def test_parse():
    docstring = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    """
    assert parse(docstring).short_description == "Parse the ReST-style docstring into its components."

# Generated at 2022-06-13 19:52:20.668577
# Unit test for function parse
def test_parse():
    docstring = '''Short string.

Long string.
:param int a: Parameter a.
:type a: int'''
    parsed_docstring = parse(docstring)
    assert parsed_docstring.short_description == "Short string."
    assert parsed_docstring.long_description == "Long string."
    assert parsed_docstring.meta[0].description == "Parameter a."
    return


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:52:29.870464
# Unit test for function parse
def test_parse():
    def f():
        """
        short description

        :param a: first parameter
        :param b: second parameter
        :returns: the return value
        :raises ValueError: if something bad happens.
        """
        pass

# Generated at 2022-06-13 19:52:44.037533
# Unit test for function parse
def test_parse():
    print('Testing parse():')
    docstring = '''
    This is a short description
    
    This is a long description
    
    :param req: The request
    :type req: `~subfinder.subfinder.SubfinderRequest`
    :param res: The response
    :type res: `~subfinder.subfinder.SubfinderResponse`
    :param str next: The next action to take
    :param bool foo: True if foo should be done, False otherwise.
    
    :raises ValueError: If the request is invalid, or something.
    
    :yields str: a string of text
    
    :returns: Something
    :rtype: str
    '''
    ds = parse(docstring)
    print('Short description: ' + ds.short_description)

# Generated at 2022-06-13 19:52:54.833562
# Unit test for function parse
def test_parse():
    assert parse("""
    Some short description.
    """).short_description == "Some short description."

    assert parse("""
    Some short description.
    And some longer one.
    """).long_description == "And some longer one."

    assert parse(
        """
    Some short description.

    And some longer one.
    """
    ).long_description == "And some longer one."

    assert parse(
        """
    Some short description.
    And some longer one.
    """
    ).long_description == "And some longer one."

    assert parse(
        """
    Some short description.

    And some longer one.
    """
    ).long_description == "And some longer one."


# Generated at 2022-06-13 19:52:59.099609
# Unit test for function parse
def test_parse():# pragma: no cover
    def dummy():
        """
        Example docstring.
        :param foo: A foo.
        """
        return

    print(parse(inspect.getdoc(dummy)))

# Generated at 2022-06-13 19:53:10.184612
# Unit test for function parse
def test_parse():
    doc_string = """\
        This function will parse docstrings.

        Arguments:
            - ``arg1``: The first argument
            - ``arg2``: The second argument

        Returns:
            - A number

        Yields:
            - The values that are yielded

        Raises:
            - TypeError: if arg1 is None
    """

    result = parse(doc_string)

    assert result.short_description == "This function will parse docstrings."
    assert result.blank_after_short_description

# Generated at 2022-06-13 19:53:21.325830
# Unit test for function parse
def test_parse():
    doc = (
        'Test docstring\n'
        '\n'
        'My Description\n'
        ':param int foo: Description of foo\n'
        ':param str bar: Description of bar\n'
        '\n'
        ':returns: Description of returns\n'
        ':raises ValueError: Something went wrong\n'
        ':return: The return value.\n'
    )
    ds = parse(doc)
    assert ds.short_description == "Test docstring"
    assert ds.long_description is None
    assert ds.blank_after_short_description is False
    assert ds.blank_after_long_description is False
    assert len(ds.meta) == 4

# Generated at 2022-06-13 19:53:26.171199
# Unit test for function parse
def test_parse():
    test_case = """
    __init__()
    Class A.
    :param str path: Path string
    """
    res = parse(test_case)
    assert res.short_description == "__init__()\nClass A."

    assert type(res.meta[0]) == DocstringParam
    assert res.meta[0].arg_name == "path"
    assert res.meta[0].type_name == "str"
    assert res.meta[0].description == "Path string"



# Generated at 2022-06-13 19:53:36.266865
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse(" ") == Docstring()
    assert parse("\n") == Docstring()
    assert parse("\n\n") == Docstring()
    assert (
        parse("nothing fancy")
        == Docstring(
            short_description="nothing fancy",
            blank_after_short_description=True,
            long_description=None,
            blank_after_long_description=None,
            meta=[],
        )
    )
    assert (
        parse("nothing fancy\n")
        == Docstring(
            short_description="nothing fancy",
            blank_after_short_description=True,
            long_description=None,
            blank_after_long_description=None,
            meta=[],
        )
    )

# Generated at 2022-06-13 19:53:42.696835
# Unit test for function parse
def test_parse():
    parse("""\
        Short description

        Long description

        :param arg1 : string
        :yields: int
        """)



# Generated at 2022-06-13 19:53:49.837500
# Unit test for function parse
def test_parse():
    assert not parse("")
    assert parse("\n") == parse("")


# Generated at 2022-06-13 19:54:02.956470
# Unit test for function parse

# Generated at 2022-06-13 19:54:12.827473
# Unit test for function parse
def test_parse():
    docstring = parse("""
        Short description

        Long description

        :param int a:
            The parameter "a".

            Defaults to 10.

        :raises KeyError:
            If the key is missing.

        Another paragraph
    """)
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == "Short description"
    assert docstring.long_description == """
        Long description

        Another paragraph
    """
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description

    param: DocstringParam = docstring.meta[0]
    assert param.keyword == "param"
    assert param.arg_name == "a"
    assert param.type_name == "int"
    assert param.is_optional is False

# Generated at 2022-06-13 19:54:21.973381
# Unit test for function parse
def test_parse():
    docstring = inspect.cleandoc(r"""
    :param a: Desc
    :param b: Desc
    :param c: Desc
    :type a: int
    :type b: str
    :type c: str
    :param d: Desc
    :param e: Desc
    :type d: int
    :returns: Desc
    :returns: Desc
    :returns: None
    :returns: Desc
    :yields: Desc
    :yields: Desc
    :yields: int
    :yields: Desc
    :raises ValueError: Desc
    :raises ValueError: Desc
    :raises ValueError: None
    :raises ValueError: Desc

    Short description
    """)
    parsed = parse(docstring)

# Generated at 2022-06-13 19:54:28.388308
# Unit test for function parse
def test_parse():
    text = '''
    """
    This is a short description.

    This is the long description.
    """
    A = B
    '''
    res = parse(text)
    assert res.short_description == 'This is a short description.'
    assert res.long_description == 'This is the long description.'
    assert res.meta == []
    assert res.blank_after_short_description
    assert res.blank_after_long_description

    text = '''
    """
    This is a short description.

    This is the long description.
    """
    '''
    res = parse(text)
    assert res.short_description == 'This is a short description.'
    assert res.long_description == 'This is the long description.'
    assert res.meta == []
    assert res.blank_after_short_

# Generated at 2022-06-13 19:54:39.280969
# Unit test for function parse
def test_parse():
    # strings
    assert parse('').short_description == None
    assert parse('').long_description == None
    assert parse('').blank_after_short_description == False
    assert parse('').blank_after_long_description == False
    assert parse('').meta == []

    assert parse('a').short_description == 'a'
    assert parse('a').long_description == None
    assert parse('a').blank_after_short_description == False
    assert parse('a').blank_after_long_description == False
    assert parse('a').meta == []

    assert parse('a\nb').short_description == 'a'
    assert parse('a\nb').long_description == 'b'
    assert parse('a\nb').blank_after_short_description == False
    assert parse('a\nb').blank_after

# Generated at 2022-06-13 19:54:43.670096
# Unit test for function parse
def test_parse():
    text = """Short description.

Long description.

:param x: x
:type x: int
:param y: y
:type y: int
:return: return"""
    _ = parse(text)


test_parse()

# Generated at 2022-06-13 19:54:44.559048
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:54:54.506594
# Unit test for function parse
def test_parse():
    docstring = """\
        Example of ReST-style docstring.

        :param str arg1: the first argument
        :param arg2: the second argument
        :raises Exception if something bad happens
        :rtype: None
        :return: None
        """

    result = parse(docstring)

    assert result.short_description == "Example of ReST-style docstring."
    assert result.blank_after_short_description
    assert result.long_description is None
    assert not result.blank_after_long_description

    assert len(result.meta) == 4

# Generated at 2022-06-13 19:55:06.864952
# Unit test for function parse
def test_parse():
    docstring = ':param a_parameter: a parameter of type int\n:type a_parameter: int\n\n:return: the sum of a, b and c\n:rtype: int'
    docstring_parsed = parse(docstring)
    print(docstring_parsed)

test_parse()

# Generated at 2022-06-13 19:55:16.695952
# Unit test for function parse
def test_parse():
    assert (
        parse("""\
        This is the first line.
    
        And this is the second.
        """
        )
        == Docstring(
            short_description="This is the first line.",
            long_description="And this is the second.",
            blank_after_short_description=True,
            blank_after_long_description=False,
        )
    )


# Generated at 2022-06-13 19:55:23.618096
# Unit test for function parse
def test_parse():
    doc = parse(
        """
        :param type_name arg_name: Description here.
        :param type_name arg_name: Description here.
        :returns: Returns description here.
        :rtype: str
        """
    )
    print(doc)
    print(doc.short_description)
    print(doc.long_description)
    print(doc.blank_after_short_description)
    print(doc.blank_after_long_description)
    for item in doc.meta:
        print(item)

test_parse()

# Generated at 2022-06-13 19:55:36.493232
# Unit test for function parse
def test_parse():
    doc = """Summary line.

Extended description.

:param foo: Description of foo.
:type foo: int
:param bar: Description of bar.
:type bar: bool
:param baz: Description of baz. Defaults to 1.
:type baz: int
:rtype: str
:returns: Description of return value.
:raises Exception: Description of exception
:yields: Description of yielded value.
"""
    docstring = parse(doc)
    assert docstring.short_description == "Summary line."
    assert docstring.long_description == "Extended description."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert len(docstring.meta) == 6

# Generated at 2022-06-13 19:55:49.013265
# Unit test for function parse
def test_parse():
    # Insert a test here
    doc = inspect.cleandoc('''
    Write a function to find the square root of a number.
    
    :param arg1: Type of arg1
    :param kwarg1: Description of kwarg1
    :type arg1: str
    :type kwarg1: int
    :returns: Description of return value
    :rtype: float
    
    :raises keyError: raises an exception
    :raises ValueError: if `arg2` is equal to `arg1`
    ''')

# Generated at 2022-06-13 19:55:50.088757
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    pass

# Generated at 2022-06-13 19:55:57.946834
# Unit test for function parse
def test_parse():
    text = """
    Find files matching a pattern.

    :param path: The path in which to search.
    :param pattern: The regular expression pattern to match.
    :type pattern: str
    :param prune: A regular expression that matches directory basenames to exclude.
    :type prune: str
    :param ignore_case: Flag indicating whether to ignore case.
    :type ignore_case: bool
    :return: Paths of matching files.
    :rtype: list
    """
    print(parse(text))
    print(str(parse(text)))
    print(repr(parse(text)))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:56:07.943874
# Unit test for function parse

# Generated at 2022-06-13 19:56:18.104971
# Unit test for function parse

# Generated at 2022-06-13 19:56:26.520410
# Unit test for function parse
def test_parse():
    text = '''
    This is a short description.

    This is a long description.
    It spans several lines.
    '''
    docstring = parse(text)
    assert docstring.short_description == "This is a short description."
    assert docstring.long_description == "This is a long description.\n" +\
                                         "It spans several lines."

    text = '''
    This is a short description.

    :type x: int
    :param y: something else
    '''
    docstring = parse(text)
    assert docstring.short_description == "This is a short description."
    assert docstring.meta[0].arg_name == "x"
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[1].arg_name == "y"

# Generated at 2022-06-13 19:56:46.976818
# Unit test for function parse
def test_parse():
    docstring = """
    Terminal control routines.

    This module provides functions for controlling the
    terminal.

    :param int fd:
        A file descriptor (defaults to ``sys.__stdout__``).
    :param encoding:
        The encoding to use for all text output to the standard
        output and error streams (defaults to
        ``locale.getpreferredencoding(False)``).

    :raises SystemExit:
        if the ``encoding`` is not supported.

    :returns:
        None

    :raises ValueError:
        if something is wrong.
    :returns:
        Something.
    """

# Generated at 2022-06-13 19:57:01.156018
# Unit test for function parse

# Generated at 2022-06-13 19:57:13.445542
# Unit test for function parse
def test_parse():
    docstring = """One line summary.

    Extensive explanation of your code and how it works.
    This can be several paragraphs long.

    Parameters
    ----------
    param1 : str
        The first parameter.
    param2 : int
        The second parameter.

    Returns
    -------
    str
        The return value.
    """
    d = parse(docstring)
    assert d.short_description == "One line summary."
    assert d.long_description == (
        "Extensive explanation of your code and how it works.\n"
        "This can be several paragraphs long."
    )
    assert len(d.meta) == 2
    assert d.meta[0].arg_name == "param1"
    assert d.meta[0].type_name == "str"

# Generated at 2022-06-13 19:57:18.987036
# Unit test for function parse
def test_parse():
    docstring = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    """
    expectation = DocstringMeta(args=["returns"], description="parsed docstring")
    assert [parse(docstring).meta[0]] == [expectation]

# Generated at 2022-06-13 19:57:26.487319
# Unit test for function parse
def test_parse():
    from .common import parse_path
    text = open(parse_path(__file__)).read()
    for match in re.finditer(r"def (\w+)[ ]?\(.*?\):\n(?:[ ]{3}\"\"\"(.*?)\"\"\")", text):
        name, text = match.groups()
        if name == "test_parse":
            continue
        print("\n" + name)
        print(parse(text))

# Generated at 2022-06-13 19:57:34.541654
# Unit test for function parse
def test_parse():
    docstring = """Single-line docstring.
    :param param: the parameter
    :param optional_param?: defaults to ``None``.
    :return: the return value
    :raises ValueError: if something goes wrong
    """
    
    doc = parse(docstring)
    assert(doc.short_description == "Single-line docstring.")
    assert(doc.long_description == "")
    assert(len(doc.meta) == 4)
    assert(doc.meta[0].args[0] == 'param')
    assert(doc.meta[0].description == 'the parameter')
    assert(doc.meta[1].args[0] == 'optional_param?')
    assert(doc.meta[1].description == 'defaults to ``None``.')

# Generated at 2022-06-13 19:57:48.534145
# Unit test for function parse
def test_parse():
    from .common import DocstringParam, DocstringReturns, DocstringMeta

    # test
    def f():
        """f

        :param datetime from_: start of period.
        :param datetime to: end of period.
        :returns: tuple of (datetime, datetime)
        """
        pass

    params = [
        ("from_", "datetime", "start of period", False, None),
        ("to", "datetime", "end of period", False, None),
    ]
    returns = [("tuple of (datetime, datetime)", None)]

    res = parse(f.__doc__)
    assert res.functions == []
    assert res.short_description == "f"
    assert res.long_description is None
    assert res.blank_after_short_description

# Generated at 2022-06-13 19:57:52.737335
# Unit test for function parse
def test_parse():
    docstring = parse(
        """Short summary.

        Long description.

        :param arg1: description.
        :type arg1: str
        :param arg2: description.
        :type arg2: int
        :returns: description
        :rtype: str
        :Raises ZeroDivisionError: description
        """
    )
    assert docstring.short_description == "Short summary."
    assert docstring.blank_after_short_description
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_long_description
    # count(None for _ in docstring.meta) == 1
    assert count(None for _ in docstring.meta) == 1


if __name__ == "__main__":
    from .test import count

    test_parse()

# Generated at 2022-06-13 19:58:04.634994
# Unit test for function parse
def test_parse():
    # Success case
    text = """
    Short description.

    This is the long description.
"""
    docstring = parse(text)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "This is the long description."
    assert len(docstring.meta) == 0
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description

    # Empty string
    text = ""
    docstring = parse(text)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert len(docstring.meta) == 0
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description

    # No short description

# Generated at 2022-06-13 19:58:14.877248
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    text = """
This is the short description.

    This is the
    long description.

    It can have
    multiple lines.
:param str foo: This is a parameter. It has a description too.
:returns: None
:raises ValueError: It's possible to raise an exception.
"""
    expected = """
This is the short description.

    This is the
    long description.

    It can have
    multiple lines.
:param str foo: This is a parameter. It has a description too.
:returns: None
:raises ValueError: It's possible to raise an exception.
""".strip()
    assert str(parse(text)).strip() == expected


# Generated at 2022-06-13 19:58:38.179793
# Unit test for function parse
def test_parse():
    text_1 = """Test function to parse the docstring

    :param a: test param
    :returns: test param
    """

    print(parse(text_1))

    text_2 = """Test function to parse the docstring

    :param a: test param
    :returns: test param
    :raises: TypeError
    """

    print(parse(text_2))
    print(type(parse(text_2)))
    print(parse(text_2).long_description)
    print(parse(text_2).short_description)
    print(parse(text_2).meta)
    print(parse(text_2).meta[0].arg_name)
    print(parse(text_2).meta[1].type_name)
    print("\n")


# Generated at 2022-06-13 19:58:45.073821
# Unit test for function parse
def test_parse():
    docstring = """
This is a normal docstring, it has a short and a long description.

This is the long description.
"""
    parsed = parse(docstring)
    assert parsed.short_description == "This is a normal docstring, it has a short and a long description."
    assert parsed.long_description == "This is the long description."
    assert parsed.blank_after_short_description == False
    assert parsed.blank_after_long_description == True
    assert parsed.meta == []


# Generated at 2022-06-13 19:58:50.343056
# Unit test for function parse
def test_parse():
    from .__main__ import test_docstring

    def f_with_docstring():
        """Short description


        Long

        description


        :param foo: first argument
        :type foo: str
        :param bar: second argument
        :type bar: int
        :returns: the return value
        :rtype: str
        :raises ValueError: if something bad happens


        """
        pass

    def f_without_docstring():
        pass

    assert repr(parse(f_with_docstring.__doc__)) == repr(test_docstring)

# Generated at 2022-06-13 19:59:01.283363
# Unit test for function parse
def test_parse():
    assert parse("This is a test function.") == Docstring(
        short_description="This is a test function.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[]
    )

    assert parse("This is a test function.\n\nA longer description.\n\n") == Docstring(
        short_description="This is a test function.",
        long_description="A longer description.",
        blank_after_short_description=False,
        blank_after_long_description=True,
        meta=[]
    )


# Generated at 2022-06-13 19:59:09.908265
# Unit test for function parse
def test_parse():
    import yaml

    text = """\
    Short summary.

    Long description (optional).

    :param foo: Foo is a required parameter with a type.
    :type foo: int
    :param bar: Bar is an optional parameter with a default.
    :type bar: str
    :param baz: Defaults to None.
    :type baz: int?
    :param fux: An optional parameter with an optional type.
    :raises: SomeError, SomeOtherError
    :returns: Whatever
    :returns: int
    :yields: Whatever
    :yields: int
    :rtype: int
    :meta: An unhandled meta info.
    """

    def do_test(docstring):
        print(docstring.as_dict())

# Generated at 2022-06-13 19:59:21.263844
# Unit test for function parse
def test_parse():
    check_parse(
        r"""
    aaa
    """
    )
    check_parse(
        r"""
        aaa
        bbb:xxxxxx
        ccc:xxxxxx
        """
    )
    check_parse(
        r"""
        :param arg1: xxx
        :param arg2: xxx
        """
    )
    check_parse(
        r"""
        :param arg1: xxx
        :param arg2: xxx
        :returns: xxx
        """
    )
    check_parse(
        r"""
        :param arg1: xxx
        :param arg2: xxx
        :returns arg1: xxx
        """
    )

# Generated at 2022-06-13 19:59:31.809593
# Unit test for function parse
def test_parse():
    docstring = inspect.cleandoc("""
        This is a test of the parse function.

        It has a short description and a long description.

        :param foo: a parameter
        :type foo: str
        :returns:
            The return value is a string.
            For string-like objects, this function returns the same object.
    """)

    ret = parse(docstring)

    assert not ret.blank_after_short_description
    assert ret.blank_after_long_description
    assert ret.short_description == "This is a test of the parse function."
    assert ret.long_description == inspect.cleandoc("""
        It has a short description and a long description.
    """)
    assert len(ret.meta) == 2
    assert ret.meta[0].args == ["param", "foo"]

# Generated at 2022-06-13 19:59:39.210397
# Unit test for function parse
def test_parse():
  str1 = parse("This is a test for function parse.\n\nThe docstring is:\n\n    This is a test for function parse.\n\n")
  if str1.short_description == "This is a test for function parse." and str1.long_description == "This is a test for function parse." and str1.blank_after_short_description == True and str1.blank_after_long_description == False:
    print("passed")
  else:
    print("failed")


# Generated at 2022-06-13 19:59:49.379818
# Unit test for function parse
def test_parse():
    exam_text=""""
    Summary line.
    Extended description of function.
    :param a: first parameter
    :param b: second parameter
    :return: nothing
    """
    answer = parse(exam_text)
    assert len(answer.meta) == 3
    assert answer.short_description == "Summary line."
    assert answer.long_description == "Extended description of function."
    assert answer.blank_after_short_description == True
    assert answer.blank_after_long_description == False
    assert answer.meta[0].description == "first parameter"
    assert answer.meta[1].description == "second parameter"
    assert answer.meta[2].description == "nothing"

# Generated at 2022-06-13 19:59:59.264280
# Unit test for function parse
def test_parse():
    text = """
    Short description.

    Longer description with
    line breaks.

    :param a: First argument.
    :type a: int

    :param b: Second argument.
    :type b: str
    """

    doc = parse(text)
    assert doc.short_description == "Short description."
    assert doc.long_description == "Longer description with line breaks."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description
    assert doc.meta[0].arg_name == "a"
    assert doc.meta[0].type_name == "int"
    assert doc.meta[0].description == "First argument."
    assert doc.meta[1].arg_name == "b"
    assert doc.meta[1].type_name == "str"

# Generated at 2022-06-13 20:00:20.126404
# Unit test for function parse
def test_parse():
    test_input = """
    :param thing:
    :param another_thing:
    :description:
    :param list things: A list of things
    :param int n_things:
    :param generator(int) n:
    :param default:
    :param non_default: defaults to "1".
    :param str optional_thing: Defaults to "default".
    :return:
    :rtype:
    :returns:
    :rtype:
    :returns list: A list of things
    :yields int:
    :yields:
    :raises:
    :raises ValueError:
    :raises:
    """


# Generated at 2022-06-13 20:00:33.347075
# Unit test for function parse

# Generated at 2022-06-13 20:00:39.467175
# Unit test for function parse
def test_parse():
    docstr = parse(
    '''Test description.
    :param blah: blah
    :type blah: str
    :raises: ValueError
    ''')
    
    assert docstr.short_description == "Test description."
    assert docstr.long_description == "param blah: blah\n\n    type blah: str\n\n    raises: ValueError"

# Generated at 2022-06-13 20:00:46.842131
# Unit test for function parse
def test_parse():
    """Unit test for the parse function."""
    docstring = """
    Short description.

    Long description.

    :param param1: This is a parameter.
    :param param2: This is a parameter.
    :type param1: str
    :type param2: int, optional
    :return: This is a return value.
    :rtype: bool

    :Example:

    >>> message = 'docstring'
    >>> parse(message)
    ['d', 'o', 'c', 's', 't', 'r', 'i', 'n', 'g']
    """
    assert isinstance(parse(docstring), Docstring)

# Generated at 2022-06-13 20:00:57.710165
# Unit test for function parse

# Generated at 2022-06-13 20:01:04.962338
# Unit test for function parse
def test_parse():

    from inspect import cleandoc

    docstring = cleandoc('''
        One sentence description here.

        Extended description here.

        Parameters
        ----------
        x, y, z : str
            Some description.

        Returns
        -------
        str
            Some description.

        Raises
        ------
        SomeException
            When something bad happens.
    ''')
    print(docstring)
    print(parse(docstring))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 20:01:10.227820
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    assert not parse("")

    with pytest.raises(ParseError):
        parse(":")

    with pytest.raises(ParseError):
        parse("Hello world!")

    assert parse("Hello world!") == Docstring(
        short_description="Hello world!",
        blank_after_short_description=False,
        long_description=None,
        meta=[],
    )

    assert parse("Hello world!\n\n") == Docstring(
        short_description="Hello world!",
        blank_after_short_description=True,
        long_description=None,
        meta=[],
    )


# Generated at 2022-06-13 20:01:17.442506
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
        short description.

        long description.

        :param foo: bar
        :param bar (str): baz
        :param baz: qux
        :returns:
            This is a very cool return value. Note that this is
            a multiline string.

        Also, this is a trailing comment.
        """
    )
    assert docstring.short_description == "short description."
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
    assert docstring.long_description == "long description."

# Generated at 2022-06-13 20:01:25.200361
# Unit test for function parse
def test_parse():
    """Test if correct docstring is parsed from docstring."""
    from .utils import check_parse
    from .common import Docstring, DocstringParam
    from .thedocs_sphinx import render_docstring
    check_parse(parse, render_docstring)

    docstring = Docstring()
    docstring.short_description = 'Sample docstring'
    docstring.meta.append(DocstringParam(args = ['arg', 'str', 'name'], description = 'Name of the person'))
    new_docstring = parse(render_docstring(docstring))
    assert docstring == new_docstring

# Generated at 2022-06-13 20:01:37.120471
# Unit test for function parse
def test_parse():
    # Use short form of docstring
    docstring = parse("""
        Hello, world.

        Returns something.
    """)

    assert docstring.short_description == "Hello, world."
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 1
    assert docstring.meta[0].key == "returns"

    # Use multiline form of docstring
    docstring = parse("""
        Hello, world.

        This is a longer description.

        Returns something.
    """)

    assert docstring.short_description == "Hello, world."
    assert docstring.long_description == "This is a longer description."
    assert docstring.blank_after_

# Generated at 2022-06-13 20:01:53.912291
# Unit test for function parse
def test_parse():
    # Test if parse works correctly
    docstring = parse(
        """This is a quick docstring!

    Parameters
    ----------

    name : str
      Name of something.

    number : int
      Number of something.
    """
    )

    assert docstring.short_description == "This is a quick docstring!"
    assert docstring.long_description == "Parameters\n----------\n\nname : str\n    Name of something.\n\nnumber : int\n    Number of something."

    assert type(docstring.meta[0]) is DocstringMeta
    assert docstring.meta[0].args == ['name', ':', 'str']
    assert docstring.meta[0].description == 'Name of something.'
    assert type(docstring.meta[1]) is DocstringMeta