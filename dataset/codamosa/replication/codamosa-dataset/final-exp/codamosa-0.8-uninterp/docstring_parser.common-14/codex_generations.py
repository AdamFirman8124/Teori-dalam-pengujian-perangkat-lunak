

# Generated at 2022-06-13 19:30:52.776485
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    tmp = DocstringMeta(['tmp'], 'tmp')
    assert tmp.args == ['tmp']
    assert tmp.description == 'tmp'


# Generated at 2022-06-13 19:30:59.842154
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring_deprecated_info = [
        "deprecated", "1.23", "this is deprecated"
    ]
    docstring_deprecated = DocstringDeprecated(
        docstring_deprecated_info, "this is deprecated", "1.23"
    )
    assert docstring_deprecated.args == docstring_deprecated_info
    assert docstring_deprecated.description == "this is deprecated"
    assert docstring_deprecated.version == "1.23"
    # Test for the case that the value of version is none
    docstring_deprecated = DocstringDeprecated(
        docstring_deprecated_info, "this is deprecated", None
    )
    assert docstring_deprecated.args == docstring_deprecated_info
    assert docstring_deprecated.description == "this is deprecated"
    assert doc

# Generated at 2022-06-13 19:31:03.459105
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    # print(ds)
    # print(ds.params)
    # print(ds.raises)
    # print(ds.returns)
    # print(ds.deprecation)

# Generated at 2022-06-13 19:31:06.085616
# Unit test for constructor of class ParseError
def test_ParseError():
    assert str(ParseError('foo')) == 'foo'


# Generated at 2022-06-13 19:31:08.837120
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.meta == []
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.deprecation is None


# Generated at 2022-06-13 19:31:15.353695
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """Test for DocstringParam constructor"""
    # Test case 1
    args = ["param", "parameter", "arg", "argument", "argument"]
    desc = "description"
    arg_name = "arg"
    type_name = "type_name"
    is_optional = True
    default = "default"
    param = DocstringParam(args, desc, arg_name, type_name, is_optional, default)
    assert param.args == args
    assert param.description == desc
    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default

    # Test case 2
    args = ["param", "parameter", "arg", "argument", "argument"]
    desc = "description"
    arg_

# Generated at 2022-06-13 19:31:18.446118
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(['param'], 'description', 'arg_name', 'type', True, 'default')
    assert docstring_param.args == ['param']
    assert docstring_param.description == 'description'
    assert docstring_param.arg_name == 'arg_name'
    assert docstring_param.type_name == 'type'
    assert docstring_param.is_optional == True
    assert docstring_param.default == 'default'


# Generated at 2022-06-13 19:31:19.495764
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    pass

# Generated at 2022-06-13 19:31:21.398351
# Unit test for constructor of class ParseError
def test_ParseError():
    pe = ParseError("Error")
    assert str(pe) == "Error"



# Generated at 2022-06-13 19:31:25.266753
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    br = DocstringReturns(['return', 'returns'], 'A docstring.', None, True)
    assert br.is_generator
    assert isinstance(br, DocstringReturns)



# Generated at 2022-06-13 19:31:34.283089
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc is not None
    assert doc.short_description is None
    assert doc.long_description is None
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 0


# Generated at 2022-06-13 19:31:36.439754
# Unit test for constructor of class ParseError
def test_ParseError():
    """Test the constructor of class ParseError."""
    assert ParseError("test")

# Generated at 2022-06-13 19:31:38.162908
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    ds = DocstringMeta([], "")
    assert ds


# Generated at 2022-06-13 19:31:48.257265
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Create a docstring
    docstring = DocstringReturns(["param"], "test", "int", False)
    # Test the initialization of docstring
    assert docstring.args == ["param"]
    assert docstring.description == "test"
    assert docstring.type_name == "int"
    assert docstring.is_generator == False
    assert docstring.return_name == None

    # Create a docstring with return name
    docstring = DocstringReturns(["param"], "test", "int", False, "return_value")
    # Test the initialization of docstring
    assert docstring.args == ["param"]
    assert docstring.description == "test"
    assert docstring.type_name == "int"
    assert docstring.is_generator == False
    assert docstring.return_name == "return_value"

