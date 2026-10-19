

# Generated at 2022-06-13 19:30:54.583101
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args=["raises", "KeyError"]
    description="If a bad key is passed"
    type_name=KeyError
    DocstringRaises(args, description, type_name)


# Generated at 2022-06-13 19:30:55.727615
# Unit test for constructor of class ParseError
def test_ParseError():
    # Test
    with pytest.raises(RuntimeError):
        raise ParseError("Test failed")


# Generated at 2022-06-13 19:31:01.989256
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstringParam = DocstringParam(["arg", "description"], None, "arg", None, None, None)
    assert docstringParam.arg_name == "arg"
    assert docstringParam.description == None
    assert docstringParam.args == ["arg", "description"]
    assert docstringParam.type_name == None
    assert docstringParam.is_optional == None
    assert docstringParam.default == None


# Generated at 2022-06-13 19:31:06.940226
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated( ["args"], "description", "version")
    assert a.args == ["args"]
    assert a.description == "description"
    assert a.version == "version"



# Generated at 2022-06-13 19:31:08.978881
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    ex = DocstringDeprecated([], "", "")
    assert ex.version == ""
    assert ex.description == ""



# Generated at 2022-06-13 19:31:12.791169
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    testParam = DocstringParam(['a'], None, "arg_name", "type_name", None, None)
    assert testParam.args == ['a']
    assert testParam.arg_name == "arg_name"
    assert testParam.type_name == "type_name"
    assert testParam.is_optional == None
    assert testParam.default == None

# Generated at 2022-06-13 19:31:20.359197
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # test_args
    args = [":param", "arg", "description"]
    assert DocstringParam(args, None, None, None, None, None).args == args
    # test_description
    assert DocstringParam(args, "description", None, None, None, None).description == "description"
    # test_arg_name
    assert DocstringParam(args, None, "arg_name", None, None, None).arg_name == "arg_name"
    # test_type_name
    assert DocstringParam(args, None, None, "type_name", None, None).type_name == "type_name"
    # test_is_optional
    assert DocstringParam(args, None, None, None, True, None).is_optional == True
    # test_default

# Generated at 2022-06-13 19:31:23.236678
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("some_err")
    except ParseError as err:
        assert str(err) == "some_err"

# Generated at 2022-06-13 19:31:26.280342
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """ Unit test for constructor of class DocstringMeta """
    dm = DocstringMeta(['params'], "description")
    assert dm.description == "description"


# Generated at 2022-06-13 19:31:31.278964
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 0




# Generated at 2022-06-13 19:31:36.301594
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstringRaises = DocstringRaises
    return 0

# Generated at 2022-06-13 19:31:40.862397
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dd = DocstringDeprecated(args=[1, 2, 3], description='desc', version='v1.0')
    assert dd.args == [1, 2, 3]
    assert dd.description == 'desc'
    assert dd.version == 'v1.0'

# Generated at 2022-06-13 19:31:48.162972
# Unit test for constructor of class Docstring
def test_Docstring():
    res = Docstring()
    assert res.short_description == None
    assert res.long_description == None
    assert res.blank_after_short_description == False
    assert res.blank_after_long_description == False
    assert res.meta == []
    assert res.params == []
    assert res.raises == []
    assert res.returns == None
    assert res.deprecation == None


# Generated at 2022-06-13 19:31:50.895142
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """stuff"""
    # stuff = DocstringReturns(["params:", "arg1", "type:", "int"], "stuff", "int", False)
    # assert stuff.args == ["params:", "arg1", "type:", "int"]
    # assert stuff.description == "stuff"
    # assert stuff.type_name == "int"
    # assert stuff.is_generator == False
    # assert stuff.return_name == None


# Generated at 2022-06-13 19:31:59.266639
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert(DocstringMeta([], "").args==[])
    assert(DocstringMeta([], "").description=="")
    assert(DocstringMeta(["arg"], "").args==["arg"])
    assert(DocstringMeta(["arg"], "").description=="")
    assert(DocstringMeta([], "desc").args==[])
    assert(DocstringMeta([], "desc").description=="desc")

