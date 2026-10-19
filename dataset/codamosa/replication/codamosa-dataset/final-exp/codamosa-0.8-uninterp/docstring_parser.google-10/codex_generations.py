

# Generated at 2022-06-13 19:31:12.505106
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print('Start GoogleParser.parse')
    d = GoogleParser().parse.__doc__
    print(d)
    if d is None:
        print('None')
    else:
        print(d.__repr__())
        print(d.__str__())
    print('End GoogleParser.parse')

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:31:20.197464
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
        Google-style docstring parser.

        :param title_colon: require colon after section title. This can be used
            to differentiate sections from subsections.
        """
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == "Google-style docstring parser."
    assert docstring.long_description == """\
        :param title_colon: require colon after section title. This can be used
            to differentiate sections from subsections."""
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ['param', 'title_colon']
    assert docstring.meta[0].description == """\
        require colon after section title. This can be used
            to differentiate sections from subsections."""

# Generated at 2022-06-13 19:31:28.415166
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class Some():
        """This is a docstring.
        
        Args:
            arg1 (str): This is first arg
            arg2 (int): This is second arg.
            
        Raises:
            SomeException: When something bad happens
            
        Returns:
            int: return value
        """
        pass
        
    assert GoogleParser().parse(Some.__doc__).short_description == "This is a docstring."


if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:31:34.998974
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:31:48.573326
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test code snippet
    text = '''\
    This is an example method.   

    Args:
        a: A string representing a.
        b: An integer representing b.

    Returns:
        True if successful, False otherwise.
    '''
    # assert the actual result and target result

# Generated at 2022-06-13 19:31:49.831802
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass


# Generated at 2022-06-13 19:32:00.657697
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
        Test GoogleParser._parse()
            
            Parameters
            ----------
            text : str
                The string to be parsed.
        
            Returns
            -------
            List of (str,str,str)
                Each tuple is composed of the line number, argument name and
                argument description of a parameter line in the docstring
        '''
    doc = GoogleParser().parse(text)
    assert doc.short_description == "Test GoogleParser._parse()"
    assert doc.long_description == "Each tuple is composed of the line number, argument name and argument description of a parameter line in the docstring"
    assert len(doc.meta) == 3
    assert doc.meta[0].args[0] == "param"
    assert doc.meta[1].args[0] == "returns"

# Generated at 2022-06-13 19:32:11.228650
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """Summary line.
    Extended description.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2
    arg3 : list of str
        Description of arg3

    Raises
    ------
    ValueError
        Description of the value error.
    """
    parser = GoogleParser()
    doc = parser.parse(docstring)
    assert doc.short_description == "Summary line."
    assert doc.long_description == "Extended description."
    assert doc.meta[0].description == "Description of arg1"
    assert doc.meta[0].args[0] == "arg1"
    assert doc.meta[0].arg_name == "arg1"
    assert doc.meta[0].type_name == "int"
    assert doc.meta

# Generated at 2022-06-13 19:32:19.782205
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import sys

    line = """
      Bla bla.

      :Example:
        Bla bla.
         Bla bla.

      :Example:
        Bla bla.
    """
    line = line.strip()
    parser = GoogleParser()
    doc = parser.parse(line)

    assert doc.short_description == "Bla bla."
    assert doc.long_description == "Bla bla.\n Bla bla.\nBla bla."
    assert len(doc.meta) == 2
    assert doc.meta[0].args[0] == "example"
    assert doc.meta[0].args[1] == ":Example:"
    assert doc.meta[0].description == "Bla bla.\n Bla bla."

# Generated at 2022-06-13 19:32:27.399265
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test one
    text = """
    Class for wrapping functions that take a block of text as input
    and produce a new block of text as output.

    Args:
      func: The text-transforming function.

      name: The name of the function being wrapped (e.g. "pre" or "post").
    """
    # _ret = parse(text)
    # print("ret=", _ret)

    # test two
    text = """
    This class describes a specific predefined command.

    Instances of this class are stored in the global_commands list.

    Attributes:
      name: The name of the command as used in user input.
      function: The function implementing the command. See the function
          document string for details.
    """
    # _ret = parse(text)
    # print("ret=", _ret)

# Generated at 2022-06-13 19:33:03.226180
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  text = """Example function with types documented in the docstring.
  
      Args:
        param1 (int): The first parameter. (optional)
        param2 (str): The second parameter. (optional)
  
      Raises:
        TypeError: if neither param1 nor param2 is given.
  
      Returns:
        bool: The return value. True for success, False otherwise.
  
  """
  # Google style docstring parsing
  import pdb; pdb.set_trace()
  google_doc = GoogleParser()
  doc = google_doc.parse(text)
  #import pdb; pdb.set_trace()
  print(doc.description)
  print(doc.meta[0])

if __name__ == "__main__":
  test_GoogleParser_parse()

# Generated at 2022-06-13 19:33:15.701267
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

# Generated at 2022-06-13 19:33:21.051356
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #TODO: add the Docstring class to the same file as the parser.
    class Docstring:
        def __init__(self):
            self.short_description = "short_description"
            self.long_description = "long_description"
            self.blank_after_short_description = True
            self.blank_after_long_description = True
            self.meta = []
    parser = GoogleParser()
    docstring = parser.parse("""short_description
        long_description

        Arguments:
            arg0: arg0's description.
            arg1 (int): arg1's description. Defaults to 1.
        Returns:
            returns description""")
    assert docstring.short_description == "short_description"
    assert docstring.long_description == "long_description"
    assert docstring.blank_after

# Generated at 2022-06-13 19:33:31.446023
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse('') == Docstring()
    assert parse('A one-line description.') == Docstring(short_description='A one-line description.', long_description=None)
    assert parse('A one-line description.\n\nA\nmulti-line\ndescription.\n') == Docstring(short_description='A one-line description.', long_description='A\nmulti-line\ndescription.')
    assert parse('A one-line description.\n\nA\nmulti-line\ndescription.\n\n') == Docstring(short_description='A one-line description.', long_description='A\nmulti-line\ndescription.')

# Generated at 2022-06-13 19:33:45.268923
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("test_GoogleParser_parse")
    from .registry import registry
    parser = registry['google']

    doc = parser.parse("""
        This is a long description.

        Longer decsription continues here.
        and goes on for a couple of lines.

        Args:
            arg1: The first argument.
            arg2: The second argument.

        Returns:
            Description of return value.
    """)

    print("short_description:", doc.short_description)
    print("long_description:", doc.long_description)
    print("meta:", doc.meta)
    assert doc.short_description == "This is a long description."
    assert doc.long_description == """\
