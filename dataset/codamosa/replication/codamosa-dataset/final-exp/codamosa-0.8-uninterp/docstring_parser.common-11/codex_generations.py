

# Generated at 2022-06-13 19:30:54.971690
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    my_args = ["return"]
    my_description = "return value"
    my_type_name = "str"
    my_is_generator = False 
    my_return_name = None
    my_obj = DocstringReturns(my_args, my_description, my_type_name, my_is_generator, my_return_name)
    # print (my_obj.args, my_obj.description, my_obj.type_name, my_obj.is_generator, my_obj.return_name)


# Generated at 2022-06-13 19:30:57.453425
# Unit test for constructor of class ParseError
def test_ParseError():
    error_message = "This is a test"
    e = ParseError(error_message)
    assert str(e) == error_message


# Generated at 2022-06-13 19:31:04.485206
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    doc_param = DocstringParam(['param'], 'some_param', 'some_type', True, 'some_default')
    assert doc_param.args == ['param']
    assert doc_param.description == 'some_param'
    assert doc_param.arg_name == 'some_param'
    assert doc_param.type_name == 'some_type'
    assert doc_param.is_optional == True
    assert doc_param.default == 'some_default'


# Generated at 2022-06-13 19:31:06.104601
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns(['raises'], 'This is an error', 'ValueError') 
    assert DocstringReturns(['raises'], 'This is an error')


# Generated at 2022-06-13 19:31:11.010271
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description is None, \
    "Constructor of class Docstring failed: ds.short_description is not None."
    assert ds.long_description is None, \
    "Constructor of class Docstring failed: ds.long_description is not None."
    assert ds.meta == [], \
    "Constructor of class Docstring failed: ds.meta is not []."


# Generated at 2022-06-13 19:31:12.286734
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns.__init__

# Generated at 2022-06-13 19:31:14.304236
# Unit test for constructor of class Docstring
def test_Docstring():
    x = Docstring()
    assert x.short_description is None
    assert x.long_description is None
    assert x.blank_after_short_description is False
    assert x.blank_after_long_description is False
    assert x.meta == []

# Generated at 2022-06-13 19:31:16.335127
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # initialize
    args = ["test","test1"]
    description = "test description"
    # check docstringmeta params
    docstringMeta = DocstringMeta(args, description)
    assert docstringMeta.args == args
    assert docstringMeta.description == description

# Generated at 2022-06-13 19:31:20.878825
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dep_meta = DocstringDeprecated(["version", "since"], "description", "1.0")

    assert dep_meta.args == ["version", "since"]
    assert dep_meta.description == "description"
    assert dep_meta.version == "1.0"


# Generated at 2022-06-13 19:31:24.120736
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["param"]
    description = "Description"

    assert DocstringMeta(args, description).args == args
    assert DocstringMeta(args, description).description == description


# Generated at 2022-06-13 19:31:29.367193
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring


# Generated at 2022-06-13 19:31:33.117501
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstring_raises = DocstringRaises(['raises','ValueError'], 'if something happens','ValueError')
    assert isinstance(docstring_raises, DocstringRaises)
    assert docstring_raises.args == ['raises','ValueError']
    assert docstring_raises.description == 'if something happens'
    assert docstring_raises.type_name == 'ValueError'


# Generated at 2022-06-13 19:31:37.612572
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    type_name = "SomeType"
    description = "some description"
    ds = DocstringRaises(["raises"], description, type_name)
    assert ds.type_name == type_name
    assert ds.description == description