# Generated at 2022-06-13 19:32:02.450026
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("An error has occurred")
    except ParseError as e:
        assert e.args[0] == "An error has occurred"


# Generated at 2022-06-13 19:32:08.487773
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ['arg', 'deprecated']
    description = 'deprecated description'
    version = '1.0'
    d = DocstringDeprecated(args, description, version)
    print(d.args)
    print(d.description)
    print(d.version)


# Generated at 2022-06-13 19:32:14.850026
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    from docstring_parser import parse

    doc = parse(
        """
    :raises ValueError: if the network is not connected and
        `strict` is true.
    """
    )
    d = DocstringRaises(["raises","raise","except","exception"], "if the network is not connected and strict is true.", "ValueError")
    assert doc.raises[0] == d
    print("Test docstring_parser.py: test_DocstringRaises passed")

# Generated at 2022-06-13 19:32:23.510614
# Unit test for constructor of class Docstring
def test_Docstring():
    # Setup
    docstring = Docstring()

    # Exercise
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.deprecation is None
    # Exercises the property returns
    docstring.meta = [DocstringReturns([], None, None, False)]
    assert docstring.returns is not None


# Generated at 2022-06-13 19:32:27.553809
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    print("Testing DocstringReturns...", end="")


# Generated at 2022-06-13 19:32:40.544526
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    test_instance = DocstringReturns(
        args=[
            "return",
            ":",
        ],
        description="Test description",
        type_name="int",
        is_generator=False,
    )
    assert test_instance.args is not None
    assert test_instance.args[0] is not None
    assert test_instance.args[1] is not None
    assert test_instance.description is not None
    assert test_instance.type_name is not None
    assert test_instance.is_generator is not None


# Generated at 2022-06-13 19:32:46.732773
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam( [ 'param'], 'A parameter', 'arg_name', 'type_name', True, 'default' )
    assert( dp.args == ['param'] )
    assert( dp.description == 'A parameter' )
    assert( dp.arg_name == 'arg_name' )
    assert( dp.type_name == 'type_name' )
    assert( dp.is_optional == True )
    assert( dp.default == 'default' )

# Generated at 2022-06-13 19:32:47.638983
# Unit test for constructor of class Docstring
def test_Docstring():
    Docstring()

Docstring()

# Generated at 2022-06-13 19:32:55.019156
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():

    #empty args
    args = []

    # empty description
    description = None
    
    # empty type_name
    type_name = None

    # is_generator
    is_generator = False

    # return_name
    return_name = None

    test_DocstringReturns = DocstringReturns(args, description, type_name, is_generator, return_name)

    assert(test_DocstringReturns.description == description)
    assert(test_DocstringReturns.type_name == type_name)
    assert(test_DocstringReturns.is_generator == is_generator)
    assert(test_DocstringReturns.return_name == return_name)
    assert(test_DocstringReturns.args == args)


# Generated at 2022-06-13 19:32:57.355468
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(["param"], "description", "arg_name", "type_name", False, "default")

# Generated at 2022-06-13 19:33:03.039421
# Unit test for constructor of class Docstring
def test_Docstring():
    str1 = """
    :param int arg1: This is param1
    :param str arg2: This is param2
    :raises TypeError: This is error1
    :raises AttributeError: This is error2
    :raises RuntimeError: This is error3
    """
    docstring1 = Docstring(str1)

    assert(docstring1.short_description == None)
    assert(docstring1.long_description == None)
    assert(len(docstring1.params) == 2)
    assert(isinstance(docstring1.params[0], DocstringParam))
    assert(isinstance(docstring1.params[1], DocstringParam))
    assert(len(docstring1.raises) == 3)
    assert(isinstance(docstring1.raises[0], DocstringRaises))