Longer decsription continues here.
and goes on for a couple of lines."""

# Generated at 2022-06-13 19:33:51.865455
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """
    This is a long description.

    This is even longer.
    """
    docstring = parser.parse(text)
    assert docstring.short_description == 'This is a long description.'
    assert docstring.long_description == 'This is even longer.'
    assert docstring.blank_after_short_description
    assert not docstring.blank_after_long_description

# Generated at 2022-06-13 19:34:00.668269
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    assert gp.parse(
            """
            Short description.

            Long description.
            """
        ) == Docstring(
            short_description="Short description.",
            long_description="Long description.",
            blank_after_long_description=False,
            blank_after_short_description=True,
            meta=[],
        )

# Generated at 2022-06-13 19:34:10.953875
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text1 = """Single line description.
    
    Long description.
    
    Args:
        arg1: Type and description of the first argument.
        arg2: Type and description of the second argument.
    
    Returns:
        Type and description of the returned value.
    
    Raises:
        ErrorName: First line of the error description.
            Additional lines are indented normally.
        
        ErrorName: First line of the second error description.
    
    Examples:
    
        Examples should be written in doctest format, and should illustrate how
        to use the function.
    
        >>> a = ["hello", "world"]
        >>> print(a)
        ['hello', 'world']
    """

    # Define expected result
    short_description1 = "Single line description."
    long_description1 = "Long description."

# Generated at 2022-06-13 19:34:20.834963
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    
    
    
a['x'].b[c].d(1, 2)

    """
    This is some random text.
    hopefully it works
    """
    '''
    actual = GoogleParser().parse(text)
    expected = Docstring(short_description="a['x'].b[c].d(1, 2)",
                         blank_after_short_description=True,
                         long_description='This is some random text.\nhopefully it works',
                         blank_after_long_description=False,
                         meta=[])
    assert expected == actual

if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 19:34:25.205915
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def parse_test(func):
        doc = inspect.getdoc(func)
        if doc:
            # print("-----------------------")
            # print(doc)
            # print("-----------------------")
            docstring = parse(doc)
            # print(docstring)

    def fun_1():
        """Test function to test method parse of class GoogleParser

            Returns:
                int: The return code.

            Yields:
                int: The return code.
        """
        return 0


# Generated at 2022-06-13 19:34:47.951476
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	car = GoogleParser().parse('''
This module contains helper functions for building plugins.

Args:
  plugin_p: Path to the plugin directory.
  name: Unique name for the plugin.
  description: A description of the plugin, used in the plugin.yaml file.
  version: Version of the plugin. Defaults to 0.1.0.

Returns:
  str: Path to the newly created plugin directory.
''')
	assert car.short_description == "This module contains helper functions for building plugins."
	assert len(car.meta) == 4
	assert car.meta[0].arg_name == "plugin_p"
	assert car.meta[1].arg_name == "name"
	assert car.meta[2].arg_name == "description"
	assert car.meta[3].arg_name == "version"


# Generated at 2022-06-13 19:34:54.564973
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    myParser = GoogleParser()
    myString = '''Arguments:
        :param p1: A parameter.
        :param p2:   A parameter.

    Returns:
        :returns:   A value.

    Raises:
        :raises:    ValueError.
        '''
    myString = myParser.parse(myString)
    assert myString.short_description == 'Arguments'
    assert len(myString.meta) == 3
    assert myString.meta[0].description == 'A parameter.'
    assert myString.meta[1].description == 'A value.'
    assert myString.meta[2].description == 'ValueError.'

# Generated at 2022-06-13 19:35:08.940650
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
    This is a test method.

    This is a longer description.

    Parameters
    ----------
    arg_1: str, optional
        This is a string argument, optional.
    arg_2: int
        This is a int argument, not optional.

    Returns
    -------
    str
        Return description.
    """

    doc = GoogleParser().parse(text)

    assert doc.short_description == "This is a test method."
    assert doc.long_description == "This is a longer description."
    assert doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 3
    assert doc.meta[0].arg_name == 'arg_1'
    assert doc.meta[0].type_name == 'str'
    assert doc