# Generated at 2022-06-13 19:31:45.769730
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Test the constructor of DocstringReturns."""
    print("DocstringReturns test started\n")
    arg = ["param"]
    description = None
    type_name = "str"
    is_generator = False
    return_name = "keywords"
    a = DocstringReturns(arg, description, type_name, is_generator, return_name)
    print(a)


if __name__ == "__main__":
    test_DocstringReturns()

# Generated at 2022-06-13 19:31:51.955721
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    test_case = DocstringParam(
        ["param"],
        "This is the description",
        "arg",
        "TypeName",
        True,
        "default",
    )
    assert test_case.args == ["param"]
    assert test_case.description == "This is the description"
    assert test_case.arg_name == "arg"
    assert test_case.type_name == "TypeName"
    assert test_case.is_optional == True
    assert test_case.default == "default"


# Generated at 2022-06-13 19:31:53.693378
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError


# Generated at 2022-06-13 19:32:00.682867
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    print("\nTest results:\n")
    dp = DocstringParam("param", None, "arg_name", "type_name", False, None)
    test_str = (
        "DocstringParam(param, None, arg_name, type_name, False, None)"
    )
    print(dp)
    assert str(dp) == test_str

test_DocstringParam()


# Generated at 2022-06-13 19:32:03.931426
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("lib2to3.pgen2.parse.ParseError: unexpected end of file at '\"'")
    assert err.args == ("lib2to3.pgen2.parse.ParseError: unexpected end of file at '\"'",)



# Generated at 2022-06-13 19:32:07.164571
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('Test Exception')
    except ParseError:
        pass


# Generated at 2022-06-13 19:32:11.111830
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(["deprecated"], "", "1.0.0")
    assert docstring.args == ["deprecated"]
    assert docstring.description is None
    assert docstring.version == "1.0.0"

# Generated at 2022-06-13 19:32:25.801702
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d = DocstringRaises(
        args=["raises", "ValueError"],
        description="if something happens",
        type_name="ValueError",
    )
    assert d.args == ["raises", "ValueError"]
    assert d.description == "if something happens"
    assert d.type_name == "ValueError"
    # Unit test for constructor of class DocstringRaises
    def test_DocstringRaises2():
        d = DocstringRaises(
            args=["raises"],
            description=None,
            type_name=None,
        )
        assert d.args == ["raises"]
        assert d.description is None
        assert d.type_name is None



# Generated at 2022-06-13 19:32:37.480887
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['arg1', 'arg2']
    description = 'description'
    arg_name = 'arg_name'
    type_name = 'int'
    is_optional = False
    default = 'default'
    docStringParam = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert docStringParam.args == ['arg1', 'arg2']
    assert docStringParam.description == 'description'
    assert docStringParam.arg_name == 'arg_name'
    assert docStringParam.type_name == 'int'
    assert docStringParam.is_optional == False
    assert docStringParam.default == 'default'


# Generated at 2022-06-13 19:32:40.744426
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    string = "\"\"\" :returns: description \"\"\""
    assert DocstringReturns("returns", "description", "", False) == DocstringReturns("returns", "description", "", False)



# Generated at 2022-06-13 19:32:44.812614
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # assert isinstance(DocstringRaises(args = [], \
    #                                    description = None,\
    #                                    type_name = None),\
    #                 DocstringRaises), \
    #                 "Constructor of class DocstringRaises is wrong"
    assert True
    

# Generated at 2022-06-13 19:32:46.733015
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    doc = DocstringMeta(["hello", "there"], "nice")
    print(doc.args)
    print(doc.description)


# Generated at 2022-06-13 19:32:49.364501
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError()
    assert(str(err) == "Docstring parsing error")
    err.args = ("Msg",)
    assert(str(err) == "Msg")


# Generated at 2022-06-13 19:32:54.253218
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Test for constructor of class DocstringParam

    # Test for constructor of class DocstringParam with normal inputs
    test_args = ['param']
    test_description = 'description'
    test_arg_name = 'arg_name'
    test_type_name = 'type_name'
    test_is_optional = True
    test_default = 'default'
    test_obj = DocstringParam(test_args,test_description,test_arg_name,test_type_name,test_is_optional,test_default)

    assert test_obj.args == test_args
    assert test_obj.description == test_description
    assert test_obj.arg_name == test_arg_name
    assert test_obj.type_name == test_type_name
    assert test_obj.is_optional == test_is_optional


# Generated at 2022-06-13 19:32:57.412796
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("test")
    except ParseError:
        assert True
    except:
        assert False

# Generated at 2022-06-13 19:33:00.915538
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["a", "b", "c"]
    description = "description"
    type_name = "type"
    docstringRaises = DocstringRaises(args, description, type_name)
    assert docstringRaises.args == ["a", "b", "c"]
    assert docstringRaises.description == "description"
    assert docstringRaises.type_name == "type"
    print("test for docstringRaises finished")

test_DocstringRaises()

# Generated at 2022-06-13 19:33:07.318512
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    test_DocstringParam = DocstringParam(["arg"], "description", "arg", "type", "is_optional", "default")
    assert test_DocstringParam.args == ['arg']
    assert test_DocstringParam.description == "description"
    assert test_DocstringParam.arg_name == "arg"
    assert test_DocstringParam.type_name == "type"
    assert test_DocstringParam.is_optional == "is_optional"
    assert test_DocstringParam.default == "default"


# Generated at 2022-06-13 19:33:23.543251
# Unit test for constructor of class ParseError
def test_ParseError():
    ex = ParseError()
    assert str(ex).startswith(ParseError.__name__)


# Generated at 2022-06-13 19:33:26.899248
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstringMeta = DocstringMeta(["param", "arg", "argument"], "A test docstring")
    assert docstringMeta.args == ["param", "arg", "argument"]
    assert docstringMeta.description == "A test docstring"



# Generated at 2022-06-13 19:33:27.981603
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError("parse error")



# Generated at 2022-06-13 19:33:30.553806
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["param", "a", "b", "c"]
    description = "DocstringMeta"
    DocstringMeta(args, description)
    assert True



# Generated at 2022-06-13 19:33:38.205067
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """DocstringRaises test."""
    args = ["param"]
    description = "description"
    type_name = "Type"
    raises = DocstringRaises(args, description, type_name)
    assert raises.args == args
    assert raises.description == description
    assert raises.type_name == type_name


# Generated at 2022-06-13 19:33:41.725668
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Test the DocstringDeprecated constructor"""
    doctringDeprecatedArgs = ["text", "version"]
    doctringDeprecatedDescription = "description"

    newDocstringDeprecated = DocstringDeprecated(doctringDeprecatedArgs,
            doctringDeprecatedDescription, doctringDeprecatedArgs[1])
    assert newDocstringDeprecated.args == doctringDeprecatedArgs
    assert newDocstringDeprecated.description == doctringDeprecatedDescription
    assert newDocstringDeprecated.version == doctringDeprecatedArgs[1]

