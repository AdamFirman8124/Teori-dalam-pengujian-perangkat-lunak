

# Generated at 2022-06-13 19:30:52.833416
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc = DocstringDeprecated(["param"], "description", "version")
    assert doc.description == "description"
    assert doc.version == "version"


# Generated at 2022-06-13 19:30:57.883971
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc = DocstringDeprecated(
        ["this", "is", "an", "example"],
        "this is the description",
        "2019"
        )
    assert doc.args == ["this", "is", "an", "example"]
    assert doc.description == "this is the description"
    assert doc.version == "2019"


# Generated at 2022-06-13 19:31:00.087309
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam(["a", "b", "c"], "argument a is b and c", "a", "b", False, None)


# Generated at 2022-06-13 19:31:03.603553
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated("a","b", "c")
    assert d.args == "a"
    assert d.description == "b"
    assert d.version == "c"

# Generated at 2022-06-13 19:31:14.736640
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["param"]
    description = "Testing Docstring"
    type_name = "int"
    is_generator = True
    return_name = None

    assert (
        DocstringReturns(
            args, description, type_name, is_generator, return_name
        ).args
        == args
    )
    assert (
        DocstringReturns(
            args, description, type_name, is_generator, return_name
        ).description
        == description
    )
    assert (
        DocstringReturns(
            args, description, type_name, is_generator, return_name
        ).type_name
        == type_name
    )

# Generated at 2022-06-13 19:31:17.680725
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():

    assert DocstringMeta([], "description").description == "description"
    assert DocstringMeta(["param", "arg"], "description").description == "description"



# Generated at 2022-06-13 19:31:22.927173
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []


# Generated at 2022-06-13 19:31:26.560714
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstring_test = DocstringMeta(["param","argument"], "description")
    assert(docstring_test.args==["param","argument"])
    assert(docstring_test.description=="description")


# Generated at 2022-06-13 19:31:28.414823
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated([], None, None)



# Generated at 2022-06-13 19:31:30.293937
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring1 = Docstring()
    print(docstring1.params)


# Generated at 2022-06-13 19:31:36.070869
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d1 = DocstringRaises(["a", "b", "c"], None, None)
    assert d1.args == ["a", "b", "c"]
    assert d1.description == None


# Generated at 2022-06-13 19:31:45.466313
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "a", "int", "b", "int", "c", "int"]
    description = "foo"
    arg_name = "a"
    type_name = "int"
    is_optional = False
    default = None
    p = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert p.description == description
    assert p.arg_name == arg_name
    assert p.type_name == type_name
    assert p.is_optional == is_optional
    assert p.default == default


# Generated at 2022-06-13 19:31:50.857403
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Test 1:
    testObject = DocstringDeprecated(["param"], "This is a description", "1.0")
    if testObject.args != ["param"]:
        print("Fail 1")
    elif testObject.description != "This is a description":
        print("Fail 2")
    elif testObject.version != "1.0":
        print("Fail 3")
    else:
        print("Pass")
    
    # Test 2:
    testObject = DocstringDeprecated(["yields"], "This is a description", "1.0")
    if testObject.args != ["yields"]:
        print("Fail 1")
    elif testObject.description != "This is a description":
        print("Fail 2")
    elif testObject.version != "1.0":
        print("Fail 3")

# Generated at 2022-06-13 19:31:58.376150
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    ds = DocstringReturns(args = ["args"], description = "description", type_name = "A", is_generator = "True")
    assert ds.args == ["args"]
    assert ds.description == "description"
    assert ds.type_name == "A"
    assert ds.is_generator == True
    assert ds.return_name == None

# Generated at 2022-06-13 19:32:04.749015
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    d = DocstringReturns(args = [],
                         description = None,
                         type_name = None,
                         is_generator = False,
                         return_name = None)
    assert d.args == []
    assert d.description == None
    assert d.type_name == None
    assert d.is_generator == False
    assert d.return_name == None

# Generated at 2022-06-13 19:32:07.448303
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False
    assert d.meta == []
    return d