# Generated at 2022-06-13 19:33:15.523834
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    line1 = ':param arg: description'
    args1 = ['arg', ':', 'description']
    line2 = ':param arg -- description'
    args2 = ['arg', '--', 'description']
    doc_param_1 = DocstringParam(args1[0:-1], 'description', 'arg', None, None, None)
    assert doc_param_1.arg_name == 'arg'
    assert doc_param_1.description == 'description'
    assert doc_param_1.type_name == None
    assert doc_param_1.is_optional == None
    assert doc_param_1.default == None
    doc_param_2 = DocstringParam(args2, 'description', 'arg', None, None, None)
    assert doc_param_2.arg_name == 'arg'
    assert doc

# Generated at 2022-06-13 19:33:18.771968
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docrais = DocstringRaises( ['raises'], 'description', 'ValueError')
    assert docrais.type_name == 'ValueError', "The type_name of the DocstringRaises instance is not correct."


# Generated at 2022-06-13 19:33:23.496194
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a full description'
    assert docstring.short_description == 'This is a short description'
    assert docstring.long_description == 'This is a full description'


# Generated at 2022-06-13 19:33:30.464932
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    #create an object of this class
    obj = DocstringDeprecated([], '', '1.0')
    #check if the object is created
    assert obj is not None, "The object is not created"
    #check if all the values are initialized properly
    assert obj.args == [], "Something went wrong in initilization of args"
    assert obj.description == '' , "Something went wrong in initilization of description"
    assert obj.version == '1.0' , "Something went wrong in initilization of version"


# Generated at 2022-06-13 19:33:36.612794
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["v1"]
    type_value = "int"
    description_value = "This is a docstring for a function"
    a = DocstringRaises(args, description_value, type_value)
    assert (a.args == args)
    assert (a.type_name == type_value)
    assert (a.description == description_value)



# Generated at 2022-06-13 19:33:37.776259
# Unit test for constructor of class ParseError
def test_ParseError():
    a = ParseError("Hi")
    assert a.args[0] == "Hi"