# Generated at 2022-06-13 19:31:52.733847
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    # short description
    assert d.short_description is None
    assert d.long_description is None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.meta == []
    # params
    assert d.params == []
    # raises
    assert d.raises == []
    # returns
    assert d.returns is None
    # deprecation
    assert d.deprecation is None


# Generated at 2022-06-13 19:32:00.124316
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Test the constructor of DocstringRaises."""
    # Create a DocstringRaises and check the attributes
    docstringraises = DocstringRaises(['x', 'y'], 'description', 'type_name')
    assert docstringraises.args == ['x', 'y']
    assert docstringraises.description == 'description'
    assert docstringraises.type_name == 'type_name'


# Generated at 2022-06-13 19:32:07.202353
# Unit test for constructor of class Docstring
def test_Docstring():
    obj = Docstring()
    assert obj.short_description == None
    assert obj.long_description == None
    assert obj.blank_after_short_description == False
    
    assert obj.blank_after_long_description == False
    assert obj.params == []
    assert obj.raises == []
    assert obj.returns == None
    assert obj.deprecation == None

test_Docstring()

# Generated at 2022-06-13 19:32:17.018586
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # Tests for Syntax Errors
    try:
        DocstringRaises(
            args = None, description = None, type_name = None)
        return False
    except TypeError:
        return True

    try:
        DocstringRaises(
            args = "List[str]", description = None, type_name = None)
        return False
    except TypeError:
        return True

    try:
        DocstringRaises(
            args = ["str"], description = None, type_name = None)
        return False
    except TypeError:
        return True

    try:
        DocstringRaises(
            args = ["str"], description = "str", type_name = "str")
        return False
    except TypeError:
        return True


# Generated at 2022-06-13 19:32:17.960730
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()


# Generated at 2022-06-13 19:32:22.208560
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['args']
    description = 'description'
    type_name = ['type_name']
    raises = DocstringRaises(args, description, type_name)

    print(raises.args)


if __name__ == "__main__":
    test_DocstringRaises()

# Generated at 2022-06-13 19:32:33.433385
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["arg"]
    description = "Description"
    type_name = "Type"
    doc = DocstringRaises(args, description, type_name)
    assert doc.args == ["arg"]
    assert doc.description == "Description"
    assert doc.type_name == "Type"

# Generated at 2022-06-13 19:32:42.488750
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["arg", "param"]
    description = "description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = False
    default = "default"

    dp = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert dp.args == args
    assert dp.description == description
    assert dp.arg_name == arg_name
    assert dp.type_name == type_name
    assert dp.is_optional == is_optional
    assert dp.default == default


# Generated at 2022-06-13 19:32:48.496981
# Unit test for constructor of class Docstring
def test_Docstring():
    """Test the Docstring class constructor."""
    doc = Docstring()
    assert doc is not None
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert doc.params == []
    assert doc.raises == []
    assert doc.returns is None
    assert doc.deprecation is None



# Generated at 2022-06-13 19:32:56.076981
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["some args"]
    description = "some description"
    arg_name = "some arg name"
    type_name = "some type name"
    is_optional = True
    default = "some default"

    expected = {
        "args": ["some args"],
        "description": "some description",
        "arg_name": "some arg name",
        "type_name": "some type name",
        "is_optional": True,
        "default": "some default",
    }

    actual = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    assert actual.args == expected["args"]
    assert actual.description == expected["description"]
    assert actual.arg_name == expected["arg_name"]
    assert actual.type_name == expected["type_name"]


# Generated at 2022-06-13 19:33:04.600856
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Unit test for constructor of class DocstringReturns"""
    args = ["returns"]
    description = "This description"
    type_name = "str"
    is_generator = False
    return_name = "This return name"
    doc_returns = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert doc_returns.args == args
    assert doc_returns.description == description
    assert doc_returns.type_name == type_name
    assert doc_returns.is_generator == is_generator
    assert doc_returns.return_name == return_name