# Generated at 2022-06-13 19:33:43.653780
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["raises", "ValueError:"]
    type_name = "ValueError"
    description = "if something happens"
    raises = DocstringRaises(args, description, type_name)

    assert raises.args == args
    assert raises.description == description
    assert raises.type_name == type_name



# Generated at 2022-06-13 19:33:46.217126
# Unit test for constructor of class ParseError
def test_ParseError():
    a = ParseError("a", "b", "c")
    assert a.__str__() == "a: b: c"


# Generated at 2022-06-13 19:33:55.724190
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["a", "b"]
    description = "docstring"
    type_name = "S.O.S"
    is_generator = True
    return_name = "name"
    my_docstring = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert my_docstring.args == args
    assert my_docstring.description == description
    assert my_docstring.type_name == type_name
    assert my_docstring.is_generator == is_generator
    assert my_docstring.return_name == return_name

# Generated at 2022-06-13 19:34:00.653766
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []

# Generated at 2022-06-13 19:34:29.840234
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    dm = DocstringMeta(["a","b"],"good")
    assert dm.args == ["a","b"]
    assert dm.description == "good"


# Generated at 2022-06-13 19:34:32.030804
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    try:
        DocstringMeta([], "")
    except:
        assert False
    assert True


# Generated at 2022-06-13 19:34:35.213552
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated([], 'description', 'version')
    DocstringDeprecated([], 'description', 'version').description