# Generated at 2022-06-13 19:33:49.781569
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Test the constructor of DocstringRaises.

    This function and accompanying functions are designed to test the functionality of the
    constructor of the currently tested class, DocstringRaises. This is done by
    initializing a DocstringRaises object with the arguments that will be given to the
    constructor as well as an expected result and then comparing the initialized object
    with the expected result.
    """
    args = ["arg1", "arg2"]
    description = "this is a description"
    type_name = "ValueError"
    expected_result = DocstringRaises(
            args = ["arg1", "arg2"],
            description = "this is a description",
            type_name = "ValueError")

# Generated at 2022-06-13 19:33:54.001064
# Unit test for constructor of class ParseError
def test_ParseError():
    # Arrange
    assert_string = "assert_string"

    # Act
    actual = ParseError(assert_string)
    expected = "assert_string"

    # Assert
    assert actual.args[0] == expected


# Generated at 2022-06-13 19:33:56.875746
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """
    """
    docstring_meta = DocstringReturns(['arg'], 'description', 'type', True)
    assert docstring_meta.type_name is 'type'

# Generated at 2022-06-13 19:33:58.345368
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns([], '', '', False, None)

# Generated at 2022-06-13 19:34:00.320407
# Unit test for constructor of class ParseError
def test_ParseError():
    assert type(ParseError) == type(Exception)


# Generated at 2022-06-13 19:34:07.868372
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    parameters = ['first parameter', 'second parameter']
    description = 'none'
    name = 'name'
    type_name = 'string'
    is_optional = True
    default = 'none'

    param = DocstringParam(parameters, description, name, type_name, is_optional, default)
    assert param.arg_name == name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default


# Generated at 2022-06-13 19:34:11.983691
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(["arg"], "description", "arg_name", "type_name", True, "default")
    assert param.args == ["arg"]
    assert param.description == "description"
    assert param.arg_name == "arg_name"
    assert param.type_name == "type_name"
    assert param.is_optional == True
    assert param.default == "default"


# Generated at 2022-06-13 19:34:21.016257
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam(['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], None, "string", None, None, None)
    assert dp.args == ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    assert dp.description is None
    assert dp.arg_name == "string"
    assert dp.type_name is None
    assert dp.is_optional is None
    assert dp.default is None


# Generated at 2022-06-13 19:34:28.463431
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["deprecated", "since", "1.0.0"]
    description = "description"
    version = "1.0.0"
    docstringDeprecated = DocstringDeprecated(args, description, version)
    assert docstringDeprecated.args == args
    assert docstringDeprecated.description == description
    assert docstringDeprecated.version == version



# Generated at 2022-06-13 19:34:30.474898
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta('args', "Description")
    d.args == 'args'
    d.description == 'Description'


# Generated at 2022-06-13 19:34:36.500490
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['arg', 'description', 'arg_name', 'type_name']
    description = 'args, arg_name and type_name'
    docstring_meta = DocstringMeta(args, description)
    assert docstring_meta.args == args
    assert docstring_meta.description == description


# Generated at 2022-06-13 19:34:42.706304
# Unit test for constructor of class Docstring
def test_Docstring():
    x = Docstring()
    assert x.short_description == None
    assert x.long_description == None
    assert x.blank_after_short_description == False
    assert x.blank_after_long_description == False
    assert x.meta == []



# Generated at 2022-06-13 19:34:52.733973
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam(args = ["param", "name"], description = "description", arg_name = "x", type_name = "type", is_optional = False, default = "None")
    assert dp.args == ["param", "name"]
    assert dp.description == "description"
    assert dp.arg_name == "x"
    assert dp.type_name == "type"
    assert dp.is_optional == False
    assert dp.default == "None"
    
    dp = DocstringParam(args = ["param", "name"], description = "description", arg_name = "x", type_name = "type", is_optional = True, default = "None")
    assert dp.args == ["param", "name"]
    assert dp.description == "description"

# Generated at 2022-06-13 19:35:04.437362
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docParam = DocstringParam(["param"], None, "param1", "int", True, "2")
    assert docParam.args == ["param"], "Initializing DocstringParam"
    assert docParam.description == None, "Initializing DocstringParam"
    assert docParam.arg_name == "param1", "Initializing DocstringParam"
    assert docParam.type_name == "int", "Initializing DocstringParam"
    assert docParam.is_optional == True, "Initializing DocstringParam"
    assert docParam.default == "2", "Initializing DocstringParam"


# Generated at 2022-06-13 19:35:10.774194
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(
        ["param", "arg", "foo", "type:", "int"],
        "description of foo",
        "foo",
        "int",
        False,
        None,
    )
    assert docstring_param.arg_name == "foo"
    assert docstring_param.type_name == "int"
    assert docstring_param.is_optional is False
    assert docstring_param.default is None


# Generated at 2022-06-13 19:35:14.550324
# Unit test for constructor of class ParseError
def test_ParseError():
    """Create an instance of ParseError class."""
    err = ParseError('Your code is not safe')
    assert err.args == ('Your code is not safe',)


# Generated at 2022-06-13 19:35:30.363626
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["args", "type_name", "is_optional", "default"]
    description = " Returns description "
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = "is_optional"
    default = "default"
    dp = DocstringParam(args, description, arg_name, type_name, is_optional, default)
   # UNIT test for constructor
    assert isinstance(dp, DocstringMeta)
    # UNIT test for the initialization of a DocstringParam
    assert dp.args[0] == "args"
    assert dp.description == " Returns description "
    assert dp.arg_name == "arg_name"
    assert dp.type_name == "type_name"
    assert dp.is_optional == "is_optional"

# Generated at 2022-06-13 19:35:34.896580
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['ccc', 'ddd']
    description = 'a'
    type_name = 'b'
    assert DocstringRaises(args, description, type_name) is not None


# Generated at 2022-06-13 19:35:43.603054
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(["param"], "description", "arg", "str", True, "None")
    assert docstring_param.arg_name == "arg"
    assert docstring_param.type_name == "str"
    assert docstring_param.is_optional == True
    assert docstring_param.default == "None"


# Generated at 2022-06-13 19:35:45.040537
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    obj = DocstringMeta(['args'], 'description')
    assert obj == obj


# Generated at 2022-06-13 19:35:48.222393
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.long_description == None
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []


# Generated at 2022-06-13 19:35:52.123762
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["version"]
    description = "test"
    version = "0.0.1"
    d = DocstringDeprecated(args, description, version)
    assert d.args == args
    assert d.description == description
    assert d.version == version



# Generated at 2022-06-13 19:35:53.408203
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises('arg','description','type')



# Generated at 2022-06-13 19:35:54.280227
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError()


# Generated at 2022-06-13 19:35:56.706796
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError
    except ParseError:
        print("Raise ParseError")
    else:
        print("Not Raise ParseError")


# Generated at 2022-06-13 19:36:00.423621
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam(["as"], "None", "a", "a", "a", "a")
    assert a.args == ["as"]
    assert a.description == "None"
    assert a.arg_name == "a"
    assert a.type_name == "a"
    assert a.is_optional == "a"
    assert a.default == "a"

# Generated at 2022-06-13 19:36:01.734280
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds is not None

# Unit tests for property params of class Docstring

# Generated at 2022-06-13 19:36:08.699847
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    arg_types = T.List[str]
    arg_description = T.Optional[str]
    arg_is_generator = bool
    arg_type_name = T.Optional[str]
    arg_return_name = T.Optional[str]
    arg_args = arg_types
    #constructor = DocstringReturns()
    constructor = DocstringReturns(arg_args, arg_description, arg_type_name,
            arg_is_generator, arg_return_name)

# Generated at 2022-06-13 19:36:15.149706
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("ParseError")
    except ParseError:
            pass


# Generated at 2022-06-13 19:36:16.545038
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises([], None, None)


# Generated at 2022-06-13 19:36:20.408732
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert doc.meta == []

# Generated at 2022-06-13 19:36:27.715934
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    docstring_returns1 = DocstringReturns("args", "description", "type_name", False)
    assert(isinstance(docstring_returns1, DocstringReturns) == True and \
        docstring_returns1.description == "description" and \
        docstring_returns1.type_name == "type_name")
    docstring_returns2 = DocstringReturns("args", "description", "type_name", True, "return_name")
    assert(isinstance(docstring_returns2, DocstringReturns) == True and \
        docstring_returns2.description == "description" and \
        docstring_returns2.type_name == "type_name")


# Generated at 2022-06-13 19:36:32.648566
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["deprecated", "since", "1.0"]
    description = "test_deprecated"
    version = "1.0"
    doc = DocstringDeprecated(args, description, version)
    assert doc.args == args
    assert doc.description == description
    assert doc.version == version


# Generated at 2022-06-13 19:36:35.394926
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    raised = DocstringRaises(['raises', 'TypeError'], "test", "TypeError")

    assert raised.args == ['raises', 'TypeError']
    assert raised.description == "test"
    assert raised.type_name == "TypeError"



# Generated at 2022-06-13 19:36:37.324072
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(ValueError) as e:
        raise ParseError("Testing error constructor")
    assert str(e) == "Testing error constructor"

# Generated at 2022-06-13 19:36:40.870520
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    ds = DocstringRaises(['raises'], 'Description', 'ValueError')
    assert ds.type_name == 'ValueError'
    assert ds.description == 'Description'
    assert ds.args == ['raises']



# Generated at 2022-06-13 19:36:43.031704
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    x = DocstringMeta(['a'], '1')
    assert x.args == ['a']
    assert x.description == '1'


# Generated at 2022-06-13 19:36:45.492280
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    if(DocstringMeta([], '') == None):
        print("constructor of class DocstringMeta is test successfully!")


# Generated at 2022-06-13 19:36:51.973093
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam(1,2,3,4,5,6)


# Generated at 2022-06-13 19:36:54.934594
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstring_raises = DocstringRaises(args = [], description = "")
    print(docstring_raises)


# Generated at 2022-06-13 19:37:01.784986
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Created a DocstringReturns object
    docstringReturns = DocstringReturns(RAISES_KEYWORDS, "Description for DocstringRaises", "Invalid Value", False)
    assert docstringReturns.return_name == None
    assert docstringReturns.is_generator == False
    assert docstringReturns.args == {'raises', 'raise', 'except', 'exception'}
    assert docstringReturns.description == "Description for DocstringRaises"


# Generated at 2022-06-13 19:37:03.659723
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(['asda'], 'dasda', 'dasdas')
    assert a.args == ['asda'] and a.description == 'dasda' and a.type_name == 'dasdas'


# Generated at 2022-06-13 19:37:09.744627
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    ds = DocstringReturns(args = [], description = None, type_name = None, is_generator = False)
    ds = DocstringReturns(args = [], description = None, type_name = None, is_generator = False, return_name = None)
    ds = DocstringReturns([], "", "", False)

# Generated at 2022-06-13 19:37:13.674616
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert (docstring.short_description == None)
    assert (docstring.long_description == None)
    assert (docstring.blank_after_short_description == False)
    assert (docstring.blank_after_long_description == False)
    assert (docstring.meta == [])



# Generated at 2022-06-13 19:37:22.517433
# Unit test for constructor of class Docstring
def test_Docstring():
    # Initialize self
    assert Docstring().short_description == None  # type: ignore
    assert Docstring().long_description == None  # type: ignore
    assert Docstring().blank_after_short_description == False  # type: ignore
    assert Docstring().blank_after_long_description == False  # type: ignore
    assert Docstring().meta == []  # type: ignore
    return Docstring()



# Generated at 2022-06-13 19:37:26.529521
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['raises', 'ValueError']
    description = 'if something happens'
    type = 'ValueError'
    assert DocstringRaises(args, description, type) is not None


# Generated at 2022-06-13 19:37:28.576845
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(args="wells", description="", arg_name="wells", type_name="int", is_optional=True, default=0)

# Generated at 2022-06-13 19:37:31.547525
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Unit test for constructor of class DocstringRaises."""
    args = ["args"]
    description = "description"
    type_name = "type_name"
    item = DocstringRaises(args, description, type_name)
    assert item.args == args
    assert item.description == description
    assert item.type_name == type_name

