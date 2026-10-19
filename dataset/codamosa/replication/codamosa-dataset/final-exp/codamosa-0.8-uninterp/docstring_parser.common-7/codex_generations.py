

# Generated at 2022-06-13 19:30:52.565061
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['raises', 'except', 'exception']
    description = "desc"
    type_name = "Exception"
    is_generator = True
    doc_return = DocstringReturns(args, description, type_name, is_generator)
    assert doc_return.long_description == "desc"

# Generated at 2022-06-13 19:30:53.299542
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError("ParseError")


# Generated at 2022-06-13 19:30:56.146782
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description == None
    assert ds.long_description == None


# Generated at 2022-06-13 19:30:57.665999
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    if isinstance(DocstringRaises, object):
        assert True
    else:
        assert False


# Generated at 2022-06-13 19:31:00.259196
# Unit test for constructor of class ParseError
def test_ParseError():
    """Constructor of class ParseError."""
    parse_error = ParseError('XXX')
    assert(parse_error.args == ('XXX',))


# Generated at 2022-06-13 19:31:05.582419
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(["param"], 'arg description', 'arg', 'str', True, None)
    assert docstring_param.args == ["param"]
    assert docstring_param.description == 'arg description'
    assert docstring_param.arg_name == "arg"
    assert docstring_param.type_name == "str"
    assert docstring_param.is_optional == True
    assert docstring_param.default == None


# Generated at 2022-06-13 19:31:08.276802
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    if __name__ == "__main__":
        DocstringReturns(["param", "parameter", "arg", "argument"],
                        "some description",
                        "Type of the argument",
                        False)

# Generated at 2022-06-13 19:31:18.350345
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    docstr = """
        Sample docstring.

        :param arg1: This is the first parameter.
        :param arg2: This is the second parameter.
        :raises: ValueError
        :returns: something
    """
    docstring = parse_docstring(docstr)
    assert docstring.short_description == "Sample docstring."
    assert len(docstring.params) == 2
    assert docstring.returns.return_name == "something"
    assert docstring.returns.is_generator is False
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description is None


# Generated at 2022-06-13 19:31:27.594937
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param"]
    description = "This is a Description"
    arg_name = "arg"
    type_name = "int"
    is_optional = False
    default = None
    param_test_1 = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert param_test_1.arg_name == "arg"
    assert param_test_1.type_name == "int"
    assert param_test_1.is_optional == False
    assert param_test_1.default == None


# Generated at 2022-06-13 19:31:35.798402
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    class_ref = DocstringParam(args=[],
                                arg_name='',
                                description='',
                                type_name=None,
                                is_optional=None,
                                default=None)
    assert class_ref.args == []
    assert class_ref.arg_name == ''
    assert class_ref.description == ''
    assert class_ref.type_name == None
    assert class_ref.is_optional == None
    assert class_ref.default == None



# Generated at 2022-06-13 19:31:40.990492
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(['args'], 'description', 'type', True)



# Generated at 2022-06-13 19:31:42.801200
# Unit test for constructor of class Docstring
def test_Docstring():
    assert type(Docstring()) == Docstring
    assert type(Docstring()) == Docstring

# Generated at 2022-06-13 19:31:48.905158
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = []
    description = "description"
    dm = DocstringMeta(args, description)
    assert dm.args == args
    assert dm.description == description
    args = ["arg1", "arg2", "arg3"]
    dm = DocstringMeta(args, description)
    assert dm.args == args
    assert dm.description == description
    description = "more description"
    dm = DocstringMeta(args, description)
    assert dm.args == args
    assert dm.description == description
    print("Test for constructor of class DocstringMeta passed.")


# Generated at 2022-06-13 19:31:51.756416
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param"]
    description = "The param arg is the first parameter"
    arg_name = "param"
    type_name = None
    is_optional = False
    default = None
    DocstringParam(args, description, arg_name, type_name, is_optional, default)


# Generated at 2022-06-13 19:31:53.566855
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError()


# Generated at 2022-06-13 19:31:59.931220
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    doc = DocstringReturns(
        ["arg1", "arg2"],
        "description",
        "type_name",
        True,
        "return_name"
    )
    assert doc.args == ["arg1", "arg2"]
    assert doc.description == "description"
    assert doc.return_name == "return_name"

# Generated at 2022-06-13 19:32:02.363682
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(args=[], type_name=None, description="")