# Generated at 2022-06-13 19:32:09.072045
# Unit test for constructor of class ParseError
def test_ParseError():
    """Unit test for constructor of class ParseError."""



# Generated at 2022-06-13 19:32:12.336756
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    param = DocstringReturns(["return"], "", "", "")
    assert param.type_name == ""
    assert param.is_generator == False


# Generated at 2022-06-13 19:32:22.245100
# Unit test for constructor of class Docstring
def test_Docstring():
    test_obj = Docstring()

    assert test_obj.short_description is None
    assert test_obj.long_description is None
    assert test_obj.blank_after_short_description is False
    assert test_obj.blank_after_long_description is False
    assert test_obj.params == []
    assert test_obj.raises == []
    assert test_obj.returns is None
    assert test_obj.deprecation is None


# Generated at 2022-06-13 19:32:26.692459
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError('test')
    assert str(err) == 'test'
    assert repr(err) == 'test'
    assert type(err) == ParseError

# Generated at 2022-06-13 19:32:34.876909
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d = DocstringRaises(['a', 'b'], 'c', 'd')
    assert d.args == ['a', 'b']
    assert d.description == 'c'
    assert d.type_name == 'd'


# Generated at 2022-06-13 19:32:39.310830
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []


# Generated at 2022-06-13 19:32:42.235190
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(['param', 'arg'], "description")
    assert d.args == ['param', 'arg']
    assert d.description == "description"


# Generated at 2022-06-13 19:32:50.003974
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    description = "A description"
    arg_name = "arg_name"
    type_name = "int"
    default = "default"
    docstring_param = DocstringParam(["param"], description, arg_name, type_name, is_optional=True, default=default)
    assert docstring_param.args[0] == "param"
    assert docstring_param.description == description
    assert docstring_param.arg_name == arg_name
    assert docstring_param.type_name == type_name
    assert docstring_param.is_optional == True
    assert docstring_param.default == default


# Generated at 2022-06-13 19:32:52.173734
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert(DocstringReturns([":returns"], "a", "str", False) == DocstringReturns([":returns"], "a", "str", False))


# Generated at 2022-06-13 19:32:54.950049
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    doc_string = DocstringReturns(["param"], "description", "None", True, "None")
    assert doc_string.description == "description"
    assert doc_string.type_name == "None"
    assert doc_string.args == ["param"]

# Generated at 2022-06-13 19:32:58.924149
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test = DocstringDeprecated(["param"], "This is a test", "1.0")
    assert test.args == ["param"]
    assert test.description == "This is a test"
    assert test.version == "1.0"


# Generated at 2022-06-13 19:33:02.767937
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Invoke constructor
    item = DocstringDeprecated(args=[], description="description", version="version")
    # Check that class variables are correctly initialized
    assert item.args == []
    assert item.description == "description"
    assert item.version == "version"


# Generated at 2022-06-13 19:33:08.173652
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert doc.meta == []


# Generated at 2022-06-13 19:33:10.106981
# Unit test for constructor of class ParseError
def test_ParseError():
    """Unit test for ParseError constructor."""
    assert issubclass(ParseError, RuntimeError)


# Generated at 2022-06-13 19:33:15.278127
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(["param", "arg"], "def __init__(self)", "str")


# Generated at 2022-06-13 19:33:16.721124
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None

# Unit tests for methods of class Docstring

# Generated at 2022-06-13 19:33:18.731740
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d_meta = DocstringMeta([], "")
    assert d_meta.args == []
    assert d_meta.description == ""


# Generated at 2022-06-13 19:33:22.182805
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    meta = DocstringMeta(['test_message'], 'test_description')
    assert meta.args[0] == 'test_message'
    assert meta.description == 'test_description'


# Unit tests for constructor and properties of class DocstringParam

# Generated at 2022-06-13 19:33:28.683789
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(
        ["parameter"],
        "description",
        "arg_name",
        "type_name",
        True,
        "default",
    )
    assert param.args == ["parameter"]
    assert param.description == "description"
    assert param.arg_name == "arg_name"
    assert param.type_name == "type_name"
    assert param.is_optional == True
    assert param.default == "default"