# Generated at 2022-06-13 19:33:05.764533
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(["arg"], "description")

# Generated at 2022-06-13 19:33:09.166174
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(
            args=[":return", ":returns"],
            description=None,
            type_name="None",
            is_generator=False,
            return_name=None
        )

# Generated at 2022-06-13 19:33:12.511023
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(["deprecated"], "", "")
    assert docstring.args == ["deprecated"]
    assert docstring.description == ""
    assert docstring.version == ""



# Generated at 2022-06-13 19:33:18.234947
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(['param'], 'description', 'arg_name', 'type_name', True, 'default')
    assert param.args == ['param']
    assert param.description == 'description'
    assert param.arg_name == 'arg_name'
    assert param.type_name == 'type_name'
    assert param.is_optional == True
    assert param.default == 'default'


# Generated at 2022-06-13 19:33:20.347198
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("Test name")
    assert error.__str__() == "Test name"


# Generated at 2022-06-13 19:33:45.585763
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["long"]
    description = "long_description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = "is_optional"
    default = "default"
    docstring_param = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert docstring_param.args == ["long"]
    assert docstring_param.description == "long_description"
    assert docstring_param.arg_name == "arg_name"
    assert docstring_param.type_name == "type_name"
    assert docstring_param.is_optional == "is_optional"
    assert docstring_param.default == "default"


# Generated at 2022-06-13 19:33:50.788509
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """
    If a line is a deprecated metadata, this function will return an instance of the DocstringDeprecated class.
    :return:
    """

    docstringDeprecated = DocstringDeprecated([], ["This is deprecated because: "], [])
    assert docstringDeprecated.description == "This is deprecated because: "