# Generated at 2022-06-13 19:32:03.875103
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    r = DocstringRaises(['a', 'b', 'c'], 'x', 'y')

# Generated at 2022-06-13 19:32:08.109148
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Test error message")
    except ParseError as e:
        assert e.args[0] == "Test error message"


# Generated at 2022-06-13 19:32:12.893265
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = [':raises']
    description = 'This is description'
    type_name = 'Type'
    is_generator = True
    return_name = 'return name'
    assert DocstringReturns(args, description, type_name, is_generator, return_name) is not None

# Generated at 2022-06-13 19:32:23.128981
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(['deprecated'], 'this is deprecated', '1.0.0')
    assert docstring.args == ['deprecated']
    assert docstring.description == 'this is deprecated'
    assert docstring.version == '1.0.0'

# Generated at 2022-06-13 19:32:26.522911
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["raises", "TypeError", "if", "something", "happens"]
    description = "testing DocstringRaises constructor"
    type_name = "TypeError"

    d = DocstringRaises(args, description, type_name)

    assert d.args == args
    assert d.description == description
    assert d.type_name == type_name

# Generated at 2022-06-13 19:32:33.290863
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam  #shortcut for reference
    param = dp(['param','parameter'], 'Normal Parameter', 'arg', 'str', True, None )
    assert param.arg_name == 'arg'
    assert param.description == 'Normal Parameter'
    assert param.type_name == 'str'
    assert param.is_optional == True
    assert param.default == None


# Generated at 2022-06-13 19:32:35.753993
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(['1', '2'], 'test', '1.0.0')


# Generated at 2022-06-13 19:32:41.201455
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    x = DocstringReturns(['returns'], "test description", "test_type", False, None)
    assert x.args == ['returns']
    assert x.description == "test description"
    assert x.type_name == "test_type"
    assert x.is_generator == False
    assert x.return_name == None
    return

# Generated at 2022-06-13 19:32:45.921073
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    a = DocstringReturns([], None, None, False, None)
    assert a.args == []
    assert a.description == None
    assert a.type_name == None
    assert a.is_generator == False
    assert a.return_name == None

# Generated at 2022-06-13 19:32:49.561888
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(["version", "1.0"], "This feature is deprecated", "1.0")
    assert d
    assert d.args == ["version", "1.0"]
    assert d.description == "This feature is deprecated"
    assert d.version == "1.0"


# Generated at 2022-06-13 19:32:51.077709
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam([], "", "arg1", None, None, None)

# Generated at 2022-06-13 19:32:55.796938
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring = Docstring()
    # Test the initialized Docstring object
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description
    assert docstring.meta == []
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.deprecation is None


# Generated at 2022-06-13 19:32:58.250042
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('test')
    except ParseError as e:
        assert str(e) == 'test'


# Generated at 2022-06-13 19:33:14.854295
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('Testing ParseError')
    except ParseError as e:
        assert e


# Generated at 2022-06-13 19:33:16.848891
# Unit test for constructor of class DocstringParam
def test_DocstringParam():

    DocstringParam(["sometype", "arg_name", "anothertype"], None, None, None, None, None)

# Generated at 2022-06-13 19:33:18.486706
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(['raises','v'], 'desc', 'TypeError')


# Generated at 2022-06-13 19:33:23.986012
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstringparam = DocstringParam(['args'], 'description', 'arg_name', 'type_name', False, 'default')

    assert docstringparam.arg_name == 'arg_name'
    assert docstringparam.type_name == 'type_name'
    assert docstringparam.is_optional == False
    assert docstringparam.default == 'default'



# Generated at 2022-06-13 19:33:26.898852
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Parsing Error")
    except ParseError as e:
        assert e.args == ("Parsing Error",)
        assert type(e) is ParseError


# Generated at 2022-06-13 19:33:29.623353
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam(args=[], description='', arg_name='', type_name='',
                          is_optional=False, default=False) is not None


# Generated at 2022-06-13 19:33:31.211888
# Unit test for constructor of class Docstring
def test_Docstring():
    a = Docstring()
    return a

if __name__ == "__main__":
    test_Docstring()