# Generated at 2022-06-13 19:37:42.179002
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Error!")
    except ParseError:
        assert True
    except:
        assert False


# Generated at 2022-06-13 19:37:46.485005
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam(args=["a", "b"],
        description=None,
        arg_name="c",
        type_name=None,
        is_optional=False,
        default=None)
    assert a.args == ['a', 'b']

# Generated at 2022-06-13 19:37:49.895177
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    doc = DocstringRaises(["a", "b", "c"], "Some description", "Type")
    assert doc.args == ["a", "b", "c"]
    assert doc.description == "Some description"
    assert doc.type_name == "Type"


# Generated at 2022-06-13 19:37:58.912629
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta([], '').args == []
    assert DocstringMeta([], '').description == ''
    assert DocstringMeta(['param'], '').args == ['param']
    assert DocstringMeta(['param'], '').description == ''
    assert DocstringMeta([], 'description').args == []
    assert DocstringMeta([], 'description').description == 'description'
    assert DocstringMeta(['param'], 'description').args == ['param']
    assert DocstringMeta(['param'], 'description').description == 'description'
    # Unit test for constructor of class DocstringParam


# Generated at 2022-06-13 19:38:02.672311
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated([], 'description', 'version')
    assert DocstringDeprecated(['args'], 'description', 'version')
    assert DocstringDeprecated(['args'], 'description', None)
    assert DocstringDeprecated(['args'], None, None)