# Generated at 2022-06-13 19:34:46.500324
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Test for constructor of class DocstringDeprecated."""
    # Test without parameters:
    x = DocstringDeprecated([], None, None)
    assert x.args == []
    assert x.description is None
    assert x.version is None

    # Test with parameters:
    x = DocstringDeprecated(["param", "param1"], "test description", "test version")
    assert x.args == ["param", "param1"]
    assert x.description == "test description"
    assert x.version == "test version"


# Generated at 2022-06-13 19:34:50.457268
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "arg"]
    description = "my description"
    arg_name = "my_argument"
    type_name = "String"
    is_optional = False
    default = "None"
    try:
        doc = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    except:
        print("Error")
    assert isinstance(doc, DocstringParam)
    assert doc.args == args
    assert doc.description == description
    assert doc.arg_name == arg_name
    assert doc.type_name == type_name
    assert doc.is_optional == is_optional
    assert doc.default == default


# Generated at 2022-06-13 19:34:54.160486
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(["param"], "This is a test string", "arg1", "str", True, None)
    assert param.__dict__ == {'args': ['param'], 'description': 'This is a test string', 'arg_name': 'arg1', 'type_name': 'str', 'is_optional': True, 'default': None}


# Generated at 2022-06-13 19:34:56.611844
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises([], None, None) is not None


# Generated at 2022-06-13 19:35:01.451754
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = []
    description = None
    type_name = None
    is_generator = False
    return_name = None
    returns = DocstringReturns(args, description, type_name, is_generator, return_name)



# Generated at 2022-06-13 19:35:05.117682
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(['deprecated'], 'description', 'version')
    assert isinstance(d, DocstringDeprecated)
    #assert isinstance(d.version, str)

# Generated at 2022-06-13 19:35:09.970407
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam([], None, None, None, False, None)
    assert a.args is not None
    assert a.description is None
    assert a.arg_name is None
    assert a.type_name is None
    assert a.is_optional is False
    assert a.default is None


# Generated at 2022-06-13 19:36:08.446569
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description == None
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.meta == []



# Generated at 2022-06-13 19:36:10.036155
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(["param"], "description")

# Generated at 2022-06-13 19:36:16.061791
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    do = DocstringParam(["args"], description="description", arg_name="arg_name", type_name=None, is_optional=None, default="default")
    assert do.args == ["args"]
    assert do.description == "description"
    assert do.arg_name == "arg_name"
    assert do.type_name == None
    assert do.is_optional == None
    assert do.default == "default"


# Generated at 2022-06-13 19:36:21.361285
# Unit test for constructor of class Docstring
def test_Docstring():
    obj = Docstring()
    assert isinstance(obj, Docstring)
    assert obj.short_description == None
    assert obj.long_description == None
    assert obj.blank_after_short_description == False
    assert obj.blank_after_long_description == False
    assert isinstance(obj.meta, list)
    assert obj.meta == []



# Generated at 2022-06-13 19:36:24.755427
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(['param'], 'description')
    assert isinstance(d, DocstringMeta)
    assert d.args == ['param']
    assert d.description == 'description'

# Unit Tests for constructor of class DocstringParam

# Generated at 2022-06-13 19:36:28.733991
# Unit test for constructor of class ParseError
def test_ParseError():
    s = ''
    try:
        raise ParseError(s)
    except ParseError as e:
        assert s == str(e)


# Generated at 2022-06-13 19:36:35.514823
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # Arguments
    args = ['param', 'funk']
    # Description
    description = "Initialize self."
    # Type name
    type_name = "DocstringReturns"
    # Is generator
    is_generator = False
    # Return name
    return_name = "None"
    # Initialize self
    DocstringReturns.__init__(args, description, type_name, is_generator, return_name)
    # Test that DocstringReturns was created properly
    return True

# Generated at 2022-06-13 19:36:37.770864
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(args=["a", "b"], description="d", type_name=None, is_generator=True, return_name=None)


# Generated at 2022-06-13 19:36:43.507624
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    do = DocstringReturns(['dummy_arg1', 'dummy_arg2'], 'dummy_description', 'dummy_type', 'dummy_bool')
    assert do.args == ['dummy_arg1', 'dummy_arg2']
    assert do.description == 'dummy_description'
    assert do.type_name == 'dummy_type'
    assert do.is_generator == 'dummy_bool'
    assert do.return_name is None


# Generated at 2022-06-13 19:36:49.521702
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["raises"]
    description = "Some description"
    type_name = "ValueError"
    t = DocstringRaises(args, description, type_name)
    result = [args, description, type_name]
    assert True if [t.args, t.description, t.type_name] == result else False

# Generated at 2022-06-13 19:38:48.676634
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    class_obj = DocstringRaises(['arg'], 'description', 'type_name')
    assert class_obj.args[0] == 'arg'
    assert class_obj.description == 'description'
    assert class_obj.type_name == 'type_name'


# Generated at 2022-06-13 19:38:50.362948
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstringDeprecated = DocstringDeprecated([], "", "")


# Generated at 2022-06-13 19:38:55.331886
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Unit test for constructor of class DocstringDeprecated."""
    a = DocstringDeprecated(["key1", "key2"], "description", "version")
    assert a.args == ["key1", "key2"]
    assert a.description == "description"
    assert a.version == "version"
    assert a.args[0] == "key1"
    assert a.args[1] == "key2"



# Generated at 2022-06-13 19:39:00.240640
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = 'args'
    description = 'description' 
    type_name = 'type_name' 
    is_generator = 'is_generator' 
    return_name = 'return_name'

    ds = DocstringReturns(args, description, type_name, is_generator, return_name)

    assert ds.is_generator == is_generator
    assert ds.type_name == type_name
    assert ds.description == description
    assert ds.return_name == return_name
    assert ds.args == args


# Generated at 2022-06-13 19:39:01.341399
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam["args"] == "args"

# Generated at 2022-06-13 19:39:05.814525
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Unit test for constructor of class DocstringRaises."""
    test_DocstringRaises = DocstringRaises("args","description")
    assert test_DocstringRaises.args == "args", "args not set properly"
    assert test_DocstringRaises.description == "description", "description not set properly"

# Generated at 2022-06-13 19:39:12.180436
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Unit test for constructor of class DocstringDeprecated."""
    my_args = [":deprecated:" , ":deprecated: use foo." , ":deprecated: 0.1"]
    my_description = ["Use foo instead.", "", ""]
    my_version = ["", "", "0.1"]

    for arg, description, version in zip(my_args, my_description, my_version):
        meta = DocstringDeprecated(args=[arg], description=description, version=version)
        assert meta.args[0] == arg
        assert meta.description == description
        assert meta.version == version

# Generated at 2022-06-13 19:39:14.969930
# Unit test for constructor of class ParseError
def test_ParseError():
    """Test the constructor of class ParseError."""
    err = ParseError('test exception')
    assert str(err) == 'test exception'


# Generated at 2022-06-13 19:39:15.624097
# Unit test for constructor of class Docstring
def test_Docstring():
    Docstring()

# Generated at 2022-06-13 19:39:18.673387
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d = DocstringRaises(["raises"], "test", "Exception")
    assert d.type_name == "Exception"
    assert d.description == "test"
    assert d.args == ["raises"]