# Generated at 2022-06-13 19:33:41.523677
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Ensure that DocstringDeprecated constructor works correctly."""
    # Create DocstringDeprecated object
    args = ['deprecated', 'since', 'version', '1.0']
    description = 'This function is deprecated.'
    version = '1.0'
    deprecated = DocstringDeprecated(args, description, version)

    # Test that DocstringDeprecated object was created with correct values
    assert deprecated.args == args
    assert deprecated.description == description
    assert deprecated.version == '1.0'

test_DocstringDeprecated()

# Generated at 2022-06-13 19:33:45.318826
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['param', 'arg', 'argument']
    description = 'description'
    dm = DocstringMeta(args, description)
    assert dm.args == args
    assert dm.description == description


# Generated at 2022-06-13 19:33:47.228404
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    from . import parse
    import doctest
    doctest.testmod(parse)

# Generated at 2022-06-13 19:34:16.691615
# Unit test for constructor of class ParseError
def test_ParseError():
  try:
    raise ParseError('Test error string')
  except ParseError as error:
    assert error.args[0] == 'Test error string'
  


# Generated at 2022-06-13 19:34:23.765202
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = [':raises', 'ValueError:', 'description']
    type_name = 'ValueError'
    description = 'description'
    assert args[1].endswith(type_name)
    assert args[1].startswith(':')
    assert args[0].startswith(':')
    assert args[2] == description
    assert args[0] == ':raises'
    args[1] = args[1].strip()
    assert args[1] == type_name

# Generated at 2022-06-13 19:34:27.766892
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(args=[], description="desc", version="1.0")
    assert a.args == []
    assert a.description == "desc"
    assert a.version == "1.0"


# Generated at 2022-06-13 19:34:29.019328
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(1, 1, 2, 3, 4)


# Generated at 2022-06-13 19:34:32.389724
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(["deprecated", "since"], None, "2.0")

    assert d.args == ["deprecated", "since"]
    assert d.description is None
    assert d.version == "2.0"



# Generated at 2022-06-13 19:34:35.900747
# Unit test for constructor of class Docstring
def test_Docstring():
    instance = Docstring()
    assert instance.short_description == None
    assert instance.long_description == None
    assert instance.blank_after_short_description == False
    assert instance.blank_after_long_description == False
    assert instance.meta == []


# Generated at 2022-06-13 19:34:39.322169
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(["deprecated", "since", "version=3.7"], "test_description", "3.7")
    assert d.args == ["deprecated", "since", "version=3.7"]
    assert d.description == "test_description"
    assert d.version == "3.7"


# Generated at 2022-06-13 19:34:42.133353
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """DocstringMeta symbolizing :returns or :yields metadata."""

    returns = DocstringReturns(["returns","return"], "this is a description", "string", False)
    assert returns.__class__.__name__ == "DocstringReturns"

test_DocstringReturns()

# Generated at 2022-06-13 19:34:53.208622
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Testing all different cases of the constructor
    DocstringReturns(["returns", "test"], "test returns", None, False)
    DocstringReturns(["returns", "test"], "test returns", "test_type", False)
    DocstringReturns(["returns", "test"], "test returns", None, True)
    DocstringReturns(["returns", "test"], "test returns", "test_type", True)
    DocstringReturns(["yields", "test"], "test yields", None, False)
    DocstringReturns(["yields", "test"], "test yields", "test_type", False)
    DocstringReturns(["yields", "test"], "test yields", None, True)
    DocstringReturns(["yields", "test"], "test yields", "test_type", True)

# Generated at 2022-06-13 19:34:56.221106
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(args=[], description=None, type_name="NotImplementedError")


# Generated at 2022-06-13 19:35:52.390244
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    _ = DocstringMeta([1, 2, 3], "description")



# Generated at 2022-06-13 19:35:54.002328
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    c = DocstringDeprecated(None, None, None)
    assert c is not None
    return

# Generated at 2022-06-13 19:36:00.523599
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['return', 'Returns']
    description = 'Return the sum of two integers'
    type_name = 'int'
    is_generator = False
    return_name = 'sum'
    returns = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert len(returns.args) == 2
    assert returns.args[0] == 'return'
    assert returns.args[1] == 'Returns'
    assert returns.description == description
    assert returns.type_name == type_name
    assert returns.is_generator == is_generator
    assert returns.return_name == return_name


# Generated at 2022-06-13 19:36:03.885195
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(["raises", "ValueError", "if", "something", "happens"], "description","ValueError")
    assert(a.type_name=="ValueError")
    assert(a.args==["raises", "ValueError", "if", "something", "happens"])
    assert(a.description=="description")


# Generated at 2022-06-13 19:36:10.538515
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert doc.meta == []
    #assert doc.params == []
    #assert doc.raises == []
    #assert doc.returns == None
    #assert doc.deprecation == None

################################################################################
# Unit tests for class DocstringMeta
#


# Generated at 2022-06-13 19:36:11.706965
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():

    assert DocstringReturns(['parameter'], '', None, False)

# Generated at 2022-06-13 19:36:13.450947
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns([], None, None, True, None)
    assert DocstringReturns(["return"], None, "str", True, "value")

# Generated at 2022-06-13 19:36:16.869857
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = [' :param arg:']
    description = 'arg'

    meta = DocstringMeta(args, description)
    assert meta.args == args
    assert meta.description == description



# Generated at 2022-06-13 19:36:21.813875
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Unit test for constructor of class DocstringMeta.

    Verifies that the constructor correctly initializes the class.
    """
    args = ["arg"]
    description = "Test description"
    doc = DocstringMeta(args, description)
    assert doc.args == args and doc.description == description