# Generated at 2022-06-13 19:38:03.854025
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """
    assertTrue(isinstance(args, T.List[str]))
    assertTrue(isinstance(description, str))
    """


# Generated at 2022-06-13 19:38:06.239477
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError
    except ParseError:
        print("Test ParseError - OK")
    else:
        print("Test ParseError - FAIL")


# Generated at 2022-06-13 19:38:11.993367
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert doc.meta == []
    assert doc.params == []
    assert doc.raises == []
    assert doc.returns == None
    assert doc.deprecation == None


# Generated at 2022-06-13 19:38:14.577147
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("This is a test error.")
    print(error)

test_ParseError()


# Generated at 2022-06-13 19:38:18.241881
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    name = "test"
    description = "test2"
    args = "test2"
    a = DocstringRaises(args, description, name)
    assert (a.type_name == name)
    assert (a.description == description)
    assert (a.args == args)


# Generated at 2022-06-13 19:38:28.936638
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(['',''],'','') is not None


# Generated at 2022-06-13 19:38:35.051138
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring_deprecated = DocstringDeprecated("args", "description", "version")
    
    assert docstring_deprecated.args == "args"
    assert docstring_deprecated.description == "description"
    assert docstring_deprecated.version == "version"

# Generated at 2022-06-13 19:38:37.767464
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(['arg1'], 'desc', 'version')
    assert d.args == ['arg1']
    assert d.description == 'desc'
    assert d.version == 'version'