# Generated at 2022-06-13 19:33:29.847963
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    print("Test construction de la class Docstring")
    print("Docstring : ", docstring)


# Generated at 2022-06-13 19:33:31.205373
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstring_var = DocstringMeta("arg", "description")
    assert docstring_var.args == "arg"
    assert docstring_var.description == "description"


# Generated at 2022-06-13 19:33:37.173740
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Test method"""
    args = ["arg1", "arg2"]
    description = "description"
    ds = DocstringMeta(args, description)
    assert args == ds.args
    assert description == ds.description


# Generated at 2022-06-13 19:33:39.146380
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated([':deprecated'], 'Hello World', '2018.01.29')


# Generated at 2022-06-13 19:33:39.967343
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """
    Comment for the test with some formatting
    """
    assert True == False

# Generated at 2022-06-13 19:33:51.976294
# Unit test for constructor of class Docstring
def test_Docstring():
    test_object = Docstring()
    assert test_object.short_description is None
    assert test_object.long_description is None
    assert test_object.blank_after_short_description is False
    assert test_object.blank_after_long_description is False
    assert test_object.meta == []
    assert test_object.params == []
    assert test_object.raises == []
    assert test_object.returns is None
    assert test_object.deprecation is None


# Generated at 2022-06-13 19:33:54.590952
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(['param', 'arg', 'key', 'attribute'], 'description', "TypeError")


# Generated at 2022-06-13 19:33:57.640534
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(['version'], 'description', 'version')
    assert d.description == 'description'
    assert d.version == 'version'
    assert d.args == ['version']


# Generated at 2022-06-13 19:33:58.766645
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
	pass


# Generated at 2022-06-13 19:34:01.311962
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(['Deprecated'], ':since: 0.0.1', '0.0.1')



# Generated at 2022-06-13 19:34:08.627502
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert isinstance(doc.short_description, type(None))
    assert isinstance(doc.long_description, type(None))
    assert isinstance(doc.params, list)
    assert isinstance(doc.raises, list)
    assert isinstance(doc.returns, type(None))
    assert isinstance(doc.deprecation, type(None))
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description



# Generated at 2022-06-13 19:34:10.987567
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Test constructor of class DocstringDeprecated"""
    docstringDeprecated = DocstringDeprecated([], "12.1", "") # pylint: disable=unused-variable
    return


# Generated at 2022-06-13 19:34:22.282844
# Unit test for constructor of class DocstringReturns

# Generated at 2022-06-13 19:34:25.613956
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    md = DocstringMeta(["DeprecationWarning"], "blahblah")
    dd = DocstringDeprecated(md.args, md.description, "0.1.0")
    assert dd.description == md.description
    assert dd.version == "0.1.0"



# Generated at 2022-06-13 19:34:30.148467
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam(1,2,3,4,5,6)
    assert dp.args == 1
    assert dp.description == 2
    assert dp.arg_name == 3
    assert dp.type_name == 4
    assert dp.is_optional == 5
    assert dp.default == 6


# Generated at 2022-06-13 19:34:41.980146
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(['test_param'], 'test_description', 'test_type_name')
    assert a.args == ['test_param']
    assert a.description == 'test_description'
    assert a.type_name == 'test_type_name'
    

# Generated at 2022-06-13 19:34:44.133842
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    arguments = ['deprecated', 'description']
    description = 'description'
    version = 'version'
    DocstringDeprecated(arguments, description, version)
    

# Generated at 2022-06-13 19:34:47.973462
# Unit test for constructor of class Docstring
def test_Docstring():
    a = Docstring()
    assert a.short_description is None
    assert a.long_description is None
    assert a.blank_after_short_description is False
    assert a.blank_after_long_description is False
    assert a.meta == []

# Generated at 2022-06-13 19:34:51.008495
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("RuntimeError")
    assert error.args == "RuntimeError"