# Generated at 2022-06-13 19:33:56.314978
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Test DocstringMeta."""
    args = ["param", "parameter"]
    description = "description of the parameter"
    instance_meta = DocstringMeta(args, description)
    assert instance_meta.args == ["param", "parameter"]
    assert instance_meta.description == "description of the parameter"



# Generated at 2022-06-13 19:34:00.312349
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    dsm = DocstringMeta(["args"], "description")
    assert dsm.args == ["args"]
    assert dsm.description == "description"


# Generated at 2022-06-13 19:34:04.576675
# Unit test for constructor of class ParseError
def test_ParseError():
    def test(msg: T.Optional[str] = None):
        e = ParseError(msg)
        assert e.args == (msg,) if msg is not None else ()

    yield test
    yield lambda: test("my message")


# Generated at 2022-06-13 19:34:06.887490
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta(['param'], 'This is a test docstring').args \
        == ['param']
    assert DocstringMeta(['param'], 'This is a test docstring').description \
        == 'This is a test docstring'


# Generated at 2022-06-13 19:34:13.601226
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test_one = DocstringDeprecated(["deprecation"], "desc", "ver")
    test_two = DocstringDeprecated(["deprecation"], "desc", None)
    test_three = DocstringDeprecated(["deprecation"], None, "ver")

    assert test_one.args == ["deprecation"]
    assert test_one.description == "desc"
    assert test_one.version == "ver"
    assert test_two.args == ["deprecation"]
    assert test_two.description == "desc"
    assert test_two.version is None
    assert test_three.args == ["deprecation"]
    assert test_three.description is None
    assert test_three.version == "ver"



# Generated at 2022-06-13 19:34:22.103001
# Unit test for constructor of class Docstring
def test_Docstring():
    """
    Unit test for constructor of class Docstring
    Args:
        None
    Returns:
        None
    Raises:
        AssertionError if the test fails
    """
    d = Docstring()
    assert d.short_description == None
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.meta == []
    assert d.params == []
    assert d.raises == []
    assert d.returns == None
    assert d.deprecation == None

# Generated at 2022-06-13 19:34:26.249593
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Create DocstringReturns and test constructor
    returns = DocstringReturns(['return'], 'does some stuff', 'str', True, 'someString')
    assert returns.args == ['return']
    assert returns.description == 'does some stuff'
    assert returns.type_name == 'str'
    assert returns.is_generator == True
    assert returns.return_name == 'someString'



# Generated at 2022-06-13 19:34:29.583564
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(args= "test", description = "test", version = "test")
    assert a.args == "test"
    assert a.description == "test"
    assert a.version == "test"


# Generated at 2022-06-13 19:35:00.429933
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d = DocstringRaises(args=[], description=None, type_name=None)
    assert d
    assert d.args == []
    assert d.description is None
    assert d.type_name is None

# Generated at 2022-06-13 19:35:02.646561
# Unit test for constructor of class ParseError
def test_ParseError():
    e = ParseError("Error")
    assert type(e) is ParseError

# Generated at 2022-06-13 19:35:09.292589
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # set up the test case
    args = ['param', 'name', 'description']
    description = "description"
    # call the function under test
    docstringMeta = DocstringMeta(args, description)
    # test the result
    assert docstringMeta.args == ['param', 'name', 'description']
    assert docstringMeta.description == "description"


# Generated at 2022-06-13 19:35:11.869433
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None
    assert len(d.meta) == 0


# Generated at 2022-06-13 19:35:24.587292
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['param']
    description = 'Название параметра'
    arg_name = 'arg_name'
    type_name = None
    is_optional = False
    default = None

    meta = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    print(meta.args)
    print(meta.description)
    print(meta.arg_name)
    print(meta.type_name)
    print(meta.is_optional)
    print(meta.default)
test_DocstringParam()


# Generated at 2022-06-13 19:35:33.420877
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # print("Testing if class DocstringDeprecated was initialized correctly: ")
    a = DocstringDeprecated(
        ['__init__', "self", "args", "description", "version"],
        'initialize self',
        '1.0.1'
    )
    assert a.args == ['__init__', "self", "args", "description", "version"], "args not initialized in constructor of DocstringMeta"
    assert a.description == 'initialize self', "description not initialized in constructor of DocstringMeta"
    assert a.version == '1.0.1', "version not initialized in constructor of DocstringMeta"



# Generated at 2022-06-13 19:35:38.173252
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    try:
        dp = DocstringParam()
        assert dp.args == [] and dp.description == "" and dp.arg_name == "" and dp.type_name == "" and dp.is_optional == None and dp.default == ""
    except Exception:
        print("Class DocstringParam has error")



# Generated at 2022-06-13 19:35:41.959940
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []


# Generated at 2022-06-13 19:35:45.831479
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam([], "", "arg_name", "type_name", "is_optional",
    "default")
    assert dp.arg_name == "arg_name"
    assert dp.type_name == "type_name"
    assert dp.is_optional
    assert dp.default


# Generated at 2022-06-13 19:35:48.122398
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam("args", "desc", "arg_name", "type_name", True, None)


# Generated at 2022-06-13 19:36:46.392656
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(["param", "arg"], "description")
    assert(d.args == ["param", "arg"])
    assert(d.description == "description")


# Generated at 2022-06-13 19:36:48.801424
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError(msg="Test")


# Generated at 2022-06-13 19:36:53.526306
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(["deprecated"], "My Description", "1.2.3")
    assert d.args == ["deprecated"]
    assert d.description == "My Description"
    assert d.version == "1.2.3"

# Generated at 2022-06-13 19:36:55.796554
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert isinstance(DocstringDeprecated([], 'description',
                                          'version'), DocstringDeprecated)

# Generated at 2022-06-13 19:36:58.699482
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    c = DocstringDeprecated(["deprecated"], "desc", "ver")
    assert c.args == ["deprecated"]
    assert c.description == "desc"
    assert c.version == "ver"

# Generated at 2022-06-13 19:36:59.628026
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError('test')
    assert str(err) == 'test'


# Generated at 2022-06-13 19:37:00.384101
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("Some error")
    assert error.args == ("Some error",)

# Generated at 2022-06-13 19:37:04.190500
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    meta = DocstringMeta(['param', 'name'], 'This is a docstring')
    assert meta.args == ['param', 'name']
    assert meta.description == 'This is a docstring'


# Generated at 2022-06-13 19:37:09.466163
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    dm = DocstringMeta(["param", "arg"], "A test docstring.")
    assert dm.args == ["param", "arg"]
    assert dm.description == "A test docstring."
    assert type(dm.description) == str


# Generated at 2022-06-13 19:37:12.130420
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc = DocstringDeprecated(["deprecated"], "", "3.0.0")
    assert doc.args == ["deprecated"]
    assert doc.description == ""
    assert doc.version == "3.0.0"

# Generated at 2022-06-13 19:39:06.402714
# Unit test for constructor of class ParseError
def test_ParseError():
    p = ParseError("Test")
    assert p.args == "Test"


# Generated at 2022-06-13 19:39:09.920404
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docStr = DocstringDeprecated(['a', 'b'], 'description', 'version')
    assert docStr.description == 'description'
    assert docStr.args == ['a', 'b']
    assert docStr.version == 'version'


# Generated at 2022-06-13 19:39:17.969403
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(["a", "b"], "c", "d", "e", False, "f")
    d2 = DocstringParam(["a", "b"], "c", "d", "e", False, None)
    assert d.args == ["a", "b"]
    assert d.description == "c"
    assert d.arg_name == "d"
    assert d.type_name == "e"
    assert d.is_optional == False
    assert d.default == "f"
    assert d2.default is None


# Generated at 2022-06-13 19:39:24.258897
# Unit test for constructor of class Docstring
def test_Docstring():
    # Docstring constructor
    assert Docstring()
    assert Docstring().short_description == None
    assert Docstring().long_description == None
    assert Docstring().blank_after_short_description == False
    assert Docstring().blank_after_long_description == False
    assert Docstring().meta == []

    # Docstring.params property
    assert Docstring().params == []

    # Docstring.raises property
    assert Docstring().raises == []

    # Docstring.returns property
    assert Docstring().returns == None

    # Docstring.deprecation property
    assert Docstring().deprecation == None



# Generated at 2022-06-13 19:39:29.007758
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    print("=================================== Test: test_DocstringRaises")
    doc = DocstringRaises(["param"], "description", "type_name")
    print("Testing: doc.args: ", doc.args)
    print("Testing: doc.description: ", doc.description)
    print("Testing: doc.type_name: ", doc.type_name)

# Generated at 2022-06-13 19:39:30.216017
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(["raises"], "description", "type_name")



# Generated at 2022-06-13 19:39:31.751615
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    dm = DocstringMeta(["a","b"], "c")
    print(dm.args)
    print(dm.description)


# Generated at 2022-06-13 19:39:33.768733
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("parse error")
    except ParseError as e:
        print(e)

# Generated at 2022-06-13 19:39:37.015934
# Unit test for constructor of class ParseError

# Generated at 2022-06-13 19:39:44.400615
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(['param', 'arg'], 'parameter is ok', "arg_name", "type_name", True, "default")
    if docstring_param.args != ['param', 'arg']:
        raise 
    if docstring_param.description != 'parameter is ok':
        raise
    if docstring_param.arg_name != "arg_name":
        raise
    if docstring_param.type_name != "type_name":
        raise
    if docstring_param.is_optional != True:
        raise
    if docstring_param.default != "default":
        raise