# Generated at 2022-06-13 19:35:17.380678
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def function1():
        """Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2
        """
        pass

    def function2():
        """Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1
            Description of arg1
        arg2
            Description of arg2
        """
        pass

    def function3():
        """Summary line.

        Extended description of function.

        Args
        ----
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2
        """
        pass


# Generated at 2022-06-13 19:35:31.694270
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    detector = GoogleParser()
    docstring1 = '''
    Parameters
    ----------
    arg1 : int
        Description of arg1

        with another line

    arg2 : str
        Description of arg2
    '''
    docstring2 = '''
    Parameters:
    ----------
    arg1 : int
        Description of arg1

        with another line

    arg2 : str
        Description of arg2
    '''
    docstring3 = '''
    Parameters
    ----------
    arg1 : int
        Description of arg1

    arg2 : str
        Description of arg2
    '''
    docstring4 = '''
    Parameters:
    ----------
    arg1 : int
        Description of arg1

    arg2 : str
        Description of arg2
    '''

# Generated at 2022-06-13 19:35:38.664159
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:35:47.435504
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    parser = GoogleParser()

    orig = """
    Short description.

    Long description.

    Parameters
    ----------
    arg1:
        Arg1 description.
    arg2:
        Arg2 description.

    Returns
    -------
    int
        Return description.
    """
    actual = parser.parse(orig)

    assert actual.short_description == "Short description."
    assert actual.long_description == "Long description."
    assert actual.blank_after_short_description
    assert actual.blank_after_long_description

    assert len(actual.meta) == 3
    assert actual.meta[0].description == "Arg1 description."
    assert actual.meta[0].type == SectionType.MULTIPLE
    assert actual.meta[0].args == ("param", "arg1")


# Generated at 2022-06-13 19:35:53.321913
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = "Short description\n\nLong description\n\nArgs: arg1 (str): Description 1.\n      arg2 (str): Description 2.\n\nRaises: Exception\n        AnotherException: Description\n"
    doc = GoogleParser().parse(docstring)
    assert doc.short_description == "Short description"
    assert doc.long_description == "Long description"
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == False

    meta = doc.meta
    arg1 = meta[0]
    assert arg1.args == ["param", "arg1 (str)"]
    assert arg1.arg_name == "arg1"
    assert arg1.type_name == "str"
    assert arg1.is_optional == False
    assert arg1