# Generated at 2022-06-13 19:34:59.567769
# Unit test for constructor of class Docstring
def test_Docstring():
    x = Docstring()
    assert x.short_description is None
    assert x.long_description is None
    assert x.blank_after_short_description is False
    assert x.blank_after_long_description is False
    assert x.meta == []
    assert x.params == []
    assert x.raises == []
    assert x.returns is None
    assert x.deprecation is None


# Generated at 2022-06-13 19:35:10.046676
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "parameter", "arg", "argument", "attribute", "key", "keyword"]
    arg_name = "arg"
    type_name = "int"
    is_optional = True
    default = "10"
    description = "A argument"
    dp = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert dp.arg_name == "arg"
    assert dp.type_name == "int"
    assert dp.is_optional == True
    assert dp.default == "10"
    assert dp.description == "A argument"


# Generated at 2022-06-13 19:35:12.408030
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(["1", "2", "3"], "desc", "arg_name", "type_name", True, "default")


# Generated at 2022-06-13 19:35:13.591136
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
	class DocstringRaises:
		pass


# Generated at 2022-06-13 19:35:16.690288
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []


# Generated at 2022-06-13 19:35:27.027268
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Test the constructor of DocstringReturns."""
    m_args = ["Test"]
    m_description = "Test description"
    m_type_name = "int"
    m_is_generator = False
    m_return_name = "Test return name"
    docstring_returns = DocstringReturns(m_args,
                                         m_description,
                                         m_type_name,
                                         m_is_generator,
                                         m_return_name)
    assert docstring_returns.args == m_args
    assert docstring_returns.description == m_description
    assert docstring_returns.type_name == m_type_name
    assert docstring_returns.is_generator == m_is_generator
    assert docstring_returns.return_name == m_return_name

# Generated at 2022-06-13 19:35:43.502629
# Unit test for constructor of class ParseError
def test_ParseError():
    assert issubclass(ParseError, RuntimeError)
    assert isinstance(ParseError(), ParseError)
    assert isinstance(ParseError('a'), ParseError)
    assert ParseError().args == ("",)
    assert ParseError('a').args == ('a',)
    try:
        raise ParseError('a')
    except ParseError as e:
        assert e.args == ('a',)
    try:
        raise ParseError('a')
    except RuntimeError as e:
        assert e.args == ('a',)

# Generated at 2022-06-13 19:35:48.759800
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """
    >>> args = ["param"]
    >>> arg_name = "arg"
    >>> type_name = "str"
    >>> description = "description"
    >>> default = "None"
    >>> is_optional = True
    >>> print (DocstringParam(args, description, arg_name, type_name, is_optional, default))
    DocstringParam(args=['param'], description='description', arg_name='arg', type_name='str', is_optional=True, default='None')
    """


# Generated at 2022-06-13 19:35:50.441700
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(["hey","hey"], "this worked", "this worked")

# Generated at 2022-06-13 19:35:53.237018
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Error happened")
    except ParseError as e:
        assert str(e) == "Error happened"


# Generated at 2022-06-13 19:35:56.454068
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description == None
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.meta == []



# Generated at 2022-06-13 19:35:57.589821
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(1,2,3,4,5,6)

# Generated at 2022-06-13 19:35:58.855703
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(["test","test2"],"test3", "test4")

# Generated at 2022-06-13 19:36:02.864404
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Arrange
    ds_r = DocstringReturns(['returns'], 'Test', 'T', False, 'test')
    # Act
    actual = ds_r
    # Assert
    assert actual.args == ['returns']
    assert actual.description == 'Test'
    assert actual.type_name == 'T'
    assert actual.is_generator == False
    assert actual.return_name == 'test'


# Generated at 2022-06-13 19:36:05.484704
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    myDocstringRaises = DocstringRaises(['raises'], "description", "string")
    assert myDocstringRaises.type_name == "string"
    assert myDocstringRaises.description == "description"
    assert myDocstringRaises.args[0] == "raises"

    assert isinstance(myDocstringRaises, DocstringMeta)


# Generated at 2022-06-13 19:36:08.946184
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    d = DocstringReturns(["args"], "description", "int")
    assert d.args == ["args"]
    assert d.description == "description"
    assert d.type_name == "int"
    assert d.is_generator == False
    

# Generated at 2022-06-13 19:36:30.327236
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(
        ['param'],
        'the args',
        'the description'
    )

# Generated at 2022-06-13 19:36:34.373433
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = []
    description = "abcd"
    type_name = "Type"
    print(DocstringRaises(args, description, type_name))
    # Expected output:
    # DocstringRaises(args=None, description='abcd', type_name='Type')


# Generated at 2022-06-13 19:36:36.198281
# Unit test for constructor of class Docstring
def test_Docstring():
    """Test to check the constructor of class Docstring."""
    d = Docstring()
    assert d

# Generated at 2022-06-13 19:36:38.858385
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("dummy message")
    assert isinstance(err, ParseError)
    assert str(err) == "dummy message"

# Generated at 2022-06-13 19:36:42.748654
# Unit test for constructor of class Docstring
def test_Docstring():
    """TODO."""
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []


# Generated at 2022-06-13 19:36:48.030906
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = [1,2,3]
    description = 'desc'
    version = None
    meta = DocstringDeprecated(args, description, version)
    assert len(meta.args) == 3
    assert meta.description == 'desc'
    assert meta.version == None


# Generated at 2022-06-13 19:36:49.560696
# Unit test for constructor of class Docstring
def test_Docstring():
    s = Docstring()
    assert s.short_description is None
    assert s.long_description is None
    assert isinstance(s.meta, list)
    assert len(s.meta) == 0
    return s


# Generated at 2022-06-13 19:36:50.265173
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError()

# Generated at 2022-06-13 19:36:57.961520
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param_object = DocstringParam(
        ["param"], "description", "arg", "type", is_optional=False, default=None
    )
    assert param_object.args == ["param"]
    assert param_object.description == "description"
    assert param_object.arg_name == "arg"
    assert param_object.type_name == "type"
    assert param_object.is_optional == False
    assert param_object.default == None



# Generated at 2022-06-13 19:36:59.269169
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises('args', 'description', 'type_name')


# Generated at 2022-06-13 19:37:45.631271
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['arg']
    description = 'this is a description'
    arg_name = 'arg'
    type_name = None
    is_optional = None
    default = None
    new_docstring_param = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert new_docstring_param.args == ["arg"]
    assert new_docstring_param.description == 'this is a description'
    assert new_docstring_param.arg_name == 'arg'
    assert new_docstring_param.type_name == None
    assert new_docstring_param.is_optional == None
    assert new_docstring_param.default == None


# Generated at 2022-06-13 19:37:49.569582
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """Unit test for constructor of class DocstringParam."""
    with pytest.raises(TypeError):
        DocstringParam(1, 2, 3, 4, 5, 6)
    assert isinstance(DocstringParam([1, 2], 3, 4, 5, 6, 7), DocstringParam)
        

# Generated at 2022-06-13 19:37:57.584940
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    doc = DocstringParam([], "This is a test docstring", "arg_name", "type_name", True, "default")
    assert doc.args == []
    assert doc.description == "This is a test docstring"
    assert doc.arg_name == "arg_name"
    assert doc.type_name == "type_name"
    assert doc.is_optional == True
    assert doc.default == "default"

test_DocstringParam()



# Generated at 2022-06-13 19:37:58.558692
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated


# Generated at 2022-06-13 19:37:59.928094
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('Test')
    except ParseError:
        pass


# Generated at 2022-06-13 19:38:04.474971
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Test DocstringReturns constructor"""
    doc = DocstringReturns(['arg1', 'arg2'], 'desc', 'type', False, 'name')
    assert doc.args == ['arg1', 'arg2']
    assert doc.description == 'desc'
    assert doc.type_name == 'type'
    assert doc.is_generator == False
    assert doc.return_name == 'name'