# Generated at 2022-06-13 19:38:46.949757
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(["arg", "description"], "description", "arg_name", "type_name", "is_optional", "default")
    assert str(docstring_param.description) == "description"
    assert str(docstring_param.args) == "['arg', 'description']"
    assert str(docstring_param.arg_name) == "arg_name"
    assert str(docstring_param.type_name) == "type_name"
    assert str(docstring_param.is_optional) == "is_optional"


# Generated at 2022-06-13 19:38:52.724922
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["Arg1", "Arg2"]
    description = "description"
    type_name = "type_name"
    d = DocstringRaises(args, description, type_name)
    assert d.args == args
    assert d.description == description
    assert d.type_name == type_name


# Generated at 2022-06-13 19:38:59.181795
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    #Create a docstring
    doc = Docstring()
    assert doc is not None
    #Create an instance of DocstringMeta
    docMet = DocstringMeta(['arg'], 'description')
    assert docMet is not None
    #Check if docMet is an instance of DocstringMeta
    assert isinstance(docMet, DocstringMeta)
    #Check the docMet properties
    assert docMet.args == ['arg']
    assert docMet.description == 'description'
    #Change the properties of docMet
    docMet.args = ['param']
    docMet.description = 'raises'
    #Check if the properties have changed
    assert docMet.args == ['param']
    assert docMet.description == 'raises'


# Generated at 2022-06-13 19:39:03.067278
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(args=["param"], description="desc", arg_name="arg_name", type_name="int", is_optional=False, default="default")
    assert docstring_param.args == ["param"]
    assert docstring_param.description == "desc"
    assert docstring_param.arg_name == "arg_name"
    assert docstring_param.type_name == "int"
    assert docstring_param.is_optional == False
    assert docstring_param.default == "default"


# Generated at 2022-06-13 19:39:05.770730
# Unit test for constructor of class Docstring
def test_Docstring():
    a = Docstring()
    print(type(a.short_description))
    print(type(a.long_description))
    print(type(a.meta))


# Generated at 2022-06-13 19:39:09.453303
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False
    assert d.meta == []