# Generated at 2022-06-13 19:35:58.171510
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    doc = """
        This is my function.

        :param arg1: first parameter.
        :type arg1: int
        :param arg2: second parameter.
        :type arg2: str
        :rtype: int

        :Example:
            >>> my_function(arg1, arg2) # doctest: +ELLIPSIS
            42
    """
    gp.parse(doc)
    return True

# Generated at 2022-06-13 19:36:05.375306
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    Single-line & multi-line description.
    '''

    result = GoogleParser().parse(text)
    assert result.short_description == 'Single-line & multi-line description.'
    assert result.blank_after_short_description == False
    assert result.blank_after_long_description == True
    assert result.long_description == None
    assert len(result.meta) == 0

    text = '''
    Single-line & multi-line description.
    
    Args:
        arg1 (int): Description of argument 1.
        arg2 (str): Description of argument 2.
    '''

    result = GoogleParser().parse(text)
    assert result.short_description == 'Single-line & multi-line description.'
    assert result.blank_after_short_description == False
    assert result

# Generated at 2022-06-13 19:36:18.978353
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #given
    text = '''
    :param arg1: Parameter description.
    :param arg2: Parameter description.
    :returns: Returns description.
    '''
    #when
    ret = GoogleParser().parse(text)
    #then
    assert len(ret.meta) == 3
    assert ret.meta[0].__class__.__name__ == 'DocstringParam'
    assert ret.meta[1].__class__.__name__ == 'DocstringParam'
    assert ret.meta[2].__class__.__name__ == 'DocstringReturns'
    assert ret.meta[2].description == 'Returns description.'

# Generated at 2022-06-13 19:36:25.490420
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("A one line Google docstring.") == Docstring(
        short_description = "A one line Google docstring."
    )
    assert GoogleParser().parse("   A one line Google docstring.") == Docstring(
        short_description = "A one line Google docstring."
    )
    assert GoogleParser().parse("A one line Google docstring.\n\n"
                                "With a long description.") == Docstring(
        short_description = "A one line Google docstring.",
        long_description = "With a long description.",
        blank_after_short_description = False,
        blank_after_long_description = False
    )

# Generated at 2022-06-13 19:36:36.931604
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:36:45.614044
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
Standard Google-style docstring.

Args:
    arg_name: description.
    arg2 (str): description.
    arg3 (str, optional): description. Defaults to `None`.
Returns:
    description of return value
Raises:
    KeyError: When a key error
    ValueError: When a value error
    TypeError: When a type error
Example:
    examples of usage
Attributes:
    attr_name: description of attribute
'''
    r = GoogleParser().parse(text)
    assert r.short_description == 'Standard Google-style docstring.'
    assert r.blank_after_short_description == True
    assert r.blank_after_long_description == True