# Generated at 2022-06-13 19:38:07.150489
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d_deprecated = DocstringDeprecated(['deprecate'], 'hello', '1.1.1')
    assert d_deprecated.args == ['deprecate']
    assert d_deprecated.description == 'hello'
    assert d_deprecated.version == '1.1.1'

# Generated at 2022-06-13 19:38:11.765328
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc_deprecated = DocstringDeprecated(['parameter'], "test", "1.0")
    assert doc_deprecated.args == ['parameter']
    assert doc_deprecated.description == "test"
    assert doc_deprecated.version == "1.0"


# Generated at 2022-06-13 19:38:14.711795
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Something went wrong")
    except ParseError as err:
        assert(str(err) == "Something went wrong")


# Generated at 2022-06-13 19:38:21.414992
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    print("test_DocstringReturns")
    param_list = ["param1", "param2"]
    description = "description"
    type_name = "int"
    is_generator = False
    test_result = DocstringMeta(param_list, description)
    test_result2 = DocstringReturns(param_list, description, type_name, is_generator)
    if test_result.__dict__ == test_result2.__dict__:
        print("test success")
    else:
        print("test failed")
    print(test_result)
    print(test_result2)

# Generated at 2022-06-13 19:39:42.429845
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    x = DocstringMeta(['a','b','c'], 'hello')
    assert isinstance(x,DocstringMeta)
    assert x.args == ['a','b','c']
    assert x.description == 'hello'