# Generated at 2022-06-13 19:39:11.338936
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    try:
        assert isinstance(DocstringMeta([], ""), DocstringMeta)
    except:
        print("Constructor of class DocstringMeta is not working")


# Generated at 2022-06-13 19:39:29.702656
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError()
    assert error.__class__.__name__ == "ParseError"


# Generated at 2022-06-13 19:39:35.157010
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # Variable names
    args = "args"
    description = "description"
    type_name = "TypeName"
    # Constants
    args_constant = "args_constant"
    description_constant = "description_constant"
    type_name_constant = "TypeName_constant"
    # Constructor for DocstringRaises
    test_docstringRaises = DocstringRaises(args, description, type_name)
    # Test if object is of correct type
    if (isinstance(test_docstringRaises, DocstringRaises)):
        print("DocstringRaises is a DocstringRaises")
    # Test if object has correct values

# Generated at 2022-06-13 19:39:40.146209
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    test = DocstringParam(args=[":param", "arg"], description="description", arg_name="arg", type_name=None, is_optional=None, default=None)
    s = repr(test)
    test_str = "<DocstringParam [':param', 'arg'] description>"
    assert s == test_str, "repr method not working"


# Generated at 2022-06-13 19:39:43.408623
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    parsed = DocstringRaises(["param"],
                             "description",
                             "type_name")
    assert parsed.args == ["param"]
    assert parsed.description == "description"
    assert parsed.type_name == "type_name"


# Generated at 2022-06-13 19:39:44.965601
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = [":raises"]
    description = "An error has been occurred"
    type_name = "RuntimeError"
    obj = DocstringRaises(args, description, type_name)
    print(obj)

# Generated at 2022-06-13 19:39:48.804550
# Unit test for constructor of class DocstringParam

# Generated at 2022-06-13 19:39:53.755381
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = []
    description = 'System error'
    type_name = None
    doc = DocstringRaises(args, description, type_name)
    assert doc.args == []
    assert doc.description == 'System error'
    assert doc.type_name == None

# Generated at 2022-06-13 19:39:58.463475
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Unit test for constructor of class DocstringRaises"""
    assert (
        DocstringRaises(
            args=[":raises", "KeyError"],
            description="Value for the key was not found.",
            type_name="KeyError",
        ).description
        == "Value for the key was not found."
    )



# Generated at 2022-06-13 19:40:04.456606
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated([], '', '')
    b = DocstringDeprecated([], '', '')
    c = DocstringDeprecated([], '', '')
    assert type(a) == type(b)
    assert type(a) == type(c)
    assert type(b) == type(c)

# Generated at 2022-06-13 19:40:09.141941
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d = DocstringRaises(args=[''], description=None, type_name=None)
    assert d.args == ['']
    assert d.description == None
    assert d.type_name == None

# Generated at 2022-06-13 19:40:34.581271
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['any']
    description = 'any'
    arg_name = 'any'
    type_name = 'any'
    is_optional = 'any'
    default = 'any'
    docstring_param = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    if not docstring_param:
        raise ParseError(docstring_param)
    print(docstring_param)


# Generated at 2022-06-13 19:40:36.581724
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    result = DocstringMeta(["param", "k"], "description")
    expected = DocstringMeta(["param", "k"], "description")
    assert result == expected


# Generated at 2022-06-13 19:40:47.215349
# Unit test for constructor of class Docstring
def test_Docstring():
    """Unit test for constructor of class Docstring"""
    test_docstring = Docstring()
    assert isinstance(test_docstring.short_description, type(None))
    assert isinstance(test_docstring.long_description, type(None))
    assert test_docstring.blank_after_short_description == False
    assert test_docstring.blank_after_long_description == False
    assert isinstance(test_docstring.meta, list)
    assert test_docstring.meta == []
    assert isinstance(test_docstring.params, list)
    assert isinstance(test_docstring.raises, list)
    assert isinstance(test_docstring.returns, type(None))
    assert isinstance(test_docstring.deprecation, type(None))