test_DocstringMeta()

# Generated at 2022-06-13 19:36:26.191376
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    meta = DocstringMeta(args=["param"], description="I am docstring metadata")
    assert meta.args == ["param"]
    assert meta.description == "I am docstring metadata"


# Generated at 2022-06-13 19:38:26.473370
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    print('testing DocstringDeprecated')
    args = ['test','test']
    description = 'test'
    version = 'test'
    D = DocstringDeprecated(args, description, version)
    assert D.args == args and D.description == description and D.version == version, 'DocstringDeprecated did not initialize properly'


# Generated at 2022-06-13 19:38:34.290405
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(['param', 'arg'], 'description', 'arg_name', 'type_name', 'is_optional', 'default')
    assert d.args == ['param', 'arg']
    assert d.description == 'description'
    assert d.arg_name == 'arg_name'
    assert d.type_name == 'type_name'
    assert d.is_optional == 'is_optional'
    assert d.default == 'default'



# Generated at 2022-06-13 19:38:41.406033
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    # check defaults
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert doc.meta == []
    # check properties
    assert doc.params == []
    assert doc.raises == []
    assert doc.returns == None
    assert doc.deprecation == None
    # check that setting attributes have the expected effect
    doc.short_description = "short desc"
    doc.long_description = "long desc"
    doc.blank_after_short_description = True
    doc.blank_after_long_description = True

# Generated at 2022-06-13 19:38:45.439860
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    result = DocstringParam(
    args=[],
    description=None,
    arg_name="s",
    type_name=None,
    is_optional=False,
    default=None
    )
    assert result is not None

# Generated at 2022-06-13 19:38:53.067581
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    dr1 = DocstringReturns(["returns", "type", None, None], None, None, True)
    dr2 = DocstringReturns(["returns", "type", None, None], None, None, False)
    dr3 = DocstringReturns(["returns", "type", None, 'test_name'], None, None, True)
    dr4 = DocstringReturns(["returns", "type", None, 'test_name'], None, None, False)
    pass


# Generated at 2022-06-13 19:38:55.599419
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(["return", "returns"], "", "str")
    DocstringReturns(["return", "returns"], "", "str", True)
    DocstringReturns(["return", "returns"], "", "str", True, "SomeReturnName")



# Generated at 2022-06-13 19:38:57.547609
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam(['param'], None, 'arg', 'str', True, 'None')
    assert(dp.is_optional)
    assert(dp.default == 'None')

# Generated at 2022-06-13 19:39:02.426782
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    description = "Hello"
    version = "1.2.3"
    docstring = DocstringDeprecated(['param','meta','deprecated'], description, version)
    assert docstring.args == ['param','meta','deprecated']
    assert docstring.description == description
    assert docstring.version == version


# Generated at 2022-06-13 19:39:03.571627
# Unit test for constructor of class ParseError
def test_ParseError():
    a = ParseError()


# Generated at 2022-06-13 19:39:08.409169
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = []
    description = 'desc'
    type_name = 'Test'
    is_generator = False
    assert DocstringReturns(args, description, type_name, is_generator)
    return_name = 'Test'
    assert DocstringReturns(args, description, type_name, is_generator, return_name)