# Generated at 2022-06-13 19:39:44.714146
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test = DocstringRaises(['a'], 'b', 'c')
    assert (test.args, test.description, test.type_name) == (['a'], 'b', 'c')

# Generated at 2022-06-13 19:39:45.697789
# Unit test for constructor of class ParseError
def test_ParseError():
    a=ParseError("ParseError")
    print(a)

# Generated at 2022-06-13 19:39:49.983812
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['param']
    description = "A parameter"
    type_name = "int"
    is_generator = True
    return_name = "return"
    return_doc = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert return_doc.args == args
    assert return_doc.description == description
    assert return_doc.type_name == type_name
    assert return_doc.is_generator == is_generator
    assert return_doc.return_name == return_name
    

# Generated at 2022-06-13 19:39:58.606438
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    # by default, each of the instance variables should be null (i.e., None)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.deprecation is None

# A unit test for the property of the class Docstring

# Generated at 2022-06-13 19:40:02.069732
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("An error message")
    assert str(err) == "An error message"
    assert err.args == ("An error message",)
    assert err.__cause__ is None


# Generated at 2022-06-13 19:40:10.029086
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(["param", "arg", "argument", "attribute", "key", "keyword"], "description", "argname", "typename", True, "default")
    assert d.args == ["param", "arg", "argument", "attribute", "key", "keyword"]
    assert d.description == "description"
    assert d.arg_name == "argname"
    assert d.type_name == "typename"
    assert d.is_optional == True
    assert d.default == "default"
    # Test for the Property
    d = DocstringParam(["param", "arg", "argument", "attribute", "key", "keyword"], "description", "argname", "typename", True, "default")

# Generated at 2022-06-13 19:40:13.524940
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    x = DocstringRaises(["parameter"], "description", "type_name")
    assert x.args == ["parameter"]
    assert x.description == "description"
    assert x.type_name == "type_name"


# Generated at 2022-06-13 19:40:16.149869
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    test_DocstringMeta = DocstringMeta('test_args', 'test_description')
    assert test_DocstringMeta.args == 'test_args'
    assert test_DocstringMeta.description == 'test_description'


# Generated at 2022-06-13 19:40:26.607219
# Unit test for constructor of class Docstring
def test_Docstring():
    import pytest
    doc = Docstring()

    # Test for both the short and long description
    with pytest.raises(AttributeError):
        x = doc.short_description
    with pytest.raises(AttributeError):
        y = doc.long_description
    with pytest.raises(AttributeError):
        z = doc.blank_after_short_description
    with pytest.raises(AttributeError):
        z = doc.blank_after_long_description
    with pytest.raises(AttributeError):
        z = doc.meta

    doc.short_description = "This is a short description"
    doc.long_description = "This is a long description"
    doc.blank_after_short_description = True
    doc.blank_after_long_description = True