# Generated at 2022-06-13 19:36:58.526870
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("Description") == Docstring(
        short_description="Description",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )
    assert GoogleParser().parse("Description\n") == Docstring(
        short_description="Description",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:37:03.182025
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:14.110342
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "Short description.\n\nLong description.\n\nArgs:\n    arg1: Argument description.\n    arg2: Argument description.\n\nRaises:\n    ValueError: If `value` is invalid, e.g. out of range.\nReturns:\n    Description of return value.\n    Description continued here.\n\nYields:\n   Description of yielded value."

    actual = parse(text)

# Generated at 2022-06-13 19:37:27.187839
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("Short description.") == Docstring(
        short_description="Short description."
    )
    assert GoogleParser().parse("Short description\n\nLong description.\n") == Docstring(
        short_description="Short description",
        blank_after_short_description=True,
        long_description="Long description.",
        blank_after_long_description=False
    )
    assert GoogleParser().parse("Short description.\nLong description.\n") == Docstring(
        short_description="Short description.",
        blank_after_short_description=False,
        long_description="Long description.",
        blank_after_long_description=False
    )

# Generated at 2022-06-13 19:37:34.171774
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:39.173830
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Check that docstring is parsed correctly"""
    assert parse('''
    Summary line.

    Extended description.

    Returns:
        int: description
    ''') == Docstring(
        short_description="Summary line.",
        long_description=(
            "Extended description.\n\n"
            "Returns:\n"
            "    int: description"
        ),
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[
            DocstringReturns(
                args=["returns", "int"],
                description="description",
                type_name="int",
                is_generator=False,
            )
        ],
    )



# Generated at 2022-06-13 19:38:01.102357
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    result = p.parse('''
        This is a docstring.

        This is the long documentation.

        Args:
            arg1: This is an argument.
            arg2: This is also an argument.
            arg3: This is an optional argument.

        Raises:
            LookupError: This is a raised exception.
            AttributeError: This is another raised exception.

        Returns:
            This is the return value.

        Examples:
            These are two examples.
        ''')
    assert result.short_description == "This is a docstring."
    assert result.blank_after_short_description
    assert result.blank_after_long_description
    assert result.long_description == "This is the long documentation."

    assert len(result.meta) == 5

    assert result.meta

# Generated at 2022-06-13 19:38:07.838555
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test = (
        "Args:\n"
        "    arg1(int): First argument\n"
        "    arg2 (str): Second argument\n\n"
        "Returns:\n"
        "    int: A return value\n\n"
    )
    expected = Docstring()
    expected.meta.append(DocstringParam(
        args=["param", "arg1(int)"],
        description="First argument",
        arg_name="arg1",
        type_name="int",
        is_optional=False,
        default=None,
    ))

# Generated at 2022-06-13 19:38:09.825244
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
	docstring = GoogleParser()
	docstring.parse("test text")


# Generated at 2022-06-13 19:38:10.864007
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert True


# Generated at 2022-06-13 19:38:20.159606
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    This is a test docstring.

    A multiline
    long description.

    Args:
      name: Name of the user.
      age: Age of the user.

    Returns:
      The user, if found.
      None, if not found.
    """
    ds = parse(text)
    assert ds.short_description == 'This is a test docstring.'
    assert ds.long_description == 'A multiline\nlong description.'
    assert len(ds.meta) == 4
    assert ds.meta[0].args[0] == 'param'
    assert ds.meta[0].arg_name == 'name'
    assert ds.meta[0].type_name == None
    assert ds.meta[0].description == 'Name of the user.'

# Generated at 2022-06-13 19:38:33.440620
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:41.064654
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()

    docstring = "Method to get the graph from the DB"
    assert gp.parse(docstring).short_description == docstring

    docstring = "Method to get the graph from the DB\n"
    assert gp.parse(docstring).short_description == docstring.strip()

    docstring = "Method to get the graph from the DB\n\n"
    d = gp.parse(docstring)
    assert d.short_description == "Method to get the graph from the DB"
    assert d.blank_after_short_description
    assert d.long_description == ""
    assert d.blank_after_long_description


# Generated at 2022-06-13 19:38:53.537721
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #Create a testing instance
    google_parser = GoogleParser()
    #Create a test docstring and a test string
    docstring = Docstring()
    text = "Javadoc and Google style docstrings.\n"
    #Set basic parts (short and long description) of docstring
    docstring.short_description = "Javadoc and Google style docstrings."
    docstring.long_description = ""
    docstring.blank_after_short_description = True
    docstring.blank_after_long_description = True
    #Test method parse by comparing the output and the expected docstring
    assert google_parser.parse(text) == docstring

# Generated at 2022-06-13 19:38:58.844953
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    parser = GoogleParser()

    docs = """
    The first line is brief explanation.

    The second line is a longer explanation, which
    may include math using, e.g., ``E = mc^2``.
    Then follows the arguments, each on its own line.

    Args:
      arg1(int): Description of `arg1`
      arg2(str, optional): Description of `arg2`. Defaults to 'hello'.
      arg3 (bool): Description of `arg3`.

    Returns:
      bool: Description of return value.
    """
    print(parser.parse(docs))

    # or Parser().parse(docs)

test_GoogleParser_parse()

# Generated at 2022-06-13 19:39:04.498516
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    g_parser = GoogleParser()
    docstring = g_parser.parse('''
        Test Google style docstring.
        Args:
            a: Test string.
    ''')
    assert docstring.short_description == 'Test Google style docstring.'
    assert docstring.meta[0].args == ['param', 'a']
    assert docstring.meta[0].description == 'Test string.'

    docstring = g_parser.parse('''
        Test Google style docstring.
        Args:
            a: Test string.
        Attributes:
            b: Test string.
    ''')
    assert docstring.short_description == 'Test Google style docstring.'
    assert docstring.meta[0].args == ['param', 'a']
    assert docstring.meta[1].args == ['attribute', 'b']

# Generated at 2022-06-13 19:39:31.150944
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class A:
        """Summary line.

        Extended description of method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        Args:
            arg1 (str): Description of `arg1`
            arg2 (:obj:`int`, optional): Description of `arg2`
            arg3 (:obj:`list` of :obj:`str`): Description of `arg3`

        Returns:
            bool:
                Description of return value

        """


# Generated at 2022-06-13 19:39:42.016235
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test method parse of class GoogleParser."""
    docstring = """
    Class to greet people.

    :param str part: string to add after greeting
    :param bool shout: if True uppercase greeting
    """

# Generated at 2022-06-13 19:39:47.077182
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # TEST1
    # text = '''Google-style docstring parsing.
    #
    #     This module parses Google-style docstrings.
    #     '''
    # ret = GoogleParser().parse(text)
    # assert ret == ''
    #
    # TEST2
    # text = '''Google-style docstring parsing.
    #
    #     This module parses Google-style docstrings.
    #     '''
    # ret = GoogleParser().parse(text)
    # assert ret == ''

    pass

# Generated at 2022-06-13 19:39:58.245094
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test the parse method from GoogleParser class."""
    parser = GoogleParser()
    text = "Implementation of the Google docstring.\n\n\nArgs:\n  path: path for the file.\n  lines: lines of the file.\n\nReturns:\n  Object: operation success (True) or not (False)."
    assert parser.parse(text).short_description == "Implementation of the Google docstring."
    text = "Implementation of the Google docstring.\n\n\nArgs:\n  path: path for the file.\n  lines: lines of the file.\n  parameters: the parameters.\n\nReturns:\n  Object: operation success (True) or not (False)."
    assert parser.parse(text).short_description == "Implementation of the Google docstring."

# Generated at 2022-06-13 19:40:03.279985
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = "This takes one parameter.\n\nArgs:\n    arg1: This is the first argument.\n    arg2: This is the second argument.\n\nReturns:\n    This returns something.\n\nRaises:\n    ValueError: If something bad happens.\n"
    GoogleParser().parse(docstring)


# Generated at 2022-06-13 19:40:07.395583
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text1 = """
        Parse the Google-style docstring into its components.
        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """
    print("Default parsing:")
    print(GoogleParser().parse(text1))
    print("==========================")



# Generated at 2022-06-13 19:40:16.925154
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring
    from nose.tools import assert_equal
    text = '''Example Function

    This is the first line of the docstring
    This is the second line of the docstring
    
    This is the first line of the long description
    This is the second line of the long description
    
    :param: foo: The first param
    :param: bar: The second param
    :param baz: The third param
    :returns: The return value
    :rtype: int
    '''

    d = GoogleParser().parse(text)

# Generated at 2022-06-13 19:40:22.715275
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from docstr_coverage import google 
    from docstr_coverage import tests

    func = tests.fake_func_1

    ret1 = google.parse(func.__doc__)
    ret2 = google.parse(func.__doc__)
    assert ret1 == ret2


# Generated at 2022-06-13 19:40:32.489558
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    Args:
        arg1: first argment
        arg2: second argument
    Returns:
        returns a docstring
    """
    docstring = GoogleParser().parse(text=docstring)
    assert isinstance(docstring, Docstring)
    assert docstring.long_description is None
    assert len(docstring.meta) == 2
    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[0].args[0] == "param"
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[0].description == "first argment"
    assert isinstance(docstring.meta[1], DocstringReturns)
    assert docstring.meta[1].args[0] == "returns"
    assert docstring

# Generated at 2022-06-13 19:40:40.262272
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Sample docstring that is ignored by parser

    Class description.

    :param p1: First parameter
    :type p1: int
    :param p2: Second parameter
    :type p2: str, optional
    :raises AttributeError: The ``Raises`` section is a list of all exceptions
     that are relevant to the interface.
    :returns: None
    :rtype: None
    """
    res = GoogleParser().parse(text)
    assert res.short_description == "Sample docstring that is ignored by parser"
    assert res.long_description == 'Class description.'
    assert res.blank_after_short_description == 0
    assert res.blank_after_long_description == 0
    assert len(res.meta) == 4
    print(res.meta)